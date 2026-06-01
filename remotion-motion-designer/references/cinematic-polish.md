# Cinematic Polish

Use polish after the core animation communicates clearly. It should improve depth, focus, and perceived production value without obscuring the subject.

## Depth

- Layer foreground, subject, and background with different motion speeds.
- Use scale, blur, opacity, and shadow consistently to imply distance.
- Make the primary subject the sharpest and highest-contrast element.

## Motion Blur

Use `@remotion/motion-blur` for fast camera moves or rapid object travel. Keep blur subtle for interface videos and stronger for title sequences or product reveals.

## Film Grain and Texture

Use low-opacity deterministic noise or a static texture overlay. Keep it under 8 percent opacity unless the brief explicitly asks for a gritty look.

## Light and Glow

- Tie glows to reveal moments or beat hits.
- Animate opacity and radius from frame values.
- Avoid permanent high-intensity glow around small text.

## Camera Moves

For 2D compositions, simulate camera movement by transforming grouped layers. For 3D compositions, animate camera position and target from `useCurrentFrame()`; do not use runtime `useFrame()` loops.

## Final Pass

Preview the first frame, each beat frame, and the final frame. Confirm there are no clipped elements, accidental scrollbars, unreadable text, or unresolved motion.
