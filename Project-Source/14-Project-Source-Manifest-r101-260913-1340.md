---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 101
document_status: "ACTIVE"
supersedes: "14-Project-Source-Manifest-r101-260913-1340.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-13T13:40:50+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.16.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
# 14 — Project Source Manifest

## Current Reconstructable Snapshot

External bootstrap artifact: `PROJECT-BOOTSTRAP.md` → active `00 / FRAMEWORK-001`.

Active Project Source documents:

- `00` — `Project-Source/00-Project-Source-Framework-r004-260912-2344.md`
- `01` — `Project-Source/01-Project-Source-Index-r101-260913-1340.md`
- `02` — `Project-Source/02-Project-Overview-r004-260912-2344.md`
- `03` — `Project-Source/03-Current-State-r097-260913-1340.md`
- `04` — `Project-Source/04-Decision-Log-r003-260912-2344.md`
- `05` — `Project-Source/05-Requirements-r003-260912-2344.md`
- `09` — `Project-Source/09-Handoff-r097-260913-1340.md`
- `10` — `Project-Source/10-Change-Log-r095-260913-1340.md`
- `11` — `Project-Source/11-Actor-Registry-r003-260912-2344.md`
- `12` — `Project-Source/12-Authorization-Registry-r041-260913-1340.md`
- `13` — `Project-Source/13-Evidence-Registry-r094-260913-1340.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r100-260913-1112.md`
- `15` — `Project-Source/15-Action-Registry-r094-260913-1340.md`
- `16` — `Project-Source/16-Migration-Registry-r007-260912-2354.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r003-260912-2344.md`
- `91` — `Project-Source/91-Project-Management-Control-r058-260913-1340.md`

All active documents carry Framework `1.16.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` reserved.

## Framework / Lifecycle Provenance

```text
ProjectFramework Canonical Self-Host Pin: Framework 1.16.0 / Schema 1.0.0
Framework Distribution Baseline: Framework 1.16.0 / Schema 1.0.0 / release format 3
Framework-Source Baseline Tree: a84e7bd0ed56bd73a7e2cb6c642885d9fefeb24a
TASK-049 / OUT-017: DONE / CANONICAL_MAIN_INTEGRATED / ACHIEVED / PR #31 merge 4039be4
TASK-050: DONE / VERIFIED_COMPLETE / ISSUE_TRACKER_RECONCILED
TASK-051: IN_PROGRESS / DESIGN_DIRECTION_APPROVED / IMPLEMENTATION_AUTHORIZED_BY_GOAL / GitHub Issue #29
Goal Lifecycle: OUT-019 IN_PROGRESS / AUTH-019 ACTIVE / ACT-031 IN_PROGRESS / ENV-019 ACTIVE
Current Goal Evidence / Change: EVD-098 / CHG-098
Current Backlog: TODO=0 / IN_PROGRESS=1 / BLOCKED=0 (TASK-051 only)
Target Framework Release: 1.17.0 / Schema 1.0.0 / release format 3
Exact Next Action: write and self-review TASK-051 design spec, then implementation plan
```

## History Preservation

All predecessors remain preserved under `Project-Source/archive/` and Git history. This terminal local-control checkpoint supersedes the previous verification-pending control revisions only; verified Root `00 r004`, Bootstrap, and implementation semantics remain unchanged.

## Publication Boundary

TASK-049 self-host reconciliation remains canonical on `origin/main` through PR #31 merge `4039be4`. TASK-050 issue reconciliation remains preserved. TASK-051 executes locally under `AUTH-019`; push/PR/merge/tag/GitHub Release remain separately governed and are not authorized by OUT-019.

Manifest does not recursively hash its own raw bytes.
