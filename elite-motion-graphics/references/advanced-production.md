# Advanced production modes

## Character and hand-drawn work

Create a character bible before multiplying scenes: silhouette, proportions, landmark positions, palette roles, line weight, expression range, poses, and permitted deformation.
Use a turnaround or reference sheet when views change.
Test recognizable poses at thumbnail size.
Define the rig's coordinate system, joint pivots, hierarchy, constraints, and attachment rules.

Animate thought and intention through poses, eyelines, anticipation, balance, and held reactions.
Track center of mass, support contacts, planted feet, hand-object relationships, and prop continuity.
Use arcs and spacing to support weight; do not add sinusoidal movement to every joint to simulate life.
For dialogue, align mouth shapes to phonetic events and let facial expression support the acting.
Speech recognition output still needs timing and spelling review.

For drawn texture, keep stroke topology stable when the underlying form is stable.
Use deliberate line boil at a controlled cadence if the art direction calls for it.
Unseeded per-frame noise causes accidental crawling and can make small details unreadable.
Separate paper texture, pigment coverage, edge behavior, and stroke variation instead of placing one noise overlay over everything.
Study actual mark-making references at the scale of the final frame.

## 3D and material-led motion

Block composition with simple geometry before expensive shading.
Choose the camera's focal length, movement path, and focus strategy from the intended perception of scale.
Anchor objects with plausible contact, shadows, reflections, or deliberately stylized alternatives.
Keep key, fill, background separation, and highlight shape under control.
Design lights as part of the composition; indiscriminate bloom hides material problems.

For physical simulation, fix units, timestep, seed, initial state, collision geometry, and bake version.
Check tunneling, intersections, contact jitter, and energy changes before polishing materials.
Use baked caches or a seekable analytic system for rendering out of order.
Budget geometry, texture memory, samples, and denoising around the highest-value shots.
Test representative frames at the final output size before committing the whole film.

## Generated footage and code-drawn reconstruction

Generated media can supply motion studies, environments, or plates when it serves the brief and is available within authorization.
Record model/tool, inputs, source rights, generation settings, cost, and output provenance where available.
Do not promise identity consistency, physical accuracy, or commercial permission merely because a tool generated the media.

For generate-then-trace workflows:

1. Define the desired style and character identity independently of the generated plate.
2. Select useful key poses, trajectories, camera information, and timing from authorized reference footage.
3. Reconstruct shapes, rig motion, or trajectories with a consistent graphic system.
4. Correct implausible anatomy, object drift, occlusion, contact, and continuity errors rather than reproducing them.
5. Compare both key poses and intermediate motion; a few matching stills do not validate a reconstruction.
6. Track which final pixels come from generated plates versus code-drawn or other sources.

Do not describe a final film as entirely code-drawn if generated footage remains visible.
Do not launch paid generations merely because the source article names an API key.
Never store credentials in the skill, source repository, render manifest, screenshots, or public prompts.

## Data visualization and factual explainers

Use authoritative data and preserve labels, units, scales, dates, and uncertainty.
Animate comparison in a way that lets viewers perceive the same baseline and scale.
Do not invent smooth interpolation through missing observations unless clearly presented as a model.
Use a reading hold after a key value lands.
For historical or scientific narratives, verify important claims and source them in the production notes.
Do not let dramatic staging imply a factual claim the evidence does not support.

## Long-form and multi-session production

Maintain a style bible, character/asset registry, timing map, sound palette, and shot contracts as durable production inputs.
Each shot contract identifies input state, output state, duration, camera, assets, copy, and transition handles.
Build one representative difficult shot before replicating its technique across chapters.
Review the film's macro pacing before polishing individual shots in isolation.

Use the available task system for live ownership and progress when coordination is needed.
Do not turn a Markdown guide into a live lock or lease database.
If parallel agents are authorized, assign non-overlapping scenes or modules and keep shared primitives under a single owner.
Integrate an early sample from each contributor to test consistency before full production.
Without authorized delegation, run the same stage gates sequentially.

For resumption, record a concise production snapshot: active revision, source paths, render settings, valid caches, next concrete task, and unresolved decisions.
Keep evidence tied to the revision that produced it.
Never assume that an overnight autonomous run or a higher reasoning setting guarantees improvement.

## Versioning and localization

Separate timing/content from per-format layout and style tokens.
Use named shot IDs and stable asset IDs so revisions can be traced.
Design vertical, square, and wide compositions from shared intent rather than stretching or blindly cropping.
Reassess camera framing, diagram arrangement, text wraps, captions, and CTA holds in every requested format.
For localization, plan expansion, script direction, numeral conventions, font coverage, pronunciation, and voice duration.
Keep brand names, legal copy, and verified claims exact.
