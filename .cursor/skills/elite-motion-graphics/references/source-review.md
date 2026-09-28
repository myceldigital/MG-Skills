# Source review and technical corrections

## Origin and scope

This skill synthesizes the user-supplied course titled "How to build motion design studio with Opus 5.5 (Full-course)", attributed in the paste to movez.substack.com, reviewed on 2026-09-28.
The supplied text contains 12 lessons, code samples, quoted social posts, and repository links.
It is the conceptual starting point, not an API specification or proof of model superiority.
The skill is model-neutral and does not depend on the course's model names, release claims, viral statistics, pricing anecdotes, or advertised production times.
No claim is made that every embedded video or truncated social thread was available for playback.
The course itself is not redistributed in this repository.

## Lesson-by-lesson synthesis

| Lesson | Retained | Strengthened or corrected | Primary destination |
|---|---|---|---|
| 01 Pixels | Code can define frames as functions of time | Reproducibility includes assets, seeds, rasterizer, fonts, simulation, and media decode | Render engineering |
| 02 Setup | A usable runtime and feedback loop matter | Discover existing tooling; local installs and verified versions; no fixed model/effort or auto-install assumptions | Skill workflow and render engineering |
| 03 One-liner | A short reel can calibrate a pipeline | A generic showreel prompt does not establish concept or distinctiveness | Art direction |
| 04 Brand | Real screenshots, logos, fonts, and product evidence | Verify behavior and claims; use authorized captures and remove private data | Art direction and production templates |
| 05 Reference | Extract a style grammar before implementation | Separate still evidence from motion evidence; transform principles into original work | Art direction |
| 06 Spec | Enumerate states, causal cursor actions, and content timing | Feasible reading windows, exact frame accounting, actual loop continuity | Motion craft and templates |
| 07 Engine | Seekable scenes, headless capture, frame-based encoding | Asset failures, encoder exit codes, local serving, repeat checks, frame-count verification | Render engineering and starter |
| 08 Springs | Closed-form motion and additive target responses | Correct all damping regimes; state assumptions; retain other suitable interpolation | Motion craft and tested motion module |
| 09 Sound | Shared timing, measured audio, synthesized options | Onsets/beats/downbeats differ; mix with headroom; destination-specific loudness | Sound and editorial |
| 10 Director brief | Style bible, characters, animatic, staged production | Scope-proportional gates, permission-respecting autonomy, provenance, truthful medium claims | Advanced production and templates |
| 11 Critique | Inspect actual frames and iterate on observed flaws | Complete timeline coverage, playback/listening, anchored ratings, bounded iteration | Review and delivery |
| 12 Ship | Reframe formats and package reusable practice | Verified exports, editable handoff, captions, source tracking; no income promises | Review and delivery |

## Corrections worth preserving

1. The source's `z >= 1` spring branch uses a critically damped equation for overdamped systems.
   The bundled motion module evaluates the overdamped roots separately and tests the governing differential equation.
2. A sum of delayed step responses models a fixed linear system starting at rest.
   It is not a general solution for changing physics, collisions, or arbitrary initial conditions.
3. `t % duration` does not repair a loop seam.
   Boundary state and usually velocity must match; do not duplicate the endpoint frame.
4. `beats[::4]` cannot establish downbeats without meter and phase confirmation.
   Beat tracking and musical interpretation are separate steps.
5. At 120 BPM, eight 4/4 bars last 16 seconds.
   Duration and beat structure must agree explicitly.
6. More subframes do not by themselves define a shutter or correct blur.
   Specify exposure interval, sample phase, accumulation color space, alpha handling, and cut behavior.
7. A seed alone does not remove history dependence if the PRNG advances differently with render order.
   Derive noise from stable identity/time or precompute it.
8. Waiting for fonts generally is not proof that a particular intended face loaded.
   Explicitly request and verify the actual font asset and inspect the output.
9. A fixed contact sheet can omit most of a long film.
   Paginate full coverage and add transition samples.
10. Hashing an encoded movie is a weak scene-determinism test.
    Compare matched scene pixels after different seek histories and verify output frame accounting separately.
11. Encoder termination does not imply successful encoding.
    Check exit status, decode health, frame count, duration, and audio requirements.
12. Never continuing until self-scores reach 8 can create an unbounded loop, and three mandatory rounds can waste effort.
    Iterate on observed defects within the task budget and report unresolved problems.
13. Springs, novelty every few seconds, one accent color, no fades, and no corner text are aesthetic heuristics rather than laws.
    Use them only when they serve the brief.
14. A ten-minute non-response cannot supply an approval the user required.
    Continue already authorized independent work; keep actual approval gates intact.
15. -14 LUFS and CRF 16 are possible delivery choices, not universal standards.
    Use destination requirements and check the encoded result.
16. The article's two-scene illustration only draws content for its first six seconds despite declaring 15 seconds.
    A starter must have complete frame coverage and must not be presented as a finished film.

## Primary technical references

Use installed versions and current official documentation when behavior matters.
These pages were consulted during creation; reread only the relevant topic when maintaining an implementation.

- [OpenAI skill format and testing](https://developers.openai.com/plugins/build/skills): concise entry point with conditional resources and realistic activation/behavior checks.
- [Remotion animation](https://www.remotion.dev/docs/animating-properties) and [official agent skills](https://www.remotion.dev/docs/ai/skills): framework-specific animation and skill guidance.
- [GSAP seek](https://gsap.com/docs/v3/GSAP/Timeline/seek()/): explicit timeline positioning and callback semantics.
- [Playwright page API](https://playwright.dev/docs/api/class-page): browser capture and page lifecycle facilities.
- [FFmpeg filters](https://ffmpeg.org/ffmpeg-filters.html): temporal mixing, tiling, and loudness processing.
- [librosa beat tracking](https://librosa.org/doc/0.11.0/generated/librosa.beat.beat_track.html): tempo/beat estimator inputs and outputs.
- [WCAG flash guidance](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html): web delivery flash considerations.

## Course-linked project reading list

Repository landing pages were checked during synthesis.
These are optional examples and research leads, not bundled dependencies, audited code, or promises that their installation recipes remain current.
Review the actual commit, license, dependency manifest, and assets before reusing code or content.

- [PDoomVideo](https://github.com/JohnHeibel/PDoomVideo): shared animation guide, storyboard, chapter organization, and rendered-film example.
- [ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase): hand-painted animation starter and character-oriented workflow.
- [claude-animation-skill](https://github.com/buildwithhanif/claude-animation-skill): code-based hand-drawn production example.
- [HyperFrames](https://github.com/heygen-com/hyperframes): seekable HTML video framework and associated production tooling.
- [Battle-of-Austerlitz-Film](https://github.com/WinterArc21/Battle-of-Austerlitz-Film): long-form film example.
- [awesome-ai-motion](https://github.com/guanmo-ai/awesome-ai-motion): curated examples and original-prompt research leads.
- [awesome-opus-5-5-videos](https://github.com/athemeroy/awesome-opus-5-5-videos): source-linked collection for comparative reference research.

Popularity and self-reported production time are not quality evidence.
No third-party project code, music, fonts, character designs, or screenshots are included in this skill.
