# Uncertainty Burndown Module

Use this module when the agent must think for a long time without drifting.

```text
UNCERTAINTY BURNDOWN:
At preflight and every checkpoint, maintain the top uncertainties:
1. uncertainty
   - impact: high/medium/low
   - current confidence: 0-100%
   - evidence needed
   - next action to reduce uncertainty
   - whether it blocks progress

Always choose the next safe action that reduces the highest-impact uncertainty or closes the most important evidence gap. Do not stop because uncertainty exists if safe evidence-producing work remains.
```
