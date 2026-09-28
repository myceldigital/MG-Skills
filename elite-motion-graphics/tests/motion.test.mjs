import test from 'node:test';
import assert from 'node:assert/strict';
import { springStep, springTrack, periodicPhase, noise01, smoothstep5, exposureTimes } from '../scripts/motion.mjs';

const near = (a, b, tolerance = 1e-8) => assert.ok(Math.abs(a - b) <= tolerance, `${a} != ${b}`);

test('spring initial conditions and limiting value across damping regimes', () => {
  for (const damping of [5, 20, 50]) {
    const config = { stiffness: 100, damping, mass: 1 };
    assert.equal(springStep(-1, config), 0);
    assert.equal(springStep(0, config), 0);
    near(springStep(1e-7, config) / 1e-7, 0, 1e-5);
    near(springStep(30, config), 1);
  }
});

test('all damping regimes satisfy the physical ODE independently of the formula', () => {
  const h = 1e-4;
  for (const damping of [0, 5, 20, 50]) {
    const config = { stiffness: 100, damping, mass: 1 };
    for (const t of [0.05, 0.2, 0.7, 1.3]) {
      const x = springStep(t, config);
      const before = springStep(t - h, config);
      const after = springStep(t + h, config);
      const velocity = (after - before) / (2 * h);
      const acceleration = (after - 2 * x + before) / (h * h);
      near(acceleration + damping * velocity + 100 * x, 100, 0.0001);
    }
  }
});

test('critical and overdamped motion is monotone; underdamped can overshoot', () => {
  for (const damping of [20, 50]) {
    let previous = 0;
    for (let i = 0; i < 1000; i++) {
      const value = springStep(i / 100, { stiffness: 100, damping });
      assert.ok(value >= previous - 1e-12 && value <= 1 + 1e-12);
      previous = value;
    }
  }
  assert.ok(springStep(0.35, { stiffness: 100, damping: 5 }) > 1);
  assert.ok(springStep(0.2, { stiffness: 100, damping: 50 }) < springStep(0.2, { stiffness: 100, damping: 20 }));
});

test('near-critical response and mass scaling are continuous', () => {
  const expected = 1 - Math.exp(-2) * 3;
  for (const damping of [19.99999, 20, 20.00001]) {
    near(springStep(0.2, { stiffness: 100, damping }), expected, 1e-6);
  }
  near(springStep(0.7, { stiffness: 100, damping: 15, mass: 2 }),
    springStep(0.7, { stiffness: 200, damping: 30, mass: 4 }));
});

test('retargeting preserves position and velocity at a target change', () => {
  const keys = [[0, 10], [0.3, 40], [0.45, -20]];
  const h = 1e-6;
  const at = springTrack(0.45, keys);
  near(at, springTrack(0.45, keys.slice(0, 2)));
  const leftVelocity = (at - springTrack(0.45 - h, keys)) / h;
  const rightVelocity = (springTrack(0.45 + h, keys) - at) / h;
  near(leftVelocity, rightVelocity, 0.02);
  near(springTrack(30, keys), -20);
});

test('tracks and indexed noise are independent of seek order', () => {
  const keys = [[0, 0], [0.2, 100], [0.4, 20]];
  const times = [0.1, 0.7, 0.4, 2, -1];
  const values = new Map(times.map(t => [t, springTrack(t, keys)]));
  for (const t of [...times].reverse()) assert.equal(springTrack(t, keys), values.get(t));
  const noise = Array.from({ length: 100 }, (_, i) => noise01(19, i));
  for (let i = 99; i >= 0; i--) {
    assert.equal(noise01(19, i), noise[i]);
    assert.ok(noise[i] >= 0 && noise[i] < 1);
  }
});

test('periodic phase wraps negative time but does not imply arbitrary track continuity', () => {
  near(periodicPhase(-0.25, 1), 0.75);
  near(periodicPhase(4, 4), 0);
  const periodic = t => Math.sin(2 * Math.PI * periodicPhase(t, 4));
  near(periodic(0), periodic(4));
  const h = 1e-4;
  near((periodic(h) - periodic(-h)) / (2 * h),
    (periodic(4 + h) - periodic(4 - h)) / (2 * h));
});

test('quintic easing has bounded endpoints and zero endpoint velocity', () => {
  assert.equal(smoothstep5(-2), 0);
  assert.equal(smoothstep5(2), 1);
  near(smoothstep5(0.5), 0.5);
  near(smoothstep5(1e-5) / 1e-5, 0, 1e-7);
  near((1 - smoothstep5(1 - 1e-5)) / 1e-5, 0, 1e-7);
});

test('exposure samples are centered, inside the shutter, and frame-local', () => {
  for (const samples of [1, 4, 8]) {
    const times = exposureTimes(12, 30, samples, 0.5);
    near(times.reduce((a, b) => a + b, 0) / samples, 12.5 / 30);
    assert.ok(times.every(t => t >= 12.25 / 30 && t <= 12.75 / 30));
  }
});

test('invalid parameters fail explicitly', () => {
  assert.throws(() => springStep(NaN));
  assert.throws(() => springStep(1, { mass: 0 }));
  assert.throws(() => springStep(1, { damping: -1 }));
  assert.throws(() => springTrack(1, []));
  assert.throws(() => springTrack(1, [[0, 1], [0, 2]]));
  assert.throws(() => periodicPhase(1, 0));
  assert.throws(() => noise01(1, 0.5));
  assert.throws(() => exposureTimes(0, 0));
  assert.throws(() => exposureTimes(0, 30, 4, 2));
});
