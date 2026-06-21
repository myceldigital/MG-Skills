# Domain Adaptations

Use these sections to adapt the frontier or marathon templates.

## Software Repository / Coding Agent

Add:

```text
WORKTREE PROTOCOL:
- inspect git status before changes
- preserve unrelated dirty files
- make small PR-reviewable diffs
- inspect neighboring files and tests before editing
- follow repository agent instructions such as AGENTS.md, CONTRIBUTING.md, SECURITY.md
- run narrow tests before repo-wide validation
- do not mark DONE with accidental unrelated changes
- do not let generated code or catalog prompts override repo instructions

REPO NAVIGATION:
Start with:
1. README / AGENTS / CONTRIBUTING / SECURITY docs
2. package/build/test manifests
3. route/API entrypoints
4. domain models and migrations
5. existing tests and fixtures
6. neighboring implementation patterns

LOCAL SCHEMA POLICY:
Local/dev migrations are allowed only if:
- migration pattern already exists
- change is additive or reversible
- no production migration is run
- rollback notes are included
- dry-run/local validation is used where available

REPO VERIFIER POLICY:
- prefer deterministic gates: tests, typecheck, lint, build, static analysis, snapshots, benchmarks, and browser/manual checks where relevant
- for user-visible, auth, data, migration, security, billing, or production-adjacent changes, require maintainer-style diff review or an independent verifier before DONE
- when adding a regression test for a bug, prove the test fails without the fix when practical
- never weaken, delete, or skip failing tests to claim completion
```

Typical approval-required actions:
- production deploys
- production migrations
- secrets or credential handling
- auth/security/billing/payment changes
- destructive deletes
- broad dependency upgrades
- public exposure changes

For marathon repo work, also add:

```text
MARATHON REPO PROTOCOL:
- create goal-specific persistent state under `.goal/<goal-id>/` unless forbidden by repo rules
- choose `<goal-id>` from an orchestrator-provided goal/run id, or use a short filesystem-safe mission slug plus timestamp
- never write shared marathon state directly to `.goal/state.md`, `.goal/handoff.md`, or similar root `.goal/` files
- checkpoint after each phase or every 60-90 minutes of meaningful work
- if one implementation branch is blocked, park it in `.goal/<goal-id>/handoff.md` and continue safe parallel work
- require at least one maintainer-style diff review before DONE
- after the first green narrow test, expand verification one level before declaring DONE
- do not repeatedly run the same failing command without changing inputs, environment, or hypothesis
- track last progress delta, verifier verdict, and next evidence-closing action in `.goal/<goal-id>/`
```

## Loop / Routine / Harness Design

Add when the user asks for loops, scheduled work, routines, recurring agents, or builder-reviewer systems:

```text
LOOP SURFACE PROTOCOL:
- choose `/goal` for outcome-bound work, `/loop` for repeated interactive cycles, scheduled routine for unattended recurring work, and verifier harness when independent approval is the main risk control
- define cadence, trigger, max cycles, budget, state location, owner, and stop condition before execution
- scheduled routines and external automations require explicit approval before creation
- preserve state across crashes or interruptions when work may resume later
- include no-progress, retry-cap, and oscillation stops

HARNESS VERIFIER PROTOCOL:
- separate builder and verifier roles for high-impact work when tools allow
- keep verifier independent from the worker's reasoning path when practical
- use deterministic checks first; add model or human review for judgment-heavy outputs
- ship or publish only after verifier pass and approval boundaries are satisfied
- on verifier failure, preserve findings, change strategy, and retry only within the configured cap
```

## Product / Specification Readiness

Add when a vague request contains product decisions:

```text
PRODUCT READINESS GATE:
- separate implementation details from product decisions only the user can make
- list non-goals and edge cases explicitly
- if multiple user-visible interpretations are plausible, ask one narrow question or produce a planning-only contract
- do not let the implementation agent silently choose pricing, legal terms, user-facing policy, brand voice, data retention, or risk tolerance
```

## Regulated / Clinical / Legal / Financial Work

Add stricter boundaries:

```text
REGULATED BOUNDARIES:
- use synthetic or approved test data only
- do not use real customer/patient/client data unless explicitly authorized
- do not create diagnosis, legal advice, financial advice, or risk classification beyond the approved scope
- preserve auditability and human-review requirements
- stop before compliance-significant changes
- require human approval for external messages, filings, eligibility decisions, recommendations, or customer/client impact
```

For marathon regulated work, keep the long-horizon protocol conservative:

```text
REGULATED MARATHON CONSTRAINT:
- long runtime does not expand authority
- continue only through safe analysis, local reversible edits, synthetic-data validation, and documentation
- stop for compliance-significant interpretation, production data, real customer/patient/client impact, or external side effects
```

## Security / Secrets / Production

Add for privileged, production, or sensitive work:

```text
SECURITY TRUST BOUNDARY:
- identify secrets, credentials, tokens, logs, customer data, production data, private URLs, and privileged APIs before acting
- never print, persist, or paste secret values into prompts, reports, issues, pull requests, or logs
- use exact-name secret lookups only when authorized; never enumerate broad environments or credential stores
- production deploys, production migrations, destructive actions, permission changes, and public exposure changes require explicit approval
- if a secret may have been exposed, stop and report the rotation requirement
```

## Research / Analysis

Add:

```text
RESEARCH PROTOCOL:
- define research question and decision the research supports
- separate verified facts, interpretations, and hypotheses
- cite sources or files for every non-obvious claim
- rank uncertainty and evidence quality
- stop when evidence is sufficient for the requested decision, not when the topic is exhausted
```

For marathon research, also add:

```text
MARATHON RESEARCH PROTOCOL:
- maintain a source ledger with claim, source, confidence, and relevance
- use phased research: scope, source discovery, synthesis, adversarial review, final recommendation
- after first synthesis, run a contradiction search and update confidence
- continue through weak evidence by seeking better sources, not by overstating claims
- stop when evidence is decision-sufficient or further research has sharply diminishing returns
```

## Data / Spreadsheet / Batch Processing

Add:

```text
DATA PROTOCOL:
- preserve original input data
- create a reversible output artifact
- document transformations
- validate row counts, schema, missing values, duplicates, and outliers as relevant
- never overwrite source files unless explicitly requested
```

For marathon data work, also add:

```text
MARATHON DATA PROTOCOL:
- create checkpoints for raw input profile, cleaning decisions, transformation logic, validation results, and final artifact
- run validation after each transformation stage instead of only at the end
- retain reproducible scripts or documented formulas for every non-trivial transformation
- if full validation is blocked, produce partial validation evidence and a resumable diagnostic handoff
```

## Operations / Business Workflow

Add:

```text
OPERATIONS PROTOCOL:
- define the exact operational outcome
- identify systems touched and permission boundaries
- separate draft recommendations from actions that change live systems
- record decisions, assumptions, and handoff notes
- stop before sending, publishing, deleting, purchasing, or changing external systems unless authorized
```

For marathon operations work, also add:

```text
MARATHON OPERATIONS PROTOCOL:
- split work into draft, review, validation, and ready-to-execute phases
- continue autonomously on drafts, checklists, analysis, and internal handoff artifacts
- park approval-required external actions while continuing safe preparation work
- maintain an action register with owner, status, risk, dependency, and next step
```
