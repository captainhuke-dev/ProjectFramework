---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 27
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-01T08:57:00+07:00"
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
→ 01-Project-Source-Index-r027-260901-0857.md
→ 03-Current-State-r027-260901-0857.md
→ task-specific routing
→ 09-Handoff-r027-260901-0857.md when continuation applies
```

## Active Document Registry

| Slot | Active File | State |
|---|---|---|
| `00` | `00-Project-Source-Framework-r002-260829-1901.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r027-260901-0857.md` | ACTIVE |
| `02` | `02-Project-Overview-r002-260829-1901.md` | ACTIVE |
| `03` | `03-Current-State-r027-260901-0857.md` | ACTIVE |
| `04` | `04-Decision-Log-r001-260829-1707.md` | ACTIVE |
| `05` | `05-Requirements-r001-260829-1707.md` | ACTIVE |
| `09` | `09-Handoff-r027-260901-0857.md` | ACTIVE |
| `10` | `10-Change-Log-r021-260901-0857.md` | ACTIVE |
| `11` | `11-Actor-Registry-r001-260829-1707.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r007-260901-0857.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r021-260901-0857.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r027-260901-0857.md` | ACTIVE |
| `15` | `15-Action-Registry-r025-260901-0857.md` | ACTIVE |
| `16` | `16-Migration-Registry-r003-260829-1916.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r001-260829-1707.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r011-260901-0857.md` | ACTIVE |

Conditional `06–08`, `40`, `60`, and `92` remain unmaterialized unless applicability is established. `91` remains ACTIVE because terminal `OUT-001` and `OUT-002` history are material. `18–19` remain RESERVED.

## Task Routing

- Framework development backlog/lifecycle source: `docs/superpowers/PROJECT-TASKS.md`.
- Framework distribution current root: `Framework-Source/` (released Framework 1.9.0 on canonical main; TASK-042 targets 1.9.1).
- ProjectFramework local Project Source pin: Framework 1.7.0 / Schema 1.0.0.
- `TASK-040 [Session] command rename`: DONE / published through PR #24.
- `TASK-041 Portable Installation Bootstrap & Project Settings Handoff`: DONE / publication `MERGED_TO_MAIN` through Pull Request `#26`; post-merge Project Source reconciliation `PERSISTED / NOT_PENDING`; reconciliation remote terminal `origin/main` observation `d650513fe01726238f6e59cde1ed7a70b28ae0e4` PASS `41/41`; Framework-Source tree `06ce4013473ec014e70d8d3233f6132aa90339fd` unchanged.
- Reconciliation Goal terminal history: `OUT-002 ACHIEVED / AUTH-002 TERMINATED / ACT-011 DONE / ENV-002 EXPIRED`; evidence `EVD-020` / `EVD-021` / `EVD-022`.
- `TASK-042 Response Finalization Hardening`: IN_PROGRESS under persistent `OUT-003 / AUTH-003 / ACT-012 / ENV-003`; root cause verified: current thin launchers bootstrap only before Material Project work while the existing Response Close Gate is already normative, leaving read-only/status/diagnostic/early-return paths able to answer before local governance is resolved; approved fix is first-response bootstrap + unskippable pre-emit gate + exceptional-path pressure coverage.
- Current selected next action: write/self-review/commit the TASK-042 design spec, then implementation plan; implementation remains NOT_STARTED until the plan is committed.
- `TASK-025 Project Knowledge Layer / Compounding Knowledge Contract`: remains TODO and is not started by TASK-042.
- Current state: `03-Current-State-r027-260901-0857.md`.
- Continuation: `09-Handoff-r027-260901-0857.md`.
- Evidence: `13-Evidence-Registry-r021-260901-0857.md`.
- Manifest: `14-Project-Source-Manifest-r027-260901-0857.md`.

The derived registry is not manually authoritative over active document state.
