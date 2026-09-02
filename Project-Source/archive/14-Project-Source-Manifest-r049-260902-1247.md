---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 49
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-02T12:47:00+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r049-260902-1247.md`
- `02` — `Project-Source/02-Project-Overview-r002-260829-1901.md`
- `03` — `Project-Source/03-Current-State-r048-260902-1247.md`
- `04` — `Project-Source/04-Decision-Log-r001-260829-1707.md`
- `05` — `Project-Source/05-Requirements-r001-260829-1707.md`
- `09` — `Project-Source/09-Handoff-r048-260902-1247.md`
- `10` — `Project-Source/10-Change-Log-r043-260902-1247.md`
- `11` — `Project-Source/11-Actor-Registry-r001-260829-1707.md`
- `12` — `Project-Source/12-Authorization-Registry-r011-260902-1240.md`
- `13` — `Project-Source/13-Evidence-Registry-r043-260902-1247.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r049-260902-1247.md`
- `15` — `Project-Source/15-Action-Registry-r046-260902-1247.md`
- `16` — `Project-Source/16-Migration-Registry-r003-260829-1916.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r001-260829-1707.md`
- `91` — `Project-Source/91-Project-Management-Control-r027-260902-1240.md`

Conditional documents `06–08`, `40`, `60`, `92`: NOT MATERIALIZED unless applicable. `91` remains active because Goal outcomes are material current/history, including active OUT-005.

Continuation-relevant repository artifacts:

- `docs/superpowers/PROJECT-TASKS.md`
- `docs/superpowers/specs/2026-09-02-task043-registered-command-strict-interface-design.md`
- `docs/superpowers/plans/2026-09-02-task043-registered-command-strict-interface.md`

## Framework Source Provenance

```text
Repository: captainhuke-dev/ProjectFramework
Framework Distribution Root: Framework-Source/
Framework baseline at TASK-043 start: 1.12.1 / Schema 1.0.0
TASK-043 target: 1.12.2 / Schema 1.0.0 / release format 3
ProjectFramework Local Project Source Pin: 1.7.0 / Schema 1.0.0
Canonical origin/main base observed at TASK-043 branch creation: 40257f7dc97219715070b3764423c17118ecc51b
Task registration: 5401fe4
Design checkpoint: f740d16
Implementation plan checkpoint: 29e63fe
Active Goal: OUT-005 / AUTH-005 / ACT-016 / ENV-005
TDD RED: scenarios 351–356 / TASK043_STRUCTURAL 7/18 PASS / 11 expected failures
Current next action: implement Strict-Interface/gate semantics, then rerun structural verifier
Publication authority: NOT_GRANTED
Captured At: 2026-09-02T12:40:00+07:00
Provenance Status: VERIFIED
```

Manifest does not recursively hash its own raw bytes.
