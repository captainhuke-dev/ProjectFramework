---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "PROJECT-MANAGEMENT-CONTROL-001"
document_type: "PROJECT_MANAGEMENT_CONTROL"
semantic_slot: "91"
revision: 67
document_status: "ACTIVE"
supersedes: "91-Project-Management-Control-r066-260916-1332.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-31T20:44:00+07:00"
updated_at: "2026-09-16T14:15:47.931+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "CHANGEABLE"
project_source_framework_version: "1.19.0"
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
- **Related AUTH / ACT / ENV:** `AUTH-019 TERMINATED` / `ACT-031 DONE` / `ENV-019 EXPIRED`.
- **Migration / Changes:** `MIG-002 COMPLETED`; `CHG-087`; `CHG-088`.
- **Prohibited Zones Preserved:** force/history rewrite; destructive branch/worktree deletion; Project Location Binding mutation; MCP/Git-native architecture migration; AI-ControlTower/V2 cutover; external disclosure; secret values; unrelated Tasks; runtime implementation.
- **Evidence / Change:** `EVD-101 / EVD-102 / CHG-101 / CHG-102`.
- **Remaining Work:** none for local OUT-019. Issue #29/publication/self-host promotion remain separately governed.

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

- **Status:** ACHIEVED.
- **Outcome Statement:** make canonical ProjectFramework self-host the verified Framework 1.16.0 release in Framework-Source, active Project Source, and PROJECT-BOOTSTRAP.md, and make future verified release merges require the same governed self-host reconciliation without a redundant `[Project Upgrade]`.
- **Success Criteria Evaluation:** VERIFIED — local self-host candidate passed AFFECTED `25/25` and state-bound `23/23 PASS_RUN_1`; PR #31 was subsequently merged and fresh remote observation proves canonical `origin/main = 4039be4` contains the TASK-049 branch and 1.16 self-host state.
- **Canonical Integration:** `PR #31 / merge 4039be4 / MERGED_TO_MAIN / PERSISTED`; GitHub Release/tag remains separate and not required for OUT-017.
- **Related AUTH / ACT / ENV:** historical `AUTH-017 TERMINATED` / `ACT-029 DONE` / `ENV-017 EXPIRED`; later user integration instruction supplied the separate merge authority and canonical result is now observed.
- **Evidence / Change:** `EVD-093 / EVD-094 / EVD-095`; current canonical readback incorporated in `EVD-096 / CHG-096`.
- **Remaining Work:** none for OUT-017.

## OUT-018 — Reconcile GitHub Issue tracker with Framework TASK backlog

- **Status:** ACHIEVED.
- **Outcome Statement:** audit GitHub Issues #25 and #29 against canonical Framework/current Task truth and leave GitHub Issue lifecycle plus Project Task backlog mutually consistent without silently implementing proposed feature work.
- **Success Criteria Evaluation:** VERIFIED — #25 was closed with evidence-backed resolved/superseded rationale and one comment; #29 remains open with one explicit TASK-051 mapping comment; remaining-work counts are exactly TODO=1 / IN_PROGRESS=0 / BLOCKED=0; stale TASK-049 canonical integration metadata is corrected from fresh remote evidence; TASK-051 implementation did not start; terminal tracker readback is recorded in EVD-097.
- **Tracker State:** Issue #25 `CLOSED / comments=1 / closed_at 2026-09-13T03:30:48Z`; Issue #29 `OPEN / comments=1 / TASK-051 mapping`.
- **Related AUTH / ACT / ENV:** `AUTH-018 TERMINATED` / `ACT-030 DONE` / `ENV-018 EXPIRED`.
- **Evidence / Change:** `EVD-096 / EVD-097 / CHG-096 / CHG-097`.
- **Remaining Work:** none for OUT-018. TASK-051 is a separate TODO requiring a future explicit Goal before design/implementation.

## OUT-019 - Deliver TASK-051 Risk-Tiered Feature Delivery Fast Path to verified local completion

- **Status:** ACHIEVED.
- **Outcome Statement:** design and implement a governed risk-tiered Feature Delivery Fast Path that materially shortens genuinely low-risk feature cycle time while preserving canonical Risk/Authority/Location, Task DONE durability, release acceptance, integration freshness, security-sensitive approvals, and evidence integrity.
- **Success Criteria:** (1) user-approved architecture is captured in a written spec; (2) implementation plan is complete; (3) Framework adds deterministic Derived Delivery Tier `LOW | MEDIUM | HIGH` without replacing `R0-R3`; (4) per-tier preflight/review/verification/parallelism/recovery and one-session semantics are normative; (5) direct Git/GitHub repository operations are governed without making MCP a false runtime prerequisite; (6) Preview/explicit approval and sensitive/high-risk gates remain preserved; (7) TDD/affected verification passes; (8) one final `RELEASE_FULL` passes on the unchanged Framework 1.17.0 candidate; (9) Task/Goal evidence is committed and freshly observed locally; (10) prohibited publication/Root/Binding/runtime effects are absent.
- **Success Criteria Evaluation:** VERIFIED - approved design/spec and plan complete; Derived Delivery Tier contract implemented; review e289f236-6dee-46fa-83b6-d0335fea12a5 REVIEW_PASS; AFFECTED 48/48 PASS; RELEASE_FULL 49/49 PASS_RUN_1 on candidate 008fc934a84d595d163a4bc25d974fcd35bac335 / Framework-Source tree 5a6a711861bbbc1e6f9315361921e28625cce854; local-only boundaries preserved.
- **Related AUTH / ACT / ENV:** `AUTH-019 TERMINATED` / `ACT-031 DONE` / `ENV-019 EXPIRED`.
- **Target Release:** Framework `1.17.0` / Schema `1.0.0` / release format `3`.
- **Publication Boundary:** local verified completion only under current authority; canonical integration/publication requires separate authority.
- **Remaining Work:** none for OUT-019 local completion; publication remains separately governed.
## OUT-020 - Deliver Project Upgrade One-Session Fast Path to verified local completion

- **Status:** ACHIEVED.
- **Outcome Statement:** make compatible Project Upgrade materially faster by using one automatic read-only assessment/Preview, one explicit mutation approval, one bounded mutation transaction, proof-domain evidence reuse, one affected verification phase, and canonical self-host chaining when exact authority covers it.
- **Success Criteria:** approved written design/spec; implementation plan; one-session FAST_PATH + bounded compatible ASSESSED_PATH contract; MAJOR exclusion; exact release-evidence reuse with invalidation rules; Project-specific affected verification; interruption recovery; canonical self-host chaining/stops; scenarios 505-528; independent review; AFFECTED + one final 1.18 RELEASE_FULL; terminal local evidence/commit; no unauthorized publication/Root/Binding/runtime effects.
- **Success Criteria Evaluation:** VERIFIED - user-approved spec self-review 15/15; plan self-review 16/16; Framework 1.18 contract/starter propagation complete; independent review 15/15 PASS with Critical/Important/Minor 0/0/0; AFFECTED 43/43 PASS; RELEASE_FULL 44/44 PASS_RUN_1 on frozen candidate 48212bb4f4b577af482afcf5758424eee2f7e036 / Framework-Source tree 929065ccac7e3ecf25fda09de5326bb40c4f8f9c; local-only boundaries preserved.
- **Related AUTH / ACT / ENV:** `AUTH-020 TERMINATED` / `ACT-032 DONE` / `ENV-020 EXPIRED`.
- **Target Release:** Framework `1.18.0` / Schema `1.0.0` / release format `3`.
- **Stacked Work Parent:** TASK-051 / commit `26fbb3c0ff298b183f23c7dabe5132dc11002185`.
- **Publication Boundary:** local verified completion only; shared publication and actual canonical self-host promotion require separate exact authority.
- **Remaining Work:** none for OUT-020 local completion; publication remains separately governed.

## OUT-021 - Complete PR #32 post-merge canonical self-host reconciliation to Framework 1.18.0

- **Status:** ACHIEVED.
- **Outcome Statement:** make canonical ProjectFramework converge to the already-merged Framework 1.18.0 release across active Root, all active Project Source, and PROJECT-BOOTSTRAP; persist PR32/reconciliation evidence and close Issue #29.
- **Success Criteria:** PR32 merge/tree freshly verified; Root/Bootstrap/all active Project Source coherently 1.18; UUID/Stable IDs/bindings/history preserved; MIG-004/evidence persisted; affected verification + required independent review pass; reconciliation integrated to canonical main; Issue #29 CLOSED by observed GitHub state; final main/worktree readback consistent.
- **Success Criteria Evaluation:** VERIFIED — PR32 release merge `f6330e9929c28977d43fc149b864d590df1c2816`; exact Framework-Source tree `929065ccac7e3ecf25fda09de5326bb40c4f8f9c`; Framework 1.18 Root/Bootstrap/all active Project Source merged; `TASK055_AFFECTED 163/163 PASS`; independent HIGH review `12/12 PASS / 0/0/0 / REVIEW_PASS`; candidate `70ef176be0f07e9ce82aeeceb90b864bc28d8ea2`; PR33 merge `5b067a1c2fcfeab867ba3879a76f675904566e27`; Issue #29 `CLOSED` at `2026-09-13T15:47:48Z`; prohibited effects absent.
- **Canonical Integration:** PR #33 / merge `5b067a1c2fcfeab867ba3879a76f675904566e27` / MERGED_TO_MAIN / ISSUE_29_CLOSED.
- **Related AUTH / ACT / ENV:** `AUTH-021 TERMINATED` / `ACT-033 DONE` / `ENV-021 EXPIRED`.
- **Target:** canonical `captainhuke-dev/ProjectFramework` `main`, Framework `1.18.0` / Schema `1.0.0`.
- **Terminal Evidence:** `EVD-107 / CHG-107`.
- **Remaining Work:** none for OUT-021. Tag/GitHub Release remain separately governed and are not required for this outcome.
