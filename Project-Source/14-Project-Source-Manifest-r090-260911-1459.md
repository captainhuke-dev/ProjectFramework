---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 90
document_status: "ACTIVE"
supersedes: "14-Project-Source-Manifest-r089-260910-2220.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-11T14:59:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.15.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
# 14 — Project Source Manifest

## Current Reconstructable Snapshot

Required external bootstrap artifact:

- `PROJECT-BOOTSTRAP.md` — root discovery/locator only; first read resolves active `00 / FRAMEWORK-001`.

Active Project Source documents:

- `00` — `Project-Source/00-Project-Source-Framework-r003-260911-1459.md`
- `01` — `Project-Source/01-Project-Source-Index-r090-260911-1459.md`
- `02` — `Project-Source/02-Project-Overview-r003-260911-1459.md`
- `03` — `Project-Source/03-Current-State-r086-260911-1459.md`
- `04` — `Project-Source/04-Decision-Log-r002-260911-1459.md`
- `05` — `Project-Source/05-Requirements-r002-260911-1459.md`
- `09` — `Project-Source/09-Handoff-r086-260911-1459.md`
- `10` — `Project-Source/10-Change-Log-r084-260911-1459.md`
- `11` — `Project-Source/11-Actor-Registry-r002-260911-1459.md`
- `12` — `Project-Source/12-Authorization-Registry-r031-260911-1459.md`
- `13` — `Project-Source/13-Evidence-Registry-r083-260911-1459.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r090-260911-1459.md`
- `15` — `Project-Source/15-Action-Registry-r084-260911-1459.md`
- `16` — `Project-Source/16-Migration-Registry-r004-260911-1459.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r002-260911-1459.md`
- `91` — `Project-Source/91-Project-Management-Control-r048-260911-1459.md`

All active files above carry Framework `1.15.0` / Schema `1.0.0` headers. Conditional `06–08`, `40`, `60`, `92`: NOT MATERIALIZED unless separately applicable. `18–19`: RESERVED.

## Framework Pin and Distribution Provenance

```text
ProjectFramework Local Project Source Pin: Framework 1.15.0 / Schema 1.0.0
Canonical Repository: captainhuke-dev/ProjectFramework
Canonical Framework Distribution Root: Framework-Source/
Framework Release: 1.15.0 / Schema 1.0.0 / release format 3
Verified Framework-Source Tree: 835c5a24c909ef7de2d413c46a6451746ed5fbf0
Pre-upgrade canonical baseline: 6e3dd6c987eacdbe8430dbd906c59f5678a07843
Upgrade: MIG-002 / ASSESSED_PATH / Direct-to-Latest 1.7.0 -> 1.15.0
Approval: ACTOR-001 explicit post-Preview mutation approval 2026-09-11T14:59:00+07:00
Evidence: EVD-086 / EVD-087
Change: CHG-087
Goal: OUT-014 / AUTH-014 / ACT-026 / ENV-014 terminal target state
```

Exact terminal commit SHA is intentionally not fabricated into this self-contained revision; it is established by fresh post-promotion Git observation and may be referenced by later history/evidence if needed.

## Preserved Historical Predecessors

The superseded active predecessor of every active slot was preserved as historical truth under `Project-Source/archive/` during `MIG-002`:

- `00-Project-Source-Framework-r002-260829-1901.md`
- `01-Project-Source-Index-r089-260910-2220.md`
- `02-Project-Overview-r002-260829-1901.md`
- `03-Current-State-r085-260910-2220.md`
- `04-Decision-Log-r001-260829-1707.md`
- `05-Requirements-r001-260829-1707.md`
- `09-Handoff-r085-260910-2220.md`
- `10-Change-Log-r083-260910-2220.md`
- `11-Actor-Registry-r001-260829-1707.md`
- `12-Authorization-Registry-r030-260910-2220.md`
- `13-Evidence-Registry-r082-260910-2220.md`
- `14-Project-Source-Manifest-r089-260910-2220.md`
- `15-Action-Registry-r083-260910-2220.md`
- `16-Migration-Registry-r003-260829-1916.md`
- `17-Secret-Reference-Registry-r001-260829-1707.md`
- `91-Project-Management-Control-r047-260910-2220.md`

## Upgrade Boundary

No Project Location Binding change, generic storage adoption, Project Graph activation, Project Knowledge, Project Execution profile, Project Change Feed, application runtime implementation, CI/CD, validator/CLI, or Git-native/MCP architecture migration is implied by this snapshot.

Manifest does not recursively hash its own raw bytes.
