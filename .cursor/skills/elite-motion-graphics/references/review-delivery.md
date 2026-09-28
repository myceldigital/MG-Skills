# Critical review and delivery

## Evidence before judgment

Use the actual rendered revision, not a remembered preview or a description of what the code should do.
Review coverage must span the whole film.
Contact sheets sampled only on beats can miss transition failures, so add off-beat frames and consecutive strips around fast actions.
For a long film, paginate the sheets and label timestamps.
One fixed 30-cell sheet at two frames per second covers only 15 seconds.

| Evidence | Supports | Does not establish |
|---|---|---|
| Style frame | Composition, palette, typography at that moment | Pacing, trajectory, audio |
| Complete contact sheets | Coverage, variety, hierarchy changes, broad story arc | Smooth motion or absence of single-frame defects |
| Consecutive frame strip | Local trajectory, mask behavior, text overlap, pops | Full-film rhythm |
| Normal-speed playback | Pacing, continuity, reading time, loop perception | Technical media compliance by itself |
| Listening to final mux | Sync, mix, voice clarity, sonic continuity | Loudness and true peak without measurement |
| Media probes and decode tests | File structure, frame accounting, corruption | Aesthetic quality or readable copy |

If a viewing or listening tool is unavailable, produce the inspectable artifact and state that limitation.
Do not call a waveform inspection a listening pass.
Do not claim a script's file hash proves that the film looks good.

## Review in three lenses

First review as the intended viewer: what was understood, where attention went, what was memorable, and what was missed.
Then review as a designer: hierarchy, type, spacing, motion personality, rhythm, transitions, sound, and finish.
Finally review as a delivery engineer: content accuracy, assets, dimensions, frame accounting, decode health, and destination requirements.
For an edit, check the neighboring material and shared components that the change could affect.

## Anchored quality rubric

Use `unverified` when evidence is unavailable and `not applicable` when the criterion does not belong to the brief.
Scores are editorial judgments, not objective measurements or a benchmark ranking.

| Dimension | 1-4: fundamental defect | 5-7: functional but weak | 8-9: strong | 10: exceptional within the brief |
|---|---|---|---|---|
| Idea and message | Viewer cannot tell what it means | Message is clear but interchangeable | Visual mechanism makes the idea memorable | Every major choice reinforces a surprising, precise idea |
| Hook and payoff | Opening confuses; ending unresolved | Competent opening and generic ending | Immediate interest and earned resolution | Opening and ending change how each other is understood |
| Composition and type | Clipping, collisions, unreadable hierarchy | Readable with uneven staging or spacing | Controlled attention and confident typography | Distinctive frame design throughout, including transitions |
| Motion and continuity | Pops, drift, incoherent physics | Smooth but uniform or unmotivated | Object-specific weight, timing, and continuity | Choreography communicates beyond the copy |
| Rhythm and comprehension | Viewer cannot read or follow | Predictable pacing or excess dead time | Contrast, holds, and escalation feel intentional | Timing produces unusually clear emotional or intellectual payoff |
| Identity and truth | Wrong assets, invented claims, derivative identity | Accurate but generic or inconsistent | Specific, coherent, truthful, recognizable | A reusable visual and sonic identity emerges |
| Sound | Clipping, unintelligible voice, sync errors | Adequate track with decorative effects | Intentional sound-picture relationship and clean mix | Sound adds meaning that picture alone cannot carry |
| Finish and delivery | Corrupt, wrong format, obvious artifacts | Usable with visible roughness | Consistent polish and verified requested delivery | Exceptional finish with no material weakness for the intended use |

An 8+ target can guide ambitious work, but cannot override a hard failure or absent evidence.
Do not average away unreadable copy, false product behavior, an audible loop click, or an incorrect export.
A quiet film can score highly without constant novelty; a silent brief does not need added music to score well.

## Prioritize fixes

Rank defects by impact on meaning, visibility, frequency, and dependency.
Repair concept and structure before decorative detail; repair reading windows before subtle easing.
Each finding should contain time range, observed problem, viewer consequence, a specific intervention, and a verification method.

Example: `00:04.20-00:04.55: the incoming heading overlaps the outgoing label during the width morph, creating two competing readings. Clear the old label before 4.20, keep the new heading masked until its box fits, and inspect consecutive frames at final resolution plus normal-speed playback.`

Fix the three most consequential issues first, or fewer when fewer remain.
Render the affected region with handles, then recheck the full film after timing or shared-system changes.
Stop when requirements and the agreed quality bar pass, or when a real budget/tool limit prevents further useful work.
Report the unresolved limit instead of issuing a fictional pass.

## Accessibility and viewing conditions

Test at the actual destination size and against the expected interface overlays.
Use current platform specifications or a supplied overlay template for safe areas; do not hard-code one universal social safe zone.
Make essential information available without sound, through captions or an equivalent provided deliverable when appropriate.
Check captions for exact words, timing, contrast, occlusion, and sufficient display time.
Do not rely on color alone to distinguish important states.

Avoid large-area rapid flashes; evaluate risky sequences against applicable flash thresholds with appropriate tools.
Ordinary contact sheets cannot establish photosensitive safety.
For interactive/autoplay use, honor reduced-motion preferences and supply a static or reduced-motion alternative when needed.
A pre-rendered MP4 does not respond to a CSS preference by itself.
Use the current [WCAG flash guidance](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html) for web delivery rather than improvising a certification.

## Useful local checks

Inspect metadata and decoded frame count:

```bash
ffprobe -v error -count_frames -show_streams -show_format -of json out/final.mp4
ffmpeg -v error -xerror -i out/final.mp4 -f null -
```

Generate all contact-sheet pages, not only the first page:

```bash
ffmpeg -n -i out/final.mp4 -vf "fps=2,scale=270:-1,tile=6x5" -fps_mode vfr out/contact-%03d.png
```

Pair those pages with a timestamp map and boundary-specific samples from the timeline.
For a 12-frame strip beginning at 4.1 seconds:

```bash
ffmpeg -n -ss 4.1 -i out/final.mp4 -vf "scale=320:-1,tile=12x1" -frames:v 1 out/strip.png
```

Compare independently captured scene pixels at matched times for determinism.
Compare boundary states and watch two cycles for a loop.
Interpret blank/frozen-frame detectors against the intended edit; deliberate holds and black frames are not automatically errors.

## Handoff

Provide the requested formats, a clearly labeled final revision, and supporting artifacts that help the recipient use or revise it.
Include source and render instructions when editable delivery is requested or implied by code-based production.
Record asset provenance, exact versions, seed, dimensions, timing, sample/shutter settings, audio source/edit map, and verification evidence.
Deliver a poster chosen for communication, not merely the first frame.
For a loop, include the tested loop preview if useful.
Keep working previews out of the final deliverable list unless their status is clear.
