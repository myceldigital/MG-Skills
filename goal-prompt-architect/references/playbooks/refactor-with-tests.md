# Playbook: Refactor With Tests

Trigger when the mission asks for structural improvement while preserving behavior.

Required additions:
- identify invariants before editing
- capture existing behavior through tests, snapshots, fixtures, or diagnostic output
- move the smallest vertical slice first
- run narrow tests after each meaningful change
- compare outputs before and after the refactor
- inspect the diff for unrelated changes before DONE

First green is not DONE. After the first passing check, run one broader verification level and a maintainer-style diff review.
