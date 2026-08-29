---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.2.1"
project_source_framework_version: "1.2.2"
project_source_schema_version: "1.0.0"
approved_at: "2026-08-21T15:05:00+07:00"
approval_basis: "USER_EXPLICIT_APPROVAL"
compatibility: "BACKWARD_COMPATIBLE_GIT_BASE_FRESHNESS_AND_FORWARD_PORT_GOVERNANCE"
---

# Framework Governance Amendment — Git Base Freshness and Forward-Port

## Binding Change

Framework `1.2.2` adds **Git Base Freshness and Forward-Port governance** while preserving Project Source Schema `1.0.0`, the existing semantic-slot namespace, existing Stable-ID families, and Project-local Framework pinning.

The binding changes are:

1. New independent Git branch/worktree work starts from a freshly verified **Canonical Integration Target** rather than inheriting whichever feature branch is currently checked out. For ProjectFramework, canonical integration is repository `main` / local `origin/main` semantics.
2. Local branch name alone is not freshness evidence. When the canonical target cannot be verified, Base Freshness is `UNKNOWN`; freshness must not be silently assumed.
3. Feature-on-feature ancestry is permitted only as explicit `STACKED_WORK`, with parent ref/commit, dependency reason, invalidation condition, and expected integration order discoverable. Material parent movement triggers child base re-evaluation.
4. Base Freshness vocabulary is `FRESH | STALE_NON_SEMANTIC | STALE_SEMANTIC | UNKNOWN`. `BASE_STALE` is a workflow condition only; it is not a Project Lifecycle/Execution state, Epistemic Status, semantic slot, or new Stable-ID family.
5. Commit count is not a semantic staleness threshold. Classification is based on whether upstream changes alter applicable Framework/Root Governance/Schema/authority/routing/Requirements/Decisions/interfaces/technical-deployment contracts or other assumptions relied upon by the work.
6. `STALE_NON_SEMANTIC` places the affected work in `BASE_STALE` until the base is updated and affected verification is re-run successfully. It may be resolved with `REBASE_REQUIRED` for private/rewritable work when appropriate; shared/public branches may use a history-preserving merge/update strategy instead. Only after the update and verification may the work return to `FRESH`; Framework does not require published-history rewriting.
7. `STALE_SEMANTIC` requires `BASE_STALE`, affected-scope reassessment, and normally `FORWARD_PORT_REQUIRED`. A conflict-free Git rebase/merge is insufficient evidence of semantic compatibility.
8. Forward-Port starts from a clean branch/worktree at the current canonical target, treats the stale branch as source material/evidence, and carries only still-valid accepted changes. Temporary staging/transport artifacts, obsolete workflows/version metadata, superseded assumptions, and unrelated experiments are excluded unless independently justified as part of the current deliverable.
9. The **Pre-Merge Base Freshness Gate** re-resolves the current target head. `UNKNOWN`, unresolved semantic drift, or material target movement after review blocks affected acceptance until re-evaluated.
10. `git conflict = 0`, `mergeable = true`, successful rebase, or a clean textual diff does not override the semantic gate. **Mergeable ≠ Acceptable.**
11. If base staleness becomes material Project truth, existing canonical objects remain authoritative: `DRIFT-*`, `CONFLICT-*`, `MIG-*`, and `CR-*` are used according to existing semantics. No parallel Git-freshness Stable-ID family is created.
12. Existing initialized Projects remain governed by their locally pinned active `FRAMEWORK-001`. Upstream Framework `1.2.2` does not auto-upgrade them; Framework migration still uses existing `MIG-*` assessment, approval, validation, promotion, and history-preservation rules.

## Base Freshness Checkpoints

When Git integration is in scope, freshness is checked at least:

```text
before new independent branch/worktree creation
before a new material implementation phase when upstream may have moved
before opening/materially updating an integration PR when base may be stale
immediately before acceptance/merge if target head changed after review
```

## Base Freshness Gate

When material, a gate may record observed values such as:

```yaml
base_freshness_gate:
  target_ref: "<VERIFIED_CURRENT_TARGET>"
  target_head_sha: "<OBSERVED_SHA>"
  reviewed_feature_base_sha: "<OBSERVED_BASE_SHA>"
  freshness: "FRESH | STALE_NON_SEMANTIC | STALE_SEMANTIC | UNKNOWN"
  semantic_base_changed: true|false|unknown
  disposition: "ACCEPT | UPDATE_BASE | REBASE_REQUIRED | FORWARD_PORT_REQUIRED | BLOCK"
```

Ref/SHA/version values are observational only. Never fabricate Git identity to make a record look complete.

## Scope Boundary

This amendment changes governance/workflow semantics only. It does not authorize Git hooks, GitHub Actions, bots, validators/CLI, schedulers, merge queues, branch-protection automation, or other executable enforcement. ProjectFramework remains documentation/governance first.

## Compatibility

Framework `1.2.2` is backward compatible with Schema `1.0.0`. Existing Projects continue under their approved local Framework pin until a governed migration explicitly upgrades them. No semantic-slot meaning or Stable-ID namespace is changed by this release.
