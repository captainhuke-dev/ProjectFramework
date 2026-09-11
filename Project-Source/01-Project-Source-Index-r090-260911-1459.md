---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 90
document_status: "ACTIVE"
supersedes: "01-Project-Source-Index-r089-260910-2220.md"
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
# 01 — Project Source Index

`PROJECT-BOOTSTRAP.md` reaches this document only after validating active `00 / FRAMEWORK-001`. This document routes Project work; it is not a second governance root.

## Bootstrap Read Order

```text
PROJECT-BOOTSTRAP.md
→ active 00 / FRAMEWORK-001
→ active 01 / Project Source Index
→ active 03 / Current State
→ task-specific routing
→ active 09 / Handoff when continuation applies
```

## Active Document Registry

| Slot | Active File | State |
|---|---|---|
| `00` | `00-Project-Source-Framework-r003-260911-1459.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r090-260911-1459.md` | ACTIVE |
| `02` | `02-Project-Overview-r003-260911-1459.md` | ACTIVE |
| `03` | `03-Current-State-r086-260911-1459.md` | ACTIVE |
| `04` | `04-Decision-Log-r002-260911-1459.md` | ACTIVE |
| `05` | `05-Requirements-r002-260911-1459.md` | ACTIVE |
| `09` | `09-Handoff-r086-260911-1459.md` | ACTIVE |
| `10` | `10-Change-Log-r084-260911-1459.md` | ACTIVE |
| `11` | `11-Actor-Registry-r002-260911-1459.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r031-260911-1459.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r083-260911-1459.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r090-260911-1459.md` | ACTIVE |
| `15` | `15-Action-Registry-r084-260911-1459.md` | ACTIVE |
| `16` | `16-Migration-Registry-r004-260911-1459.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r002-260911-1459.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r048-260911-1459.md` | ACTIVE |

All active mandatory Project Source documents plus active conditional `91` are stamped Framework `1.15.0` / Schema `1.0.0`. Conditional `06–08`, `40`, `60`, and `92` remain unmaterialized because this upgrade does not establish new applicability. `18–19` remain RESERVED.

## Current Framework and Upgrade Routing

- ProjectFramework Project Source pin: Framework `1.15.0` / Schema `1.0.0`.
- Framework distribution: `Framework-Source/`, Framework `1.15.0`, Schema `1.0.0`, release format `3`.
- Verified pre-upgrade canonical publication baseline: `main@6e3dd6c987eacdbe8430dbd906c59f5678a07843`; Framework-Source tree `835c5a24c909ef7de2d413c46a6451746ed5fbf0`.
- Direct-to-Latest Project upgrade: `MIG-002`, path class `ASSESSED_PATH`, source pin `1.7.0`, target pin `1.15.0`.
- Upgrade approval/evidence: `EVD-086`; resulting-state verification: `EVD-087`.
- Applied upgrade change: `CHG-087`.
- Goal/action lifecycle: `OUT-014 / AUTH-014 / ACT-026 / ENV-014` terminalized subject to fresh canonical observation of the terminal commit, as recorded in their canonical homes.
- Framework development backlog/lifecycle source remains `docs/superpowers/PROJECT-TASKS.md`.

## Current Routing

- Current state: active `03`.
- Continuation: active `09`.
- Evidence: active `13`.
- Manifest: active `14`.
- Migration: active `16`.
- Outcome/management control: active `91`.

## Active Warnings / Drift / Conflict

None known within the approved 1.7.0 → 1.15.0 upgrade scope after the terminal resulting-state verification recorded by `EVD-087`. Historical predecessor revisions are preserved under `Project-Source/archive/`.

## Exact Next Action

ไม่มีขั้นตอนถัดไป for this Project upgrade after terminal commit observation; Git-native/MCP execution-architecture changes remain a separate scope and are not authorized by `MIG-002`.
