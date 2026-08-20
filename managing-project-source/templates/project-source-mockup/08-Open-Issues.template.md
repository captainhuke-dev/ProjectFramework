---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<OPEN_ISSUES_DOCUMENT_ID>"
document_type: "OPEN_ISSUES"
semantic_slot: "08"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "<CLASS>"
project_source_framework_version: "1.1.3"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 08 — Open Issues

> **CONDITIONAL:** Create an active document only when `ISS-*`, `DRIFT-*`, or `CONFLICT-*` objects exist or the project needs this canonical home.

## Active Issues

### <ISS / DRIFT / CONFLICT>-<NNN> — <TITLE>
- **Type:** <TYPE>
- **Status:** <STATUS>
- **Affected Scope:** <SCOPE>
- **Owner:** <ACTOR_REF>
- **Evidence:** <EVD_REFS>
- **Blocking Semantics:** <CONTENT>
- **Resolution / Next Action:** <ACTION>
