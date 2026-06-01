# Example: Software Repository /goal Prompt

```text
/goal

MISSION:
Implement password reset end-to-end so users can request a reset email, open a valid token link, set a new password, and log in with the new password, without changing the existing login flow, session model, or auth provider architecture.

PREFLIGHT:
Before implementation, inspect and summarize:
- README / AGENTS / CONTRIBUTING / SECURITY docs
- package/build/test manifests
- auth routes, models, services, and tests
- email or notification infrastructure
- token/session storage patterns
- relevant migrations
- existing UI form patterns

Produce a mission manifest with observed context, candidate strategies, selected strategy, success criteria, evidence plan, risk envelope, expected touched files, rollback plan, and stop conditions.

GROUNDED STRATEGY SEARCH:
Generate up to 3 implementation strategies grounded in observed repo evidence.
For each strategy include touched files/systems, verification path, risk class, rollback plan, and likely failure mode.
Select the smallest strategy that fits existing architecture and can be verified.

RISK + ACTION POLICY:
Proceed autonomously only with read-only and local reversible edits.
Proceed with local schema changes only if the repo already has a migration pattern, the migration is additive/reversible, rollback notes are included, and no production migration is run.
Stop before production deploys, production migrations, secrets, external email-provider changes, auth-provider reconfiguration, destructive deletes, or broad dependency upgrades.

SUCCESS CRITERIA:
1. User can request a password reset for an existing account.
2. A reset token is generated, stored safely, expires, and cannot be reused.
3. User can set a new password through a valid token.
4. Invalid, expired, and reused tokens fail safely.
5. Existing login/session behavior still works.
6. Relevant tests pass and verification evidence is recorded.

EVIDENCE MATRIX:
For each criterion, maintain required proof, evidence found, pass/fail/unknown, confidence, source, and remaining gap.

EXECUTION LOOP:
Repeat: observe smallest relevant evidence, update uncertainty ranking, choose the next action that closes the largest evidence gap, act within the risk policy, verify narrowly, reflect on failures, compact memory, and continue only if the next action closes an evidence gap.

VERIFY:
Run narrow auth/password-reset tests first, then relevant lint/typecheck/build/test commands discovered from the repo.
If verification cannot be completed, explain exactly why and provide closest available evidence.

STOP:
Stop when all success criteria are verified, the next action does not close an evidence gap, action exceeds authorization, ambiguity is high-impact, repeated failure indicates the selected strategy is wrong, or scope expansion is required.

TERMINAL STATE:
Return exactly one: DONE, BLOCKED, UNSAFE, BUDGET EXHAUSTED, or NEEDS HUMAN DECISION.

OUTPUT:
Return terminal state, selected strategy, evidence matrix, files changed, checks run, verification results, failures and lessons, risk/rollback notes, unresolved uncertainties, and recommended follow-ups.
```
