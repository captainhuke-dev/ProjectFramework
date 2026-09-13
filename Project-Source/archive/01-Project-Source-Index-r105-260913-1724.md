---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 105
document_status: "ACTIVE"
supersedes: "01-Project-Source-Index-r104-260913-1457.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-13T17:24:10.030+07:00"
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
| `01` | `01-Project-Source-Index-r105-260913-1724.md` | ACTIVE |
| `02` | `02-Project-Overview-r004-260912-2344.md` | ACTIVE |
| `03` | `03-Current-State-r101-260913-1724.md` | ACTIVE |
| `04` | `04-Decision-Log-r003-260912-2344.md` | ACTIVE |
| `05` | `05-Requirements-r003-260912-2344.md` | ACTIVE |
| `09` | `09-Handoff-r101-260913-1724.md` | ACTIVE |
| `10` | `10-Change-Log-r099-260913-1724.md` | ACTIVE |
| `11` | `11-Actor-Registry-r003-260912-2344.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r043-260913-1724.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r098-260913-1724.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r105-260913-1724.md` | ACTIVE |
| `15` | `15-Action-Registry-r098-260913-1724.md` | ACTIVE |
| `16` | `16-Migration-Registry-r007-260912-2354.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r003-260912-2344.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r062-260913-1724.md` | ACTIVE |

All active Project Source documents now carry Framework `1.16.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` remain reserved.

## Current Framework / Lifecycle

- Project Source canonical self-host pin: Framework `1.16.0` / Schema `1.0.0`.
- Framework distribution candidate: Framework `1.17.0` / Schema `1.0.0` / release format `3`; Framework-Source tree `5a6a711861bbbc1e6f9315361921e28625cce854`.
- TASK-049 / OUT-017: `DONE / CANONICAL_MAIN_INTEGRATED / OUT-017 ACHIEVED`; PR #31 merge `4039be4` remains canonical baseline.
- TASK-050: `DONE / VERIFIED_COMPLETE / ISSUE_TRACKER_RECONCILED`.
- TASK-051: `DONE / VERIFIED_COMPLETE / LOCAL_ONLY / RELEASE_CANDIDATE_VERIFIED / NOT_PUBLISHED`.
- TASK-052: `IN_PROGRESS / DESIGN_COMPLETE / WRITTEN_SPEC_SELF_REVIEWED / USER_REVIEW_REQUIRED`.
- Goal lifecycle: `OUT-020 ACTIVE / AUTH-020 ACTIVE / ACT-032 IN_PROGRESS / ENV-020 ACTIVE`.
- Current evidence/change: `EVD-103 / CHG-103`.
- Current backlog: `TODO=0 / IN_PROGRESS=1 / BLOCKED=0` - TASK-052 only.
- Parent verified Framework release candidate: `1.17.0 / Schema 1.0.0 / release format 3`.
- TASK-052 target Framework release: `1.18.0 / Schema 1.0.0 / release format 3`.
- TASK-052 design spec: `docs/superpowers/specs/2026-09-13-project-upgrade-one-session-fast-path-design.md`; self-review `15/15 PASS`; USER_REVIEW_REQUIRED.
- TASK-051 implementation plan remains historical parent evidence; TASK-052 implementation plan not yet written.
- Exact next action: ACTOR-001 reviews the TASK-052 written spec; implementation planning starts only after approval.

## Current Routing

- Current state: active `03`.
- Continuation: active `09`.
- Evidence: active `13`.
- Manifest: active `14`.
- Migration: active `16`.
- Outcome/control: active `91`.

## Exact Next Action

ACTOR-001 reviews `docs/superpowers/specs/2026-09-13-project-upgrade-one-session-fast-path-design.md`; after approval, invoke writing-plans.
