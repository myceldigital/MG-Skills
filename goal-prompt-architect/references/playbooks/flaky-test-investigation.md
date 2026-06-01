# Playbook: Flaky Test Investigation

Trigger when the mission involves intermittent failures, nondeterministic tests, race conditions, or CI failures that do not reproduce consistently.

Required additions:
- capture failing command, seed, environment, timing, and recent changes
- repeat only enough times to classify the failure; do not brute-force indefinitely
- isolate shared state, time, randomness, network, filesystem, and concurrency assumptions
- create the smallest reproducible diagnostic artifact
- distinguish product bug, test bug, infrastructure issue, and insufficient oracle

Done when the failure is either fixed with evidence, classified with a reproducible handoff, or blocked by a hard dependency with no safe parallel work.
