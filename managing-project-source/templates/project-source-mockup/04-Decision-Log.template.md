---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<DECISION_LOG_DOCUMENT_ID>"
document_type: "DECISION_LOG"
semantic_slot: "04"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "<CLASS>"
project_source_framework_version: "1.1.2"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 04 — Decision Log

Canonical home of `DEC-*`.

## Current Decisions

### DEC-<NNN> — <TITLE>
- **Status:** <STATUS>
- **Decision:** <MATERIALIZED_CURRENT_DECISION>
- **Reason:** <REASON>
- **Alternatives / Rejections:** <WHEN_MATERIAL>
- **Approved By:** <ACTOR_OR_AUTHORITY>
- **Approved At:** <ISO8601>
- **Related:** <REQ / ACT / EVD REFS>
- **Supersedes / Superseded By:** <REFS_OR_NONE>

Current semantics must be materialized here or linked to an active/current canonical Detail Document; archive-dependent shorthand is not authoritative current payload.
