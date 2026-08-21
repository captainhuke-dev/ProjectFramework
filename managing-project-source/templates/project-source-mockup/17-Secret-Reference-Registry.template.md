---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<SECRET_REFERENCE_REGISTRY_DOCUMENT_ID>"
document_type: "SECRET_REFERENCE_REGISTRY"
semantic_slot: "17"
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

# 17 — Secret Reference Registry

Canonical home of `SECRET-*` metadata only. Actual secret values are forbidden.

## SECRET-<NNN> — <TITLE>
- **Secret Type:** <TYPE>
- **System / Environment:** <SYSTEM>
- **External Storage Reference:** <REFERENCE_ONLY>
- **Required Authority:** <AUTH_REF>
- **Status:** <STATUS>

```yaml
secret_value_present: false
```
