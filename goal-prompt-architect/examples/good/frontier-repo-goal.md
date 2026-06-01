/goal

MISSION:
Implement password reset for the existing authentication flow so users can request a reset email, set a new password with a valid token, and keep the existing login behavior unchanged.

PREFLIGHT:
Before implementation, inspect README, AGENTS, CONTRIBUTING, SECURITY, package manifests, auth routes, user model, mailer utilities, existing tests, and neighboring authentication patterns. Produce a mission manifest with observed context, candidate strategies, selected strategy, success criteria, evidence plan, risk envelope, expected touched files, rollback plan, and stop conditions.

CONTEXT:
Work only in the local repository. Preserve current login, signup, session, and authorization behavior. If commands are unknown, discover narrow test, lint, typecheck, and build commands from repository manifests before running broad checks.

GROUNDED STRATEGY SEARCH:
Generate up to 3 candidate strategies. Each strategy must cite observed evidence and include files or systems touched, verification path, risk class, rollback or containment plan, likely failure mode, and the first evidence-producing action. Select the strategy with the best tradeoff between success probability, minimality, reversibility, verification clarity, architectural fit, and scope control. Revisit the selected strategy after repeated failure or newly discovered constraints.

RISK + ACTION POLICY:
Classify meaningful actions as read-only, local reversible edit, costly-to-reverse local edit, external side effect, or irreversible/production-impacting action.

Allowed without approval:
- read-only inspection
- reversible local code and test edits directly needed for password reset
- narrow local verification commands

Allowed with rollback plan:
- local dev schema additions if the repository already uses migrations and rollback notes are included

Approval required:
- production deploys or production migrations
- secrets, credentials, external email provider changes, billing, destructive actions, or public exposure changes

Forbidden:
- changing unrelated auth behavior
- weakening password hashing, session security, or authorization checks

SUCCESS CRITERIA:
1. Users can request a reset token through the existing auth UI or API without leaking whether an email exists.
2. Users can set a new password with a valid unexpired token and cannot reuse invalid, expired, or already-used tokens.
3. Existing login and signup tests still pass or equivalent evidence explains any unavailable check.

EVIDENCE MATRIX:
For each criterion, maintain required proof, evidence found, pass/fail/unknown, confidence, source, remaining gap, and next action to close the gap.

EXECUTION LOOP:
Repeat observe, orient, decide, act, verify, reflect, compact, and continue or stop. Choose the next action that most directly closes an evidence gap and is permitted by the risk envelope.

MEMORY:
Maintain working memory, an episodic ledger, and semantic mission memory. Each durable memory must include claim, source/provenance, confidence, scope, and type. Re-verify stale or high-impact memory before relying on it.

VERIFY:
Run the narrowest relevant tests first, then touched-module tests, lint or typecheck, build, and broader validation where practical. Map every success criterion to evidence. If verification cannot be completed, explain exactly why and provide the closest available evidence.

STOP:
Stop when all success criteria are verified, the next action does not close an evidence gap, action exceeds authorization, high-impact ambiguity cannot be resolved by inspection, repeated diverse failure leaves no safe alternate, a budget gate triggers, or scope expansion is required. Do not stop merely because the first approach failed, tests initially failed, documentation is incomplete, or a reversible assumption is required.

TERMINAL STATE:
Return exactly one: DONE, PARTIAL DONE, BLOCKED, UNSAFE, BUDGET EXHAUSTED, or NEEDS HUMAN DECISION.

OUTPUT:
Return terminal state, concise summary, selected strategy and why, evidence matrix, files changed, commands/checks run, verification results, failures and lessons, risk/rollback notes, unresolved uncertainties, and recommended follow-ups.
