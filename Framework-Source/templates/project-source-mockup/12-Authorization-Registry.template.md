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
project_source_framework_version: "1.12.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 12 — Authorization Registry

Canonical home of `AUTH-*` and `DEL-*`.

## AUTH-<NNN> — <TITLE>
- **Grantor:** <ACTOR_REF>
- **Grantee:** <ACTOR_REF>
- **Related Goal Outcome:** <OUT-* or NOT_APPLICABLE>
- **Allowed Actions:** <ACTIONS>
- **Scope / Paths:** <SCOPE>
- **Explicitly Included Shared / External Effects:** <PUSH_TARGET / DESTRUCTIVE_OPERATION+TARGET / ROOT_BINDING_MUTATION+TARGET / DISCLOSURE_SCOPE / NONE>
- **Forbidden Actions / Effects:** <CONTENT>
- **Risk Ceiling:** <R0_R1_R2_R3>
- **Start:** <ISO8601>
- **Expiry / Termination:** <CONTENT>
- **Revocation Trigger:** <CONTENT>
- **Status:** <STATUS>
- **Evidence / User Approval Reference:** <EVD_OR_USER_APPROVAL_REF>

For Goal-related authorization, the parent `OUT-*` terminal state `ACHIEVED | CANCELLED | SUPERSEDED` terminates or supersedes dependent Goal authority. A Goal `AUTH-*` is persistent Project Source truth; `09 Handoff` may reference it but `authority_transfer: false` remains binding.

Unless explicitly narrowed, Goal `AUTH-*` may cover bounded local design/plan/edit/test/fix/verify/local-commit/checkpoint work. Push, destructive effects, Root/Binding mutation, and external disclosure require their exact opt-in semantics from current Root Governance. Actual secret values are never stored here.

### Optional Standing External-AI Disclosure `AUTH-*` Fields

```text
Consumer / Grantee
Provider / Tool / Provider Class
Allowed Content / Source Scope
Allowed Disclosure Classes
Purpose
Minimum-context / Redaction Conditions
Forbidden Content / Effects
Start
Expiry / Termination / Revocation
Risk Ceiling when applicable
Evidence / Approval Reference
Status
```

Standing disclosure authority is provider/purpose/content scoped. `EXTERNAL_OK` classification or provider eligibility is not authorization. An exact one-off User Explicit Instruction may authorize one bounded disclosure action without materializing synthetic standing `AUTH-*`.

## DEL-<NNN> — <TITLE>
- **Parent Authorization:** <AUTH_REF>
- **Delegated Scope:** <MUST_NOT_EXCEED_PARENT>
- **Status:** <STATUS>
