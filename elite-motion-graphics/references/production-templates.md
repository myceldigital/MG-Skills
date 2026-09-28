# Production templates and example briefs

Use only the sections relevant to the task.
Replace fields with actual decisions or explicit unresolved facts; do not ship an unfilled template as a finished plan.

## Director's brief fields

| Field | Required decision |
|---|---|
| Purpose | Audience, takeaway, desired feeling/action, success evidence |
| Film premise | One sentence connecting the message to a visual mechanism |
| Content | Exact copy, claim sources, factual uncertainty, CTA if relevant |
| Inputs | Local paths/URLs, assets, ownership/permission, capture status |
| Reference analysis | Observed visual grammar, motion observations, borrow/transform/avoid |
| Design system | Palette/type roles, geometry, material, texture, camera, motion, sound |
| Timing | Frame rate, frame count, shot boundaries, reading holds, loop requirement |
| Audio | Source, excerpt/edit map, grid confidence, stems, voice, cue strategy |
| Delivery | Formats, codecs, alpha/color needs, captions, destination, editable sources |
| Resources | Existing engine, available tools, spend cap, render budget, deadline |
| Verification | Frames to inspect, playback/listening, target-size and technical checks |
| Approval | Only the actual user-requested decision gates and existing permissions |

## Shot/state table

| ID | Frames [start,end) | Purpose | Focal object / exact copy | Incoming state | Main action and hold | Outgoing state / transition | Audio cue | Verification |
|---|---|---|---|---|---|---|---|---|
| S01 | 0-60 at 30 fps | Establish scattered information | Five neutral information fragments | Stable fragments in distinct regions | Fragments make one incomplete alignment, then hold | One fragment becomes the anchor for S02 | One dry contact, then space | Hook understood without narration; no unreadable small copy |
| S02 | 60-150 at 30 fps | Explain organization | Verified product state, if supplied | Anchor retained in the same screen region | Authentic UI assembles around it, then holds | Selection prepares a causal feature transition | Quiet musical resolution | Match screenshot; sufficient reading time |

These two rows illustrate the contract, not a complete film.
Write every shot needed by the actual brief and confirm full coverage with no unintended gaps.

## Asset manifest fields

For each asset record: stable ID, local path, source URL or creator, permission/license status, capture or retrieval date, content hash, dimensions/duration, role, modifications, and any privacy redaction.
Distinguish user-supplied assets, original work, generated assets, licensed assets, and analysis-only references.
Do not copy private local paths or sensitive metadata into a public deliverable.

## Review record fields

Record the source revision, render manifest, exact artifacts inspected, viewing conditions, timestamps, criterion, observation, consequence, fix, and recheck result.
Keep automated checks, visual review, auditory review, and unverified criteria separate.
Scores without observations are not evidence.

## Example: short brand film with a clear mechanism

```text
Use $elite-motion-graphics to make a 16-second vertical film for the product in the supplied assets.
The idea is scattered updates becoming one useful decision.
Use the verified screenshots and exact supplied copy; do not add performance claims.
Make the motion precise and tactile, with one meaningful container transformation connecting the scenes.
Choose a restrained original visual system from the brand assets and explain the central device briefly.
Use supplied music if its rights and timing are established; otherwise develop a silent animatic first.
Proceed through style frames, timing, render, and critique using the available local tools.
Deliver the final MP4, poster, contact sheets, source, and checks actually completed.
```

## Example: UI state loop

```text
Use $elite-motion-graphics to animate the supplied interface states into an eight-second seamless loop.
Keep one container's identity throughout and make cursor actions causally accurate.
Preserve exact product text and data.
Choose reading holds before distributing transitions over the available frames.
If the requested states cannot be read in eight seconds, recommend the smallest content reduction or timing change before detailed animation.
Test geometry, text swaps, cursor continuity, and the boundary velocity; show a two-cycle preview.
```

## Example: music-led illustrated film

```text
Use $elite-motion-graphics to direct a 90-second illustrated film using the supplied track unchanged.
Build a character bible and three representative style frames from the user's reference library.
Map phrases and verified musical accents before the shot list.
Carry one character's objective through setup, complication, and payoff.
Use a rough full-duration animatic to resolve pacing before detailed rigs and textures.
Use generated media only within the already authorized tools and budget, recording provenance.
Verify identity, contacts, occlusion, captions, sound sync, and final encoded playback.
```

## Example: narrow critique and repair

```text
Use $elite-motion-graphics to review the supplied film and repair the unreadable transition around 4.2 seconds.
Reproduce it through playback and a consecutive-frame strip.
Preserve the existing visual direction and renderer.
Change only the affected timing, masks, or layout and any shared logic necessary to fix the cause.
Re-render that interval with handles, verify its neighbors, and report the before/after evidence.
```

## Delivery note structure

State the concept and delivered artifact first.
List requested dimensions, duration/frame rate, audio/caption state, source location, and key evidence.
Name any meaningful remaining issue or unavailable review capability.
Avoid unsupported award, ranking, conversion, or production-value claims.
