import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile, writeFile, mkdir, realpath } from 'node:fs/promises';
import { dirname, resolve, relative, extname, sep } from 'node:path';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { exposureTimes } from './motion.mjs';

const execute = promisify(execFile);
const [input, destination, ...flags] = process.argv.slice(2);
const settings = { fps: 30, frames: 120, width: 640, height: 360, samples: 1 };
if (!input || !destination || flags.length % 2) {
  throw new Error('Usage: node render.mjs scene.html NEW_OUTPUT_DIR [--fps 30 --frames 120 --width 640 --height 360 --samples 1]');
}
for (let i = 0; i < flags.length; i += 2) {
  const key = flags[i].slice(2);
  const value = Number(flags[i + 1]);
  if (!flags[i].startsWith('--') || !Object.hasOwn(settings, key) ||
      !Number.isSafeInteger(value) || value <= 0) {
    throw new Error(`Invalid option ${flags[i]}`);
  }
  settings[key] = value;
}
if (settings.width % 2 || settings.height % 2) throw new Error('H.264 yuv420p requires even dimensions');
const inputPath = await realpath(resolve(input));
const root = dirname(inputPath);
const out = resolve(destination);
const duration = settings.frames / settings.fps;
const mime = { '.html': 'text/html', '.mjs': 'text/javascript', '.js': 'text/javascript', '.css': 'text/css', '.png': 'image/png', '.woff2': 'font/woff2' };
await execute('ffmpeg', ['-version']);
await execute('ffprobe', ['-version']);
await mkdir(dirname(out), { recursive: true });
await mkdir(out);
const framesDir = resolve(out, 'frames');
await mkdir(framesDir);

const server = createServer(async (request, response) => {
  try {
    const url = new URL(request.url, 'http://localhost');
    const file = await realpath(resolve(root, '.' + decodeURIComponent(url.pathname)));
    const pathFromRoot = relative(root, file);
    if (pathFromRoot === '..' || pathFromRoot.startsWith('..' + sep) || pathFromRoot.startsWith(sep)) {
      response.writeHead(403).end();
      return;
    }
    const bytes = await readFile(file);
    response.writeHead(200, { 'Content-Type': mime[extname(file)] || 'application/octet-stream' });
    response.end(bytes);
  } catch {
    response.writeHead(404).end();
  }
});
await new Promise((ok, fail) => {
  server.once('error', fail);
  server.listen(0, '127.0.0.1', ok);
});
let browser;
try {
  const origin = `http://127.0.0.1:${server.address().port}`;
  const url = new URL(encodeURIComponent(relative(root, inputPath)), origin + '/');
  url.searchParams.set('width', settings.width);
  url.searchParams.set('height', settings.height);
  url.searchParams.set('mode', 'render');
  browser = await chromium.launch({ executablePath: process.env.MOTION_CHROMIUM_EXECUTABLE_PATH });
  const context = await browser.newContext({
    viewport: { width: settings.width, height: settings.height },
    deviceScaleFactor: 1, locale: 'en-US', timezoneId: 'UTC', colorScheme: 'light',
    serviceWorkers: 'block',
  });
  const errors = [];
  await context.route('**/*', async route => {
    if (new URL(route.request().url()).origin === origin) await route.continue();
    else {
      errors.push('Blocked nonlocal browser request');
      await route.abort();
    }
  });
  async function openScene() {
    const page = await context.newPage();
    page.on('pageerror', error => errors.push(error.message));
    page.on('response', response => {
      if (response.status() >= 400) errors.push(`Asset request failed: HTTP ${response.status()}`);
    });
    page.on('requestfailed', () => errors.push('Scene request failed'));
    await page.goto(url.href, { waitUntil: 'load', timeout: 30000 });
    await page.waitForFunction(() => window.ready && typeof window.seek === 'function', { }, { timeout: 30000 });
    await page.evaluate(() => {
      Promise.resolve(window.ready).then(
        () => { window.__captureReady = true; },
        error => { window.__captureFailure = String(error); },
      );
    });
    await page.waitForFunction(() => window.__captureReady || window.__captureFailure, { }, { timeout: 30000 });
    const failure = await page.evaluate(() => window.__captureFailure);
    if (failure) throw new Error(`Scene readiness failed: ${failure}`);
    const dimensions = await page.locator('canvas').evaluate(c => [c.width, c.height]);
    if (dimensions[0] !== settings.width || dimensions[1] !== settings.height) {
      throw new Error('Scene dimensions do not match the requested output');
    }
    return page;
  }
  function assertSceneHealthy() {
    if (errors.length) throw new Error(`Scene failed: ${errors.join('; ')}`);
  }
  async function pixelHash(page, time) {
    return page.evaluate(async t => {
      await window.seek(t);
      const canvas = document.querySelector('canvas');
      const pixels = canvas.getContext('2d').getImageData(0, 0, canvas.width, canvas.height).data;
      const digest = await crypto.subtle.digest('SHA-256', pixels);
      return Array.from(new Uint8Array(digest), x => x.toString(16).padStart(2, '0')).join('');
    }, time);
  }
  const page = await openScene();
  const checkTimes = [0, duration * 0.37, (settings.frames - 0.5) / settings.fps];
  const checks = [];
  for (const time of checkTimes) {
    const first = await pixelHash(page, time);
    await pixelHash(page, duration * 0.83);
    if (first !== await pixelHash(page, time)) throw new Error(`History-dependent scene at ${time}`);
    checks.push({ time, pixelHash: first });
  }
  const fresh = await openScene();
  for (const check of [...checks].reverse()) {
    if (check.pixelHash !== await pixelHash(fresh, check.time)) {
      throw new Error(`Fresh-page pixel mismatch at ${check.time}`);
    }
  }
  await fresh.close();
  assertSceneHealthy();
  for (let frame = 0; frame < settings.frames; frame++) {
    const times = exposureTimes(frame, settings.fps, settings.samples, 0.5);
    await page.evaluate(async sampleTimes => {
      if (sampleTimes.length > 1) {
        if (typeof window.renderSamples !== 'function') throw new Error('Scene does not support temporal sampling');
        await window.renderSamples(sampleTimes);
      } else await window.seek(sampleTimes[0]);
    }, times);
    assertSceneHealthy();
    await page.locator('canvas').screenshot({
      path: resolve(framesDir, `${String(frame).padStart(6, '0')}.png`),
      type: 'png', scale: 'css', animations: 'allow',
    });
    if (frame % settings.fps === 0) process.stdout.write(`Captured ${frame}/${settings.frames}\n`);
  }
  assertSceneHealthy();
  const video = resolve(out, 'silent.mp4');
  await execute('ffmpeg', ['-v', 'error', '-n', '-framerate', String(settings.fps),
    '-i', resolve(framesDir, '%06d.png'), '-frames:v', String(settings.frames),
    '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', video]);
  const probe = JSON.parse((await execute('ffprobe', ['-v', 'error', '-count_frames',
    '-show_streams', '-show_format', '-of', 'json', video])).stdout);
  const stream = probe.streams.find(item => item.codec_type === 'video');
  const [rateN, rateD] = stream.avg_frame_rate.split('/').map(Number);
  if (Number(stream.nb_read_frames) !== settings.frames || stream.width !== settings.width ||
      stream.height !== settings.height || Math.abs(rateN / rateD - settings.fps) > 1e-8 ||
      Math.abs(Number(stream.duration) - duration) > 1 / settings.fps) {
    throw new Error('Encoded video failed frame/dimension/rate/duration validation');
  }
  await execute('ffmpeg', ['-v', 'error', '-xerror', '-i', video, '-f', 'null', '-']);
  await writeFile(resolve(out, 'manifest.json'), JSON.stringify({
    settings, duration, shutter: 0.5, frameTime: 'midpoint',
    node: process.version, chromium: browser.version(),
    determinism: { scope: 'same runtime, out-of-order and fresh-page raw pixel hashes', checks },
    verification: { encodedFrames: Number(stream.nb_read_frames), decode: 'passed', audio: 'intentionally absent', visualReview: 'not performed by this script' },
  }, null, 2) + '\n');
  process.stdout.write(`Verified ${video}\n`);
} finally {
  await browser?.close();
  await new Promise(resolveClose => server.close(resolveClose));
}
