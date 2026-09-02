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
project_source_framework_version: "1.13.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 11 — Actor Registry

Canonical home of `ACTOR-*` and `INST-*`. Role is descriptive only; authority is in `12`.

## Responsibility Mapping

Key each row by governed scope:

```text
Scope
Responsible
Accountable
Consulted
Informed
```

**Responsibility ≠ Authority.** Mapping does not grant approval/mutation permission.
