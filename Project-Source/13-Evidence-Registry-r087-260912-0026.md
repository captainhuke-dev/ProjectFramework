---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "EVIDENCE-REGISTRY-001"
document_type: "EVIDENCE_REGISTRY"
semantic_slot: "13"
revision: 87
document_status: "ACTIVE"
supersedes: "13-Evidence-Registry-r086-260912-0016.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-12T00:26:10+07:00"
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

## EVD-089 - User-directed current backlog cancellation reconciliation

- **Type:** USER_INSTRUCTION_AND_CURRENT_BACKLOG_RECONCILIATION
- **User Instruction:** ACTOR-001 directed that `CANCELLED` work not be reported as remaining work and that unstarted scope already present in this Project be cancelled rather than retained as backlog.
- **Fresh Pre-Mutation Git Observation:** local `main = origin/main = bf53f30a18f28c1d05284980984429ec30d7dd36`; working tree clean.
- **Fresh Current-State Scan:** current Task ledger contains zero `TODO`, zero `IN_PROGRESS`, and zero `BLOCKED` Tasks. Active Project Source contains exactly three future-scope references, all naming the same unregistered Git-native/MCP execution-architecture scope in active `01`, `03`, and `09`.
- **Reconciliation Result:** that unstarted future scope is cancelled before Task/Goal creation and removed from active remaining-work/current-state surfaces. Remaining-work reporting is normalized to `TODO | IN_PROGRESS | BLOCKED`; cancelled history remains available only when history/cancelled work is explicitly requested.
- **Boundary:** historical Task records and archives are preserved; no Framework distribution, runtime, binding, remote publication, external workspace, disclosure, or secret mutation is authorized or performed.

No evidence record stores secret values or private chain-of-thought.

## EVD-090 — TASK-047 regression reproduction, root cause, design approval, and live UI acceptance

- **Type:** REGRESSION_OBSERVATION / ROOT_CAUSE_EVIDENCE / USER_CONFIRMED_UI_ACCEPTANCE.
- **Observed Regression:** after successful `.md` bootstrap, an assistant response emitted bare `[Next Action]:` and `[Next Goal]:` lines; the user-provided UI screenshot showed those two fields absent while `[Reason]:` remained visible. The prior assistant `PASS` claim was corrected to `FAIL`.
- **Root Cause Investigation:** current `Framework-Source/SKILL.md` already requires Markdown-safe visible fields `**[Next Action]:**`, `**[Next Goal]:**`, `**[Reason]:**` as separate paragraphs in that order, and `Framework-Source/tests/pressure-scenarios.md` Scenario 432 explicitly treats hidden/non-visible labels as failure. Git history also contains `16664a8` (`docs(framework): reconcile 1.15 response close drift`) establishing the existing safe-wrapper contract.
- **Root Cause Classification:** response-generation/compliance failure against an already-correct Framework contract; not a missing Framework semantic rule and not a Project Source binding/bootstrap defect.
- **TDD RED Observation:** before TASK-047 materialization, `TASK-047=False` while `SCENARIO_432=True` and `MARKDOWN_SAFE_SKILL=True`; the bounded regression lifecycle/evidence was absent as expected.
- **Bounded Design Approval:** ACTOR-001 explicitly replied `อนุมัติ` after the proposed approach stated that no Framework semantic change would be made and that TASK-047 would close only on Scenario 432 plus live UI acceptance.
- **Live UI Acceptance:** the approval prompt explicitly required ACTOR-001 to reply `อนุมัติ` only if the immediately preceding Markdown-safe footer visibly showed `[Next Action] → [Next Goal] → [Reason]` in the ChatGPT UI. The reply therefore records USER_CONFIRMED live-UI acceptance for the safe presentation.
- **Boundary:** no `Framework-Source` semantic/version mutation, runtime enforcement, UI hook, parser, validator, push/publication, binding change, disclosure, or secret persistence is authorized by this evidence.

## EVD-091 — TASK-047 GREEN verification and completion checkpoint

- **Type:** TASK_COMPLETION_VERIFICATION / RESULTING_STATE_EVIDENCE.
- **TDD Cycle:** RED was observed before lifecycle materialization; GREEN was then run after TASK/Goal/checkpoint promotion and returned `TASK047_GREEN=PASS`.
- **GREEN Coverage:** TASK-047 registration/status; SKILL Markdown-safe `Next Action` / `Next Goal` / `Reason`; Scenario 432; EVD-090; OUT-015/AUTH-015/ACT-027/ENV-015; exact successor revision headers; predecessor archival/root absence; `Framework-Source` unchanged; `git diff --check` PASS.
- **Live UI Result:** USER_CONFIRMED by ACTOR-001 under the explicit instruction to approve only if `[Next Action] → [Next Goal] → [Reason]` were visibly rendered in the immediately preceding safe-footer response.
- **Completion Checkpoint Commit:** `196ddd0d5a2ec7c48c7a9232bafc909b0284522b` (`docs(task047): register footer UI compliance regression`), freshly observed before terminal reconciliation; working tree was clean.
- **Framework Distribution:** no `Framework-Source` semantic/version file changed; existing Framework 1.15 contract is retained as the correct source rule.
- **Resulting Lifecycle Candidate:** `TASK-047 DONE / OUT-015 ACHIEVED / AUTH-015 TERMINATED / ACT-027 DONE / ENV-015 EXPIRED`; final completion claim requires terminal successor commit plus fresh readback.
- **Publication:** NOT_PUSHED / NOT_AUTHORIZED.
