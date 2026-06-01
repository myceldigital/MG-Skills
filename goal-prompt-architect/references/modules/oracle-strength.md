# Oracle Strength Module

Use this module to prevent weak evidence from being treated as DONE.

```text
ORACLE STRENGTH:
For each success criterion, assign the strongest available verification oracle:

Level 5: deterministic automated test, benchmark, or build artifact proves the criterion
Level 4: integration check plus targeted manual or diagnostic evidence
Level 3: reproducible diagnostic artifact, snapshot, log, or fixture comparison
Level 2: static inspection plus plausible reasoning, with explicit uncertainty
Level 1: unverified claim or subjective judgment

DONE requires Level 4 or 5 evidence for core behavior unless the environment makes that impossible. If only Level 1-3 evidence is available, explain why stronger verification is unavailable and mark confidence accordingly.
```
