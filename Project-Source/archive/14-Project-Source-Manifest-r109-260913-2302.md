---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 109
document_status: "ACTIVE"
supersedes: "14-Project-Source-Manifest-r108-260913-2151.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-13T23:02:09.699+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.18.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
# 14 — Project Source Manifest

## Current Reconstructable Snapshot

External bootstrap artifact: `PROJECT-BOOTSTRAP.md` → active `00 / FRAMEWORK-001`.

Active Project Source documents:

- `10` — `Project-Source/10-Change-Log-r103-260913-2302.md`
- `11` — `Project-Source/11-Actor-Registry-r004-260913-2151.md`
- `12` — `Project-Source/12-Authorization-Registry-r046-260913-2302.md`
- `13` — `Project-Source/13-Evidence-Registry-r102-260913-2302.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r109-260913-2302.md`
- `15` — `Project-Source/15-Action-Registry-r101-260913-2302.md`
- `16` — `Project-Source/16-Migration-Registry-r009-260913-2302.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r004-260913-2151.md`
- `91` — `Project-Source/91-Project-Management-Control-r065-260913-2302.md`
- `00` — `Project-Source/00-Project-Source-Framework-r005-260913-2151.md`
- `01` — `Project-Source/01-Project-Source-Index-r109-260913-2302.md`
- `02` — `Project-Source/02-Project-Overview-r005-260913-2151.md`
- `03` — `Project-Source/03-Current-State-r105-260913-2302.md`
- `04` — `Project-Source/04-Decision-Log-r004-260913-2151.md`
- `05` — `Project-Source/05-Requirements-r004-260913-2151.md`
- `09` — `Project-Source/09-Handoff-r105-260913-2302.md`

All active documents carry Framework `1.18.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` reserved.

## Framework / Lifecycle Provenance

```text
ProjectFramework Canonical Self-Host Pin: Framework 1.18.0 / Schema 1.0.0
Canonical Framework Distribution: Framework 1.18.0 / Schema 1.0.0 / release format 3
PR #32 Release Merge: f6330e9929c28977d43fc149b864d590df1c2816
PR #33 Reconciliation Merge: 5b067a1c2fcfeab867ba3879a76f675904566e27
Framework-Source Tree: 929065ccac7e3ecf25fda09de5326bb40c4f8f9c
TASK-051: DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_32 / ISSUE_29_CLOSED
TASK-052: DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_32
TASK-055: DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_33 / ISSUE_CLOSED
Goal Lifecycle: OUT-021 ACHIEVED / AUTH-021 TERMINATED / ACT-033 DONE / ENV-021 EXPIRED
Current Evidence / Change: EVD-107 / CHG-107
Current Backlog: TODO=0 / IN_PROGRESS=0 / BLOCKED=0
Migration: MIG-004 / COMPLETED / PERSISTED / NOT_PENDING
Issue #29: CLOSED / closed_at 2026-09-13T15:47:48Z
Exact Next Action: none for TASK-055
```

## History Preservation

All predecessors are preserved under `Project-Source/archive/` and Git history. Project UUID, Stable document IDs, Project-specific truth, Project Location Binding values, and secret-reference boundary are preserved.

## Publication Boundary

PR #32 and PR #33 are merged. TASK-055 canonical self-host reconciliation is complete and Issue #29 is CLOSED. This terminal snapshot is externally claimable when this exact successor set is observed on canonical `origin/main`; tag/GitHub Release remain separately governed.

Manifest does not recursively hash its own raw bytes.
