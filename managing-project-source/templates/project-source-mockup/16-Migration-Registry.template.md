---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<MIGRATION_REGISTRY_DOCUMENT_ID>"
document_type: "MIGRATION_REGISTRY"
semantic_slot: "16"
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

# 16 — Migration Registry

Canonical home of `MIG-*`.

Record source/target, compatibility, affected documents/objects, steps, rollback, approval, validation/evidence, lifecycle.

Framework `1.2.0` migration explicitly checks pre-existing slot `91` collision and forbids automatic promotion of old free-text into new management Stable IDs.
