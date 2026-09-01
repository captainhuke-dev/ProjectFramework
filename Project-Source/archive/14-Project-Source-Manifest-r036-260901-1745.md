---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 36
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-01T17:45:00+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r036-260901-1745.md`
- `02` — `Project-Source/02-Project-Overview-r002-260829-1901.md`
- `03` — `Project-Source/03-Current-State-r035-260901-1745.md`
- `04` — `Project-Source/04-Decision-Log-r001-260829-1707.md`
- `05` — `Project-Source/05-Requirements-r001-260829-1707.md`
- `09` — `Project-Source/09-Handoff-r035-260901-1745.md`
- `10` — `Project-Source/10-Change-Log-r030-260901-1745.md`
- `11` — `Project-Source/11-Actor-Registry-r001-260829-1707.md`
- `12` — `Project-Source/12-Authorization-Registry-r009-260901-1721.md`
- `13` — `Project-Source/13-Evidence-Registry-r030-260901-1745.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r036-260901-1745.md`
- `15` — `Project-Source/15-Action-Registry-r033-260901-1745.md`
- `16` — `Project-Source/16-Migration-Registry-r003-260829-1916.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r001-260829-1707.md`
- `91` — `Project-Source/91-Project-Management-Control-r018-260901-1745.md`

Conditional documents `06–08`, `40`, `60`, `92`: NOT MATERIALIZED unless applicable. `91` remains active because terminal Goal outcomes are material history, including OUT-003.

Continuation-relevant repository artifacts:

- `docs/superpowers/PROJECT-TASKS.md`
- `docs/superpowers/specs/2026-09-01-task025-project-knowledge-layer-design.md`

## Framework Source Provenance

```text
Repository: captainhuke-dev/ProjectFramework
Framework Distribution Root: Framework-Source/
Framework Upstream Local Candidate State: 1.10.0 / Schema 1.0.0
ProjectFramework Local Project Source Pin: 1.7.0 / Schema 1.0.0
TASK-025: DONE_LOCAL / OUT-003 ACHIEVED / AUTH-003 TERMINATED / ACT-012 DONE / ACT-013 DONE / ENV-003 EXPIRED
TASK-025 candidate: 99c2f5a90e0c8f02dd68001d0e22b5362cd45a03
TASK-025 candidate tree: 26d1f5354ab0a59616b9fbca28d25c74ac6746ca
TASK-025 Framework-Source tree: d39c4550a4272e3ae2c5f957ec444f93bd514485
TASK-025 verification: GREEN 68/68 / Task2 62/62 / Task3 77/77 / AFFECTED 175/175 / RELEASE_FULL 120/120 PASS
TASK-025 release evidence: e428eaa52de64546138fc4ca46fe84f1aa697e7f / EVD-028
TASK-025 publication: NOT_PUSHED
Current Git head/ref after terminal lifecycle commit: DYNAMIC / VERIFY_EACH_SESSION
Next action: ไม่มีขั้นตอนถัดไป
Captured At: 2026-09-01T16:16:00+07:00
Provenance Status: VERIFIED for recorded local completion facts; EVD-029 records terminal diff-hygiene correction
```

Manifest does not recursively hash its own raw bytes.
