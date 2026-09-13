# Framework Governance Amendment — TASK-052 Project Upgrade One-Session Fast Path

Date: `2026-09-13`
Framework: `1.18.0`
Schema: `1.0.0`
Release format: `3`
Source Task: `TASK-052`

## 1. Scope

Framework `1.18.0` adds a **Project Upgrade One-Session Fast Path** for compatible initialized-Project upgrades. It is an additive workflow change: no Project Source semantic slot, Stable-ID family, Registered Command, Schema family, or release-descriptor format changes.

The chosen architecture is **Single-Preview / Single-Approval Upgrade Transaction**. `[Project Upgrade]` remains read-only through exact Preview and never grants mutation, publication, Root, Binding, destructive, production, disclosure, or secret authority by invocation alone.

## 2. One read-only command pass

When a fresh exact target differs from the active local pin, `[Project Upgrade]` performs the safe read-only work needed to reach one real Human decision point:

```text
fresh current + target resolution
→ cumulative current→target assessment
→ FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED
→ one-session eligibility assessment
→ exact state-bound Preview
→ request one explicit mutation approval
```

The prior separate “prepare?” round-trip is removed. Preview generation remains read-only; Material mutation begins only after explicit mutation approval bound to the exact Preview/candidate.

`ONE_SESSION_ELIGIBLE` is working vocabulary only. It is not lifecycle, Risk, authority, Epistemic Status, migration status, or a Stable-ID family.

## 3. Eligibility

`FAST_PATH` and bounded compatible `ASSESSED_PATH` MAY use one-session execution when exact target identity, affected surfaces, preservation invariants, rollback, authority, and verification route are bounded and no unresolved material conflict remains.

`MAJOR_MIGRATION_REQUIRED` is never one-session eligible.

## 4. Preview as transaction contract

The exact Preview binds current Project/pin, target release and tree/content identity, path classification, one-session eligibility, affected Root/Project Source/Bootstrap surfaces, preservation invariants, rollback/recovery, Framework release-evidence reuse decision, Project verification plan, integration/publication scope, canonical self-host applicability, exact authority requested, and known stop boundaries.

Material change to candidate/tree, path classification, semantic scope, compatibility, binding assumptions, rollback, or required authority invalidates the affected Preview approval and requires re-Preview/reapproval.

Deterministic monotonic revision numbers, timestamps, filenames, and routing references implied by the approved transaction do not require reapproval by themselves.

## 5. One bounded mutation transaction

After approval and fresh prerequisite checks, an eligible upgrade executes as one bounded transaction:

```text
freeze approved Preview/candidate
→ materialize required successors
→ preserve/archive predecessors
→ update exact routing/index/manifest
→ reconcile approved Root/Bootstrap scope
→ Project affected verification
→ completion commit
→ fresh terminal readback
```

Per-document Logical Checkpoints are not required during an uninterrupted transaction. Persist a mid-transaction checkpoint only when interruption/handoff, a real blocker, or a non-idempotent/shared effect creates genuine continuation state.

## 6. Proof-domain separation and evidence reuse

**Framework Release Acceptance ≠ Project Upgrade Acceptance.**

Framework Release Acceptance proves the exact Framework candidate/distribution. Project Upgrade Acceptance proves that a consuming Project correctly adopted that candidate while preserving Project-specific invariants.

For either `FAST_PATH` or bounded compatible `ASSESSED_PATH`, exact committed state-bound `RELEASE_FULL` evidence MAY be reused when the freshly observed target tree/content identity exactly matches the evidence binding and all material assumptions remain valid.

Release-proof reuse never removes Project affected verification. The consuming Project still verifies applicable Root/Project Source/Bootstrap/routing/history/UUID/Stable-ID/Project-specific-rule/Binding/rollback/resulting-state invariants.

Release evidence is not reusable when target identity differs, the candidate changed after evidence capture, evidence is stale/contradictory/incomplete/unverifiable, the upgrade changes the Framework candidate itself, or impact cannot be bounded. In that case run the applicable current verification and, when genuinely required, at most one final `RELEASE_FULL` on the exact unchanged final candidate.

Normal consuming-upgrade `RELEASE_FULL` budget is therefore `0` with exact reusable release proof and `1` maximum when a full run is genuinely required absent later evidence invalidation.

## 7. Recovery

After interruption, fresh-read volatile Git/current-routing state, resolve the approved Preview/candidate, inspect durable effects, reuse still-valid comparison/assessment/release evidence, execute only unfinished safe operations, and rerun only invalidated/newly affected checks.

A session/transport failure alone does not invalidate unchanged Git or release evidence. Unknown possibly-applied shared/non-idempotent results use `RESULT_VERIFICATION_REQUIRED` before retry.

## 8. Canonical ProjectFramework chaining

For canonical `captainhuke-dev/ProjectFramework`, integration and self-host reconciliation MAY chain under one exact approved Preview when authority already covers both boundaries:

```text
verified release candidate
→ INTEGRATION_GATE
→ authorized integration
→ fresh merged-result identity/tree verification
→ FRAMEWORK-001 successor
→ applicable Project Source + PROJECT-BOOTSTRAP reconciliation
→ affected postflight
→ terminal reconciliation
```

No second `[Project Upgrade]`, Preview, or approval is required when the merged result exactly matches the already-approved self-host delta.

If integration authority exists but Root/self-host authority does not, complete only the authorized integration, surface `RECONCILIATION_REQUIRED`, and stop before Root mutation. If only local authority exists, stop successfully before integration.

`INTEGRATION_GATE` remains mandatory immediately before every applicable mutable-target integration/publication action; reusable release proof and Preview approval never become permanent target freshness evidence.

## 9. Completion and Brownfield safety

Material Git-backed local upgrade completion still requires approved resulting state, Project affected verification, required review/approval, direct resulting-state confirmation, durable evidence, an observed completion commit, and clean/understood working-tree state.

Existing initialized Projects never auto-adopt Framework `1.18.0` or later. They remain locally pinned until explicit `[Project Upgrade]` invocation and exact mutation approval.

## 10. No runtime expansion

TASK-052 adds no upgrade daemon, auto-updater, merge/release bot, CI/CD mutator, scheduler, watcher, runtime migration engine, validator/CLI, MCP upgrade router, credential store, or persistent service/database.
