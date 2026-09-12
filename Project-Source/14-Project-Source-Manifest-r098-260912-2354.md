---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 98
document_status: "ACTIVE"
supersedes: "14-Project-Source-Manifest-r097-260912-2344.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-12T23:54:00+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r098-260912-2354.md`
- `02` — `Project-Source/02-Project-Overview-r004-260912-2344.md`
- `03` — `Project-Source/03-Current-State-r094-260912-2354.md`
- `04` — `Project-Source/04-Decision-Log-r003-260912-2344.md`
- `05` — `Project-Source/05-Requirements-r003-260912-2344.md`
- `09` — `Project-Source/09-Handoff-r094-260912-2354.md`
- `10` — `Project-Source/10-Change-Log-r092-260912-2354.md`
- `11` — `Project-Source/11-Actor-Registry-r003-260912-2344.md`
- `12` — `Project-Source/12-Authorization-Registry-r038-260912-2354.md`
- `13` — `Project-Source/13-Evidence-Registry-r091-260912-2354.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r098-260912-2354.md`
- `15` — `Project-Source/15-Action-Registry-r091-260912-2354.md`
- `16` — `Project-Source/16-Migration-Registry-r007-260912-2354.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r003-260912-2344.md`
- `91` — `Project-Source/91-Project-Management-Control-r055-260912-2354.md`

All active documents carry Framework `1.16.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` reserved.

## Framework / Lifecycle Provenance

```text
ProjectFramework Canonical Self-Host Pin: Framework 1.16.0 / Schema 1.0.0
Framework Distribution: Framework 1.16.0 / Schema 1.0.0 / release format 3
Framework-Source Tree: a84e7bd0ed56bd73a7e2cb6c642885d9fefeb24a
Normative Source Commit: 9f5471b690df09d1993cb931a653fd85b35a2cd0
Verified Implementation Candidate: 759c7dd29c060888b3ef9c4424cdcb17cd809eed / 6659e0e8494cbcff5daea89e8af16bf5ff4311b8
TASK-049: DONE / LOCAL_VERIFIED / CANONICAL_INTEGRATION_PENDING
Goal Lifecycle: OUT-017 BLOCKED / AUTH-017 TERMINATED / ACT-029 DONE / ENV-017 EXPIRED
Terminal Evidence / Change: EVD-095 / CHG-095
Current Backlog: none / TODO=0 / IN_PROGRESS=0 / BLOCKED=0
Exact Next Action: obtain separate integration authority if canonical main should adopt task049-self-hosting-reconcile
```

## History Preservation

All predecessors remain preserved under `Project-Source/archive/` and Git history. This terminal local-control checkpoint supersedes the previous verification-pending control revisions only; verified Root `00 r004`, Bootstrap, and implementation semantics remain unchanged.

## Publication Boundary

TASK-049 implementation is locally verified. Canonical `main` integration, push/PR/merge, and release/tag publication remain separately governed and were not authorized by `AUTH-017`. `OUT-017` therefore remains blocked rather than falsely marked achieved.

Manifest does not recursively hash its own raw bytes.
