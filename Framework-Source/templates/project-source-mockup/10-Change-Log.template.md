---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<CHANGE_LOG_DOCUMENT_ID>"
document_type: "CHANGE_LOG"
semantic_slot: "10"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "<CLASS>"
project_source_framework_version: "1.8.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 10 — Change Log

Canonical home of logical append-only `CHG-*` history.

## CHG-<NNN> — <TITLE>
- **Timestamp:** <ISO8601>
- **Actor / Instance:** <ACTOR / INST REFS>
- **Object / Document:** <REF>
- **Previous State:** <CONTENT>
- **New State:** <CONTENT>
- **Reason / Trigger:** <CONTENT>
- **Related User Instruction / DEC / EVD:** <REFS>
