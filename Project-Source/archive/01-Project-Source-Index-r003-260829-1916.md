---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 3
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-08-29T19:16:56+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.7.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 01 — Project Source Index

Framework `1.7.0+` root `PROJECT-BOOTSTRAP.md` reaches this document only after validating active `00 / FRAMEWORK-001`. This document routes Project work; it is not a second governance root.

## Bootstrap Read Order

```text
PROJECT-BOOTSTRAP.md
→ 00-Project-Source-Framework-r002-260829-1901.md
→ 01-Project-Source-Index-r003-260829-1916.md
→ 03-Current-State-r003-260829-1916.md
→ task-specific routing
→ 09-Handoff-r003-260829-1916.md when continuation applies
```

## Active Document Registry

| Slot | Active File | State |
|---|---|---|
| `00` | `00-Project-Source-Framework-r002-260829-1901.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r003-260829-1916.md` | ACTIVE |
| `02` | `02-Project-Overview-r002-260829-1901.md` | ACTIVE |
| `03` | `03-Current-State-r003-260829-1916.md` | ACTIVE |
| `04` | `04-Decision-Log-r001-260829-1707.md` | ACTIVE |
| `05` | `05-Requirements-r001-260829-1707.md` | ACTIVE |
| `09` | `09-Handoff-r003-260829-1916.md` | ACTIVE |
| `10` | `10-Change-Log-r003-260829-1916.md` | ACTIVE |
| `11` | `11-Actor-Registry-r001-260829-1707.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r001-260829-1707.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r003-260829-1916.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r003-260829-1916.md` | ACTIVE |
| `15` | `15-Action-Registry-r003-260829-1916.md` | ACTIVE |
| `16` | `16-Migration-Registry-r003-260829-1916.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r001-260829-1707.md` | ACTIVE |

Conditional `06–08`, `40`, `60`, `91`, and `92` remain unmaterialized unless applicability is established. `18–19` remain RESERVED.

## Task Routing

- Framework development backlog/lifecycle source: `docs/superpowers/PROJECT-TASKS.md`.
- Framework distribution current root: `Framework-Source/` (upstream Framework 1.8.0).
- ProjectFramework local Project Source pin: Framework 1.7.0 / Schema 1.0.0.
- `TASK-038`: DONE after AFFECTED `74/74` + RELEASE_FULL `198/198`; release evidence `docs/superpowers/evidence/2026-08-29-task-038-framework-source-rename-release-full.md`.
- `TASK-039`: approved design/implementation plan and now unblocked; exact next implementation plan is `docs/superpowers/plans/2026-08-29-task039-persistent-goal-command.md`.
- Current state: `03-Current-State-r003-260829-1916.md`.
- Continuation: `09-Handoff-r003-260829-1916.md`.
- Evidence: `13-Evidence-Registry-r003-260829-1916.md`.
- Manifest: `14-Project-Source-Manifest-r003-260829-1916.md`.

The derived registry is not manually authoritative over active document state.
