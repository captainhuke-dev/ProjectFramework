---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 88
document_status: "ACTIVE"
supersedes: "01-Project-Source-Index-r087-260910-2057.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-10T21:33:39+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.7.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
# 01 — Project Source Index

Framework `1.7.0+` root `PROJECT-BOOTSTRAP.md` reaches this document only after validating active `00 / FRAMEWORK-001`. This document routes Project work; it is not a second governance root.

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
| `00` | `00-Project-Source-Framework-r002-260829-1901.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r088-260910-2133.md` | ACTIVE |
| `02` | `02-Project-Overview-r002-260829-1901.md` | ACTIVE |
| `03` | `03-Current-State-r084-260910-2057.md` | ACTIVE |
| `04` | `04-Decision-Log-r001-260829-1707.md` | ACTIVE |
| `05` | `05-Requirements-r001-260829-1707.md` | ACTIVE |
| `09` | `09-Handoff-r084-260910-2057.md` | ACTIVE |
| `10` | `10-Change-Log-r082-260910-2133.md` | ACTIVE |
| `11` | `11-Actor-Registry-r001-260829-1707.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r029-260910-2057.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r081-260910-2057.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r088-260910-2133.md` | ACTIVE |
| `15` | `15-Action-Registry-r082-260910-2057.md` | ACTIVE |
| `16` | `16-Migration-Registry-r003-260829-1916.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r001-260829-1707.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r046-260910-2057.md` | ACTIVE |

Conditional `06–08`, `40`, `60`, and `92` remain unmaterialized unless applicable. `91` remains ACTIVE for materially applicable management-control outcome history; no `OUT-013` execution authority remains active. `18–19` remain RESERVED.

## Task Routing

- Framework development backlog/lifecycle source: `docs/superpowers/PROJECT-TASKS.md`.
- Framework distribution current root: `Framework-Source/` (local TASK-045 branch is verified Framework 1.15.0 / Schema 1.0.0; final candidate `bc7f91c` passed RELEASE_FULL 33/33; publication of 1.15 is NOT_AUTHORIZED / NOT_PUSHED; canonical `origin/main` remains the published 1.14 baseline).
- ProjectFramework local Project Source pin: Framework 1.7.0 / Schema 1.0.0.
- `TASK-028 [Project Audit] Integrity & Drift Command`: DONE / implementation `a38d514` / `TASK028_FOCUSED 23/23 PASS` / `EVD-057`; target Framework 1.13.0; publication not authorized.
- Suite design: `docs/superpowers/specs/2026-09-02-task028-task032-integrity-remediation-design.md`.
- Suite plan: `docs/superpowers/plans/2026-09-02-task028-task032-integrity-remediation.md`.
- `TASK-032 Governed Project Repair / Remediation`: DONE / implementation `dd20987`; focused `23/23 PASS`; structural `40/40 PASS`; corrected AFFECTED `59/59 PASS`; final candidate `089fc186`; RELEASE_FULL `49/49 PASS`; evidence `950bff9`; cumulatively merged by PR #28 / `eda1f2b`; reconciliation checkpoint `0d7fcd4` persisted / NOT_PENDING.
- `TASK-043 Registered Command Strict-Interface & Contract Completeness Hardening`: DONE / Framework 1.12.2; candidate `a4a2712ba41c35275401b31ac49b75d45eec8643`; structural `18/18 PASS`; AFFECTED `37/37 PASS`; RELEASE_FULL `25/25 PASS`; release evidence commit `2b7a23e8c5b06a1b9f37f8f2097b06223f5fbd18`; `OUT-005 ACHIEVED / AUTH-005 TERMINATED / ACT-016 DONE / ENV-005 EXPIRED`; publication `MERGED_TO_MAIN / PERSISTED / NOT_PENDING`; PR #27 merge `bdae13896ebec08235d5ef7101f189fa6861d801`; terminal reconciliation `2da8fcbd2b11121db72599d1a6b3d33157619e17`; `OUT-006 ACHIEVED / AUTH-006 TERMINATED / ACT-018 DONE / ENV-006 EXPIRED`; `EVD-050 / EVD-051 / EVD-052`.
- TASK-043 release evidence: `docs/superpowers/evidence/2026-09-02-task-043-registered-command-strict-interface-release-full.md`.
- TASK-043 design: `docs/superpowers/specs/2026-09-02-task043-registered-command-strict-interface-design.md`.
- TASK-042 prerequisite: DONE / Framework 1.12.1 integrated; scenarios 339–350; Response Close Completeness Gate remains final global pre-emit gate.
- `TASK-036 Project Change/Event History Feed`: DONE / implementation `5c9ed7c` / focused text verification `30/30 PASS` / `EVD-066`; Framework 1.14.0 foundation A complete; no executable verifier artifact.
- `TASK-030 Cross-Project Relation Reconciliation`: DONE / implementation `360a1ad` / focused text verification `30/30 PASS` / `EVD-067`; foundation B complete; no cross-Project write/runtime.
- `TASK-029 Cross-Project Impact Analysis`: DONE / implementation `daf01eb` / focused text verification `34/34 PASS` / `EVD-068`; advisory impact contract complete; no executable verifier artifact.
- `TASK-031 Project Event & Notification Contract`: DONE / implementation `e58c7a0` / focused text verification `33/33 PASS` / `EVD-070`; notification governance complete; no delivery runtime/new command/new Stable-ID family.
- Federated Change Intelligence suite target: Framework 1.14.0 / Schema 1.0.0 / release format 3; design `d061f1f`; plan `95c1ca3`; TDD RED `23/40`; TASK-036 DONE `5c9ed7c`; TASK-030 DONE `360a1ad`; TASK-029 DONE `daf01eb`; TASK-031 DONE `e58c7a0`; Framework 1.14 local release acceptance complete: cumulative AFFECTED `33/33 PASS` / `EVD-071`; final candidate `6a9ef8c`; RELEASE_FULL `33/33 PASS_RUN_1`; release evidence `e0646c9`; OUT-008 ACHIEVED / AUTH-008 TERMINATED / ACT-020 DONE / ENV-008 EXPIRED; publication MERGED_TO_MAIN via PR #28 / merge `eda1f2b`; post-merge reconciliation checkpoint `0d7fcd4` persisted / NOT_PENDING; terminal reconciliation prepared.
- Current state: active `03`.
- Continuation: active `09`.
- Evidence: active `13`.
- Manifest: active `14`.

The derived registry is not manually authoritative over active document state.


## TASK-045 — Response Close + Next Goal
- **State:** DONE / VERIFIED_COMPLETE / LOCAL_RELEASE_VERIFIED.
- **Collision note:** V2 `TASK-044` preserved and not modified.
- **Goal:** `OUT-012 ACHIEVED / AUTH-012 TERMINATED / ACT-024 DONE / ENV-012 EXPIRED`.
- **Result:** Framework `1.15.0` visible response close = `[Next Action] -> [Next Goal] -> [Reason]`; internal Chat/Required Read routing preserved; Suggested Goal creates no authority.
- **Verification:** RED `4/13` expected; structural `13/13`; AFFECTED `27/27`; final candidate `bc7f91c`; RELEASE_FULL `33/33 PASS_RUN_1`; `EVD-080`; release evidence commit `4278182`.
- **Publication:** NOT_AUTHORIZED / NOT_PUSHED.

## Exact next action
ไม่มีขั้นตอนถัดไป for TASK-045 local completion; publication/adoption requires a new exact instruction.
## OUT-013 — Framework 1.15 Reconciliation Terminal State
- **State:** OUT-013 ACHIEVED / AUTH-013 TERMINATED / ACT-025 DONE / ENV-013 EXPIRED.
- **Framework:** local distribution 1.15.0 / Schema 1.0.0 / release format 3; no 2.0 cutover active.
- **Preserved lineage:** TASK-044 CANCELLED / IMPLEMENTATION_NOT_STARTED; TASK-045 DONE / VERIFIED_COMPLETE implementation lineage; TASK-046 CANCELLED / SUPERSEDED_BEFORE_IMPLEMENTATION.
- **Frozen verified candidate:** `16664a8b61d1641a842210773c8f997178502be5` / tree `e2db01ce75fb9c5abf7c442f6d103120c09b8a3d` / Framework-Source tree `835c5a24c909ef7de2d413c46a6451746ed5fbf0`.
- **Verification:** OUT013_AFFECTED 27/27 PASS; OUT013_RELEASE_FULL 29/29 PASS; exactly one recorded PASS run.
- **Release evidence:** `docs/superpowers/evidence/2026-09-10-out013-framework115-reconciliation-release-full.md` / evidence commit `009b4dbd5de93f56d5f9eb1c2ce1a1dedc4eedb7`.
- **Evidence / Change:** EVD-084 / CHG-084 terminal reconciliation; EVD-083 / CHG-083 retained as prior design/plan history.
- **Publication:** NOT_AUTHORIZED / NOT_PUSHED.
- **Exact Next Action:** ไม่มีขั้นตอนถัดไป for local OUT-013 completion; publication/adoption requires separate authority.
