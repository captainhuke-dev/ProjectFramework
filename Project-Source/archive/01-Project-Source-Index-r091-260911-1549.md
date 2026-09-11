---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 91
document_status: "ACTIVE"
supersedes: "01-Project-Source-Index-r090-260911-1459.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-11T15:49:24+07:00"
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
| `01` | `01-Project-Source-Index-r091-260911-1549.md` | ACTIVE |
| `02` | `02-Project-Overview-r003-260911-1459.md` | ACTIVE |
| `03` | `03-Current-State-r087-260911-1549.md` | ACTIVE |
| `04` | `04-Decision-Log-r002-260911-1459.md` | ACTIVE |
| `05` | `05-Requirements-r002-260911-1459.md` | ACTIVE |
| `09` | `09-Handoff-r087-260911-1549.md` | ACTIVE |
| `10` | `10-Change-Log-r085-260911-1549.md` | ACTIVE |
| `11` | `11-Actor-Registry-r002-260911-1459.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r032-260911-1549.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r084-260911-1549.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r091-260911-1549.md` | ACTIVE |
| `15` | `15-Action-Registry-r085-260911-1549.md` | ACTIVE |
| `16` | `16-Migration-Registry-r005-260911-1549.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r002-260911-1459.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r049-260911-1549.md` | ACTIVE |

All active Project Source documents are Framework `1.15.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` remain reserved.

## Current Framework / Lifecycle

- Project Source pin: Framework `1.15.0` / Schema `1.0.0`.
- Framework distribution: `Framework-Source/` 1.15.0; tree `835c5a24c909ef7de2d413c46a6451746ed5fbf0`.
- Upgrade: `MIG-002 COMPLETED / ASSESSED_PATH / Direct-to-Latest`.
- Canonical upgrade commit observed: `015f76df0ee667f45e4712bcefa0d5bc4d9bbd05` / tree `aedaf7b2b6b8fc5feda7cdd5551c441733cb8615`.
- Verification/evidence: `EVD-086`, `EVD-087`, `EVD-088`; `UPGRADE_AFFECTED PASS`; `UPGRADE_RELEASE_FULL PASS_RUN_1`.
- Lifecycle: `OUT-014 ACHIEVED / AUTH-014 TERMINATED / ACT-026 DONE / ENV-014 EXPIRED`.
- Applied history: `CHG-087 / CHG-088`.
- Persistence: `PERSISTED / NOT_PENDING`.
- Framework backlog source remains `docs/superpowers/PROJECT-TASKS.md`.

## Current Routing

- Current state: active `03`.
- Continuation: active `09`.
- Evidence: active `13`.
- Manifest: active `14`.
- Migration: active `16`.
- Outcome/control: active `91`.

## Exact Next Action

ไม่มีขั้นตอนถัดไป for OUT-014. Git-native/MCP execution-architecture work remains a separate future scope.
