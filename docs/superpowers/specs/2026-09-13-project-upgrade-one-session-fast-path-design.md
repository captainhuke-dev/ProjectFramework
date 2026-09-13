# TASK-052 Project Upgrade One-Session Fast Path — Design

Date: `2026-09-13` (Asia/Bangkok)
Task: `TASK-052`
Design state: `USER_APPROVED_FINAL_DESIGN / WRITTEN_SPEC_SELF_REVIEWED`
Approval basis: ACTOR-001 invoked an explicit Goal to design and implement a Project Upgrade One-Session Fast Path, then explicitly approved Design Sections 1, 2, and 3 in chat.
Goal lifecycle target: `OUT-020 / AUTH-020 / ACT-032 / ENV-020`
Repository: `captainhuke-dev/ProjectFramework`
Execution ancestry: deliberate `STACKED_WORK` on TASK-051 terminal local commit `26fbb3c0ff298b183f23c7dabe5132dc11002185`; parent TASK-051 Framework 1.17 candidate remains verified and unpublished.
Target release: Framework `1.18.0` / Schema `1.0.0` / release format `3`
Release classification: `BACKWARD_COMPATIBLE_UPGRADE_WORKFLOW_ACCELERATION`
Spec self-review: `TASK052_SPEC_SELF_REVIEW 15/15 PASS`

## 1. Purpose

Make normal compatible `[Project Upgrade]` materially faster by converting the existing multi-round prepare/Preview/approval/mutate/verify workflow into a governed one-session transaction where evidence permits, while preserving explicit mutation approval, rollback, Root/Binding safety, state-bound evidence validity, release acceptance, integration freshness, history preservation, and truthful partial-stop boundaries.

The normal success target is:

```text
one [Project Upgrade] invocation
→ one current→target comparison/assessment
→ one exact Preview
→ one explicit Human mutation approval
→ one bounded mutation batch
→ one affected verification phase
→ one completion commit
→ one terminal readback
```

When the exact target Framework candidate already carries valid state-bound `RELEASE_FULL` evidence, the normal eligible upgrade performs **zero redundant `RELEASE_FULL` reruns**.

## 2. Problem

The current Framework already includes Direct-to-Latest upgrade semantics, standardized upgrade Preview, `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`, state-bound evidence reuse, and a narrow FAST_PATH substitution for exact release evidence. However the end-to-end command remains slow because it commonly performs:

```text
compare
→ ask whether to prepare
→ assess
→ Preview
→ ask mutation approval
→ mutate
→ checkpoints/persistence
→ affected verification
→ RELEASE_FULL or confirmation
→ terminal reconciliation
```

For canonical ProjectFramework, verified release integration and self-host reconciliation can also become separate workflows even when one approved transaction could safely cover both.

The result is excessive round-trips and repeated proof rather than insufficient safety semantics.

## 3. Design Goals

The contract MUST:

- remove the redundant “prepare?” round-trip after `UPGRADE_AVAILABLE`;
- preserve exactly one explicit mutation approval bound to an exact Preview/candidate;
- allow compatible `FAST_PATH` and bounded compatible `ASSESSED_PATH` upgrades to complete in one session when prerequisites remain valid;
- keep `MAJOR_MIGRATION_REQUIRED` outside the one-session fast path;
- batch deterministic Project Source successor/archive/routing mutations into one bounded transaction;
- reuse exact upstream Framework release evidence across Project upgrade acceptance where the proof domain is unchanged;
- verify Project-specific resulting state separately from Framework release acceptance;
- keep `INTEGRATION_GATE` distinct and fresh immediately before mutable-target integration/publication;
- reuse valid comparison/assessment/release evidence after interruption instead of restarting from zero;
- chain canonical ProjectFramework integration and self-host reconciliation when one exact Preview and authority covers both;
- stop truthfully at the first unauthorized boundary without treating local completion as failure;
- define measurable verification/round-trip budgets so “Fast Path” is observable behavior rather than a label; and
- add no runtime upgrade engine, bot, daemon, scheduler, validator/CLI, CI/CD mutator, or background reconciler.

## 4. Non-Goals

TASK-052 does NOT:

- make `[Project Upgrade]` mutation-authorizing by invocation alone;
- eliminate Preview or explicit Human mutation approval;
- auto-upgrade initialized Brownfield Projects;
- auto-merge, auto-push, auto-release, auto-tag, or auto-deploy;
- bypass Project Location Binding, Root Governance, secrets, disclosure, destructive, production, or external-action gates;
- redefine `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED` as lifecycle/authority states;
- guarantee one-session completion when target/evidence/authority changes or a real blocker appears;
- treat a Framework release proof as proof of Project-specific migration correctness;
- reuse mismatched or stale candidate/tree evidence;
- make `INTEGRATION_GATE` optional;
- create a second upgrade command, new Stable-ID family, or new Project Source semantic slot; or
- require optional `Project-Execution/` profiles to exist.

## 5. Chosen Architecture

Chosen architecture: **Single-Preview / Single-Approval Upgrade Transaction with proof-domain evidence reuse**.

```text
[Project Upgrade]
→ resolve current local pin + fresh exact target
→ cumulative current→target assessment automatically
→ classify FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED
→ determine one-session eligibility
→ materialize one exact Preview
→ request one explicit mutation approval
→ if approved state remains valid:
     bounded mutation batch
     → Project affected verification
     → completion commit
     → terminal readback
→ optional separately-authorized integration/self-host continuation
```

One-session eligibility is a workflow disposition only. It does not create a lifecycle, Epistemic Status, Risk, authority, migration, or Stable-ID family.

## 6. Rejected Alternatives

### 6.1 Keep the “prepare?” gate and only optimize verification

Rejected because it leaves an unnecessary Human round-trip before a read-only assessment/Preview that can be produced safely without mutation authority.

### 6.2 Auto-approve compatible upgrades

Rejected because compatible does not mean authorized. Root/Project Source mutation remains a Material governance change requiring explicit approval of the exact Preview.

### 6.3 Always rerun `RELEASE_FULL` for ASSESSED_PATH

Rejected because it confuses Framework Release Acceptance with consuming-Project Upgrade Acceptance. Exact unchanged release proof should not be recomputed merely because another Project adopts that already-verified candidate.

### 6.4 Treat canonical self-host reconciliation as a second upgrade

Rejected when the same exact approved transaction and authority covers integration plus post-merge self-host reconciliation. A second invocation/Preview/approval adds ceremony without new information.

## 7. Existing Path Classes Remain Canonical

TASK-052 preserves the existing upgrade classification:

```text
FAST_PATH
ASSESSED_PATH
MAJOR_MIGRATION_REQUIRED
```

These remain upgrade workflow classifications, not authority or lifecycle states.

- `FAST_PATH` — bounded compatible delta with deterministic preservation and rollback.
- `ASSESSED_PATH` — compatible but materially broader/cross-surface migration requiring explicit cumulative assessment.
- `MAJOR_MIGRATION_REQUIRED` — breaking schema/namespace/root semantics, non-reconstructable truth, material unresolved conflicts/unknowns, or another condition preventing bounded compatible migration.

TASK-052 changes execution efficiency, not the meaning of “compatible.”

## 8. One-Session Eligibility

An upgrade is `ONE_SESSION_ELIGIBLE` in working evidence only when all applicable conditions are true:

- current Project identity and active local `FRAMEWORK-001` are resolved;
- exact target Framework release/version/schema/release-format and source/tree identity are resolved;
- path is `FAST_PATH` or bounded compatible `ASSESSED_PATH`;
- affected Project Source/root/bootstrap surfaces are bounded;
- preservation invariants are explicit;
- rollback/revert route is explicit and feasible;
- no unresolved semantic conflict exists;
- Project Location Binding/authority prerequisites required by the approved transaction are resolved;
- exact mutation scope can be represented in one Preview;
- required verification route is available;
- any stricter Project/tool/capability/trust rule is satisfied; and
- uncertainty is low enough to preserve the chosen path.

The disposition MUST NOT be persisted as a new canonical state family.

## 9. Ineligible / Escalation Conditions

One-session execution is not eligible when any material condition includes:

- `MAJOR_MIGRATION_REQUIRED`;
- breaking Schema or semantic-slot/namespace migration;
- unresolved Root/Binding/source identity contradiction;
- non-reconstructable current truth;
- unresolved semantic conflict;
- destructive/irreversible migration without a separately governed path;
- unknown target candidate/tree/evidence;
- rollback that cannot be established for the proposed transaction;
- material scope not represented in the approved Preview; or
- higher-level tool/platform controls that require an external stop.

A previously eligible transaction loses eligibility when a material approved assumption changes.

## 10. Command Flow — Remove the Prepare Round-Trip

`[Project Upgrade]` remains read-only until explicit mutation approval, but `UPGRADE_AVAILABLE` no longer asks whether the Human wants to “prepare” an upgrade before assessment.

The command SHOULD immediately perform all safe read-only work needed to produce the exact Preview:

```text
resolve current local pin
→ fresh-resolve exact upstream target
→ compare current→target
→ read target migration notes/current normative delta
→ cumulative assessment
→ classify upgrade path
→ assess one-session eligibility
→ materialize exact Preview
→ request explicit mutation approval
```

The Human therefore sees one decision point that actually matters: approve or reject the exact proposed mutation transaction.

## 11. Preview as Transaction Contract

The approved Preview binds at least:

- current Project identity and local Framework/Schema pin;
- exact target Framework version/Schema/release format;
- target repository/ref/tree or equivalent exact content identity when available/material;
- path classification;
- one-session eligibility disposition;
- affected Project Source/root/bootstrap surfaces;
- preservation invariants including Project UUID, Stable IDs, Project-specific rules, bindings, current truth, and history;
- rollback/recovery route;
- verification plan and evidence-reuse decision;
- publication/integration scope when requested;
- canonical self-host applicability when the Project is the canonical ProjectFramework repository;
- exact authority being requested; and
- known stop boundaries.

Human approval is state-bound to this Preview/candidate.

## 12. Preview Validity and Re-Approval

A new Preview/approval is required when a material approved assumption changes, including:

- target Framework tree/content identity changes;
- path changes among `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`;
- affected semantic scope expands;
- Schema/namespace compatibility changes;
- a material conflict or binding mismatch appears;
- rollback/recovery premise changes materially;
- required authority scope expands; or
- project-specific migration semantics differ from the approved transaction.

A new Preview is NOT required solely for deterministic execution details already implied by the approved transaction, such as:

- monotonic revision numbers;
- timestamps;
- filenames derived deterministically from approved successor revisions;
- routing/index/manifest references to those exact generated successors; or
- formatting-only normalization that cannot alter meaning.

## 13. One Bounded Mutation Transaction

After approval and a final freshness check, eligible upgrade mutation is executed as one bounded transaction:

```text
freeze approved Preview/candidate
→ materialize all required successors
→ preserve/archive predecessors
→ update exact index/manifest/routing
→ reconcile required root/bootstrap state within approved scope
→ verify final combined Project state
→ one completion commit
→ fresh terminal readback
```

The Framework MUST NOT require a Logical Checkpoint after each document edit merely because multiple governed files participate in the transaction.

A mid-transaction durable checkpoint is required only when real continuation state must survive interruption/handoff, a material blocker appears, a non-idempotent external effect is involved, or the transaction must safely stop before completion.

## 14. Proof-Domain Separation

TASK-052 makes this distinction explicit:

```text
Framework Release Acceptance
≠
Consuming Project Upgrade Acceptance
```

Framework Release Acceptance proves the exact reusable Framework candidate/distribution.

Project Upgrade Acceptance proves that the consuming Project correctly adopted the approved target while preserving Project-specific invariants.

Neither proof substitutes for the other.

## 15. Framework Release Evidence Reuse

When the exact target Framework candidate has committed, state-bound `RELEASE_FULL` evidence and the freshly observed target tree/content identity exactly matches that evidence, an eligible `FAST_PATH` or bounded compatible `ASSESSED_PATH` upgrade MAY reuse that Framework release proof.

The consuming Project then runs only the verification needed for its migration result, including applicable:

- target release identity confirmation;
- affected active Project Source semantics;
- Root successor validity;
- Project UUID/Stable-ID preservation;
- Project-specific rule preservation;
- Project Location Binding preservation;
- Index/Manifest/current routing correctness;
- Bootstrap correctness;
- predecessor/history preservation;
- rollback/recovery truth;
- diff hygiene; and
- direct resulting-state confirmation.

This is not “skipping verification.” It avoids recomputing proof in the wrong domain.

## 16. Evidence Reuse Invalidation

Framework release evidence MUST NOT be reused when:

- observed target tree/content identity differs from the evidence binding;
- the target changed after the evidence was captured;
- evidence is missing, stale, contradictory, incomplete, or unverifiable;
- the upgrade process itself changes the Framework Release Candidate;
- the reused evidence does not cover the actual target release semantics; or
- impact cannot be bounded confidently.

In these cases, run the applicable current verification, with at most one final `RELEASE_FULL` on the exact final unchanged candidate where required.

## 17. Verification Budget

Normal eligible upgrade budget:

```text
Comparison / cumulative assessment   1
Preview                              1
Human mutation approval              1
Mutation batch                       1
Project affected verification        1
Completion commit                    1
Terminal readback                    1
```

`RELEASE_FULL` budget:

- `0` when exact target release evidence is valid and reusable;
- `1` maximum when release evidence cannot be reused and a full candidate verification is actually required;
- never repeated merely because multiple internal phases or checkpoints occurred.

Review budget:

- upgrade classification alone does not create an independent-review requirement;
- apply any review requirement actually triggered by active Project/capability policy, migration complexity, or another binding contract;
- reusable upstream release review/evidence may support release semantics but never fabricates Project-specific review evidence;
- normal flow has no “review of the review.”

## 18. Relationship to TASK-051 Feature Delivery Tiers

`LOW | MEDIUM | HIGH` remains the Feature Delivery classification introduced by TASK-051. `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED` remains the Project Upgrade classification.

Do not collapse these systems into one family.

The implementation work of TASK-052 changes upgrade/release verification semantics and is therefore HIGH under TASK-051 sensitive-surface rules; TASK-052 implementation acceptance requires independent review absent a valid governed waiver.

A consuming Project upgrade does not gain a new Feature Delivery tier merely from invoking `[Project Upgrade]`; its upgrade safety remains governed by the upgrade classification plus all independently applicable Root/authority/review/tool constraints.

## 19. Interruption and Recovery

After interruption of local Git-backed upgrade work:

```text
fresh-read branch/worktree/HEAD/current active routing
→ resolve approved Preview fingerprint/candidate
→ inspect which transaction effects are durable
→ compare evidence bindings
→ reuse still-valid comparison/assessment/release evidence
→ execute only unfinished safe affected operations
→ rerun only invalidated/newly affected verification
```

A chat/tool transport failure alone does not invalidate unchanged Git or release evidence.

Committed correct successors are not recreated merely because the session restarted.

If partial state cannot be reconstructed confidently, fail closed for the affected transaction and require a new Preview/repair path as appropriate.

Unknown possibly-applied non-idempotent/shared/external effects remain `RESULT_VERIFICATION_REQUIRED` before retry.

## 20. Canonical ProjectFramework Self-Host Chaining

For the canonical `captainhuke-dev/ProjectFramework` repository, integration and self-host reconciliation MAY be one governed delivery transaction when the exact Preview and authority already cover both boundaries.

Eligible chained flow:

```text
verified release candidate
→ INTEGRATION_GATE
→ authorized integration/merge
→ fresh-read exact merged canonical result
→ verify merged release identity/tree matches approved transaction
→ immediately reconcile FRAMEWORK-001 successor
→ reconcile applicable active Project Source metadata/routing
→ reconcile PROJECT-BOOTSTRAP
→ affected postflight
→ terminal reconciliation
```

No second `[Project Upgrade]`, Preview, or approval is required when the post-merge result exactly matches the already-approved self-host delta.

## 21. Canonical Self-Host Stop Boundaries

If authority covers integration but not Root/self-host mutation:

```text
integration complete
→ RECONCILIATION_REQUIRED
→ stop safely
```

If authority covers local candidate work but not integration:

```text
local verified candidate complete
→ stop before shared-state integration
```

If the merged result differs materially from the approved Preview, stop and re-Preview the changed self-host delta.

Fast Path never synthesizes missing publication or Root authority.

## 22. INTEGRATION_GATE Remains Mandatory

TASK-052 does not weaken `INTEGRATION_GATE`.

Immediately before applicable mutable-target integration/publication, fresh-resolve:

- Canonical Integration Target;
- Base Freshness;
- candidate identity;
- validity of prior release/review/upgrade evidence; and
- exact shared-state authority.

A prior `RELEASE_FULL`, reusable release proof, or approved Preview is not permanent target freshness evidence.

## 23. Completion Semantics

A Material Git-backed Project upgrade is complete locally only when:

- approved intended resulting state exists;
- Project affected verification passes;
- required review/approval obligations are satisfied;
- resulting Root/Project Source/Bootstrap state is directly confirmed;
- required evidence is persisted;
- completed result is represented in observed durable commit(s);
- working tree is clean or explained; and
- current lifecycle/next-action truth is accurate.

`completion commit ≠ push ≠ merge ≠ release` remains binding.

## 24. Brownfield Safety

Existing initialized Projects never auto-adopt Framework 1.18 or any later release merely because upstream moves.

The One-Session Fast Path executes only after explicit `[Project Upgrade]` invocation and exact mutation approval.

Direct-to-Latest remains cumulative; skipping intermediate execution never skips preservation assessment, rollback, Preview, authority, affected verification, or history preservation.

## 25. No Runtime Expansion

TASK-052 is a Human/Agent governance workflow contract.

It adds no:

- upgrade daemon;
- auto-updater;
- merge/release bot;
- CI/CD mutator;
- scheduler;
- background watcher;
- runtime migration engine;
- validator/CLI;
- MCP upgrade router;
- credential store; or
- persistent service/database.

## 26. Version / Compatibility Classification

Target Framework release: `1.18.0` / Schema `1.0.0` / release format `3`.

Reason for minor release:

- adds additive Project Upgrade workflow behavior;
- does not change Project Source semantic slots;
- does not add a Stable-ID family;
- does not add a Registered Command;
- does not change Schema;
- preserves existing path-class vocabulary;
- preserves explicit mutation approval;
- preserves Root/Binding and publication authority boundaries; and
- preserves Brownfield no-auto-upgrade behavior.

TASK-051 Framework 1.17 release candidate remains historical verified evidence and is not retroactively rewritten; TASK-052 is deliberate stacked work on top of that local lineage.

## 27. Normative Framework Surfaces

Implementation should update the minimum current surfaces needed for a coherent 1.18 contract:

- `Framework-Source/FRAMEWORK-RELEASE.yaml`;
- new TASK-052 current governance amendment;
- `Framework-Source/references/core-governance-rules.md` — `[Project Upgrade]` and canonical self-host reconciliation;
- `Framework-Source/SKILL.md` — command/operational workflow;
- `Framework-Source/MIGRATION-NOTES.md`;
- root `README.md` current release/upgrade guidance;
- `Framework-Source/templates/upgrade-preview.md` if exact transaction-binding fields require clarification;
- applicable maintained current templates/starters carrying Framework version/current upgrade semantics;
- pressure scenarios;
- TASK-052 task/evidence/current-state lifecycle records.

Thin vendor launchers remain unchanged unless they actually contain version-bound or upgrade-contract semantics that must change.

## 28. Pressure Scenario Contract

Fresh inspection proves current scenarios `1–504` are contiguous and unique. TASK-052 allocates exactly `505–528`:

505. `[Project Upgrade]` performs compare + assessment + Preview without a prepare prompt.
506. exact Preview still requires explicit mutation approval.
507. eligible FAST_PATH completes through one bounded mutation batch.
508. bounded compatible ASSESSED_PATH is one-session eligible.
509. MAJOR_MIGRATION_REQUIRED is not one-session eligible.
510. exact valid upstream RELEASE_FULL evidence is reusable for FAST_PATH.
511. exact valid upstream RELEASE_FULL evidence is reusable for bounded ASSESSED_PATH.
512. mismatched target tree blocks release-evidence reuse.
513. post-evidence target mutation invalidates reuse.
514. Project-specific affected verification remains mandatory after release-proof reuse.
515. uninterrupted eligible transaction does not require per-document Logical Checkpoints.
516. interruption reuses unchanged comparison/assessment/release evidence.
517. reconstructable partial local transaction resumes only unfinished work.
518. unknown non-idempotent/shared result becomes RESULT_VERIFICATION_REQUIRED before retry.
519. material Preview delta requires re-Preview and reapproval.
520. deterministic revision/timestamp/routing generation does not require reapproval.
521. canonical integration + self-host reconciliation chains when exact authority covers both.
522. integration-only authority stops at RECONCILIATION_REQUIRED before Root mutation.
523. local-only authority stops before integration without invalidating local completion.
524. INTEGRATION_GATE remains mandatory immediately before mutable-target action.
525. upgrade completion still requires observed durable completion commit.
526. Brownfield Project never auto-adopts newer Framework.
527. contract adds no runtime upgrade automation.
528. normal verification budget forbids repeated RELEASE_FULL runs without evidence invalidation.

## 29. TASK-052 Implementation Verification Strategy

TASK-052 itself modifies `[Project Upgrade]`, release-evidence reuse, and self-host integration semantics. It is HIGH under Framework 1.17 sensitive-surface rules.

Implementation therefore requires:

1. TDD RED scenarios `505–528` before production Framework changes;
2. focused structural checks during normative and propagation phases;
3. independent review of the stable implementation candidate;
4. cumulative AFFECTED verification covering command flow, approval boundary, evidence reuse/invalidation, ASSESSED_PATH eligibility, transaction batching, recovery, self-host chaining/stops, Brownfield safety, starter/version consistency, historical preservation, and no-runtime scope;
5. freeze one exact Framework 1.18 candidate;
6. one final current-distribution `RELEASE_FULL` on that TASK-052 release candidate because TASK-052 itself creates a new Framework release candidate;
7. state-bound durable release evidence;
8. terminal local Task/Goal reconciliation; and
9. fresh completion-commit + clean-tree readback before external completion claim.

This implementation-time `RELEASE_FULL` does not contradict the new consuming-upgrade evidence-reuse rule: TASK-052 is producing Framework 1.18, not consuming an already verified Framework release.

## 30. Goal / Publication Boundary

The current TASK-052 Goal authorizes bounded local design, specification, implementation planning, Framework documentation/governance implementation, pressure scenarios/tests, review, verification, evidence, local commits, and Project Source lifecycle updates through verified local completion.

It does NOT by itself authorize:

- push;
- PR creation/update as a Material shared-state delivery action;
- merge to canonical `main`;
- tag/GitHub Release;
- actual canonical self-host Root promotion to 1.18;
- Project Location Binding mutation;
- destructive branch/worktree cleanup;
- external AI/provider disclosure;
- secret-value persistence; or
- runtime automation.

The design defines how a future authorized chained self-host transaction behaves; it does not execute that future Root/shared-state action under the present Goal.

## 31. Completion Criteria

TASK-052 design/implementation is acceptable when all are true:

1. `[Project Upgrade]` automatically performs read-only assessment + exact Preview without a prepare round-trip;
2. one explicit mutation approval remains mandatory;
3. one-session eligibility includes FAST_PATH and bounded compatible ASSESSED_PATH but excludes MAJOR;
4. approved Preview is a state-bound transaction contract;
5. material Preview changes require reapproval while deterministic generated metadata does not;
6. eligible mutation is one bounded batch rather than one checkpoint per document;
7. Framework Release Acceptance and Project Upgrade Acceptance are explicitly distinct proof domains;
8. exact valid release evidence is reusable for both FAST_PATH and bounded ASSESSED_PATH;
9. target/evidence mismatch invalidates reuse;
10. Project affected verification remains mandatory;
11. normal release-full budget is zero with reusable evidence and at most one when genuinely required;
12. interruption selectively reuses still-valid evidence and reconstructable durable state;
13. unknown external/shared result verifies before retry;
14. canonical integration and self-host reconciliation can chain under one exact Preview/authority;
15. missing Root authority stops at RECONCILIATION_REQUIRED rather than silently expanding scope;
16. local-only authority stops successfully before integration;
17. INTEGRATION_GATE remains distinct and mandatory where applicable;
18. Material Git-backed completion still requires observed durable commit;
19. Brownfield Projects never auto-upgrade;
20. Framework 1.18 remains Schema 1.0.0 / release format 3;
21. scenarios 505–528 cover the new contract;
22. TASK-052 implementation receives independent review because this implementation changes sensitive verification/upgrade semantics;
23. AFFECTED + one final Framework 1.18 RELEASE_FULL pass on the unchanged implementation candidate;
24. terminal TASK-052/OUT-020 state is committed and freshly observed locally; and
25. no unauthorized publication, Root/Binding mutation, runtime automation, external disclosure, or secret persistence occurs.

## 32. Written Spec Self-Review Checklist

Before implementation planning, the written spec must pass:

- no unresolved placeholder or design choice;
- no removal of explicit mutation approval;
- no implicit auto-upgrade;
- no confusion between release proof and Project upgrade proof;
- no unconditional release-evidence reuse;
- no ASSESSED_PATH widening into MAJOR semantics;
- no bypass of Project affected verification;
- no bypass of INTEGRATION_GATE;
- no hidden publication or Root authority;
- no second lifecycle/Stable-ID family for one-session eligibility;
- no contradiction between transaction batching and interruption durability;
- no contradiction between canonical self-host chaining and authority boundaries;
- no runtime/daemon/CI/CD/validator expansion;
- scenario range is collision-free; and
- implementation scope is bounded to one coherent Framework release plan.
