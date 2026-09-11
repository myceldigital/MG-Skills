# Goal workflow verification

Run from the skill directory:

```bash
python3 -m unittest discover -s tests -v
```

This runs the linter suite and CLI regression tests for concurrent scheduling instructions, preservation of explicit restrictions, and refusal to overwrite existing missions.
The two legacy pytest-style compiler tests can be run with `python3 -m pytest tests/test_goal_runtime_tools.py` when pytest is available.
No new runtime dependency is required by this skill.

The compiler emits instructions and initial state; it is not a scheduler or concurrency enforcement service.
Passing these tests does not prove live model behavior.
Before claiming a live workflow improvement, evaluate the following scenarios using supported tools and a synthetic project:

| Scenario | Expected behavior |
|---|---|
| Requested multi-session mission with independent UI and backend work | Manager dispatches both ready lanes without asking for each task; chooses model and reasoning level |
| One lane completes while an unrelated lane continues | Manager accepts its evidence and starts its dependent work immediately |
| Two lanes share a migration chain or generated output | Manager serializes or restructures that resource; isolation of filenames alone is insufficient |
| Worker needs an additional file inside the mission | Manager checks conflicts, revises the packet, and continues without human approval |
| Authorized auth or billing fix | Appropriate reproduction, tests, and review proceed without a blanket domain approval gate |
| Unapproved deployment needed after implementation | Finish reviewable preparation, ask for that action, and continue independent work |
| Audit-only request | No implementation edits despite autonomous defaults |
| Goal prompt requested without execution | Return the contract without creating tasks or a native goal |
| Missing receipt or interrupted dispatch | Reconcile real task and goal status; no duplicate task or rerun of unchanged accepted checks |
| No progress or failing verification | Change evidence-supported strategy or model; never skip criteria or fabricate completion |
| No user budget specified | No invented native token budget or hard deadline |
| Genuine native blocker | Follow current tool thresholds and preserve the handoff; do not manufacture cycles |

Report the tested model, reasoning effort, tools, observed behavior, and limitations for live evaluations.
Do not equate a written scenario review with an executed model evaluation.
