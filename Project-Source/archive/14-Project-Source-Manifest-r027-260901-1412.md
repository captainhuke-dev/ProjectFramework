---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 27
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-01T14:12:41+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r027-260901-1412.md`
- `02` — `Project-Source/02-Project-Overview-r002-260829-1901.md`
- `03` — `Project-Source/03-Current-State-r027-260901-1412.md`
- `04` — `Project-Source/04-Decision-Log-r001-260829-1707.md`
- `05` — `Project-Source/05-Requirements-r001-260829-1707.md`
- `09` — `Project-Source/09-Handoff-r027-260901-1412.md`
- `10` — `Project-Source/10-Change-Log-r021-260901-1412.md`
- `11` — `Project-Source/11-Actor-Registry-r001-260829-1707.md`
- `12` — `Project-Source/12-Authorization-Registry-r006-260901-0820.md`
- `13` — `Project-Source/13-Evidence-Registry-r021-260901-1412.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r027-260901-1412.md`
- `15` — `Project-Source/15-Action-Registry-r025-260901-1412.md`
- `16` — `Project-Source/16-Migration-Registry-r003-260829-1916.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r001-260829-1707.md`
- `91` — `Project-Source/91-Project-Management-Control-r010-260901-0820.md`

Conditional documents `06–08`, `40`, `60`, `92`: NOT MATERIALIZED unless applicable. `91` remains active for historical management-control outcomes; no new `OUT-*` is created for TASK-025 design.

Continuation-relevant repository artifacts:

- `docs/superpowers/PROJECT-TASKS.md`
- `docs/superpowers/specs/2026-09-01-task025-project-knowledge-layer-design.md`

## Framework Source Provenance

```text
Repository: captainhuke-dev/ProjectFramework
Framework Distribution Root: Framework-Source/
Framework Upstream Released State at branch base: 1.9.0 / Schema 1.0.0
ProjectFramework Local Project Source Pin: 1.7.0 / Schema 1.0.0
TASK-025: IN_PROGRESS / ACT-012 IN_PROGRESS / written spec ready for explicit user review
TASK-025 design checkpoint: ec9911451f6a1271b473e7f1a02e8e3c1cd3d1f7 / self-review 42/42 PASS
TASK-025 proposed target: Framework 1.10.0 / Schema 1.0.0 / release format 3
TASK-025 implementation: NOT_STARTED
TASK-025 publication: NOT_PERFORMED
Branch: task025-project-knowledge
Observed branch base: origin/main 5b95718f74b53685d9b6fa8c8bf21b87837fd557
Base freshness: FRESH at branch creation; VERIFY_EACH_SESSION and re-evaluate before implementation/integration
Next action: explicit written-spec user review
Captured At: 2026-09-01T14:12:41+07:00
Provenance Status: VERIFIED for recorded current facts
```

Manifest does not recursively hash its own raw bytes.
