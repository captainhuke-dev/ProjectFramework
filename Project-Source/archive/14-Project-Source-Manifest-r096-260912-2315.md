---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 96
document_status: "ACTIVE"
supersedes: "14-Project-Source-Manifest-r095-260912-1103.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-12T23:15:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.15.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
# 14 — Project Source Manifest

## Current Reconstructable Snapshot

External bootstrap artifact: `PROJECT-BOOTSTRAP.md` → active `00 / FRAMEWORK-001`.

Active Project Source documents:

- `00` — `Project-Source/00-Project-Source-Framework-r003-260911-1459.md`
- `01` — `Project-Source/01-Project-Source-Index-r096-260912-2315.md`
- `02` — `Project-Source/02-Project-Overview-r003-260911-1459.md`
- `03` — `Project-Source/03-Current-State-r092-260912-2315.md`
- `04` — `Project-Source/04-Decision-Log-r002-260911-1459.md`
- `05` — `Project-Source/05-Requirements-r002-260911-1459.md`
- `09` — `Project-Source/09-Handoff-r092-260912-2315.md`
- `10` — `Project-Source/10-Change-Log-r090-260912-2315.md`
- `11` — `Project-Source/11-Actor-Registry-r002-260911-1459.md`
- `12` — `Project-Source/12-Authorization-Registry-r036-260912-2315.md`
- `13` — `Project-Source/13-Evidence-Registry-r089-260912-2315.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r096-260912-2315.md`
- `15` — `Project-Source/15-Action-Registry-r089-260912-2315.md`
- `16` — `Project-Source/16-Migration-Registry-r005-260911-1549.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r002-260911-1459.md`
- `91` — `Project-Source/91-Project-Management-Control-r053-260912-2315.md`

All active Project Source documents remain Framework `1.15.0` / Schema `1.0.0` at this pre-promotion authority checkpoint. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` reserved.

## Framework / Lifecycle Provenance

```text
ProjectFramework Local Project Source Pin: Framework 1.15.0 / Schema 1.0.0 (pre-promotion checkpoint)
Framework Distribution Root: Framework-Source/
Framework Distribution: Framework 1.16.0 / Schema 1.0.0 / release format 3
Framework-Source Tree: 5e06595f419d21b03ed2ef8e959189594628dbf2
TASK-049: IN_PROGRESS / Canonical Self-Hosting Release Reconciliation
Goal Lifecycle: OUT-017 ACTIVE / AUTH-017 ACTIVE / ACT-029 IN_PROGRESS / ENV-017 ACTIVE
Goal Checkpoint Evidence / Change: EVD-093 / CHG-093
Current Backlog: TASK-049 IN_PROGRESS / TODO=0 / IN_PROGRESS=1 / BLOCKED=0
Exact Next Action: add RED pressure scenarios 469–472 and verify the missing self-hosting contract/state
```

## History Preservation

All predecessors remain preserved under `Project-Source/archive/` and Git history. This Goal-activation checkpoint supersedes active revisions `01 r095`, `03 r091`, `09 r091`, `10 r089`, `12 r035`, `13 r088`, `14 r095`, `15 r088`, and `91 r052`; those predecessors remain preserved in archive/Git history.

## TASK-049 Pre-Promotion Boundary

This checkpoint creates Task/Goal/authority/evidence routing only. It does not yet change active `FRAMEWORK-001`, active `16`, `PROJECT-BOOTSTRAP.md`, Framework-Source semantics, Project Location Binding, runtime/CI/CD, external disclosure, secret persistence, or remote publication. Root/self-host promotion begins only after RED scenarios `469–472` establish the missing contract.

Manifest does not recursively hash its own raw bytes.
