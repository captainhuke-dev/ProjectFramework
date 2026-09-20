---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 113
document_status: "ACTIVE"
supersedes: "01-Project-Source-Index-r112-260920-1016.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-20T13:16:07.724+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.21.0"
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
| `10` | `10-Change-Log-r107-260920-1316.md` | ACTIVE |
| `11` | `11-Actor-Registry-r008-260920-1316.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r050-260920-1316.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r106-260920-1316.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r113-260920-1316.md` | ACTIVE |
| `15` | `15-Action-Registry-r105-260920-1316.md` | ACTIVE |
| `16` | `16-Migration-Registry-r013-260920-1316.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r008-260920-1316.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r069-260920-1316.md` | ACTIVE |
| `00` | `00-Project-Source-Framework-r009-260920-1316.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r113-260920-1316.md` | ACTIVE |
| `02` | `02-Project-Overview-r009-260920-1316.md` | ACTIVE |
| `03` | `03-Current-State-r109-260920-1316.md` | ACTIVE |
| `04` | `04-Decision-Log-r008-260920-1316.md` | ACTIVE |
| `05` | `05-Requirements-r008-260920-1316.md` | ACTIVE |
| `09` | `09-Handoff-r109-260920-1316.md` | ACTIVE |

All active Project Source documents now carry Framework `1.21.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` remain reserved.

## Current Framework / Lifecycle

- Canonical self-host reconciliation: `MIG-007 / COMPLETED / PERSISTED / NOT_PENDING` (Framework 1.20.0 to 1.21.0; canonical commit `7602fb10d238afcbd818874e07edb7820061b561`); `MIG-006` (1.19.0 to 1.20.0; canonical commit `71c9d9c2a1db4882f024c5537093b7dd501e9312`) remains the immediately-preceding historical reconciliation.

- Project Source canonical self-host pin: Framework `1.21.0` / Schema `1.0.0`.
- Canonical Framework distribution: Framework `1.21.0` / Schema `1.0.0` / release format `3`; TASK-059 release candidate `0d51582b553953a176dcb3f40fe942e177588028`; Framework-Source tree `ea6aa84b179c0f470fd6231cf364e6d8a5a59e72`.
- TASK-051: `DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_32 / ISSUE_29_CLOSED`; Issue #29 closed through PR #33 `Closes #29`.
- TASK-052: `DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_32`.
- TASK-055: `DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_33 / ISSUE_CLOSED`.
- Goal lifecycle: `OUT-021 ACHIEVED / AUTH-021 TERMINATED / ACT-033 DONE / ENV-021 EXPIRED`.
- Current evidence/change: `EVD-107 / CHG-107`.
- Current backlog: `TODO=0 / IN_PROGRESS=0 / BLOCKED=0` (TASK-058 DONE locally; post-merge self-host 1.20 reconciliation in progress).
- Canonical reconciliation: PR #33 merge `5b067a1c2fcfeab867ba3879a76f675904566e27`; Issue #29 `CLOSED` at `2026-09-13T15:47:48Z`.
- Exact next action: none for TASK-055; tag/GitHub Release remain separately governed and are not required for OUT-021.

## Current Routing

- Current state: active `03`.
- Continuation: active `09`.
- Evidence: active `13`.
- Manifest: active `14`.
- Migration: active `16`.
- Outcome/control: active `91`.

## Exact Next Action

None for TASK-055. Tag/GitHub Release remain separately governed and are not required for OUT-021.
