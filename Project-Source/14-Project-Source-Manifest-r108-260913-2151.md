---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 108
document_status: "ACTIVE"
supersedes: "14-Project-Source-Manifest-r107-260913-1932.md"
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
# 14 — Project Source Manifest

## Current Reconstructable Snapshot

External bootstrap artifact: `PROJECT-BOOTSTRAP.md` → active `00 / FRAMEWORK-001`.

Active Project Source documents:

- `10` — `Project-Source/10-Change-Log-r102-260913-2151.md`
- `11` — `Project-Source/11-Actor-Registry-r004-260913-2151.md`
- `12` — `Project-Source/12-Authorization-Registry-r045-260913-2151.md`
- `13` — `Project-Source/13-Evidence-Registry-r101-260913-2151.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r108-260913-2151.md`
- `15` — `Project-Source/15-Action-Registry-r100-260913-2151.md`
- `16` — `Project-Source/16-Migration-Registry-r008-260913-2151.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r004-260913-2151.md`
- `91` — `Project-Source/91-Project-Management-Control-r064-260913-2151.md`
- `00` — `Project-Source/00-Project-Source-Framework-r005-260913-2151.md`
- `01` — `Project-Source/01-Project-Source-Index-r108-260913-2151.md`
- `02` — `Project-Source/02-Project-Overview-r005-260913-2151.md`
- `03` — `Project-Source/03-Current-State-r104-260913-2151.md`
- `04` — `Project-Source/04-Decision-Log-r004-260913-2151.md`
- `05` — `Project-Source/05-Requirements-r004-260913-2151.md`
- `09` — `Project-Source/09-Handoff-r104-260913-2151.md`

All active documents carry Framework `1.18.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` reserved.

## Framework / Lifecycle Provenance

```text
ProjectFramework Canonical Self-Host Pin Candidate: Framework 1.18.0 / Schema 1.0.0
Canonical Framework Distribution: Framework 1.18.0 / Schema 1.0.0 / release format 3
PR #32 Merge: f6330e9929c28977d43fc149b864d590df1c2816
Framework-Source Tree: 929065ccac7e3ecf25fda09de5326bb40c4f8f9c
TASK-051: DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_32 / Issue #29 closure pending reconciliation merge
TASK-052: DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_32
TASK-055: IN_PROGRESS / SELF_HOST_RECONCILIATION_CANDIDATE / CANONICAL_INTEGRATION_PENDING
Goal Lifecycle: OUT-021 ACTIVE / AUTH-021 ACTIVE / ACT-033 IN_PROGRESS / ENV-021 ACTIVE
Current Evidence / Change: EVD-106 / CHG-106
Current Backlog: TODO=0 / IN_PROGRESS=1 / BLOCKED=0
Migration: MIG-004 / Framework 1.16.0 → 1.18.0 canonical self-host post-merge reconciliation
Exact Next Action: verify candidate then integrate to canonical main
```

## History Preservation

All predecessors are preserved under `Project-Source/archive/` and Git history. Project UUID, Stable document IDs, Project-specific truth, Project Location Binding values, and secret-reference boundary are preserved.

## Publication Boundary

PR #32 is already merged. This TASK-055 successor set is the separately authorized post-merge reconciliation candidate; canonical-main integration and Issue #29 closure require resulting-state readback before OUT-021 may become ACHIEVED.

Manifest does not recursively hash its own raw bytes.
