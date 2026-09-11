# ADR 0001: Autonomous parallel goal execution

Date: 2026-09-07

## Status

Accepted by the user's request to remove per-subgoal authorization and unnecessary restrictions.

## Context

The main skill allowed parallelism only exceptionally, while its compiler still emitted a global serial-worker rule.
Generic templates also imposed broad approval categories and artificial persistence and polishing gates.
These instructions could stall an already authorized mission.

## Decision

Within a requested Manager/Implementer workflow, the Manager autonomously dispatches independent dependency-ready lanes, routes models, revises in-scope packets, and accepts verified phases.
Use one writer per conflicting resource scope and an integration owner.
Carry forward existing authority; request only a specific missing material decision after safe preparation.
Use real acceptance criteria and native runtime limits instead of invented deadlines or subjective quality scores.

## Alternatives considered

- Global sequential execution: simple, but delays independent work without evidence of a conflict.
- Unrestricted fan-out: permits conflicting writes and obscures integration responsibility.
- Per-task human approval: contradicts the requested autonomous workflow.

## Consequences

New scaffolds set `one_active_task: false` and `one_writer_per_scope: true`.
Task statuses identify active work; the existing `active_task` key remains a legacy focus pointer.
The compiler does not enforce scheduling, and existing boards are not rewritten.
Consumers that only support one active task must remain serial until explicitly adapted; read-only parallel work can still be useful.
Native task-creation, model-selection, goal-lifecycle, and destructive-action boundaries remain in effect.

## Verification

See EVALS.md and tests/test_autonomous_runtime.py.
