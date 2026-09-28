# Deterministic rendering and delivery engineering

## Choose an engine from the project

| Route | Good fit | Main constraint |
|---|---|---|
| Canvas/SVG + browser capture | Compact bespoke 2D films and UI studies | You own asset readiness, timing, capture, and encoding |
| Remotion | React components, parameterized films, repeatable data-driven series | Use the installed version's APIs and frame-driven state |
| HTML + seekable timeline | DOM typography and web layout compositions | Pause autonomous tickers and explicitly seek all media and animation |
| Blender or another existing DCC | Real 3D, lighting, material, complex rigging | Bake simulations and declare render/color settings |
| Existing timeline/compositing project | Editorial, compositing, handoff to human animators | Preserve editable structure and verify frame-accurate exports |

Do not replace an existing engine merely because the course used a single HTML file.
Choose additional packages only when existing capabilities are insufficient.
Check license, maintenance, vulnerabilities, version compatibility, and runtime cost before adding them.
Keep installs local and lock the resolved versions.
Do not assume a slash command, model name, plugin, or skill from a social post exists in the current environment.

## Render contract

Define `frame = render(time, dimensions, inputs, assets, seed)`.
For a browser scene, expose an awaitable readiness signal and a synchronous or awaitable `window.seek(t)` that completes the requested frame.
Make render mode explicit; do not use `navigator.webdriver` as the switch.
Preview playback may use a clock, but both paths must call the same time-based drawing function.

Reset transforms, clipping, alpha, compositing, and mutable drawing state on every frame.
Random values must derive from stable object/event identity and seed, not from how many frames have been rendered.
For temporally coherent variation, use smooth indexed noise or stable procedural geometry.
Bake stateful particles, physics, or cloth once with a fixed timestep and interpolate cached states by time.

Assets must be loaded, decoded, and correctly sized before capture.
Explicitly load required font faces; `document.fonts.ready` does not prove that an undeclared or unused face was requested.
Verify representative glyphs and line breaks.
Capture and fail on required asset errors, browser exceptions, and missing frames.
Avoid remote asset fetches during final rendering when local authorized copies are available.

For Remotion, derive animation from the composition frame and configuration, account for sequence-local time, and use framework-managed media/readiness facilities appropriate to the installed version.
For GSAP, pause the timeline and seek explicitly; avoid callbacks that mutate persistent state.
For video elements, wait for the requested decoded frame rather than treating assignment to `currentTime` as completion.
See [Remotion animation guidance](https://www.remotion.dev/docs/animating-properties) and [GSAP seek semantics](https://gsap.com/docs/v3/GSAP/Timeline/seek()/).

## Frame accounting

Set the frame rate `f` and integer frame count `N` as authoritative; duration is `N/f`.
If converting a requested duration, declare the rounding policy and actual duration.
For rational rates such as `30000/1001`, preserve the fraction and derive timestamps without accumulating floating-point step increments.
Use half-open shot intervals `[start, end)` so every output frame belongs to the intended shot.
Overlapping layers can cross these boundaries; scene ownership still needs to be explicit.

Map audio cues to sample indices independently of video rounding, then measure the residual sync error.
Include transition and exposure handles when rendering or caching a partial interval.
Cache keys must include code, assets, fonts, layout, seed, timing, renderer version, and quality settings.
Do not reuse a prior render after a relevant input has changed.

## Bundled Canvas calibration route

The starter demonstrates a complete seekable scene and deterministic capture without external assets.
It is silent and uses a system font, so it tests the pipeline rather than portable typography or final art quality.
The renderer supports integer frame rates, opaque Canvas output, a fixed 180-degree shutter in the scene sampler, and a single continuous scene.
It does not implement media seeking, alpha masters, shot-aware blur, rational frame rates, final audio, or color-managed mastering.
Use the project's production renderer or extend and test those features when required.

Copy `assets/canvas-starter.html`, `scripts/motion.mjs`, and `scripts/render.mjs` into the same directory in a motion project.
Have Node, FFmpeg, and a project-local compatible Playwright installation with its Chromium browser available.
An explicitly selected existing Chromium binary can be supplied through `MOTION_CHROMIUM_EXECUTABLE_PATH`; verify compatibility and record that browser version rather than silently substituting it.
Playwright is an optional tooling dependency because Node alone cannot render Canvas; it is Apache-2.0 licensed and maintained by Microsoft.
It affects development/render size and browser attack surface, not a shipped site's bundle.
Reuse an existing browser renderer when possible; verify the installed version and advisories before adding it.

From that directory, after installing the chosen Playwright version through the project's normal dependency process:

```bash
node render.mjs canvas-starter.html out/calibration --fps 30 --frames 120 --width 640 --height 360 --samples 1
node render.mjs canvas-starter.html out/calibration-blur --fps 30 --frames 120 --width 640 --height 360 --samples 4
```

Output directories must be new to prevent stale-frame contamination.
The renderer captures numbered PNGs, checks an out-of-order repeat, encodes a silent MP4, counts decoded frames, and records a manifest.
It fails if the browser, scene, encoder, or expected dimensions/frame count fail.
It uses a loopback-only static server and blocks nonlocal browser requests.
Only render trusted local scene code; executing code supplied by an arbitrary reference is a separate security decision.

## Reproducibility and resource management

Compare uncompressed scene pixels at the same timestamp after seeking elsewhere and in a fresh session.
Repeat at multiple timestamps, including boundaries.
Byte-identical encoded MP4s are neither necessary nor sufficient for proving scene determinism.
Declare the runtime/OS/font envelope because cross-platform rasterization can differ.

Estimate render cost from a representative interval: frame count times samples times capture cost, plus encoding and I/O.
At 1920x1080, one RGBA frame is about 8.3 MB before compression; avoid retaining an entire film in memory.
Use bounded concurrency and backpressure; cache expensive static geometry.
Capture frames to a fresh directory or use a pipe with explicit error, drain, exit, and cleanup handling.
An encoder's close event is not success unless its exit code is zero.
Publish a final filename only after validation; leave failures clearly marked as partial output.

## Encoding and mastering

Use the destination specification first.
For a broadly compatible opaque SDR review copy, H.264 with `yuv420p`, even dimensions, and fast-start metadata is a useful starting point.
CRF is a quality control, not a guaranteed bitrate or file size.
Inspect thin saturated strokes, small text, and gradients after compression.
For alpha or intermediate mastering, choose a codec and pixel format that preserve the required channels and bit depth.

Specify source and output transfer characteristics, primaries, range, and conversion when a color-managed workflow is required.
Adding metadata tags does not perform a color conversion.
Avoid claiming broadcast, HDR, or color-accurate delivery from an ordinary browser screenshot pipeline.
Measure delivered duration, frame rate, frame count, dimensions, audio streams, and decode integrity with actual media tools.
Read current [FFmpeg documentation](https://ffmpeg.org/ffmpeg.html) and [filter documentation](https://ffmpeg.org/ffmpeg-filters.html) for the installed build's capabilities.
