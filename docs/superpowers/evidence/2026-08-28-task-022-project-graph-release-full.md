# TASK-022 Project Graph + OpenViking Relation Governance (Framework 1.6.0) — RELEASE_FULL Evidence

Captured: `2026-08-28T20:18:18+07:00` (Asia/Bangkok)

Task: `TASK-022`
Execution branch: `main` (inline fallback after isolated-worktree mutation routing was blocked by host Active Workspace guard)
Base before TASK-022 registration: `6cd1137518f850864a95225f23e122d492c1e7fa`

## Release identity

- Framework: **1.6.0** (previous 1.5.0)
- Schema: **1.0.0** (unchanged)
- Release format: **3** (unchanged)
- Latest amendment: `references/framework-governance-amendment-260828-task022.md`
- Candidate commit: `6eb87904374f1fb3034db572e3773238e4ed0e14`
- Candidate `managing-project-source` tree SHA: `9d1d06916b944f8169477c220777ee5874e689bf`

## Implemented scope

1. **Standard conditional `92 Project Graph`** — current `REL-*` Project-relation assertions have one canonical Project-local home; generic extension space moves to `93–99`; `18–19` remain RESERVED.
2. **Stable relation identity and vocabulary** — endpoints use immutable `project_uuid`; core relation types are `PARENT_OF | CHILD_OF | PEER_OF | DEPENDS_ON | SUPPORTS | RELATED_TO`; namespaced extensions use `X-<PROJECT_OR_DOMAIN_NAMESPACE>:<RELATION_TOKEN>`; assertion states are `ASSERTED | CORROBORATED | CONFLICTED | RETIRED`.
3. **Late binding and semantic nesting** — Projects may begin unrelated and materialize `92` later; Project relation topology does not transfer repository/storage/local-workspace/integration/implementation/runtime authority.
4. **Federated authority boundary** — AI-ControlTower owns cross-Project indexing/orchestration; OpenViking is exactly `DERIVED_ONLY` and `REBUILDABLE` from authoritative Project Sources. Derived inverse edges, ranking, confidence, or recency never become Project authority.
5. **Merge/split and drift/conflict behavior** — successor/descendant relations are reassessed rather than bulk-cloned; existing `DRIFT-*`, `CONFLICT-*`, and `MIG-*` families are reused.
6. **Brownfield custom-slot-92 migration safety** — existing custom `92` is never overwritten; `MIG-*` preserves identity/history/references and relocates only through governed approval before standard `92` activation.
7. **Concrete starter propagation** — root template, core skeletons, mockup routing/index/manifest/migration guidance, new `92-Project-Graph.template.md`, all 22 current starter stamps at 1.6.0, and launcher release headers updated while marker bodies stay byte-identical.
8. **Pressure coverage** — scenarios `163–171` cover late binding, derived-only index authority, corroboration, conflict, Brownfield collision, semantic nesting, merge/split reassessment, full rebuild, and namespaced relation types.

## Commits

Preparation / design:

- `2583020` — register TASK-022 Project Graph governance
- `793a37c` — approve TASK-022 Project Graph design
- `61cee5b` — add TASK-022 implementation plan

Implementation:

- `9f32f72` — define Framework 1.6 Project Graph release
- `ea43867` — add federated Project Graph governance
- `0d9978b` — add Project Graph slot 92 templates
- `2240cec` — add Project Graph pressure scenarios
- `6eb8790` — align Project Graph derived-index canonical tokens

## Verification history

### First candidate finding

Candidate `2240cec` failed the first RELEASE_FULL attempt at the cross-surface check **OpenViking derived-only**: the TASK-022 amendment described OpenViking as derived/rebuildable but did not carry the exact canonical token `DERIVED_ONLY`. The candidate evidence was invalidated. The amendment was corrected in `6eb8790` to use exact `DERIVED_ONLY` and `REBUILDABLE` vocabulary.

### Verification-method correction

On corrected candidate `6eb8790`, one rerun initially stopped at the historical TASK-021 immutability check because the check compared Git blob LF bytes to a Windows CRLF working-tree representation. This was a verification-method defect, not a candidate edit. Git blob identities were then checked directly:

- base `6cd113...` TASK-021 amendment blob: `e12c98c9c3ab8cb39b1358c29761714f8506889c`
- candidate `6eb8790...` TASK-021 amendment blob: `e12c98c9c3ab8cb39b1358c29761714f8506889c`

The candidate remained unchanged and clean; the full verification was rerun with the correct blob-identity assertion.

### Final unchanged-candidate RELEASE_FULL

Final result on candidate `6eb87904374f1fb3034db572e3773238e4ed0e14`, distribution tree `9d1d06916b944f8169477c220777ee5874e689bf`:

**`RELEASE_FULL PASS 73/73`**

Observed supporting results:

- ChatGPT launcher: **4,487** Unicode characters
- Claude launcher: **4,486** Unicode characters
- shared marker bodies: byte-identical
- pressure scenarios: **1–171**, exactly once each
- mockup templates: **22**, all stamped Framework `1.6.0`
- changed files from pre-TASK-022 base: **37**
- Framework change scope: Markdown/YAML only; no graph/runtime executable artifacts
- `git diff --check`: clean
- candidate working tree before RELEASE_FULL: clean
- historical TASK-021 amendment Git blob unchanged from base

The 73 checks cover release identity, amendment/SKILL alignment, namespace, canonical object homes, exact relation vocabulary/states, immutable endpoint identity, late binding, authority separation, AI-ControlTower/OpenViking derived/rebuildable boundary, Brownfield migration, merge/split reassessment, DRIFT/CONFLICT/MIG reuse, templates/index/manifest/migration propagation, launcher invariants, scenario uniqueness, reserved slots, historical amendment preservation, documentation-only scope, and clean candidate state.

## Non-goals preserved

No OpenViking runtime/deployment, graph database selection/provisioning, Graphify integration, crawler, watcher, webhook, scheduler, sync daemon, MCP graph service, validator/CLI, automatic Project discovery/promotion, or automatic conflict resolution was implemented.

## Publication state

`commit ≠ push` remains binding. This evidence records local verified completion only. Remote publication state at evidence creation: **`NOT_PUSHED`**.
