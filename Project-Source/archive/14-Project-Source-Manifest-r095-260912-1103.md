---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 95
document_status: "ACTIVE"
supersedes: "14-Project-Source-Manifest-r094-260912-0026.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-12T11:03:41+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r095-260912-1103.md`
- `02` — `Project-Source/02-Project-Overview-r003-260911-1459.md`
- `03` — `Project-Source/03-Current-State-r091-260912-1103.md`
- `04` — `Project-Source/04-Decision-Log-r002-260911-1459.md`
- `05` — `Project-Source/05-Requirements-r002-260911-1459.md`
- `09` — `Project-Source/09-Handoff-r091-260912-1103.md`
- `10` — `Project-Source/10-Change-Log-r089-260912-1103.md`
- `11` — `Project-Source/11-Actor-Registry-r002-260911-1459.md`
- `12` — `Project-Source/12-Authorization-Registry-r035-260912-1103.md`
- `13` — `Project-Source/13-Evidence-Registry-r088-260912-1103.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r095-260912-1103.md`
- `15` — `Project-Source/15-Action-Registry-r088-260912-1103.md`
- `16` — `Project-Source/16-Migration-Registry-r005-260911-1549.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r002-260911-1459.md`
- `91` — `Project-Source/91-Project-Management-Control-r052-260912-1103.md`

All active documents above carry Framework `1.15.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` reserved.

## Framework / Publication Provenance

```text
ProjectFramework Local Project Source Pin: Framework 1.15.0 / Schema 1.0.0
Framework Distribution Root: Framework-Source/
Framework-Source Tree: 835c5a24c909ef7de2d413c46a6451746ed5fbf0
TASK-047: DONE
TASK-047 Published Implementation Commits: 196ddd0d5a2ec7c48c7a9232bafc909b0284522b / bc880c75190f967a3b87c2842b8cc284f8a3bcab
Pre-Reconciliation Canonical Observation: local main = origin/main = bc880c75190f967a3b87c2842b8cc284f8a3bcab
Publication Reconciliation Lifecycle: OUT-016 ACHIEVED / AUTH-016 TERMINATED / ACT-028 DONE / ENV-016 EXPIRED
Publication Evidence / Change: EVD-092 / CHG-092
Publication State: PUBLISHED_TO_ORIGIN_MAIN / PERSISTED / NOT_PENDING when this active Manifest is read from canonical origin/main
Current Backlog: NONE / TODO=0 / IN_PROGRESS=0 / BLOCKED=0
```
## History Preservation

All predecessors remain preserved under `Project-Source/archive/` and Git history. This publication reconciliation supersedes active revisions `01 r094`, `03 r090`, `09 r090`, `10 r088`, `12 r034`, `13 r087`, `14 r094`, `15 r087`, and `91 r051`; those predecessors remain preserved in archive/Git history.
## TASK-047 Publication-Reconciliation Boundary

This snapshot reconciles publication/current truth only. It does not change `Framework-Source`, Framework version/schema, Project Location Binding, storage, optional surfaces, application runtime, CI/CD, validator/CLI, external disclosure, secret persistence, or unrelated Task semantics.

Manifest does not recursively hash its own raw bytes.