---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 23
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-08-31T21:45:00+07:00"
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
→ 01-Project-Source-Index-r016-260831-2022.md
→ 03-Current-State-r023-260831-2145.md
→ task-specific routing
→ 09-Handoff-r023-260831-2145.md when continuation applies
```

## Active Document Registry

| Slot | Active File | State |
|---|---|---|
| `00` | `00-Project-Source-Framework-r002-260829-1901.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r016-260831-2022.md` | ACTIVE |
| `02` | `02-Project-Overview-r002-260829-1901.md` | ACTIVE |
| `03` | `03-Current-State-r023-260831-2145.md` | ACTIVE |
| `04` | `04-Decision-Log-r001-260829-1707.md` | ACTIVE |
| `05` | `05-Requirements-r001-260829-1707.md` | ACTIVE |
| `09` | `09-Handoff-r023-260831-2145.md` | ACTIVE |
| `10` | `10-Change-Log-r017-260831-2145.md` | ACTIVE |
| `11` | `11-Actor-Registry-r001-260829-1707.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r003-260831-2145.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r017-260831-2145.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r023-260831-2145.md` | ACTIVE |
| `15` | `15-Action-Registry-r021-260831-2145.md` | ACTIVE |
| `16` | `16-Migration-Registry-r003-260829-1916.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r001-260829-1707.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r007-260831-2145.md` | ACTIVE |

Conditional `06–08`, `40`, `60`, and `92` remain unmaterialized unless applicability is established. `91` is ACTIVE because OUT-001 is material under the user-invoked TASK-041 Goal. `18–19` remain RESERVED.

## Task Routing

- Framework development backlog/lifecycle source: `docs/superpowers/PROJECT-TASKS.md`.
- Framework distribution current root: `Framework-Source/` (released Framework 1.8.0 on canonical main; TASK-041 targets 1.9.0).
- ProjectFramework local Project Source pin: Framework 1.7.0 / Schema 1.0.0.
- `TASK-038`: DONE; release evidence `docs/superpowers/evidence/2026-08-29-task-038-framework-source-rename-release-full.md`.
- `TASK-039`: DONE; release evidence `docs/superpowers/evidence/2026-08-29-task-039-persistent-goal-command-release-full.md`.
- `TASK-024 [Meeting]`: DONE; release evidence `docs/superpowers/evidence/2026-08-29-task-024-meeting-llm-council-release-full.md`.
- `TASK-026 External AI Context & Disclosure Governance`: DONE; integrated through PR #21/#22/#23 reconciliation; prior evidence remains registered.
- `TASK-040 [Session] command rename`: DONE and published; Pull Request `#24` merged exact head `8622ef5ebfb38596ceedddd7dd668f8d9ba48bae` to `main` at `5a51b105ff4430c04605dcb254d41a8e80faad8b` on `2026-08-31T16:23:57+07:00`; resulting tree `67b62402e0659310e160a7396b4c88cb72aa73fa`; Framework-Source tree `36804c105604fe8da492a9d71a1f0270e5e035ee`.
- `TASK-041 Portable Installation Bootstrap & Project Settings Handoff`: DONE locally; candidate `f5cee5fb2f3cb4da7967f56dcb294ce2a1703530`; AFFECTED `273/273 PASS`; RELEASE_FULL `248/248 PASS`; release evidence `docs/superpowers/evidence/2026-08-31-task-041-portable-installation-bootstrap-release-full.md` committed at `06fe0c0a06d1c6c6a1abcf3c5cb9052471c5d8ef`; OUT-001 ACHIEVED / AUTH-001 TERMINATED / ENV-001 EXPIRED; publication `NOT_PUSHED`.
- Current selected next action: ไม่มีขั้นตอนถัดไป; TASK-025 remains the next roadmap candidate but is not started without separate user selection.
- `TASK-025 Project Knowledge Layer / Compounding Knowledge Contract`: remains TODO and is not implemented by this checkpoint.
- Current state: `03-Current-State-r023-260831-2145.md`.
- Continuation: `09-Handoff-r023-260831-2145.md`.
- Evidence: `13-Evidence-Registry-r017-260831-2145.md`.
- Manifest: `14-Project-Source-Manifest-r023-260831-2145.md`.

The derived registry is not manually authoritative over active document state.
