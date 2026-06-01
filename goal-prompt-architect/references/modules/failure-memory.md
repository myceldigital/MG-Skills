# Failure Memory Module

Use this module for long-running or failure-prone autonomous work.

```text
FAILURE MEMORY:
Every failed attempt must produce a concise failure record:
- attempt: what was tried
- expected result: what should have happened
- actual result: what happened instead
- error signal: test failure, exception, mismatch, missing artifact, unclear observation, or other signal
- root-cause hypothesis: best current explanation
- what this rules out: assumption, strategy, file, command, or approach that is now less likely
- what to avoid repeating: exact command, edit, or assumption that should not be retried unchanged
- next changed strategy: what will be different on the next attempt
- confidence: low, medium, or high

Classify each failure as one of:
- environment issue
- wrong assumption
- insufficient context
- implementation bug
- test oracle issue
- dependency/tooling issue
- scope/risk boundary issue

Do not repeat the same failed action more than twice without changing inputs, assumptions, or strategy.
```
