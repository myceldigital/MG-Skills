# Compact /goal Prompt Template

Use this when the user wants a shorter prompt or the task is low-risk.

```text
/goal

GOAL:
<one measurable outcome>

CONTEXT:
<known project/repo/workflow context>
<files/docs/tools to inspect first>

CONSTRAINTS:
Preserve:
- <existing behavior or standards>

Do not:
- <forbidden changes/actions>

Approval required before:
- <high-risk or external-side-effect actions>

SUCCESS CRITERIA:
1. <criterion>
2. <criterion>
3. <criterion>

PLAN:
First inspect the relevant context and restate understanding.
Rank key uncertainties by impact, confidence, and reversibility.
Choose the smallest sufficient in-scope change.
Proceed only on low-risk reversible assumptions.

VERIFY:
Run:
- <narrow check>
- <lint/typecheck/build/test/manual check>

Map each success criterion to evidence.
State anything that could not be verified and why.

DONE WHEN:
All success criteria are met, required verification passes or is explicitly bounded, and no extra scope is added.

STOP RULES:
Stop if the goal is satisfied, scope expansion is required, high-impact ambiguity remains, or a high-risk/irreversible action needs approval.

OUTPUT:
Provide summary, changed files/artifacts, checks run, evidence, risks, and follow-ups.
```
