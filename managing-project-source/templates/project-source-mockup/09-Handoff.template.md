---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<HANDOFF_DOCUMENT_ID>"
document_type: "HANDOFF"
semantic_slot: "09"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "CHANGEABLE"
project_source_framework_version: "1.2.1"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 09 — Handoff

```text
Handoff From / To
Previous Handoff
Trigger
Current Phase / State
Completed Work
Pending Work
Formal Drafts / WIP
Active ACT / ISS / DRIFT / CONFLICT
Active RISK / ASM / DEP / MS / OUT / CR / GATE when applicable
Technical / Deployment warnings
Source/Docker known variance
Knowledge Debt affecting continuation
Material Persistence State: PERSISTED | PERSISTENCE_PENDING | NOT_APPLICABLE
External Working Source / Pointers
Unpersisted Material State when applicable
Required Read Order
Authority References
authority_transfer: false
Freshness Warnings
Exact Next Action
Chat Continuity: CONTINUE_CURRENT_CHAT | START_NEW_CHAT
Chat Continuity Reason
Required Read Before Continue
```

Use this as a compact continuation contract. Do not turn Handoff into an MCP transcript, raw tool log, search dump, full diff archive, or private intermediate-reasoning store.

Lifecycle: `DRAFT → OFFERED → ACKNOWLEDGED → ACCEPTED → SUPERSEDED`.
