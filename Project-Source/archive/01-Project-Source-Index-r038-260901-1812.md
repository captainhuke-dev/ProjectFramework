---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 38
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-01T18:12:00+07:00"
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
→ 01-Project-Source-Index-r038-260901-1812.md
→ 03-Current-State-r037-260901-1812.md
→ task-specific routing
→ 09-Handoff-r037-260901-1812.md when continuation applies
```

## Active Document Registry

| Slot | Active File | State |
|---|---|---|
| `00` | `00-Project-Source-Framework-r002-260829-1901.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r038-260901-1812.md` | ACTIVE |
| `02` | `02-Project-Overview-r002-260829-1901.md` | ACTIVE |
| `03` | `03-Current-State-r037-260901-1812.md` | ACTIVE |
| `04` | `04-Decision-Log-r001-260829-1707.md` | ACTIVE |
| `05` | `05-Requirements-r001-260829-1707.md` | ACTIVE |
| `09` | `09-Handoff-r037-260901-1812.md` | ACTIVE |
| `10` | `10-Change-Log-r032-260901-1812.md` | ACTIVE |
| `11` | `11-Actor-Registry-r001-260829-1707.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r009-260901-1721.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r032-260901-1812.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r038-260901-1812.md` | ACTIVE |
| `15` | `15-Action-Registry-r035-260901-1812.md` | ACTIVE |
| `16` | `16-Migration-Registry-r003-260829-1916.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r001-260829-1707.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r020-260901-1812.md` | ACTIVE |

Conditional `06–08`, `40`, `60`, and `92` remain unmaterialized unless applicability is established. `91` remains ACTIVE for terminal prior Goal history. `18–19` remain RESERVED.

## Task Routing

- Framework development backlog/lifecycle source: `docs/superpowers/PROJECT-TASKS.md`.
- Framework distribution current root: `Framework-Source/` (TASK-025 local verified candidate Framework 1.10.0; canonical `origin/main` remains separately published state).
- ProjectFramework local Project Source pin: Framework 1.7.0 / Schema 1.0.0.
- `TASK-041 Portable Installation Bootstrap & Project Settings Handoff`: DONE / publication reconciliation persisted on canonical main before this branch base.
- `TASK-025 Project Knowledge Layer / Compounding Knowledge Contract`: DONE locally / Framework 1.10.0 candidate `99c2f5a90e0c8f02dd68001d0e22b5362cd45a03` / AFFECTED `175/175 PASS` / RELEASE_FULL `120/120 PASS` / release evidence `e428eaa52de64546138fc4ca46fe84f1aa697e7f` / publication `NOT_PUSHED`.
- TASK-025 terminal Goal history: `OUT-003 ACHIEVED / AUTH-003 TERMINATED / ACT-013 DONE / ENV-003 EXPIRED`; Project Knowledge remains advisory/derived and does not become Project authority.
- Current state: `03-Current-State-r037-260901-1812.md`.
- Continuation: `09-Handoff-r037-260901-1812.md`.
- Evidence: `13-Evidence-Registry-r032-260901-1812.md`.
- Manifest: `14-Project-Source-Manifest-r038-260901-1812.md`.

The derived registry is not manually authoritative over active document state.
