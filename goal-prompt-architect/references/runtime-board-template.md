# Runtime Board Template

Use this template when a `/goal` should run from a durable board. Prefer generating it with `tools/compile_goal_runtime.py` when the mission is simple enough to express as JSON or a mission string.

## File layout

```text
docs/goals/<slug>/
  goal.md
  state.yaml
  notes/
```

## `goal.md` skeleton

```markdown
# <Title>

## /goal Runtime Contract

MISSION:
<one measurable owner outcome>

RUNTIME SURFACE:
Use this goal as a frontier runtime-backed `/goal`: compile intent into a board, keep `state.yaml` as machine truth, execute independent dependency-ready tasks concurrently with one writer per conflicting scope, require receipts, and complete only after a final PM or Judge audit maps evidence back to the oracle.

ORACLE:
- live signal: <observable signal that keeps the run honest>
- final proof: <evidence required before DONE>

SUCCESS CRITERIA:
1. <observable criterion>
2. <observable criterion>

RISK POLICY:
Carry forward existing authorization; routine concurrent tasks and Manager packet revisions need no per-task approval.
Allowed without approval:
- <read-only or reversible local action>

Approval required:
- <specific action outside existing user authority; omit actions already covered by the request>

Forbidden:
- <explicit no-go>

VERIFICATION:
- <narrow check>
- <broader check>

EXECUTION LOOP:
1. Read `state.yaml`; derive active tasks from task statuses and select independent dependency-ready work with non-conflicting scopes.
2. Dispatch newly unblocked tasks without waiting for unrelated lanes; Scout/Judge tasks are read-only.
3. Worker tasks may write only inside `allowed_files` and must run `verify`.
4. PM records receipts and advances the board.
5. Final audit decides DONE or next task.

STOP RULES:
Return exactly one terminal state: DONE, PARTIAL DONE, BLOCKED, UNSAFE, BUDGET EXHAUSTED, or NEEDS HUMAN DECISION.

FINAL REPORT:
Include terminal state, evidence-to-criteria mapping, changed files, commands/checks, receipts used, unresolved risks, and exact next action if not DONE.
```

## `state.yaml` skeleton

```yaml
version: 1
generated_by: mg-goal-runtime-v1
goal:
  title: "<Title>"
  slug: "<slug>"
  kind: "specific"
  status: "active"
  mission: "<Mission>"
  oracle:
    signal: "<Observable signal>"
    final_proof: "<Required final proof>"
rules:
  one_active_task: false
  one_writer_per_scope: true
  dependencies_required: true
  state_yaml_is_truth: true
  prefer_largest_safe_useful_slice: true
  worker_must_stay_inside_allowed_files: true
  final_audit_required_for_done: true
active_task: T001
tasks:
  - id: T001
    type: scout
    assignee: Scout
    status: active
    objective: "Map relevant context, verification commands, constraints, and the first safe useful slice."
    receipt: null
  - id: T002
    type: judge
    assignee: Judge
    status: queued
    objective: "Choose the largest safe useful Worker slice."
    receipt: null
  - id: T003
    type: worker
    assignee: Worker
    status: queued
    objective: "Execute the first Judge-approved implementation or artifact slice."
    allowed_files: []
    verify: []
    stop_if:
      - "Need a Manager packet revision for files outside allowed_files; continue independent in-scope work."
      - "Need an action outside existing user authority; complete safe preparation and ask only for the missing decision."
      - "Verification fails twice without new evidence: change hypothesis or request Manager replanning; do not abandon the mission."
    receipt: null
  - id: T999
    type: judge
    assignee: Judge
    status: queued
    objective: "Final audit: decide whether the full original owner outcome is complete."
    receipt: null
checks:
  last_verification:
    result: unknown
    commands: []
  dirty_fingerprint: unknown
```

## Board health checks

Before reporting DONE, check:

- active tasks are derived from `tasks[*].status`; `active_task` is only a legacy focus pointer
- each active task has accepted prerequisites, an owner, and a non-conflicting write/resource scope
- integrated results are verified before dependent work is accepted
- all done and blocked tasks have receipts
- every Worker receipt lists changed files and verification results where applicable
- final audit receipt includes `full_outcome_complete: true`
- no required Worker remains queued or active
- latest verification is fresh enough for the final claim
