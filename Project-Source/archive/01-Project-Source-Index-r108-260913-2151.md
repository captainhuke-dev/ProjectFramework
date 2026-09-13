---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 108
document_status: "ACTIVE"
supersedes: "01-Project-Source-Index-r107-260913-1932.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-13T21:51:48.631+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.18.0"
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
| `10` | `10-Change-Log-r102-260913-2151.md` | ACTIVE |
| `11` | `11-Actor-Registry-r004-260913-2151.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r045-260913-2151.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r101-260913-2151.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r108-260913-2151.md` | ACTIVE |
| `15` | `15-Action-Registry-r100-260913-2151.md` | ACTIVE |
| `16` | `16-Migration-Registry-r008-260913-2151.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r004-260913-2151.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r064-260913-2151.md` | ACTIVE |
| `00` | `00-Project-Source-Framework-r005-260913-2151.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r108-260913-2151.md` | ACTIVE |
| `02` | `02-Project-Overview-r005-260913-2151.md` | ACTIVE |
| `03` | `03-Current-State-r104-260913-2151.md` | ACTIVE |
| `04` | `04-Decision-Log-r004-260913-2151.md` | ACTIVE |
| `05` | `05-Requirements-r004-260913-2151.md` | ACTIVE |
| `09` | `09-Handoff-r104-260913-2151.md` | ACTIVE |

All active Project Source documents now carry Framework `1.18.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` remain reserved.

## Current Framework / Lifecycle

- Project Source canonical self-host pin: Framework `1.18.0` / Schema `1.0.0`.
- Canonical Framework distribution: Framework `1.18.0` / Schema `1.0.0` / release format `3`; PR #32 merge `f6330e9929c28977d43fc149b864d590df1c2816`; Framework-Source tree `929065ccac7e3ecf25fda09de5326bb40c4f8f9c`.
- TASK-051: `DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_32`; GitHub Issue #29 closure is bound to the TASK-055 reconciliation PR via `Closes #29`.
- TASK-052: `DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_32`.
- TASK-055: `IN_PROGRESS / SELF_HOST_RECONCILIATION_CANDIDATE / CANONICAL_INTEGRATION_PENDING`.
- Goal lifecycle: `OUT-021 ACTIVE / AUTH-021 ACTIVE / ACT-033 IN_PROGRESS / ENV-021 ACTIVE`.
- Current evidence/change: `EVD-106 / CHG-106`.
- Current backlog: `TODO=0 / IN_PROGRESS=1 / BLOCKED=0` — TASK-055 only.
- Exact next action: verify the 1.18 self-host reconciliation candidate, then publish/merge the reconciliation line to canonical `main`.

## Current Routing

- Current state: active `03`.
- Continuation: active `09`.
- Evidence: active `13`.
- Manifest: active `14`.
- Migration: active `16`.
- Outcome/control: active `91`.

## Exact Next Action

Verify the TASK-055 candidate; if accepted, run INTEGRATION_GATE and merge the reconciliation line to canonical `main`.
