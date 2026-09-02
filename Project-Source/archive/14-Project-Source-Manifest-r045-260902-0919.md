---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
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

# 14 — Project Source Manifest

Framework `1.7.0+` GREENFIELD Project requires `<Project-Root>/PROJECT-BOOTSTRAP.md` as an external bootstrap artifact outside semantic slots. It has no fake document/slot ID.

## Current Reconstructable Snapshot

Required external bootstrap artifact:

- `PROJECT-BOOTSTRAP.md` — root discovery/locator only

Active Project Source documents after this revision is promoted:

- `00` — `Project-Source/00-Project-Source-Framework-r002-260829-1901.md`
- `01` — `Project-Source/01-Project-Source-Index-r045-260902-0919.md`
- `02` — `Project-Source/02-Project-Overview-r002-260829-1901.md`
- `03` — `Project-Source/03-Current-State-r044-260902-0919.md`
- `04` — `Project-Source/04-Decision-Log-r001-260829-1707.md`
- `05` — `Project-Source/05-Requirements-r001-260829-1707.md`
- `09` — `Project-Source/09-Handoff-r044-260902-0919.md`
- `10` — `Project-Source/10-Change-Log-r039-260902-0919.md`
- `11` — `Project-Source/11-Actor-Registry-r001-260829-1707.md`
- `12` — `Project-Source/12-Authorization-Registry-r010-260901-1845.md`
- `13` — `Project-Source/13-Evidence-Registry-r039-260902-0919.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r045-260902-0919.md`
- `15` — `Project-Source/15-Action-Registry-r042-260902-0919.md`
- `16` — `Project-Source/16-Migration-Registry-r003-260829-1916.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r001-260829-1707.md`
- `91` — `Project-Source/91-Project-Management-Control-r026-260901-1845.md`

Conditional documents `06–08`, `40`, `60`, `92`: NOT MATERIALIZED unless applicable. `91` remains active because terminal Goal outcomes are material history, including OUT-003.

Continuation-relevant repository artifacts:

- `docs/superpowers/PROJECT-TASKS.md`
- `docs/superpowers/specs/2026-09-01-task025-project-knowledge-layer-design.md`

## Framework Source Provenance

```text
Repository: captainhuke-dev/ProjectFramework
Framework Distribution Root: Framework-Source/
Framework Upstream Integrated Local State: 1.12.1 / Schema 1.0.0
ProjectFramework Local Project Source Pin: 1.7.0 / Schema 1.0.0
Integrated work: TASK-025; Set 1 TASK-033/027/034/035/037; TASK-042 forward-port
TASK-042 Base Freshness: STALE_SEMANTIC / FORWARD_PORT_REQUIRED → FORWARD_PORTED
Cumulative scenarios: 1–350
Integration verification: AFFECTED 180/180 PASS / RELEASE_FULL 14/14 PASS
Verified integration candidate: 7b98161ceda1d53794e5f2b16855f257c560db4b
Framework-Source tree: 993b481c0d36057108df0eb87e41194bead64577
Integration evidence commit: 0c8d972 / EVD-041
Repository publication: LOCAL_MAIN_INTEGRATED / MAIN_PUSH_PENDING
Canonical origin/main before push: 5b95718f74b53685d9b6fa8c8bf21b87837fd557
Next action: push validated local main without force and fresh-verify remote
Captured At: 2026-09-02T09:19:44+07:00
Provenance Status: VERIFIED for local integration state; remote publication pending
```

Manifest does not recursively hash its own raw bytes.
