---
name: elite-api-documentation
description: Use this skill when creating, rewriting, auditing, or maintaining elite API documentation for REST, GraphQL, RPC, SDK, webhook, event, platform, or developer-product APIs. It guides Codex to produce accurate, findable, executable, production-grade API docs with strong concepts, task guides, references, examples, troubleshooting, versioning, and maintenance workflows.
---

# Elite API Documentation

Use this skill to produce API documentation that helps developers succeed quickly, reason accurately, and operate safely in production. Treat documentation as part of the API contract, not as marketing copy or after-the-fact explanation.

## Core Standard

Elite API documentation must be:

- **True**: technically accurate, verified against the implementation, schema, SDK, or authoritative source.
- **Findable**: organized around user intent, system concepts, and predictable reference structure.
- **Executable**: examples are complete, realistic, current, and runnable where possible.
- **Operational**: covers errors, limits, retries, security, observability, versioning, migration, and production failure.
- **Maintainable**: tied to owners, source-of-truth artifacts, release workflows, tests, and freshness checks.
- **Humane**: respects the developer's time, context, uncertainty, and production risk.

If these goals conflict, preserve truth first, then usability, then elegance.

## Immutable Laws

1. Documentation is part of the API. If the docs are wrong, the API is broken from the developer's point of view.
2. Truth beats style. Beautiful wrong docs are worse than ugly correct docs.
3. The first success must be real. A quickstart must produce a visible, verifiable outcome.
4. Concepts, guides, reference, examples, troubleshooting, and changelogs must not be blended into one undifferentiated page.
5. Every hidden prerequisite is a bug.
6. Name one concept one way. Do not alternate between near-synonyms unless they are distinct domain objects.
7. Explain the model before the maze. Developers need resources, relationships, lifecycles, permissions, and state transitions.
8. Examples are product code, not decoration. They must be maintained like code.
9. Failure is first-class documentation. Errors, retries, timeouts, partial failure, and debugging deserve explicit treatment.
10. Production is not an edge case. Document security, quotas, observability, deployment, rollback, and operational limits.
11. Versioning must be impossible to miss.
12. Reference pages must be exhaustive and predictable.
13. Constraints are part of the contract. Limits, unsupported behavior, ordering, consistency, retention, and regional rules must be explicit.
14. Authentication must be over-explained.
15. The docs must help users choose between APIs, SDKs, auth flows, versions, and integration paths.
16. Search is not information architecture.
17. Docs must be maintained like software.
18. Documentation should push back on bad API design.
19. Do not document around avoidable pain when a better API, SDK, dashboard, validation, or error message can solve it.
20. Measure developer success, not page output.

## Operating Modes

Identify the user's requested mode before writing.

- **Create**: Build new docs for an API, SDK, endpoint, feature, or platform.
- **Rewrite**: Improve existing docs while preserving correct content and public contract details.
- **Audit**: Review docs for accuracy, usability, completeness, structure, maintainability, and production readiness.
- **Repair**: Fix broken examples, stale references, vague concepts, missing prerequisites, or inaccurate behavior.
- **Reference design**: Define a repeatable reference-page structure for endpoints, objects, SDK methods, events, or GraphQL schema entries.
- **Onboarding design**: Create quickstarts, tutorials, first-call flows, and getting-started journeys.
- **Migration design**: Explain version changes, deprecations, breaking changes, and upgrade paths.
- **Troubleshooting design**: Build diagnostic docs for errors, webhooks, auth, rate limits, SDK setup, or production failures.

When the user does not specify a mode, infer it from the artifact:

- New API or feature: Create.
- Existing page with quality issues: Rewrite or repair.
- Request for "review": Audit first, then propose or implement fixes if asked.
- Version change or deprecation: Migration design.
- Repeated support issue: Troubleshooting design.

## Context To Gather

Before drafting docs, gather only the context needed for the requested scope.

For any API documentation task, identify:

- The API type: REST, GraphQL, gRPC, RPC, SDK, CLI, webhook, event stream, schema, or hybrid.
- The target audience: beginner, experienced integrator, partner developer, internal engineer, admin, DevOps, security, data engineer, frontend, backend, mobile, AI agent, or SDK user.
- The user goal: what job the developer is trying to complete.
- The canonical source of truth: OpenAPI spec, GraphQL schema, protobuf, SDK source, endpoint implementation, product spec, API design doc, tests, release notes, or existing docs.
- The API surface: resources, methods, objects, events, SDK classes, permissions, auth flows, versions, and environments.
- The product state: beta, GA, deprecated, internal, private preview, breaking change, or migration.
- The operational realities: rate limits, quotas, pagination, consistency, retries, idempotency, webhooks, async jobs, observability, security, data retention, regional rules, and failure modes.

If the task is blocked by missing facts, do not invent behavior. Mark assumptions explicitly and ask for the smallest missing set of facts. If code, schemas, or tests are available locally, inspect them before asking.

## Workflow

### 1. Define The Developer Job

Start with the developer's actual task, not the API object.

Write down:

- "The developer wants to..."
- "They already know..."
- "They likely do not know..."
- "They must complete these prerequisites..."
- "They are successful when..."
- "They may fail because..."

Use this to determine whether the page should be a concept, guide, reference page, troubleshooting page, migration guide, or index.

### 2. Model The API

Before writing prose, build the mental model.

Capture:

- Core resources and their relationships.
- Resource ownership: account, organization, workspace, project, user, app, environment, region, tenant.
- State transitions: pending, active, failed, canceled, expired, archived, deleted, completed.
- Actions that change state.
- Read-only versus mutating operations.
- Sync versus async behavior.
- Eventual consistency or ordering guarantees.
- Idempotency and retry behavior.
- Authentication and authorization boundaries.
- Permission scopes, roles, and token types.
- Rate limits, quotas, pagination, filters, and sorting.
- Error families and recovery paths.
- Webhook, event, or callback behavior.
- Versioning and deprecation behavior.

If the model is hard to explain simply, flag possible API design debt: inconsistent naming, overloaded resources, implicit state, unclear ownership, missing errors, confusing auth, or duplicate flows.

### 3. Choose The Documentation Architecture

Separate content by job.

- **Overview**: What the API is for, who should use it, main concepts, environments, auth summary, and links to next steps.
- **Quickstart**: Fastest real path to a visible success.
- **Concepts**: Mental models, resources, lifecycle, permissions, event flow, architecture, and constraints.
- **How-to guides**: Task-focused procedures for common jobs.
- **Reference**: Exact contract for endpoints, methods, objects, events, SDK methods, parameters, responses, errors, and permissions.
- **Examples**: Runnable patterns for realistic use cases.
- **Troubleshooting**: Symptoms, causes, confirmation steps, fixes, and escalation data.
- **Versioning and migration**: Versions, changelogs, breaking changes, deprecations, compatibility, and upgrade paths.
- **Production guide**: Security, retries, observability, scaling, limits, rollout, rollback, monitoring, and incident handling.

Do not force everything into one page. When the user asks for one document, include clear sections and anchors that preserve these jobs.

### 4. Design The First Success

For any getting-started or quickstart content:

- State prerequisites before commands.
- Include account, environment, token, permission, SDK/runtime, and test-data requirements.
- Use copyable, complete code.
- Show the exact request.
- Show an expected response or visible result.
- Tell the user how to confirm success.
- Explain the most likely first failure.
- Link to the next logical task.

A quickstart is not complete until the developer can answer: "Did it work?"

### 5. Write Exact Reference

Reference pages must be predictable and exhaustive.

For REST endpoints include:

- Method and path.
- Purpose in one precise sentence.
- Authentication requirement.
- Required permissions or scopes.
- Path parameters.
- Query parameters.
- Headers.
- Request body schema.
- Response body schema.
- Status codes.
- Error codes.
- Rate limits or quotas.
- Idempotency behavior for mutating requests.
- Pagination, filtering, sorting, and ordering.
- Side effects.
- Async behavior and job/status polling if relevant.
- Webhooks or events emitted by the operation.
- Example request and response.
- SDK equivalents where relevant.
- Version availability and deprecation notes.

For GraphQL include:

- Operation type: query, mutation, subscription.
- Schema entry point.
- Arguments and input objects.
- Return type and important nested objects.
- Required scopes or permissions.
- Cost or complexity behavior.
- Pagination pattern.
- Errors and partial-data behavior.
- Example operation with variables.
- Example response.
- Version availability and deprecation notes.

For SDK docs include:

- Install command and version requirement.
- Import or initialization.
- Authentication setup.
- Method signature.
- Parameters and types.
- Return type.
- Exceptions or error objects.
- Async or promise behavior.
- Retries and timeout configuration.
- Thread/process safety if relevant.
- Equivalent API endpoint if useful.
- Complete example.

For webhooks/events include:

- Event name and purpose.
- When it fires.
- Delivery semantics: at-most-once, at-least-once, retry schedule, ordering, duplication.
- Payload schema.
- Signature verification.
- Idempotency guidance.
- Expected response from receiver.
- Timeout behavior.
- Replay or redelivery options.
- Example payload.
- Local testing guidance.
- Common failure modes.

### 6. Make Examples Production-Aware

Examples should be minimal but not fake.

An elite example:

- Runs as written after prerequisites are met.
- Uses realistic values and names.
- Avoids placeholder sprawl.
- Shows request and response together.
- Demonstrates the recommended path, not every possible path.
- Uses idiomatic language-specific code.
- Uses environment variables for secrets.
- Includes error handling when the absence of it would teach unsafe behavior.
- Calls out test mode versus live mode when relevant.
- Avoids obsolete SDKs, deprecated endpoints, or soon-to-be-removed versions.

Do not use examples that hide required setup. If setup is too long, link to a setup guide and state that dependency clearly.

### 7. Document Failure And Recovery

For every serious integration path, document the unhappy path.

Cover:

- Authentication errors: missing token, expired token, wrong token type, wrong environment, missing scope.
- Authorization errors: role, organization, workspace, resource ownership, tenant mismatch.
- Validation errors: invalid field, wrong type, missing required field, enum mismatch, unsupported combination.
- Rate limits and quotas: how limits are measured, headers, reset behavior, retry timing, backoff.
- Timeouts and network failures: safe retry conditions and idempotency keys.
- Async failures: job states, polling, callbacks, partial success, cancellation.
- Webhook failures: signature mismatch, duplicate delivery, delayed delivery, retries, receiver timeout.
- Pagination mistakes: missing pages, cursor expiration, changing result sets, ordering assumptions.
- Consistency issues: stale reads, propagation delay, read-after-write behavior.
- Production debugging: request IDs, trace IDs, logs, dashboards, support escalation data.

Use diagnostic tables when helpful:

| Symptom | Likely cause | How to confirm | How to fix |
| --- | --- | --- | --- |
| 401 Unauthorized | Token is missing or for the wrong environment | Inspect auth header and token source | Use a valid token for the target environment |

### 8. Explain Choices

When a platform has multiple paths, include decision guidance.

Use direct recommendations:

- Use this API when...
- Do not use this API when...
- Use this SDK if...
- Choose OAuth when...
- Choose service-account authentication when...
- Use webhooks instead of polling when...
- Use bulk operations when...
- Use async jobs when...

Avoid making developers infer product strategy from scattered pages.

### 9. Maintain The Docs Like Software

When creating or improving docs, recommend or implement maintenance mechanisms appropriate to the project.

Use:

- Generated reference from OpenAPI, GraphQL schema, protobuf, or SDK source where possible.
- Tested examples in CI.
- Docs review gates for API changes.
- Release checklist items for docs.
- Page ownership metadata.
- Version badges and deprecation notices.
- Link checking.
- Style and terminology linting.
- Freshness checks for examples, screenshots, SDK names, and dashboard paths.
- Analytics for failed searches, high-exit pages, support deflection, and onboarding completion.

If maintenance is not addressed, the docs may be temporarily good but structurally fragile.

### 10. Review Against The Quality Bar

Before finalizing, run this checklist.

Accuracy:

- Is every behavior verified or explicitly marked as an assumption?
- Are parameter names, types, defaults, constraints, and examples correct?
- Are version, beta, deprecation, and compatibility details visible?
- Are SDK examples compatible with current SDK syntax?

Usability:

- Can the target developer identify the right starting point?
- Are prerequisites stated before they are needed?
- Does the quickstart produce a visible result?
- Are concepts explained before advanced procedures rely on them?
- Are common choices explained?

Completeness:

- Are auth, permissions, scopes, environments, and token types covered?
- Are errors, retries, rate limits, pagination, idempotency, and webhooks covered where relevant?
- Are production concerns covered or linked?
- Are unsupported use cases and constraints explicit?

Structure:

- Are concepts, guides, reference, examples, troubleshooting, and changelogs separated?
- Is navigation predictable?
- Are headings task-oriented and scannable?
- Does the page avoid burying critical warnings in prose?

Maintainability:

- Is there a source of truth?
- Can examples be tested?
- Is ownership clear?
- Will version changes be reflected automatically or through a defined process?

## Writing Style

Use clear, precise, developer-respecting prose.

Prefer:

- "Create a payment intent before you collect payment details."
- "The request fails with `403` if the token does not include `orders:write`."
- "Use an idempotency key when retrying this request after a timeout."
- "The webhook may be delivered more than once."

Avoid:

- "Simply", "easily", "just", "seamlessly", unless the task is genuinely simple.
- Marketing claims in reference docs.
- Vague phrases like "works with your data", "set things up", "proper permissions", or "handle errors accordingly".
- Passive warnings that hide consequences.
- Unexplained acronyms.
- Multiple names for one concept.

Use requirement language consistently:

- **Must**: required for correctness or security.
- **Should**: strongly recommended, but not required.
- **Can**: optional capability.
- **May**: possible behavior, often from the API.
- **Do not**: unsafe, unsupported, deprecated, or incorrect.

## Recommended Templates

Use these compact structures and expand only where the task needs detail:

- **API overview**: what it does, who should use it, core concepts, common workflows, auth and environments, SDKs/tools, limits and production constraints, versioning, quickstart, reference, troubleshooting.
- **Quickstart**: goal, visible result, prerequisites, setup, authenticate, first request, expected response, success check, common first errors, next steps.
- **How-to guide**: goal, when to use it, before you begin, permissions, steps, full example, expected result, error handling, production considerations, related tasks.
- **Endpoint reference**: title, purpose, method/path, availability/version, auth/permissions, path/query params, headers, request body, responses, errors, rate limits/idempotency, side effects/events, examples, SDK equivalents.
- **Object reference**: object name, purpose, lifecycle, ownership, fields, types, nullability, defaults, constraints, expandable/nested fields, state values, related operations/events, example object, version notes.
- **Error reference**: code/family, meaning, trigger conditions, retry safety, required fix, example response, logs/request IDs/headers, support escalation data.
- **Migration guide**: affected users, changes, reason if useful, deadline, before/after behavior, required code/data changes, testing checklist, rollout/rollback, common migration errors.
- **Troubleshooting page**: symptoms, fast checks, diagnostic table, detailed causes, fixes, prevention, what to log, when to contact support.

## Audit Rubric

When auditing existing docs, rate each area as Pass, Partial, or Fail and give concrete fixes.

- First success: Can a new developer complete a real first call?
- Conceptual model: Are resources, states, relationships, permissions, and constraints clear?
- Reference precision: Are every parameter, response, error, permission, and side effect documented?
- Example quality: Are examples current, runnable, realistic, and idiomatic?
- Production readiness: Are auth, retries, idempotency, rate limits, pagination, observability, and failure covered?
- Information architecture: Can users find the right content without search-dependent scavenging?
- Versioning: Are versions, deprecations, and migration paths visible?
- Maintainability: Are docs tied to source-of-truth artifacts, owners, and tests?
- Developer choice: Do docs explain which API, SDK, auth flow, or pattern to use?
- API design feedback: Do docs reveal confusing or inconsistent product design?

Lead audits with the highest-risk issues first. Tie each finding to user impact.

## Common Documentation Smells

Watch for these and fix them directly:

- A quickstart that lacks expected output.
- Authentication described only as "use your API key".
- Prerequisites scattered after the steps that need them.
- Examples that omit imports, initialization, or token setup.
- Reference docs with no examples.
- Examples with no responses.
- Error docs that list codes but not recovery actions.
- Webhook docs with no retry, ordering, duplicate, or signature-verification guidance.
- Rate-limit docs with no headers, reset behavior, or backoff recommendation.
- Pagination docs that do not explain cursor lifetime or ordering.
- Versioning docs that list changes but do not provide migration steps.
- SDK docs that mirror endpoint names but do not explain idiomatic usage.
- Marketing claims mixed into reference pages.
- Multiple terms for one resource.
- A warning that appears only after the dangerous step.
- A dashboard instruction that is likely to rot but has no freshness owner.

## Output Expectations

When producing docs, include the artifact in a polished form, not only advice.

When producing an audit, structure the answer as:

1. Findings ordered by severity.
2. Concrete fixes.
3. Missing information or assumptions.
4. Suggested revised structure or sample rewrite when useful.

When producing a rewrite, preserve correct technical facts and improve:

- Accuracy.
- Prerequisite ordering.
- Scannability.
- Examples.
- Failure guidance.
- Links between concepts, guides, and reference.

When producing new docs, make the first draft complete enough that an engineer or product owner can review facts, not guess the intended structure.

## Final Gate

Before returning work, ask:

- Can the target developer succeed without private context?
- Are all prerequisites visible before use?
- Are all examples executable or clearly illustrative?
- Is failure documented as carefully as success?
- Is the source of truth clear?
- Will this page survive the next API release?
- Did the docs expose any API design problem that should be raised?

If the answer to any question is no, either fix it or state the remaining gap explicitly.
