#!/usr/bin/env python3
"""Lint and score /goal prompts as executable mission contracts.

The linter is heuristic by design. It catches failure modes that make autonomous
coding goals unsafe or unproductive: vague missions, missing verification,
unbounded authority, weak stop rules, no evidence matrix, marathon prompts
without durable state, and runtime-backed goals without an oracle/board/receipt
loop.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

CANONICAL_SECTIONS = {
    "mission": ("MISSION", "GOAL"),
    "context": ("CONTEXT", "PREFLIGHT", "RUNTIME SURFACE"),
    "constraints": ("CONSTRAINTS", "RISK + ACTION POLICY", "RISK POLICY", "RISK AND ACTION POLICY"),
    "success_criteria": ("SUCCESS CRITERIA",),
    "evidence_matrix": ("EVIDENCE MATRIX", "ORACLE"),
    "execution_loop": ("EXECUTION LOOP", "PLAN"),
    "verify": ("VERIFY", "VERIFICATION"),
    "stop": ("STOP", "STOP RULES", "DONE WHEN"),
    "output": ("OUTPUT", "FINAL REPORT"),
}

MARATHON_SECTIONS = {
    "long_horizon_intent": ("LONG-HORIZON INTENT", "LONG HORIZON INTENT"),
    "target_runtime": ("TARGET RUNTIME", "CYCLE BUDGET", "RUNTIME"),
    "persistent_state": ("PERSISTENT STATE", "DURABLE STATE"),
    "soft_hard_blockers": ("SOFT VS HARD BLOCKERS", "SOFT AND HARD BLOCKERS"),
    "failure_recovery": ("FAILURE RECOVERY",),
    "quality_ratchet": ("QUALITY RATCHET",),
    "phased_execution": ("PHASED EXECUTION",),
}

RUNTIME_SECTIONS = {
    "runtime_surface": ("RUNTIME SURFACE", "GOAL RUNTIME", "BOARD"),
    "oracle": ("ORACLE",),
    "task_rules": ("TASK RULES", "EXECUTION LOOP"),
    "receipts": ("RECEIPTS", "FINAL REPORT"),
    "final_audit": ("FINAL AUDIT", "STOP RULES", "FINAL REPORT"),
}

ANTI_PATTERNS = {
    "make no mistakes": "replaces verification with aspiration",
    "make it perfect": "creates unbounded polishing pressure",
    "do whatever it takes": "removes authority boundaries",
    "use every tool": "encourages indiscriminate tool use",
    "keep going until everything is fixed": "creates unbounded scope",
    "no need to run tests": "weakens the verification oracle",
    "skip tests": "weakens the verification oracle",
    "planning is complete so stop": "confuses planning with execution",
}

EVIDENCE_TERMS = (
    "required proof",
    "evidence found",
    "pass/fail",
    "confidence",
    "source",
    "remaining gap",
    "next action",
    "oracle",
    "receipt",
)

RISK_TERMS = (
    "allowed without approval",
    "approval required",
    "forbidden",
    "external side effect",
    "production",
    "secrets",
    "irreversible",
    "allowed_files",
)

VERIFY_TERMS = (
    "test",
    "lint",
    "typecheck",
    "build",
    "check",
    "manual",
    "evidence",
    "oracle",
    "receipt",
)

RUNTIME_TERMS = (
    "state.yaml",
    "board",
    "one active task",
    "active task",
    "receipt",
    "oracle",
    "scout",
    "judge",
    "worker",
    "allowed_files",
)

GOAL_SPECIFIC_STATE_TERMS = (
    ".goal/<goal-id>/",
    ".goal/<goal_id>/",
    ".goal/<run-id>/",
    ".goal/<run_id>/",
    "goal-specific",
    "unique state directory",
    "current-goal directory",
    "orchestrator-provided goal/run id",
    "mission slug plus timestamp",
    "docs/goals/<slug>",
)

ROOT_GOAL_STATE_TERMS = (
    ".goal/state.md",
    ".goal/evidence.md",
    ".goal/decisions.md",
    ".goal/failures.md",
    ".goal/commands.md",
    ".goal/handoff.md",
)

TERMINAL_STATES = (
    "DONE",
    "PARTIAL DONE",
    "BLOCKED",
    "UNSAFE",
    "BUDGET EXHAUSTED",
    "NEEDS HUMAN DECISION",
)


@dataclass
class Finding:
    code: str
    severity: str
    message: str
    recommendation: str


@dataclass
class CategoryScore:
    name: str
    score: int
    max_score: int
    notes: list[str]


@dataclass
class LintReport:
    path: str
    mode: str
    score: int
    max_score: int
    passed: bool
    category_scores: list[CategoryScore]
    findings: list[Finding]


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def has_heading(text: str, headings: Iterable[str]) -> bool:
    for heading in headings:
        pattern = rf"(?im)^\s*{re.escape(heading)}\s*:"
        if re.search(pattern, text):
            return True
    return False


def has_any(text: str, terms: Iterable[str]) -> bool:
    low = text.lower()
    return any(term.lower() in low for term in terms)


def count_success_criteria(text: str) -> int:
    match = re.search(r"(?ims)^\s*SUCCESS CRITERIA\s*:\s*(.*?)(?:^\s*[A-Z][A-Z /+\-]{2,}\s*:|\Z)", text)
    if not match:
        return 0
    block = match.group(1)
    numbered = re.findall(r"(?m)^\s*(?:\d+\.|[-*])\s+\S", block)
    return len(numbered)


def mission_text(text: str) -> str:
    match = re.search(r"(?ims)^\s*(?:MISSION|GOAL)\s*:\s*(.*?)(?:^\s*[A-Z][A-Z /+\-]{2,}\s*:|\Z)", text)
    return match.group(1).strip() if match else ""


def infer_mode(text: str, explicit: str | None) -> str:
    if explicit:
        return explicit
    if has_any(text, ["RUNTIME SURFACE", "state.yaml", "one active task", "Scout", "Judge", "Worker"]):
        return "runtime"
    if has_any(text, ["LONG-HORIZON INTENT", "PERSISTENT STATE", "SOFT VS HARD BLOCKERS"]):
        return "marathon"
    return "frontier"


def score_bool(name: str, value: bool, notes: list[str], weight: int = 5) -> CategoryScore:
    return CategoryScore(name=name, score=weight if value else 0, max_score=weight, notes=notes)


def score_goal(text: str, path: str = "<memory>", mode: str | None = None) -> LintReport:
    findings: list[Finding] = []
    categories: list[CategoryScore] = []
    low = normalize(text)
    inferred_mode = infer_mode(text, mode)

    if "/goal" not in low:
        findings.append(Finding("MISSING_GOAL_PREFIX", "error", "Prompt does not contain /goal.", "Start the prompt with /goal or explicitly state the generated /goal command."))
        categories.append(score_bool("goal_prefix", False, ["missing /goal"], 3))
    else:
        categories.append(score_bool("goal_prefix", True, ["contains /goal"], 3))

    miss = mission_text(text)
    vague_terms = ("better", "improve", "fix stuff", "make it good", "perfect", "everything")
    mission_ok = bool(miss) and len(miss.split()) >= 6 and not any(t in miss.lower() for t in vague_terms)
    if not mission_ok:
        findings.append(Finding("WEAK_MISSION", "error", "Mission is missing, too short, or vague.", "Define one measurable durable outcome with a clear scope boundary."))
    categories.append(score_bool("mission_singularity", mission_ok, ["mission is concrete" if mission_ok else "mission is vague or missing"], 8))

    criteria_count = count_success_criteria(text)
    criteria_ok = criteria_count >= 2
    if not criteria_ok:
        findings.append(Finding("WEAK_SUCCESS_CRITERIA", "error", f"Found {criteria_count} success criteria.", "Add at least two observable, testable success criteria."))
    categories.append(score_bool("measurable_success_criteria", criteria_ok, [f"criteria_count={criteria_count}"], 8))

    missing_sections = [name for name, headings in CANONICAL_SECTIONS.items() if not has_heading(text, headings)]
    if missing_sections:
        findings.append(Finding("MISSING_CORE_SECTIONS", "error", "Missing core sections: " + ", ".join(missing_sections), "Add the missing execution-contract sections."))
    section_score = max(0, 12 - len(missing_sections) * 2)
    categories.append(CategoryScore("contract_completeness", section_score, 12, ["missing=" + ",".join(missing_sections) if missing_sections else "all core sections present"]))

    evidence_score = sum(1 for term in EVIDENCE_TERMS if term in low)
    evidence_ok = ((has_heading(text, CANONICAL_SECTIONS["evidence_matrix"]) and evidence_score >= 4) or (inferred_mode == "runtime" and has_heading(text, ("ORACLE",)) and "receipt" in low and "evidence" in low))
    if not evidence_ok:
        findings.append(Finding("WEAK_EVIDENCE_MATRIX", "error", "Evidence matrix/oracle/receipt proof is missing or underspecified.", "Include required proof, evidence found, pass/fail/unknown, confidence, source, remaining gap, next action, or a runtime oracle plus receipts."))
    categories.append(CategoryScore("evidence_architecture", min(10, evidence_score + (3 if has_heading(text, CANONICAL_SECTIONS["evidence_matrix"]) else 0)), 10, [f"evidence_terms={evidence_score}"]))

    risk_score = sum(1 for term in RISK_TERMS if term in low)
    risk_ok = risk_score >= 4
    if not risk_ok:
        findings.append(Finding("WEAK_RISK_POLICY", "error", "Risk policy does not clearly bound authority.", "Separate allowed, rollback-required, approval-required, and forbidden actions; runtime Worker tasks should name allowed_files."))
    categories.append(CategoryScore("risk_policy", min(10, risk_score * 2), 10, [f"risk_terms={risk_score}"]))

    verify_score = sum(1 for term in VERIFY_TERMS if term in low)
    verify_ok = has_heading(text, CANONICAL_SECTIONS["verify"]) and verify_score >= 3
    if not verify_ok:
        findings.append(Finding("WEAK_VERIFICATION_ORACLE", "error", "Verification is absent or too weak.", "Name the narrow checks, broader checks, oracle, receipts, and evidence mapping required for DONE."))
    categories.append(CategoryScore("verification_oracle", min(10, verify_score * 2), 10, [f"verify_terms={verify_score}"]))

    terminal_count = sum(1 for state in TERMINAL_STATES if state.lower() in low)
    stop_ok = has_heading(text, CANONICAL_SECTIONS["stop"]) and terminal_count >= 3
    if not stop_ok:
        findings.append(Finding("WEAK_STOP_RULES", "error", "Stop rules or terminal states are missing.", "Define DONE/BLOCKED/UNSAFE/BUDGET EXHAUSTED/NEEDS HUMAN DECISION as applicable."))
    categories.append(CategoryScore("stop_conditions", min(8, terminal_count + (3 if has_heading(text, CANONICAL_SECTIONS["stop"]) else 0)), 8, [f"terminal_states={terminal_count}"]))

    anti_hits = [phrase for phrase in ANTI_PATTERNS if phrase in low]
    if anti_hits:
        findings.append(Finding("ANTI_PATTERNS", "error", "Detected anti-patterns: " + ", ".join(anti_hits), "Replace motivational or unbounded language with evidence, authority, runtime state, and stop rules."))
    categories.append(CategoryScore("anti_patterns", 0 if anti_hits else 7, 7, ["hits=" + ",".join(anti_hits) if anti_hits else "none detected"]))

    if inferred_mode == "marathon":
        score_marathon(text, findings, categories)
    if inferred_mode == "runtime":
        score_runtime(text, findings, categories)

    max_score = sum(c.max_score for c in categories)
    total_score = sum(c.score for c in categories)
    threshold_ratio = 0.84 if inferred_mode == "runtime" else 0.82 if inferred_mode == "marathon" else 0.78
    threshold = int(max_score * threshold_ratio)
    has_errors = any(f.severity == "error" for f in findings)
    passed = total_score >= threshold and not has_errors
    return LintReport(path=path, mode=inferred_mode, score=total_score, max_score=max_score, passed=passed, category_scores=categories, findings=findings)


def score_marathon(text: str, findings: list[Finding], categories: list[CategoryScore]) -> None:
    missing_marathon = [name for name, headings in MARATHON_SECTIONS.items() if not has_heading(text, headings)]
    if missing_marathon:
        findings.append(Finding("MISSING_MARATHON_SECTIONS", "error", "Missing marathon sections: " + ", ".join(missing_marathon), "Add runtime budget, persistent state, blocker policy, failure recovery, phases, and quality ratchet."))
    marathon_score = max(0, 15 - len(missing_marathon) * 3)
    categories.append(CategoryScore("marathon_protocol", marathon_score, 15, ["missing=" + ",".join(missing_marathon) if missing_marathon else "all marathon sections present"]))

    low = text.lower()
    has_state_artifacts = has_any(text, [".goal/", "state.md", "evidence.md", "handoff.md"])
    has_goal_specific_state = has_any(text, GOAL_SPECIFIC_STATE_TERMS)
    uses_goal_files = ".goal/" in low or ".goal" in low
    durable_state_ok = has_state_artifacts and (has_goal_specific_state or not uses_goal_files)
    if not durable_state_ok:
        findings.append(Finding("WEAK_DURABLE_STATE", "error", "Marathon prompt does not specify goal-specific durable state artifacts.", "Use .goal/<goal-id>/... or an equivalent goal-specific durable state structure."))
    shared_root_state = has_any(text, ROOT_GOAL_STATE_TERMS) and not has_goal_specific_state
    if shared_root_state:
        findings.append(Finding("SHARED_GOAL_STATE", "error", "Marathon prompt uses shared root .goal/ state files that can collide across concurrent goals.", "Namespace durable files under .goal/<goal-id>/ and reuse that directory only for continuation of the same goal."))
    durable_notes = ["goal-specific durable state specified" if durable_state_ok else "goal-specific durable state missing"]
    if shared_root_state:
        durable_notes.append("shared root .goal/ files detected")
    categories.append(score_bool("durable_memory", durable_state_ok and not shared_root_state, durable_notes, 7))


def score_runtime(text: str, findings: list[Finding], categories: list[CategoryScore]) -> None:
    missing_runtime = [name for name, headings in RUNTIME_SECTIONS.items() if not has_heading(text, headings)]
    if missing_runtime:
        findings.append(Finding("MISSING_RUNTIME_SECTIONS", "error", "Missing runtime sections: " + ", ".join(missing_runtime), "Add runtime surface, oracle, task rules, receipts/final report, and final audit/stop rules."))
    runtime_section_score = max(0, 15 - len(missing_runtime) * 3)
    categories.append(CategoryScore("runtime_protocol", runtime_section_score, 15, ["missing=" + ",".join(missing_runtime) if missing_runtime else "all runtime sections present"]))

    runtime_hits = sum(1 for term in RUNTIME_TERMS if term in text.lower())
    runtime_ok = runtime_hits >= 6
    if not runtime_ok:
        findings.append(Finding("WEAK_RUNTIME_BOARD", "error", "Runtime-backed goal does not specify enough board machinery.", "Name state.yaml or equivalent board truth, one active task, oracle, receipts, Scout/Judge/Worker or equivalent roles, and allowed_files for writes."))
    categories.append(CategoryScore("runtime_board_truth", min(10, runtime_hits), 10, [f"runtime_terms={runtime_hits}"]))


def render_text(report: LintReport) -> str:
    status = "PASS" if report.passed else "FAIL"
    lines = [f"{status} {report.path}", f"mode: {report.mode}", f"score: {report.score}/{report.max_score}", ""]
    lines.append("Category scores:")
    for category in report.category_scores:
        note = "; ".join(category.notes)
        lines.append(f"- {category.name}: {category.score}/{category.max_score} ({note})")
    if report.findings:
        lines.append("")
        lines.append("Findings:")
        for finding in report.findings:
            lines.append(f"- [{finding.severity}] {finding.code}: {finding.message}")
            lines.append(f"  Recommendation: {finding.recommendation}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint /goal prompts as mission contracts.")
    parser.add_argument("paths", nargs="+", help="Prompt files to lint")
    parser.add_argument("--mode", choices=["compact", "frontier", "marathon", "runtime"], default=None, help="Override inferred mode")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    args = parser.parse_args(argv)

    reports = []
    for raw_path in args.paths:
        path = Path(raw_path)
        text = path.read_text(encoding="utf-8")
        reports.append(score_goal(text, path=str(path), mode=args.mode))

    if args.json:
        print(json.dumps([asdict(r) for r in reports], indent=2))
    else:
        for index, report in enumerate(reports):
            if index:
                print("\n" + "-" * 72 + "\n")
            print(render_text(report))

    return 0 if all(report.passed for report in reports) else 1


if __name__ == "__main__":
    raise SystemExit(main())
