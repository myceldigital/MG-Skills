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
```

For marathon regulated work, keep the long-horizon protocol conservative:

```text
REGULATED MARATHON CONSTRAINT:
- long runtime does not expand authority
- continue only through safe analysis, local reversible edits, synthetic-data validation, and documentation
- stop for compliance-significant interpretation, production data, real customer/patient/client impact, or external side effects
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
