# Sound, music, and editorial timing

## Establish the sonic idea

Define the role of sound before choosing a track: propulsion, tension, warmth, scale, material, explanation, or surprise.
Use music, voice, designed effects, ambience, and silence as separate layers with distinct jobs.
A click should communicate contact; a tonal motif can communicate identity; silence can create anticipation.
Do not attach a whoosh to every moving element.

Choose music from the story's energy curve and delivery rights.
Use a supplied track unchanged if that is the instruction.
An original code-synthesized score is one option, not a quality guarantee or a requirement.
Do not claim a synth patch is an acoustic instrument recording.
Use authorized voices and confirm consent for voice cloning; do not infer permission from a public voice sample.

## Measure before synchronizing

For existing audio, determine the exact source file, sample rate, timeline offset, chosen excerpt, tempo behavior, meter, phrase boundaries, and useful transients.
Keep source times and composition times separate, with an explicit offset or edit map.
Listen to the result; a detected onset is not necessarily a beat, and a beat is not necessarily a downbeat.

`librosa.beat.beat_track` returns a tempo estimate and beat locations, not verified bar starts.
Taking every fourth detected beat assumes both 4/4 meter and a correct initial beat phase.
For pickups, half-time errors, tempo changes, or ambiguous percussion, annotate or correct the grid manually or use a suitable downbeat model and verify its output.
Store confidence and provenance so an estimated grid cannot silently become a measured fact.
See the [librosa beat tracker documentation](https://librosa.org/doc/0.11.0/generated/librosa.beat.beat_track.html).

A beat record should carry time in seconds, musical location if known, event type, confidence, and whether the entry is measured, inferred, or confirmed.
Use sample-accurate onset times when useful; convert to video frames only at the picture scheduling boundary.
If no reliable musical grid exists, cut to phrasing, speech, movement, or designed accents instead of forcing a guessed BPM.

## Compose the visual rhythm

Assign large changes to phrases and key structural beats, smaller reactions to selected subdivisions, and reading holds to musical space.
Contrast synchronization with controlled counterpoint.
If every action lands on every beat, the film can become predictable and exhausting.
Vary density and give the strongest event a quieter lead-in.

At 120 BPM a quarter-note beat is 0.5 seconds.
Eight bars in 4/4 contain 32 beats and last 16 seconds; do not label that plan a 15-second film without editing its structure.
For variable tempo, schedule from explicit beat times rather than a single BPM formula.
Voice intelligibility and comprehension take precedence over a perfect beat-aligned cut.

## Sound effects that belong to the world

Design a small family of effects with related timbre and distinct functions.
Use amplitude envelopes with short ramps, appropriate decay, and controlled tails.
For a frequency sweep, integrate instantaneous frequency into phase: `phase(t) = 2*pi*integral(f(t) dt)`.
Multiplying a time-varying frequency by time changes the resulting instantaneous frequency and may not create the intended sweep.

Generate noise from a deterministic cue-specific seed so adding an earlier cue does not alter every later effect.
Validate cue time, type, duration, channel layout, and gain.
Handle an empty cue list as silence, not as an invalid maximum or infinite buffer allocation.
Mix in floating point with headroom; hard clipping to 16-bit bounds is not a mixing strategy.
Reduce or filter aliasing in bright synthetic tones and discontinuous waveforms.

For a simple original score, define a motif, tonal center or intentional atonality, harmonic rhythm, register allocation, and sectional dynamics.
Vary articulation, voicing, and density with the narrative.
Humanization should be bounded and deterministic, preserving intentional picture synchronization.
Save music, voice, and SFX stems when future revisions will benefit.

## Mix and loudness

Balance the mix before normalization.
Clear the speech range, reduce competing transients, and automate music around voice when needed.
Check on headphones, small speakers, and in mono when those surfaces are available.
Use meters to supplement listening, not replace it.

Set loudness and true-peak targets from the destination or user brief.
For an unspecified social review copy, -14 LUFS integrated and at most -1 dBTP can be declared starting targets, not a universal platform standard.
Short idents, silent films, broadcast material, and music releases may need different treatment.
For two-pass normalization, measure the actual mixed program, apply its measured values, and measure the encoded delivery again.
Do not blindly amplify silence or invalid infinite measurements.
See [FFmpeg loudnorm](https://ffmpeg.org/ffmpeg-filters.html#loudnorm).

Match audio duration to the planned video duration deliberately.
Do not let an unexpectedly short audio file trim the film through an unexamined `-shortest` option.
Inspect beginnings, endings, silence, clipping, channel balance, sync, and any loop seam after final muxing.
If listening is unavailable, report metering and stream checks as completed and auditory judgment as unverified.
