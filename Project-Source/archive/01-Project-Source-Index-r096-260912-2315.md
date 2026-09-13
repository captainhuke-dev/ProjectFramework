---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 96
document_status: "ACTIVE"
supersedes: "01-Project-Source-Index-r095-260912-1103.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-12T23:15:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.15.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
# 01 — Project Source Index

## Bootstrap Read Order

`PROJECT-BOOTSTRAP.md → active 00 / FRAMEWORK-001 → active 01 → active 03 → task-specific routing → active 09 when continuation applies`.

## Active Document Registry

| Slot | Active File | State |
|---|---|---|
| `00` | `00-Project-Source-Framework-r003-260911-1459.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r096-260912-2315.md` | ACTIVE |
| `02` | `02-Project-Overview-r003-260911-1459.md` | ACTIVE |
| `03` | `03-Current-State-r092-260912-2315.md` | ACTIVE |
| `04` | `04-Decision-Log-r002-260911-1459.md` | ACTIVE |
| `05` | `05-Requirements-r002-260911-1459.md` | ACTIVE |
| `09` | `09-Handoff-r092-260912-2315.md` | ACTIVE |
| `10` | `10-Change-Log-r090-260912-2315.md` | ACTIVE |
| `11` | `11-Actor-Registry-r002-260911-1459.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r036-260912-2315.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r089-260912-2315.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r096-260912-2315.md` | ACTIVE |
| `15` | `15-Action-Registry-r089-260912-2315.md` | ACTIVE |
| `16` | `16-Migration-Registry-r005-260911-1549.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r002-260911-1459.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r053-260912-2315.md` | ACTIVE |

All active Project Source documents remain Framework `1.15.0` / Schema `1.0.0` at this pre-promotion authority checkpoint. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` remain reserved.

## Current Framework / Lifecycle

- Project Source pin: Framework `1.15.0` / Schema `1.0.0` (pre-promotion authority checkpoint).
- Framework distribution: `Framework-Source/` Framework `1.16.0`; tree `5e06595f419d21b03ed2ef8e959189594628dbf2`.
- TASK-049: `IN_PROGRESS` — Canonical Self-Hosting Release Reconciliation.
- Goal / Authority / Action / Envelope: `OUT-017 ACTIVE / AUTH-017 ACTIVE / ACT-029 IN_PROGRESS / ENV-017 ACTIVE`.
- Goal checkpoint evidence/change: `EVD-093 / CHG-093`.
- Current approved gap: canonical Framework distribution is 1.16.0 while ProjectFramework active Project Source/bootstrap remain 1.15.0 until governed self-host promotion completes.
- Current backlog: `TASK-049 IN_PROGRESS` (`TODO=0 / IN_PROGRESS=1 / BLOCKED=0`).
- Framework backlog source: `docs/superpowers/PROJECT-TASKS.md`.

## Current Routing

- Current state: active `03`.
- Continuation: active `09`.
- Evidence: active `13`.
- Manifest: active `14`.
- Migration: active `16`.
- Outcome/control: active `91`.

## Exact Next Action

Add RED pressure scenarios `469–472` and verify they fail for the missing canonical self-hosting rule/state.
