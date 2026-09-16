---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 111
document_status: "ACTIVE"
supersedes: "01-Project-Source-Index-r111-260916-1415.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-16T14:15:47.931+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.19.0"
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
| `10` | `10-Change-Log-r105-260916-1415.md` | ACTIVE |
| `11` | `11-Actor-Registry-r006-260916-1415.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r048-260916-1415.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r104-260916-1415.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r111-260916-1415.md` | ACTIVE |
| `15` | `15-Action-Registry-r103-260916-1415.md` | ACTIVE |
| `16` | `16-Migration-Registry-r011-260916-1415.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r006-260916-1415.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r067-260916-1415.md` | ACTIVE |
| `00` | `00-Project-Source-Framework-r007-260916-1415.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r111-260916-1415.md` | ACTIVE |
| `02` | `02-Project-Overview-r007-260916-1415.md` | ACTIVE |
| `03` | `03-Current-State-r107-260916-1415.md` | ACTIVE |
| `04` | `04-Decision-Log-r006-260916-1415.md` | ACTIVE |
| `05` | `05-Requirements-r006-260916-1415.md` | ACTIVE |
| `09` | `09-Handoff-r107-260916-1415.md` | ACTIVE |

All active Project Source documents now carry Framework `1.19.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` remain reserved.

## Current Framework / Lifecycle

- Canonical self-host reconciliation: `MIG-005 / COMPLETED / PERSISTED / NOT_PENDING` (Framework 1.18.0 to 1.19.0; canonical commit `5b08c5c1438aa9898daa13fae4dc00e0bcfc0df5`).

- Project Source canonical self-host pin: Framework `1.19.0` / Schema `1.0.0`.
- Canonical Framework distribution: Framework `1.19.0` / Schema `1.0.0` / release format `3`; TASK-057 release candidate `f378e0a0b4796a94ec52ba1286d17d05e6a5c9b2`; Framework-Source tree `23274ada739c56a10c8edcfc14e6a9a0e46e9a0b`.
- TASK-051: `DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_32 / ISSUE_29_CLOSED`; Issue #29 closed through PR #33 `Closes #29`.
- TASK-052: `DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_32`.
- TASK-055: `DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_33 / ISSUE_CLOSED`.
- Goal lifecycle: `OUT-021 ACHIEVED / AUTH-021 TERMINATED / ACT-033 DONE / ENV-021 EXPIRED`.
- Current evidence/change: `EVD-107 / CHG-107`.
- Current backlog: `TODO=1 / IN_PROGRESS=0 / BLOCKED=0` (TASK-058 TODO; Phase 0 self-host 1.19 reconciliation in progress).
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
