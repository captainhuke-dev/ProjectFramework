---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-MANAGEMENT-CONTROL-001"
document_type: "PROJECT_MANAGEMENT_CONTROL"
semantic_slot: "91"
revision: 55
document_status: "ACTIVE"
supersedes: "91-Project-Management-Control-r054-260912-2344.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-31T20:44:00+07:00"
updated_at: "2026-09-12T23:54:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "CHANGEABLE"
project_source_framework_version: "1.16.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
# 91 — Project Management Control

Historical `OUT-001` through `OUT-013` remain preserved in archive/Git history. Current outcome truth is below.

## OUT-014 — Publish Framework 1.15 and upgrade ProjectFramework to Framework 1.15

- **Status:** ACHIEVED.
- **Outcome Statement:** make verified Framework 1.15 canonical, then upgrade this initialized ProjectFramework Project Source from Framework pin 1.7.0 to 1.15.0 through governed Direct-to-Latest.
- **Success Criteria Evaluation:** VERIFIED — publication baseline/evidence confirmed; canonical Framework 1.15 present; comparison/Preview completed; separate post-Preview Root mutation approval captured; Brownfield Project Source/root bootstrap promoted with identity/bindings/history preserved; ASSESSED_PATH verification passed; promoted commit `015f76df0ee667f45e4712bcefa0d5bc4d9bbd05` freshly observed on canonical `main`; terminal persistence reconciled; prohibited effects absent.
- **Terminal Upgrade Commit:** `015f76df0ee667f45e4712bcefa0d5bc4d9bbd05` / tree `aedaf7b2b6b8fc5feda7cdd5551c441733cb8615`.
- **Verification:** `UPGRADE_AFFECTED PASS`; `UPGRADE_RELEASE_FULL PASS_RUN_1`; `EVD-087`; canonical readback/persistence `EVD-088`.
- **Related AUTH / ACT / ENV:** `AUTH-014 TERMINATED` / `ACT-026 DONE` / `ENV-014 EXPIRED`.
- **Migration / Changes:** `MIG-002 COMPLETED`; `CHG-087`; `CHG-088`.
- **Prohibited Zones Preserved:** force/history rewrite; destructive branch/worktree deletion; Project Location Binding mutation; MCP/Git-native architecture migration; AI-ControlTower/V2 cutover; external disclosure; secret values; unrelated Tasks; runtime implementation.
- **Remaining Work:** none for OUT-014.

`ACT DONE ≠ OUT ACHIEVED` remains a general invariant; OUT-014 is ACHIEVED because all declared criteria above are independently evidenced.

## OUT-015 — Close TASK-047 footer rendering/compliance regression with visible UI acceptance

- **Status:** ACHIEVED.
- **Outcome Statement:** register and close the newly observed response-close compliance regression by proving the existing Framework 1.15 Markdown-safe contract is correct and that `[Next Action] → [Next Goal] → [Reason]` is visibly rendered in the ChatGPT UI when followed.
- **Success Criteria Evaluation:** VERIFIED — TASK-047 registered; current SKILL retains Markdown-safe three-field order; Scenario 432 retains hidden-label failure; live ChatGPT UI visibility is USER_CONFIRMED; no Framework semantic/version change occurred; `TASK047_GREEN PASS` and `git diff --check` passed; local completion checkpoint commit `196ddd0d5a2ec7c48c7a9232bafc909b0284522b` was freshly observed; terminal successor set is prepared for durable commit/readback.
- **Verification:** `EVD-090` / `EVD-091`; completion checkpoint commit `196ddd0d5a2ec7c48c7a9232bafc909b0284522b`.
- **Related AUTH / ACT / ENV:** `AUTH-015 TERMINATED` / `ACT-027 DONE` / `ENV-015 EXPIRED`.
- **Prohibited Zones:** push/publication; destructive history operations; Project Location Binding/Root mutation; Framework semantic/version change; runtime/UI-hook/parser/validator implementation; external disclosure; secrets; unrelated work.
- **Remaining Work:** none for OUT-015.
## OUT-016 — Reconcile TASK-047 publication state with canonical remote

- **Status:** ACHIEVED.
- **Outcome Statement:** make TASK-047 publication/current-truth records match the already-published implementation and finish with Project Source, local `main`, and `origin/main` aligned.
- **Success Criteria Evaluation:** VERIFIED when this active record is read from canonical `origin/main` after non-force publication: TASK-047 remains DONE; implementation commits `196ddd0d5a2ec7c48c7a9232bafc909b0284522b` and `bc880c75190f967a3b87c2842b8cc284f8a3bcab` are remote; stale `NOT_PUSHED` metadata is removed; active routing/history are valid; Framework-Source is unchanged; reconciliation commit is on both local/remote main; divergence is zero; working tree is clean.
- **Verification:** `EVD-092 / CHG-092`.
- **Related AUTH / ACT / ENV:** `AUTH-016 TERMINATED` / `ACT-028 DONE` / `ENV-016 EXPIRED`.
- **Prohibited Zones Preserved:** force/history rewrite; destructive branch/worktree deletion; Root/Binding mutation; Framework semantic/version change; runtime implementation; external disclosure; secrets; unrelated work.
- **Remaining Work:** none when canonical remote readback resolves this active terminal record.

## OUT-017 — Canonical ProjectFramework self-hosting reconciliation to Framework 1.16.0

- **Status:** BLOCKED / AWAITING_INTEGRATION_AUTHORITY.
- **Outcome Statement:** make canonical ProjectFramework self-host the verified Framework 1.16.0 release in Framework-Source, active Project Source, and PROJECT-BOOTSTRAP.md, and make future verified release merges require the same governed self-host reconciliation without a redundant `[Project Upgrade]`.
- **Local Success Criteria Evaluation:** VERIFIED — canonical self-host rule implemented; consuming-Project pin preserved; local Root/active Project Source/Bootstrap all 1.16.0; UUID/binding/history preserved; `RECONCILIATION_REQUIRED` fail-closed rule present; no runtime automation; AFFECTED `25/25`; final state-bound `23/23 PASS_RUN_1`; candidate `759c7dd29c060888b3ef9c4424cdcb17cd809eed`.
- **Unsatisfied Goal Criterion:** canonical `main` has not yet adopted the branch because `AUTH-017` explicitly excluded push/PR/merge/publication.
- **Related AUTH / ACT / ENV:** `AUTH-017 TERMINATED` / `ACT-029 DONE` / `ENV-017 EXPIRED`.
- **Evidence / Change:** `EVD-093 / EVD-094 / EVD-095` and `CHG-093 / CHG-094 / CHG-095`; durable evidence `docs/superpowers/evidence/2026-09-12-task-049-canonical-self-hosting-release-full.md`.
- **Prohibited Zones Preserved:** no push/PR/merge/tag under terminated AUTH-017; no binding mutation; no destructive history; no runtime automation; no external disclosure/secrets.
- **Remaining Work:** one separately authorized canonical-main integration path plus fresh resulting-state readback; no implementation work remains.
