---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.8.0"
project_source_framework_version: "1.8.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_EXPLICIT_CONTINUOUS_APPROVAL_2026-08-29"
compatibility: "BACKWARD_COMPATIBLE_PERSISTENT_GOAL_COMMAND"
---

# Framework 1.8.0 Amendment — Persistent `[Goal]` Continuous Execution Command

Framework `1.8.0` preserves the TASK-038 `Framework-Source/` distribution-root semantics and all prior Framework behavior unless refined here. Project Source Schema remains `1.0.0`; release format remains `3`. This amendment registers `[Goal]` as a persistent, bounded Project command for continuous execution toward a user-authorized outcome across chat/session boundaries.

## 1. Command identity and authority boundary

The canonical registered command is:

```text
[Goal] : create/show/change/cancel a persistent outcome and its bounded continuous-execution authorization
```

Literal `[` and `]` are required. Registered-name matching inside the brackets is case-insensitive. Unbracketed uses of the word `goal` remain ordinary language and do not silently materialize persistent Project authority.

`[Goal]` records **bounded user authorization**. It is never Agent self-approval, never unlimited authorization, and never authority to override system/developer instructions, product safety policy, MCP/tool confirmation requirements, authentication/authorization enforced by external systems, or other mandatory platform controls.

Core invariant:

```text
Goal authorization ≠ unlimited authorization
```

Operational invariant:

```text
Do not request Framework-level approval again solely for an action already covered by the current valid Goal authorization.
```

## 2. Canonical object composition — no new Goal family

TASK-039 adds no `GOAL-*` Stable-ID family and no semantic slot. A persistent Goal composes existing canonical homes:

```text
[Goal] command  = user-facing interaction/workflow
OUT-* in 91     = intended Goal outcome + success criteria/evidence
AUTH-* in 12    = persistent user-granted Goal execution authority
ACT-* in 15     = executable work decomposition
ENV-* in 15     = session/task envelope derived from Goal AUTH-*
03              = current Goal status/progress/blocker summary
09              = continuation references only; authority_transfer: false
10 / 13         = material history/evidence when applicable
```

`Outcome ≠ Action ≠ Authority ≠ Handoff` remains binding. `ACT DONE ≠ OUT ACHIEVED` remains binding.

## 3. Persistent Goal lifecycle

A Goal-specific `OUT-*` uses:

```text
ACTIVE | BLOCKED | ACHIEVED | CANCELLED | SUPERSEDED
```

- `ACTIVE` — outcome remains valid and at least one safe in-scope action can proceed or is ready.
- `BLOCKED` — outcome remains desired, but a global blocker leaves no meaningful safe next action. It is non-terminal and may return to `ACTIVE` after fresh resolution.
- `ACHIEVED` — every declared success criterion is sufficiently evidenced or has an explicitly approved revision.
- `CANCELLED` — the user withdrew the Goal; future Goal-authorized execution stops immediately after control returns.
- `SUPERSEDED` — an explicitly approved replacement Goal supersedes this Goal while preserving history.

The related Goal `AUTH-*` remains the durable cross-chat authority basis and MUST terminate/revoke/supersede when the Goal reaches `ACHIEVED | CANCELLED | SUPERSEDED`, unless another independent valid authorization covers an action.

## 4. Default local-development authorization

Unless the user explicitly narrows the Goal, a persistent `[Goal]` MUST by default pre-authorize the normal local development workflow required to pursue the stated outcome within the governed Project target:

```text
read / inspect / research local Project sources
architecture/design
implementation planning
create/edit/move non-destructive in-scope Project files
tests / lint / typecheck / build / validation
debugging and corrective edits
local Git add / commit
Logical Checkpoints
required Project Source continuation/evidence updates
```

This grant remains bounded by Goal scope, applicable `REQ-*` / `DEC-*`, Root Governance, Risk ceiling, Project Location Binding, Canonical Integration Target/Base Freshness, Canonical Implementation Source, verification rules, and higher-level tool/platform controls.

A clearly covered Framework-level local operation MUST NOT be re-prompted solely for approval. The Agent continues to the next safe in-scope action and persists required checkpoints.

## 5. Push/publication is opt-in

`push` / remote publication is excluded by default. It is pre-authorized only when the Goal explicitly includes publish/push intent and the intended governed target is sufficiently identified or uniquely resolvable from active Project governance.

Before any Goal-authorized push, fresh-resolve repository identity, binding compatibility, branch/worktree, Canonical Integration Target/Base Freshness, remote target, verification/evidence validity, unrelated-work risk, and working-tree state.

A material target change, unresolved/contradictory binding, stale integration evidence, unrelated publication payload, or mandatory higher-level confirmation blocks the affected push. `commit ≠ push` remains binding.

## 6. Destructive actions are exact opt-in

Destructive actions are excluded by default. They may be pre-authorized only when the Goal explicitly identifies the destructive **operation + target**, including any required condition.

Such authorization is exact-scope only and MUST NOT be generalized to other branches, files, resources, data, environments, tags, histories, or state. Mandatory tool/platform confirmation remains binding.

## 7. Root Governance / Project Location Binding changes are exact opt-in

Root Governance or Project Location Binding mutation is excluded by default. It may be pre-authorized only when the Goal explicitly identifies the intended mutation and target.

Even when pre-authorized, the normal governed lifecycle remains mandatory:

```text
fresh active root
→ bounded candidate revision
→ validate
→ promote
→ supersede/archive prior revision
→ sync Index/Manifest/Change Log
→ verify resulting state
```

A broad Goal such as “finish the release” never implies permission to rewrite Project identity, repository/local/storage bindings, Root Governance invariants, or schema authority.

## 8. Secrets and external disclosure remain separate

A Goal may authorize use of governed `SECRET-*` references when otherwise permitted, but actual secret values MUST NOT be persisted or revealed in Goal records, Project Source, Handoff, Evidence, plans, logs, or exports.

External AI/provider disclosure is not implied by Goal execution authority. It remains governed by TASK-026 once adopted or by applicable explicit current disclosure authorization. Unknown or mixed-sensitivity outbound context fails closed for the affected disclosure action while independent safe local Goal work may continue.

## 9. ACT / ENV execution semantics

Goal work is decomposed into existing `ACT-*`; each Action retains `TODO | IN_PROGRESS | DONE | BLOCKED | CANCELLED` and the existing Verified Task Completion Checkpoint requirements.

An `ENV-*` may be created/refreshed from current valid Goal `AUTH-*` without new user approval only when the envelope is equal to or narrower than its parent authorization, remains bounded by session/task/time expiry, and preserves prohibited zones. `ENV-*` never expands parent `AUTH-*` and never represents a higher-level tool/platform confirmation as waived.

## 10. Cross-chat resume

A fresh chat/Agent resumes an active persistent Goal through canonical Project Source, never from chat memory:

```text
PROJECT-BOOTSTRAP.md
→ validate 00 / FRAMEWORK-001
→ 01
→ 03
→ 09 when continuation applies
→ active Goal OUT-* in 91
→ related current AUTH-* in 12
→ active/pending ACT-* and ENV-* in 15
→ fresh-check volatile prerequisites/bindings
→ continue the exact safe next action
```

`09 Handoff` carries pointers only and MUST retain `authority_transfer: false`. A stale Handoff pointer is repaired from canonical registries; Handoff itself never grants authority.

## 11. Partial versus global blockers

If one operation is unauthorized/blocked but independent in-scope work remains safe, block only the affected operation, surface/persist the blocker when material, and continue the independent safe Goal work without broad re-approval.

Move the Goal to `BLOCKED` only when a global prerequisite/authority/evidence conflict leaves no meaningful safe next action or when achievement requires an unresolved material change to accepted Project intent.

## 12. Governed intent cannot be rewritten for convenience

Goal authority authorizes execution toward the accepted outcome; it does not authorize silent changes to `REQ-*`, `DEC-*`, accepted Risk, architecture contracts, or other governed truth merely to make completion easier. Route any required material semantic change through its existing authority/governance process. Another compliant path may continue when available.

## 13. Multiple Goals, cancellation, and supersession

Multiple Goals may coexist only when compatible. A later Goal never wins by recency alone. Determine whether it is an independent compatible Goal, an explicit change, an explicit supersession, or a material conflict. Material conflicts use existing `CONFLICT-*` handling when applicable and fail closed for the conflicting scope.

Cancellation has immediate prospective effect: `OUT-* → CANCELLED`, dependent Goal `AUTH-*` is revoked/terminated, completed commits/evidence/history remain preserved, and no further Goal-authorized action occurs after control returns. Supersession preserves the old Goal/authorization history rather than silently rewriting it.

## 14. Goal achievement requires independent evidence

Completing all linked Actions never automatically proves the outcome. Before `OUT-* → ACHIEVED`, evaluate each declared success criterion against observed/resulting state and evidence, including residual blocker/risk when relevant.

```text
ACT DONE ≠ OUT ACHIEVED
```

For Git-backed development Goals, evidence may include completion commits, working-tree state, affected verification, `RELEASE_FULL` when required, Base Freshness/integration evidence, and remote publication evidence when publication is part of the Goal.

## 15. Status, Handoff, GREENFIELD, and Brownfield integration

`[Project Status]` surfaces active/blocked Goal `OUT-*`, status, success-criteria progress, related `AUTH-*` validity, current/next `ACT-*`, boundary inclusion flags, blockers, and continuation freshness without mutating Goal authority.

`09 Handoff` may reference active Goal `OUT-*`, `AUTH-*`, `ACT-*`, `ENV-*`, last authorization verification, next safe action, and blocker, but never duplicates or transfers the authority payload.

Framework `1.8.0` GREENFIELD starters include Goal semantics but MUST NOT create an active Goal, `OUT-*`, or Goal `AUTH-*` automatically. Brownfield upgrade MUST NOT synthesize a Goal from prior prose, backlog, Handoff, existing `OUT-*`, or historical “continue” instructions. Existing object records are preserved; persistent Goal semantics begin only through explicit `[Goal]` invocation/adoption under this contract.

## 16. Higher-level platform/tool boundary

ProjectFramework can remove redundant **Framework-level** approval prompts for operations already covered by valid Goal authority. It cannot waive or override system/developer instructions, product safety policy, MCP/tool confirmation rules, authentication, external-system authorization, platform capability limits, or mandatory user-interaction controls imposed above ProjectFramework.

A mandatory higher-level confirmation is reported as a platform/tool gate, not as evidence that the Project-level Goal authorization is absent.

## 17. Compatibility and non-goals

This amendment is a backward-compatible command/authorization semantic expansion inside Framework `1.8.0`; Schema remains `1.0.0`, release format remains `3`, existing semantic slots remain unchanged, and TASK-038 `Framework-Source/` remains the canonical distribution root.

No `GOAL-*` registry/family, new semantic slot, background autonomous agent, scheduler, watcher, daemon, external authorization service, secret store, CI/CD/deployment automation, provider-routing runtime, or bypass of product/tool safety controls is introduced.
