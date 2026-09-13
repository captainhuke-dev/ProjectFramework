---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "AUTHORIZATION-REGISTRY-001"
document_type: "AUTHORIZATION_REGISTRY"
semantic_slot: "12"
revision: 39
document_status: "ACTIVE"
supersedes: "12-Authorization-Registry-r038-260912-2354.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-13T08:35:00+07:00"
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
- **Authorized Scope:** read canonical GitHub issues/current Framework/Task truth; reconcile TASK-049 integration metadata from freshly observed remote facts; create TASK-050 audit lifecycle; register TASK-051 TODO for genuine pending Issue #29; comment/close Issue #25 if supported by audit evidence; comment Issue #29 with TASK-051 mapping while keeping it open; update bounded Project Source/task/evidence records; local commits and verification.
- **Explicitly Excluded:** implementing TASK-051; Framework semantic/version changes; Root/Project Location Binding mutation; push/PR/merge/tag/GitHub Release; force/history rewrite; destructive branch/worktree deletion; runtime/daemon/CI/CD; external disclosure beyond the two public GitHub issue reconciliation comments; secret values; unrelated work.
- **Status:** ACTIVE.
- **Verification Basis:** `EVD-096`; terminal issue-state readback required before termination.
- **Authority Transfer:** false.
