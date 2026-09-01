---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 30
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-01T13:45:00+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r030-260901-1345.md`
- `02` — `Project-Source/02-Project-Overview-r002-260829-1901.md`
- `03` — `Project-Source/03-Current-State-r030-260901-1345.md`
- `04` — `Project-Source/04-Decision-Log-r001-260829-1707.md`
- `05` — `Project-Source/05-Requirements-r001-260829-1707.md`
- `09` — `Project-Source/09-Handoff-r030-260901-1345.md`
- `10` — `Project-Source/10-Change-Log-r024-260901-1345.md`
- `11` — `Project-Source/11-Actor-Registry-r001-260829-1707.md`
- `12` — `Project-Source/12-Authorization-Registry-r008-260901-1345.md`
- `13` — `Project-Source/13-Evidence-Registry-r024-260901-1345.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r030-260901-1345.md`
- `15` — `Project-Source/15-Action-Registry-r028-260901-1345.md`
- `16` — `Project-Source/16-Migration-Registry-r003-260829-1916.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r001-260829-1707.md`
- `91` — `Project-Source/91-Project-Management-Control-r014-260901-1345.md`

Conditional documents `06–08`, `40`, `60`, `92`: NOT MATERIALIZED unless applicable. `91` is ACTIVE for terminal prior Goals including terminal TASK-042 outcome `OUT-003`.

## Framework Source Provenance

```text
Repository: captainhuke-dev/ProjectFramework
Framework Distribution Root: Framework-Source/
Framework Upstream Local Candidate State: 1.9.1 / Schema 1.0.0
ProjectFramework Local Project Source Pin: 1.7.0 / Schema 1.0.0
TASK-041 publication/reconciliation: MERGED_TO_MAIN / PERSISTED / NOT_PENDING
TASK-042: DONE locally / OUT-003 ACHIEVED / AUTH-003 TERMINATED / ACT-012 DONE / ENV-003 EXPIRED
TASK-042 candidate: d698ee25f4337535c1c991721c617ee7f7cf9de2
TASK-042 candidate tree: 4a8546f38d1c4ff223620924fa477c1f3a723c58
TASK-042 Framework-Source tree: 9f8bac7fd32a21af6244a9723739a2f747810f70
TASK-042 verification: structural GREEN 74/74 PASS; AFFECTED 110/110 PASS; RELEASE_FULL 171/171 PASS
TASK-042 release evidence: docs/superpowers/evidence/2026-09-01-task-042-response-finalization-hardening-release-full.md
TASK-042 release evidence commit: 6547769876af52a0c3ff196cad434cd083f5fd53
TASK-042 publication: NOT_PUSHED
Next roadmap candidate: TASK-025 (not started)
Current Git head/ref after this Project Source checkpoint: DYNAMIC / VERIFY_EACH_SESSION
Next action: ไม่มีขั้นตอนถัดไป
Captured At: 2026-09-01T13:45:00+07:00
Provenance Status: VERIFIED for recorded candidate/evidence facts
```

Manifest does not recursively hash its own raw bytes.
