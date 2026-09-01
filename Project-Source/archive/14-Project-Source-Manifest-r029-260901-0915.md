---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 29
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-01T09:15:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.7.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 14 — Project Source Manifest

Framework `1.7.0+` GREENFIELD Project requires `<Project-Root>/PROJECT-BOOTSTRAP.md` as an external bootstrap artifact outside semantic slots. It has no fake document/slot ID.

## Current Reconstructable Snapshot

Required external bootstrap artifact:

- `PROJECT-BOOTSTRAP.md` — root discovery/locator only

Active Project Source documents after this revision is promoted:

- `00` — `Project-Source/00-Project-Source-Framework-r002-260829-1901.md`
- `01` — `Project-Source/01-Project-Source-Index-r029-260901-0915.md`
- `02` — `Project-Source/02-Project-Overview-r002-260829-1901.md`
- `03` — `Project-Source/03-Current-State-r029-260901-0915.md`
- `04` — `Project-Source/04-Decision-Log-r001-260829-1707.md`
- `05` — `Project-Source/05-Requirements-r001-260829-1707.md`
- `09` — `Project-Source/09-Handoff-r029-260901-0915.md`
- `10` — `Project-Source/10-Change-Log-r023-260901-0915.md`
- `11` — `Project-Source/11-Actor-Registry-r001-260829-1707.md`
- `12` — `Project-Source/12-Authorization-Registry-r007-260901-0857.md`
- `13` — `Project-Source/13-Evidence-Registry-r023-260901-0915.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r029-260901-0915.md`
- `15` — `Project-Source/15-Action-Registry-r027-260901-0915.md`
- `16` — `Project-Source/16-Migration-Registry-r003-260829-1916.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r001-260829-1707.md`
- `91` — `Project-Source/91-Project-Management-Control-r013-260901-0915.md`

Conditional documents `06–08`, `40`, `60`, `92`: NOT MATERIALIZED unless applicable. `91` is ACTIVE for terminal prior Goals plus active TASK-042 outcome `OUT-003`.

## Framework Source Provenance

```text
Repository: captainhuke-dev/ProjectFramework
Framework Distribution Root: Framework-Source/
Framework Upstream Released State: 1.9.0 / Schema 1.0.0
ProjectFramework Local Project Source Pin: 1.7.0 / Schema 1.0.0
TASK-041 publication/reconciliation: MERGED_TO_MAIN / PERSISTED / NOT_PENDING
TASK-042: IN_PROGRESS / OUT-003 ACTIVE / AUTH-003 ACTIVE / ACT-012 IN_PROGRESS / ENV-003 ACTIVE
TASK-042 target: Framework 1.9.1 / Schema 1.0.0
TASK-042 root-cause evidence: EVD-023
TASK-042 written spec: c4c163a / PASS 31/31
TASK-042 implementation plan: 1a25c29 / PASS 34/34
TASK-042 Task 1 RED: 47/74 FAIL expected / scenarios 1–280 / commit 985e84b
TASK-042 implementation: TASK_2_NORMATIVE_NEXT
TASK-042 publication authority: NOT_GRANTED_BY_GOAL
Current Git head/ref after this Project Source checkpoint: DYNAMIC / VERIFY_EACH_SESSION
Next action: implement Task 2 normative Framework 1.9.1 hardening
Captured At: 2026-09-01T09:15:00+07:00
Provenance Status: VERIFIED for recorded current facts
```

Manifest does not recursively hash its own raw bytes.
