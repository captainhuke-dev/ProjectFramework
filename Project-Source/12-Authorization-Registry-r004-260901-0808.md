---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "AUTHORIZATION-REGISTRY-001"
document_type: "AUTHORIZATION_REGISTRY"
semantic_slot: "12"
revision: 4
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-01T08:08:00+07:00"
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
- **Validity:** TERMINATED at 2026-08-31T21:45:00+07:00; parent `OUT-001` achieved and this authority permits no future execution
- **Verification Requirement:** terminal — no new operation may rely on AUTH-001 after 2026-08-31T21:45:00+07:00; historical completed actions/evidence remain preserved
- **Status:** TERMINATED
- **Expiry / Termination:** parent `OUT-001` ACHIEVED after TASK-041 AFFECTED `273/273`, RELEASE_FULL `248/248`, and committed release evidence
- **Evidence:** `EVD-017`, `EVD-019`

No `DEL-*` record is created. This authorization does not transfer through Handoff (`authority_transfer: false`) and `commit ≠ push`.


## AUTH-002 — TASK-041 publication reconciliation Goal authority

- **Authority Type:** USER_EXPLICIT_PERSISTENT_GOAL_AUTHORIZATION
- **Granted By:** ACTOR-001
- **Granted At:** 2026-09-01T08:08:00+07:00
- **Purpose / Outcome:** finish TASK-041 PR #26 post-merge Project Source reconciliation and persist corrected publication/routing truth to canonical `main`
- **Parent Outcome:** `OUT-002`
- **Authorized Scope:** read/verify PR #26 and `origin/main`; non-destructive Project Source/Task metadata reconciliation; repair stale current routing pointers; local add/commit; exact fast-forward push of the validated terminal reconciliation commit to `captainhuke-dev/ProjectFramework` branch `main`; post-push verification
- **Explicitly Included Shared / External Effects:** push exact reconciliation commit(s) to `origin/main` only when fresh base proves fast-forward from observed `2bfe5efbb24480bc44dbd8e949ed632af4d759ee`
- **Explicitly Excluded:** force push; branch deletion; destructive operations; Root/Project Location Binding mutation; Framework distribution edits; external AI/provider disclosure; actual secret values; unrelated Tasks
- **Validity:** active while `OUT-002` is ACTIVE/BLOCKED; terminates when reconciliation terminal commit is observed on canonical `origin/main` or user revokes/narrows
- **Verification Requirement:** `origin/main` freshness, clean worktree, Project Source integrity, unchanged Framework-Source tree, fast-forward push, and fresh post-push remote observation
- **Status:** ACTIVE
- **Evidence:** `EVD-020`

No `DEL-*` record is created. `commit ≠ push`; this AUTH explicitly includes only the bounded terminal reconciliation push described above.
