# Audio Reactive Remotion

Use this reference when the video includes music, voiceover, beat sync, waveforms, or spectrum visuals.

## Basic Approach

1. Import audio with `staticFile()` and render it with `<Audio />`.
2. Use `@remotion/media-utils` for audio analysis when the project includes it.
3. Align important visual beats to measured or user-specified timestamps.
4. Keep all visual response frame-driven and deterministic.

## Beat Sync

Represent beat points as seconds and convert to frames:

```ts
const beat = (seconds: number) => Math.round(seconds * fps);
const logoHit = beat(4.2);
```

Use beats for scene cuts, burst timing, major scale changes, and text landings. Avoid making every minor detail hit the beat; contrast creates impact.

## Spectrum and Waveform Patterns

- Bars: scale Y from analyzed amplitude, clamp minimum height for visibility.
- Waveform: draw an SVG polyline or path from sampled values.
- Bass pulse: apply subtle scale or glow to primary elements.
- Vocal focus: reduce background movement during spoken phrases.

## Restraint

Audio-reactive visuals should support the edit, not fight it. Smooth raw values, limit extreme scale changes, and keep text readable during loud sections.
