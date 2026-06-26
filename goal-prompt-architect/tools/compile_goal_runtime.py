#!/usr/bin/env python3
"""Compile a /goal mission into a durable runtime board scaffold.

This tool is intentionally dependency-free. It turns a small JSON spec or a
single mission string into Goal Prompt Architect runtime files:

  docs/goals/<slug>/goal.md
  docs/goals/<slug>/state.yaml
  docs/goals/<slug>/notes/

The generated board is a local execution surface, not proof of completion.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

DEFAULT_VERIFY = ["discover narrowest meaningful check before implementation"]


@dataclass
class GoalSpec:
    title: str
    mission: str
    slug: str
    kind: str = "specific"
    oracle_signal: str = "The owner outcome is demonstrably true using the listed verification steps."
    final_proof: str = "Final PM or Judge audit maps receipts and checks back to the mission."
    constraints: list[str] = field(default_factory=list)
    non_goals: list[str] = field(default_factory=list)
    success_criteria: list[str] = field(default_factory=list)
    allowed_without_approval: list[str] = field(default_factory=list)
    approval_required: list[str] = field(default_factory=list)
    forbidden: list[str] = field(default_factory=list)
    verify: list[str] = field(default_factory=lambda: list(DEFAULT_VERIFY))


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    slug = re.sub(r"-+", "-", slug)
    return slug[:64].strip("-") or "goal"


def as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def load_spec(args: argparse.Namespace) -> GoalSpec:
    if args.spec:
        raw = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    else:
        raw = {"mission": args.mission or ""}

    mission = str(raw.get("mission") or "").strip()
    if not mission:
        raise SystemExit("mission is required via --mission or --spec")

    title = str(raw.get("title") or mission.split(".")[0]).strip()
    slug = str(raw.get("slug") or slugify(title)).strip()
    oracle = raw.get("oracle") or {}
    if isinstance(oracle, str):
        oracle = {"signal": oracle}

    return GoalSpec(
        title=title,
        mission=mission,
        slug=slugify(slug),
        kind=str(raw.get("kind") or "specific").strip(),
        oracle_signal=str(oracle.get("signal") or raw.get("oracle_signal") or GoalSpec.oracle_signal).strip(),
        final_proof=str(oracle.get("final_proof") or raw.get("final_proof") or GoalSpec.final_proof).strip(),
        constraints=as_list(raw.get("constraints")),
        non_goals=as_list(raw.get("non_goals")),
        success_criteria=as_list(raw.get("success_criteria")),
        allowed_without_approval=as_list(raw.get("allowed_without_approval")),
        approval_required=as_list(raw.get("approval_required")),
        forbidden=as_list(raw.get("forbidden")),
        verify=as_list(raw.get("verify")) or list(DEFAULT_VERIFY),
    )


def yaml_scalar(value: str) -> str:
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def yaml_list(items: list[str], indent: int = 4) -> str:
    pad = " " * indent
    if not items:
        return f"{pad}[]"
    return "\n".join(f"{pad}- {yaml_scalar(item)}" for item in items)


def render_goal_md(spec: GoalSpec) -> str:
    constraints = "\n".join(f"- {item}" for item in spec.constraints) or "- No additional constraints supplied; discover and record constraints during preflight."
    non_goals = "\n".join(f"- {item}" for item in spec.non_goals) or "- Do not expand beyond the mission without a PM or owner decision."
    criteria = "\n".join(f"{idx}. {item}" for idx, item in enumerate(spec.success_criteria, 1)) or "1. Mission has observable evidence mapped to current receipts.\n2. Final audit confirms the owner outcome is complete or states the remaining gap."
    allowed = "\n".join(f"- {item}" for item in spec.allowed_without_approval) or "- Read-only inspection and reversible local edits inside the active task's allowed_files."
    approval = "\n".join(f"- {item}" for item in spec.approval_required) or "- Production changes, secrets, external side effects, destructive operations, broad dependency upgrades, or scope expansion."
    forbidden = "\n".join(f"- {item}" for item in spec.forbidden) or "- Claiming DONE without evidence, editing outside allowed_files, or using the worker's assertion as sole proof."
    verify = "\n".join(f"- {item}" for item in spec.verify)

    return f"""# {spec.title}

## /goal Runtime Contract

MISSION:
{spec.mission}

RUNTIME SURFACE:
Use this goal as a frontier runtime-backed `/goal`: compile intent into a board, keep `state.yaml` as machine truth, execute one active task at a time, require receipts, and complete only after a final PM or Judge audit maps evidence back to the oracle.

ORACLE:
- live signal: {spec.oracle_signal}
- final proof: {spec.final_proof}

KIND:
{spec.kind}

SUCCESS CRITERIA:
{criteria}

CONSTRAINTS:
{constraints}

NON-GOALS:
{non_goals}

RISK POLICY:
Allowed without approval:
{allowed}

Approval required:
{approval}

Forbidden:
{forbidden}

VERIFICATION:
{verify}

EXECUTION LOOP:
1. Read `state.yaml` and select exactly one active task.
2. If no active task exists, PM activates the next safest evidence-closing task.
3. Scout and Judge tasks are read-only and return receipts.
4. Worker tasks may write only inside `allowed_files` and must run the listed checks.
5. PM records receipts, updates board truth, and continues until the final audit proves completion.

STOP RULES:
Return exactly one terminal state: DONE, PARTIAL DONE, BLOCKED, UNSAFE, BUDGET EXHAUSTED, or NEEDS HUMAN DECISION.
Do not stop because planning is complete, one slice passed, docs are incomplete, or a task is blocked while safe local work remains.

FINAL REPORT:
Include terminal state, evidence-to-criteria mapping, changed files, commands/checks, receipts used, unresolved risks, and exact next action if not DONE.
"""


def render_state_yaml(spec: GoalSpec) -> str:
    verify_yaml = yaml_list(spec.verify, 8)
    return f"""version: 1
generated_by: "mg-goal-runtime-v1"
goal:
  title: {yaml_scalar(spec.title)}
  slug: {yaml_scalar(spec.slug)}
  kind: {yaml_scalar(spec.kind)}
  status: "active"
  mission: {yaml_scalar(spec.mission)}
  oracle:
    signal: {yaml_scalar(spec.oracle_signal)}
    final_proof: {yaml_scalar(spec.final_proof)}
rules:
  one_active_task: true
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
    inputs:
      - "goal.md"
    constraints:
      - "Read-only. Do not edit implementation files."
    expected_output:
      - "Findings"
      - "Verification options"
      - "Candidate first Worker slice"
    receipt: null
  - id: T002
    type: judge
    assignee: Judge
    status: queued
    objective: "Choose the largest safe useful Worker slice by impact, reversibility, and verification strength."
    inputs:
      - "T001 receipt"
    expected_output:
      - "Decision"
      - "allowed_files"
      - "verify"
      - "stop_if"
    receipt: null
  - id: T003
    type: worker
    assignee: Worker
    status: queued
    objective: "Execute the first Judge-approved implementation or artifact slice."
    allowed_files: []
    verify:
{verify_yaml}
    stop_if:
      - "Need files outside allowed_files."
      - "Need production, secrets, destructive action, or external side effect."
      - "Verification fails twice without a changed hypothesis."
    receipt: null
  - id: T999
    type: judge
    assignee: Judge
    status: queued
    objective: "Final audit: decide whether the full original owner outcome is complete."
    inputs:
      - "All receipts"
      - "Latest verification"
      - "Current diff or generated artifacts"
    expected_output:
      - "complete | not_complete"
      - "full_outcome_complete: true | false"
      - "missing evidence"
      - "next task if not complete"
    receipt: null
checks:
  last_verification:
    result: unknown
    commands: []
  dirty_fingerprint: unknown
"""


def write_goal(spec: GoalSpec, root: Path, force: bool = False) -> Path:
    goal_dir = root / spec.slug
    goal_md = goal_dir / "goal.md"
    state_yaml = goal_dir / "state.yaml"
    notes_dir = goal_dir / "notes"

    if goal_dir.exists() and not force:
        raise SystemExit(f"refusing to overwrite existing goal directory: {goal_dir} (use --force)")

    notes_dir.mkdir(parents=True, exist_ok=True)
    goal_md.write_text(render_goal_md(spec), encoding="utf-8")
    state_yaml.write_text(render_state_yaml(spec), encoding="utf-8")
    return goal_dir


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compile a mission into a runtime-backed /goal board scaffold.")
    parser.add_argument("--spec", help="Path to a JSON goal spec.")
    parser.add_argument("--mission", help="Mission text when no JSON spec is provided.")
    parser.add_argument("--out", default="docs/goals", help="Output root for goal folders. Default: docs/goals")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing goal folder.")
    parser.add_argument("--dry-run", action="store_true", help="Print generated files instead of writing them.")
    args = parser.parse_args(argv)

    spec = load_spec(args)
    if args.dry_run:
        print(f"# FILE: docs/goals/{spec.slug}/goal.md\n")
        print(render_goal_md(spec))
        print(f"\n# FILE: docs/goals/{spec.slug}/state.yaml\n")
        print(render_state_yaml(spec))
        return 0

    goal_dir = write_goal(spec, Path(args.out), force=args.force)
    print(json.dumps({"goal_dir": str(goal_dir), "goal_md": str(goal_dir / "goal.md"), "state_yaml": str(goal_dir / "state.yaml")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
