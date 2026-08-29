---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<ACTION_REGISTRY_DOCUMENT_ID>"
document_type: "ACTION_REGISTRY"
semantic_slot: "15"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "<CLASS>"
project_source_framework_version: "1.8.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 15 — Action Registry

Canonical home of `ACT-*`.

## ACT-<NNN> — <TITLE>
- **Status:** <TODO | IN_PROGRESS | DONE | BLOCKED | CANCELLED>
- **Owner:** <ACTOR_REF>
- **Scope:** <CONTENT>
- **Related REQ / DEC / ISS:** <REFS>
- **Exact Next Step:** <EXECUTABLE_ACTION>
- **Affected Verification / Completion Criteria:** <CRITERIA>
- **Verification Result / Evidence Pointer:** <PASS_FAIL_BLOCKED_AND_EVD_OR_REFERENCE>
- **Completion Commit(s):** <OBSERVED_GIT_SHA_OR_NOT_APPLICABLE>
- **Remaining Working-tree State:** <CLEAN_OR_EXPLAINED_WIP_OR_NOT_APPLICABLE>

For Material Git-backed mutation, `DONE` requires a Verified Task Completion Checkpoint; required completed state cannot remain only uncommitted. Read-only/no-mutation Actions require no synthetic commit; `WIP commit ≠ Task DONE`; `commit ≠ push`.

**Session Envelope (`ENV-*`)** — pre-approved bounded operation scope: allowed operation types, target surfaces, expiry (session end / task completion / explicit time), prohibited zones. Envelopes never override fail-closed governance (location/binding changes, Root Governance, schema authority, secrets, push keep their own approval gates).
