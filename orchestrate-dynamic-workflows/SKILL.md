---
name: orchestrate-dynamic-workflows
description: Design, run, or emulate dynamic multi-agent workflows for large audits, broad research, migrations, cross-checking, implementation planning, adversarial review, or any task that benefits from choosing specialized agents, spawning subagents, synthesizing their work, and preserving a repeatable orchestration plan. Use when a user asks for dynamic workflows, agent teams, subagents, council/debate style analysis, parallel agent work, workflow scripts, or "elite" agent orchestration.
---

# Orchestrate Dynamic Workflows

## Core Rule

Move coordination out of fragile chat context and into an explicit orchestration plan. Use agents for bounded work, a reducer for synthesis, and an adversarial verifier before conclusions or edits are accepted.

If the current environment has native dynamic workflows, generate or use one. If it only has subagents, emulate the workflow manually with parallel delegation and an explicit reduce step. If neither exists, run the phases sequentially in the main agent while preserving the same contracts.

For Claude Code-specific behavior, read [references/claude-code-dynamic-workflows.md](references/claude-code-dynamic-workflows.md) when the user asks about Claude Code, workflow scripts, `/workflows`, `/deep-research`, or saving reusable workflow commands.

## Mode Selector

Use this decision sequence before spawning agents:

1. **Single-agent path**: Use for narrow edits, one-file questions, or tasks where decomposition adds coordination cost.
2. **Subagent path**: Use for 2-8 independent investigations, review passes, or specialist opinions where the main agent can hold the synthesis.
3. **Dynamic workflow path**: Use for dozens of files, broad codebase audits, large migrations, many-source research, repeated processes, or tasks requiring independent critique, voting, and resumable state.
4. **Ask first**: Stop and ask if the workflow would touch production systems, secrets, real private data, clinical/regulated decisions, destructive operations, or unclear user intent.

Prefer the smallest mode that can preserve correctness. Scale up when independent partitions, evidence requirements, or verification depth exceed what one conversation can reliably track.

Before execution, identify the available orchestration primitive:

- **Native workflow runtime**: Use when the environment exposes workflow scripts, resumable background runs, or saved workflow commands.
- **Subagent tool only**: Emulate the workflow with explicit parallel delegation, a reducer pass, and a verifier pass.
- **No delegation tool**: Keep the same phases, but perform them sequentially and say that the workflow was simulated in-process.

If the tool surface is unclear, inspect available tools or state the assumption before proceeding.

## Council Of Five

For important workflow design, simulate these five roles as decision lenses. Do not impersonate real people or claim actual private views; use the roles as archetypes.

1. **Research lead**: Define the intellectual decomposition. Ask what must be independently explored, what hypotheses compete, and what evidence would change the answer.
2. **Systems orchestrator**: Turn the plan into phases, budgets, concurrency, retry rules, result schemas, and resume points.
3. **Product/operator**: Protect user time and cost. Decide whether the workflow is worth it, what progress should be visible, and what final output is actionable.
4. **Safety/domain guard**: Apply repo, user, legal, privacy, deployment, and clinical boundaries. Remove tasks that require prohibited data or approvals.
5. **Verification lead**: Design adversarial checks, duplicate review, source/file-line evidence, conflict resolution, and final acceptance criteria.

Resolve disagreements by writing down the tradeoff, choosing the safer smaller plan when uncertainty is high, and escalating only when correctness risk justifies the cost.

## Intake Gate

Do not fan out until the task contract is clear enough for independent agents to avoid inventing incompatible assumptions.

For each workflow, establish:

- The exact target and non-target areas.
- The source of truth for required behavior, such as API mappings, specs, policies, tests, docs, or user-provided criteria.
- The allowed write scope and prohibited operations.
- The evidence each agent must return.
- The validation commands or reason validation is not available.
- The unresolved questions that should block execution rather than be guessed.

If these are missing, run a read-only mapping phase first or ask the user for the missing contract. For migrations, require old/new API names, semantic differences, import changes, error behavior, and test expectations before edit agents begin.

## Workflow Blueprint

Create a compact plan before execution:

```yaml
objective: "One sentence result the workflow must produce"
mode: "single-agent | subagent | dynamic-workflow"
constraints:
  - "User, repo, policy, data, deployment, cost, and time limits"
phases:
  - name: "map"
    purpose: "Discover partitions, sources, files, or hypotheses"
  - name: "fanout"
    purpose: "Assign bounded independent work to agents"
  - name: "reduce"
    purpose: "Normalize outputs, merge duplicates, identify conflicts"
  - name: "verify"
    purpose: "Adversarial review, reproduction, tests, or source checks"
  - name: "finalize"
    purpose: "Apply changes or produce the answer"
agents:
  - role: "Specialist name"
    scope: "Exact files, question, or partition"
    permissions: "read-only | edit-scoped | test-only"
    output_schema: "Fields the reducer needs"
budgets:
  max_agents: 8
  max_concurrency: 4
  stop_conditions:
    - "Enough evidence to decide"
    - "Repeated blocker"
    - "Budget no longer justified"
acceptance:
  - "Tests, citations, line references, screenshots, or reviewer sign-off"
```

## Confidence Rubric

Define the task-specific rubric before fan-out so agents grade results consistently:

- **High confidence**: Direct evidence satisfies the acceptance criteria, obvious alternative explanations have been checked, and a verifier can reproduce or trace the claim.
- **Medium confidence**: Evidence points in the right direction, but one material alternative explanation, dependency, runtime condition, or missing source remains unresolved.
- **Low confidence**: The claim is speculative, inferred from naming or style only, blocked on missing context, or not independently checkable.

Only report medium or low confidence items when the user explicitly asks for leads, hypotheses, or open questions. Otherwise, keep them out of the final answer or place them in a clearly labeled residual-risk section.

## Agent Contracts

Give each subagent a narrow prompt with all necessary constraints and no hidden expected answer:

```text
Role: <specialist role>
Task: <bounded objective>
Scope: <files, URLs, components, or hypothesis>
Constraints: <repo/user/policy boundaries; no production secrets/data; allowed tools>
Do not: <out-of-scope actions, broad refactors, deployment, private data access>
Return:
- finding_or_result:
- evidence: <file:line, command output summary, source URL, or reproduction step>
- confidence: high|medium|low
- risks_or_open_questions:
- recommended_next_step:
```

When agents may edit files, isolate ownership by file path, module, or worktree. Avoid assigning overlapping edits unless the workflow has an explicit merge owner.

## Reduce And Verify

After fan-out:

1. Normalize all outputs into the same schema.
2. Drop unsupported claims and duplicate low-value findings.
3. Surface conflicts explicitly instead of averaging them away.
4. Send high-impact conclusions, security/clinical/deployment implications, and broad edits through an adversarial review pass.
5. Prefer reproducible evidence: tests, command output summaries, source citations, or file-line references.
6. Finalize only after the verifier's objections are answered, downgraded with a reason, or reported as residual risk.

For code work, run the narrowest relevant checks first, then broader repo checks when risk warrants it. Document skipped validation with the exact command and reason.

## Reusable Patterns

Use these patterns as building blocks:

- **Map-reduce audit**: mapper agents inspect partitions; reducer deduplicates; verifier spot-checks top findings.
- **Council debate**: five role agents produce independent plans; reducer extracts tradeoffs; verifier attacks the selected plan.
- **Migration factory**: mapper inventories targets; editor agents patch non-overlapping partitions; test agents validate; merger reconciles style and contracts.
- **Research claim voting**: scout agents collect sources; checker agents validate claims against sources; reducer reports only claims that survive cross-checking.
- **Implementation gauntlet**: planner proposes; implementer edits; reviewer hunts regressions; tester runs checks; finalizer writes concise status.

## Quality Bar

The final answer should state:

- Which mode was used and why.
- What agents or phases ran.
- What changed or what conclusion survived verification.
- What checks passed.
- What was skipped, blocked, or left as residual risk.

Keep workflow artifacts concise enough to rerun. Save or document the workflow when the user will repeat it.
