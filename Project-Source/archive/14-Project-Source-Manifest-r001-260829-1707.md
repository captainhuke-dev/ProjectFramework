---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-08-29T17:07:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "USER_CONFIRMED"
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

Active Project Source documents:

- `00` — `Project-Source/00-Project-Source-Framework-r001-260829-1707.md`
- `01` — `Project-Source/01-Project-Source-Index-r001-260829-1707.md`
- `02` — `Project-Source/02-Project-Overview-r001-260829-1707.md`
- `03` — `Project-Source/03-Current-State-r001-260829-1707.md`
- `04` — `Project-Source/04-Decision-Log-r001-260829-1707.md`
- `05` — `Project-Source/05-Requirements-r001-260829-1707.md`
- `09` — `Project-Source/09-Handoff-r001-260829-1707.md`
- `10` — `Project-Source/10-Change-Log-r001-260829-1707.md`
- `11` — `Project-Source/11-Actor-Registry-r001-260829-1707.md`
- `12` — `Project-Source/12-Authorization-Registry-r001-260829-1707.md`
- `13` — `Project-Source/13-Evidence-Registry-r001-260829-1707.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r001-260829-1707.md`
- `15` — `Project-Source/15-Action-Registry-r001-260829-1707.md`
- `16` — `Project-Source/16-Migration-Registry-r001-260829-1707.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r001-260829-1707.md`

Conditional documents `06–08`, `40`, `60`, `91`, `92`: NOT MATERIALIZED at initialization; create only when applicable.

## Framework Source Provenance

```text
Repository: captainhuke-dev/ProjectFramework
Framework Distribution Root: managing-project-source/
Source Ref: main (dynamic; verify when material)
Framework Version: 1.7.0
Schema Version: 1.0.0
Captured At: 2026-08-29T17:07:00+07:00
Provenance Status: VERIFIED for repository/distribution identity; exact release SHA is optional assurance and not pinned here
```

Manifest does not recursively hash its own raw bytes.
