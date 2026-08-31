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
project_source_framework_version: "1.9.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 09 — Handoff

Framework `1.7.0+` root bootstrap resolves this document only when continuation/resume applies. Resume Block truth remains here; never copy it into `PROJECT-BOOTSTRAP.md`.

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

Project Location Binding / Local Workspace / File Storage Binding Reference: active FRAMEWORK-001 (no independent repo/folder/path/storage authority copy)
Bootstrap Location Mismatch / Freshness Warning when material
Observed MCP execution path/workspace evidence when needed
File Storage routing reference by storage_key/content scope/provider/source-native pointer when continuation requires external storage
Observed Repository Identity when material
Current Work Branch / Worktree
Verified HEAD SHA
Working-tree State
Last Completed Task / ACT
Completion Commit(s) when applicable
Verification Result / Evidence Pointer
Remote Reachability / Push State when receiving environment needs it
External Working Source / Pointers
Unpersisted Material State when applicable
Required Read Order
Authority References
Active Goal: <OUT-* or none>
Goal Status: <ACTIVE | BLOCKED | ACHIEVED | CANCELLED | SUPERSEDED | none>
Goal Authorization: <AUTH-* or none>
Current Goal Action: <ACT-* or none>
Goal Envelope: <ENV-* or none>
Last Verified Goal Authorization At: <ISO8601_OR_UNKNOWN>
Next Safe Goal Action: <ACTION_OR_NONE>
Goal Blocker: <BLOCKER_OR_NONE>
authority_transfer: false
Freshness Warnings
Exact Next Action
Chat Continuity: CONTINUE_CURRENT_CHAT | START_NEW_CHAT
Chat Continuity Reason
Required Read Before Continue
```

Use this as a compact continuation contract. Do not turn Handoff into an MCP transcript, raw tool log, search dump, full diff archive, or private intermediate-reasoning store.

Continuation invariants:

```text
Exact Next Action = ไม่มีขั้นตอนถัดไป → Chat Continuity = START_NEW_CHAT
Chat Continuity = CONTINUE_CURRENT_CHAT → concrete Exact Next Action required
Material Persistence State = PERSISTENCE_PENDING → CONTINUE_CURRENT_CHAT + concrete persistence/recovery action
```

When continuation depends on GitHub/Drive/local/File Storage routing, reference the active `FRAMEWORK-001` Project Location Binding and source-native durable identities. `09` does not persist an independent Bootstrap Location Block, repository/workspace binding, or File Storage binding authority; current branch/worktree/HEAD remains observed dynamic evidence.
Lifecycle: `DRAFT → OFFERED → ACKNOWLEDGED → ACCEPTED → SUPERSEDED`.

**Resume Block (latest checkpoint):**

```text
Task: <TASK/ACT id> | Done: <last completed step> | Next: <exact next step> | Blockers: <none or list> | Envelope: <ENV-* or none>
```

Goal pointers are compact references only. Handoff never transfers Goal authority; a receiving Agent resolves current `OUT-* / AUTH-* / ACT-* / ENV-*` from their canonical homes before resuming.
