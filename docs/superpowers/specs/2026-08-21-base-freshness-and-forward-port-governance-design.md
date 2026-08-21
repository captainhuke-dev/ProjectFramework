# Base Freshness and Forward-Port Governance Design

Date: 2026-08-21
Status: WRITTEN SPEC APPROVED — 2026-08-21T15:05:00+07:00
Repository: `captainhuke-dev/ProjectFramework`
Base: `main@0dbfce789486f6c28853d3abfff0966f1ab8256d` (Framework 1.2.1)
Release target: Framework 1.2.2 / Schema 1.0.0

## 1. Purpose

Prevent new Git worktrees/branches from becoming semantically stale while canonical `main` continues to evolve. The Framework must distinguish ordinary Git divergence from Framework/governance drift, require new independent work to start from a fresh canonical base, and provide a safe Forward-Port path when a feature was built on an obsolete semantic base.

The governing principle is:

> A branch being mergeable by Git does not prove that it is acceptable against the current Framework.

## 2. Scope

This feature governs Git-backed Project work when branches/worktrees are used, including ProjectFramework development itself:

1. authoritative base selection for new worktrees/branches;
2. base snapshot/freshness recording when material;
3. independent work vs explicitly stacked work;
4. checkpoint and pre-merge base freshness checks;
5. non-semantic vs semantic upstream drift;
6. `BASE_STALE`, `REBASE_REQUIRED`, and `FORWARD_PORT_REQUIRED` workflow conditions;
7. Forward-Port into a clean branch/worktree from current canonical `main`;
8. clean integration and pre-merge acceptance gates;
9. preservation of existing Project-local Framework pinning.

## 3. Non-Goals

This feature does not:

- require worktrees for every Project or every task;
- create GitHub Actions, bots, hooks, validators, schedulers, merge queues, or branch-protection automation;
- require rebasing public/shared history;
- require a fixed commit-count threshold for staleness;
- treat every upstream commit as semantic drift;
- auto-cherry-pick or auto-rewrite stale branches;
- make upstream Framework changes auto-upgrade initialized Projects;
- change Project Source semantic slots, Stable-ID namespaces, or Schema 1.0.0.

## 4. Terminology

### 4.1 Canonical Integration Target

For the ProjectFramework repository, the canonical integration target is `origin/main` / repository `main`. For another Git-backed Project, use that Project's explicitly verified canonical integration branch. Do not guess a production/integration branch when it is unknown.

### 4.2 Base Snapshot

A material work package may record:

```yaml
work_base:
  repository: "<OWNER/REPO>"
  target_ref: "<VERIFIED_CANONICAL_INTEGRATION_REF>"
  base_commit_sha: "<OBSERVED_SHA>"
  framework_version: "<PINNED_OR_APPLICABLE_VERSION>"
  schema_version: "<PINNED_OR_APPLICABLE_VERSION>"
  captured_at: "<ISO8601_WITH_TIMEZONE>"
```

Values are observational. Never fabricate a SHA/ref/version merely to complete metadata.

### 4.3 Independent Work

A worktree/branch whose deliverable does not depend on unmerged feature-branch state.

### 4.4 Stacked Work

A deliberate feature-on-feature dependency. `STACKED_WORK` is allowed only when the dependency is explicit, including parent branch/ref or commit and the reason the work cannot start independently from the canonical integration target.

### 4.5 Base Freshness

Base freshness is evaluated against the current canonical integration target, not merely local `main`.

```text
FRESH
STALE_NON_SEMANTIC
STALE_SEMANTIC
UNKNOWN
```

`UNKNOWN` is used when the target/base relationship cannot be verified; do not silently assume freshness.

### 4.6 BASE_STALE

`BASE_STALE` is a workflow condition, not a new Project lifecycle/execution state and not an Epistemic Status. It means the current work package cannot safely start another material implementation phase or be accepted for integration until the base relationship is resolved.

### 4.7 REBASE_REQUIRED

A workflow disposition for private/rewritable work when upstream drift is non-semantic and replaying work on the current target is appropriate. For shared/public branches, merge/update strategies that preserve published history may be used instead; the Framework does not mandate history rewriting.

### 4.8 FORWARD_PORT_REQUIRED

A workflow disposition used when upstream changes alter applicable Framework/governance/schema/authority/contracts or otherwise invalidate assumptions of the stale work. The stale branch is evidence/source material, not the integration base.

## 5. Latest-Main-First Contract

Before creating a new **independent** branch/worktree, the Agent must fresh-read/fetch the canonical integration target and create the new work from that current target state.

For ProjectFramework, the conceptual default is equivalent to:

```text
fetch canonical repository
→ resolve current origin/main
→ create independent branch/worktree from current origin/main
→ record observed base when material
```

Do not create a new independent branch from whichever feature branch happens to be checked out.

Local `main` is not assumed current merely because its name is `main`.

## 6. Stacked Work Exception

Feature-on-feature ancestry is allowed only as explicit `STACKED_WORK`.

A stacked work package must record or make discoverable:

```text
Parent branch/ref or commit
Dependency reason
What becomes invalid if parent changes
Expected integration order
```

When the parent changes materially, the child must re-evaluate its base. Parent merge/closure does not automatically prove the child is fresh.

## 7. Base Freshness Checkpoints

Freshness is checked at material checkpoints, not after every commit.

Minimum checkpoints:

1. before starting a new independent worktree/branch;
2. before beginning a new material implementation phase after upstream may have moved;
3. before opening or materially updating an integration PR when the base may be stale;
4. immediately before accepting/merging into the canonical target if the target head changed since the last review.

Commit count alone is not a semantic threshold. One governance/schema commit can be more material than many unrelated documentation commits.

## 8. Drift Classification

### 8.1 Non-Semantic Upstream Drift

Examples include changes that do not alter assumptions/contracts relevant to the feature, such as unrelated formatting, typo fixes, or independent content.

Disposition:

```text
BASE_STALE
→ verify non-semantic impact
→ REBASE_REQUIRED for private/rewritable work
   OR merge/update target into shared work without rewriting public history
→ re-run affected verification
→ FRESH
```

### 8.2 Semantic Upstream Drift

Semantic drift includes changes to applicable:

- Framework version or Root Governance;
- Project Source Schema or namespace semantics;
- authority/approval contract;
- canonical ownership/routing;
- Requirements/Decisions/interfaces relied upon by the work;
- technical/deployment contracts materially assumed by the branch;
- source-of-truth or migration semantics.

Disposition:

```text
BASE_STALE
→ stop affected new implementation scope
→ assess changed assumptions/contracts
→ FORWARD_PORT_REQUIRED
→ create clean branch/worktree from current canonical target
→ port only still-valid accepted changes
→ validate against current semantics
→ FRESH
```

A conflict-free rebase/merge is insufficient evidence for semantic compatibility.

## 9. Forward-Port Contract

When `FORWARD_PORT_REQUIRED` applies:

1. Fresh-read/fetch the current canonical integration target.
2. Create a clean branch/worktree from that exact target state.
3. Treat the stale branch as source material/evidence, not authority.
4. Re-evaluate each intended change against current Framework/Requirements/Decisions/contracts.
5. Carry over only still-valid changes. Use selective cherry-pick when commit boundaries are clean; otherwise re-implement the accepted intent on the current base.
6. Exclude temporary staging/transport artifacts, obsolete workflows, old version metadata, superseded assumptions, and unrelated branch history.
7. Re-run applicable validation and record remaining drift/conflict explicitly.
8. Integrate the clean result, not the stale branch as-is.

Forward-Port is a semantic adaptation process, not merely a Git command.

## 10. Clean Integration Branch

For large, old, experimental, stacked, or semantically drifted work, prefer a clean integration branch/worktree created from the current canonical target.

Conceptual flow:

```text
stale/experimental feature
        |
        | accepted changes only
        v
current canonical main → clean integration branch → validate → PR/merge
```

The clean integration result should contain the intended current deliverable, not temporary branch scaffolding or transport history.

## 11. Pre-Merge Base Freshness Gate

Before acceptance/merge, determine:

```yaml
base_freshness_gate:
  target_ref: "<CURRENT_CANONICAL_TARGET>"
  target_head_sha: "<OBSERVED_CURRENT_SHA>"
  reviewed_feature_base_sha: "<OBSERVED_BASE_SHA>"
  freshness: "FRESH | STALE_NON_SEMANTIC | STALE_SEMANTIC | UNKNOWN"
  semantic_base_changed: true|false|unknown
  disposition: "ACCEPT | UPDATE_BASE | REBASE_REQUIRED | FORWARD_PORT_REQUIRED | BLOCK"
```

Acceptance requires `FRESH` or an explicitly resolved equivalent after update/Forward-Port. `UNKNOWN`, unresolved semantic drift, or a changed target head requiring re-evaluation blocks acceptance of the affected scope.

`git conflict = 0` does not override this gate.

## 12. Relationship to Existing DRIFT / CONFLICT

`BASE_STALE` is the work-package condition. Use existing canonical objects when the condition becomes material Project truth:

- `DRIFT-*` when expected and observed implementation/governance domains no longer align;
- `CONFLICT-*` when competing semantic states require resolution;
- `MIG-*` when an initialized Project changes its pinned Framework/Schema;
- `CR-*` when a material Project change requires governed impact/decision handling.

Do not create a parallel Stable-ID family solely for Git base freshness.

## 13. Project-Local Framework Pinning

Existing initialized Projects remain governed by their locally pinned active `FRAMEWORK-001`. Upstream ProjectFramework moving from 1.2.1 to 1.2.2 does not auto-upgrade them.

This design governs how Git work packages are based and integrated. A local Project Framework upgrade still uses existing `MIG-*` + assessment + approval + validation semantics.

## 14. Operational Guidance for Agents

When Git worktrees/branches are in scope, operational guidance should prefer:

```text
Independent new work → current canonical integration target
Explicit dependent work → STACKED_WORK
Checkpoint drift, non-semantic → update/rebase appropriately
Semantic drift → FORWARD_PORT_REQUIRED
Before merge → Base Freshness Gate against current target head
```

Do not force rebase on a shared/public branch. Do not choose a canonical branch by guess. Do not equate branch ancestry with authority.

## 15. Framework Distribution Changes

The 1.2.2 implementation should update:

- `managing-project-source/tests/pressure-scenarios.md` first as the behavioral RED contract;
- `managing-project-source/references/core-governance-rules.md` as normative semantics;
- `managing-project-source/templates/00-project-source-framework.md` so initialized Projects can pin the contract;
- `managing-project-source/SKILL.md` with operational workflow/quick-reference/red flags;
- applicable mockup starter/template material needed to keep current starter semantics aligned;
- `managing-project-source/FRAMEWORK-RELEASE.yaml` and README/version surfaces for release identity;
- a new Framework amendment for 1.2.2.

Platform ChatGPT/Claude launchers do not require expansion unless the new contract cannot be reached through their existing canonical read-through. Their <=4,500-character and shared-contract constraints remain unchanged.

## 16. Acceptance Scenarios

The implementation must pass pressure scenarios covering at least:

1. independent worktree created while a feature branch is currently checked out;
2. local `main` stale while `origin/main` has advanced;
3. feature behind upstream only by unrelated/non-semantic changes;
4. feature based on Framework 1.2.1 while main changes Root Governance/Framework semantics;
5. conflict-free Git merge that is semantically stale;
6. explicit stacked work and parent changes;
7. Forward-Port that excludes temporary/staging artifacts;
8. target `main` moving after review but before merge.

## 17. Compatibility and Release Semantics

Framework 1.2.2 remains backward compatible with Schema 1.0.0. It introduces no new semantic slot and no new Stable-ID namespace. Existing local Project pins remain unchanged until governed migration.

The change is documentation/governance first. No executable Git enforcement, CI, bot, hook, validator, or branch-protection mechanism is authorized by this release.
