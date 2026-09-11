---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-MANAGEMENT-CONTROL-001"
document_type: "PROJECT_MANAGEMENT_CONTROL"
semantic_slot: "91"
revision: 48
document_status: "ACTIVE"
supersedes: "91-Project-Management-Control-r047-260910-2220.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-31T20:44:00+07:00"
updated_at: "2026-09-11T14:59:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "CHANGEABLE"
project_source_framework_version: "1.15.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
# 91 — Project Management Control

Historical management-control records `OUT-001` through `OUT-013` and related prior objects remain preserved in `archive/91-Project-Management-Control-r047-260910-2220.md` and Git history. This active materialized current projection retains the current/terminal `OUT-014` semantics required for present truth without relying on archive traversal.

## OUT-014 — Publish Framework 1.15 and upgrade ProjectFramework to Framework 1.15

- **Outcome Statement:** make the verified Framework 1.15 lineage canonical on `main`/`origin/main`, then upgrade this initialized ProjectFramework Project Source from Framework pin 1.7.0 to 1.15.0 through the governed `[Project Upgrade]` Direct-to-Latest flow.
- **Status:** ACHIEVED once the prepared terminal upgrade commit is freshly observed on canonical `main`; this revision represents that terminal target state and is not externally claimable before the fresh observation.
- **Success Criteria / Success Measure:** (1) fresh Base Freshness/publication evidence confirmed; (2) verified Framework 1.15 canonical publication exists; (3) remote publication identity/tree confirmed; (4) `[Project Upgrade]` comparison and cumulative Preview completed; (5) separate explicit post-Preview mutation approval captured and Brownfield Project Source/root bootstrap promoted to Framework 1.15 with history/bindings/current truth preserved; (6) upgrade verification/evidence and terminal Project Source reconciliation committed and freshly observed; (7) no force push, destructive history rewrite, V2/AI-ControlTower cutover, unauthorized disclosure, secret persistence, or unrelated architecture migration.
- **Criteria 1–3:** VERIFIED — canonical pre-upgrade `main@6e3dd6c987eacdbe8430dbd906c59f5678a07843`, parent verified lineage `c21145e1efe56bdc03791249e11c8ba42b84f93b`, Framework-Source tree `835c5a24c909ef7de2d413c46a6451746ed5fbf0`.
- **Criterion 4:** VERIFIED — comparison result `UPGRADE_AVAILABLE`; `ASSESSED_PATH`; Direct-to-Latest cumulative Preview prepared.
- **Criterion 5:** VERIFIED — ACTOR-001 explicit post-Preview mutation approval at 2026-09-11T14:59:00+07:00; `MIG-002` preserves identity/bindings/history and applies approved successor/archive/bootstrap scope.
- **Criterion 6:** VERIFIED only after `EVD-087` checks and fresh canonical observation of the terminal commit; no external completion claim before that observation.
- **Criterion 7:** VERIFIED by candidate/tree scope and post-promotion comparison; no prohibited surface is included in `MIG-002`.
- **Evidence Required / Current Evidence:** `EVD-086`, `EVD-087`, `MIG-002`, `CHG-087`, terminal Git commit observation.
- **Scope:** Framework 1.15 canonical publication reconciliation followed by ProjectFramework's governed 1.7.0 → 1.15.0 Project upgrade only.
- **Owner:** ACTOR-001 outcome owner; ACTOR-002 / INST-001 executor under `AUTH-014`.
- **Related AUTH:** `AUTH-014`.
- **Related ACT / ENV:** `ACT-026`, `ENV-014`.
- **Prohibited Zones Preserved:** force/history rewrite; destructive branch/worktree deletion; Project Location Binding mutation; Git-native/MCP architecture migration; AI-ControlTower/V2 cutover; external disclosure; secret values; unrelated Tasks; runtime implementation.
- **Terminal Evidence:** `EVD-087`; exact terminal commit SHA is established by fresh Git observation rather than self-referential fabrication in this record.
- **Success Criteria Evaluation:** terminal target semantics are materialized; `ACT DONE ≠ OUT ACHIEVED` remains binding until the exact promoted commit is freshly observed on canonical `main`, after which all seven criteria are satisfied.
