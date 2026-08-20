---
project_uuid: "12000000-0000-4000-8000-000000000001"
project_id: "GOLDEN-SW-001"
project_name: "HarborDesk Reference Service"
document_id: "AUTHORIZATIONS-001"
document_type: "AUTHORIZATION_REGISTRY"
semantic_slot: "12"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-20T11:45:00+07:00"
updated_at: "2026-08-20T11:45:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-GOLDEN-001"
epistemic_status: "VERIFIED"
freshness_class: "CHANGEABLE"
project_source_framework_version: "1.2.0"
project_source_schema_version: "1.0.0"
synthetic_reference: true
---

# 12 — Authorization Registry

## AUTH-001 — Documentation / Reference Maintenance Authority

- **Grantor:** ACTOR-001
- **Grantee:** ACTOR-002
- **Allowed Actions:** edit/review synthetic Project Source documentation and evidence references
- **Scope:** `examples/golden-reference-software-project/Project-Source/`
- **Risk Ceiling:** R1 REVERSIBLE_LOCAL
- **Start:** 2026-08-20T11:45:00+07:00
- **Termination:** When the synthetic reference snapshot is superseded or authorization is revoked
- **Status:** ACTIVE
- **Forbidden Actions:** production deployment; external-system mutation; creation/use of real credentials; creation of application runtime, Docker images, or real infrastructure

`AUTH-001` does not authorize R2/R3 actions. Responsibility mapping in `11` does not extend this authority.
