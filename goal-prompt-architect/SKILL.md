---
name: goal-prompt-architect
description: create, audit, and improve high-performance /goal prompts for autonomous coding agents and long-running agent workflows. use when the user asks for a /goal prompt, goal prompt template, codex/claude code/hermes mission prompt, long-running agent prompt, multi-day autonomous execution prompt, marathon agent prompt, repo-specific autonomous task prompt, or wants to transform a vague task into a measurable, risk-bounded, verification-driven execution contract.
---

# Goal Prompt Architect

## Core Rule

Generate `/goal` prompts as autonomous execution contracts, not motivational instructions. Always optimize for: one measurable mission, bounded authority, grounded strategy, uncertainty reduction, verification evidence, memory/progress discipline, and clean stopping conditions.

For long-running or high-ambition goals, optimize for sustained bounded progress, not early stopping. Distinguish hard blockers from soft blockers, require durable progress memory, define explicit time/cycle budgets, include recovery policies for failed attempts, and require quality ratchets after initial success.

## Workflow

1. **Classify the request**
   - **Repo/software task**: inspect any provided repo/files/docs first when available. Include concrete commands, paths, worktree rules, migrations, and validation.
   - **Business/ops/research task**: adapt the same architecture to documents, tools, datasets, or workflows.
   - **Prompt-only request**: produce a reusable `/goal` prompt without executing the underlying mission.
   - **Audit/improvement request**: critique the provided prompt, then provide a revised version.
   - **Marathon/autonomous run request**: use `references/marathon-template.md` when the user asks for multi-hour, multi-day, maximum-quality, resilient, or deeply autonomous execution.

2. **Gather missing essentials only when needed**
   Ask concise follow-up questions only if the mission, expected output, or verification standard is impossible to infer. Prefer making safe assumptions and marking them in the prompt over asking open-ended questions.

3. **Create a mission-grade prompt**
   Use `references/compact-template.md` for simple tasks or when the user asks for brevity. Use `references/frontier-template.md` for complex or high-risk single-session work. Use `references/marathon-template.md` for multi-hour/multi-day, high-ambition, maximum-quality, or interruption-resilient autonomous work.

4. **Adapt to context**
   Pull in domain-specific sections from `references/domain-adaptations.md` when relevant.

5. **Quality-check before final output**
   Run the checklist in this file before answering. If the prompt fails any mandatory item, revise it.

## Template Selection

- **Compact**: low-risk, narrow, short-lived tasks where a concise execution contract is enough.
- **Frontier**: complex or high-risk tasks that need strategy search, evidence mapping, risk controls, and strong stopping conditions.
- **Marathon**: long-horizon tasks intended to run for many cycles, hours, or days. Choose this when the user asks for best results, deep autonomy, persistent execution, repo-wide work, large implementation missions, or prompts that should not stop after a short investigation.

If unsure between frontier and marathon, choose marathon when the user emphasizes duration, resilience, ambition, or quality; choose frontier when the user emphasizes caution, bounded scope, or a single-session deliverable.

## Mandatory Design Principles

Every serious `/goal` prompt must include:

- **Single mission**: one durable objective, not a bundle of unrelated tasks.
- **Measurable success criteria**: observable, testable, and scoped.
- **Grounded preflight**: inspect context before acting; do not invent architecture.
- **Risk envelope**: allowed, forbidden, and approval-required actions.
- **Action classification**: read-only, reversible local edit, costly-to-reverse edit, external side effect, irreversible/production-impacting action.
- **Evidence matrix**: each success criterion maps to required proof and current evidence.
- **Execution loop**: observe, orient, decide, act, verify, reflect, compact, continue or stop.
- **Memory protocol**: working memory, episodic ledger, semantic mission memory for long runs.
- **Stop rules**: halt on done, unsafe action, high-impact ambiguity, budget exhaustion, or genuine hard blocker.
- **Continuation rules**: continue through ordinary uncertainty, first failures, incomplete docs, and reversible assumptions when a safe evidence-producing action remains.
- **Terminal state**: DONE, PARTIAL DONE, BLOCKED, UNSAFE, BUDGET EXHAUSTED, or NEEDS HUMAN DECISION.
- **Output contract**: summary, evidence, changed files/artifacts, checks run, risks, and follow-ups.

Marathon prompts must additionally include:

- **Explicit runtime or cycle budget**: target duration, checkpoint cadence, minimum effort before BLOCKED.
- **Soft vs hard blocker policy**: soft blockers trigger recovery; hard blockers can halt only when no safe parallel work remains.
- **Persistent state protocol**: goal-specific durable handoff files or equivalent sections for state, evidence, decisions, failures, commands, and next actions. If writing under `.goal/`, always namespace files under a unique current-goal directory such as `.goal/<goal-id>/`, never directly in `.goal/`.
- **Phase gates**: reconnaissance, minimal vertical slice, expansion, hardening, and handoff or equivalent phases.
- **Failure recovery**: diverse strategy changes, decomposition, minimal reproductions, and anti-thrashing rules.
- **Quality ratchet**: after the first working solution, require correctness, test, maintainability, and reviewability passes.

## Construction Procedure

### Step 1: Define the mission

Convert vague user intent into one measurable mission:

- Bad: `make the app better`
- Better: `implement password reset so users can request a reset email, set a new password through a valid token, and pass auth tests without changing the existing login flow`

If there are multiple missions, split them or make the prompt explicitly choose one.

### Step 2: Add context and inspection instructions

Include known repo/product/workflow facts. For software repos, include:

- app/service/package layout
- languages/frameworks
- files/docs to inspect first
- setup, test, build, lint commands
- existing rules such as AGENTS.md, CONTRIBUTING.md, SECURITY.md
- migration or deployment docs

For unknown repos, instruct the agent to inspect these before implementation.

### Step 3: Define risk and authority

Always separate:

- **Allowed without approval**: safe, reversible, local, in-scope actions.
- **Allowed with rollback plan**: costly-to-reverse local changes.
- **Approval required**: production, secrets, external side effects, destructive ops, broad dependency upgrades, migrations, auth/security/billing/payment changes.
- **Forbidden**: anything the user/org explicitly disallows.

Use stricter defaults for regulated, clinical, legal, financial, production, or privacy-sensitive tasks.

### Step 4: Require grounded strategy search

For non-trivial work, require up to 3 candidate strategies. Each must cite observed evidence, expected files/systems touched, verification path, risk class, rollback plan, and failure mode. The agent selects the strategy with best success probability, minimality, reversibility, verification clarity, architectural fit, and scope control.

For marathon prompts, strategy search must be revisited after repeated failure, phase changes, or discovery of new architecture constraints.

### Step 5: Build the evidence matrix

For every success criterion, specify:

- required proof
- evidence found
- pass/fail/unknown
- confidence
- source
- remaining gap
- next action to close the gap

The agent must continue when the next action closes an evidence gap and is permitted by the risk envelope. Do not make an incomplete evidence matrix a reason to stop when safe evidence-producing work remains.

### Step 6: Add execution loop and memory

Use the loop to control long runs. For multi-hour or multi-day goals, include goal-specific persistent state and memory compaction every checkpoint, phase transition, or few meaningful steps. Require stale-memory re-verification for high-impact actions.

When the prompt creates `.goal/` files, require a unique state directory for the current goal because users may run multiple `/goal` missions at once. Prefer `.goal/<goal-id>/`, where `<goal-id>` is a stable, filesystem-safe mission slug plus a timestamp or run id, for example `.goal/password-reset-20260529-1430/`.

If an orchestrator provides a goal/run id, use it. Do not write shared state files such as `.goal/state.md` or `.goal/handoff.md`.

### Step 7: Add verification commands

Use actual known commands when available. If unknown, tell the agent to discover and run narrow checks first, then broader checks. Do not include fake commands as if certain.

Use a verification ladder: narrow check, touched-module check, related integration check, lint/typecheck/build, broader suite where practical, and manual or diagnostic evidence when automated verification is unavailable.

### Step 8: Add stop, continuation, and output contracts

Make stopping explicit, but do not over-trigger early stopping. A `/goal` prompt should prevent endless polishing and scope creep while still continuing through ordinary difficulty.

For marathon prompts, include minimum persistence before BLOCKED, hard blocker definitions, soft blocker recovery, checkpoint cadence, goal-specific state directory requirements, and resumable handoff requirements.

## Response Style

When returning a `/goal` prompt:

- Put the final prompt in a single copyable fenced code block.
- Precede it with a short note only if needed to explain assumptions.
- Avoid long essays unless the user asks for rationale or debate.
- If the user asked for multiple versions, label them clearly: compact, standard/frontier, marathon, repo-specific.
- Do not claim you inspected a repo, file, or docs unless you actually did.

## Quality Checklist

Before finalizing, verify the prompt answers:

1. What exact outcome must be achieved?
2. What context must be inspected first?
3. What must not be changed?
4. What actions require approval?
5. What are the measurable success criteria?
6. What evidence proves each criterion?
7. What loop governs execution?
8. How are failures and memory handled?
9. When must the agent stop?
10. What must the final report contain?

For marathon prompts, also verify:

11. Does the prompt distinguish soft blockers from hard blockers?
12. Does it require continuation through ordinary uncertainty?
13. Does it define explicit runtime or cycle budgets?
14. Does it require persistent resumable state in a goal-specific namespace?
15. Does it include failure recovery policies?
16. Does it require quality passes after the first working solution?
17. Does it allow safe parallel work when one branch is blocked?
18. Does it prevent repeated identical failed attempts?
19. Does it include checkpoint and handoff behavior for interruptions?
20. Does it prevent long-running scope creep while preserving useful persistence?

If any answer is missing, revise the prompt.

## Common Anti-Patterns to Remove

- `make no mistakes`
- `make it perfect`
- `use every tool`
- `do whatever it takes`
- `keep going until everything is fixed`
- broad rewrites when minimal edits suffice
- verification postponed until the very end
- open-ended clarification questions inside the running goal
- unbounded production/deployment/secrets access
- success criteria with no proof path
- stopping merely because the first strategy failed
- stopping merely because tests initially failed
- stopping because documentation is incomplete when code can be inspected
- repeating the same failed action without changing strategy
- persistent state files that become a substitute for real verification
- shared `.goal/` files that collide when multiple `/goal` missions run at once

## References

- Use `references/marathon-template.md` for multi-hour, multi-day, maximum-quality, or resilient autonomous prompts.
- Use `references/frontier-template.md` for complex or high-risk single-session prompts.
- Use `references/compact-template.md` for lightweight prompts.
- Use `references/domain-adaptations.md` for repo, product, data, research, and operations variants.
