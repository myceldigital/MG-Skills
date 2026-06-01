# Playbook: Regulated Feature Change

Trigger when the repo or workflow touches clinical, legal, financial, privacy-sensitive, or compliance-significant behavior.

Required additions:
- use synthetic or explicitly approved test data only
- preserve auditability and human-review boundaries
- stop before production data, real customer/patient/client impact, or compliance-significant interpretation
- separate local reversible implementation from approval-required operational changes
- include risk, rollback, and evidence notes in the final report

Long runtime does not expand authority. Marathon work may continue on safe analysis, local reversible edits, synthetic-data validation, and documentation only.
