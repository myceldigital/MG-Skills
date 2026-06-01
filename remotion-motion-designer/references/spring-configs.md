# Spring Configs

Use `spring()` for most Remotion motion. Pick a personality based on the role of the layer, then tune from the preview.

## Core Presets

```ts
const bouncy = { damping: 12, stiffness: 100 };
const snappy = { damping: 25, stiffness: 180 };
const buttery = { damping: 50, stiffness: 50 };
const heavy = { damping: 30, stiffness: 80, mass: 3 };
```

- Bouncy: badges, small UI elements, playful counters.
- Snappy: professional text reveals, logo lockups, panels, product UI.
- Buttery: background parallax, camera drift, atmospheric elements.
- Heavy: large product renders, dramatic cards, hero objects.

## Usage Pattern

```ts
const progress = spring({
  frame: frame - startFrame,
  fps,
  config: snappy,
  durationInFrames: 24,
});
```

Offset `frame` by the element's start frame instead of nesting magic numbers in transforms.

## Tuning Guide

- Increase stiffness for faster acceleration.
- Increase damping to reduce bounce and overshoot.
- Increase mass for heavier, slower objects.
- Use `durationInFrames` when the beat must land on an exact frame.
- Delay secondary springs by 3 to 8 frames for follow-through.

## Common Pairings

- Logo reveal: snappy primary scale, bouncy particles, buttery background.
- Product hero: heavy product motion, snappy text, subtle buttery light move.
- Social clip: snappy headline, bouncy badges, quick staggered accents.
- Data viz: snappy bars or points, buttery camera, minimal bounce for accuracy.
