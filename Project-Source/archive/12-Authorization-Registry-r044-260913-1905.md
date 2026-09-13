---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "AUTHORIZATION-REGISTRY-001"
document_type: "AUTHORIZATION_REGISTRY"
semantic_slot: "12"
revision: 44
document_status: "ACTIVE"
supersedes: "12-Authorization-Registry-r043-260913-1724.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-13T19:05:56.966+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "USER_CONFIRMED"
freshness_class: "STABLE"
project_source_framework_version: "1.16.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
# 12 — Authorization Registry

Historical AUTH records through `AUTH-013` remain preserved in archive/Git history. Current terminal authority truth is below.

## AUTH-014 — Framework 1.15 publication and Project upgrade authority

- **Authority Type:** USER_EXPLICIT_PERSISTENT_GOAL_AUTHORIZATION + USER_EXPLICIT_POST_PREVIEW_ROOT_MUTATION_APPROVAL
- **Granted By:** ACTOR-001
- **Initial Goal Authority Granted At:** 2026-09-10T22:20:10+07:00
- **Post-Preview Mutation Approval:** 2026-09-11T14:59:00+07:00
- **Parent Outcome:** `OUT-014`
- **Authorized Scope Completed:** canonical Framework 1.15 publication reconciliation; Direct-to-Latest comparison/Preview; approved `ASSESSED_PATH` Root/Project Source promotion; successor/archive/bootstrap reconciliation; verification and terminal persistence.
- **Explicitly Excluded:** force/history rewrite; destructive branch/worktree deletion; Project Location Binding mutation; MCP/Git-native execution-architecture migration; AI-ControlTower/V2 cutover; external disclosure; secret values; unrelated Tasks; runtime/CLI/CI-CD implementation.
- **Observed Upgrade Commit:** `015f76df0ee667f45e4712bcefa0d5bc4d9bbd05` on canonical `main`.
- **Verification:** `EVD-087`; post-promotion observation/persistence `EVD-088`.
- **Status:** TERMINATED.
- **Validity:** no future operation may rely on `AUTH-014`; historical completed effects/evidence remain preserved.
- **Authority Transfer:** false.

No `DEL-*` record is created.

## AUTH-015 — TASK-047 footer rendering/compliance Goal authority

- **Authority Type:** USER_EXPLICIT_PERSISTENT_GOAL_AUTHORIZATION.
- **Granted By:** ACTOR-001 through `[Goal] ลงและปิด Task สำหรับ footer rendering/compliance regression ให้ยืนยันว่า [Next Action] → [Next Goal] → [Reason] แสดงครบใน UI`.
- **Design Approval:** ACTOR-001 replied `อนุมัติ` after the bounded design and live-UI confirmation condition were presented.
- **Parent Outcome:** `OUT-015`.
- **Authorized Scope Completed:** registered and closed TASK-047; inspected current response-close governance; reproduced/classified the regression; verified existing Scenario 432 and Markdown-safe contract; captured USER_CONFIRMED live ChatGPT UI acceptance; updated Project Task/Project Source lifecycle/evidence; completed bounded verification and local commits.
- **Explicitly Excluded:** push/publication; destructive history rewrite; branch/worktree deletion; Project Location Binding or Root Governance mutation; Framework semantic/version change; runtime/parser/validator/CLI/CI-CD implementation; external disclosure; secret values; unrelated Tasks.
- **Status:** TERMINATED.
- **Verification:** `EVD-090` / `EVD-091`; completion checkpoint commit `196ddd0d5a2ec7c48c7a9232bafc909b0284522b`.
- **Validity:** no future operation may rely on `AUTH-015`; completed effects/evidence remain preserved.
- **Authority Transfer:** false.
## AUTH-016 — TASK-047 publication reconciliation authority

- **Authority Type:** USER_EXPLICIT_PERSISTENT_GOAL_AUTHORIZATION_WITH_PUBLICATION.
- **Granted By:** ACTOR-001 through `[Goal] ปิด TASK-047 ให้ครบถึง publication reconciliation โดยทำให้ Project Source, local main และ origin/main ตรงกันทั้งหมด`.
- **Parent Outcome:** `OUT-016`.
- **Authorized Scope Completed:** fresh-observe local/remote TASK-047 publication; reconcile Task/Project Source publication metadata; create successor/archive state; local commit; non-force push reconciliation to governed target `origin/main`; fresh remote readback and terminal persistence verification.
- **Governed Publication Target:** `origin/main` of `https://github.com/captainhuke-dev/ProjectFramework.git`.
- **Explicitly Excluded:** force push/history rewrite; destructive branch/worktree deletion; Root/Project Location Binding mutation; Framework semantic/version changes; runtime/parser/validator/CLI/CI-CD implementation; external disclosure; secret values; unrelated Tasks.
- **Status:** TERMINATED.
- **Verification:** `EVD-092`; canonical readback of this active authority record from `origin/main` establishes completed publication reconciliation.
- **Validity:** no future operation may rely on `AUTH-016`; completed effects/evidence remain preserved.
- **Authority Transfer:** false.

## AUTH-017 — Canonical self-hosting reconciliation authority

- **Authority Type:** USER_EXPLICIT_PERSISTENT_GOAL_AUTHORIZATION + USER_EXPLICIT_ROOT_GOVERNANCE_MUTATION_APPROVAL.
- **Granted By:** ACTOR-001 through the explicit `[Goal]` for ProjectFramework self-hosting reconciliation and subsequent bounded-design approval.
- **Parent Outcome:** `OUT-017`.
- **Authorized Scope Completed:** bounded Framework governance edits; TDD scenarios; exact `FRAMEWORK-001` successor/promotion 1.15.0 → 1.16.0; active Project Source/bootstrap reconciliation; verification/evidence; local commits.
- **Explicitly Excluded:** push/PR/merge/GitHub Release/tag publication; force/history rewrite; destructive branch/worktree deletion; Project Location Binding mutation; bot/daemon/CI/CD/hook/runtime auto-updater; external disclosure; secret values; unrelated work.
- **Status:** TERMINATED.
- **Verification:** `EVD-095`; candidate `759c7dd29c060888b3ef9c4424cdcb17cd809eed`; AFFECTED `25/25 PASS`; final state-bound `23/23 PASS_RUN_1`.
- **Validity:** no future integration/publication operation may rely on `AUTH-017`; a new explicit instruction/authority is required.
- **Authority Transfer:** false.

## AUTH-018 — GitHub issue backlog reconciliation Goal authority

- **Authority Type:** USER_EXPLICIT_PERSISTENT_GOAL_AUTHORIZATION.
- **Granted By:** ACTOR-001 through the exact `[Goal]` auditing GitHub Issues #25/#29 against current Framework state and reconciling Issue tracker with TASK ledger.
- **Parent Outcome:** `OUT-018`.
- **Authorized Scope Completed:** read canonical GitHub issues/current Framework/Task truth; reconcile TASK-049 integration metadata from fresh remote facts; create/execute TASK-050 audit lifecycle; register TASK-051 TODO for genuine Issue #29; comment and close Issue #25; comment Issue #29 with TASK-051 mapping while keeping it open; update bounded Project Source/task/evidence records; local commits and verification.
- **Explicitly Excluded / Preserved:** TASK-051 implementation; Framework semantic/version changes; Root/Project Location Binding mutation; push/PR/merge/tag/GitHub Release; force/history rewrite; destructive branch/worktree deletion; runtime/daemon/CI/CD; external disclosure beyond the two public issue reconciliation comments; secret values; unrelated work.
- **Status:** TERMINATED.
- **Verification:** `EVD-096 / EVD-097`; tracker readback proves #25 CLOSED and #29 OPEN/mapped.
- **Validity:** no future operation may rely on `AUTH-018`; TASK-051 requires a future explicit Goal/authority.
- **Authority Transfer:** false.

## AUTH-019 - TASK-051 Feature Delivery Fast Path Goal authority

- **Authority Type:** USER_EXPLICIT_PERSISTENT_GOAL_AUTHORIZATION.
- **Granted By:** ACTOR-001 through the TASK-051 Goal, followed by explicit selection of recommended architecture choices and a direction to continue through completion.
- **Parent Outcome:** `OUT-019`.
- **Authorized Scope:** read/research current Framework and Issue #29; architectural design and written spec; implementation planning; bounded local Framework documentation/governance edits for the approved TASK-051 contract; pressure scenarios/TDD; affected and final release-candidate verification; evidence/Task/Project Source lifecycle updates; isolated local branch/worktree management; local commits and logical checkpoints through verified local TASK-051 completion.
- **Risk Ceiling:** `R1 REVERSIBLE_LOCAL` for authorized mutations. Existing R2/R3/shared/external/destructive/Root/Binding/disclosure gates remain independent and are not granted by this authority.
- **Explicitly Excluded:** push/PR/merge/tag/GitHub Release; force/history rewrite; destructive branch/worktree deletion; Project Location Binding mutation; Root Governance self-host promotion; external AI/provider disclosure; secret values; application runtime/daemon/router/watcher/CI/CD/validator/CLI implementation; unrelated Tasks/issues.
- **Design Approval Basis:** ACTOR-001 chose Derived Delivery Tier option A, authority-gated Continuous Delivery option B, conditional MEDIUM review option B, tier + acceptance-boundary verification option B, then instructed the Agent to choose all remaining recommended design options and finish the Goal.
- **Status:** TERMINATED.
- **Validity:** terminated after verified local TASK-051 completion; no future operation may rely on AUTH-019.
- **Authority Transfer:** false.
## AUTH-020 - TASK-052 Project Upgrade One-Session Fast Path Goal authority

- **Authority Type:** USER_EXPLICIT_PERSISTENT_GOAL_AUTHORIZATION.
- **Granted By:** ACTOR-001 through explicit [Goal], followed by explicit approval of Design Sections 1, 2, and 3.
- **Parent Outcome:** `OUT-020`.
- **Authorized Scope:** read/research current upgrade governance; written architectural spec; after required spec review, implementation planning; bounded local Framework documentation/governance edits for the approved TASK-052 contract; pressure scenarios/TDD; independent review; affected/final release-candidate verification; evidence/Task/Project Source lifecycle updates; local commits/checkpoints through verified local completion.
- **Risk Ceiling:** `R1 REVERSIBLE_LOCAL` for present authorized mutations. Existing R2/R3/shared/external/destructive/Root/Binding/disclosure gates remain independent and are not granted.
- **Explicitly Excluded:** push/PR/merge/tag/GitHub Release; actual canonical self-host Root promotion; Project Location Binding mutation; force/history rewrite; destructive branch/worktree cleanup; external AI/provider disclosure; secret values; runtime/daemon/auto-updater/router/watcher/CI-CD/validator-CLI implementation; unrelated work.
- **Higher-Level Process Gate:** SATISFIED - written-spec approval, implementation planning, independent review, AFFECTED, and RELEASE_FULL completed.
- **Status:** TERMINATED.
- **Validity:** terminated after verified local TASK-052 completion; no future operation may rely on AUTH-020.
- **Authority Transfer:** false.


No `DEL-*` record is created.
