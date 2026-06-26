import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPILE = ROOT / "tools" / "compile_goal_runtime.py"
LINT = ROOT / "tools" / "lint_goal.py"


def run(*args, cwd=None):
    return subprocess.run([sys.executable, *map(str, args)], cwd=cwd, text=True, capture_output=True)


def test_compile_goal_runtime_from_mission(tmp_path):
    result = run(COMPILE, "--mission", "Implement password reset with token validation and regression tests.", "--out", tmp_path)
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    goal_dir = Path(payload["goal_dir"])
    assert (goal_dir / "goal.md").exists()
    assert (goal_dir / "state.yaml").exists()
    assert (goal_dir / "notes").is_dir()
    text = (goal_dir / "state.yaml").read_text()
    assert "active_task: T001" in text
    assert "final_audit_required_for_done: true" in text


def test_compile_goal_runtime_from_spec_and_lint(tmp_path):
    spec = {
        "title": "Password Reset",
        "mission": "Implement password reset so users can request a reset email and set a new password through a valid token.",
        "oracle": {
            "signal": "Auth tests and a manual walkthrough prove reset works.",
            "final_proof": "Final audit maps passing checks to reset request and reset completion criteria."
        },
        "success_criteria": [
            "A user can request a password reset email for an existing account.",
            "A user can set a new password with a valid unexpired token."
        ],
        "verify": ["npm test -- auth", "npm run typecheck"],
        "allowed_without_approval": ["Local code and test edits inside allowed_files."],
        "approval_required": ["Production deploys and email-provider credential changes."],
        "forbidden": ["Skipping tests and claiming DONE from inspection only."]
    }
    spec_path = tmp_path / "spec.json"
    spec_path.write_text(json.dumps(spec), encoding="utf-8")

    result = run(COMPILE, "--spec", spec_path, "--out", tmp_path)
    assert result.returncode == 0, result.stderr
    goal_md = tmp_path / "password-reset" / "goal.md"
    assert goal_md.exists()

    lint = run(LINT, "--mode", "runtime", goal_md)
    assert lint.returncode == 0, lint.stdout + lint.stderr
    assert "PASS" in lint.stdout
    assert "mode: runtime" in lint.stdout
