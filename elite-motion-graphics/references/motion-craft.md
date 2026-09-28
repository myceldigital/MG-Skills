# Motion craft and continuity

## Choreograph events, not properties

Describe each action in phases: preparation, impulse, travel, arrival, response, and rest.
Choose which phases matter for this object and this shot.
A cursor click may need a travel arc, a readable hover, a press, and a causally ordered response.
A monumental title may need almost no overshoot but a long deceleration and a stable hold.

Assign primary action, secondary reaction, and optional texture to separate timing channels.
Secondary motion supports the main action; it must not create a second competing focal event.
Use stagger to express causality or spatial order, not as a universal delay applied to every element.
Keep related elements grouped when their unity carries meaning.

Anticipation is useful when it improves comprehension or character.
Follow-through should reveal material or mass.
Use squash/stretch with volume and attachment in mind; a rigid interface panel should not deform like a rubber toy without a reason.

## Choose the right interpolation

| Behavior | Starting choice | What to inspect |
|---|---|---|
| Readable information placement | Monotone easing or critically damped response | No oscillation during reading |
| Responsive container or object | Damped spring | Overshoot, settling time, collisions |
| Camera move | Designed position/velocity curve | Stable horizon, focal continuity, comfortable acceleration |
| Mechanical conveyor or continuous drift | Constant velocity | No accidental deceleration at shot boundaries |
| Character gesture | Pose-to-pose arcs and holds | Silhouette, motivation, balance, contact |
| Seamless cyclic motion | Periodic function or periodic spline | Matching position and velocity across the boundary |

Springs are one tool, not a substitute for timing judgment.
For a spring with mass `m`, stiffness `k`, and damping `c`, use `w0 = sqrt(k/m)` and damping ratio `z = c/(2*sqrt(k*m))`.
An underdamped spring oscillates; a critically damped spring returns without oscillation; an overdamped spring has a different, slower response.
Do not treat every `z >= 1` as critical damping.
The bundled [motion module](../scripts/motion.mjs) implements all three regimes analytically.

Tune settling time and overshoot against the distance traveled and available reading window.
The same normalized overshoot can be negligible on a small toggle and enormous on a full-frame camera move.
For opacity, bounded radii, or reveal percentages, clamp where semantics demand it.
For position, clamping a spring can introduce a velocity discontinuity; choose a suitable response instead.

## Retargeting and continuity

For a fixed linear spring system starting at rest, a sequence of target changes can be evaluated as the initial value plus the sum of each target delta multiplied by its delayed step response.
This preserves position and velocity without simulating earlier frames.
It assumes fixed physical parameters, an ordered target schedule, and that specific initial condition.
It does not automatically handle collisions, constraints, changing spring parameters, or arbitrary initial velocity.
Use an analytic piecewise state solution or a baked simulation for those cases.

Sample both sides of every event boundary.
Position continuity is C0; velocity continuity is C1; acceleration continuity is C2.
Choose the necessary continuity from the intended effect.
A motivated hard cut deliberately breaks spatial continuity; an unplanned snap inside a morph is a defect.

## UI morphs as a state machine

Define each state's container, content, cursor, selection, focus, data, and permitted transition.
Keep object identity perceptible through location, shape, color, or a conserved detail.
Use separate tracks for container geometry and content visibility.
Let departing content clear before it collides with incoming content, and reveal new content when sufficient geometry exists to contain it.
A short mask or blur can support a swap; it must not hide a broken state change.

Cursor actions need plausible targets and causality: movement, hover, press, response.
Match click audio to the chosen contact moment.
Ensure a hand cursor, hover state, text field, or loading indicator matches the actual interaction being represented.
Do not show real-product functionality that has not been verified.

For elastic tab indicators, give leading and trailing edges related but distinct timing.
Reverse the leading edge when travel direction reverses.
Preserve minimum width and avoid inversion.
For SVG path morphs, normalize compatible topology, winding, anchors, and point correspondence; arbitrary path-string interpolation is insufficient.

## Transitions carry information

Choose a transition by what it preserves or changes:

- Match cut: carry shape, position, scale, direction, or meaning across scenes.
- Occlusion wipe: an existing object passes in front and reveals the next state.
- Spatial travel: the camera reveals a neighboring part of an established world.
- Transformation: one object becomes another through a meaningful shared property.
- Graphic cut: switch decisively when the idea needs a contrast or reset.
- Dissolve: convey duration, memory, softness, or an intentional ambiguity.

Design the transition midpoint as carefully as the key poses.
Inspect overlaps, unreadable composite text, masks, camera speed, and premature disappearance.
Avoid spending more visual attention on the transition than on the message it connects.

## Camera and motion blur

Separate world motion from camera motion.
Avoid simultaneously moving every layer and the camera unless the viewer has a stable anchor.
Use parallax according to the intended depth model and maintain consistent occlusion.
For 3D work, choose focal length and camera distance together; perspective is not just object scale.

Temporal blur integrates exposure over time; it is not a spatial Gaussian blur or a trail overlay.
For sample count `S`, frame rate `f`, shutter fraction `a`, and center time `tc`, sample `tc + a/f * ((j+0.5)/S - 0.5)` for `j = 0..S-1`.
Define whether `tc` is frame-start time or the midpoint of the frame interval.
The bundled starter renderer uses the midpoint `(n+0.5)/f`.
Do not blend across a hard cut; clamp exposure to that shot or render the shots independently.
Linear-light, premultiplied-alpha accumulation is the physically appropriate route; simple encoded-color averaging is a preview approximation.
Test fast thin strokes and typography for ghosting before increasing samples.

## Seamless loops

Modulo time is an address calculation, not a continuity guarantee.
Design `x(T) = x(0)` and, where motion should remain smooth, `v(T) = v(0)` for every visible track.
Include cursor, camera, masks, particles, texture, lighting, and audio state.
Use periodic paths, boundary-matched splines, baked periodic simulation, or a motivated editorial seam.
For spring-based loops, solve or pre-roll the periodic state; merely returning to the first target may leave residual velocity.

Export frames `0..N-1`, not an extra duplicate endpoint at `T`.
The last exported sample is normally just before the boundary and need not be pixel-identical to the first.
Test values around the boundary, then watch at least two cycles at normal speed.
For audio, consider waveform continuity, musical phrase resolution, reverb tails, and codec priming; a visually seamless MP4 may still have an audible seam in a target player.
