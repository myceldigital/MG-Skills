# Claude Code Dynamic Workflows Snapshot

Source checked: https://code.claude.com/docs/en/workflows on 2026-05-30.

Verify the live docs before relying on version numbers, plan availability, limits, or UI behavior.

## What The Feature Is

Claude Code dynamic workflows are JavaScript orchestration scripts that spawn and coordinate subagents while the user session stays responsive. The script owns loops, branching, intermediate state, and synthesis. Agents do the actual reading, editing, tool use, and command execution.

Use this when a task is too large for turn-by-turn subagent coordination, or when the orchestration itself should be inspectable, reusable, and resumable.

## Current Claude Code Notes

- Research preview.
- Docs state Claude Code v2.1.154 or later is required.
- The word `workflow` in a prompt can trigger workflow generation when enabled.
- `/deep-research` is the bundled workflow for many-source research and claim cross-checking.
- `/workflows` opens running/completed workflow management.
- Saved workflows can become slash commands.
- Project workflows live under `.claude/workflows/`; personal workflows live under `~/.claude/workflows/`.
- The workflow script itself does not directly access the filesystem or shell; spawned agents perform those actions.
- Docs state up to 16 concurrent agents and 1,000 agents total per run.
- No mid-run user input is available except permission prompts; split stages into separate workflows when human sign-off is required between stages.
- Workflows can be disabled via Claude Code configuration, settings JSON, environment variable, or organization settings.

## Claude Workflow Prompt Template

```text
Run a workflow to <objective>.

Use phases:
1. Map the target space and produce partitions.
2. Fan out independent specialist agents with non-overlapping scope.
3. Reduce results into a normalized schema.
4. Run adversarial verification on high-impact findings or edits.
5. Return a concise final report with evidence and skipped checks.

Constraints:
- Respect all repository and user data boundaries.
- Do not access production secrets, production data, or private customer/patient data.
- Do not deploy or widen public access.
- Keep edits scoped and PR-reviewable.
- Prefer smaller models/agents for low-risk mapping if available.
```

## Save Criteria

Save a workflow for reuse only when:

- The task will recur with similar structure.
- The phases and result schemas are stable.
- The workflow does not bake in stale file paths, dates, secrets, private data, or one-off assumptions.
- The approval and permission behavior is acceptable for future runs.
