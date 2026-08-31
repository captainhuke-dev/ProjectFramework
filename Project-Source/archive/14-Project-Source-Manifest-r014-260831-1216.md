---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 14
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-08-31T12:16:00+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r014-260831-1216.md`
- `02` — `Project-Source/02-Project-Overview-r002-260829-1901.md`
- `03` — `Project-Source/03-Current-State-r014-260831-1216.md`
- `04` — `Project-Source/04-Decision-Log-r001-260829-1707.md`
- `05` — `Project-Source/05-Requirements-r001-260829-1707.md`
- `09` — `Project-Source/09-Handoff-r014-260831-1216.md`
- `10` — `Project-Source/10-Change-Log-r012-260831-1216.md`
- `11` — `Project-Source/11-Actor-Registry-r001-260829-1707.md`
- `12` — `Project-Source/12-Authorization-Registry-r001-260829-1707.md`
- `13` — `Project-Source/13-Evidence-Registry-r012-260831-1216.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r014-260831-1216.md`
- `15` — `Project-Source/15-Action-Registry-r012-260831-1216.md`
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
Latest completed Framework candidate: TASK-026 / commit 4c3103dfcf8e454555d234d6b3acc3571c7c2483
Latest completed Framework candidate tree: c8d589722a3e404c54f0c5e2351e412712b3927a
Latest verified Framework-Source tree: d66803fc41c540efcf072e9e45eb98c83d1f1bb5
Latest completed Framework verification: AFFECTED 144/144 PASS; RELEASE_FULL 243/243 PASS
Latest release evidence: docs/superpowers/evidence/2026-08-30-task-026-external-ai-context-disclosure-release-full.md
Latest release evidence commit: fda8300ba48a38e5b2a1e1809b9e4c6f689c1707
PR #21 integration: MERGED at c729a7b19b7cdc6d4dfdd211437d4a0b2f685da7
PR #22 post-merge reconciliation publication: MERGED at 471debc25ab353b50ace0c43f2533b4d1597d862
Published reconciliation tree: 2867d28b2c25eb9288856deb18ed92a79d415dc1
Reconciliation publication state: PERSISTED / NOT_PENDING
Observed canonical main checkpoint containing published reconciliation: 471debc25ab353b50ace0c43f2533b4d1597d862
Current Git head/ref after this bookkeeping revision: DYNAMIC / VERIFY_EACH_SESSION
Next architectural action: TASK-025 Project Knowledge Layer / Compounding Knowledge Contract design
Captured At: 2026-08-31T12:16:00+07:00
Provenance Status: VERIFIED; no Framework-Source tree drift observed
```

Manifest does not recursively hash its own raw bytes.
