# Codex Manager/Implementer Protocol

## Purpose and activation

Use this adapter when designing or executing phased work with an Astra Manager and smaller-model Implementers in separate Codex tasks.
It supplements the goal charter and runtime protocol, rather than replacing their verification and authority rules.
Read actual tool schemas and relevant local project instructions first.
The available host tools are the operational authority; recheck model availability and lifecycle semantics when they differ from this reference.

A request to write a prompt, plan, or update this skill is not a request to execute that prompt.
Only create user-visible tasks when the user explicitly requests separate tasks or explicitly requests execution of this multi-session workflow.
For ordinary subtasks, use available multi-agent tools inside the current task.
Do not silently change the user's model, create schedules, or edit global concurrency settings.
Carry forward authorization already granted in the session without asking again.
A request to execute the Manager/Implementer workflow covers its routine concurrent tasks, phase handoffs, model routing, reviews, and repairs.
Do not ask for separate approval of each subgoal, task, or lane.
Manager acceptance is an internal verification gate, not a request for human permission.

## Responsibilities and naming

| Role | Responsibility | Task title |
|---|---|---|
| Manager | Design mission, order phases, route models, resolve scope, review evidence, integrate and accept | `Manager: <project> - <mission>` |
| Implementer | Reproduce, implement and verify one bounded phase | `Implementer: <project> - <mission> - P01 <outcome>` |
| Reused Implementer | Continue related dependent phases with useful context | Rename to the current phase while retaining the `Implementer:` prefix |
| Parallel Implementer | Own an isolated dependency-ready lane | `Implementer: <project> - <mission> - <lane>` |

Use `set_thread_title` for an existing task or fork.
For a newly created task, supply `title`, then check the returned/listed title and repair normalization if it lost the exact role prefix.
Use the current task as Manager when that is the user's intended workspace.
Store IDs in the coordination system; names are for humans and must never substitute for IDs.
Do not rename unrelated existing tasks while designing or updating a skill.

The Manager is the goal designer and acceptance owner, not a second concurrent implementation worker.
It may inspect code, run scoped checks, maintain its charter/board, and coordinate integration.
Delegate substantial code production to Implementers, including repair phases discovered during review.
Any manager write window must be explicit and non-overlapping with implementation scope.

## Model routing

The user-requested manager is `gpt-6-astra`.
For this requested Astra/smaller-model workflow, choose concrete Implementer models and reasoning levels autonomously within the user's preferences.
For an ordinary skill invocation outside that arrangement, preserve configured model settings unless the user requests a model choice.
A requested execution of this explicit Astra/smaller-model arrangement supplies that preference; keep the final concrete selection visible in the phase packet.
Check available IDs and supported reasoning efforts in the calling host's tool schema.
If no model preference is authorized, omit model overrides and preserve the user's configured model.

These are starting heuristics from the local tool descriptions, not benchmark claims:

| Work | Preferred available model | Starting reasoning effort |
|---|---|---|
| Goal design, architectural decisions, difficult acceptance review | `gpt-6-astra` | `high`; raise only for concrete unresolved complexity |
| Simple isolated fixes, clear test additions, narrow mechanical changes | `gpt-5.6-luna` | `medium` |
| Bounded feature implementation involving several related files | `gpt-5.6-terra` | `high` |
| Complex implementation or integration requiring broader reasoning | `gpt-5.6-sol` | `high` |
| Very small, unambiguous work with strong deterministic checks | `gpt-5.4-mini` | `medium` |

Before every dispatch, decide which model and reasoning level best fit this phase.
Choose the smallest model likely to complete it reliably, rather than routing solely by cost or the task label.
Record model, reasoning effort, selection rationale, and an escalation trigger in the phase packet.
Choose by ambiguity, coupled systems, failure impact, and verification strength.

Select reasoning effort separately from model size:

| Reasoning | Use when |
|---|---|
| `low` | The transformation is explicit, local, low impact, and checked deterministically |
| `medium` | A familiar bounded task needs some investigation and straightforward verification |
| `high` | Several interacting paths, difficult debugging, or material correctness risks require careful reasoning |
| `xhigh` or higher, only if supported | A specific unresolved design or adversarial edge case justifies extra reasoning; reassess after it is resolved |

Higher reasoning is not a substitute for missing evidence, an oversized phase, or inadequate tests.
Do not treat these choices as measured optimal settings.
Do not put a high-risk authorization or migration change on a small model solely because the diff is small.
Give security, data, billing, and public-contract phases a capable Implementer plus independent review.
Astra may resolve the difficult design and return the resulting bounded implementation to a smaller model.
After two attempts fail to produce new evidence, change the hypothesis, narrow the phase, or escalate the model; do not blindly retry or immediately send the whole mission to Astra.
After the difficult phase, reassess model size for the next phase.
If a selected model is unavailable, use an available model consistent with user authorization and disclose the substitution; otherwise preserve the current setting and report the limitation.
Never claim a task switched models merely because its prompt names one.
Use the real `model` and `thinking` fields on supported creation/message tools and check for errors.
There is no self-model-switch tool implied by this protocol.

## Plan once, refine at phase boundaries

1. Inspect the repo, existing tasks, current changes, relevant instructions, verification commands, and prior receipts.
2. Convert the user's full outcome into stable criterion IDs with observable proof, including user-facing integration and final delivery where requested.
3. Group criteria into dependency-ordered phases with useful end-to-end outcomes.
4. Define the next phase precisely; keep later phases as concise outcomes until their prerequisites are known.
5. Choose model, write scope, verifier, and explicit exit criteria for each ready phase.
6. Dispatch independent ready phases concurrently; gate each lane only on its own accepted prerequisites and shared-resource constraints.

The checklist should cover the complete mission, but avoid an enormous speculative list of micro-edits.
Every required criterion must belong to a phase and have a proof path.
A phase finishes when its required criteria pass and material findings are resolved.
Use "Complete this phase completely, extremely well" followed by concrete criteria.
Do not use an open-ended perfection standard.
Discovery and scaffolding are legitimate phases, but their completion must lead to implementation when the mission requires it.

## Native goal lifecycle

A `/goal` string in a message is not proof that native goal mode activated.
Each task must explicitly inspect and use its own goal tools.
The Manager cannot use its local goal tools to set another task's goal.

| Situation | Action |
|---|---|
| User authorizes goal execution | Call `get_goal` in the current task; create the requested mission with `create_goal` only when none is unfinished |
| Matching unfinished goal exists | Continue it; do not create a duplicate |
| Different unfinished goal exists | Preserve it and resolve the task/mission mismatch; never overwrite it or falsely complete it |
| Implementer receives an authorized phase | Call its own `get_goal`, then `create_goal` for that bounded phase if allowed by the existing status |
| Phase verified | Implementer marks only its own bounded goal `complete`, then sends its receipt |
| Manager finds a defect after phase completion | Dispatch a new bounded repair goal; do not pretend to reopen a completed goal |
| Mission verified and no required work remains | Manager calls `update_goal(status="complete")` |

Only set `token_budget` when the user explicitly requested a token budget.
Do not invent per-phase allocations from a mission budget; use a user-specified allocation or omit the native field.
Measured usage is shared/account-wide where the tool says so and must not be misreported as this phase's spend.
For a completed budgeted goal, report final usage returned by the tool.

Under the current tools, `update_goal` changes status only to `complete` or `blocked`.
It cannot pause, resume, edit objectives, or change budgets.
Use `blocked` only after the same blocking condition recurs across at least three consecutive goal turns and no meaningful safe progress is possible without user input or external change.
A resumed blocked goal starts a fresh three-turn audit.
Do not manufacture turns to reach this threshold.
Report a pending user action immediately and do safe independent work while the native blocker threshold is not yet met.
Once the threshold is met and the agent is at an impasse, mark blocked instead of repeating an active-goal status indefinitely.
Board labels such as `waiting_for_approval`, `review_pending`, or `budget_exhausted` are not extra native statuses.
Reaching a checkpoint or budget limit never proves completion.

## Create or reuse the Implementer

Inspect existing relevant tasks before launching another one.
Reuse an idle related Implementer when its goal state and checkout match the next phase.
Use a fresh task for an unrelated phase, stale context, or a different isolated write lane.

For explicit separate-task creation, call `list_projects` before `create_thread`.
Use the returned project ID and default to a worktree for a Git repository, local otherwise.
Respect an explicit instruction to use the saved project directly.
Do not invent branch names or starting refs in tool arguments that require a user-requested ref.
If the phase depends on earlier changes, verify that the new checkout actually contains the accepted prerequisite revision before any implementation.
Never assume a newly created worktree contains another worktree's uncommitted edits.
Include returned task IDs in the required created-task UI directive when reporting creation.

A same-directory `fork_thread` is useful for a sequential dependent Implementer, as observed in Lirena.
Use it only inside an authorized separate-session workflow, never as a workaround for missing task-creation authorization.
The fork copies completed history only; resend the full current phase packet because the active turn is absent.
Rename the fork, then send the phase prompt with explicit authorized model/effort fields.
A same-directory fork shares files and Git state: permit exactly one code writer and assign any manager-owned files separately.
Do not concurrently checkout, reset, stage, commit, regenerate shared outputs, or integrate changes in that shared directory.
Separate worktrees isolate files but do not eliminate public API, database, or merge conflicts.

Creation/forking may return `clientThreadId` while setup is pending.
Do not pass it to tools that require `threadId`.
Resolve readiness through returned status/UI and task listing before messaging or waiting; do not repeatedly relaunch after an uncertain response.
Check errors before recording a launch as successful.
A created task with an initial prompt is already dispatched; do not send the same packet again automatically.

## Required phase packet

Use a structured tool argument for this prose, not shell-escaped text.
Resolve placeholders from inspected context before dispatch; unknown verification commands require discovery before edits.

```text
/goal Complete phase <ID>: <outcome> completely, extremely well.

ROLE: Implementer. Do not run the whole manager mission or spawn additional user-visible tasks.
MANAGER: <actual manager task ID and host ID>
PACKET: <mission ID / phase ID / revision / attempt>
MODEL: <selected available model and effort; brief reason>
CONTEXT: <relevant instructions and concise design decisions>
CHECKOUT: <project ID, actual cwd, branch, prerequisite revision or fingerprint>
DEPENDENCIES: <accepted phase IDs and accessible evidence>
MISSION CONTRIBUTION: <criterion IDs this phase closes>
ALLOWED_FILES: <bounded paths and shared resources>
NON-GOALS: <explicit exclusions>
AUTHORITY: <inherited user authorization and approval-required actions>
SUCCESS CRITERIA: <observable phase outcomes>
VERIFY: <exact scoped commands and necessary E2E/manual evidence>
STOP_IF: <scope collision, unsafe next action, missing required decision>
PROGRESS: <meaningful evidence delta; two no-progress cycles trigger replanning>
RECEIPT: <result, changed files, revision/fingerprint, commands/exits, evidence paths, limitations>

Inspect your native goal with get_goal.
Create this bounded phase goal with create_goal only if no unfinished incompatible goal exists.
Do not set token_budget unless the user explicitly requested it.
Reproduce bugs through the closest practical end-user flow before fixing them.
Make the smallest correct change, verify the criteria, and inspect the final diff.
After necessary checks pass, advance without speculative polishing or repeated unchanged sweeps.
Mark only this bounded goal complete when verified.
Send the receipt directly to the manager using send_message_to_thread, then return the same concise result as your final answer.
If receipt delivery fails, preserve the receipt and report the delivery failure.
Await the next bounded phase; never self-authorize later phases.
```

The Manager dispatches a dependent phase after accepting its prerequisites, without waiting for unrelated lanes.
Within the original mission, the Manager resolves routine scope changes and missing files by checking collisions, updating the packet, and continuing; human approval is not needed.
An Implementer must not silently exceed its packet, but should request a Manager revision and continue independent in-scope work.
Preassigned work may proceed when its recorded dependencies are accepted; do not interpret every numbered phase as a global barrier.
Follow-up corrections that change scope get a new packet revision and clear supersession.
A read-only question about prior evidence must explicitly say it does not authorize edits or another goal.

## Manager acceptance loop

1. Dispatch exactly one ready packet per write scope.
2. Use `wait_threads` with real `threadId`, host ID, and the last cursor as `afterCursor`.
3. For an immediate snapshot use `timeoutMs: 0`; for event waits use bounded waits no longer than 60 seconds and obey current tool limits.
4. Do useful independent review or planning between waits; do not produce unchanged polling commentary.
5. On completion, inspect the receipt, actual diff/artifacts, and required checks against the packet's revision.
6. Return `accept`, `repair`, `split`, or `waiting_for_input` with the smallest evidence-based reason.
7. Record acceptance in the authoritative task system/board, release the writer scope, and dispatch the next dependency-ready phase.
8. After all phases, verify integration and the full original mission before completing the Manager goal.

A receipt must distinguish local/scoped success from integrated application behavior and production rollout.
Required fields are mission/phase/packet IDs, worker ID, outcome, checked revision or dirty fingerprint, files changed, exact commands with results, evidence locations, known limitations, and the proposed next action.
A worker final answer, an idle task, or a checked checkbox is not sufficient acceptance evidence.
Bind evidence to the files actually reviewed; rerun relevant checks when those files or dependencies materially change.
For high-impact changes, use an independent reviewer and appropriate deterministic checks.
Do not commission repeated full reviews when an accepted revision has no material change or unresolved finding.

If a snapshot omits the final message or is stale, make one bounded read or ask the Implementer for the missing receipt via task messaging.
Do not interpret missing text as failure, rerun accepted tests, or send duplicate phase instructions.
Receipt delivery and native goal completion are separate facts; reconcile both after interruption.
The Manager stays active through ordinary phase handoffs and uses waits to receive completion.
A final answer does not itself schedule future work; use a heartbeat only when the user asks for a scheduled follow-up or monitoring.

## Durable state and optional HTML progress

Reuse a task system/queue when present.
Otherwise designate one Manager-owned `state.yaml` as phase coordination truth and update it atomically.
Store mission and phase IDs, packet revisions, dependencies, task/host IDs, selected models, scopes, checkout/base identity, phase outcomes, receipts, acceptance decisions, timestamps, and next action.
Native goal status remains owned by native tools.
Immutable receipts can be JSON or durable evidence documents; live claims and leases must not be hand-edited Markdown.
Do not put sensitive customer content into receipts or progress pages.

The Manager may request a small local HTML dashboard when useful or user-requested.
Implement it once as a generated read-only view of structured state, showing the full criteria checklist, accepted/total count, phase, blockers, last evidence delta, and accepted criteria over time.
Keep submitted-but-unreviewed work separate from manager-accepted work.
Use timestamped events; never fabricate historical progress or equate unequal checkbox counts to percentage of effort.
Reopened criteria must visibly reduce current completion or be recorded as reversals.
Do not hand-toggle the HTML as a separate authority, publish it without authorization, or make dashboard polish a mission of its own.

Two meaningful work cycles without evidence delta trigger a changed hypothesis, narrower reproduction, model escalation, or a dependency-ready alternative.
Count actual work cycles, not polls or elapsed time while a known long-running check is progressing.
Do not interrupt useful verification merely to satisfy an artificial progress counter.
An optional elapsed-time checkpoint is a review signal, not permission to skip required criteria or mark them done.
Blocked required work stays visible and prevents full mission completion until resolved or explicitly removed by the user.

## Concurrency and recovery

Automatically run independent dependency-ready lanes concurrently, with one write-capable owner per conflicting scope.
The workflow request supplies orchestration authority; do not seek per-lane approval.
After an acceptance or repair decision, fill useful available capacity with newly unblocked work.
Prioritize work that unblocks downstream outcomes rather than maximizing the number of agents.
For a single shared checkout, retain one code writer; use isolated worktrees for concurrent code production.
Treat databases, public contracts, generated outputs, ports, test fixtures, and Git operations as shared resources even when filenames differ.
Assign each lane an integration owner and acceptance dependencies; record why work is serialized when an actual conflict requires it.
Use in-task subagents for bounded research/review or isolated work where available.
Do not confuse user-visible tasks with subagent concurrency slots.
Numbers such as 64 or 96 are not default targets and do not authorize changing configuration.
Choose fan-out from ready independent work, shared-file/API/data constraints, machine capacity, rate limits, and ability to review results.
An isolated branch still needs an integration owner and compatibility checks.

On interruption or compaction:

1. Read the charter, authoritative state, latest receipts, and actual native goal state.
2. Reconcile task IDs and statuses before any relaunch.
3. Inspect checkout revision and unexpected changes; preserve other agents' work.
4. Validate only evidence invalidated by changes, then resume the next permitted action.
5. Reuse the current phase packet if it is still active; do not dispatch duplicates.

Do not manually edit Codex internal databases, session transcripts, or native goal state to force continuity.
Do not consume usage-reset credits without explicit authorization.

## Grounding and limits

Reviewed in the local Codex installation on 2026-09-07:

- `Lirena international compliance manager` and `Lirena international compliance implementer` used a same-directory fork, actual native goal calls, scoped implementation, explicit messages, and independent manager acceptance.
- Their inspected model metadata showed `gpt-6-astra` in both roles; smaller-model routing above is a proposed improvement, not a measured success from that pair.
- `Build assessment catalog guide` and `Assessment catalog implementer` showed detailed evidence receipts, shared-file write windows, separate offline versus application acceptance, and explicit avoidance of redundant final sweeps.
- Missing final text in task snapshots required direct receipt recovery in the compliance workflow.
- Existing task names did not consistently use the requested prefixes.

These observations support the protocol mechanics, not a claim that the entire Lirena mission is complete or that a particular fan-out/model is optimal.
Recheck current tools on future hosts rather than copying private task IDs, absolute paths, or project-specific constraints into generic prompts.
