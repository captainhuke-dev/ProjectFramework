---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 76
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-04T22:54:42+07:00"
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
→ 00-Project-Source-Framework-r002-260829-1901.md
→ 01-Project-Source-Index-r076-260904-2254.md
→ 03-Current-State-r074-260904-2254.md
→ task-specific routing
→ 09-Handoff-r074-260904-2254.md when continuation applies
```

## Active Document Registry

| Slot | Active File | State |
|---|---|---|
| `00` | `00-Project-Source-Framework-r002-260829-1901.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r076-260904-2254.md` | ACTIVE |
| `02` | `02-Project-Overview-r002-260829-1901.md` | ACTIVE |
| `03` | `03-Current-State-r074-260904-2254.md` | ACTIVE |
| `04` | `04-Decision-Log-r001-260829-1707.md` | ACTIVE |
| `05` | `05-Requirements-r001-260829-1707.md` | ACTIVE |
| `09` | `09-Handoff-r074-260904-2254.md` | ACTIVE |
| `10` | `10-Change-Log-r070-260904-2254.md` | ACTIVE |
| `11` | `11-Actor-Registry-r001-260829-1707.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r020-260904-2254.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r070-260904-2254.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r076-260904-2254.md` | ACTIVE |
| `15` | `15-Action-Registry-r072-260904-2254.md` | ACTIVE |
| `16` | `16-Migration-Registry-r003-260829-1916.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r001-260829-1707.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r036-260904-2254.md` | ACTIVE |

Conditional `06–08`, `40`, `60`, and `92` remain unmaterialized unless applicable. `91` remains ACTIVE for terminal Goal outcome history plus active `OUT-008`. `18–19` remain RESERVED.

## Task Routing

- Framework development backlog/lifecycle source: `docs/superpowers/PROJECT-TASKS.md`.
- Framework distribution current root: `Framework-Source/` (local development distribution Framework 1.14.0 / Schema 1.0.0; canonical `origin/main` remains Framework 1.12.2 until publication/integration).
- ProjectFramework local Project Source pin: Framework 1.7.0 / Schema 1.0.0.
- `TASK-028 [Project Audit] Integrity & Drift Command`: DONE / implementation `a38d514` / `TASK028_FOCUSED 23/23 PASS` / `EVD-057`; target Framework 1.13.0; publication not authorized.
- Suite design: `docs/superpowers/specs/2026-09-02-task028-task032-integrity-remediation-design.md`.
- Suite plan: `docs/superpowers/plans/2026-09-02-task028-task032-integrity-remediation.md`.
- `TASK-032 Governed Project Repair / Remediation`: DONE / implementation `dd20987`; focused `23/23 PASS`; structural `40/40 PASS`; corrected AFFECTED `59/59 PASS`; final candidate `089fc186`; RELEASE_FULL `49/49 PASS`; evidence `950bff9`; publication NOT_PUSHED.
- `TASK-043 Registered Command Strict-Interface & Contract Completeness Hardening`: DONE / Framework 1.12.2; candidate `a4a2712ba41c35275401b31ac49b75d45eec8643`; structural `18/18 PASS`; AFFECTED `37/37 PASS`; RELEASE_FULL `25/25 PASS`; release evidence commit `2b7a23e8c5b06a1b9f37f8f2097b06223f5fbd18`; `OUT-005 ACHIEVED / AUTH-005 TERMINATED / ACT-016 DONE / ENV-005 EXPIRED`; publication `MERGED_TO_MAIN / PERSISTED / NOT_PENDING`; PR #27 merge `bdae13896ebec08235d5ef7101f189fa6861d801`; terminal reconciliation `2da8fcbd2b11121db72599d1a6b3d33157619e17`; `OUT-006 ACHIEVED / AUTH-006 TERMINATED / ACT-018 DONE / ENV-006 EXPIRED`; `EVD-050 / EVD-051 / EVD-052`.
- TASK-043 release evidence: `docs/superpowers/evidence/2026-09-02-task-043-registered-command-strict-interface-release-full.md`.
- TASK-043 design: `docs/superpowers/specs/2026-09-02-task043-registered-command-strict-interface-design.md`.
- TASK-042 prerequisite: DONE / Framework 1.12.1 integrated; scenarios 339–350; Response Close Completeness Gate remains final global pre-emit gate.
- `TASK-036 Project Change/Event History Feed`: DONE / implementation `5c9ed7c` / focused text verification `30/30 PASS` / `EVD-066`; Framework 1.14.0 foundation A complete; no executable verifier artifact.
- `TASK-030 Cross-Project Relation Reconciliation`: DONE / implementation `360a1ad` / focused text verification `30/30 PASS` / `EVD-067`; foundation B complete; no cross-Project write/runtime.
- `TASK-029 Cross-Project Impact Analysis`: DONE / implementation `daf01eb` / focused text verification `34/34 PASS` / `EVD-068`; advisory impact contract complete; no executable verifier artifact.
- `TASK-031 Project Event & Notification Contract`: DONE / implementation `e58c7a0` / focused text verification `33/33 PASS` / `EVD-070`; notification governance complete; no delivery runtime/new command/new Stable-ID family.
- Federated Change Intelligence suite target: Framework 1.14.0 / Schema 1.0.0 / release format 3; design `d061f1f`; plan `95c1ca3`; TDD RED `23/40`; TASK-036 DONE `5c9ed7c`; TASK-030 DONE `360a1ad`; TASK-029 DONE `daf01eb`; TASK-031 DONE `e58c7a0`; Framework 1.14 local release acceptance complete: cumulative AFFECTED `33/33 PASS` / `EVD-071`; final candidate `6a9ef8c`; RELEASE_FULL `33/33 PASS_RUN_1`; release evidence `e0646c9`; OUT-008 ACHIEVED / AUTH-008 TERMINATED / ACT-020 DONE / ENV-008 EXPIRED; publication NOT_PUSHED / main NOT_MERGED.
- Current state: `03-Current-State-r074-260904-2254.md`.
- Continuation: `09-Handoff-r074-260904-2254.md`.
- Evidence: `13-Evidence-Registry-r070-260904-2254.md`.
- Manifest: `14-Project-Source-Manifest-r076-260904-2254.md`.

The derived registry is not manually authoritative over active document state.
