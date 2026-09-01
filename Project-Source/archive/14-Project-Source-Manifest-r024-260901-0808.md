---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 24
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-01T08:08:00+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r024-260901-0808.md`
- `02` — `Project-Source/02-Project-Overview-r002-260829-1901.md`
- `03` — `Project-Source/03-Current-State-r024-260901-0808.md`
- `04` — `Project-Source/04-Decision-Log-r001-260829-1707.md`
- `05` — `Project-Source/05-Requirements-r001-260829-1707.md`
- `09` — `Project-Source/09-Handoff-r024-260901-0808.md`
- `10` — `Project-Source/10-Change-Log-r018-260901-0808.md`
- `11` — `Project-Source/11-Actor-Registry-r001-260829-1707.md`
- `12` — `Project-Source/12-Authorization-Registry-r004-260901-0808.md`
- `13` — `Project-Source/13-Evidence-Registry-r018-260901-0808.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r024-260901-0808.md`
- `15` — `Project-Source/15-Action-Registry-r022-260901-0808.md`
- `16` — `Project-Source/16-Migration-Registry-r003-260829-1916.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r001-260829-1707.md`
- `91` — `Project-Source/91-Project-Management-Control-r008-260901-0808.md`

Conditional documents `06–08`, `40`, `60`, `92`: NOT MATERIALIZED unless applicable. `91` is ACTIVE for persistent Goal outcome `OUT-001`.

## Framework Source Provenance

```text
Repository: captainhuke-dev/ProjectFramework
Framework Distribution Root: Framework-Source/
Framework Upstream Released State: 1.9.0 / Schema 1.0.0
ProjectFramework Local Project Source Pin: 1.7.0 / Schema 1.0.0
Latest published Framework completion: TASK-041 through PR #26 merge 2bfe5efbb24480bc44dbd8e949ed632af4d759ee
Published Framework-Source tree: 06ce4013473ec014e70d8d3233f6132aa90339fd
TASK-041 candidate: f5cee5fb2f3cb4da7967f56dcb294ce2a1703530 / tree 71756d53cbbcff54883915f24ef353e40b37bda6
TASK-041 release evidence commit: 06fe0c0a06d1c6c6a1abcf3c5cb9052471c5d8ef
TASK-041 publication: MERGED_TO_MAIN / PR #26
PR #26 merge tree: 51f453db8dd3942cb01c701d11ceaf4c203bd5df
Active reconciliation Goal: OUT-002 / AUTH-002 / ACT-011 / ENV-002
Current Git head/ref after this Project Source checkpoint: DYNAMIC / VERIFY_EACH_SESSION
Next action: validate/commit active reconciliation checkpoint, prepare terminal revision, fast-forward publish terminal commit to main, verify remote
Captured At: 2026-09-01T08:08:00+07:00
Provenance Status: VERIFIED for recorded PR/main/tree facts
```

Manifest does not recursively hash its own raw bytes.
