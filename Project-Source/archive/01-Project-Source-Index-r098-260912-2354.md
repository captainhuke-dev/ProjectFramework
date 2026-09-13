---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 98
document_status: "ACTIVE"
supersedes: "01-Project-Source-Index-r097-260912-2344.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-12T23:54:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.16.0"
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
| `00` | `00-Project-Source-Framework-r004-260912-2344.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r098-260912-2354.md` | ACTIVE |
| `02` | `02-Project-Overview-r004-260912-2344.md` | ACTIVE |
| `03` | `03-Current-State-r094-260912-2354.md` | ACTIVE |
| `04` | `04-Decision-Log-r003-260912-2344.md` | ACTIVE |
| `05` | `05-Requirements-r003-260912-2344.md` | ACTIVE |
| `09` | `09-Handoff-r094-260912-2354.md` | ACTIVE |
| `10` | `10-Change-Log-r092-260912-2354.md` | ACTIVE |
| `11` | `11-Actor-Registry-r003-260912-2344.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r038-260912-2354.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r091-260912-2354.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r098-260912-2354.md` | ACTIVE |
| `15` | `15-Action-Registry-r091-260912-2354.md` | ACTIVE |
| `16` | `16-Migration-Registry-r007-260912-2354.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r003-260912-2344.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r055-260912-2354.md` | ACTIVE |

All active Project Source documents now carry Framework `1.16.0` / Schema `1.0.0`. Conditional `06–08/40/60/92` remain unmaterialized; `18–19` remain reserved.

## Current Framework / Lifecycle

- Project Source canonical self-host pin: Framework `1.16.0` / Schema `1.0.0`.
- Framework distribution: Framework `1.16.0` / Schema `1.0.0` / release format `3`; Framework-Source tree `a84e7bd0ed56bd73a7e2cb6c642885d9fefeb24a`.
- TASK-049: `DONE / LOCAL_VERIFIED / CANONICAL_INTEGRATION_PENDING`.
- Goal lifecycle: `OUT-017 BLOCKED / AUTH-017 TERMINATED / ACT-029 DONE / ENV-017 EXPIRED`.
- Terminal local evidence/change: `EVD-095 / CHG-095`; implementation evidence: `docs/superpowers/evidence/2026-09-12-task-049-canonical-self-hosting-release-full.md`.
- Verification: RED `5/10` expected → normative `8/10` → AFFECTED `25/25 PASS` → state-bound `23/23 PASS_RUN_1`.
- Verified implementation candidate: `759c7dd29c060888b3ef9c4424cdcb17cd809eed` / tree `6659e0e8494cbcff5daea89e8af16bf5ff4311b8` / Framework-Source tree `a84e7bd0ed56bd73a7e2cb6c642885d9fefeb24a`.
- Current backlog: none (`TODO=0 / IN_PROGRESS=0 / BLOCKED=0`).
- Exact next action: obtain separate integration authority if canonical `main` should adopt branch `task049-self-hosting-reconcile`; no push/PR/merge is authorized by terminated `AUTH-017`.

## Current Routing

- Current state: active `03`.
- Continuation: active `09`.
- Evidence: active `13`.
- Manifest: active `14`.
- Migration: active `16`.
- Outcome/control: active `91`.

## Exact Next Action

Obtain separate integration authority for `task049-self-hosting-reconcile` if canonical `main` should adopt the verified self-host state.
