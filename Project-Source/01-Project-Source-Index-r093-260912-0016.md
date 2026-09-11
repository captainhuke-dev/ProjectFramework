---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 93
document_status: "ACTIVE"
supersedes: "01-Project-Source-Index-r092-260911-2308.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-12T00:16:41+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.15.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
# 01 — Project Source Index

## Bootstrap Read Order

`PROJECT-BOOTSTRAP.md → active 00 / FRAMEWORK-001 → active 01 → active 03 → task-specific routing → active 09 when continuation applies`.

## Active Document Registry

| Slot | Active File | State |
|---|---|---|
| `00` | `00-Project-Source-Framework-r003-260911-1459.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r093-260912-0016.md` | ACTIVE |
| `02` | `02-Project-Overview-r003-260911-1459.md` | ACTIVE |
| `03` | `03-Current-State-r089-260912-0016.md` | ACTIVE |
| `04` | `04-Decision-Log-r002-260911-1459.md` | ACTIVE |
| `05` | `05-Requirements-r002-260911-1459.md` | ACTIVE |
| `09` | `09-Handoff-r089-260912-0016.md` | ACTIVE |
| `10` | `10-Change-Log-r087-260912-0016.md` | ACTIVE |
| `11` | `11-Actor-Registry-r002-260911-1459.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r033-260912-0016.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r086-260912-0016.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r093-260912-0016.md` | ACTIVE |
| `15` | `15-Action-Registry-r086-260912-0016.md` | ACTIVE |
| `16` | `16-Migration-Registry-r005-260911-1549.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r002-260911-1459.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r050-260912-0016.md` | ACTIVE |

All active Project Source documents remain Framework `1.15.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` remain reserved.

## Current Framework / Lifecycle

- Project Source pin: Framework `1.15.0` / Schema `1.0.0`.
- Framework distribution: `Framework-Source/` 1.15.0; tree `835c5a24c909ef7de2d413c46a6451746ed5fbf0`.
- Prior Project upgrade: `MIG-002 COMPLETED / ASSESSED_PATH / Direct-to-Latest`.
- Current Task: `TASK-047 IN_PROGRESS` — Response Close UI Rendering Compliance Regression.
- Current Goal lifecycle: `OUT-015 ACTIVE / AUTH-015 ACTIVE / ACT-027 IN_PROGRESS / ENV-015 ACTIVE`.
- Current evidence: `EVD-090`; current change checkpoint: `CHG-090`.
- Root-cause result: existing Markdown-safe Framework contract and Scenario 432 are correct; no Framework semantic/version mutation is required.
- Live UI acceptance: USER_CONFIRMED by ACTOR-001 after Markdown-safe footer presentation.
- Persistence: checkpoint materialization in progress; remote publication not authorized.
- Current backlog: `TODO=0 / IN_PROGRESS=1 / BLOCKED=0`.
- Framework backlog source remains `docs/superpowers/PROJECT-TASKS.md`.

## Current Routing

- Current state: active `03`.
- Continuation: active `09`.
- Evidence: active `13`.
- Manifest: active `14`.
- Migration: active `16`.
- Outcome/control: active `91`.

## Exact Next Action

Run bounded GREEN verification, create a local completion commit, then terminalize TASK-047 / OUT-015 if all declared acceptance criteria pass.
