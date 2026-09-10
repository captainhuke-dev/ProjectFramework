# TASK-046 Framework 1.15 Reconciliation and V2 Cancellation Design

**Task:** TASK-046 — Final Response Close Simplification / supersession reconciliation
**Goal:** OUT-013 — Reconcile ProjectFramework to Framework 1.15, cancel the 2.0 line, preserve TASK-044/TASK-046 history, and complete local verification
**Design State:** USER_APPROVED_REVISED_DIRECTION / WRITTEN_SPEC
**Date:** 2026-09-10
**Implementation boundary:** local ProjectFramework governance/documentation/templates/tests/reconciliation only; no push/publication/merge, no AI-ControlTower mutation, no runtime/parser/validator/CLI work

## 1. Decision Summary

The user superseded the original TASK-046 two-field close direction before TASK-046 implementation. The current desired visible Final Response contract is the already-implemented TASK-045 Framework 1.15 contract:

```text
### ทำอะไรไป?

<concise statement of what was done or determined>

### และถัดไปคืออะไร?

[Next Action]: <one exact next action or ไม่มีขั้นตอนถัดไป>

[Next Goal]: <one safe copy-ready [Goal] ... / [Goal] CHANGE ... command or ไม่มี>

[Reason]: <concise reason>
```

`[Next Goal]` is mandatory as a visible semantic field. Its value may be `ไม่มี`. It is presentation-only and never creates `OUT-*`, `AUTH-*`, `ACT-*`, or `ENV-*` until the Human explicitly invokes `[Goal]`.

`[Chat]` and `[Required Read]` remain internal continuation/read-routing concepts where applicable, but are not mandatory visible Final Response fields. Nothing follows `[Reason]`.

ProjectFramework 2.0 / AI-ControlTower Protocol Integration (TASK-044) is cancelled by explicit user direction before implementation/cutover. ProjectFramework remains on the 1.15 line.

## 2. Observed Baseline

Canonical published repository state at Goal start is `origin/main` Framework 1.14.0. TASK-045 exists as a separate local, unpushed verified Framework 1.15.0 lineage with:

- final candidate `bc7f91c49372ff33e9726da7461288479438b86a`;
- candidate tree `9170ba8fccbc1bf3f6031441389392d372f8950a`;
- Framework-Source tree `c095bd6570adb9668755d4598087dee0e4729208`;
- structural `13/13 PASS`;
- AFFECTED `27/27 PASS`;
- one final RELEASE_FULL `33/33 PASS_RUN_1`;
- release evidence commit `4278182`;
- publication `NOT_AUTHORIZED / NOT_PUSHED`.

TASK-046 was later registered separately with a two-field `Next Action + Reason` target and `BREAKING_RESPONSE_INTERFACE` classification. That direction is now superseded by the explicit user instruction that `[Next Goal]` remains mandatory and Framework 1.15 should be used instead of 2.0.0.

TASK-044 V2 reached `PRE_MERGE_READY / IMPLEMENTATION_NOT_STARTED`; its pre-merge Goal is terminal and no V2 execution authority remains. No ProjectFramework→AI-ControlTower cutover or V2 runtime implementation occurred.

## 3. Reconciliation Model

### 3.1 TASK-045 becomes the implementation baseline

Do not reimplement the response-close feature under TASK-046. Reuse the TASK-045 Framework 1.15 implementation as the implementation baseline because its intended contract matches the user's current direction:

`Next Action → Next Goal → Reason`.

TASK-045 remains historical `DONE / VERIFIED_COMPLETE`. Its original candidate/evidence are immutable provenance and are not rewritten.

### 3.2 TASK-046 is cancelled as superseded before implementation

TASK-046's original two-field/breaking direction is intentionally cancelled rather than marked DONE. Its registration commit remains historical evidence that the two-field direction was once requested. Current records state that the user superseded it before implementation.

`TASK-046 CANCELLED` means its original implementation scope was intentionally closed; it does not mean TASK-045 is cancelled.

### 3.3 TASK-044 / ProjectFramework 2.0 is cancelled before cutover

TASK-044 is brought into the current Task ledger as a historical record with `CANCELLED` status and explicit cancellation basis. Its V2 design/spec/plan/merge-manifest artifacts are preserved byte-for-byte where imported into the reconciliation branch, with original V2 head/provenance recorded.

Cancellation must not:

- delete or rewrite the V2 design/plan/evidence history;
- mutate AI-ControlTower;
- perform the planned repository merge/cutover;
- reuse V2 `OUT-009/AUTH-009/ACT-021/ENV-009` or `OUT-011/AUTH-011/ACT-023/ENV-011` as new authority;
- imply that V2 implementation ever occurred.

## 4. Framework 1.15 Correction Pass

Fresh review found at least one current user-facing README statement that still claims every governed response exposes `[Chat]` and `[Required Read]`, despite the 1.15 section defining `Next Action → Next Goal → Reason`. The SKILL continuation section also retains old `[Chat]`-field wording in lifecycle bullets even though 1.15 moved Chat lifecycle state to internal Handoff semantics.

Therefore the existing TASK-045 release evidence remains valid provenance for its exact candidate, but that candidate is not automatically accepted as the final reconciliation candidate. The reconciliation implementation must perform a bounded current-surface drift audit before final acceptance.

Rules:

1. Historical release sections/specs/plans/amendments/evidence that accurately describe older four-field Framework versions remain unchanged.
2. Current/generic normative or user-facing statements that contradict Framework 1.15 are corrected.
3. If any `Framework-Source/` byte changes are required, the old TASK-045 candidate is preserved as historical evidence and a corrected Framework 1.15.0 candidate is created and verified. Because 1.15.0 is not published, a correction may remain version `1.15.0`; no automatic `1.15.1` bump is required solely for an unpublished candidate correction.
4. If the correction changes the final candidate, prior RELEASE_FULL evidence must not be represented as verification of the changed candidate. Run exactly one RELEASE_FULL on the corrected unchanged final candidate.
5. Schema remains `1.0.0`; release format remains `3` unless verification discovers a requirement that genuinely changes Project Source schema.

## 5. TASK-042 / TASK-043 Compatibility

TASK-042's unskippable finalization guarantee remains binding. TASK-043's Strict Governed Interface / Command Contract Completeness Gate remains binding.

The pipeline remains:

`Command Contract Completeness Gate → Response Close Completeness Gate → Emit`.

The Response Close Completeness Gate validates exactly the Framework 1.15 visible shape:

- two required headings, exactly once and ordered;
- exactly one `[Next Action]` field;
- exactly one mandatory `[Next Goal]` field;
- exactly one `[Reason]` field;
- field order `Next Action → Next Goal → Reason`;
- no mandatory visible `[Chat]` or `[Required Read]` field;
- nothing after `[Reason]`;
- valid Next Goal safety disposition.

## 6. Continuity and Required-Read Boundary

Removing visible `[Chat]` and `[Required Read]` does not remove their internal semantics.

Internal continuation remains governed through applicable:

- `03 Current State`;
- `09 Handoff`;
- `OUT-* / AUTH-* / ACT-* / ENV-*`;
- Resume/continuation pointers and `authority_transfer: false`;
- `PROJECT-BOOTSTRAP.md → 00 → 01 → 03 → task-specific source → 09 when applicable`.

No visible response-close field becomes a substitute for Project Source persistence.

## 7. Brownfield and Release Behavior

Existing initialized Projects remain locally pinned and do not silently adopt Framework 1.15. Adoption remains governed through `[Project Upgrade]` or another explicitly authorized migration.

This Goal authorizes local reconciliation/verification only. It does not authorize:

- push, publication, PR creation, or merge;
- destructive branch/worktree deletion;
- Root Governance / Project Location Binding mutation;
- external AI disclosure;
- actual secret-value handling;
- AI-ControlTower mutation;
- ProjectFramework 2.0 cutover or runtime implementation.

## 8. Historical Provenance Preservation

Preserve without semantic rewriting:

- TASK-045 design/plan/release evidence and candidate identities;
- original TASK-046 registration commit and its former two-field direction;
- TASK-044 V2 written design, migration plan, merge manifest, V2 branch/head provenance, and pre-merge evidence;
- TASK-042/TASK-043 historical artifacts;
- older release documentation whose four-field representation was true at capture time.

Current records may add cancellation/supersession annotations; they must not falsify the earlier captured state.

## 9. Verification Strategy

Before local completion:

1. Fresh-observe canonical `origin/main` and reconciliation branch ancestry.
2. Verify TASK-045 implementation history is an ancestor of the reconciliation branch.
3. Verify TASK-046 registration history is preserved.
4. Preserve/import TASK-044 V2 historical artifacts and record original V2 head/hash references.
5. Run a current-surface scan for response-close statements and classify each hit as current/generic versus explicitly historical.
6. Correct current/generic drift only.
7. Verify Core/SKILL/README/current maintained templates/starters/migration guidance agree on mandatory `Next Action → Next Goal → Reason` and internal-only Chat/Required Read semantics.
8. Verify TASK-042 no-early-return semantics and TASK-043 command-gate ordering remain intact.
9. Verify seven Registered Commands remain unchanged.
10. Verify scenario numbering remains contiguous/unique and current response-close pressure scenarios cover the 1.15 contract.
11. Verify 22 maintained starter stamps and Framework/Schema identity are internally consistent.
12. Run `git diff --check` and ensure no unintended runtime/parser/validator/CLI artifacts are introduced.
13. Run affected verification for the reconciliation/correction scope.
14. If the Framework candidate changed, freeze the corrected candidate and run exactly one final RELEASE_FULL on that unchanged candidate; otherwise reuse valid state-bound TASK-045 release evidence and run proportional reconciliation verification.
15. Persist final evidence and terminalize OUT-013/AUTH-013/ACT-025/ENV-013 only after direct verification and completion-commit observation.

## 10. Acceptance Criteria

The Goal is locally complete when all of the following are true:

- Framework remains on the 1.15 line; no 2.0 cutover remains active.
- `[Next Goal]` is mandatory in the current visible Final Response contract.
- `[Chat]` and `[Required Read]` are internal-only continuation/read-routing semantics, not mandatory visible close fields.
- TASK-044 is `CANCELLED / IMPLEMENTATION_NOT_STARTED`, with V2 provenance preserved.
- TASK-046 is `CANCELLED / SUPERSEDED_BEFORE_IMPLEMENTATION`, with its registration provenance preserved.
- TASK-045 remains `DONE / VERIFIED_COMPLETE` as the implementation lineage used for Framework 1.15.
- current/generic Framework 1.15 surfaces have no contradictory four-field close requirement.
- historical four-field records remain preserved where true at capture time.
- TASK-042 and TASK-043 guarantees remain intact.
- applicable affected verification passes.
- final candidate verification/evidence is state-bound and valid.
- local Project Source lifecycle records are reconciled and the completion commit is freshly observed.
- publication remains `NOT_AUTHORIZED / NOT_PUSHED`.

## 11. Rollback

Before any correction commit, the reconciliation branch can be abandoned without modifying TASK-045, TASK-044 V2, TASK-046 registration, `main`, or `origin/main`. After commits, rollback uses ordinary Git history/revert semantics; never rewrite or delete historical Task/evidence objects as a substitute for cancellation.
