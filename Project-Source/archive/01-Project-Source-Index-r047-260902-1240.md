---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 47
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-02T12:40:00+07:00"
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
→ 01-Project-Source-Index-r047-260902-1240.md
→ 03-Current-State-r046-260902-1240.md
→ task-specific routing
→ 09-Handoff-r046-260902-1240.md when continuation applies
```

## Active Document Registry

| Slot | Active File | State |
|---|---|---|
| `00` | `00-Project-Source-Framework-r002-260829-1901.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r047-260902-1240.md` | ACTIVE |
| `02` | `02-Project-Overview-r002-260829-1901.md` | ACTIVE |
| `03` | `03-Current-State-r046-260902-1240.md` | ACTIVE |
| `04` | `04-Decision-Log-r001-260829-1707.md` | ACTIVE |
| `05` | `05-Requirements-r001-260829-1707.md` | ACTIVE |
| `09` | `09-Handoff-r046-260902-1240.md` | ACTIVE |
| `10` | `10-Change-Log-r041-260902-1240.md` | ACTIVE |
| `11` | `11-Actor-Registry-r001-260829-1707.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r011-260902-1240.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r041-260902-1240.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r047-260902-1240.md` | ACTIVE |
| `15` | `15-Action-Registry-r044-260902-1240.md` | ACTIVE |
| `16` | `16-Migration-Registry-r003-260829-1916.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r001-260829-1707.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r027-260902-1240.md` | ACTIVE |

Conditional `06–08`, `40`, `60`, and `92` remain unmaterialized unless applicable. `91` remains ACTIVE for Goal outcome history and active `OUT-005`. `18–19` remain RESERVED.

## Task Routing

- Framework development backlog/lifecycle source: `docs/superpowers/PROJECT-TASKS.md`.
- Framework distribution current root: `Framework-Source/` (baseline Framework 1.12.1 / Schema 1.0.0 on canonical main; TASK-043 target 1.12.2 is not yet implemented).
- ProjectFramework local Project Source pin: Framework 1.7.0 / Schema 1.0.0.
- `TASK-043 Registered Command Strict-Interface & Contract Completeness Hardening`: IN_PROGRESS under `OUT-005 / AUTH-005 / ACT-016 / ENV-005`; task registration `5401fe4`; written design `f740d16`; target Framework 1.12.2; implementation plan next; publication not authorized.
- TASK-043 design: `docs/superpowers/specs/2026-09-02-task043-registered-command-strict-interface-design.md`.
- TASK-042 prerequisite: DONE / Framework 1.12.1 integrated; scenarios 339–350; Response Close Completeness Gate remains final global pre-emit gate.
- Current state: `03-Current-State-r046-260902-1240.md`.
- Continuation: `09-Handoff-r046-260902-1240.md`.
- Evidence: `13-Evidence-Registry-r041-260902-1240.md`.
- Manifest: `14-Project-Source-Manifest-r047-260902-1240.md`.

The derived registry is not manually authoritative over active document state.
