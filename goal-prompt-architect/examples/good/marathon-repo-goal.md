/goal

MISSION:
Refactor the reporting pipeline into a testable module boundary while preserving existing report outputs and producing evidence-backed tests for the migrated behavior.

LONG-HORIZON INTENT:
This is a sustained autonomous execution mission. Optimize for durable, reviewable, evidence-backed completion, not a short investigation. Continue through normal uncertainty, failed attempts, and multi-step implementation unless a hard blocker or explicit budget limit is reached.

TARGET RUNTIME:
Work for up to 8 hours or until DONE. Checkpoint every 60 to 90 minutes or at every meaningful phase transition.

MINIMUM PERSISTENCE BEFORE BLOCKED:
Do not return BLOCKED until at least 3 materially distinct strategies have been tried or ruled out, at least 8 meaningful observe-orient-act-verify cycles have been completed, decomposition into smaller safe subgoals has been attempted, partial evidence or diagnostic artifacts have been produced, and no safe parallel work remains.

PREFLIGHT:
Inspect README, AGENTS, CONTRIBUTING, SECURITY, build/test/lint manifests, reporting entrypoints, existing fixtures, neighboring tests, CI workflow, known TODOs, and relevant issues if available. Produce a mission manifest with objective, observed context, invariants, risk envelope, candidate strategies, selected strategy, success criteria, verification plan, expected touched files, rollback plan, hard blockers, and soft blockers.

CONTEXT:
Work only in the local repository. Preserve report output semantics, public APIs, existing fixtures, unrelated dirty files, and any documented agent instructions. Discover commands from repository manifests instead of inventing them.

PERSISTENT STATE:
Create or update a goal-specific state directory unless forbidden by repository rules. Use an orchestrator-provided goal/run id if available; otherwise use a short filesystem-safe mission slug plus timestamp, for example .goal/reporting-refactor-20260529-1430/.
- .goal/<goal-id>/state.md for current phase and next action
- .goal/<goal-id>/evidence.md for success criteria and proof collected
- .goal/<goal-id>/decisions.md for architectural decisions and rationale
- .goal/<goal-id>/failures.md for failed attempts and lessons
- .goal/<goal-id>/commands.md for commands run and results
- .goal/<goal-id>/handoff.md for resumable summary
Do not write shared state directly under .goal/, such as .goal/state.md or .goal/handoff.md, because multiple /goal missions may run at once.
At restart, read persistent state, re-verify high-impact claims, and resume from the next evidence-closing action.

GROUNDED STRATEGY SEARCH:
Generate up to 3 candidate strategies before implementation. Each strategy must cite observed evidence and include touched files/systems/artifacts/tools, verification path, risk class, rollback plan, likely failure mode, and expected first evidence-producing action. Select the strategy with the best tradeoff between success probability, minimality, reversibility, verification clarity, architecture fit, scope control, and ability to continue through soft blockers. Revisit strategy after repeated failure, phase transitions, or new constraints.

RISK + ACTION POLICY:
Classify actions as read-only inspection, reversible local edit, costly-to-reverse local edit with rollback, external side effect, or irreversible/production-impacting action.

Allowed without approval:
- read-only inspection
- reversible local source, docs, fixture, and test edits directly required by the mission
- narrow local verification commands

Allowed with rollback plan:
- broader local refactors constrained to the reporting boundary
- generated files if the repository already expects them and rollback notes are included

Approval required:
- production deploys, production migrations, secrets, credentials, external systems, billing, auth, security, destructive actions, broad dependency upgrades, or public exposure changes

Forbidden:
- changing report semantics without explicit evidence and documentation
- modifying unrelated modules for cosmetic reasons
- deleting source data or fixtures without approval

SUCCESS CRITERIA:
1. Reporting logic has a clear module boundary with minimal, reviewable diffs and no unrelated changes.
2. Existing report outputs are preserved or intentional differences are documented with evidence and approval need.
3. Narrow and broader verification checks provide evidence for migrated behavior, unchanged outputs, and maintainability.

EVIDENCE MATRIX:
For each criterion, maintain required proof, evidence found, pass/fail/unknown, confidence, source, remaining gap, and next action to close the gap. Continue when the next action closes an evidence gap and is permitted by the risk policy.

PHASED EXECUTION:
Phase 1: Reconnaissance. Inspect instructions, architecture, tests, and relevant files. Exit when touched systems and verification strategy are known.
Phase 2: Minimal vertical slice. Move the smallest end-to-end slice and add or update narrow tests. Exit when core behavior works locally or failure is diagnosed.
Phase 3: Expansion. Handle edge cases, integrate neighboring patterns, and broaden tests. Exit when all main criteria have evidence or clear gaps.
Phase 4: Hardening. Run broader validation, inspect diff, and check security/performance/operational risks. Exit when reviewable and evidence-backed.
Phase 5: Handoff. Produce final or resumable summary with evidence, risks, checks, changed files, and next actions.

EXECUTION LOOP:
Repeat observe, orient, decide, act, verify, reflect, compact, and continue or stop. Update uncertainty ranking, state, and evidence gaps. Choose the next action that closes an evidence gap. Execute only actions allowed by the risk policy. Run the narrowest meaningful check. Record failures and change strategy. Update persistent state before compaction, phase transition, interruption, or final output.

FAILURE RECOVERY:
Do not repeat the same failed action more than twice without changing inputs, assumptions, or strategy. When a strategy fails, diagnose the failure, inspect a different evidence source, narrow the reproduction, try a smaller subgoal, search neighboring patterns, update assumptions, and continue with the next safest evidence-closing action.

SOFT VS HARD BLOCKERS:
Soft blockers include failing tests, unclear local architecture, incomplete docs, flaky commands, missing optional environment setup, ambiguous low-risk implementation details, and partial verification. For soft blockers, narrow the check, inspect neighboring code/docs, create a diagnostic artifact, try an alternate strategy, document assumptions, and continue safe parallel work.

Hard blockers include production-impacting actions, irreversible/destructive actions, secrets/security/privacy/compliance risk, external side effects without approval, unavailable required external dependencies with no safe parallel work, or no safe validation/diagnostic evidence possible. Only hard blockers may produce BLOCKED when no parallel safe work remains.

QUALITY RATCHET:
After the first apparently working solution, do not immediately stop. Run quality passes: make it work, make it correct and tested, then make it maintainable, minimal, and reviewable. Score correctness, verification strength, maintainability, minimality, architectural fit, and risk containment from 1 to 5. Any score below 4 requires another improvement cycle or an explanation of why further safe improvement is not possible within budget.

VERIFY:
Use a verification ladder: narrowest relevant test/check, touched-module check, related integration check, lint/typecheck/build/static validation, broader suite or end-to-end validation where practical, and manual or diagnostic evidence if automated checks are unavailable. Never claim DONE without mapping success criteria to evidence.

STOP:
Stop when all success criteria are verified and the quality ratchet is satisfied, the next action does not close an evidence gap, action exceeds authorization, a hard blocker prevents progress and no safe parallel work remains, repeated diverse strategies show the mission is not currently achievable, budget is exhausted after resumable handoff, or scope expansion is required. Do not stop merely because the task is large, the first approach failed, tests initially failed, docs are incomplete, multiple files are touched, a reversible assumption is required, or one branch is blocked while safe parallel work remains.

TERMINAL STATE:
Return exactly one: DONE, PARTIAL DONE, BLOCKED, UNSAFE, BUDGET EXHAUSTED, or NEEDS HUMAN DECISION.

OUTPUT:
Return terminal state, concise summary, phase reached, selected strategy and why, evidence matrix, files/artifacts changed, commands/checks run, verification results, quality-ratchet scores, failures and lessons, risk/rollback notes, unresolved uncertainties, exact next recommended actions, and location/content of persistent handoff.
