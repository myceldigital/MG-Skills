# Strategy Tree Module

Use this module when the task is non-trivial, high-risk, or likely to require multiple implementation paths.

```text
STRATEGY TREE:
Before acting, generate up to 3 candidate strategies.

For each strategy, specify:
- hypothesis: why this path should work
- observed evidence: files, docs, tests, logs, or artifacts supporting it
- first evidence-producing action: the smallest action that can confirm or disconfirm the path
- expected observation: what success should look like
- disconfirming signal: what would prove the path is wrong or too risky
- risk class: read-only, reversible edit, rollback-required edit, external side effect, or irreversible action
- rollback or containment: how to safely undo or isolate the work
- fallback branch: what to try next if this path fails
- max cycles before reassessment: usually 2-3 for the same failure mode

Selection rule:
Choose the strategy with the best combination of success probability, minimality, reversibility, verification clarity, architectural fit, scope control, and safe continuation options.

Backtracking rule:
If a branch fails, do not repeat it unchanged. Either change the hypothesis, inspect a new evidence source, reduce to a smaller subgoal, or move to a fallback branch.
```
