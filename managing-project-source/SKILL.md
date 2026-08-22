---
name: managing-project-source
description: Use when creating, adopting, importing, updating, reviewing, handing off, or exporting a Project Source; when a project needs consistent governance, naming, source-of-truth handling, continuation context, project-management control, or technical/install documentation.
---

# Managing Project Source

## Overview

Maintain a consistent `Project-Source/` governance layer. Make **current truth, current authority, Project health, and exact next action** explicit without inventing facts.

Current distribution: **Framework 1.2.5 / Schema 1.0.0**.

ProjectFramework is **conceptual governance/planning first**. Technical and integrity requirements are semantic contracts. **Do not expand Tech Stack, installation, Docker, governance, or integrity work into application code, Dockerfile/Compose, scripts, validator/CLI, CI/CD, scheduler, background automation, or other implementation unless the user explicitly requests a separate implementation scope.**

## Required References

Before creating or materially changing Project Source, read:

- `FRAMEWORK-RELEASE.yaml` for current distribution identity/bootstrap policy
- `references/framework-governance-amendment-260822-1835.md`
- `references/framework-governance-amendment-260822-1424.md`
- `references/framework-governance-amendment-260821-1934.md`
- `references/framework-governance-amendment-260821-1505.md` (historical approved amendment)
- `references/framework-governance-amendment-260821-1254.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-1142.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-1024.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0821.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0735.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0707.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0646.md` (historical approved amendment)
- `references/framework-governance-amendment-260814-0808.md` (historical approved amendment)
- `references/core-governance-rules.md`
- `templates/00-project-source-framework.md`
- `templates/core-document-skeletons.md`
- `templates/project-source-mockup/README.md`

Historical spec/design files are rationale only. Latest Framework amendment wins on conflict.

## Platform Project Bootstrap Entrypoints

Official platform launchers:

- `CHATGPT-PROJECT-INSTRUCTIONS.md`
- `CLAUDE-PROJECT-INSTRUCTIONS.md`

Their text between `PROJECTFRAMEWORK-SHARED-CONTRACT:START` and `PROJECTFRAMEWORK-SHARED-CONTRACT:END` MUST remain byte-identical. Platform wrappers may differ only in placement instructions. Launchers are bootstrap/continuation helpers, never a competing governance root.

If active local `FRAMEWORK-001` exists, local pinned Project Source is authoritative. NEW Project bootstrap begins from canonical repository `main`. Exact Git tag/SHA and branch protection are optional assurance, not normal-use prerequisites.

## Framework 1.2.4 Project Location Binding

For initialized Projects, active local `FRAMEWORK-001` is the canonical home of **Project Location Binding**. Resolve it before Material GitHub/Google Drive work. The binding answers **where Project work belongs**; Authority/Risk rules independently answer **who may mutate what**.

Keep these concepts distinct:

```text
Repository Location Binding
  ≠ current work branch/worktree
  ≠ Canonical Integration Target
  ≠ Canonical Implementation Source
```

Do not add or infer `canonical_branch` from Location Binding. Framework `1.2.2` Canonical Integration Target/Base Freshness and Framework `1.2.3` Canonical Implementation Source/Runtime Authority remain independently authoritative.

GitHub and Drive each resolve to exactly one state:

```text
BOUND
NOT_APPLICABLE
VERIFICATION_REQUIRED
```

Operational rules:

1. `BOUND` requires durable routing identity: GitHub owner/repository or canonical repository URL; Drive project-root folder ID or canonical folder URL. Display names, Drive text paths, recent activity, chat memory, ranking, and discovery hits do not establish authority by themselves.
2. `BOUND` → compare the intended Material target to the durable routing identity when possible; a material mismatch stops the affected mutation and is surfaced.
3. `VERIFICATION_REQUIRED` → discovery/read/search and candidate comparison may continue; Material mutation is blocked by default.
4. A User Explicit Instruction naming one exact target may authorize that one otherwise-permitted action; it does not persistently rewrite Root Governance or promote the binding to `BOUND`.
5. `NOT_APPLICABLE` → no Material Project work through that connector until an explicitly approved binding/scope revision.
6. Persistent binding change → User Explicit Approval + governed `FRAMEWORK-001` revision/validate/promote/supersede/archive flow. Connector discovery, recent activity, or search ranking never transfers Project authority.
7. `03`/`09` may reference the active root binding; they do not keep independent authoritative repository/folder copies.
8. Project-specific repository/Drive/progress pointers belong in local `FRAMEWORK-001`, not platform launchers.

GREENFIELD has no active local binding. Use read-only candidate discovery as needed → include proposed GitHub/Drive states and durable identities in Preview → obtain explicit approval → first Material Project-Source write creates active `00 / FRAMEWORK-001` with the approved binding → subsequent Material connector work resolves that active binding. Unresolved applicable systems remain `VERIFICATION_REQUIRED` and fail-closed for Material mutation.

## Framework 1.2.5 Agent Continuity, Progressive Verification, and Local Workspace Binding

Framework `1.2.5` composes with `1.2.1–1.2.4` and adds no new slot, Stable-ID family, lifecycle state, Git freshness state, or authority family.

### Local Workspace Binding

Before Material local/MCP work, resolve the applicable environment-scoped **Local Workspace Binding** from active `FRAMEWORK-001`. Reuse exactly `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED`. `BOUND` requires a verified/user-confirmed absolute path for that environment; for Git-backed work, cross-check repository identity when practical. `VERIFICATION_REQUIRED` allows read/list/search/inspect needed to resolve the workspace but blocks Material mutation by default. `NOT_APPLICABLE` blocks Material local scope. MCP `workspaceId`, editor handles, active/recent workspace lists, and similar tool identifiers are routing evidence only, not canonical Project identity.

Keep the separation explicit:

```text
Repository Location Binding
  ≠ Local Workspace Binding
  ≠ current branch/worktree
  ≠ Canonical Integration Target
  ≠ Canonical Implementation Source
  ≠ Runtime Location
```

A one-off exact local target instruction is action-specific and does not persistently rewrite Root Governance. Persistent Local Workspace Binding changes require User Explicit Approval plus `FRAMEWORK-001` revision/validate/promote/supersede/archive.

### Verified Task Completion Checkpoint

For a Material Task / `ACT-*` that materially mutates a Git-backed Canonical Implementation Source or another authoritative repository artifact, durable `DONE` requires a **Verified Task Completion Checkpoint**: affected/risk-appropriate verification passed; required completed state is represented by observed Git commit(s); no required completed result remains only uncommitted; remaining working-tree state is understood. Read-only/no-mutation Tasks require no synthetic commit. `WIP commit ≠ Task DONE`. One Task may use multiple commits. **commit ≠ push**; remote publication remains a separate shared-state/authority action.

### Progressive Verification and Evidence Reuse

Choose the minimum sufficient verification from changed scope → affected dependencies/invariants → `R0 / R1 / R2 / R3` risk. Operational labels are:

```text
TASK_LOCAL_FAST
CHECKPOINT_INTEGRITY
RELEASE_FULL
INTEGRATION_GATE
```

These are workflow vocabulary only. `TASK_LOCAL_FAST` verifies affected scope before Task completion. `CHECKPOINT_INTEGRITY` verifies durable continuation; **Logical Checkpoint ≠ RELEASE_FULL**. `RELEASE_FULL` runs once on the completed release/candidate state. `INTEGRATION_GATE` re-resolves Canonical Integration Target/Base Freshness and prior evidence validity. Fresh state-bound evidence may be reused while candidate/dependency/target assumptions remain materially unchanged; selectively invalidate affected evidence when assumptions change, and escalate when impact cannot be bounded safely. Exact fast-forward to an already verified candidate normally needs resulting-state confirmation rather than an unconditional full rerun.

### Response Close Completeness Gate

Before every Framework-governed assistant response emit, run the lightweight **Response Close Completeness Gate** on the assistant final-response representation: two mandatory headings exactly once and in order; exactly one `[Next Action]:`, `[Chat]:`, `[Reason]:`, `[Required Read]:` as separate Markdown paragraphs in that order; lifecycle-consistent `[Chat]`; and nothing after `[Required Read]`. Missing/duplicate/malformed/out-of-order/contradictory close content is incomplete and must be corrected before emit. Do not claim visibility into downstream app rendering; a user-visible omission is regression evidence while its generation/transport/rendering layer remains unverified unless independently observed.

## Framework 1.2.0 Namespace and Routing

Mandatory core remains `00–05` and `09–17`; `06–08` remain conditional; `18–19` remain reserved.

Framework `1.2.0` standardizes:

```text
40 Technical Design               CONDITIONAL
60 Deployment Plan                CONDITIONAL
90 General / Special Governance Extension anchor
91 Project Management Control     CONDITIONAL / STANDARD IN 1.2.0+
92–99 Project-specific / Governance Extension
```

When active, route:

```text
40 → Tech Stack / components / source structure / workspace / config / runtime / Source-Docker technical blueprint
60 → installation / startup-shutdown / verification / diagnostics / runtime-persistence-recreation / upgrade-rollback / backup-restore / cleanup
91 → RISK-* / ASM-* / MS-* / OUT-* / DEP-* / CR-* / GATE-*
```

Do not create conditional documents merely to make the Project tree look complete.

## Canonical Project-Management Homes

```text
RISK-* → 91 Project Management Control
ASM-*  → 91 Project Management Control
MS-*   → 91 Project Management Control
OUT-*  → 91 Project Management Control
DEP-*  → 91 Project Management Control
CR-*   → 91 Project Management Control
GATE-* → 91 Project Management Control
```

Existing canonical homes remain unchanged for `DEC-*`, `REQ-*`, `ISS-*`, `DRIFT-*`, `CONFLICT-*`, `CHG-*`, actors, authority, evidence, actions, migrations, and secret references.

Key distinctions:

```text
RISK-* future uncertainty ≠ ISS-* materialized/current problem
ACT DONE ≠ MS REACHED ≠ OUT ACHIEVED
DEP AVAILABLE ≠ DEP SATISFIED
CR-* proposed/material change control ≠ CHG-* applied/observed history
Responsibility ≠ Authority
```

Risk materialization preserves the Risk and links an Issue. Accepted material Risk records applicable decision/authority and review trigger.

## Project Health and Review Cadence

`03 Current State` may summarize applicable dimensions:

```text
Scope
Progress / Schedule
Risk
Quality / Validation
Dependencies
Authority
Knowledge
Readiness
Technical / Deployment when applicable
```

Use `GREEN / AMBER / RED / UNKNOWN`, each with Reason, supporting Stable IDs/evidence, Owner, Last Reviewed, Next Review/Trigger. Omit non-applicable optional dimensions rather than marking them GREEN. Do not invent an opaque automatic aggregate score.

Review Cadence modes:

```text
TIME_BASED
EVENT_BASED
```

Cadence may cover Current State, Risk, Assumption, Milestone/Outcome, Decision Revalidation, Technical Design, Deployment Readiness, and Handoff Refresh. Framework semantics do not create a scheduler/reminder runtime.

## Decision Revalidation

`DEC-*` remains canonical in `04`. When material, record:

```text
Validity Basis
Review Trigger
Review By
Last Revalidated
Revalidation Status
Revalidation Evidence
```

Use `NOT_DUE / REVIEW_DUE / REVALIDATED / SUPERSEDED`. Revalidate when the stated basis changes, including invalidated assumptions, changed dependencies/requirements/Tech Stack/deployment mode, approved material Change Request, external change, review date, or contradicting runtime evidence.

## Responsibility and Authority

`11 Actor Registry` may contain scope-keyed `Responsible / Accountable / Consulted / Informed` mapping. It grants no authorization. Actual permission remains in `12 Authorization Registry` through `AUTH-* / DEL-*` plus risk/approval rules.

## Knowledge Debt

Material stale/missing operational knowledge remains canonical in `08 Open Issues`:

```text
ISS-* with issue_type: KNOWLEDGE_DEBT
```

Runtime success does not erase Knowledge Debt. If material it may degrade Knowledge/Readiness and makes `08` applicable if no active `08` exists.

## Technical Blueprint Boundary

### `40 Technical Design`

Use when deeper technical detail is needed beyond `06 Architecture`. Document material Tech Stack entries with Technology, Role/Responsibility, Version/Supported Range, Required/Optional state, reason/Decision reference, component usage, operational dependency, lifecycle/support constraint, replacement boundary, and epistemic/verification state.

May also document component interfaces, source-area responsibilities, **Development Workspace Contract**, Configuration Contract, Runtime Requirements, deployment-mode architecture, and parity/variance.

When material, Development Workspace Contract resolves Canonical Implementation Source, repository/source identity, workspace type/location/durability, Human/Agent edit location, execution environment, Source-to-Runtime Mapping, dependency isolation, Runtime Mutability Boundary, Persistent-State Boundary, and verification/drift notes.

Descriptive workspace/mapping labels such as `LOCAL_WORKSPACE`, `GIT_WORKTREE`, `REMOTE_DURABLE_WORKSPACE`, `DEV_CONTAINER_DURABLE_WORKSPACE`, `DIRECT_EXECUTION`, `BIND_MOUNT`, `WORKSPACE_VOLUME`, `IMAGE_OR_ARTIFACT_BUILD`, and `REMOTE_SYNC` are blueprint vocabulary only; they are not Project states or Stable-ID families.

### `60 Deployment Plan`

Use when install/deployment/operation is in scope. Deployment support vocabulary:

```text
SOURCE_ONLY
DOCKER_ONLY
SOURCE_AND_DOCKER
NOT_APPLICABLE
```

For `SOURCE_AND_DOCKER`, preserve one declared application/configuration/data/security/persistence contract. Intentional differences are explicit Deployment Mode Variance; unexpected mismatch is `DRIFT-*`.

`60` may document prerequisites, Source installation, Docker installation, configuration/secret refs, deployment source/artifact acquisition, Source-to-Runtime Mapping, Runtime Mutability Expectation, Persistent-State Boundary, Data/Storage Authority, Replacement/Recreation Expectation, development/production mapping differences, data initialization, start/stop, health verification, logs, upgrade, rollback, backup/restore, cleanup, troubleshooting. A real Project may include concrete commands/paths only when verified as actual Project truth.

**Planning is not implementation authorization:** a request to define Tech Stack, installation, Docker topology, ports/volumes, workspace mapping, persistence, or verification does not authorize creation of source code, Dockerfile, Compose/Kubernetes/Helm, package manifests, install scripts, CI, or automation.

## Development Workspace and Runtime Authority

Apply this contract when implementation exists and workspace/runtime distinction is material. It composes with, but does not replace, Framework 1.2.2 Git Base Freshness.

Operational sequence:

```text
resolve Canonical Implementation Source / durable workspace
→ if Git branch/worktree integration is in scope, apply existing Base Freshness contract
→ mutate canonical durable source / valid worktree
→ execute/test through declared Source-to-Runtime Mapping
→ compare Implementation Truth with Runtime Truth when material
→ DRIFT-* for mismatch that should align
→ ensure required-survival state has declared persistent authority/mechanism
→ verify resulting Implementation/Runtime state appropriate to risk
```

Required behavior:

1. **Canonical Implementation Source:** identify the durable declared source location whose verified state determines affected `IMPLEMENTATION` Truth. For Git-backed Projects this is normally verified Git/source tree under the Project's repository/workspace contract.
2. **Durability, not host-only:** source must be durable enough for the Project's declared development/recovery lifecycle. Host Git repo, worktree, remote/VM durable workspace, and Dev Container backed by durable bind/workspace storage are all valid when declared. Do not require a physical host folder merely because development is containerized.
3. **Runtime Authority:** fresh runtime observation determines `RUNTIME` Truth only. Editing/running code in an otherwise disposable runtime does not silently transfer Implementation authority.
4. **Runtime-only hotfix:** diagnosis/emergency runtime edits may be observed as runtime state, but canonical implementation completion requires accepted intent to be transferred through the governed change path into Canonical Implementation Source and reverified.
5. **DRIFT reuse:** if canonical implementation and runtime should align but differ materially, use existing `DRIFT-*`; do not invent a workspace/runtime drift family.
6. **Persistence boundary:** state required by REQ/DEC/Technical/Deployment contracts to survive expected runtime replacement must have a declared persistent-state authority/mechanism. Rebuildable cache/temp/scratch state may remain ephemeral when survival is not required.
7. **Production mapping:** production source mounts and image/artifact deployment are evaluated against declared lifecycle, recovery, authority, security, and persistence requirements. Do not blanket-forbid source mounts or universally require immutable images.
8. **Docker optional:** this contract applies equally to native/non-Docker Projects. Do not require Docker merely because software development exists.
9. **Git semantics unchanged:** workspace governance never replaces `FRESH / STALE_NON_SEMANTIC / STALE_SEMANTIC / UNKNOWN`, `BASE_STALE`, `REBASE_REQUIRED`, `FORWARD_PORT_REQUIRED`, `STACKED_WORK`, or the Pre-Merge Base Freshness Gate.

## Materialized Current State Invariant

Every referenced current Stable ID must resolve from Current Reconstructable Snapshot to current authoritative semantics without archive traversal. Archive is Historical Truth only. Delta-only shorthand cannot substitute for current payload.

This applies equally to current `DEC-*`, `REQ-*`, and `RISK/ASM/MS/OUT/DEP/CR/GATE` records. Active `40`, `60`, `91` required to interpret current truth belong in `14 Manifest` and `CURRENT` export.

## Migration Safety

Existing Projects never auto-upgrade.

For Framework `1.2.0` migration:

- if Brownfield slot `91` is already occupied, open `MIG-*`, preserve identity/history/references, relocate only with approval, then activate standard `91` when applicable;
- never automatically convert old prose into new management Stable IDs; promotion requires sufficient current semantics, status, ownership, and evidence/epistemic state;
- preserve local Project-specific rules unless explicitly resolved otherwise.

Framework `1.2.3` migration does not invent workspace topology. Unknown Canonical Implementation Source, workspace durability, Source-to-Runtime Mapping, or persistence boundary remains explicit `UNKNOWN / VERIFICATION_REQUIRED` until verified from actual Project sources/runtime.

## Maintained Starter Representation

`templates/project-source-mockup/` is the **single maintained concrete starter representation** for the current Framework distribution. It covers the governed semantic namespace and current starter surfaces used during GREENFIELD bootstrap.

Do not maintain a second full Project Source example/template tree in the current distribution. Historical composition examples remain available through Git history; current bootstrap and maintenance use Core Governance, the root `00` template, core skeletons, and `templates/project-source-mockup/`.

## MCP Material Persistence and Chat Lifecycle

Connector activity is classified as **Material Project Work** or **Transient MCP Activity**. Chat is temporary interaction/execution state, not canonical Project memory merely because MCP/connectors are available.

Operational sequence:

1. Inspect/read/search as needed; keep intermediate connector detail transient.
2. Classify the outcome as Material Project Work or Transient MCP Activity.
3. If Material, determine the source-native canonical owner.
4. Batch related connector activity until a Logical Checkpoint.
5. Persist current usable state/pointers once at the checkpoint; CHECKPOINT_INTEGRITY verifies continuation state and only affected cross-surface integrity, not full release regression by default.
6. If persistence fails, report `PERSISTENCE_PENDING` and identify what remains unpersisted.
7. Return a compact Chat result; do not replay the connector transcript.
8. Recommend exactly `CONTINUE_CURRENT_CHAT` or `START_NEW_CHAT`.
9. Recommend `START_NEW_CHAT` only after the persistence gate passes: durable current state, pending/blocker state, Exact Next Action, and Required Read location exist outside Chat.
10. If `[Next Action]` is exactly `ไม่มีขั้นตอนถัดไป`, `[Chat]` MUST be `START_NEW_CHAT`.
11. `CONTINUE_CURRENT_CHAT` requires one concrete Next Action and MUST NOT pair with `ไม่มีขั้นตอนถัดไป`.
12. `PERSISTENCE_PENDING` requires `CONTINUE_CURRENT_CHAT` plus one concrete persistence/recovery Next Action; it cannot pair with `START_NEW_CHAT` or `ไม่มีขั้นตอนถัดไป`.
13. `START_NEW_CHAT` may carry a concrete Next Action when state is durably persisted and continuation is safe from Required Read locations.

Mandatory Framework response close:

```text
### ทำอะไรไป?

<concise statement of what was done or determined>

### และถัดไปคืออะไร?

[Next Action]: <one exact next action or ไม่มีขั้นตอนถัดไป>

[Chat]: CONTINUE_CURRENT_CHAT | START_NEW_CHAT

[Reason]: <concise reason>

[Required Read]: <canonical locations or ไม่มี>
```

The four bracketed fields are separate Markdown paragraphs. Canonical lifecycle tokens stay unescaped; Markdown escaping is display-only.

GitHub routing examples:

```text
03 → current state / current phase / current blocker
04 → DEC-* current decision state
05 → REQ-* current requirement state
08 → ISS-* / DRIFT-* / CONFLICT-* / Knowledge Debt
09 → continuation contract and exact next action
10 → applied/observed historical change
13 → material evidence references
15 → ACT-* current action state
91 → RISK-* / ASM-* / MS-* / OUT-* / DEP-* / CR-* / GATE-*
```

If the natural owner is a normal repository artifact outside Project Source (for example implementation code, README, config, or an approved plan), persist there rather than duplicating the whole state into Project Source. Cross-system GitHub/Drive continuation uses pointers to each source-native owner.

For Google Drive, update the existing designated Project progress `.md` when one already exists. Only when no designated progress Markdown exists and durable continuation state is required, use one stable `PROJECT-PROGRESS.md` as a continuation cache. It references authoritative Drive artifacts and MUST NOT become a duplicate source of truth or MCP transcript.

Do not persist raw tool payloads, long search results, full diffs, repetitive intermediate state, or private intermediate reasoning merely for audit convenience. `09 Handoff` remains a continuation contract, not an execution log. A new chat must be able to continue from persisted state and Required Read pointers without the old transcript.

## Git Base Freshness and Worktree/Branch Integration

Apply this section only when Git branches/worktrees are actually in scope. It operationalizes the binding Core Governance contract; it does not replace it.

Operational sequence:

```text
resolve verified Canonical Integration Target
→ fresh-read/fetch current target
→ classify Independent Work vs STACKED_WORK
→ create work from verified current base
→ check Base Freshness at material checkpoints
→ classify STALE_NON_SEMANTIC vs STALE_SEMANTIC
→ BASE_STALE while unresolved
→ update/rebase appropriately OR FORWARD_PORT_REQUIRED
→ re-resolve target head immediately before acceptance/merge
```

Required behavior:

1. **Independent Work:** create the new branch/worktree from current observed canonical target, not from whichever feature branch is checked out. For ProjectFramework use repository `main` / local `origin/main` semantics. Never assume local `main` is current without a fresh target check.
2. **STACKED_WORK:** feature-on-feature ancestry is allowed only when deliberate and discoverable. Preserve parent branch/ref or commit, dependency reason, what becomes invalid if parent changes, and expected integration order. Material parent movement requires child re-evaluation.
3. **Base Snapshot:** when material, record only observed repository/ref/SHA/version/time values. Never fabricate Git identity merely to complete metadata.
4. **Checkpoint:** re-evaluate base before new independent work, before a new material implementation phase when upstream may have moved, before material PR/integration updates, and immediately before merge if target head moved after review.
5. **STALE_NON_SEMANTIC:** mark the work `BASE_STALE` until its base is updated appropriately and affected verification passes. Use `REBASE_REQUIRED` for private/rewritable work when appropriate; for shared/public branches, prefer a history-preserving merge/update rather than rewriting published history. Return to `FRESH` only after the update and affected verification succeed.
6. **STALE_SEMANTIC:** mark `BASE_STALE`, stop affected new implementation scope, inspect changed Framework/governance/schema/authority/REQ/DEC/interface/contracts, and use `FORWARD_PORT_REQUIRED` by default.
7. **Forward-Port:** create a clean branch/worktree from the current target, treat the stale branch as source material/evidence, and carry only still-valid accepted changes. Cherry-pick only when boundaries are clean; otherwise re-implement accepted intent on the current base. Exclude temporary staging/transport artifacts, obsolete workflow/version metadata, superseded assumptions, and unrelated experiments.
8. **Pre-Merge Base Freshness Gate:** re-resolve current target head and classify `FRESH | STALE_NON_SEMANTIC | STALE_SEMANTIC | UNKNOWN`. `UNKNOWN` or unresolved semantic drift blocks affected acceptance.
9. `git conflict = 0`, `mergeable = true`, or successful rebase is not semantic approval. **Mergeable ≠ Acceptable.**
10. Use existing `DRIFT-* / CONFLICT-* / MIG-* / CR-*` only when base staleness becomes material Project truth; do not invent a parallel Stable-ID family.

Commit count alone never decides semantic freshness. One Root Governance change can matter more than many unrelated commits.

### Framework 1.2.5 Integration Evidence Behavior

Immediately before integration, `INTEGRATION_GATE` re-resolves the current Canonical Integration Target, applies Framework `1.2.2` Base Freshness, and checks whether prior `RELEASE_FULL`/Task evidence remains valid. Reuse fresh evidence when its bound state/assumptions remain unchanged; selectively rerun invalidated/newly affected checks. Candidate/tree changes, semantic/unknown target movement, conflict resolution, rebase result, merge-time edits, or unbounded impact require affected/full reverification. `Mergeable ≠ Acceptable` remains binding.

## Workflow

1. Classify `GREENFIELD`, `BROWNFIELD`, or `IMPORT` and detect whether valid local Project Source already exists.
2. NEW Project: read canonical `main` in governed order: README → descriptor → SKILL → latest amendment → Core Governance → Framework template → skeletons → mockup.
3. Resolve explicit `FAST/GRILL`; otherwise `ADAPTIVE`.
4. Confirm active `FRAMEWORK-001`; if missing in an existing Project, stop affected work and propose governed repair.
5. Existing Project: read `00 → 01 → 03`, follow `01` routing, preserve local pin.
6. Before Material GitHub/Drive work in an initialized Project, resolve the applicable Project Location Binding from active `FRAMEWORK-001`; enforce `BOUND / NOT_APPLICABLE / VERIFICATION_REQUIRED` fail-closed routing and do not infer authority from recency/ranking/chat memory.
7. Before Material local/MCP work, resolve the environment-scoped Local Workspace Binding; tool/MCP workspace IDs are evidence only and unresolved applicable local execution is fail-closed.
8. For each Material Task, derive minimum sufficient verification from affected scope/dependencies/risk; a Git-backed Material Task becomes durably DONE only after a Verified Task Completion Checkpoint.
9. At Logical Checkpoints use CHECKPOINT_INTEGRITY, not RELEASE_FULL by default; run RELEASE_FULL once on a completed release/candidate and reuse valid state-bound evidence until invalidated.
10. Before integration run INTEGRATION_GATE with current Base Freshness + evidence-validity review.
11. Before every governed response emit run Response Close Completeness Gate.
12. Inspect accessible sources before asking; do not ask for facts that can be verified.
13. Classify material claims by Truth Domain, Epistemic Status, Freshness; use DRIFT/CONFLICT instead of silent reconciliation.
14. Initial creation/major structural migration requires Preview → explicit user approval → write; GREENFIELD Preview includes proposed Project Location Binding states/identities.
15. For GREENFIELD create mandatory `00–05`, `09–17`; evaluate `06–08`, `40`, `60`, `91`; keep `18–19` reserved.
16. Route management objects to `91`; technical blueprint to `40`; install/operations to `60` when applicable.
17. Pin imported Framework/Schema locally; upgrades use `MIG-*` and approval; Framework `1.2.5` migration never invents repository/Drive/local-workspace identities, commit provenance, verification evidence, or `canonical_branch`.
18. If exact Git provenance is observed/material, record consistently in `00`/`14`; otherwise never fabricate it.
19. If Git branch/worktree integration is in scope, resolve the canonical integration target, classify Independent vs `STACKED_WORK`, enforce Base Freshness checkpoints, and route semantic staleness to Forward-Port before integration.
20. If implementation/runtime mapping is material, resolve Canonical Implementation Source, workspace durability, Source-to-Runtime Mapping, Runtime Mutability Boundary, and required persistent-state authority before implementation-completion/readiness claims.
21. Verify referenced current Stable IDs resolve without archive traversal before readiness/CURRENT export claims.
22. Never store actual secrets; use `SECRET-*` metadata references only.
23. Preserve history and finish with completion/readiness/exact-next-action summary using the mandatory bracketed response close; enforce Chat Closure Consistency and Response Close Completeness Gate.

## Quick Reference

| Situation | Required behavior |
|---|---|
| New Project | canonical main → Preview → approval → mandatory core; conditionals only when applicable |
| Project-management control | use `91`; canonical `RISK/ASM/MS/OUT/DEP/CR/GATE` |
| Technical design | use `40` when deeper than `06`; include workspace contract when material; do not silently code |
| Install/deployment | use `60`; document source/runtime/persistence/recreation and resulting-state verification when material |
| Source + Docker | shared contract + explicit variance; unexpected mismatch = DRIFT |
| Runtime-only hotfix | Runtime Truth only; preserve accepted intent through governed update to Canonical Implementation Source before canonical completion |
| Host Git/worktree + bind-mounted Docker | Git/worktree = Canonical Implementation Source; Docker = execution/runtime environment |
| Durable Dev Container workspace | valid when source identity/durability/recovery are declared; host-folder source not required |
| Required-survival runtime state | declare persistent-state authority/mechanism compatible with expected recreation |
| Rebuildable cache/temp state | may remain ephemeral when no survival requirement exists |
| Production source mount | evaluate declared lifecycle/recovery/authority/security/persistence contract; no blanket prohibition |
| Non-Docker software Project | apply workspace/runtime authority semantics without requiring Docker |
| Project Health | dimensional `GREEN/AMBER/RED/UNKNOWN` in `03`, evidence-backed |
| Decision changed basis | mark/review revalidation in `04` |
| Responsibility | mapping in `11`; permission still comes from `12` |
| Knowledge Debt | `ISS-* issue_type: KNOWLEDGE_DEBT` in `08` |
| Existing custom slot 91 | `MIG-*`; never overwrite; approved relocation first |
| Initialized Project + Material GitHub/Drive work | resolve active `FRAMEWORK-001` Project Location Binding before mutation |
| `BOUND` connector | require durable routing identity and compare intended Material target when possible |
| `VERIFICATION_REQUIRED` connector | discovery/read-only allowed; Material mutation blocked by default |
| `NOT_APPLICABLE` connector | Material Project work blocked until approved Root Governance binding/scope revision |
| One-off exact target instruction | may govern that action only; never silently persist as new binding authority |
| Persistent binding change | User Explicit Approval + governed `FRAMEWORK-001` revision/promotion |
| Repository binding | never substitute for current branch/worktree, Canonical Integration Target, or Canonical Implementation Source |
| `ไม่มีขั้นตอนถัดไป` | pair with `START_NEW_CHAT` |
| `CONTINUE_CURRENT_CHAT` | requires one concrete Next Action |
| `PERSISTENCE_PENDING` | `CONTINUE_CURRENT_CHAT` + concrete persistence/recovery Next Action |
| Old free text | never auto-promote into new Stable IDs |
| Exact Git provenance unavailable | normal bootstrap continues if canonical source accessible; never fabricate |
| Independent Git worktree/branch | fresh canonical target first; do not inherit current feature branch by default |
| Feature depends on unmerged feature | explicit `STACKED_WORK` with parent/dependency/integration order |
| `STALE_NON_SEMANTIC` base | `BASE_STALE` → update safely; rebase private/rewritable or preserve shared history → reverify → `FRESH` |
| `STALE_SEMANTIC` base | `BASE_STALE` → reassess → `FORWARD_PORT_REQUIRED` into clean current-base work |
| Pre-merge Git acceptance | re-resolve current target head; `Mergeable ≠ Acceptable` |
| Material MCP work | batch to Logical Checkpoint; persist usable state/pointers to source-native owner; compact Chat result |
| Persistence failure / chat switch | `PERSISTENCE_PENDING` → `CONTINUE_CURRENT_CHAT`; `START_NEW_CHAT` only after durable continuation state exists |
| Handoff | authority does not transfer |
| R2/R3 mutation | fresh authority + required postflight/evidence |

## Red Flags

- removing/bypassing/demoting `FRAMEWORK-001`;
- creating empty conditional `06–08`, `40`, `60`, `91` merely for completeness;
- materializing reserved `18–19`;
- storing `RISK/ASM/MS/OUT/DEP/CR/GATE` as authoritative current truth outside `91`;
- treating Action completion as Milestone/Outcome success;
- treating responsibility as authority;
- hiding material Knowledge Debt because runtime works;
- overwriting a Brownfield custom slot `91`;
- auto-promoting old prose into Stable IDs;
- Source/Docker divergence without declared variance or DRIFT;
- turning Tech Stack/install/Docker/workspace/persistence planning into unrequested source code/Dockerfile/Compose/scripts/CI/automation;
- claiming implementation DONE after editing only an otherwise disposable runtime;
- silently promoting a runtime hotfix into Implementation Truth;
- assuming every container filesystem is ephemeral without checking the declared workspace durability/source contract;
- requiring Canonical Implementation Source to live on a physical host filesystem;
- requiring Docker for all software/AI-assisted Projects;
- blanket-forbidding production source mounts or universally requiring immutable images;
- storing state that must survive expected recreation only in a disposable runtime layer while claiming recreation/readiness support;
- inventing `WORKSPACE_STALE`, `RUNTIME_STALE`, or another parallel freshness/Stable-ID family instead of reusing 1.2.2 and `DRIFT-*`;
- inferring Project GitHub/Drive authority from chat memory, recent activity, search ranking, display names, or another accessible Project instead of resolving active Project Location Binding;
- treating `VERIFICATION_REQUIRED` or `NOT_APPLICABLE` as permission for Material connector mutation;
- accepting `BOUND` without minimum durable routing identity;
- silently rewriting Project Location Binding from connector discovery or a one-off exact-target instruction;
- adding `canonical_branch` or other parallel Git branch authority to Location Binding;
- pairing `ไม่มีขั้นตอนถัดไป` with `CONTINUE_CURRENT_CHAT`, or `PERSISTENCE_PENDING` with `START_NEW_CHAT`;
- omitting one of `[Next Action] / [Chat] / [Reason] / [Required Read]` from the mandatory Framework response close;
- maintaining a second full Project Source example/template tree alongside `templates/project-source-mockup/` in the current distribution;
- creating unrelated Independent Work from the currently checked-out feature branch by default;
- assuming local `main` is current without verifying the canonical integration target;
- using commit count alone as proof of semantic staleness/freshness;
- continuing or merging a `STALE_SEMANTIC` branch merely because Git reports no conflict;
- treating `mergeable = true` as semantic acceptance;
- rewriting shared/public branch history merely to satisfy a rebase preference;
- hiding feature-on-feature ancestry instead of declaring `STACKED_WORK`;
- carrying temporary staging/transport or obsolete metadata into a Forward-Port merely to preserve branch history;
- merging after the canonical target moves materially without rechecking Base Freshness;
- reconstructing inaccessible Framework/project facts from memory;
- archive-dependent Current Truth;
- guessing facts/secrets/provenance;
- claiming completion without risk-appropriate verification.
