---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 99
document_status: "ACTIVE"
supersedes: "01-Project-Source-Index-r099-260913-0835.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-13T08:35:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.16.0"
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
| `00` | `00-Project-Source-Framework-r004-260912-2344.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r099-260913-0835.md` | ACTIVE |
| `02` | `02-Project-Overview-r004-260912-2344.md` | ACTIVE |
| `03` | `03-Current-State-r095-260913-0835.md` | ACTIVE |
| `04` | `04-Decision-Log-r003-260912-2344.md` | ACTIVE |
| `05` | `05-Requirements-r003-260912-2344.md` | ACTIVE |
| `09` | `09-Handoff-r095-260913-0835.md` | ACTIVE |
| `10` | `10-Change-Log-r093-260913-0835.md` | ACTIVE |
| `11` | `11-Actor-Registry-r003-260912-2344.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r039-260913-0835.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r092-260913-0835.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r099-260913-0835.md` | ACTIVE |
| `15` | `15-Action-Registry-r092-260913-0835.md` | ACTIVE |
| `16` | `16-Migration-Registry-r007-260912-2354.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r003-260912-2344.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r056-260913-0835.md` | ACTIVE |

All active Project Source documents now carry Framework `1.16.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` remain reserved.

## Current Framework / Lifecycle

- Project Source canonical self-host pin: Framework `1.16.0` / Schema `1.0.0`.
- Framework distribution: Framework `1.16.0` / Schema `1.0.0` / release format `3`; Framework-Source tree `a84e7bd0ed56bd73a7e2cb6c642885d9fefeb24a`.
- TASK-049 / OUT-017: `DONE / CANONICAL_MAIN_INTEGRATED / OUT-017 ACHIEVED`; PR #31 merge `4039be4` freshly observed on `origin/main`.
- TASK-050: `IN_PROGRESS` — audit/reconcile GitHub Issues #25/#29 against canonical Framework/task truth.
- TASK-051: `TODO / DESIGN_REQUIRED / IMPLEMENTATION_NOT_STARTED` — risk-tiered Feature Delivery Fast Path, sourced from GitHub Issue #29.
- Goal lifecycle: `OUT-018 ACTIVE / AUTH-018 ACTIVE / ACT-030 IN_PROGRESS / ENV-018 ACTIVE`.
- Audit checkpoint: `EVD-096 / CHG-096`.
- Current backlog: `TODO=1 / IN_PROGRESS=1 / BLOCKED=0`.
- Exact next action: persist TASK-050 checkpoint, reconcile GitHub Issue #25/#29 states, then terminalize TASK-050 without implementing TASK-051.

## Current Routing

- Current state: active `03`.
- Continuation: active `09`.
- Evidence: active `13`.
- Manifest: active `14`.
- Migration: active `16`.
- Outcome/control: active `91`.

## Exact Next Action

Reconcile GitHub Issue #25/#29 against TASK-050/TASK-051, then verify issue tracker and local Task ledger agree.
