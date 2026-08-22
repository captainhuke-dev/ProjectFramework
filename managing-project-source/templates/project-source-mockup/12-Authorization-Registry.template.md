---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<AUTHORIZATION_REGISTRY_DOCUMENT_ID>"
document_type: "AUTHORIZATION_REGISTRY"
semantic_slot: "12"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "<CLASS>"
project_source_framework_version: "1.2.5"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 12 — Authorization Registry

Canonical home of `AUTH-*` and `DEL-*`.

## AUTH-<NNN> — <TITLE>
- **Grantor:** <ACTOR_REF>
- **Grantee:** <ACTOR_REF>
- **Allowed Actions:** <ACTIONS>
- **Scope / Paths:** <SCOPE>
- **Forbidden Actions / Effects:** <CONTENT>
- **Risk Ceiling:** <R0_R1_R2_R3>
- **Start:** <ISO8601>
- **Expiry / Termination:** <CONTENT>
- **Status:** <STATUS>

## DEL-<NNN> — <TITLE>
- **Parent Authorization:** <AUTH_REF>
- **Delegated Scope:** <MUST_NOT_EXCEED_PARENT>
- **Status:** <STATUS>
