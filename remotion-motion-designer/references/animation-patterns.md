# Animation Patterns

Use these patterns when translating motion design principles into Remotion.

## Staggered Entrance

```ts
const itemProgress = spring({
  frame: frame - startFrame - index * 3,
  fps,
  config: { damping: 24, stiffness: 170 },
});
```

Use for lists, words, cards, and data points. Keep the stagger short enough that the whole group reads as one event.

## Anticipation

Use a small reverse movement before the main move.

```ts
const prep = interpolate(frame, [start, start + 6, start + 18], [0, -10, 0], {
  extrapolateLeft: "clamp",
  extrapolateRight: "clamp",
});
```

Pair anticipation with a spring reveal for logos, hero objects, and title cards.

## Follow-Through

Drive secondary elements from delayed versions of the primary progress.

```ts
const primary = spring({ frame: frame - start, fps, config: snappy });
const secondary = spring({ frame: frame - start - 5, fps, config: bouncy });
```

Use this for shadows, glows, particles, label chips, or supporting text.

## Kinetic Typography

For readable kinetic type:

- Animate phrase groups, not every letter by default.
- Use clipping masks, y-translation, and opacity together.
- Keep final text still long enough to read.
- For typewriter effects, reveal with string slicing based on frame count.

## Data Reveal

For charts:

- Disable library animations.
- Use frame-driven scales, path lengths, opacity, and counters.
- Preserve chart accuracy over decorative bounce.
- Label key values after the visual motion settles.

## Deterministic Detail

For particles or repeated details:

```ts
const seed = random(`particle-${index}`);
```

Do not use `Math.random()`. It can make renders non-deterministic.
