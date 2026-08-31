---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-INDEX-001"
document_type: "PROJECT_SOURCE_INDEX"
semantic_slot: "01"
revision: 14
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-08-31T12:16:00+07:00"
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
→ 01-Project-Source-Index-r014-260831-1216.md
→ 03-Current-State-r014-260831-1216.md
→ task-specific routing
→ 09-Handoff-r014-260831-1216.md when continuation applies
```

## Active Document Registry

| Slot | Active File | State |
|---|---|---|
| `00` | `00-Project-Source-Framework-r002-260829-1901.md` | ACTIVE |
| `01` | `01-Project-Source-Index-r014-260831-1216.md` | ACTIVE |
| `02` | `02-Project-Overview-r002-260829-1901.md` | ACTIVE |
| `03` | `03-Current-State-r014-260831-1216.md` | ACTIVE |
| `04` | `04-Decision-Log-r001-260829-1707.md` | ACTIVE |
| `05` | `05-Requirements-r001-260829-1707.md` | ACTIVE |
| `09` | `09-Handoff-r014-260831-1216.md` | ACTIVE |
| `10` | `10-Change-Log-r012-260831-1216.md` | ACTIVE |
| `11` | `11-Actor-Registry-r001-260829-1707.md` | ACTIVE |
| `12` | `12-Authorization-Registry-r001-260829-1707.md` | ACTIVE |
| `13` | `13-Evidence-Registry-r012-260831-1216.md` | ACTIVE |
| `14` | `14-Project-Source-Manifest-r014-260831-1216.md` | ACTIVE |
| `15` | `15-Action-Registry-r012-260831-1216.md` | ACTIVE |
| `16` | `16-Migration-Registry-r003-260829-1916.md` | ACTIVE |
| `17` | `17-Secret-Reference-Registry-r001-260829-1707.md` | ACTIVE |

Conditional `06–08`, `40`, `60`, `91`, and `92` remain unmaterialized unless applicability is established. `18–19` remain RESERVED.

## Task Routing

- Framework development backlog/lifecycle source: `docs/superpowers/PROJECT-TASKS.md`.
- Framework distribution current root: `Framework-Source/` (upstream Framework 1.8.0).
- ProjectFramework local Project Source pin: Framework 1.7.0 / Schema 1.0.0.
- `TASK-038`: DONE; release evidence `docs/superpowers/evidence/2026-08-29-task-038-framework-source-rename-release-full.md`.
- `TASK-039`: DONE; release evidence `docs/superpowers/evidence/2026-08-29-task-039-persistent-goal-command-release-full.md`.
- `TASK-024 [Meeting]`: DONE; release evidence `docs/superpowers/evidence/2026-08-29-task-024-meeting-llm-council-release-full.md`.
- `TASK-026 External AI Context & Disclosure Governance`: DONE; AFFECTED `144/144` PASS; RELEASE_FULL `243/243` PASS; evidence `docs/superpowers/evidence/2026-08-30-task-026-external-ai-context-disclosure-release-full.md` committed at `fda8300ba48a38e5b2a1e1809b9e4c6f689c1707`.
- TASK-026 publication/integration: Pull Request `#21` was merged to `main` on `2026-08-31T10:36:13+07:00`; GitHub merge commit `c729a7b19b7cdc6d4dfdd211437d4a0b2f685da7` has parents base `eb231ee2d1d83b42455ab2f3cab250d4d442fda0` and PR head `714108a526db1a492d980690e50b1b484b88f6a1`.
- PR #21 exact pre-merge gate: `PASS 21/21`; published Framework-Source tree `d66803fc41c540efcf072e9e45eb98c83d1f1bb5` matched the state-bound TASK-026 release evidence.
- Second-AI review: `WAIVED_BY_USER / NOT_REQUIRED_FOR_PR_21` via `EVD-011`.
- Post-merge Project Source reconciliation publication: Pull Request `#22` was merged to `main` on `2026-08-31T12:08:17+07:00`; merge commit `471debc25ab353b50ace0c43f2533b4d1597d862` has parents `c729a7b19b7cdc6d4dfdd211437d4a0b2f685da7` + reconciliation head `a08e774d291deed837c7ad5b5c9e7d8d01faa921`; resulting tree `2867d28b2c25eb9288856deb18ed92a79d415dc1`; Framework-Source tree remains `d66803fc41c540efcf072e9e45eb98c83d1f1bb5`.
- Reconciliation publication state: `PERSISTED / NOT_PENDING`; canonical `main` contains the post-merge reconciliation checkpoint from PR #22.
- Next architectural action: `TASK-025 Project Knowledge Layer / Compounding Knowledge Contract`; prepare its architectural design spec before implementation.
- Current state: `03-Current-State-r014-260831-1216.md`.
- Continuation: `09-Handoff-r014-260831-1216.md`.
- Evidence: `13-Evidence-Registry-r012-260831-1216.md`.
- Manifest: `14-Project-Source-Manifest-r014-260831-1216.md`.

The derived registry is not manually authoritative over active document state.
