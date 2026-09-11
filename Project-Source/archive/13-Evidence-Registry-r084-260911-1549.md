---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "EVIDENCE-REGISTRY-001"
document_type: "EVIDENCE_REGISTRY"
semantic_slot: "13"
revision: 84
document_status: "ACTIVE"
supersedes: "13-Evidence-Registry-r083-260911-1459.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-11T15:49:24+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.15.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
# 13 — Evidence Registry

Historical evidence through `EVD-085` remains preserved in archive/Git history. Current upgrade evidence is materialized below.

## EVD-086 — Framework 1.15 Project Upgrade Preview and approval

- **Type:** GOVERNED_UPGRADE_PREVIEW_AND_USER_APPROVAL
- **Current / Target:** Project Source Framework `1.7.0` → `1.15.0`; Schema `1.0.0` unchanged; target release format `3`.
- **Canonical Pre-upgrade Baseline:** `6e3dd6c987eacdbe8430dbd906c59f5678a07843`.
- **Framework-Source Tree:** `835c5a24c909ef7de2d413c46a6451746ed5fbf0`.
- **Comparison / Class:** `UPGRADE_AVAILABLE` / `ASSESSED_PATH` / Direct-to-Latest cumulative.
- **Approval:** ACTOR-001 explicit post-Preview Root/Project Source mutation approval on 2026-09-11.
- **Boundary:** approval covers Project upgrade/preservation/verification only; not MCP/Git-native architecture, binding changes, runtime, disclosure, secrets, or destructive history operations.

## EVD-087 — Corrected upgrade candidate verification

- **Type:** STATE_BOUND_UPGRADE_VERIFICATION
- **Rejected Initial Candidate:** `3df92a407e1170e238d6b8c6171ac5492032b188` — NOT_PROMOTED after verification found stale active `02` 1.7/1.8 truth and 1.7 header stamps in active `04/05/11/17`.
- **Corrected Upgrade Candidate:** `015f76df0ee667f45e4712bcefa0d5bc4d9bbd05` / tree `aedaf7b2b6b8fc5feda7cdd5551c441733cb8615`, parent `6e3dd6c987eacdbe8430dbd906c59f5678a07843`.
- **Git Freshness:** one commit ahead / zero behind; merge base exact pre-upgrade baseline; non-force fast-forward eligible.
- **Scope Verification:** diff contains root `PROJECT-BOOTSTRAP.md`, active Project Source successors, and predecessor moves to `Project-Source/archive/` only; no `Framework-Source` or unrelated path changes.
- **Active-State Verification:** active mandatory Project Source plus `91` are Framework `1.15.0` / Schema `1.0.0`; `FRAMEWORK-001` and Project UUID preserved; Project Location Binding preserved; Index/Manifest exact routing; stale `02` truth repaired; bootstrap no longer hard-codes `01/03/09` revisions; predecessor active paths removed and preserved in archive; optional surfaces not synthesized.
- **Framework Distribution Verification:** recursive corrected tree reports unchanged `Framework-Source` subtree `835c5a24c909ef7de2d413c46a6451746ed5fbf0` and unchanged release descriptor blob `720518e929c2880c46a4b531dde6bca1a2a0ccfa`.
- **Verification Result:** `UPGRADE_AFFECTED PASS`; one `UPGRADE_RELEASE_FULL PASS_RUN_1` on the unchanged corrected upgrade candidate. Verification is deterministic governance/documentation Git-tree/current-state checking; no nonexistent application-runtime test is fabricated.

## EVD-088 — Canonical promotion and terminal persistence observation

- **Type:** POST_PROMOTION_CANONICAL_OBSERVATION_AND_PERSISTENCE
- **Promotion Mode:** non-force ref updates only (`force=false`).
- **Observed Canonical Result:** `main = 015f76df0ee667f45e4712bcefa0d5bc4d9bbd05`; parent `6e3dd6c987eacdbe8430dbd906c59f5678a07843`; tree `aedaf7b2b6b8fc5feda7cdd5551c441733cb8615`.
- **Post-Promotion Readback:** active Project Source successor set visible on canonical `main`; `PROJECT-BOOTSTRAP.md` resolves `00 r003`; active root reads Framework `1.15.0` and preserves GitHub/Drive/local-workspace binding truth; active `03/09/91` terminal conditions are satisfied by the fresh canonical observation.
- **Post-Promotion Diff:** canonical `main` remains exactly one commit ahead of pre-upgrade baseline with only the approved bootstrap/Project Source/archive delta; no Framework-Source changes.
- **Release Descriptor Readback:** canonical `main` still reports Framework `1.15.0` / Schema `1.0.0` / release format `3`, Direct-to-Latest policy, and one final release-full requirement.
- **Lifecycle Result:** OUT-014 `ACHIEVED`; AUTH-014 `TERMINATED`; ACT-026 `DONE`; ENV-014 `EXPIRED`; MIG-002 `COMPLETED`; Project Source persistence `NOT_PENDING`.
- **Boundary:** no branch deletion, force push/history rewrite, Project Location Binding change, runtime implementation, optional-surface auto-adoption, external disclosure, secret persistence, AI-ControlTower/V2 cutover, or MCP→Git-native architecture migration occurred.

No evidence record stores secret values or private chain-of-thought.
