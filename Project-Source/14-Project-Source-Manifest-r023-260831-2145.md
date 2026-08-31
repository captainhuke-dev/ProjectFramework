---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 23
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-08-31T21:45:00+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r018-260831-2059.md`
- `02` — `Project-Source/02-Project-Overview-r002-260829-1901.md`
- `03` — `Project-Source/03-Current-State-r023-260831-2145.md`
- `04` — `Project-Source/04-Decision-Log-r001-260829-1707.md`
- `05` — `Project-Source/05-Requirements-r001-260829-1707.md`
- `09` — `Project-Source/09-Handoff-r023-260831-2145.md`
- `10` — `Project-Source/10-Change-Log-r017-260831-2145.md`
- `11` — `Project-Source/11-Actor-Registry-r001-260829-1707.md`
- `12` — `Project-Source/12-Authorization-Registry-r003-260831-2145.md`
- `13` — `Project-Source/13-Evidence-Registry-r017-260831-2145.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r023-260831-2145.md`
- `15` — `Project-Source/15-Action-Registry-r021-260831-2145.md`
- `16` — `Project-Source/16-Migration-Registry-r003-260829-1916.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r001-260829-1707.md`
- `91` — `Project-Source/91-Project-Management-Control-r007-260831-2145.md`

Conditional documents `06–08`, `40`, `60`, `92`: NOT MATERIALIZED unless applicable. `91` is ACTIVE for persistent Goal outcome `OUT-001`.

## Framework Source Provenance

```text
Repository: captainhuke-dev/ProjectFramework
Framework Distribution Root: Framework-Source/
Framework Upstream Released State: 1.8.0 / Schema 1.0.0
ProjectFramework Local Project Source Pin: 1.7.0 / Schema 1.0.0
Latest published Framework completion: TASK-040 through PR #24 merge 5a51b105ff4430c04605dcb254d41a8e80faad8b
Published Framework-Source tree: 36804c105604fe8da492a9d71a1f0270e5e035ee
TASK-041 target: Framework 1.9.0 / Schema 1.0.0
TASK-041 written design checkpoint: da1d2201eead976c4e4ad10e97afb244664dc571
TASK-041 spec self-review: PASS 30/30
TASK-041: DONE locally / OUT-001 ACHIEVED / AUTH-001 TERMINATED / ENV-001 EXPIRED
Latest completed Framework candidate: TASK-041 / commit f5cee5fb2f3cb4da7967f56dcb294ce2a1703530
Latest completed Framework candidate tree: 71756d53cbbcff54883915f24ef353e40b37bda6
Latest verified Framework-Source tree: 06ce4013473ec014e70d8d3233f6132aa90339fd
Latest completed Framework verification: AFFECTED 273/273 PASS; RELEASE_FULL 248/248 PASS
Latest release evidence: docs/superpowers/evidence/2026-08-31-task-041-portable-installation-bootstrap-release-full.md
Latest release evidence commit: 06fe0c0a06d1c6c6a1abcf3c5cb9052471c5d8ef
TASK-041 publication: NOT_PUSHED
Next roadmap candidate: TASK-025 Project Knowledge Layer / Compounding Knowledge Contract design (not started)
Current Git head/ref after this Project Source checkpoint: DYNAMIC / VERIFY_EACH_SESSION
Task 2 normative: PASS 51/51 / commit 61bfb3724347a4cba988d987604ade92f66cc45d
Task 3 thin adapters: PASS 42/42 / commit 062c20a8bedc002650dd059e65b1fa792db6dd8c
Task 4 README/starter: PASS 53/53 / commit 5d2349ab2e89091e7bbf31c5ae2d9a76e7fc1e6e / RED 93/97 migration-only
Next action: execute Task 5 migration + affected candidate
Captured At: 2026-08-31T21:45:00+07:00
Provenance Status: VERIFIED for recorded Git/design checkpoint facts
```

Manifest does not recursively hash its own raw bytes.
