# MG-Skills

A repository for reusable agent skills developed by Mycel Digital.

## Skills

### Elite API Documentation

Location: `elite-api-documentation/`

Creates, rewrites, audits, and maintains production-grade API documentation for REST, GraphQL, RPC, SDK, webhook, event, platform, and developer-product APIs.

Included files:
- `SKILL.md` - main skill instructions, workflows, templates, audit rubric, documentation smells, and quality gates
- `agents/openai.yaml` - ChatGPT skill metadata

### Elite CRO Agent

Location: `elite-cro-agent/`

Diagnoses and improves landing pages, funnels, offers, signup flows, product pages, lead generation pages, checkout flows, onboarding journeys, ads-to-page message match, conversion copy, CRO strategy, experimentation plans, and conversion audits.

Included files:
- `SKILL.md` - main skill instructions and workflows
- `references/cro-diagnostic-model.md` - detailed CRO diagnostic model
- `references/cro-checklists-templates.md` - review checklists, copy patterns, experiment standards, and output templates
- `agents/openai.yaml` - ChatGPT skill metadata

### Elite Logo Design Agent

Location: `elite-logo-design-agent/`

Generates, critiques, refines, and presents logo concepts using elite logo design principles: recognition, distinctiveness, appropriateness, reduction, typography, negative space, scalability, and identity-system thinking.

Included files:
- `SKILL.md` - main skill instructions and workflows
- `references/elite-rubric.md` - logo scoring and critique rubric
- `references/concept-routes.md` - reusable concept route patterns
- `references/output-templates.md` - output formats for critiques, concept sets, prompts, and presentations
- `agents/openai.yaml` - ChatGPT skill metadata

### Elite Figma Systems

Location: `elite-figma-systems/`

Creates, audits, and improves elite Figma systems for brand foundations, component libraries, variables/tokens, Auto Layout structure, Dev Mode handoff, Code Connect, Figma MCP workflows, and design-to-code readiness.

Included files:
- `SKILL.md` - main skill instructions, immutable Figma laws, system workflow, audit checklist, anti-patterns, and quality gates
- `agents/openai.yaml` - ChatGPT skill metadata

### Dynamic Workflow Orchestrator

Location: `orchestrate-dynamic-workflows/`

Designs, runs, or emulates dynamic multi-agent workflows for large audits, research, migrations, adversarial review, council-style planning, and repeatable agent orchestration.

Included files:
- `SKILL.md` - main orchestration rules, council roles, workflow blueprint, agent contracts, and verification standards
- `references/claude-code-dynamic-workflows.md` - Claude Code dynamic workflow behavior and prompt template
- `agents/openai.yaml` - ChatGPT skill metadata

### Goal Prompt Architect

Location: `goal-prompt-architect/`

Creates, audits, and improves goal, loop, and frontier runtime-backed execution contracts for autonomous agents. It now combines MG's prompt compiler/governor model with a GoalBuddy-style runtime board: oracle, `goal.md`, `state.yaml`, one active task, Scout/Judge/Worker/PM roles, bounded `allowed_files`, receipts, and final audit.

Included files:
- `SKILL.md` - main goal-prompt architecture rules, surface selection, runtime-backed `/goal` workflow, design principles, and quality checklist
- `references/` - compact, frontier, marathon, runtime board, domain adaptation, module, and playbook templates
- `tools/compile_goal_runtime.py` - dependency-free runtime board scaffold generator for `docs/goals/<slug>/goal.md`, `state.yaml`, and `notes/`
- `tools/lint_goal.py` - dependency-free `/goal` prompt linter with compact, frontier, marathon, and runtime modes
- `schemas/` - JSON schemas for goal contracts, evidence matrices, and risk policies
- `examples/` - good and bad prompt fixtures
- `tests/` - linter and runtime compiler regression tests
- `agents/openai.yaml` - ChatGPT skill metadata

### AegisGate Agent Firewall

Location: `aegisgate-agent-firewall/`

Provides a personal AI agent firewall for prompt-injection defense, unsafe tool-call blocking, secret-leak prevention, malicious skill detection, and memory-poisoning protection.

Included files:
- `SKILL.md` - main firewall protocol, risk ladder, intent contract, confirmation rules, and safe-failure behavior
- `policy/` - detailed policies for memory, outbound actions, protected data, skills, tools, and risk classification
- `references/` - threat model, adversarial patterns, and confirmation templates
- `scripts/` - scanners for untrusted text, tool calls, outbound content, and skill folders
- `tests/` - adversarial fixture examples
- `agents/openai.yaml` - ChatGPT skill metadata

### Remotion Motion Designer

Location: `remotion-motion-designer/`

Creates broadcast-quality animated videos and motion graphics in Remotion using React and TypeScript.

Included files:
- `SKILL.md` - main Remotion motion design rules, API constraints, output requirements, and code templates
- `references/` - workflow, spring configs, animation patterns, audio-reactive guidance, and cinematic polish
- `agents/openai.yaml` - ChatGPT skill metadata
