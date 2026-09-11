---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 92
document_status: "ACTIVE"
supersedes: "14-Project-Source-Manifest-r092-260911-2308.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-11T23:08:34+07:00"
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

External bootstrap artifact: `PROJECT-BOOTSTRAP.md` → active `00 / FRAMEWORK-001`.

Active Project Source documents:

- `00` — `Project-Source/00-Project-Source-Framework-r003-260911-1459.md`
- `01` — `Project-Source/01-Project-Source-Index-r092-260911-2308.md`
- `02` — `Project-Source/02-Project-Overview-r003-260911-1459.md`
- `03` — `Project-Source/03-Current-State-r088-260911-2308.md`
- `04` — `Project-Source/04-Decision-Log-r002-260911-1459.md`
- `05` — `Project-Source/05-Requirements-r002-260911-1459.md`
- `09` — `Project-Source/09-Handoff-r088-260911-2308.md`
- `10` — `Project-Source/10-Change-Log-r086-260911-2308.md`
- `11` — `Project-Source/11-Actor-Registry-r002-260911-1459.md`
- `12` — `Project-Source/12-Authorization-Registry-r032-260911-1549.md`
- `13` — `Project-Source/13-Evidence-Registry-r085-260911-2308.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r092-260911-2308.md`
- `15` — `Project-Source/15-Action-Registry-r085-260911-1549.md`
- `16` — `Project-Source/16-Migration-Registry-r005-260911-1549.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r002-260911-1459.md`
- `91` — `Project-Source/91-Project-Management-Control-r049-260911-1549.md`

All active documents above carry Framework `1.15.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` reserved.

## Framework / Upgrade Provenance

```text
ProjectFramework Local Project Source Pin: Framework 1.15.0 / Schema 1.0.0
Framework Distribution Root: Framework-Source/
Framework-Source Tree: 835c5a24c909ef7de2d413c46a6451746ed5fbf0
Pre-upgrade Canonical Baseline: 6e3dd6c987eacdbe8430dbd906c59f5678a07843
Observed Upgrade Commit: 015f76df0ee667f45e4712bcefa0d5bc4d9bbd05
Observed Upgrade Tree: aedaf7b2b6b8fc5feda7cdd5551c441733cb8615
Migration: MIG-002 COMPLETED / ASSESSED_PATH
Evidence: EVD-086 / EVD-087 / EVD-088 / EVD-089
Changes: CHG-087 / CHG-088 / CHG-089
Lifecycle: OUT-014 ACHIEVED / AUTH-014 TERMINATED / ACT-026 DONE / ENV-014 EXPIRED
Persistence: NOT_PENDING
Current Backlog: NONE / TODO=0 / IN_PROGRESS=0 / BLOCKED=0
```

## History Preservation

All predecessors replaced during the 1.7.0 → 1.15.0 upgrade are preserved under `Project-Source/archive/` and Git history. The pre-terminal metadata revisions `01 r090`, `03 r086`, `09 r086`, `10 r084`, `12 r031`, `13 r083`, `14 r090`, `15 r084`, `16 r004`, and `91 r048` are likewise superseded by the terminal reconciliation and preserved in archive. This backlog reconciliation additionally supersedes `01 r091`, `03 r087`, `09 r087`, `10 r085`, `13 r084`, and `14 r091`; those predecessors remain preserved in archive/Git history.

## Upgrade Boundary

No Project Location Binding change, storage adoption, Project Graph activation, Knowledge/Execution/Change-Feed auto-adoption, application runtime, CI/CD, validator/CLI, external disclosure, secret persistence, or MCP→Git-native architecture migration is represented by this snapshot.

Manifest does not recursively hash its own raw bytes.
