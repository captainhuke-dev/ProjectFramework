---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 45
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-02T09:19:44+07:00"
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
→ 01-Project-Source-Index-r045-260902-0919.md
→ 03-Current-State-r044-260902-0919.md
→ task-specific routing
→ 09-Handoff-r044-260902-0919.md when continuation applies
```

## Active Document Registry

| Slot | Active File | State |
|---|---|---|
| `00` | `00-Project-Source-Framework-r002-260829-1901.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r045-260902-0919.md` | ACTIVE |
| `02` | `02-Project-Overview-r002-260829-1901.md` | ACTIVE |
| `03` | `03-Current-State-r044-260902-0919.md` | ACTIVE |
| `04` | `04-Decision-Log-r001-260829-1707.md` | ACTIVE |
| `05` | `05-Requirements-r001-260829-1707.md` | ACTIVE |
| `09` | `09-Handoff-r044-260902-0919.md` | ACTIVE |
| `10` | `10-Change-Log-r039-260902-0919.md` | ACTIVE |
| `11` | `11-Actor-Registry-r001-260829-1707.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r010-260901-1845.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r039-260902-0919.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r045-260902-0919.md` | ACTIVE |
| `15` | `15-Action-Registry-r042-260902-0919.md` | ACTIVE |
| `16` | `16-Migration-Registry-r003-260829-1916.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r001-260829-1707.md` | ACTIVE |
| `91` | `91-Project-Management-Control-r026-260901-1845.md` | ACTIVE |

Conditional `06–08`, `40`, `60`, and `92` remain unmaterialized unless applicability is established. `91` remains ACTIVE for terminal prior Goal history. `18–19` remain RESERVED.

## Task Routing

- Framework development backlog/lifecycle source: `docs/superpowers/PROJECT-TASKS.md`.
- Framework distribution current root: `Framework-Source/` (integrated local-main Framework 1.12.1 / Schema 1.0.0; canonical push pending).
- ProjectFramework local Project Source pin: Framework 1.7.0 / Schema 1.0.0.
- `TASK-041 Portable Installation Bootstrap & Project Settings Handoff`: DONE / publication reconciliation persisted on canonical main before this branch base.
- `TASK-025 Project Knowledge Layer / Compounding Knowledge Contract`: DONE locally / Framework 1.10.0 candidate `99c2f5a90e0c8f02dd68001d0e22b5362cd45a03` / AFFECTED `175/175 PASS` / RELEASE_FULL `120/120 PASS` / release evidence `e428eaa52de64546138fc4ca46fe84f1aa697e7f` / publication `NOT_PUSHED`.
- TASK-025 terminal Goal history: `OUT-003 ACHIEVED / AUTH-003 TERMINATED / ACT-013 DONE / ENV-003 EXPIRED`; Project Knowledge remains advisory/derived and does not become Project authority.
- Set 1 Foundation Suite: DONE locally — `TASK-033 / TASK-027 / TASK-034 / TASK-035 / TASK-037` DONE; Framework 1.12.0 candidate `125e10f1d00263ddda0031e02383b179ecd12699`; AFFECTED `75/75 PASS`; RELEASE_FULL `108/108 PASS`; evidence `f37a7474235d847f14dca77d54f9c3b217eed11f`; publication `NOT_PUSHED`.
- Set 1 terminal Goal history: `OUT-004 ACHIEVED / AUTH-004 TERMINATED / ACT-014 DONE / ENV-004 EXPIRED`; STACKED_WORK parent `45a0fffc6b9040464bf24de7f6245d70465b0165` must integrate before Set 1.
- `TASK-025 Project Knowledge Layer / Compounding Knowledge Contract`: DONE; integrated into local `main`; original AFFECTED `175/175 PASS`, RELEASE_FULL `120/120 PASS`; feature branch is ancestor of integration candidate.
- `Set 1 Foundation Suite`: DONE; TASK-033 / TASK-027 / TASK-034 / TASK-035 / TASK-037 integrated into local `main`; original AFFECTED `75/75 PASS`, RELEASE_FULL `108/108 PASS`; feature branch is ancestor of integration candidate.
- `TASK-042 Response Finalization Hardening`: DONE; original Framework 1.9.1 branch classified `STALE_SEMANTIC / FORWARD_PORT_REQUIRED` and forward-ported onto cumulative Framework 1.12.1; original AFFECTED `110/110 PASS`, RELEASE_FULL `171/171 PASS`; cumulative scenarios `339–350`; feature branch ancestry connected after semantic forward-port.
- Completed-work integration verification: AFFECTED `180/180 PASS`; RELEASE_FULL `14/14 PASS`; verified candidate `7b98161ceda1d53794e5f2b16855f257c560db4b` / Framework-Source tree `993b481c0d36057108df0eb87e41194bead64577`; evidence `docs/superpowers/evidence/2026-09-02-completed-work-main-integration-release-full.md` committed at `0c8d972`.
- Integration publication state: `LOCAL_MAIN_INTEGRATED / MAIN_PUSH_PENDING`; exact next action is non-force push of validated local `main` to `origin/main` followed by fresh remote verification.
- Current state: `03-Current-State-r044-260902-0919.md`.
- Continuation: `09-Handoff-r044-260902-0919.md`.
- Evidence: `13-Evidence-Registry-r039-260902-0919.md`.
- Manifest: `14-Project-Source-Manifest-r045-260902-0919.md`.

The derived registry is not manually authoritative over active document state.
