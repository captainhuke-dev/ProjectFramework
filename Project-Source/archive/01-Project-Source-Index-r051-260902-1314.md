---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 51
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-02T13:14:00+07:00"
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
→ 01-Project-Source-Index-r051-260902-1314.md
→ 03-Current-State-r050-260902-1314.md
→ task-specific routing
→ 09-Handoff-r050-260902-1314.md when continuation applies
```

## Active Document Registry

| Slot | Active File | State |
|---|---|---|
| `00` | `00-Project-Source-Framework-r002-260829-1901.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r051-260902-1314.md` | ACTIVE |
| `02` | `02-Project-Overview-r002-260829-1901.md` | ACTIVE |
| `03` | `03-Current-State-r050-260902-1314.md` | ACTIVE |
| `04` | `04-Decision-Log-r001-260829-1707.md` | ACTIVE |
| `05` | `05-Requirements-r001-260829-1707.md` | ACTIVE |
| `09` | `09-Handoff-r050-260902-1314.md` | ACTIVE |
| `10` | `10-Change-Log-r045-260902-1314.md` | ACTIVE |
| `11` | `11-Actor-Registry-r001-260829-1707.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r012-260902-1314.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r045-260902-1314.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r051-260902-1314.md` | ACTIVE |
| `15` | `15-Action-Registry-r048-260902-1314.md` | ACTIVE |
| `16` | `16-Migration-Registry-r003-260829-1916.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r001-260829-1707.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r028-260902-1314.md` | ACTIVE |

Conditional `06–08`, `40`, `60`, and `92` remain unmaterialized unless applicable. `91` remains ACTIVE for terminal Goal outcome history, including `OUT-005`. `18–19` remain RESERVED.

## Task Routing

- Framework development backlog/lifecycle source: `docs/superpowers/PROJECT-TASKS.md`.
- Framework distribution current root: `Framework-Source/` (Framework 1.12.2 / Schema 1.0.0 verified local TASK-043 candidate; publication NOT_PUSHED).
- ProjectFramework local Project Source pin: Framework 1.7.0 / Schema 1.0.0.
- `TASK-043 Registered Command Strict-Interface & Contract Completeness Hardening`: DONE / Framework 1.12.2; candidate `a4a2712ba41c35275401b31ac49b75d45eec8643`; structural `18/18 PASS`; AFFECTED `37/37 PASS`; RELEASE_FULL `25/25 PASS`; release evidence commit `2b7a23e8c5b06a1b9f37f8f2097b06223f5fbd18`; `OUT-005 ACHIEVED / AUTH-005 TERMINATED / ACT-016 DONE / ENV-005 EXPIRED`; publication `NOT_PUSHED`.
- TASK-043 release evidence: `docs/superpowers/evidence/2026-09-02-task-043-registered-command-strict-interface-release-full.md`.
- TASK-043 design: `docs/superpowers/specs/2026-09-02-task043-registered-command-strict-interface-design.md`.
- TASK-042 prerequisite: DONE / Framework 1.12.1 integrated; scenarios 339–350; Response Close Completeness Gate remains final global pre-emit gate.
- Current state: `03-Current-State-r050-260902-1314.md`.
- Continuation: `09-Handoff-r050-260902-1314.md`.
- Evidence: `13-Evidence-Registry-r045-260902-1314.md`.
- Manifest: `14-Project-Source-Manifest-r051-260902-1314.md`.

The derived registry is not manually authoritative over active document state.
