---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 107
document_status: "ACTIVE"
supersedes: "14-Project-Source-Manifest-r106-260913-1905.md"
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
# 14 — Project Source Manifest

## Current Reconstructable Snapshot

External bootstrap artifact: `PROJECT-BOOTSTRAP.md` → active `00 / FRAMEWORK-001`.

Active Project Source documents:

- `00` — `Project-Source/00-Project-Source-Framework-r004-260912-2344.md`
- `01` — `Project-Source/01-Project-Source-Index-r107-260913-1932.md`
- `02` — `Project-Source/02-Project-Overview-r004-260912-2344.md`
- `03` — `Project-Source/03-Current-State-r103-260913-1932.md`
- `04` — `Project-Source/04-Decision-Log-r003-260912-2344.md`
- `05` — `Project-Source/05-Requirements-r003-260912-2344.md`
- `09` — `Project-Source/09-Handoff-r103-260913-1932.md`
- `10` — `Project-Source/10-Change-Log-r101-260913-1932.md`
- `11` — `Project-Source/11-Actor-Registry-r003-260912-2344.md`
- `12` — `Project-Source/12-Authorization-Registry-r044-260913-1905.md`
- `13` — `Project-Source/13-Evidence-Registry-r100-260913-1932.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r107-260913-1932.md`
- `15` — `Project-Source/15-Action-Registry-r099-260913-1905.md`
- `16` — `Project-Source/16-Migration-Registry-r007-260912-2354.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r003-260912-2344.md`
- `91` — `Project-Source/91-Project-Management-Control-r063-260913-1905.md`

All active documents carry Framework `1.16.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` reserved.

## Framework / Lifecycle Provenance

```text
ProjectFramework Canonical Self-Host Pin: Framework 1.16.0 / Schema 1.0.0
Framework Distribution Candidate: Framework 1.18.0 / Schema 1.0.0 / release format 3
Framework-Source Candidate Tree: 929065ccac7e3ecf25fda09de5326bb40c4f8f9c / HEAD 48212bb4f4b577af482afcf5758424eee2f7e036
TASK-049 / OUT-017: DONE / CANONICAL_MAIN_INTEGRATED / ACHIEVED / PR #31 merge 4039be4
TASK-050: DONE / VERIFIED_COMPLETE / ISSUE_TRACKER_RECONCILED
TASK-051: DONE / VERIFIED_COMPLETE / PUSHED / PR_32_OPEN / NOT_MERGED / NOT_RELEASED / GitHub Issue #29 OPEN
TASK-052: DONE / VERIFIED_COMPLETE / PUSHED / PR_32_OPEN / NOT_MERGED / NOT_RELEASED
Goal Lifecycle: OUT-020 ACHIEVED / AUTH-020 TERMINATED / ACT-032 DONE / ENV-020 EXPIRED
Current Evidence / Change: EVD-105 / CHG-105
Current Backlog: TODO=0 / IN_PROGRESS=0 / BLOCKED=0
Parent Verified Distribution Candidate: 1.17.0 / Schema 1.0.0 / release format 3
TASK-052 Target Framework Release: 1.18.0 / Schema 1.0.0 / release format 3
TASK-052 Design: docs/superpowers/specs/2026-09-13-project-upgrade-one-session-fast-path-design.md / USER_APPROVED / SELF_REVIEW 15/15 PASS
TASK-052 Plan: docs/superpowers/plans/2026-09-13-project-upgrade-one-session-fast-path.md / commit 07f8026 / SELF_REVIEW 16/16 PASS / EXECUTED
Exact Next Action: none under current authority; PR #32 OPEN; merge/tag/release/self-host reconciliation separately governed
```

## History Preservation

All predecessors remain preserved under `Project-Source/archive/` and Git history. This terminal local-control checkpoint supersedes the previous verification-pending control revisions only; verified Root `00 r004`, Bootstrap, and implementation semantics remain unchanged.

## Publication Boundary

TASK-049 self-host reconciliation remains canonical on `origin/main` through PR #31 merge `4039be4`. TASK-050 issue reconciliation remains preserved. TASK-051/TASK-052 verified lineage is pushed and represented by PR #32 under ACTOR-001 action-specific publication authority. PR merge, tag/GitHub Release, Issue #29 closure, and canonical self-host promotion remain separately governed and were not performed.

Manifest does not recursively hash its own raw bytes.
