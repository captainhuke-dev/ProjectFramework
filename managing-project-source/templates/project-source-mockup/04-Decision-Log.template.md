---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<DECISION_LOG_DOCUMENT_ID>"
document_type: "DECISION_LOG"
semantic_slot: "04"
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

# 04 — Decision Log

Canonical home of `DEC-*`.

## DEC-<NNN> — <TITLE>

- **Status:** <STATUS>
- **Decision:** <CURRENT_DECISION>
- **Reason:** <REASON>
- **Approved By:** <ACTOR_OR_USER>
- **Approved At:** <ISO8601>
- **Validity Basis:** <BASIS>
- **Review Trigger:** <TRIGGER>
- **Review By:** <DATE_OR_EVENT>
- **Last Revalidated:** <ISO8601_OR_NONE>
- **Revalidation Status:** <NOT_DUE | REVIEW_DUE | REVALIDATED | SUPERSEDED>
- **Revalidation Evidence:** <EVD_REFS_OR_NONE>
- **Related:** <REQ / ACT / RISK / ASM / DEP / CR / GATE / EVD>
- **Supersedes / Superseded By:** <REFS_OR_NONE>

Current semantics must resolve without archive traversal.
