# Frontier /goal Runtime Protocol

Use this reference when a `/goal` prompt should become an execution system, not only a prompt. The protocol combines the Goal Prompt Architect contract layer with a GoalBuddy-style local runtime: oracle, board truth, one active task, bounded workers, receipts, and final audit.

## Council decision

The best frontier `/goal` shape is two-layered:

1. **Compiler/governor**: decide readiness, execution surface, success criteria, trust boundaries, risk policy, verifier architecture, anti-spin rules, and terminal states.
2. **Runtime surface**: persist the mission in files, expose a board, execute one active task at a time, require receipts, and prevent completion until a final audit maps evidence to the oracle.

Do not choose prompt-only for a long, vague, stale, or high-risk autonomous mission when a runtime board would materially reduce drift, false DONE, forgotten context, or tiny-task churn.

## Frontier runtime primitives

### 1. Charter

`goal.md` is the owner-facing contract. It states:

- original user request
- interpreted mission
- selected execution surface and why
- live oracle and final proof
- success criteria
- constraints and non-goals
- risk policy
- verification ladder
- stop rules
- final report contract

### 2. Board truth

`state.yaml` is machine truth for the current run. It should be small enough to keep current, and explicit enough to resume safely.

Minimum fields:

```yaml
version: 1
generated_by: mg-goal-runtime-v1
goal:
  title: "..."
  slug: "..."
  kind: specific | open_ended | existing_plan | recovery | audit
  status: active | done | blocked | unsafe | budget_exhausted
  mission: "..."
  oracle:
    signal: "..."
    final_proof: "..."
rules:
  one_active_task: true
  state_yaml_is_truth: true
  prefer_largest_safe_useful_slice: true
  worker_must_stay_inside_allowed_files: true
  final_audit_required_for_done: true
active_task: T001
tasks: []
checks:
  last_verification:
    result: unknown
    commands: []
  dirty_fingerprint: unknown
```

### 3. Task

Exactly one task is active unless the user explicitly asks for parallel work and disjoint write scopes are proven.

Task types:

- **Scout**: read-only evidence mapping.
- **Judge**: read-only decision, risk, scope, or completion review.
- **Worker**: bounded write task with `allowed_files`, `verify`, and `stop_if`.
- **PM**: board maintenance, handoff, task activation, and final reporting.

A Worker task must include:

```yaml
allowed_files: []
verify: []
stop_if: []
```

The worker may not edit outside `allowed_files`. If it needs to, it must stop and leave a receipt.

### 4. Receipt

Every done, blocked, or escalated task leaves a compact receipt on the task card.

Scout receipt:

```yaml
receipt:
  result: done
  summary: "Mapped auth flow and found reset-token tests."
  evidence:
    - src/auth/reset.ts
    - tests/auth/reset.test.ts
  spawned_tasks:
    - T004
```

Judge receipt:

```yaml
receipt:
  result: done
  decision: approved | rejected | needs_more_evidence
  full_outcome_complete: false
  rationale: "The first worker slice is bounded and verifiable."
  next_task: T003
```

Worker receipt:

```yaml
receipt:
  result: done
  changed_files:
    - src/auth/reset.ts
    - tests/auth/reset.test.ts
  commands:
    - cmd: npm test -- tests/auth/reset.test.ts
      status: pass
  summary: "Password reset token path works and has regression coverage."
  stopped_because: null
```

Blocked receipt:

```yaml
receipt:
  result: blocked
  summary: "Needs production credential not available locally."
  missing_requirement: "Staging API token."
  safe_followup_task: T006
```

Blocked tasks do not automatically block the goal. The PM should continue with safe local work until no safe evidence-closing action remains.

## Runtime-backed `/goal` decision rule

Choose runtime-backed `/goal` when any of these are true:

- the mission is broad, vague, multi-hour, stale, or likely to need multiple work packages
- the task involves repo-wide implementation, release prep, bug hunts, refactors, or recovery
- false DONE is a major risk
- progress must survive context compaction or interruption
- several agents or roles are useful, but work still needs one authoritative board
- the user wants a frontier, maximum-quality, or deeply autonomous run

Choose a prompt-only compact/frontier `/goal` when the mission is narrow and can complete in one bounded pass without durable state.

Choose planning-only, audit-only, verifier harness, `/loop`, scheduled routine, or NOT READY when that surface is materially safer or more correct.

## Compiler workflow

1. Parse the user request into one measurable mission.
2. Run readiness and trust-boundary gates.
3. Select the smallest sufficient surface.
4. If runtime-backed, create `docs/goals/<slug>/goal.md`, `state.yaml`, and `notes/`.
5. Seed a board appropriate to the input shape:
   - vague/open-ended: Scout, Judge, Worker slot, final audit
   - specific but under-evidenced: Scout or Judge before Worker
   - existing plan: preserve plan facts, validate plan, then Worker slices
   - recovery: evidence mapping or triage before writes
   - audit: read-only unless fixes are separately approved
6. Activate exactly one first task.
7. Print the starter command:

```text
/goal Follow docs/goals/<slug>/goal.md.
```

## Execution policy

During `/goal` execution:

- Treat planning, Scout findings, Judge decisions, and queued Worker tasks as setup, not terminal outcomes.
- Prefer the largest safe useful slice over tiny helper churn.
- Continue after a verified Worker package when the full owner outcome remains incomplete.
- Do not run Judge after every Worker by default; use Judge at risk, ambiguity, phase, verification failure, or final audit boundaries.
- Do not mark the goal done while required Worker tasks are queued or active.
- Run the final PM/Judge audit before DONE.

## Final audit requirements

A final audit may mark DONE only when it maps:

- original mission
- oracle signal
- success criteria
- receipts
- latest verification
- current artifacts or diff
- unresolved risks

If the final audit proves only a tranche or work package, keep the goal active and create the next safe Worker, Scout, Judge, or PM task.
