# Marathon /goal Prompt Template

Use this for long-horizon autonomous missions intended to run for many cycles, hours, or days. Prefer it when the user asks for maximum quality, deep autonomous execution, resilient continuation, or prompts that should not stop after a short investigation.

```text
/goal

MISSION:
<one measurable durable objective; one mission only>

LONG-HORIZON INTENT:
This is a sustained autonomous execution mission. Optimize for durable, reviewable, evidence-backed completion, not a short investigation. Continue through normal uncertainty, failed attempts, and multi-step implementation/work unless a hard blocker or explicit budget limit is reached.

TARGET RUNTIME:
Work for up to <N hours/days> or until DONE. Checkpoint every <60-90 minutes or meaningful phase transition>.

MINIMUM PERSISTENCE BEFORE BLOCKED:
Do not return BLOCKED until you have:
- tried at least 3 materially distinct strategies, or explained why fewer are possible
- completed at least 8 meaningful observe-orient-act-verify cycles
- attempted decomposition into smaller safe subgoals
- produced partial evidence, diagnostic artifacts, or a resumable handoff
- confirmed no safe parallel work remains

PREFLIGHT:
Inspect:
- repo/project/workflow instructions
- README / AGENTS / CONTRIBUTING / SECURITY or equivalent docs
- build, test, lint, and package manifests
- relevant source, docs, data, or workflow files
- neighboring implementation patterns
- existing tests, fixtures, examples, or prior artifacts
- known constraints, issues, or TODOs if available

Produce a mission manifest:
- objective
- observed context
- invariants
- risk envelope
- candidate strategies
- selected initial strategy
- success criteria
- verification plan
- expected touched files/systems/artifacts
- rollback or containment plan
- hard blockers
- soft blockers

CONTEXT:
<repo/product/system/workflow state>
<known assumptions>
<relevant files/docs/tests/issues/data/tools>
<prior decisions>
<environment constraints>

PERSISTENT STATE:
Create or update a durable mission state area unless forbidden by the repo/workflow.

Use a goal-specific namespace because multiple `/goal` missions may run at once:

.goal/<goal-id>/
- state.md: current mission state, phase, next action
- evidence.md: success criteria and proof collected
- decisions.md: architectural/workflow decisions and rationale
- failures.md: failed attempts and lessons
- commands.md: commands run, results, known-good checks
- handoff.md: resumable summary for the next agent/session

Choose `<goal-id>` as a stable, filesystem-safe identifier for this mission, preferably `<short-mission-slug>-<YYYYMMDD-HHMM>` or an orchestrator-provided goal/run id. Reuse the same directory on continuation of the same goal.

Do not write shared mission files directly under `.goal/`, such as `.goal/state.md` or `.goal/handoff.md`.

If creating files is inappropriate, maintain the same structure in the final output.

Before context compaction, interruption, phase transition, or final output, update the mission state.

At restart or continuation:
1. Read the persistent state.
2. Re-verify the latest high-impact claims against current files/systems.
3. Resume from the next evidence-closing action.

GROUNDED STRATEGY SEARCH:
Generate up to 3 candidate strategies before implementation.

Each strategy must cite observed evidence and include:
- files/systems/artifacts/tools touched
- verification path
- risk class
- rollback or containment plan
- likely failure mode
- expected first evidence-producing action

Select the strategy with the best tradeoff between:
- success probability
- minimality
- reversibility
- verification clarity
- architectural/workflow fit
- scope control
- ability to continue through soft blockers

Revisit strategy selection after repeated failure, phase transitions, or discovery of new constraints.

RISK + ACTION POLICY:
Classify meaningful actions:

0. read-only inspection
1. reversible local edit
2. costly-to-reverse local edit with rollback
3. external side effect
4. irreversible or production-impacting action

Proceed autonomously with in-scope Class 0-1.
Proceed with Class 2 only with an explicit rollback or containment plan.
Stop or request approval before Class 3-4 unless explicitly authorized.

Allowed without approval:
- <safe reversible local actions>
- <inspection and narrow verification>
- <documentation or test changes directly required by the mission>

Allowed with rollback plan:
- <costly-to-reverse local actions>
- <local dev migrations or generated files if directly required>
- <broader local refactors constrained to the mission>

Approval required:
- <production deploys or production migrations>
- <secrets, credentials, external systems, billing, auth, security, destructive actions>
- <broad dependency upgrades or public exposure changes>

Forbidden:
- <actions never allowed>

SUCCESS CRITERIA:
1. <specific measurable criterion>
2. <specific measurable criterion>
3. <specific measurable criterion>

EVIDENCE MATRIX:
For each criterion, maintain:
- required proof
- evidence found
- pass/fail/unknown
- confidence
- source
- remaining gap
- next action to close the gap

Continue when the next action closes an evidence gap and is permitted by the risk policy.

PHASED EXECUTION:

Phase 1: Reconnaissance
- inspect instructions, architecture/workflow, tests/checks, and relevant files
- identify invariants and risk boundaries
- produce mission map
Exit when touched systems are known, verification strategy is known, and the first implementation or work slice is selected.

Phase 2: Minimal vertical slice
- implement or produce the smallest end-to-end version
- prefer narrow, reversible changes
- add or update narrow tests/checks where relevant
Exit when core behavior works locally or failure is well diagnosed.

Phase 3: Expansion
- handle edge cases
- integrate with neighboring patterns
- broaden test/check coverage
Exit when all main success criteria have evidence or clear remaining evidence gaps.

Phase 4: Hardening
- run broader validation
- inspect diff/output for maintainability and accidental changes
- check security, performance, migration, privacy, or operational risks as relevant
Exit when the solution is reviewable and evidence-backed.

Phase 5: Handoff
- produce final or resumable summary
- include evidence, risks, commands/checks, changed files/artifacts, and next actions

EXECUTION LOOP:
Repeat until a terminal state is reached:

1. OBSERVE
   Read the smallest relevant evidence.

2. ORIENT
   Update uncertainty ranking, state, and evidence gaps.

3. DECIDE
   Choose the next action that most directly closes an evidence gap.

4. ACT
   Execute only actions allowed by the risk policy.

5. VERIFY
   Run the narrowest meaningful check.

6. REFLECT
   If the action failed, record the lesson and change strategy.

7. COMPACT
   Update persistent state and discard redundant context.

8. CONTINUE / STOP
   Continue if any safe evidence-closing action remains.

FAILURE RECOVERY:
Do not repeat the same failed action more than twice without changing inputs, assumptions, or strategy.

When a strategy fails:
- diagnose the failure
- inspect a different evidence source
- narrow the reproduction
- try a smaller subgoal
- search for neighboring patterns
- update assumptions
- continue with the next safest evidence-closing action

SOFT VS HARD BLOCKERS:
Soft blockers do not justify stopping if safe work remains.

Soft blockers include:
- failing tests/checks
- unclear local architecture or workflow
- incomplete docs
- flaky commands
- missing optional environment setup
- ambiguous low-risk implementation detail
- partial verification only

For soft blockers:
- narrow the test/check
- inspect neighboring code/docs/artifacts
- create a minimal reproduction or diagnostic artifact
- try an alternate strategy
- document assumptions
- continue with safe parallel work

Hard blockers include:
- production-impacting action required
- irreversible or destructive action required
- secrets/security/privacy/compliance risk
- external side effect required without approval
- required external dependency unavailable and no safe parallel work remains
- no safe local validation or diagnostic evidence possible

Only hard blockers may produce BLOCKED when no parallel safe work remains.

QUALITY RATCHET:
After the first apparently working solution, do not immediately stop.

Run quality passes:
- Pass 1: make it work.
- Pass 2: make it correct and tested.
- Pass 3: make it maintainable, minimal, and reviewable.

Score the result from 1-5 on:
- correctness
- verification strength
- maintainability
- minimality
- architectural/workflow fit
- risk containment

Any score below 4 requires another improvement cycle or an explicit explanation of why further safe improvement is not possible within budget.

VERIFY:
Use a verification ladder:
1. narrowest relevant test/check
2. touched-module or touched-artifact check
3. related integration check
4. lint/typecheck/build/static validation where relevant
5. broader suite or end-to-end validation where practical
6. manual or diagnostic evidence if automated checks are unavailable

Never claim DONE without mapping success criteria to evidence.
If verification cannot be completed, explain exactly why and provide the closest available evidence.

STOP:
Stop when:
- all success criteria are verified and quality ratchet is satisfied
- the next action does not close an evidence gap
- action exceeds authorization
- hard blocker prevents progress and no safe parallel work remains
- repeated diverse strategies show the mission is not currently achievable
- budget is exhausted after producing a resumable handoff
- scope expansion is required to satisfy the mission

Do not stop merely because:
- the task is large
- the first approach failed
- tests/checks initially failed
- documentation is incomplete
- multiple files/artifacts must be touched
- a reversible assumption is required
- one branch is blocked but safe parallel work remains

TERMINAL STATE:
Return exactly one:
- DONE
- PARTIAL DONE
- BLOCKED
- UNSAFE
- BUDGET EXHAUSTED
- NEEDS HUMAN DECISION

OUTPUT:
Return:
- terminal state
- concise summary
- phase reached
- selected strategy and why
- evidence matrix
- files/artifacts changed
- commands/checks run
- verification results
- quality-ratchet scores
- failures and lessons
- risk/rollback notes
- unresolved uncertainties
- exact next recommended actions
- location/content of persistent handoff

SKILL EXTRACTION:
After DONE only:
- list reusable procedures discovered
- suggest future automations/templates
- do not implement generalized tooling unless separately requested
```
