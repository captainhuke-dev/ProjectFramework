---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 4
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-08-29T19:30:00+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r004-260829-1930.md`
- `02` — `Project-Source/02-Project-Overview-r002-260829-1901.md`
- `03` — `Project-Source/03-Current-State-r004-260829-1930.md`
- `04` — `Project-Source/04-Decision-Log-r001-260829-1707.md`
- `05` — `Project-Source/05-Requirements-r001-260829-1707.md`
- `09` — `Project-Source/09-Handoff-r004-260829-1930.md`
- `10` — `Project-Source/10-Change-Log-r004-260829-1930.md`
- `11` — `Project-Source/11-Actor-Registry-r001-260829-1707.md`
- `12` — `Project-Source/12-Authorization-Registry-r001-260829-1707.md`
- `13` — `Project-Source/13-Evidence-Registry-r004-260829-1930.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r004-260829-1930.md`
- `15` — `Project-Source/15-Action-Registry-r004-260829-1930.md`
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
Verified Candidate Commit: 0f2ecfde7112a7d7d101e316fc0c3069c8ece5db
Verified Candidate Tree: a3adaeef91d3a729f9d14d570400ed73b47ee3a2
Verified Framework-Source Tree: 2101c2d22b9d23d0bae3517a6462c4895edecf15
Verification: AFFECTED 43/43 PASS; RELEASE_FULL 220/220 PASS
Release Evidence: docs/superpowers/evidence/2026-08-29-task-039-persistent-goal-command-release-full.md
Release Evidence Commit: b7f63bb949536d2ba68b4322a564533c19fe1c88
Source Ref: main (dynamic; verify when material)
Captured At: 2026-08-29T19:30:00+07:00
Provenance Status: VERIFIED for TASK-039 local candidate; remote publication NOT_PUSHED
```

Manifest does not recursively hash its own raw bytes.
