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

## Implementation gate

No candidate in this document authorizes implementation. Before any candidate changes normative/current Framework distribution artifacts, it must go through design consolidation, scope review, explicit user approval, and a separate implementation plan.
