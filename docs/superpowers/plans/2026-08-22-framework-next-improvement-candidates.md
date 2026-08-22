# Framework Next Improvement Candidates

Status: PLANNING_ONLY / NOT_IMPLEMENTED

Created: 2026-08-22

## Purpose

Collect user-approved candidate improvements for the next ProjectFramework revision before a final design, version assignment, implementation plan, or normative Framework change is approved.

This document is a planning checkpoint only. It does not change Framework `1.2.4`, Schema `1.0.0`, Root Governance, launcher behavior, or current distribution semantics.

---

## Candidate 1 — Verified Material Task Completion Commit

**Planning status:** USER_APPROVED_FOR_PLANNING

**Implementation status:** NOT_STARTED

### Problem

When GPT-Web, Codex, or another Agent hands work to another execution context, repository identity alone does not guarantee continuation from the same usable state. Material work can exist only as uncommitted working-tree changes, leaving the next Agent unable to distinguish completed work from partial/WIP state or to identify the exact durable checkpoint that should be continued.

### Selected direction — Approach B

For Git-backed work, a Material Task / `ACT-*` that mutates the authoritative repository should not become `DONE` merely because editing finished. Completion should require a verified, durable Git checkpoint containing the current usable result of that Task.

Conceptual flow:

```text
Material Git-backed Task
→ implement / modify
→ verify affected scope
→ completion criteria PASS
→ create coherent Git commit checkpoint
→ verify commit identity + resulting working-tree state
→ Task may become DONE
→ next Task / Agent handoff
```

### Proposed semantic contract

1. **Material repository mutation:** If a Task materially changes the Git-backed Canonical Implementation Source or other authoritative repository artifact, `Task DONE` requires a verified Git commit that contains the usable completed result.
2. **Verification before completion:** A Task must satisfy its affected verification/completion criteria before the completion checkpoint can justify `DONE`.
3. **No required result left only uncommitted:** A Task cannot be treated as durably complete if required completed state exists only in the working tree.
4. **Read-only / no-repository-mutation exception:** Discovery, analysis, review, or another Task that makes no repository mutation has no commit requirement merely to mark the Task complete.
5. **Failed / blocked work:** Failed, blocked, or incomplete work must not be represented as a successful completion checkpoint. WIP commits may exist when useful, but `WIP commit ≠ Task DONE`.
6. **One Task may use multiple commits:** Atomic intermediate commits are allowed. The completion rule concerns whether the final usable Task result is durably represented and verifiable, not whether every Task has exactly one commit.
7. **Commit is distinct from Push:** Local Git commit establishes a durable repository checkpoint in the current workspace. Push/publication to a remote is a separate durability/shared-state and authority decision and must not be silently implied by `Task DONE`.
8. **Cross-Agent handoff:** When continuation crosses execution environments and the receiving Agent cannot access the same local Git object/state, remote publication or another governed durable transfer may be required before claiming continuation-safe handoff.
9. **Handoff observability when material:** Continuation metadata should be able to identify the observed repository, work branch/worktree, verified HEAD SHA, working-tree state, last completed Task, and its completion commit when those facts are needed for reliable continuation.
10. **Authority separation:** Observed work branch/worktree and completion commit do not redefine Repository Location Binding, Canonical Integration Target, or Canonical Implementation Source.
11. **Existing distinctions remain:** `ACT DONE ≠ MS REACHED ≠ OUT ACHIEVED`; a Git completion checkpoint proves durable completion of governed work only, not milestone or outcome success.

### Intended benefit

Provide a deterministic handoff boundary between GPT-Web, Codex, and other Agents so the next Agent can establish exactly which Task result is complete, which Git state is authoritative for continuation, and whether any required work remains only as uncommitted state.

### Explicit non-goals at this planning stage

- Do not modify `SKILL.md`, Core Governance, templates, launchers, release metadata, or Framework version declarations yet.
- Do not require `push` after every Task.
- Do not require commits for read-only Tasks.
- Do not create a new Stable-ID family or Git lifecycle state.
- Do not add automation, hooks, CI/CD, bots, schedulers, or enforcement tooling.

### Design questions reserved for the final design phase

- Exact terminology for the checkpoint in normative Framework text.
- Whether cross-environment handoff should require a remotely reachable commit by default or only when the receiving execution context cannot access the same local repository.
- Minimum verification evidence needed before `Task DONE` for different risk classes.
- Exact `09 Handoff`, `15 Action Registry`, and Git workflow fields/surfaces to update without duplicating authority.

---

## Candidate 2 — Progressive / Risk-Scoped Verification and Evidence Reuse

**Planning status:** USER_APPROVED_FOR_PLANNING

**Implementation status:** NOT_STARTED

### Problem

Verification has accumulated across Framework releases. Later features often repeat semantic scans, release checks, launcher checks, starter checks, Base Freshness checks, and post-integration checks at multiple Task boundaries even when only a small affected scope changed. This improves safety but can make normal development unnecessarily slow and can cause verification work to grow with the number of Tasks rather than with actual scope, dependency impact, and risk.

### Selected direction

Use progressive verification whose depth is determined by affected scope, dependency impact, and Framework risk class. Full-distribution verification is reserved for semantic acceptance points such as a Release Candidate or equivalent release gate. Logical Checkpoints verify durable continuation and only the cross-surface integrity actually affected by the checkpoint; they do not imply a full regression run by default.

Conceptual model:

```text
Task change
→ identify affected invariants / dependencies / risk
→ run minimum sufficient affected-scope verification
→ PASS
→ Candidate 1 completion commit when repository mutation is Material
→ continue

Logical Checkpoint / handoff
→ verify durable continuation state
→ verify only affected cross-surface integrity when applicable

Release Candidate
→ run full release/distribution verification once

Pre-Merge / Integration Gate
→ re-resolve target freshness
→ confirm existing verification evidence is still valid
→ rerun only invalidated or newly affected verification

Post-Merge
→ if resulting tree is exactly the already verified candidate, confirm resulting state
→ if integration changed the verified tree, escalate affected/full verification as required
```

### Proposed verification profiles

1. **`TASK_LOCAL_FAST`** — default for a Material Task before `DONE`; verifies the directly affected behavior, files, invariants, and risk-appropriate completion criteria.
2. **`CHECKPOINT_INTEGRITY`** — used at a Logical Checkpoint or Agent handoff; verifies persistence/continuity facts and only materially affected cross-surface relationships.
3. **`RELEASE_FULL`** — full current Framework/distribution regression for a completed Release Candidate or equivalent semantic acceptance point.
4. **`INTEGRATION_GATE`** — verifies Canonical Integration Target/Base Freshness, blocking semantic movement, and validity of prior acceptance evidence immediately before integration.

The exact profile names are planning vocabulary only until final design approval.

### Proposed semantic contract

1. **Minimum sufficient verification:** Each Task runs the smallest verification set that is sufficient for its affected scope, dependencies, and risk. `Every Task → run everything` is not the default.
2. **Dependency-aware selection:** Verification derives from `changed scope → affected invariants/dependencies → required checks`, not merely from which Task number is executing.
3. **Risk scaling:** Existing `R0 / R1 / R2 / R3` risk semantics influence verification depth. Higher shared/external impact requires stronger preflight and resulting-state confirmation than read-only or reversible-local work.
4. **Logical Checkpoint is not Release Full:** A Logical Checkpoint primarily proves durable continuation state. Full Framework/distribution verification is required there only when the checkpoint itself is an applicable semantic acceptance/release gate or the changed scope demands it.
5. **Full verification at acceptance boundary:** A completed Framework Release Candidate receives one full current-distribution verification before release/integration acceptance, subject to stricter Project rules.
6. **Verification evidence is state-bound:** Verification evidence should identify enough observed state to know what it proves, including candidate/source identity or HEAD when Git-backed, affected scope/profile, relevant target/dependency state when material, and result.
7. **Evidence reuse:** Fresh verification evidence may be reused while the state it proves remains materially unchanged. Re-running the same full suite without an invalidating change is not required by default.
8. **Selective invalidation:** Candidate/source change, materially changed dependency, materially moved integration target, changed verification rule, or another affected invariant invalidates only the evidence whose assumptions are no longer true unless the impact cannot be bounded safely.
9. **Escalation on uncertainty:** If affected scope or evidence validity cannot be determined safely, verification escalates rather than guessing that prior evidence remains valid.
10. **Pre-Merge behavior:** `INTEGRATION_GATE` re-resolves the current Canonical Integration Target and Base Freshness and checks whether previous `RELEASE_FULL`/affected evidence is still valid. A target movement does not automatically require a full rerun when it is verified non-semantic and does not invalidate the evidence assumptions.
11. **Post-Merge proportionality:** Exact fast-forward/integration to an already verified candidate tree normally needs resulting-state confirmation rather than an unconditional full rerun. Conflict resolution, rebase/tree changes, merge-time edits, semantic target movement, or another changed resulting tree triggers affected/full re-verification as appropriate.
12. **No weakening of acceptance:** Faster verification changes when and how much is rerun; it does not allow a Task, Release Candidate, or integration to claim completion when required applicable verification has not passed.

### Relationship to Candidate 1

Candidate 1 and Candidate 2 are intended to compose:

```text
Material Task
→ TASK_LOCAL_FAST / risk-appropriate affected verification PASS
→ verified completion commit
→ Task DONE
→ next Task

Release Candidate complete
→ RELEASE_FULL once
→ evidence bound to verified candidate state
→ INTEGRATION_GATE reuses or selectively invalidates that evidence
```

This keeps Agent handoffs deterministic without making every Task pay the cost of a full release regression.

### Intended benefit

- Shorten normal Task completion time while preserving fail-closed behavior where risk or uncertainty requires it.
- Prevent verification volume from growing mechanically with Task count.
- Reduce duplicate full-regression runs when the verified candidate has not changed.
- Make verification behavior more deterministic between GPT-Web, Codex, and other Agents.
- Preserve strong Release and Integration gates while keeping Task-level work responsive.

### Explicit non-goals at this planning stage

- Do not remove existing safety, authority, Base Freshness, or resulting-state verification requirements.
- Do not declare that `git diff --check`, a clean working tree, or a successful merge alone proves semantic correctness.
- Do not make Logical Checkpoints equivalent to full release verification.
- Do not add executable validators, CI/CD, hooks, bots, schedulers, or background verification automation.
- Do not modify current Framework `1.2.4` behavior until the consolidated next-revision design is explicitly approved.

### Design questions reserved for the final design phase

- Final names and normative definitions of verification profiles.
- Exact minimum metadata needed to bind reusable verification evidence to candidate/dependency/target state without creating excessive bookkeeping.
- Which changes invalidate `TASK_LOCAL_FAST`, `CHECKPOINT_INTEGRITY`, `RELEASE_FULL`, or `INTEGRATION_GATE` evidence.
- How to express risk-based escalation concisely in Core Governance, `SKILL.md`, plans, Handoff, and pressure scenarios without creating another large verification bureaucracy.
- Whether Framework plans should declare verification profiles per Task or derive them from affected-scope/risk rules with only exceptional overrides.

---

## Implementation gate

No candidate in this document authorizes implementation. Before any candidate changes normative/current Framework distribution artifacts, it must go through design consolidation, scope review, explicit user approval, and a separate implementation plan.
