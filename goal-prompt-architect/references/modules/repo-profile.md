# Repo Profile Module

Use this module before generating repo-specific /goal prompts.

```text
REPO PROFILE:
Inspect and summarize:
- language and framework
- package manager
- application/service layout
- build commands
- test commands
- lint/typecheck/static validation commands
- route/API/CLI entrypoints
- domain models, migrations, and fixtures
- CI workflows
- AGENTS, README, CONTRIBUTING, SECURITY, and other instructions
- risky domains: auth, billing, payments, security, privacy, regulated data, production operations
- verification oracles: tests, snapshots, fixtures, benchmarks, logs, generated artifacts

Use discovered commands and files. Do not invent commands as certain. If unknown, instruct the agent to discover narrow checks first.
```
