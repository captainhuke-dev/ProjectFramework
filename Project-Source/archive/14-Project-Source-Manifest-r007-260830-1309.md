---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 7
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-08-30T13:09:00+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r007-260830-1309.md`
- `02` — `Project-Source/02-Project-Overview-r002-260829-1901.md`
- `03` — `Project-Source/03-Current-State-r007-260830-1309.md`
- `04` — `Project-Source/04-Decision-Log-r001-260829-1707.md`
- `05` — `Project-Source/05-Requirements-r001-260829-1707.md`
- `09` — `Project-Source/09-Handoff-r007-260830-1309.md`
- `10` — `Project-Source/10-Change-Log-r005-260829-2301.md`
- `11` — `Project-Source/11-Actor-Registry-r001-260829-1707.md`
- `12` — `Project-Source/12-Authorization-Registry-r001-260829-1707.md`
- `13` — `Project-Source/13-Evidence-Registry-r005-260829-2301.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r007-260830-1309.md`
- `15` — `Project-Source/15-Action-Registry-r005-260829-2301.md`
- `16` — `Project-Source/16-Migration-Registry-r003-260829-1916.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r001-260829-1707.md`

Conditional documents `06–08`, `40`, `60`, `91`, `92`: NOT MATERIALIZED unless applicable.

## Framework Source Provenance

```text
Repository: captainhuke-dev/ProjectFramework
Framework Distribution Root: Framework-Source/
Framework Upstream Current Release: 1.8.0
ProjectFramework Local Project Source Pin: 1.7.0
Schema Version: 1.0.0
Latest completed Framework candidate: TASK-024 / commit e1c8ba0ad40fe956911043ff98239b7682a3d23e
Latest completed Framework candidate tree: 3cae37a05c97a3efa66ffb6f2e1cf941579187aa
Latest verified Framework-Source tree: 9a959e20723c28c58e7b37be7fd52aef8501d8f1
Latest completed Framework verification: AFFECTED 55/55 PASS; RELEASE_FULL 314/314 PASS
Latest release evidence: docs/superpowers/evidence/2026-08-29-task-024-meeting-llm-council-release-full.md
Latest release evidence commit: a4ab73696e67b6cc921e49eed62322ce477ae740
Current governance/design checkpoint: TASK-026 written design spec commit 1d61ce8790ad48bf8216af88bafd26b57e1aa979
TASK-026 design state: USER_APPROVED_DESIGN / WRITTEN_SPEC_REVIEW_REQUIRED
Source Ref: main (dynamic; verify when material)
Captured At: 2026-08-30T13:09:00+07:00
Provenance Status: VERIFIED for TASK-024 local candidate; remote publication NOT_PUSHED
```

Manifest does not recursively hash its own raw bytes.
