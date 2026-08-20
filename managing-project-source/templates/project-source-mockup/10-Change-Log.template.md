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
project_source_framework_version: "1.2.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 10 — Change Log

Canonical logical append-only home of `CHG-*` history.

```text
CHG-ID
Timestamp
Actor / Instance
Object / Document
Previous State
New State
Reason / Trigger
Related User Instruction / DEC / CR / EVD
```
