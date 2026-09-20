---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "MIGRATION-REGISTRY-001"
document_type: "MIGRATION_REGISTRY"
semantic_slot: "16"
revision: 13
document_status: "ACTIVE"
supersedes: "16-Migration-Registry-r012-260920-1016.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-20T13:16:07.724+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.21.0"
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

- **Status:** VERIFIED_LOCAL / CANONICAL_INTEGRATION_PENDING.
- **Adoption Mode:** CANONICAL_SELF_HOST_POST_MERGE_RECONCILIATION; not an ordinary consuming-Project `[Project Upgrade]`.
- **Source / Target:** Framework `1.15.0` → `1.16.0`; Schema remains `1.0.0`; release format remains `3`.
- **Normative Source Commit / Tree:** `9f5471b690df09d1993cb931a653fd85b35a2cd0` / `a84e7bd0ed56bd73a7e2cb6c642885d9fefeb24a`.
- **Verified Implementation Candidate:** `759c7dd29c060888b3ef9c4424cdcb17cd809eed` / tree `6659e0e8494cbcff5daea89e8af16bf5ff4311b8`.
- **Canonical Merged 1.16 Baseline Before TASK-049:** `7ffe1f871d7c0f6a8f64a9c3211425a792cde870`.
- **Strategy:** preserve-first Root successor plus coherent active Project Source/bootstrap metadata/routing reconciliation.
- **Preserved:** Project UUID; `FRAMEWORK-001` stable identity; exact Project Location Binding values; Stable document IDs; Project-specific truth; predecessor history; historical MIG/CHG/EVD semantics; secret-reference boundary.
- **Consumer Boundary:** ordinary initialized Projects remain pinned and still require governed `[Project Upgrade]`; this migration is canonical-upstream self-host only.
- **Automation Boundary:** mandatory governed workflow step only; no daemon/bot/watcher/Git hook/CI/CD mutation job/scheduler/auto-updater/runtime.
- **Approval:** `AUTH-017` covered local Root/self-host implementation only and is now TERMINATED; canonical-main integration requires new authority.
- **Verification:** RED `5/10` expected; normative `8/10`; AFFECTED `25/25 PASS`; final state-bound `23/23 PASS_RUN_1`.
- **Local Result:** active Project Source + Bootstrap candidate coherently self-host Framework 1.16.0; `EVD-095 / CHG-095`.
- **Canonical Result:** pending integration of branch `task049-self-hosting-reconcile`; do not claim canonical `origin/main` convergence before separately authorized integration/readback.
- **Related:** `OUT-017`, `AUTH-017`, `ACT-029`, `ENV-017`, `EVD-093`, `EVD-094`, `EVD-095`, `CHG-093`, `CHG-094`, `CHG-095`.

## MIG-004 — Canonical ProjectFramework self-host reconciliation Framework 1.16.0 → 1.18.0

- **Status:** COMPLETED / PERSISTED / NOT_PENDING.
- **Adoption Mode:** CANONICAL_SELF_HOST_POST_MERGE_RECONCILIATION; not an ordinary consuming-Project `[Project Upgrade]`.
- **Source / Target:** Framework `1.16.0` → `1.18.0`; Schema remains `1.0.0`; release format remains `3`.
- **Canonical Merged Release:** PR #32 merge `f6330e9929c28977d43fc149b864d590df1c2816`; Framework-Source tree `929065ccac7e3ecf25fda09de5326bb40c4f8f9c`.
- **Strategy:** preserve-first Root successor plus coherent active Project Source/bootstrap metadata/routing reconciliation in one bounded transaction.
- **Release Evidence Reuse:** exact unchanged Framework tree reuses TASK-052 RELEASE_FULL evidence; Project-specific affected verification remains mandatory.
- **Preserved:** Project UUID; `FRAMEWORK-001` stable identity; exact Project Location Binding values; Stable document IDs; Project-specific truth; predecessor history; historical MIG/CHG/EVD semantics; secret-reference boundary.
- **Issue Reconciliation:** Issue #29 is `CLOSED` at `2026-09-13T15:47:48Z` through PR #33 `Closes #29`; fresh issue readback verified closure.
- **Consumer Boundary:** ordinary initialized Projects remain pinned and still require governed `[Project Upgrade]`; MIG-004 applies only to canonical ProjectFramework self-host.
- **Automation Boundary:** no daemon/bot/watcher/Git hook/CI-CD mutation job/scheduler/auto-updater/runtime is introduced.
- **Approval:** `AUTH-021`.
- **Verification:** `TASK055_AFFECTED 163/163 PASS`; independent HIGH review `12/12 PASS`, Critical/Important/Minor `0/0/0`, `REVIEW_PASS`; canonical PR #33 merge and Issue #29 closure freshly read back.
- **Canonical Result:** candidate `70ef176be0f07e9ce82aeeceb90b864bc28d8ea2` merged by PR #33 at `5b067a1c2fcfeab867ba3879a76f675904566e27`; canonical ProjectFramework self-host is Framework 1.18.0.
- **Related:** `TASK-055`, `OUT-021`, `AUTH-021`, `ACT-033`, `ENV-021`, `EVD-106`, `EVD-107`, `CHG-106`, `CHG-107`.

## MIG-005 - Canonical ProjectFramework self-host reconciliation Framework 1.18.0 to 1.19.0

- **Status:** COMPLETED / PERSISTED / NOT_PENDING.
- **Adoption Mode:** CANONICAL_SELF_HOST_POST_RELEASE_RECONCILIATION; not an ordinary consuming-Project `[Project Upgrade]`.
- **Source / Target:** Framework `1.18.0` to `1.19.0`; Schema remains `1.0.0`; release format remains `3`.
- **Canonical Release Basis:** TASK-057 release candidate `f378e0a0b4796a94ec52ba1286d17d05e6a5c9b2`; Framework-Source tree `23274ada739c56a10c8edcfc14e6a9a0e46e9a0b`; observed on canonical `origin/main` (head `f81992064d49c1f50f80c790667ec5be9b9ada0f`) before mutation.
- **Strategy:** preserve-first Root successor plus coherent active Project Source/bootstrap metadata/routing reconciliation in one bounded transaction; single filename stamp `260916-1332`.
- **Release Evidence Reuse:** exact unchanged Framework-Source tree reuses TASK-057 `RELEASE_FULL 77/77 PASS PASS_RUN_1`; Project-specific affected verification remains mandatory.
- **Preserved:** Project UUID; `FRAMEWORK-001` stable identity; exact Project Location Binding values; Stable document IDs; Project-specific truth; predecessor history; historical MIG/CHG/EVD semantics; secret-reference boundary.
- **Consumer Boundary:** ordinary initialized Projects remain pinned and still require governed `[Project Upgrade]`; MIG-005 applies only to canonical ProjectFramework self-host.
- **Automation Boundary:** no daemon/bot/watcher/Git hook/CI-CD mutation job/scheduler/auto-updater/runtime is introduced.
- **Approval:** ACTOR-001 explicit 2026-09-16 execution directive for TASK-058 including the Phase 0 prerequisite.
- **Verification:** Phase 0 local structural self-host checks 18/18 PASS; Project-specific affected verification 32/32 PASS; fresh canonical readback verified all 16 active stamps at 1.19.0 / 1.0.0 and Bootstrap routing.
- **Canonical Result:** candidate `5b08c5c1438aa9898daa13fae4dc00e0bcfc0df5` is canonical on `origin/main`; canonical ProjectFramework self-host is Framework 1.19.0.
- **Related:** `TASK-058`, `EVD-109`, `EVD-110`, `CHG-108`, `CHG-109`.

## MIG-006 - Canonical ProjectFramework self-host reconciliation Framework 1.19.0 to 1.20.0

- **Status:** COMPLETED / PERSISTED / NOT_PENDING.
- **Adoption Mode:** CANONICAL_SELF_HOST_POST_RELEASE_RECONCILIATION; not an ordinary consuming-Project `[Project Upgrade]`.
- **Source / Target:** Framework `1.19.0` to `1.20.0`; Schema remains `1.0.0`; release format remains `3`.
- **Canonical Release Basis:** TASK-058 frozen release candidate `63f264076becc7910b8d832db61280d064f0fb11`; Framework-Source tree `28b4003cf620f3cb553a1afea4a2b0063e47e845`; PR #35 merged to canonical `origin/main` at merge commit `71c9d9c2a1db4882f024c5537093b7dd501e9312`; observed on canonical `origin/main` before mutation.
- **Strategy:** preserve-first Root successor plus coherent active Project Source/bootstrap metadata/routing reconciliation in one bounded transaction; single filename stamp `260920-1016`.
- **Release Evidence Reuse:** exact unchanged Framework-Source tree reuses TASK-058 `RELEASE_FULL 55/55 PASS PASS_RUN_1` (frozen candidate `63f2640`); Project-specific affected verification remains mandatory.
- **Preserved:** Project UUID; `FRAMEWORK-001` stable identity; exact Project Location Binding values; Stable document IDs; Project-specific truth; predecessor history; historical MIG/CHG/EVD semantics; secret-reference boundary.
- **Consumer Boundary:** ordinary initialized Projects remain pinned and still require governed `[Project Upgrade]`; MIG-006 applies only to canonical ProjectFramework self-host.
- **Automation Boundary:** no daemon/bot/watcher/Git hook/CI-CD mutation job/scheduler/auto-updater/runtime is introduced.
- **Approval:** ACTOR-001 explicit 2026-09-20 approval ("อนุมัติ 2") for PR #35 merge and post-merge 1.20 self-host reconciliation.
- **Verification:** local structural self-host checks and Project-specific affected verification recorded at run time; fresh canonical readback verifies all 16 active stamps at 1.20.0 / 1.0.0 and Bootstrap routing.
- **Canonical Result:** the 1.20 self-host candidate is canonical on `origin/main`; canonical ProjectFramework self-host is Framework 1.20.0.
- **Related:** `TASK-058`, `EVD-111`, `CHG-110`, `MIG-005`.

## MIG-007 - Canonical ProjectFramework self-host reconciliation Framework 1.20.0 to 1.21.0

- **Status:** COMPLETED / PERSISTED / NOT_PENDING.
- **Adoption Mode:** CANONICAL_SELF_HOST_POST_RELEASE_RECONCILIATION; not an ordinary consuming-Project `[Project Upgrade]`.
- **Source / Target:** Framework `1.20.0` to `1.21.0`; Schema remains `1.0.0`; release format remains `3`.
- **Canonical Release Basis:** TASK-059 frozen release candidate `0d51582b553953a176dcb3f40fe942e177588028`; Framework-Source tree `ea6aa84b179c0f470fd6231cf364e6d8a5a59e72`; PR #36 merged to canonical `origin/main` at merge commit `7602fb10d238afcbd818874e07edb7820061b561`; observed on canonical `origin/main` before mutation.
- **Strategy:** preserve-first Root successor plus coherent active Project Source/bootstrap metadata/routing reconciliation in one bounded transaction; single filename stamp `260920-1316`.
- **Release Evidence Reuse:** exact unchanged Framework-Source tree reuses TASK-059 `RELEASE_FULL 21/21 PASS PASS_RUN_1` (frozen candidate `0d51582`); Project-specific affected verification remains mandatory.
- **Preserved:** Project UUID; `FRAMEWORK-001` stable identity; exact Project Location Binding values; Stable document IDs; Project-specific truth; predecessor history; historical MIG/CHG/EVD semantics; secret-reference boundary.
- **Consumer Boundary:** ordinary initialized Projects remain pinned and still require governed `[Project Upgrade]`; MIG-007 applies only to canonical ProjectFramework self-host.
- **Automation Boundary:** no daemon/bot/watcher/Git hook/CI-CD mutation job/scheduler/auto-updater/runtime is introduced.
- **Approval:** ACTOR-001 explicit 2026-09-20 approval ("ทำ self-host 1.21") for the post-merge 1.21 self-host reconciliation.
- **Verification:** local structural self-host checks and Project-specific affected verification recorded at run time; fresh canonical readback verifies all 16 active stamps at 1.21.0 / 1.0.0 and Bootstrap routing.
- **Canonical Result:** the 1.21 self-host candidate is canonical on `origin/main`; canonical ProjectFramework self-host is Framework 1.21.0.
- **Related:** `TASK-059`, `EVD-112`, `CHG-111`, `MIG-006`.
