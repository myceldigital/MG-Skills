# Remotion Motion Workflow

Use this reference when planning a video before writing Remotion code.

## Storyboard Pass

Define the video in four layers:

- Objective: what the viewer should understand or feel by the final frame.
- Duration and format: seconds, fps, aspect ratio, platform, and any safe areas.
- Narrative arc: setup, anticipation, reveal or payoff, settle.
- Visual hierarchy: background, primary subject, secondary reaction, micro-detail.

Convert every beat to frames with `const seconds = fps * n` or a named helper. Keep timing values named so changes are localized.

## Timing Breakdown

For each scene or beat, record:

- Start frame and end frame.
- Main visual event.
- Primary spring or interpolation.
- Secondary follow-through delay.
- Audio or copy cue, if any.

Prefer fewer strong beats over many equal-weight events. A short video should still breathe: give the viewer a setup, a focal moment, and a settle.

## Implementation Order

1. Register composition dimensions, fps, duration, and props in `Root.tsx`.
2. Build the static final layout first.
3. Add primary motion with `useCurrentFrame()`, `useVideoConfig()`, `spring()`, and `interpolate()`.
4. Add staggered secondary and tertiary layers.
5. Add polish only after the core timing is readable.
6. Preview frame ranges around each beat and fix clipping, overshoot, or illegible text.

## Quality Check

Before final output, verify:

- No CSS animations or transitions drive render-critical motion.
- All randomness uses stable `random("seed")` values.
- All interpolations clamp both sides unless overshoot is intentionally handled.
- Text remains legible during motion.
- Elements settle cleanly before the last frame.
- Render commands and composition IDs match the code.
