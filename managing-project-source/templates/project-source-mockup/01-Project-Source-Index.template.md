---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<PROJECT_SOURCE_INDEX_DOCUMENT_ID>"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "<CLASS>"
project_source_framework_version: "1.2.2"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 01 — Project Source Index

Front Door + derived Active Document Registry + task routing.

## Routing

```text
00 Framework / governance root
03 current state / health / next action
04 DEC-* / Decision Revalidation
05 REQ-*
08 ISS-* / DRIFT-* / CONFLICT-* / KNOWLEDGE_DEBT
40 Tech Stack / technical / source / config / runtime blueprint when active
60 installation / deployment / operations blueprint when active
91 RISK-* / ASM-* / MS-* / OUT-* / DEP-* / CR-* / GATE-* when active
```

The derived registry is not manually authoritative.
