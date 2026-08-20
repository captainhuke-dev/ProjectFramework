---
project_uuid: "12000000-0000-4000-8000-000000000001"
project_id: "GOLDEN-SW-001"
project_name: "HarborDesk Reference Service"
document_id: "INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-20T11:45:00+07:00"
updated_at: "2026-08-20T11:45:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-GOLDEN-001"
epistemic_status: "VERIFIED"
freshness_class: "CHANGEABLE"
project_source_framework_version: "1.2.0"
project_source_schema_version: "1.0.0"
synthetic_reference: true
---

# 01 — Project Source Index

## Bootstrap Read Order

```text
00 → 01 → 03
```

Then route by task.

## Active Document Routing

| Need | Route |
|---|---|
| Project purpose/context | `02` |
| Current state, health, cadence, next action | `03` |
| Decisions/revalidation | `04` |
| Requirements | `05` |
| Major architecture | `06` |
| Work plan | `07` |
| Issues/DRIFT/CONFLICT/Knowledge Debt | `08` |
| Continuation/handoff | `09` |
| History | `10` |
| Actors/responsibility | `11` |
| Authority | `12` |
| Evidence | `13` |
| Current snapshot inventory | `14` |
| Actions | `15` |
| Migrations | `16` |
| Secret references | `17` |
| Tech Stack/source/config/runtime/Source-Docker blueprint | `40` |
| Installation/deployment/operations blueprint | `60` |
| Risk/Assumption/Milestone/Outcome/Dependency/Change/Gate | `91` |

## Current Key Objects

```text
DEC-001 DEC-002
REQ-001 REQ-002 REQ-003
ACT-001
ISS-001
RISK-001 ASM-001 MS-001 OUT-001 DEP-001 CR-001 GATE-001
AUTH-001 EVD-001 MIG-001 SECRET-001
```

## Current Handoff

`09-Handoff-r001-260820-1145.md`

## Current Manifest

`14-Project Source Manifest-r001-260820-1145.md`
