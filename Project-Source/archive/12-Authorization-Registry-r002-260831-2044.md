---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "AUTHORIZATION-REGISTRY-001"
document_type: "AUTHORIZATION_REGISTRY"
semantic_slot: "12"
revision: 2
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-08-31T20:44:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "USER_CONFIRMED"
freshness_class: "STABLE"
project_source_framework_version: "1.7.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 12 — Authorization Registry

Canonical home of `AUTH-*` and `DEL-*`.

## Initialization Authority

Project Source initialization was executed under the user's explicit approval of the GREENFIELD Preview and subsequent instruction to proceed continuously. That tier-0 user authority is captured as `EVD-001`; it is not converted into a fabricated standing `AUTH-*` grant.

## Current Standing AUTH / DEL Records

## AUTH-001 — TASK-041 persistent Goal execution authority

- **Authority Type:** USER_EXPLICIT_PERSISTENT_GOAL_AUTHORIZATION
- **Granted By:** ACTOR-001
- **Granted At:** 2026-08-31T20:44:00+07:00
- **Purpose / Outcome:** complete TASK-041 Portable Installation Bootstrap & Project Settings Handoff through verified local Task completion
- **Parent Outcome:** `OUT-001`
- **Authorized Scope:** local read/inspection/research; architecture/design/spec refinement; implementation planning; non-destructive in-scope Framework documentation/governance edits/moves; pressure scenarios; tests/validation; debugging/corrective edits; local Git add/commit; Logical Checkpoints; Project Source continuation/evidence/completion reconciliation required by TASK-041
- **Authorization Boundary:** ProjectFramework repository local work for TASK-041 only
- **Explicitly Excluded:** push/publication; destructive operations; Root/Project Location Binding mutation; external AI/provider disclosure; storage/revelation of actual secret values; unrelated Tasks
- **Validity:** active while `OUT-001` is `ACTIVE | BLOCKED`; terminates prospectively when `OUT-001` becomes `ACHIEVED | CANCELLED | SUPERSEDED` or user revokes/narrows authority
- **Verification Requirement:** operation must remain in TASK-041 scope and satisfy active Project/Framework safety, binding, evidence, and tool/platform gates
- **Evidence:** `EVD-017`

No `DEL-*` record is created. This authorization does not transfer through Handoff (`authority_transfer: false`) and `commit ≠ push`.
