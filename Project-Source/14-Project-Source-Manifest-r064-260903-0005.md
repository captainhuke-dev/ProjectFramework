---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-SOURCE-MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 64
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-03T00:05:04+07:00"
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
- `01` — `Project-Source/01-Project-Source-Index-r064-260903-0005.md`
- `02` — `Project-Source/02-Project-Overview-r002-260829-1901.md`
- `03` — `Project-Source/03-Current-State-r062-260903-0005.md`
- `04` — `Project-Source/04-Decision-Log-r001-260829-1707.md`
- `05` — `Project-Source/05-Requirements-r001-260829-1707.md`
- `09` — `Project-Source/09-Handoff-r062-260903-0005.md`
- `10` — `Project-Source/10-Change-Log-r058-260903-0005.md`
- `11` — `Project-Source/11-Actor-Registry-r001-260829-1707.md`
- `12` — `Project-Source/12-Authorization-Registry-r017-260902-2313.md`
- `13` — `Project-Source/13-Evidence-Registry-r058-260903-0005.md`
- `14` — `Project-Source/14-Project-Source-Manifest-r064-260903-0005.md`
- `15` — `Project-Source/15-Action-Registry-r060-260903-0005.md`
- `16` — `Project-Source/16-Migration-Registry-r003-260829-1916.md`
- `17` — `Project-Source/17-Secret-Reference-Registry-r001-260829-1707.md`
- `91` — `Project-Source/91-Project-Management-Control-r033-260902-2313.md`

Conditional documents `06–08`, `40`, `60`, `92`: NOT MATERIALIZED unless applicable. `91` remains active because terminal Goal outcomes are material history and active OUT-007 is current.

Continuation-relevant repository artifacts:

- `docs/superpowers/specs/2026-09-02-task028-task032-integrity-remediation-design.md`
- `docs/superpowers/plans/2026-09-02-task028-task032-integrity-remediation.md`
- `docs/superpowers/PROJECT-TASKS.md`
- `docs/superpowers/specs/2026-09-02-task043-registered-command-strict-interface-design.md`
- `docs/superpowers/plans/2026-09-02-task043-registered-command-strict-interface.md`
- `docs/superpowers/evidence/2026-09-02-task-043-registered-command-strict-interface-release-full.md`

## Framework Source Provenance

```text
Repository: captainhuke-dev/ProjectFramework
Framework Distribution Root: Framework-Source/
Framework canonical baseline: 1.12.2 / Schema 1.0.0 / release format 3
ProjectFramework Local Project Source Pin: 1.7.0 / Schema 1.0.0
TASK-043 status: DONE local
Candidate: a4a2712ba41c35275401b31ac49b75d45eec8643
Candidate tree: 259db179349e1cdae3b8b6df0a4bec0a947b7fec
Framework-Source tree: 7417f06000e03a4e897e9d812fb0274544777a00
Scenarios: 1–356 contiguous/unique
Structural GREEN: 18/18 PASS
AFFECTED: 37/37 PASS
RELEASE_FULL: 25/25 PASS
Release evidence commit: 2b7a23e8c5b06a1b9f37f8f2097b06223f5fbd18
Goal: OUT-005 ACHIEVED / AUTH-005 TERMINATED / ACT-016 DONE / ENV-005 EXPIRED
TASK-042 preservation: VERIFIED / historical amendment unchanged
Registered Command set: unchanged
Publication: MERGED_TO_MAIN / PERSISTED / NOT_PENDING — PR #27 / merge bdae13896ebec08235d5ef7101f189fa6861d801 / terminal reconciliation 2da8fcbd2b11121db72599d1a6b3d33157619e17
Pre-PR hygiene: EVD-048 / diff-hygiene correction; Framework-Source unchanged
Next action: freeze corrected Framework 1.13.0 candidate after corrected AFFECTED 59/59 PASS
Captured At: 2026-09-02T16:06:00+07:00
Provenance Status: VERIFIED
```

Suite Goal: OUT-007 / AUTH-007 / ACT-019 / ENV-007
Suite order: TASK-028 → TASK-032
Suite target: Framework 1.13.0 / Schema 1.0.0 / release format 3
Suite base: a5e73faf3d13ed8baad6a259c52e15efc981804f
Publication authority: NOT_GRANTED
Design checkpoint: 181c715 / self-review 12/12 PASS
Plan checkpoint: 7ec4d1b / self-review 13/13 PASS
TDD RED: scenarios 357–380 / TASK028032_STRUCTURAL 14/40 PASS expected
TASK-028 implementation: a38d514 / TASK028_FOCUSED 23/23 PASS / EVD-057
TASK-028 state: DONE
TASK-032 implementation: dd20987 / TASK032_FOCUSED 23/23 PASS
TASK-032 state: IN_PROGRESS / AFFECTED_REVERIFIED / corrected candidate freeze pending
Suite structural: 40/40 PASS
Prior cumulative AFFECTED: 58/58 PASS / EVD-058
Corrected cumulative AFFECTED: 59/59 PASS / EVD-060
Prospective full branch diff hygiene: PASS
Invalidated candidate: 5991c9f / RELEASE_FULL NOT_RUN / EVD-059
Candidate hygiene: Project Source EOF normalization only; Framework-Source tree 61c27af unchanged
Corrected state: AFFECTED reverified / READY_FOR_CORRECTED_CANDIDATE_FREEZE
Maintained starters: 22/22 at Framework 1.13.0
Captured At: 2026-09-03T00:05:04+07:00

Manifest does not recursively hash its own raw bytes.
