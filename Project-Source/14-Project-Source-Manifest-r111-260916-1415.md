---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 111
document_status: "ACTIVE"
supersedes: "14-Project-Source-Manifest-r111-260916-1415.md"
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
# 14 — Project Source Manifest

## Current Reconstructable Snapshot

External bootstrap artifact: `PROJECT-BOOTSTRAP.md` → active `00 / FRAMEWORK-001`.

Active Project Source documents:

- `10` — `Project-Source/10-Change-Log-r105-260916-1415.md`
- `11` — `Project-Source/11-Actor-Registry-r006-260916-1415.md`
- `12` — `Project-Source/12-Authorization-Registry-r048-260916-1415.md`
- `13` — `Project-Source/13-Evidence-Registry-r104-260916-1415.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r111-260916-1415.md`
- `15` — `Project-Source/15-Action-Registry-r103-260916-1415.md`
- `16` — `Project-Source/16-Migration-Registry-r011-260916-1415.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r006-260916-1415.md`
- `91` — `Project-Source/91-Project-Management-Control-r067-260916-1415.md`
- `00` — `Project-Source/00-Project-Source-Framework-r007-260916-1415.md`
- `01` — `Project-Source/01-Project-Source-Index-r111-260916-1415.md`
- `02` — `Project-Source/02-Project-Overview-r007-260916-1415.md`
- `03` — `Project-Source/03-Current-State-r107-260916-1415.md`
- `04` — `Project-Source/04-Decision-Log-r006-260916-1415.md`
- `05` — `Project-Source/05-Requirements-r006-260916-1415.md`
- `09` — `Project-Source/09-Handoff-r107-260916-1415.md`

All active documents carry Framework `1.19.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` reserved.

## Framework / Lifecycle Provenance

```text
ProjectFramework Canonical Self-Host Pin: Framework 1.19.0 / Schema 1.0.0
Canonical Framework Distribution: Framework 1.19.0 / Schema 1.0.0 / release format 3
TASK-057 Release Candidate: f378e0a0b4796a94ec52ba1286d17d05e6a5c9b2
Previous Reconciliation Merge (MIG-004): 5b067a1c2fcfeab867ba3879a76f675904566e27
Framework-Source Tree: 23274ada739c56a10c8edcfc14e6a9a0e46e9a0b
TASK-051: DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_32 / ISSUE_29_CLOSED
TASK-052: DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_32
TASK-055: DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_33 / ISSUE_CLOSED
TASK-057: DONE / VERIFIED_COMPLETE / PUSHED_TO_ORIGIN_MAIN / SELF_HOST_NOT_PROMOTED
TASK-058: TODO / PHASE0_SELF_HOST_1_19_IN_PROGRESS
Goal Lifecycle: OUT-021 ACHIEVED / AUTH-021 TERMINATED / ACT-033 DONE / ENV-021 EXPIRED
Current Evidence / Change: EVD-110 / CHG-109
Current Backlog: TODO=1 / IN_PROGRESS=0 / BLOCKED=0 (TASK-058)
Migration: MIG-005 / COMPLETED / PERSISTED / NOT_PENDING (MIG-004 COMPLETED / PERSISTED / NOT_PENDING)
Issue #29: CLOSED / closed_at 2026-09-13T15:47:48Z
Exact Next Action: TASK-058 normative implementation from the reconciled canonical baseline
```

## History Preservation

All predecessors are preserved under `Project-Source/archive/` and Git history. Project UUID, Stable document IDs, Project-specific truth, Project Location Binding values, and secret-reference boundary are preserved.

## Publication Boundary

The Framework 1.19.0 self-host reconciliation (MIG-005) is COMPLETED / PERSISTED / NOT_PENDING on canonical `origin/main`. This snapshot is externally claimable when this exact successor set is observed on canonical `origin/main`; TASK-058 normative implementation and tag/GitHub Release remain separately governed.

Manifest does not recursively hash its own raw bytes.
