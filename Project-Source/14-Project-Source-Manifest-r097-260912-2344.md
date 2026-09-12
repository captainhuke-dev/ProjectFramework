---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 97
document_status: "ACTIVE"
supersedes: "14-Project-Source-Manifest-r096-260912-2315.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-12T23:44:57+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r097-260912-2344.md`
- `02` — `Project-Source/02-Project-Overview-r004-260912-2344.md`
- `03` — `Project-Source/03-Current-State-r093-260912-2344.md`
- `04` — `Project-Source/04-Decision-Log-r003-260912-2344.md`
- `05` — `Project-Source/05-Requirements-r003-260912-2344.md`
- `09` — `Project-Source/09-Handoff-r093-260912-2344.md`
- `10` — `Project-Source/10-Change-Log-r091-260912-2344.md`
- `11` — `Project-Source/11-Actor-Registry-r003-260912-2344.md`
- `12` — `Project-Source/12-Authorization-Registry-r037-260912-2344.md`
- `13` — `Project-Source/13-Evidence-Registry-r090-260912-2344.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r097-260912-2344.md`
- `15` — `Project-Source/15-Action-Registry-r090-260912-2344.md`
- `16` — `Project-Source/16-Migration-Registry-r006-260912-2344.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r003-260912-2344.md`
- `91` — `Project-Source/91-Project-Management-Control-r054-260912-2344.md`

All active documents above carry Framework `1.16.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` reserved.

## Framework / Lifecycle Provenance

```text
ProjectFramework Canonical Self-Host Pin: Framework 1.16.0 / Schema 1.0.0
Framework Distribution Root: Framework-Source/
Framework Distribution: Framework 1.16.0 / Schema 1.0.0 / release format 3
Incorporated Framework-Source Tree: a84e7bd0ed56bd73a7e2cb6c642885d9fefeb24a
Normative Source Commit: 9f5471b690df09d1993cb931a653fd85b35a2cd0
TASK-049: IN_PROGRESS / SELF_HOST_PROMOTED / RESULT_VERIFICATION_PENDING
Goal Lifecycle: OUT-017 ACTIVE / AUTH-017 ACTIVE / ACT-029 IN_PROGRESS / ENV-017 ACTIVE
Promotion Evidence / Change / Migration: EVD-094 / CHG-094 / MIG-003
Current Backlog: TASK-049 IN_PROGRESS / TODO=0 / IN_PROGRESS=1 / BLOCKED=0
Exact Next Action: run structural and affected verification on the promoted self-host candidate
```

## History Preservation

All predecessors remain preserved under `Project-Source/archive/` and Git history. This self-host promotion supersedes the previous active 1.15 checkpoint set while preserving Stable IDs, Project UUID, bindings, and historical record payloads.

## TASK-049 Promotion Boundary

The 1.16 self-host promotion is local and verification-pending. It does not authorize push/PR/merge/tag publication, Project Location Binding mutation, destructive history, runtime automation, external disclosure, or secret persistence. `OUT-017 / AUTH-017 / ACT-029 / ENV-017` remain active until state-bound verification and terminal evidence complete.

Manifest does not recursively hash its own raw bytes.
