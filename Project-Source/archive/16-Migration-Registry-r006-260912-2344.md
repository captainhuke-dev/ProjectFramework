---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "MIGRATION-REGISTRY-001"
document_type: "MIGRATION_REGISTRY"
semantic_slot: "16"
revision: 6
document_status: "ACTIVE"
supersedes: "16-Migration-Registry-r005-260911-1549.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-12T23:44:57+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.16.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
# 16 — Migration Registry

Historical `MIG-001` remains preserved in archive/Git history.

## MIG-002 — ProjectFramework Direct-to-Latest Framework 1.7.0 → 1.15.0

- **Status:** COMPLETED / PERSISTED / NOT_PENDING.
- **Adoption Mode:** BROWNFIELD / initialized Project.
- **Source / Target:** Framework `1.7.0` → `1.15.0`; Schema remains `1.0.0`; target release format `3`.
- **Strategy / Class:** `DIRECT_TO_LATEST_CUMULATIVE` / `ASSESSED_PATH`; intermediate release execution not required.
- **Pre-upgrade Canonical Baseline:** `6e3dd6c987eacdbe8430dbd906c59f5678a07843`.
- **Promoted Upgrade Commit:** `015f76df0ee667f45e4712bcefa0d5bc4d9bbd05` / tree `aedaf7b2b6b8fc5feda7cdd5551c441733cb8615`, freshly observed on canonical `main`.
- **Framework-Source Tree:** `835c5a24c909ef7de2d413c46a6451746ed5fbf0` unchanged.
- **Compatibility:** bounded governance/documentation migration; no schema/namespace/2.0/application-runtime migration; no non-reconstructable current truth.
- **Applied Project Corrections:** all active mandatory Project Source documents plus active `91` coherently stamped 1.15.0; stale `02` current 1.7/1.8 version truth repaired; root bootstrap revision-pointer drift repaired; every superseded active predecessor archived.
- **Preserved:** immutable Project UUID; `FRAMEWORK-001`; Project Location Binding; Stable IDs/current Project truth; source-native task/history; Git history; secret-reference boundary; Framework distribution.
- **Not Materialized / Not Changed:** optional `06–08/40/60/92`, `Project-Knowledge/`, `Project-Execution/`, `Project-Change-Feed/`, application runtime, Project Location Binding, external storage, Git-native/MCP execution architecture.
- **Approval:** ACTOR-001 explicit post-Preview mutation approval 2026-09-11.
- **Verification:** `UPGRADE_AFFECTED PASS`; one final `UPGRADE_RELEASE_FULL PASS_RUN_1` on unchanged upgrade candidate `015f76df0ee667f45e4712bcefa0d5bc4d9bbd05`; post-promotion observation/persistence `EVD-088`.
- **Rollback:** history-preserving governed successor/revert to pre-upgrade semantics; no force push/history rewrite or predecessor deletion.
- **Related:** `OUT-014`, `AUTH-014`, `ACT-026`, `ENV-014`, `EVD-086`, `EVD-087`, `EVD-088`, `CHG-087`, `CHG-088`.

`MIG-002` grants no future execution authority and does not authorize the separate MCP → Git-native/GitHub-direct architecture change.


## MIG-003 — Canonical ProjectFramework self-host reconciliation Framework 1.15.0 → 1.16.0

- **Status:** APPLIED / RESULT_VERIFICATION_PENDING.
- **Adoption Mode:** CANONICAL_SELF_HOST_POST_MERGE_RECONCILIATION; not an ordinary consuming-Project `[Project Upgrade]`.
- **Source / Target:** active Project Source Framework `1.15.0` → `1.16.0`; Schema remains `1.0.0`; release format remains `3`.
- **Normative Source Commit / Tree:** `9f5471b690df09d1993cb931a653fd85b35a2cd0` / `a84e7bd0ed56bd73a7e2cb6c642885d9fefeb24a`.
- **Canonical Merged 1.16 Baseline:** `7ffe1f871d7c0f6a8f64a9c3211425a792cde870`.
- **Strategy:** preserve-first Root successor plus coherent active Project Source/bootstrap metadata/routing reconciliation.
- **Preserved:** Project UUID; `FRAMEWORK-001` stable identity; exact Project Location Binding values; stable document IDs; Project-specific truth; predecessor history; historical MIG/CHG/EVD semantics; secret-reference boundary.
- **Consumer Boundary:** ordinary initialized Projects remain pinned and still require governed `[Project Upgrade]`; this migration is canonical-upstream self-host only.
- **Automation Boundary:** mandatory governed workflow step only; no daemon/bot/watcher/Git hook/CI/CD mutation job/scheduler/auto-updater/runtime.
- **Approval:** `AUTH-017` carries ACTOR-001 explicit persistent Goal authorization plus explicit bounded Root Governance mutation approval.
- **Verification:** pending structural/affected/final state-bound verification.
- **Related:** `OUT-017`, `AUTH-017`, `ACT-029`, `ENV-017`, `EVD-093`, `EVD-094`, `CHG-093`, `CHG-094`.
