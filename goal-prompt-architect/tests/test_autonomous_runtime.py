"""Exercise the user-facing compiler contract through its CLI."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class AutonomousRuntimeTests(unittest.TestCase):
    def compile(self, directory, *args):
        return subprocess.run(
            [sys.executable, str(ROOT / 'tools/compile_goal_runtime.py'),
             '--out', str(directory), *args], text=True, capture_output=True,
        )

    def test_default_contract_enables_parallel_work_and_keeps_safety_boundaries(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.compile(directory, '--mission', 'Fix assessment assignment with verified UI and backend behavior.')
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            goal = Path(payload['goal_md']).read_text()
            state = Path(payload['state_yaml']).read_text()
            self.assertIn('one_active_task: false', state)
            self.assertIn('one_writer_per_scope: true', state)
            self.assertIn('depends_on: [T001]', state)
            self.assertIn('depends_on: [T002]', state)
            self.assertNotIn('select exactly one active task', goal)
            self.assertIn('without per-task approval', goal)
            self.assertIn('without waiting for unrelated lanes', goal)
            self.assertIn('Only actions outside existing user authority', goal)
            self.assertIn('final_audit_required_for_done: true', state)
            lint = subprocess.run(
                [sys.executable, str(ROOT / 'tools/lint_goal.py'), '--mode', 'runtime', payload['goal_md']],
                text=True, capture_output=True,
            )
            self.assertEqual(lint.returncode, 0, lint.stdout + lint.stderr)

    def test_explicit_user_restrictions_are_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            spec = Path(directory) / 'spec.json'
            spec.write_text(json.dumps({
                'mission': 'Audit assessment permissions and return evidence without editing code.',
                'constraints': ['Audit only. Do not edit implementation files.'],
                'approval_required': ['Ask before deployment to the shared staging environment.'],
                'forbidden': ['Do not change role grants.'],
            }))
            result = self.compile(directory, '--spec', str(spec))
            self.assertEqual(result.returncode, 0, result.stderr)
            goal = Path(json.loads(result.stdout)['goal_md']).read_text()
            for expected in ['Audit only. Do not edit implementation files.',
                             'Ask before deployment to the shared staging environment.',
                             'Do not change role grants.']:
                self.assertIn(expected, goal)

    def test_existing_mission_is_not_overwritten_by_new_defaults(self):
        with tempfile.TemporaryDirectory() as directory:
            args = ('--mission', 'Implement verified assessment assignment.')
            first = self.compile(directory, *args)
            self.assertEqual(first.returncode, 0, first.stderr)
            state = Path(json.loads(first.stdout)['state_yaml'])
            before = state.read_bytes()
            second = self.compile(directory, *args)
            self.assertNotEqual(second.returncode, 0)
            self.assertIn('refusing to overwrite', second.stderr)
            self.assertEqual(state.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
