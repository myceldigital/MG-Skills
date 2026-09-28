function finite(value, name) {
  if (!Number.isFinite(value)) throw new TypeError(`${name} must be finite`);
}

export function clamp01(value) {
  finite(value, 'value');
  return Math.max(0, Math.min(1, value));
}

// Unit step response of m*x'' + damping*x' + stiffness*x = stiffness,
// with zero displacement and velocity at t=0.
export function springStep(t, { stiffness = 170, damping = 26, mass = 1 } = {}) {
  for (const [name, value] of Object.entries({ t, stiffness, damping, mass })) {
    finite(value, name);
  }
  if (stiffness <= 0 || mass <= 0 || damping < 0) {
    throw new RangeError('Require positive stiffness/mass and nonnegative damping');
  }
  if (t <= 0) return 0;
  const w0 = Math.sqrt(stiffness / mass);
  const z = damping / (2 * Math.sqrt(stiffness * mass));
  if (Math.abs(z - 1) < 1e-7) {
    return 1 - Math.exp(-w0 * t) * (1 + w0 * t);
  }
  if (z < 1) {
    const wd = w0 * Math.sqrt(1 - z * z);
    return 1 - Math.exp(-z * w0 * t) *
      (Math.cos(wd * t) + z * w0 / wd * Math.sin(wd * t));
  }
  const root = Math.sqrt(z * z - 1);
  // The reciprocal form avoids cancellation in the slow root for high damping.
  const r1 = -w0 / (z + root);
  const r2 = -w0 * (z + root);
  return 1 - (r2 * Math.exp(r1 * t) - r1 * Math.exp(r2 * t)) / (r2 - r1);
}

export function springTrack(t, keys, config) {
  finite(t, 't');
  if (!Array.isArray(keys) || keys.length === 0) {
    throw new TypeError('keys must be a nonempty array of [time, target] pairs');
  }
  keys.forEach((key, index) => {
    if (!Array.isArray(key) || key.length !== 2) throw new TypeError('Invalid key');
    finite(key[0], 'key time');
    finite(key[1], 'key target');
    if (index && key[0] <= keys[index - 1][0]) {
      throw new RangeError('Key times must be strictly increasing');
    }
  });
  springStep(0, config);
  let value = keys[0][1];
  for (let i = 1; i < keys.length; i++) {
    value += (keys[i][1] - keys[i - 1][1]) * springStep(t - keys[i][0], config);
  }
  return value;
}

export function smoothstep5(t) {
  const u = clamp01(t);
  return u * u * u * (u * (6 * u - 15) + 10);
}

export function periodicPhase(t, duration) {
  finite(t, 't');
  finite(duration, 'duration');
  if (duration <= 0) throw new RangeError('duration must be positive');
  return ((t % duration) + duration) % duration / duration;
}

// Stateless indexed noise: call order does not change an object's value.
export function noise01(seed, index) {
  if (!Number.isSafeInteger(seed) || !Number.isSafeInteger(index)) {
    throw new TypeError('seed and index must be safe integers');
  }
  let x = (seed ^ Math.imul(index, 0x9e3779b1)) >>> 0;
  x ^= x >>> 16;
  x = Math.imul(x, 0x7feb352d);
  x ^= x >>> 15;
  x = Math.imul(x, 0x846ca68b);
  x ^= x >>> 16;
  return (x >>> 0) / 4294967296;
}

export function exposureTimes(frame, fps, samples = 1, shutter = 0.5) {
  if (!Number.isSafeInteger(frame) || frame < 0 ||
      !Number.isSafeInteger(samples) || samples < 1) {
    throw new RangeError('frame must be nonnegative and samples must be positive integers');
  }
  finite(fps, 'fps');
  finite(shutter, 'shutter');
  if (fps <= 0 || shutter < 0 || shutter > 1) {
    throw new RangeError('Require positive fps and shutter between 0 and 1');
  }
  const center = (frame + 0.5) / fps;
  return Array.from({ length: samples }, (_, j) =>
    center + shutter / fps * ((j + 0.5) / samples - 0.5));
}
