---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 44
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-01T18:45:00+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r044-260901-1845.md`
- `02` — `Project-Source/02-Project-Overview-r002-260829-1901.md`
- `03` — `Project-Source/03-Current-State-r043-260901-1845.md`
- `04` — `Project-Source/04-Decision-Log-r001-260829-1707.md`
- `05` — `Project-Source/05-Requirements-r001-260829-1707.md`
- `09` — `Project-Source/09-Handoff-r043-260901-1845.md`
- `10` — `Project-Source/10-Change-Log-r038-260901-1845.md`
- `11` — `Project-Source/11-Actor-Registry-r001-260829-1707.md`
- `12` — `Project-Source/12-Authorization-Registry-r010-260901-1845.md`
- `13` — `Project-Source/13-Evidence-Registry-r038-260901-1845.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r044-260901-1845.md`
- `15` — `Project-Source/15-Action-Registry-r041-260901-1845.md`
- `16` — `Project-Source/16-Migration-Registry-r003-260829-1916.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r001-260829-1707.md`
- `91` — `Project-Source/91-Project-Management-Control-r026-260901-1845.md`

Conditional documents `06–08`, `40`, `60`, `92`: NOT MATERIALIZED unless applicable. `91` remains active because terminal Goal outcomes are material history, including OUT-003.

Continuation-relevant repository artifacts:

- `docs/superpowers/PROJECT-TASKS.md`
- `docs/superpowers/specs/2026-09-01-task025-project-knowledge-layer-design.md`

## Framework Source Provenance

```text
Repository: captainhuke-dev/ProjectFramework
Framework Distribution Root: Framework-Source/
Framework Upstream Local Candidate State: 1.12.0 / Schema 1.0.0
ProjectFramework Local Project Source Pin: 1.7.0 / Schema 1.0.0
Set 1 work classification: STACKED_WORK
Set 1 parent: TASK-025 completion 45a0fffc6b9040464bf24de7f6245d70465b0165
Set 1 integration order: TASK-025 before Set 1
Set 1 Tasks: TASK-033 DONE / TASK-027 DONE / TASK-034 DONE / TASK-035 DONE / TASK-037 DONE
Set 1 Goal: OUT-004 ACHIEVED / AUTH-004 TERMINATED / ACT-014 DONE / ENV-004 EXPIRED
Set 1 candidate: 125e10f1d00263ddda0031e02383b179ecd12699
Set 1 candidate tree: f7849ecebe2a8da104882b5996098befc52419c2
Set 1 Framework-Source tree: ce68037371568f98786b62f9afefc47907a91cc6
Set 1 verification: structural 159/159 PASS / AFFECTED 75/75 PASS / RELEASE_FULL 108/108 PASS
Set 1 release evidence: f37a7474235d847f14dca77d54f9c3b217eed11f / EVD-040
Set 1 publication: NOT_PUSHED
Current Git head/ref after terminal lifecycle commit: DYNAMIC / VERIFY_EACH_SESSION
Next action: ไม่มีขั้นตอนถัดไป
Captured At: 2026-09-01T18:45:00+07:00
Provenance Status: VERIFIED for recorded local completion facts subject to terminal commit observation
```

Manifest does not recursively hash its own raw bytes.
