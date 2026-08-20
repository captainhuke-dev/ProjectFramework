---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<ACTOR_REGISTRY_DOCUMENT_ID>"
document_type: "ACTOR_REGISTRY"
semantic_slot: "11"
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

# 11 — Actor Registry

Canonical home of `ACTOR-*` and `INST-*`.

## ACTOR-<NNN> — <DISPLAY_NAME>
- **Actor Type:** <TYPE>
- **Platform:** <PLATFORM>
- **Role:** <DESCRIPTIVE_ROLE_ONLY>
- **Status:** <STATUS>

## INST-<NNN> — <INSTANCE>
- **Actor:** <ACTOR_REF>
- **Instance / Session:** <IDENTIFIER>
- **Status:** <STATUS>

Role is descriptive only; authority is governed by slot `12`.
