---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 107
document_status: "ACTIVE"
supersedes: "01-Project-Source-Index-r106-260913-1905.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-13T19:32:51.798+07:00"
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
| `01` | `01-Project-Source-Index-r107-260913-1932.md` | ACTIVE |
| `02` | `02-Project-Overview-r004-260912-2344.md` | ACTIVE |
| `03` | `03-Current-State-r103-260913-1932.md` | ACTIVE |
| `04` | `04-Decision-Log-r003-260912-2344.md` | ACTIVE |
| `05` | `05-Requirements-r003-260912-2344.md` | ACTIVE |
| `09` | `09-Handoff-r103-260913-1932.md` | ACTIVE |
| `10` | `10-Change-Log-r101-260913-1932.md` | ACTIVE |
| `11` | `11-Actor-Registry-r003-260912-2344.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r044-260913-1905.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r100-260913-1932.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r107-260913-1932.md` | ACTIVE |
| `15` | `15-Action-Registry-r099-260913-1905.md` | ACTIVE |
| `16` | `16-Migration-Registry-r007-260912-2354.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r003-260912-2344.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r063-260913-1905.md` | ACTIVE |

All active Project Source documents now carry Framework `1.16.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` remain reserved.

## Current Framework / Lifecycle

- Project Source canonical self-host pin: Framework `1.16.0` / Schema `1.0.0`.
- Framework distribution candidate: Framework `1.18.0` / Schema `1.0.0` / release format `3`; frozen HEAD `48212bb4f4b577af482afcf5758424eee2f7e036`; Framework-Source tree `929065ccac7e3ecf25fda09de5326bb40c4f8f9c`.
- TASK-049 / OUT-017: `DONE / CANONICAL_MAIN_INTEGRATED / OUT-017 ACHIEVED`; PR #31 merge `4039be4` remains canonical baseline.
- TASK-050: `DONE / VERIFIED_COMPLETE / ISSUE_TRACKER_RECONCILED`.
- TASK-051: `DONE / VERIFIED_COMPLETE / PUSHED / PR_32_OPEN / NOT_MERGED / NOT_RELEASED`.
- TASK-052: `DONE / VERIFIED_COMPLETE / PUSHED / PR_32_OPEN / NOT_MERGED / NOT_RELEASED`.
- Goal lifecycle: `OUT-020 ACHIEVED / AUTH-020 TERMINATED / ACT-032 DONE / ENV-020 EXPIRED`.
- Current evidence/change: `EVD-105 / CHG-105`.
- Current backlog: `TODO=0 / IN_PROGRESS=0 / BLOCKED=0`.
- Parent verified Framework release candidate: `1.17.0 / Schema 1.0.0 / release format 3`.
- TASK-052 target Framework release: `1.18.0 / Schema 1.0.0 / release format 3`.
- TASK-052 design spec: `docs/superpowers/specs/2026-09-13-project-upgrade-one-session-fast-path-design.md`; user-approved; self-review `15/15 PASS`.
- TASK-052 implementation plan: `docs/superpowers/plans/2026-09-13-project-upgrade-one-session-fast-path.md`; commit `07f8026`; self-review `16/16 PASS`; executed inline.
- Exact next action: none under current authority; PR #32 is OPEN and merge/tag/release/self-host reconciliation remain separately governed.

## Current Routing

- Current state: active `03`.
- Continuation: active `09`.
- Evidence: active `13`.
- Manifest: active `14`.
- Migration: active `16`.
- Outcome/control: active `91`.

## Exact Next Action

PR #32 is OPEN. No merge/tag/release/self-host action is authorized by this publication checkpoint.
