---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 93
document_status: "ACTIVE"
supersedes: "14-Project-Source-Manifest-r092-260911-2308.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-12T00:16:41+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r093-260912-0016.md`
- `02` — `Project-Source/02-Project-Overview-r003-260911-1459.md`
- `03` — `Project-Source/03-Current-State-r089-260912-0016.md`
- `04` — `Project-Source/04-Decision-Log-r002-260911-1459.md`
- `05` — `Project-Source/05-Requirements-r002-260911-1459.md`
- `09` — `Project-Source/09-Handoff-r089-260912-0016.md`
- `10` — `Project-Source/10-Change-Log-r087-260912-0016.md`
- `11` — `Project-Source/11-Actor-Registry-r002-260911-1459.md`
- `12` — `Project-Source/12-Authorization-Registry-r033-260912-0016.md`
- `13` — `Project-Source/13-Evidence-Registry-r086-260912-0016.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r093-260912-0016.md`
- `15` — `Project-Source/15-Action-Registry-r086-260912-0016.md`
- `16` — `Project-Source/16-Migration-Registry-r005-260911-1549.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r002-260911-1459.md`
- `91` — `Project-Source/91-Project-Management-Control-r050-260912-0016.md`

All active documents above carry Framework `1.15.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` reserved.

## Framework / Upgrade Provenance

```text
ProjectFramework Local Project Source Pin: Framework 1.15.0 / Schema 1.0.0
Framework Distribution Root: Framework-Source/
Framework-Source Tree: 835c5a24c909ef7de2d413c46a6451746ed5fbf0
Prior Migration: MIG-002 COMPLETED / ASSESSED_PATH
Prior Evidence: EVD-086 / EVD-087 / EVD-088 / EVD-089
Prior Changes: CHG-087 / CHG-088 / CHG-089
Current Task: TASK-047 IN_PROGRESS
Current Lifecycle: OUT-015 ACTIVE / AUTH-015 ACTIVE / ACT-027 IN_PROGRESS / ENV-015 ACTIVE
Current Evidence / Change: EVD-090 / CHG-090
Response-Close Contract: existing Framework 1.15 Markdown-safe contract + Scenario 432; no Framework mutation required
Live UI Acceptance: USER_CONFIRMED
Persistence: CHECKPOINT_MATERIALIZING / REMOTE_PUBLICATION_NOT_AUTHORIZED
Current Backlog: TODO=0 / IN_PROGRESS=1 / BLOCKED=0
```

## History Preservation

All predecessors replaced during earlier Framework upgrades/reconciliations remain preserved under `Project-Source/archive/` and Git history. This TASK-047 checkpoint supersedes `01 r092`, `03 r088`, `09 r088`, `10 r086`, `12 r032`, `13 r085`, `14 r092`, `15 r085`, and `91 r049`; those predecessors are preserved in archive/Git history.

## TASK-047 Boundary

This snapshot records response-compliance regression lifecycle/evidence only. It does not change `Framework-Source`, Framework version/schema, Project Location Binding, storage, optional surfaces, application runtime, CI/CD, validator/CLI, external disclosure, secret persistence, or remote publication.

Manifest does not recursively hash its own raw bytes.
