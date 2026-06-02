---
name: elite-figma-systems
description: Use this skill when the user asks for elite Figma guidance, Figma file creation or critique, design system setup, brand foundations in Figma, component libraries, variables/tokens, Auto Layout, Dev Mode handoff, Code Connect, Figma MCP workflows, design-to-code readiness, or best practices that separate expert Figma work from ordinary design files.
---

# Elite Figma Systems

Use this skill to operate like an elite Figma practitioner: treat Figma as a collaborative product-design system, not a static drawing tool. Your output should help the user create Figma work that is visually strong, structurally sound, implementation-ready, scalable across a team, and resilient to real product complexity.

The core standard is simple: great Figma work must survive content changes, edge cases, engineering implementation, design-system governance, and time.

## Operating Mindset

When using this skill, make decisions through these lenses:

1. **System over screen**: A single beautiful frame is not enough. Prefer reusable foundations, components, patterns, and file structures.
2. **Structure over decoration**: Use Auto Layout, components, variants, properties, constraints, variables, and clean hierarchy before visual polish.
3. **Semantics over raw values**: Prefer named decisions such as `surface/default`, `text/primary`, and `action/primary/background` over disconnected hex values or arbitrary spacing.
4. **Implementation over handoff**: Design files should be easy for engineers to inspect, map to code, and build accurately.
5. **Governance over chaos**: A system needs ownership, publishing rules, naming conventions, contribution criteria, and deprecation paths.
6. **Edge cases over happy paths**: Test long copy, empty states, error states, loading states, permissions, density, localization, dark mode, and responsive behavior.
7. **Automation over repeated manual drift**: Use plugins, APIs, variables, Code Connect, Dev Resources, webhooks, or MCP workflows when repeated manual work causes inconsistency.

## Immutable Laws

Follow these laws unless the user explicitly asks for a looser exploratory artifact.

### 1. The Canvas Is Not The Product

Do not optimize only for a polished screenshot. The work must be understandable, reusable, inspectable, and buildable.

### 2. Auto Layout Is The Default

Use Auto Layout for buttons, cards, inputs, nav bars, lists, tables, modals, page sections, dashboards, and any repeated structure. Manual positioning is acceptable only for expressive illustration, custom spatial compositions, or early throwaway exploration.

### 3. Components Are Contracts

Treat components as product contracts. They define what can change, what must stay stable, what states exist, and how the object should be used.

### 4. Component Properties Are The API

Expose customization through clear properties:

- Text properties for editable labels.
- Boolean properties for optional elements.
- Instance swap properties for icons, avatars, nested controls, or replaceable subcomponents.
- Variant properties for controlled differences such as `intent`, `size`, `state`, `density`, `theme`, and `platform`.

If a user must dig through layers to configure an instance, improve the component API.

### 5. Variants Must Be Predictable

Use variants only for meaningful, enumerable differences. Avoid variant sets that encode every accidental visual combination.

Good variant axes:

- `intent`: primary, secondary, destructive, neutral
- `size`: sm, md, lg
- `state`: default, hover, active, disabled, loading, error
- `density`: comfortable, compact
- `theme`: light, dark
- `platform`: web, iOS, Android

### 6. Variables Beat Raw Values

Use variables and styles for color, typography, spacing, radius, elevation, opacity, duration, and other reusable values. Avoid raw values in production-ready components unless intentionally local and documented.

### 7. Semantic Tokens Beat Primitive Tokens

Use primitives as source values, but apply semantic tokens in product work.

Example hierarchy:

- Primitive: `color/blue/600`
- Semantic: `action/primary/background`
- Component: `button/primary/background/default`

### 8. Modes Are System Multipliers

Use modes to manage light/dark themes, brands, density, platform, or regional differences without cloning whole files or component sets.

### 9. Names Are Interfaces

Layer names, component names, variable names, file names, page names, and section names should be readable by designers, engineers, and future maintainers.

### 10. Detach Is A Last Resort

If users often detach a component, inspect why. Usually the component is missing a property, state, slot, or layout behavior.

### 11. Dev Mode Starts Before Handoff

Prepare files for implementation throughout the design process:

- Mark ready-for-dev frames or sections.
- Add annotations where intent is not obvious.
- Use variables so values are inspectable.
- Keep hierarchy clean.
- Attach relevant resources.
- Connect components to code where possible.

### 12. The Best Figma Work Makes Everyone Faster

Evaluate success by team throughput, implementation quality, consistency, onboarding speed, and reduced ambiguity.

## Core Workflow

Use this workflow when creating, auditing, or improving serious Figma work.

### 1. Clarify The Artifact Type

Identify what the user needs:

- Brand foundation
- Design system
- Component library
- Product flow
- Website or app screens
- Dev Mode handoff
- Design-to-code workflow
- Figma plugin/API automation
- Figma MCP or AI-assisted workflow
- Audit or critique of existing Figma work

If the user does not specify, assume they need a practical system that can start small and scale.

### 2. Define The File Architecture

For a new serious Figma file, recommend or create pages like:

- `00 Cover`
- `01 Foundations`
- `02 Variables`
- `03 Components`
- `04 Patterns`
- `05 Product Flows`
- `06 Ready for Dev`
- `07 Experiments`
- `99 Archive`

For smaller files, compress this structure but preserve the intent: foundations, reusable components, actual work, and archive should not be mixed randomly.

### 3. Establish Foundations

Define the minimum viable foundations before deep screen work:

- Color system
- Typography scale
- Spacing scale
- Radius scale
- Elevation/shadow rules
- Grid and layout rules
- Icon style
- Motion principles, if relevant
- Accessibility rules
- Imagery or illustration direction, if relevant
- Voice or content conventions, if brand work is involved

Prefer a small complete system over a huge incomplete one.

### 4. Build Variables And Tokens

Create or recommend a token structure with three levels:

1. **Primitive tokens**: raw source values.
2. **Semantic tokens**: product meaning.
3. **Component tokens**: component-specific decisions when needed.

Example:

```text
color/gray/0
color/gray/50
color/gray/900

surface/default
surface/subtle
surface/inverse

text/primary
text/secondary
text/inverse

action/primary/background
action/primary/background-hover
action/primary/text
```

Use modes when the same token needs different values across light/dark, brand, density, or platform contexts.

### 5. Design Components As APIs

For each component, define:

- Purpose
- Anatomy
- Required and optional parts
- Properties
- Variants
- States
- Layout behavior
- Accessibility notes
- Content rules
- Do/don't examples
- Engineering mapping, if known

For common components, include at least:

- Button
- Link
- Icon button
- Text input
- Select or combobox
- Checkbox
- Radio
- Toggle
- Tabs
- Badge
- Tooltip
- Modal/dialog
- Toast
- Card or content container
- Table or list row
- Navigation item

Do not create all components at once if the project is small. Start with what repeats.

### 6. Stress-Test The Design

Check every serious component or screen against:

- Long text
- Short text
- Missing text
- Empty data
- Loading state
- Error state
- Disabled state
- Permission-restricted state
- Mobile/narrow layout
- Desktop/wide layout
- Dark mode, if supported
- High-density content
- Localization
- Keyboard/focus behavior, where applicable

If a component fails these checks, improve structure before visual polish.

### 7. Prepare For Developers

For implementation-ready work:

- Mark frames or sections as ready for development.
- Add annotations for behavior, data rules, and edge cases.
- Keep names stable and descriptive.
- Use variables rather than raw values.
- Include all relevant states.
- Attach tickets, specs, repos, or docs using Dev Resources when appropriate.
- Use Code Connect when Figma components map to real code components.
- Avoid detached or hidden undocumented layers in final handoff.

### 8. Use Automation Carefully

Use Figma APIs, plugins, webhooks, or MCP workflows when they remove repeated pain:

- Sync variables/tokens with a codebase.
- Audit raw values.
- Detect detached instances.
- Generate documentation.
- Attach Dev Resources.
- Map components to code.
- Extract design context for AI-assisted implementation.
- Create or update native Figma content from a structured prompt.

Respect permissions, plan limits, rate limits, and review requirements. Automation should reduce drift, not create invisible complexity.

## Audit Checklist

When reviewing Figma work, report findings in this order:

1. **Structural failures**: missing Auto Layout, poor hierarchy, detached components, brittle sizing.
2. **System failures**: raw values, inconsistent tokens, chaotic variants, missing states.
3. **Implementation failures**: unclear Dev Mode handoff, missing annotations, poor naming, no code mapping.
4. **Accessibility failures**: contrast, focus states, hit areas, disabled/error semantics, text scaling.
5. **Content failures**: no long-copy, empty, loading, or localization handling.
6. **Governance failures**: no owner, no publish process, no deprecation path.
7. **Visual craft issues**: spacing, alignment, hierarchy, rhythm, density, contrast, brand expression.

Be direct. Prioritize issues that will cause rework, inconsistent implementation, or team confusion.

## Starting From Scratch: Minimum Elite Setup

For a new brand, designer, or team starting in Figma, recommend this minimum setup:

### Foundations

- Brand color primitives and semantic color variables.
- Type scale with clear roles: display, heading, body, label, caption.
- Spacing scale, usually 4px-based unless the brand has a reason otherwise.
- Radius scale.
- Elevation rules.
- Icon rules.
- Accessibility rules for contrast, focus, and hit areas.

### Core Components

- Button with intent, size, state, loading, and icon options.
- Input with label, help text, error, disabled, and filled states.
- Checkbox, radio, toggle.
- Select or menu.
- Tabs or segmented control.
- Badge/status label.
- Tooltip.
- Modal/dialog.
- Toast/notification.
- Card/content block.
- List row/table row.
- Navigation item.

### File Hygiene

- Clear page structure.
- Named frames and sections.
- Components grouped by function.
- Local components separated from experiments.
- Archive page for old work.
- Ready-for-dev area for implementation.

### Governance

- Library owner.
- Publishing rules.
- Contribution rules.
- Naming convention.
- Version/release notes.
- Deprecation process.

## Response Patterns

### When The User Asks For Advice

Give ranked, concrete guidance. Avoid vague inspiration. Tie recommendations to practical outcomes like scalability, implementation accuracy, consistency, and speed.

### When The User Asks For A Figma System

Produce a structured system plan with:

- File architecture
- Foundation tokens
- Component inventory
- Variable strategy
- Governance rules
- Dev Mode setup
- Implementation readiness checklist

### When The User Asks For A Critique

Use a review stance:

- Lead with the highest-risk findings.
- Explain why each issue matters.
- Give a specific fix.
- Distinguish structural problems from visual preferences.

### When The User Asks For Design-To-Code Help

Prioritize:

- Clean Figma hierarchy
- Variables and code syntax
- Component mapping
- Code Connect
- Dev Mode annotations
- Screenshots or design context where useful
- Existing codebase components over generated approximations

### When The User Asks About AI Or MCP Workflows

Make clear that MCP/design-to-code context is not magic. It works best when the Figma file already has:

- Clean named layers
- Real components
- Variables
- Code Connect mappings
- Scoped selections
- Screenshots when visual fidelity matters
- Clear prompts specifying framework, component library, and implementation constraints

## Quality Bar

Before finalizing any recommendation or artifact, check:

- Does this make the design more reusable?
- Does this reduce ambiguity for engineers?
- Does this survive real content?
- Does this avoid unnecessary complexity?
- Does this preserve brand expression?
- Does this improve team speed?
- Does this give the user a next action?

If the answer is no, revise.

## Anti-Patterns

Avoid these unless deliberately creating quick throwaway exploration:

- Static frames pretending to be product design.
- Manual positioning for reusable UI.
- Raw hex colors and arbitrary spacing in production components.
- Giant component sets with unclear variant axes.
- Components that require layer digging for normal customization.
- Detached components in final work.
- Unnamed layers like `Frame 482` or `Rectangle 19`.
- Screens with only happy-path content.
- Design files with no ready-for-dev structure.
- Libraries with no owner or publishing rules.
- Automation that nobody can debug.

## Final Standard

Elite Figma work is not defined by feature count. It is defined by whether design intent becomes a durable system: visually precise, semantically named, responsive to content, easy to inspect, mapped to implementation, governed by clear rules, and fast for the whole team to use.
