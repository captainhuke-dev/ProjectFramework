# ProjectFramework 2.0 → AI-ControlTower Merge Manifest

Date: `2026-09-05`
Manifest state: `SELF_REVIEWED / PRE_MERGE_GATE_PENDING`
Source Project: `ProjectFramework`
Source Project UUID: `00575e76-17ce-4dd3-ad24-377494a4a45b`
Source Repository: `https://github.com/captainhuke-dev/ProjectFramework.git`
Verified Last Stable 1.x baseline: `main@aae65796a8d4ad5f23323889b65b060bd36302c1`
Verified Framework-Source tree: `d5d04e4563157246872b1e02c791b94a6c564d95`
Target Project: `AI-ControlTower`
Target Project UUID: `2ab1b99a-901c-4159-87f1-953db0af5015`
Target Repository: `https://github.com/captainhuke-dev/ai-controltower.git`
Target `origin/main` observed during preparation: `5abcb8cbd2dde8d241ae74cf1f107721cd8b969a`
Target canonical Project Source path: `Project-Source/`
Target ProjectFramework 2.x canonical-development path after cutover promotion: `projectframework/`

## 1. Purpose

This manifest defines exactly what is preserved, copied, transformed, referenced, excluded, or later generated when ProjectFramework is merged into AI-ControlTower. It prevents a repository-level copy from becoming an accidental authority transfer, prevents ProjectFramework V1 Project Source from overwriting AI-ControlTower Project Source, and keeps runtime/software licensing separate from the public Protocol/Core lineage.

The manifest does **not** authorize the merge. It is an input to a later explicitly authorized cross-Project cutover.

## 2. Mapping Classes

Only these mapping classes are used:

```text
MOVE
= ownership/home moves to the named target canonical location at cutover; the source repository retains history/mirror representation but no longer owns 2.x development truth

TRANSFORM
= source semantics are intentionally re-expressed in a different 2.0 structure; transformation requires explicit verification and does not imply byte copy

RETAIN_HISTORY
= preserve immutable source bytes/history/provenance; do not make the retained copy/current reference a new governance authority

REFERENCE
= preserve an exact durable source pointer/commit/digest instead of copying the payload into the target active structure

DO_NOT_IMPORT
= content must not be copied into the target surface because it would duplicate authority, mix runtime boundaries, carry source-specific state, or otherwise be non-applicable

GENERATE_AS_PROJECTION
= rebuild/readable output is produced later from canonical 2.0 resources/contracts; the projection is not authority
```

## 3. Authority and Identity Rules

```text
AI-ControlTower project_uuid remains 2ab1b99a-901c-4159-87f1-953db0af5015
ProjectFramework source project_uuid remains 00575e76-17ce-4dd3-ad24-377494a4a45b as lineage/provenance
AI-ControlTower active FRAMEWORK-001 remains target Project root authority
ProjectFramework V1 FRAMEWORK-001 never becomes target Project root authority
ProjectFramework V1 Project Source = source Project history/migration provenance
AI-ControlTower Project Source = target Project governance authority
AI-ControlTower/projectframework/ = ProjectFramework 2.x development source only after cutover promotion
public ProjectFramework repository = one-way distribution mirror only after cutover promotion
```

No Stable ID is copied from source into a target canonical family merely because the spelling is unused. Cross-Project references carry source Project/repository/commit context. Target IDs are allocated from fresh target state.

## 4. Source → Target File/Tree Mapping

| Source surface | Class | Cutover-foundation target | Rule / acceptance |
|---|---|---|---|
| ProjectFramework Git commit graph through exact source cutover commit | RETAIN_HISTORY | AI-ControlTower Git ancestry via `-s ours --allow-unrelated-histories` bridge | Full source history must be reachable from target cutover branch/main; ancestry bridge changes no target tree bytes by itself |
| `Framework-Source/` at verified Framework 1.14 tree | RETAIN_HISTORY | `projectframework/migration/v1-baseline/Framework-Source/` | Copy exact source-cutover tree; `FRAMEWORK-RELEASE.yaml` remains `1.14.0 / 1.0.0 / format 3`; retained baseline is migration truth, not 2.0 active protocol |
| `Framework-Source/FRAMEWORK-RELEASE.yaml` | RETAIN_HISTORY | `projectframework/migration/v1-baseline/Framework-Source/FRAMEWORK-RELEASE.yaml` | Byte/content identity to source cutover commit required |
| `Framework-Source/SKILL.md` | RETAIN_HISTORY | `projectframework/migration/v1-baseline/Framework-Source/SKILL.md` | Historical/1.x migration baseline only |
| `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md` | RETAIN_HISTORY | same relative path under V1 baseline snapshot | Historical launcher baseline only; not automatically a 2.0 launcher |
| `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md` | RETAIN_HISTORY | same relative path under V1 baseline snapshot | Historical launcher baseline only |
| `Framework-Source/MIGRATION-NOTES.md` | RETAIN_HISTORY | same relative path under V1 baseline snapshot | Historical 1.x migration guidance, not 2.0 active migration registry |
| `Framework-Source/references/**` | RETAIN_HISTORY | same relative path under V1 baseline snapshot | Preserve normative 1.x provenance/history |
| `Framework-Source/templates/**` | RETAIN_HISTORY | same relative path under V1 baseline snapshot | Preserve 1.x starters for migration/conformance comparison |
| `Framework-Source/tests/**` | RETAIN_HISTORY | same relative path under V1 baseline snapshot | Preserve 1.x pressure scenarios as historical/conformance inputs; no executable product is created |
| V2 architecture spec `docs/superpowers/specs/2026-09-04-projectframework-2-controltower-architecture-design.md` | MOVE | `projectframework/migration/design/2026-09-04-projectframework-2-controltower-architecture-design.md` | Exact source-cutover version becomes canonical design provenance inside target; source copy remains mirror/history |
| Merge/cutover plan `docs/superpowers/plans/2026-09-05-projectframework-2-ai-controltower-migration.md` | MOVE | `projectframework/migration/2026-09-05-projectframework-2-ai-controltower-migration.md` | Exact source-cutover version copied into target migration provenance |
| This merge manifest | MOVE | `projectframework/migration/2026-09-05-projectframework-2-ai-controltower-merge-manifest.md` | Exact digest recorded in target Migration/Evidence before promotion |
| ProjectFramework `Project-Source/00` root | RETAIN_HISTORY | source Git ancestry only; optional exact references from target migration evidence | MUST NOT be copied as target `FRAMEWORK-001`; source root describes source Project only |
| ProjectFramework active `Project-Source/01–17`, `91` | RETAIN_HISTORY | source Git ancestry + qualified target migration references | MUST NOT replace AI-ControlTower active Project Source files |
| ProjectFramework `Project-Source/archive/**` | RETAIN_HISTORY | source Git ancestry | No bulk copy into AI-ControlTower `Project-Source/archive`; archive namespaces remain Project-specific |
| ProjectFramework `docs/superpowers/PROJECT-TASKS.md` | REFERENCE | target migration/evidence points to exact source cutover commit/path | Source Task lifecycle is not AI-ControlTower Task/Action authority |
| Framework 1.13/1.14 release evidence under `docs/superpowers/evidence/**` | REFERENCE | target Migration/Evidence refs to source repository/commit/path | Exact evidence remains reconstructable without duplicating target EVD IDs |
| Historical ProjectFramework specs/plans/evidence not needed for active cutover | RETAIN_HISTORY | source Git ancestry | Searchable through history; not copied into active target docs |
| ProjectFramework root `PROJECT-BOOTSTRAP.md` | RETAIN_HISTORY | source Git ancestry | Target bootstrap/root remains governed by AI-ControlTower; do not copy to target root |
| ProjectFramework root `README.md` | RETAIN_HISTORY | source Git ancestry | Do not replace target README by import |
| ProjectFramework `.github/**` | DO_NOT_IMPORT | none | Source repository workflow/config is not target workflow authority |
| ProjectFramework `.gitignore` or repository-local tooling config | DO_NOT_IMPORT | none | Target repository owns its own tooling/configuration |
| Any source runtime/application code | DO_NOT_IMPORT | none | ProjectFramework V1 verified release contains no intended runtime implementation; future runtime belongs outside Protocol/Core |

## 5. ProjectFramework 2.0 Structural Transformation Map

The cutover foundation does not implement these protocol contracts yet. It establishes their future canonical ownership under `AI-ControlTower/projectframework/` and assigns each source semantic domain to the correct 2.0 home.

| 1.x semantic input | Class | 2.0 canonical home after post-cutover implementation | Transformation rule |
|---|---|---|---|
| Core governance rules / `FRAMEWORK-001` semantics | TRANSFORM | `projectframework/protocol/` | Re-express provider-neutral governance/authority invariants; AI-ControlTower root Project Source remains separate target Project truth |
| Project Source document schema/slot semantics | TRANSFORM | `projectframework/schemas/` | Convert document-centric schema into Typed Governance Resources + Active Resource Registry + Human Views under Project Source Schema `2.0.0` |
| Current Task/Goal lifecycle semantics | TRANSFORM | `projectframework/workflows/` | Encode declarative workflows and state-domain separation; no generic `SET DONE` |
| Completion/change/approval operations | TRANSFORM | `projectframework/transitions/` | Encode named typed transitions, expected state version, idempotency, evidence/authority guards |
| Tool/provider boundaries | TRANSFORM | `projectframework/capabilities/` | Encode capability contracts independent of OpenViking/Graphify/NexusRAG/GitNexus/Serena/EMIF vendor identity |
| V1 migration rules/history | TRANSFORM | `projectframework/migration/` | Use side-by-side 1.x→2.0 candidate/validation/promotion model; retained 1.14 snapshot is migration input |
| Pressure scenarios / protocol acceptance behaviors | TRANSFORM | `projectframework/conformance/` | Produce declarative conformance scenarios/test vectors; executable tooling stays outside Protocol/Core |
| Current State / Handoff human readability | GENERATE_AS_PROJECTION | Project Source 2.0 Human Views | Views derive from typed resources/current checkpoint state and never outrank active resources |

No post-cutover transformation is considered complete merely because the 1.x file was copied into `migration/v1-baseline/`.

## 6. AI-ControlTower Project Source Reconciliation Map

AI-ControlTower current canonical Project Source observed at `origin/main@5abcb8cbd2dde8d241ae74cf1f107721cd8b969a` uses Framework `1.3.0` / Schema `1.0.0`. The target cutover must mutate only canonical owners through new revisions after a fresh re-read.

| Target owner | Class | Required cutover semantic change |
|---|---|---|
| `00 / FRAMEWORK-001` | REFERENCE by default | Preserve AI-ControlTower identity/bindings/root. Revise only if the fresh target Framework/Root contract explicitly requires a Root change; ProjectFramework import alone does not justify it |
| `01 Project Source Index` | TRANSFORM | Route new target Decision/Requirements/Architecture/Migration/Action/Evidence/current-state records and `projectframework/` canonical-development reference |
| `03 Current State` | TRANSFORM | Record cutover candidate/promotion phase, exact source/target commits, no runtime implementation, existing target Action states |
| `04 Decision Log` | TRANSFORM | Add target Decision approving ProjectFramework 2.x canonical-source/module architecture and explicit Control Tower→Control Plane reconciliation |
| `05 Requirements` | TRANSFORM | Add target requirements for history preservation, no dual authority, module/runtime boundary, one-way mirror, rollback, version/licensing gates |
| `06 Architecture` | TRANSFORM | Preserve CT-1 router/classifier constraint as bounded routing responsibility while explicitly adding ProjectFramework Protocol/Core + Control Plane runtime architecture; do not silently replace current architecture text |
| `07 Implementation Plan` | TRANSFORM | Route this merge/cutover foundation and subsequent independently authorized post-cutover streams |
| `09 Handoff` | TRANSFORM | Record exact cutover status and continuation; authority transfer remains false unless separately governed |
| `10 Change Log` | TRANSFORM | Record source-history bridge/import/promotion events using fresh target `CHG-*` IDs |
| `12 Authorization Registry` | TRANSFORM | Record bounded target merge/cutover authority; no source AUTH ID reuse |
| `13 Evidence Registry` | TRANSFORM | Record exact source commit/tree, history bridge, manifest digest, target merge/promotion evidence using fresh target `EVD-*` IDs |
| `14 Manifest` | TRANSFORM | Include `projectframework/` module/migration surfaces and exact source provenance in target reconstructable snapshot |
| `15 Action Registry` | TRANSFORM | Add target cutover Action; preserve `ACT-017`, `ACT-018`, `ACT-020`, `ACT-021` independently |
| `16 Migration Registry` | TRANSFORM | Add ProjectFramework source→AI-ControlTower cutover migration record with rollback phase/state |
| `40 Technical Design` | TRANSFORM | Record module boundary/dependency direction and non-runtime cutover implementation contract |
| `91 Project Management Control` | DO_NOT_IMPORT / applicability only | Do not materialize solely to mirror source OUT records; create only if target management truth makes it applicable under target Framework |

## 7. Current Target Architecture Conflict/Reconciliation Contract

Observed AI-ControlTower Architecture says:

```text
AI CONTROL TOWER — Router / Classifier ONLY
CT-1: Control Tower classifies/routes intent only; never universal runtime gateway
```

Approved ProjectFramework 2.0 architecture adds:

```text
ProjectFramework Protocol/Core
Control Plane Runtime
  API/Auth
  State Engine
  Workflow Engine
  Event Log
  MULTICA coordination integration
  Recovery
  Checkpoint/Outbox
Capability Providers / Adapters
```

These are reconciled, not treated as mutually exclusive, by the following target rule:

```text
The Control Tower's intent/capability routing role remains bounded and does not become a universal tool-execution gateway.
The wider AI-ControlTower Control Plane may host protocol-enforcement state/workflow/API/session/recovery/checkpoint responsibilities that are logically separate from lane/provider execution.
ProjectFramework defines the protocol/guard/state semantics; AI-ControlTower runtime implements them.
Specialist execution authority remains with the applicable capability/runtime/source-native owner.
```

This wording must be reviewed/promoted through target Decision/Requirements/Architecture owners before canonical-source cutover.

## 8. Existing AI-ControlTower Action Preservation

At preparation time the target reports exactly four non-terminal actions:

```text
ACT-017 — ProjectFramework Direct-to-Latest upgrade record — PLANNED / NOT_STARTED / EXECUTION_NOT_AUTHORIZED
ACT-018 — GitNexus comparative evaluation — PLANNED / NOT_STARTED / EXECUTION_NOT_AUTHORIZED / LICENSE_REVIEW_REQUIRED
ACT-020 — Multica Control Tower Integration PoC — PLANNED / NOT_STARTED / EXECUTION_NOT_AUTHORIZED / INTERNAL_USE_LICENSE_BOUNDARY
ACT-021 — NexusRAG Document Evidence PoC — PLANNED / NOT_STARTED / EXECUTION_NOT_AUTHORIZED / LICENSE_VERIFICATION_REQUIRED
```

The ProjectFramework 2.0 cutover may reference `ACT-017` as related historical/future upgrade intent, but **does not automatically satisfy, supersede, complete, authorize, or cancel any of these actions**. Any reconciliation of those action semantics is a separate target governance decision.

## 9. Version Matrix

| Version domain | Cutover/pre-implementation value | Authority |
|---|---|---|
| ProjectFramework | `2.0.0` target | ProjectFramework Protocol/Core release contract |
| Project Source Schema | `2.0.0` target | ProjectFramework schema contract |
| API Protocol | `1.0.0` initial | Independent public API contract |
| Workflow Schema | `1.0.0` initial | Independent workflow/transition schema contract |
| AI-ControlTower application | current target version at execution | AI-ControlTower release governance; not assigned by this manifest |
| Framework 1.x retained baseline | `1.14.0` / Schema `1.0.0` / format `3` | Immutable migration/source evidence |

No version number grants compatibility. Compatibility is declared/tested explicitly; incompatible mutation requests fail closed.

## 10. Licensing Boundary Matrix

| Target scope | Classification | Cutover rule |
|---|---|---|
| `projectframework/` future Protocol/Core | public-domain protocol/specification intent | Exact dedication/legal instrument remains release/legal-packaging work; do not claim a specific instrument here |
| `projectframework/migration/v1-baseline/` | source provenance/history snapshot | Preserve source notices/provenance; no implication that target runtime licensing changed |
| AI-ControlTower existing/future Control Plane runtime | separately governed software license | DO NOT reclassify as public domain by proximity/import |
| `adapters/` | provider-compatible software licensing | Provider terms remain independent; no adapter included in public protocol projection automatically |
| `apps/` | target software licensing | Separate from ProjectFramework protocol |
| Public ProjectFramework mirror projection | protocol-only publication | Cannot contain private runtime config, credentials, differently licensed runtime/adapters, or target Project Source secrets |

## 11. Git Provenance / History Preservation

Full ProjectFramework source history is preserved by an ancestry-only merge into the target cutover branch:

```powershell
git merge -s ours --allow-unrelated-histories $SourceCommit -m "chore: bridge ProjectFramework history for 2.0 cutover"
```

Acceptance:

```text
$SourceCommit is an ancestor of target cutover HEAD/main after merge
ancestry bridge changes no target tree content by itself
source repository/commit remains independently resolvable
selected migration assets are copied only in a subsequent bounded commit
no root-level source tree overlay occurs
```

This avoids a naïve unrelated-history merge that would collide `README`, `.github`, Project Source, tooling, and repository-root files.

## 12. Rollback Mapping

| Phase | Rollback class | Required behavior |
|---|---|---|
| Before target branch mutation | REFERENCE | No target rollback; source ProjectFramework remains canonical |
| Target cutover branch before PR merge | RETAIN_HISTORY | Abandon/revert branch only after governed cleanup approval; target main unchanged |
| Target PR merged, source mirror role not yet reconciled | TRANSFORM | Governed target revert + verification required before restoring source 2.x authority; never assume source automatically regained authority |
| Target promoted + source mirror role reconciled, no non-representable 2.0-only truth | TRANSFORM | Coordinated two-Project rollback may be possible after explicit assessment and verification |
| 2.0-only governance/runtime truth exists | DO_NOT_IMPORT as rollback mechanism | Git revert/branch switch is insufficient; execute reverse migration/recovery under a new plan |

## 13. Public Mirror Projection Rule

After cutover promotion:

```text
AI-ControlTower/projectframework/ canonical candidate
        ↓ exact commit + subtree/content digest + conformance evidence
Verified Release Projection
        ↓ one way
captainhuke-dev/ProjectFramework public repository
```

A direct change in the public mirror may be accepted as contribution input but never becomes canonical by recency. Accepted semantic change is applied/reconciled in AI-ControlTower canonical source and then projected outward.

## 14. Cutover Foundation Exclusions

The merge/cutover foundation does not produce:

```text
Project Source 2.0 typed-resource implementation
public API server or token service
State Engine/Event Log/materialized database
Workflow Engine or transition executor
MULTICA lease/fencing runtime
Checkpoint/Outbox runtime
Recovery daemon/service
OpenViking/Graphify/NexusRAG/GitNexus/Serena/EMIF adapter implementation
public release/mirror projection
specific public-domain dedication or software license choice
production deployment
```

Those are separate post-cutover work streams under AI-ControlTower authority.

## 15. Pre-Merge Readiness Acceptance Checklist

`PRE_MERGE_READY` requires every item below to be verified before the current ProjectFramework preparation Goal closes:

```text
[PASS REQUIRED] V1 Framework 1.14 Last Stable baseline exact and canonical
[PASS REQUIRED] V2 written architecture approved and forward-ported
[PASS REQUIRED] no unresolved ProjectFramework Stable-ID collision
[PASS REQUIRED] migration/cutover plan complete and self-reviewed
[PASS REQUIRED] this merge manifest complete and self-reviewed
[PASS REQUIRED] exact AI-ControlTower repository/Project UUID/GitHub binding/Local Workspace binding verified
[PASS REQUIRED] current target architecture read and Control Tower→Control Plane semantic delta explicitly mapped
[PASS REQUIRED] target existing non-terminal Actions preserved in plan/manifest
[PASS REQUIRED] fresh isolated target worktree strategy defined
[PASS REQUIRED] full source Git history preservation mechanism defined
[PASS REQUIRED] source V1 Project Source not imported as target active Project Source
[PASS REQUIRED] source/target file mapping complete
[PASS REQUIRED] initial independent version matrix explicit
[PASS REQUIRED] component licensing boundary classified
[PASS REQUIRED] rollback phases explicit
[PASS REQUIRED] no actual AI-ControlTower target mutation performed by preparation Goal
[PASS REQUIRED] no actual canonical-source cutover performed by preparation Goal
[PASS REQUIRED] no V2 runtime implementation performed by preparation Goal
```

Source premerge branch publication, target Project Source Preview approval, target mutation, target PR/merge, canonical-source promotion, and source mirror-role reconciliation are **merge-time execution gates**, not claims made by `PRE_MERGE_READY`.

## 16. Self-Review Result

`PF2_PLAN_MANIFEST_SELF_REVIEW 36/36 PASS` — `2026-09-05T12:42:18+07:00`.

The manifest is complete for Pre-Merge evaluation: mapping classes, authority/identity separation, V1 baseline retention, target Project Source reconciliation, current Control Tower→Control Plane semantic delta, target Action preservation, version/licensing matrices, Git history preservation, rollback mapping, mirror direction, cutover exclusions, and merge-time gates are explicit.