---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 104
document_status: "ACTIVE"
supersedes: "14-Project-Source-Manifest-r103-260913-1412.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-13T14:57:05.342+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r104-260913-1457.md`
- `02` — `Project-Source/02-Project-Overview-r004-260912-2344.md`
- `03` — `Project-Source/03-Current-State-r100-260913-1457.md`
- `04` — `Project-Source/04-Decision-Log-r003-260912-2344.md`
- `05` — `Project-Source/05-Requirements-r003-260912-2344.md`
- `09` — `Project-Source/09-Handoff-r100-260913-1457.md`
- `10` — `Project-Source/10-Change-Log-r098-260913-1457.md`
- `11` — `Project-Source/11-Actor-Registry-r003-260912-2344.md`
- `12` — `Project-Source/12-Authorization-Registry-r042-260913-1457.md`
- `13` — `Project-Source/13-Evidence-Registry-r097-260913-1457.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r104-260913-1457.md`
- `15` — `Project-Source/15-Action-Registry-r097-260913-1457.md`
- `16` — `Project-Source/16-Migration-Registry-r007-260912-2354.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r003-260912-2344.md`
- `91` — `Project-Source/91-Project-Management-Control-r061-260913-1457.md`

All active documents carry Framework `1.16.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` reserved.

## Framework / Lifecycle Provenance

```text
ProjectFramework Canonical Self-Host Pin: Framework 1.16.0 / Schema 1.0.0
Framework Distribution Candidate: Framework 1.17.0 / Schema 1.0.0 / release format 3
Framework-Source Candidate Tree: 5a6a711861bbbc1e6f9315361921e28625cce854
TASK-049 / OUT-017: DONE / CANONICAL_MAIN_INTEGRATED / ACHIEVED / PR #31 merge 4039be4
TASK-050: DONE / VERIFIED_COMPLETE / ISSUE_TRACKER_RECONCILED
TASK-051: DONE / VERIFIED_COMPLETE / LOCAL_ONLY / RELEASE_CANDIDATE_VERIFIED / NOT_PUBLISHED / GitHub Issue #29 OPEN
Goal Lifecycle: OUT-019 ACHIEVED / AUTH-019 TERMINATED / ACT-031 DONE / ENV-019 EXPIRED
Current Evidence / Change: EVD-101 / EVD-102 / CHG-101 / CHG-102
Current Backlog: TODO=0 / IN_PROGRESS=0 / BLOCKED=0
Target Framework Release: 1.17.0 / Schema 1.0.0 / release format 3
Design: docs/superpowers/specs/2026-09-13-task051-risk-tiered-feature-delivery-fast-path-design.md / SELF_REVIEW 13/13 PASS
Plan: docs/superpowers/plans/2026-09-13-task051-risk-tiered-feature-delivery-fast-path.md / SELF_REVIEW 18/18 PASS
Exact Next Action: none for local TASK-051 completion
```

## History Preservation

All predecessors remain preserved under `Project-Source/archive/` and Git history. This terminal local-control checkpoint supersedes the previous verification-pending control revisions only; verified Root `00 r004`, Bootstrap, and implementation semantics remain unchanged.

## Publication Boundary

TASK-049 self-host reconciliation remains canonical on `origin/main` through PR #31 merge `4039be4`. TASK-050 issue reconciliation remains preserved. TASK-051 executes locally under `AUTH-019`; push/PR/merge/tag/GitHub Release remain separately governed and are not authorized by OUT-019.

Manifest does not recursively hash its own raw bytes.
