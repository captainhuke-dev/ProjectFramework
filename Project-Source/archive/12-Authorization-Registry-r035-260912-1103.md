---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "AUTHORIZATION-REGISTRY-001"
document_type: "AUTHORIZATION_REGISTRY"
semantic_slot: "12"
revision: 35
document_status: "ACTIVE"
supersedes: "12-Authorization-Registry-r034-260912-0026.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-12T11:03:41+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "USER_CONFIRMED"
freshness_class: "STABLE"
project_source_framework_version: "1.15.0"
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
