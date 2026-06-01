from pathlib import Path
import importlib.util
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("lint_goal", ROOT / "tools" / "lint_goal.py")
lint_goal = importlib.util.module_from_spec(SPEC)
sys.modules["lint_goal"] = lint_goal
SPEC.loader.exec_module(lint_goal)


def load(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


class GoalLintTests(unittest.TestCase):
    def test_bad_vague_goal_fails(self):
        report = lint_goal.score_goal(load("examples/bad/vague-goal.md"), "vague-goal.md")
        self.assertFalse(report.passed)
        self.assertTrue(any(f.code == "WEAK_MISSION" for f in report.findings))
        self.assertTrue(any(f.code == "WEAK_VERIFICATION_ORACLE" for f in report.findings))

    def test_bad_unbounded_goal_fails_on_anti_patterns(self):
        report = lint_goal.score_goal(load("examples/bad/unbounded-marathon.md"), "unbounded-marathon.md", mode="marathon")
        self.assertFalse(report.passed)
        self.assertTrue(any(f.code == "ANTI_PATTERNS" for f in report.findings))
        self.assertTrue(any(f.code == "MISSING_MARATHON_SECTIONS" for f in report.findings))

    def test_good_frontier_goal_passes(self):
        report = lint_goal.score_goal(load("examples/good/frontier-repo-goal.md"), "frontier-repo-goal.md", mode="frontier")
        self.assertTrue(report.passed, [f.code for f in report.findings])
        self.assertGreaterEqual(report.score / report.max_score, 0.78)

    def test_good_marathon_goal_passes(self):
        report = lint_goal.score_goal(load("examples/good/marathon-repo-goal.md"), "marathon-repo-goal.md", mode="marathon")
        self.assertTrue(report.passed, [f.code for f in report.findings])
        self.assertGreaterEqual(report.score / report.max_score, 0.82)

    def test_marathon_goal_rejects_shared_root_goal_state(self):
        text = load("examples/good/marathon-repo-goal.md").replace(
            """Create or update a goal-specific state directory unless forbidden by repository rules. Use an orchestrator-provided goal/run id if available; otherwise use a short filesystem-safe mission slug plus timestamp, for example .goal/reporting-refactor-20260529-1430/.
- .goal/<goal-id>/state.md for current phase and next action
- .goal/<goal-id>/evidence.md for success criteria and proof collected
- .goal/<goal-id>/decisions.md for architectural decisions and rationale
- .goal/<goal-id>/failures.md for failed attempts and lessons
- .goal/<goal-id>/commands.md for commands run and results
- .goal/<goal-id>/handoff.md for resumable summary
Do not write shared state directly under .goal/, such as .goal/state.md or .goal/handoff.md, because multiple /goal missions may run at once.""",
            """Create or update .goal/ unless forbidden by repository rules:
- .goal/state.md for current phase and next action
- .goal/evidence.md for success criteria and proof collected
- .goal/decisions.md for architectural decisions and rationale
- .goal/failures.md for failed attempts and lessons
- .goal/commands.md for commands run and results
- .goal/handoff.md for resumable summary""",
        )
        report = lint_goal.score_goal(text, "old-marathon-repo-goal.md", mode="marathon")
        self.assertFalse(report.passed)
        self.assertTrue(any(f.code == "SHARED_GOAL_STATE" for f in report.findings))

    def test_json_shape_is_stable(self):
        report = lint_goal.score_goal(load("examples/good/frontier-repo-goal.md"), "frontier-repo-goal.md", mode="frontier")
        payload = lint_goal.asdict(report)
        self.assertEqual(set(payload), {"path", "mode", "score", "max_score", "passed", "category_scores", "findings"})


if __name__ == "__main__":
    unittest.main()
