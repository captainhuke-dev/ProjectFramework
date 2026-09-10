# ProjectFramework 2.0 AI-ControlTower Merge/Cutover Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Merge ProjectFramework into AI-ControlTower as the governed ProjectFramework 2.x canonical development home while preserving the verified Framework 1.14 source baseline, full Git provenance, AI-ControlTower Project identity/current truth, rollback ability, and a strict boundary between protocol assets and runtime software.

**Architecture:** This plan is the **Merge/Cutover Foundation only**. It first publishes the verified ProjectFramework pre-merge checkpoint, then uses a fresh isolated AI-ControlTower worktree, bridges complete ProjectFramework Git ancestry without overlaying repository roots, materializes a bounded `projectframework/` migration foundation, explicitly reconciles AI-ControlTower architecture/Project Source, and promotes the new canonical-source role only after target verification. ProjectFramework 2.0 protocol/schema implementation and Control Plane/API/State/Workflow/MULTICA/adapter runtime work are decomposed into separate post-cutover plans.

**Tech Stack:** Git/GitHub, Markdown/YAML Project Source governance, existing AI-ControlTower Python repository/toolchain for verification only; no application runtime code, database, API service, workflow engine, MULTICA runtime, or adapter implementation is added by this plan.

**Spec:** `docs/superpowers/specs/2026-09-04-projectframework-2-controltower-architecture-design.md`

## Global Constraints

- ProjectFramework source baseline before cutover is canonical `captainhuke-dev/ProjectFramework main@aae65796a8d4ad5f23323889b65b060bd36302c1`; Framework-Source tree `d5d04e4563157246872b1e02c791b94a6c564d95` is the verified Framework `1.14.0` Last Stable 1.x distribution.
- The exact Pre-Merge Readiness completion commit produced after this plan is written becomes the source preparation commit; it must be published/reconciled to ProjectFramework `main` under the later merge authorization before target import begins.
- AI-ControlTower target repository is `https://github.com/captainhuke-dev/ai-controltower.git`; target Project UUID is `2ab1b99a-901c-4159-87f1-953db0af5015`.
- AI-ControlTower active `FRAMEWORK-001` remains the Project root/governance authority. ProjectFramework's V1 `FRAMEWORK-001` and Project Source history are migration provenance only and MUST NOT replace AI-ControlTower Project Source.
- ProjectFramework identity remains a named Protocol/Core lineage inside AI-ControlTower; after governed promotion `AI-ControlTower/projectframework/` is ProjectFramework 2.x canonical development source.
- The public ProjectFramework repository becomes a one-way verified distribution mirror only after target canonical-source promotion; it never reverse-syncs automatically.
- `Project Source Governance Authority ≠ Workflow/Execution State Authority`; the merge foundation must not create runtime state authority in Project Source.
- `Authentication ≠ Authority`, `Execution success ≠ Task DONE`, `Task DONE ≠ OUT achieved`, `commit ≠ push`, and `MERGED ≠ canonical-source cutover` remain invariant.
- No dual active 1.x/2.0 governance authority is allowed. V1 remains authoritative until the target cutover promotion is freshly verified.
- Current AI-ControlTower architecture says Control Tower is `Router / Classifier ONLY`. The cutover must explicitly reconcile this with the approved 2.0 Control Plane model; no silent newest-wins overwrite is permitted.
- Existing AI-ControlTower non-terminal actions `ACT-017`, `ACT-018`, `ACT-020`, and `ACT-021` remain independent and must not be auto-completed, cancelled, or adopted by this migration.
- The current local AI-ControlTower root checkout is not a merge workspace because it was observed `ahead 67 / behind 113` with untracked `.worktrees/`. Use a fresh isolated worktree from then-current `origin/main`.
- Initial ProjectFramework 2.0 contract matrix for implementation planning is: ProjectFramework `2.0.0`; Project Source Schema `2.0.0`; API Protocol `1.0.0`; Workflow Schema `1.0.0`. AI-ControlTower application version remains independently governed by AI-ControlTower and is not assigned by this ProjectFramework plan.
- Component licensing boundary is fixed conceptually: `projectframework/` = public-domain protocol/specification intent; `control-plane/`, `adapters/`, and `apps/` retain separately governed software/provider-compatible licensing. Exact legal instruments are a release/legal-packaging gate and are not selected here.
- No force push, destructive history rewrite, branch/worktree deletion, target Root/Binding rewrite by implication, secret-value persistence, public mirror publication, or V2 runtime implementation is authorized by this plan itself.

---

## Planned File/Repository Responsibilities

| Surface | Responsibility after cutover foundation |
|---|---|
| `AI-ControlTower/projectframework/README.md` | Declares ProjectFramework 2.x canonical module boundary, canonical-source role, dependency direction, and implementation-not-started status at cutover |
| `AI-ControlTower/projectframework/migration/v1-baseline/Framework-Source/` | Exact immutable copy of verified ProjectFramework Framework 1.14 distribution used for 1.x→2.0 migration/conformance reference |
| `AI-ControlTower/projectframework/migration/design/2026-09-04-projectframework-2-controltower-architecture-design.md` | Approved 2.0 architecture source carried into the canonical development repository |
| `AI-ControlTower/projectframework/migration/2026-09-05-projectframework-2-ai-controltower-migration.md` | This merge/cutover foundation plan copied as migration provenance |
| `AI-ControlTower/projectframework/migration/2026-09-05-projectframework-2-ai-controltower-merge-manifest.md` | Exact source→target mapping/classification and cutover acceptance contract |
| AI-ControlTower `Project-Source/` current owners | Records target-side Decision/Requirement/Architecture/Migration/Action/Authority/Evidence/Current State/Handoff truth; never copied from ProjectFramework Project Source wholesale |
| ProjectFramework `Project-Source/` after target promotion | Records final canonical-source transfer and public-mirror role while retaining 1.x history and local Project identity |
| `AI-ControlTower/control-plane/`, `adapters/`, `apps/` | Unchanged by this foundation plan; runtime implementation is separate follow-on work |

---

### Task 1: Publish the exact ProjectFramework Pre-Merge Readiness checkpoint

**Files:**
- Verify: `docs/superpowers/PROJECT-TASKS.md`
- Verify: `docs/superpowers/specs/2026-09-04-projectframework-2-controltower-architecture-design.md`
- Verify: `docs/superpowers/plans/2026-09-05-projectframework-2-ai-controltower-migration.md`
- Verify: `docs/superpowers/plans/2026-09-05-projectframework-2-ai-controltower-merge-manifest.md`
- Verify: active ProjectFramework `Project-Source/01/03/09/10/12/13/14/15/91`

**Interfaces:**
- Consumes: local `PRE_MERGE_READY` completion commit and its evidence.
- Produces: one exact ProjectFramework canonical source-preparation commit on `origin/main`, named in all later target import evidence.

- [ ] **Step 1: Re-resolve ProjectFramework canonical main and local readiness commit**

Run from `E:\GitHub\ProjectFramework\.worktrees\pf2-design`:

```powershell
git fetch origin
git rev-parse HEAD
git rev-parse origin/main
git status --short --branch
git diff --check origin/main...HEAD
```

Expected: the readiness branch is clean, its completion commit is a descendant of the recorded V1 baseline, and the verified Framework-Source tree is unchanged from `d5d04e4563157246872b1e02c791b94a6c564d95`.

- [ ] **Step 2: Verify source-side publication authority before any push**

Read active ProjectFramework `00 -> 01 -> 03 -> 09 -> 12 -> 15 -> 91`. Continue only when the new merge/cutover Goal explicitly includes source branch push/PR/merge and post-merge reconciliation. Existing `AUTH-011` does not provide this authority.

Expected: a current authorization record explicitly covers the shared-state publication operation.

- [ ] **Step 3: Push the exact readiness branch and create a ProjectFramework PR to `main`**

Use the exact branch `v2-premerge-readiness`:

```powershell
git push -u origin v2-premerge-readiness
gh pr create --repo captainhuke-dev/ProjectFramework --base main --head v2-premerge-readiness --title "ProjectFramework 2.0 pre-merge readiness" --body-file docs/superpowers/plans/2026-09-05-projectframework-2-ai-controltower-migration.md
```

Expected: remote branch head equals the locally verified completion commit and one PR targets ProjectFramework `main`.

- [ ] **Step 4: Verify PR identity/mergeability and merge without rewriting history**

```powershell
gh pr view --repo captainhuke-dev/ProjectFramework --json number,state,baseRefName,baseRefOid,headRefName,headRefOid,mergeable,mergeStateStatus,statusCheckRollup,url
gh pr merge --repo captainhuke-dev/ProjectFramework --merge
```

Expected before merge: exact head SHA matches readiness evidence; base is freshly observed `main`; merge state is acceptable; no required check is failing. Use a merge commit, not squash/rebase, so source preparation provenance remains explicit.

- [ ] **Step 5: Reconcile ProjectFramework publication state and bind the cutover source commit**

After merge, fetch and create one governed source-side reconciliation revision that records the PR merge and sets:

```text
PROJECTFRAMEWORK_CUTOVER_SOURCE_COMMIT = exact freshly observed origin/main commit after reconciliation
Framework-Source tree = d5d04e4563157246872b1e02c791b94a6c564d95
Pre-Merge Readiness = PERSISTED / NOT_PENDING
Canonical 2.x source transfer = NOT_YET_PROMOTED
```

Commit and fast-forward push this bounded reconciliation only under the merge Goal authority. Freshly observe remote `origin/main` and use that exact SHA for every later `$SourceCommit` binding.

---

### Task 2: Create a fresh isolated AI-ControlTower merge worktree from canonical remote

**Files:**
- Read: AI-ControlTower active `Project-Source/00`, `01`, `03`, `04`, `05`, `06`, `07`, `09`, `10`, `12`, `13`, `14`, `15`, `16`, `40`
- Do not modify: existing root checkout `E:\GitHub\ai-controltower`

**Interfaces:**
- Consumes: exact `PROJECTFRAMEWORK_CUTOVER_SOURCE_COMMIT` from Task 1.
- Produces: clean isolated branch `projectframework-2-cutover` from fresh AI-ControlTower `origin/main`.

- [ ] **Step 1: Fetch AI-ControlTower and verify the bound repository**

```powershell
git -C E:\GitHub\ai-controltower fetch origin
git -C E:\GitHub\ai-controltower remote get-url origin
git -C E:\GitHub\ai-controltower rev-parse origin/main
```

Expected remote: `https://github.com/captainhuke-dev/ai-controltower.git`.

- [ ] **Step 2: Verify the existing root checkout is not being repurposed**

```powershell
git -C E:\GitHub\ai-controltower status --short --branch
```

Expected: regardless of whether its divergence has changed since planning, do not reset, clean, checkout, merge, or mutate this root checkout as part of the cutover.

- [ ] **Step 3: Create the fixed isolated cutover worktree**

First verify branch/path absence:

```powershell
git -C E:\GitHub\ai-controltower branch --list projectframework-2-cutover
Test-Path E:\GitHub\ai-controltower\.worktrees\projectframework-2-cutover
```

Expected: no existing branch and `False` for the path. If either exists, stop and reconcile ownership instead of choosing a lookalike.

Create it:

```powershell
git -C E:\GitHub\ai-controltower worktree add E:\GitHub\ai-controltower\.worktrees\projectframework-2-cutover -b projectframework-2-cutover origin/main
```

- [ ] **Step 4: Bootstrap target governance from the isolated worktree**

Read the active `FRAMEWORK-001` first, then `01 -> 03`, and `09` for continuation. Freshly verify:

```text
project_uuid = 2ab1b99a-901c-4159-87f1-953db0af5015
GitHub binding = BOUND / VERIFIED / captainhuke-dev/ai-controltower
Local Workspace binding = BOUND / VERIFIED / E:\GitHub\ai-controltower
Google Drive = NOT_APPLICABLE
```

If the target root/binding is incompatible with these identities, fail closed before Material target mutation.

---

### Task 3: Prepare the AI-ControlTower Project Source cutover Preview before mutation

**Files:**
- Preview changes for target active `Project-Source/04`, `05`, `06`, `07`, `03`, `09`, `10`, `12`, `13`, `14`, `15`, `16`, `40`
- Do not create target `91` merely for completeness

**Interfaces:**
- Consumes: target current truth from Task 2 and approved ProjectFramework architecture spec.
- Produces: a reviewable target Project Source Preview with exact current-vs-target semantic delta and rollback route.

- [ ] **Step 1: Allocate target Stable IDs only from fresh target state**

Scan the current reconstructable snapshot for the highest existing `DEC-*`, `REQ-*`, `CHG-*`, `AUTH-*`, `EVD-*`, `ACT-*`, and `MIG-*` identifiers. Allocate the next unused IDs in the target Project namespace. Never copy ProjectFramework source IDs as target IDs; source references are qualified by source Project/repository/commit.

Expected: no duplicate target Stable ID and no archive-dependent current reference.

- [ ] **Step 2: Draft one explicit target Decision for the canonical-source/architecture evolution**

The Decision must state all of the following semantics:

```text
ProjectFramework 2.0 remains a named Protocol/Core module inside AI-ControlTower.
AI-ControlTower Project UUID/root authority remains unchanged.
ProjectFramework V1 Project Source is migration provenance, not target Project Source authority.
Current Control Tower router/classifier responsibility is preserved as a bounded Control Plane responsibility.
ProjectFramework 2.0 additionally defines state/workflow/API/checkpoint protocol semantics; this does not make the router a universal execution gateway.
AI-ControlTower/projectframework/ becomes 2.x canonical development source only after verified target promotion.
Public ProjectFramework becomes a one-way verified distribution mirror only after that promotion.
```

- [ ] **Step 3: Draft target Requirements that bind the cutover safety contract**

Requirements must cover:

```text
exact source commit + history preservation
no dual active governance authority
preserve target ACT-017/018/020/021 state
component licensing boundary
independent version matrix
fresh target worktree and Base Freshness
rollback before/after canonical-source promotion
public mirror one-way direction
no runtime implementation in cutover foundation
```

- [ ] **Step 4: Draft Architecture/Technical Design reconciliation**

Update the Preview so target `06` and `40` preserve current CT-1..CT-4 and specialist boundaries while adding the approved future logical layering:

```text
ProjectFramework Protocol/Core
Control Plane Runtime
Capability Provider/Adapter layer
Apps
```

The Preview must explicitly say that runtime implementation remains not started by the cutover foundation.

- [ ] **Step 5: Draft Migration/Action/Authority/Evidence lifecycle records**

Prepare a target `MIG-*` record and bounded target `AUTH-* / ACT-* / EVD-* / CHG-*` records for the cutover. The migration record must reference the exact ProjectFramework source Project UUID/repository/commit and the merge manifest digest. Existing AI-ControlTower actions remain unchanged unless separately authorized by their own current contracts.

- [ ] **Step 6: Present the target Preview under the later merge Goal before writes**

The actual target mutation begins only after explicit approval for this Preview or an already-active target merge Goal whose scope unambiguously covers the exact Preview. Do not infer target mutation authority from this ProjectFramework-side plan.

---

### Task 4: Bridge complete ProjectFramework Git history into the target branch without tree collision

**Files:**
- Git history only in this task; target working tree content remains unchanged by the ancestry-bridge commit

**Interfaces:**
- Consumes: exact `$SourceCommit` from Task 1 and approved target Preview from Task 3.
- Produces: target branch whose ancestry contains the complete ProjectFramework source history while retaining the pre-import AI-ControlTower tree.

- [ ] **Step 1: Add/fetch a temporary ProjectFramework source remote in the isolated target worktree**

```powershell
$Target = 'E:\GitHub\ai-controltower\.worktrees\projectframework-2-cutover'
git -C $Target remote add projectframework-source https://github.com/captainhuke-dev/ProjectFramework.git
git -C $Target fetch projectframework-source main
$SourceCommit = (git -C $Target rev-parse projectframework-source/main).Trim()
```

Expected: `$SourceCommit` equals the exact `PROJECTFRAMEWORK_CUTOVER_SOURCE_COMMIT` established in Task 1. If not, stop and reconcile source publication before continuing.

- [ ] **Step 2: Confirm histories are unrelated or not already bridged**

```powershell
git -C $Target merge-base --is-ancestor $SourceCommit HEAD
$LASTEXITCODE
```

Expected for first cutover: non-zero. If it is already an ancestor, inspect prior cutover evidence instead of creating another history bridge.

- [ ] **Step 3: Create an ancestry-only merge commit**

```powershell
git -C $Target merge -s ours --allow-unrelated-histories $SourceCommit -m "chore: bridge ProjectFramework history for 2.0 cutover"
```

This merge intentionally keeps the AI-ControlTower tree for this commit while making full ProjectFramework Git history reachable. It must not be confused with canonical-source promotion.

- [ ] **Step 4: Verify the bridge**

```powershell
git -C $Target merge-base --is-ancestor $SourceCommit HEAD
git -C $Target diff --check HEAD^1..HEAD
git -C $Target status --short
```

Expected: ancestor check succeeds, tree diff is empty for the ancestry bridge, worktree clean.

---

### Task 5: Materialize the ProjectFramework cutover foundation under `AI-ControlTower/projectframework/`

**Files:**
- Create: `projectframework/README.md`
- Create copy: `projectframework/migration/v1-baseline/Framework-Source/**`
- Create copy: `projectframework/migration/design/2026-09-04-projectframework-2-controltower-architecture-design.md`
- Create copy: `projectframework/migration/2026-09-05-projectframework-2-ai-controltower-migration.md`
- Create copy: `projectframework/migration/2026-09-05-projectframework-2-ai-controltower-merge-manifest.md`
- Do not modify: `control-plane/`, `adapters/`, `apps/`, existing `src/` runtime in this task

**Interfaces:**
- Consumes: source commit/history bridge and merge manifest.
- Produces: a bounded canonical-development foundation that contains migration provenance but no V2 runtime implementation.

- [ ] **Step 1: Export the exact Framework 1.14 baseline from the bound source commit**

From the target worktree, create the destination and archive the source tree directly from Git:

```powershell
$Target = 'E:\GitHub\ai-controltower\.worktrees\projectframework-2-cutover'
$SourceCommit = (git -C $Target rev-parse projectframework-source/main).Trim()
New-Item -ItemType Directory -Force -Path "$Target\projectframework\migration\v1-baseline" | Out-Null
git -C $Target archive --format=tar $SourceCommit Framework-Source | tar -xf - -C "$Target\projectframework\migration\v1-baseline"
```

Verify copied `FRAMEWORK-RELEASE.yaml` still declares Framework `1.14.0`, Schema `1.0.0`, release format `3`.

- [ ] **Step 2: Copy the approved design/plan/manifest from the exact source commit**

Export the three files from the exact source commit with `git archive`, then use byte-preserving filesystem copies. This prevents uncommitted source state or PowerShell text re-encoding from entering the target:

```powershell
$Stage = Join-Path ([IO.Path]::GetTempPath()) 'projectframework-cutover-export'
if (Test-Path $Stage) { throw "Owned export stage already exists: $Stage" }
New-Item -ItemType Directory -Path $Stage | Out-Null
git -C $Target archive --format=tar $SourceCommit docs/superpowers/specs/2026-09-04-projectframework-2-controltower-architecture-design.md docs/superpowers/plans/2026-09-05-projectframework-2-ai-controltower-migration.md docs/superpowers/plans/2026-09-05-projectframework-2-ai-controltower-merge-manifest.md | tar -xf - -C $Stage
New-Item -ItemType Directory -Force -Path "$Target\projectframework\migration\design" | Out-Null
Copy-Item -LiteralPath "$Stage\docs\superpowers\specs\2026-09-04-projectframework-2-controltower-architecture-design.md" -Destination "$Target\projectframework\migration\design\2026-09-04-projectframework-2-controltower-architecture-design.md"
Copy-Item -LiteralPath "$Stage\docs\superpowers\plans\2026-09-05-projectframework-2-ai-controltower-migration.md" -Destination "$Target\projectframework\migration\2026-09-05-projectframework-2-ai-controltower-migration.md"
Copy-Item -LiteralPath "$Stage\docs\superpowers\plans\2026-09-05-projectframework-2-ai-controltower-merge-manifest.md" -Destination "$Target\projectframework\migration\2026-09-05-projectframework-2-ai-controltower-merge-manifest.md"
Remove-Item -LiteralPath $Stage -Recurse
```

Verify the three copied SHA256 digests against the source-commit export before staging them.

- [ ] **Step 3: Create the module-boundary README with exact cutover semantics**

Create `projectframework/README.md` with this content:

```markdown
# ProjectFramework 2.x Canonical Development Root

This directory is the canonical ProjectFramework 2.x development root **only after the governed AI-ControlTower cutover promotion is verified**.

At cutover-foundation time:

- `migration/v1-baseline/Framework-Source/` is the immutable verified Framework 1.14 Last Stable 1.x migration baseline.
- `migration/design/` and adjacent migration documents preserve the approved 2.0 architecture and cutover provenance.
- ProjectFramework Protocol/Core remains logically separate from AI-ControlTower runtime software.
- No Control Plane/API/State/Workflow/MULTICA/adapter runtime implementation is implied by this directory existing.
- AI-ControlTower Project Source remains Governance Authority for the AI-ControlTower Project; ProjectFramework V1 Project Source remains historical migration provenance.
- Public ProjectFramework repository becomes a one-way verified distribution mirror only after canonical-source promotion.

Dependency direction for later implementation is `control-plane -> projectframework`; `projectframework` must not depend on Control Plane runtime or product-specific adapters.
```

- [ ] **Step 4: Verify the import boundary before commit**

```powershell
git -C $Target status --short
git -C $Target diff --check
```

Expected changed content is confined to `projectframework/` in this task. No runtime/source file under existing AI-ControlTower `src/`, `tests/`, `control-plane/`, `adapters/`, or `apps/` is changed.

- [ ] **Step 5: Commit the cutover foundation content**

```powershell
git -C $Target add projectframework
git -C $Target diff --cached --check
git -C $Target commit -m "docs: import ProjectFramework 2 cutover foundation"
```

---

### Task 6: Apply the approved AI-ControlTower Project Source cutover candidate

**Files:**
- Modify through new governed revisions only: target `Project-Source/01`, `03`, `04`, `05`, `06`, `07`, `09`, `10`, `12`, `13`, `14`, `15`, `16`, `40`
- Preserve: active target `00 / FRAMEWORK-001` identity/binding unless the approved Preview separately requires a Root revision

**Interfaces:**
- Consumes: approved Preview, history bridge, imported module foundation.
- Produces: target Project Source candidate that explicitly recognizes ProjectFramework 2.x cutover semantics without claiming target-main persistence yet.

- [ ] **Step 1: Create new target revisions from the freshly resolved current owners**

Copy each affected active owner to its next revision; update `supersedes`, revision, timestamp, and routing. Do not overwrite existing active files in place.

- [ ] **Step 2: Persist the approved target Decision/Requirements/Architecture delta**

Use the exact target Stable IDs allocated in Task 3. Ensure `06` explicitly reconciles the prior `Router / Classifier ONLY` wording rather than deleting it: routing/classification remains a bounded Control Plane responsibility, while ProjectFramework 2.0 state/workflow/API/checkpoint engines are separate protocol-enforcement/runtime responsibilities and do not create a universal execution gateway.

- [ ] **Step 3: Persist target Migration and lifecycle evidence**

Target migration/evidence must bind:

```text
ProjectFramework source repository = captainhuke-dev/ProjectFramework
source project_uuid = 00575e76-17ce-4dd3-ad24-377494a4a45b
source cutover commit = exact Task-1 commit
source Framework 1.14 tree = d5d04e4563157246872b1e02c791b94a6c564d95
target repository = captainhuke-dev/ai-controltower
target project_uuid = 2ab1b99a-901c-4159-87f1-953db0af5015
history bridge commit = exact Task-4 commit
module import commit = exact Task-5 commit
merge manifest digest = exact SHA256 of imported manifest
canonical-source promotion state = CANDIDATE / NOT_YET_CANONICAL before target PR merge
```

- [ ] **Step 4: Preserve independent target work**

Verify `ACT-017`, `ACT-018`, `ACT-020`, and `ACT-021` retain their source states and authorization/license gates. The cutover may reference them but must not mutate their lifecycle state without separate authority.

- [ ] **Step 5: Promote target Project Source candidate and commit locally**

Run target routing/reconstructability checks, archive superseded revisions, promote exactly one active revision per owner, then:

```powershell
git -C $Target add Project-Source
git -C $Target diff --cached --check
git -C $Target commit -m "docs: prepare ProjectFramework 2 canonical-source cutover"
```

---

### Task 7: Run target integration verification and create the AI-ControlTower PR

**Files:**
- Verify all target changes since fresh `origin/main`
- No new runtime files beyond the documented `projectframework/` cutover foundation

**Interfaces:**
- Consumes: target cutover candidate commits.
- Produces: one verified AI-ControlTower PR candidate.

- [ ] **Step 1: Re-fetch target main and re-evaluate Base Freshness**

```powershell
git -C $Target fetch origin
git -C $Target rev-parse origin/main
git -C $Target merge-base --is-ancestor origin/main HEAD
git -C $Target diff --check origin/main...HEAD
```

If `origin/main` advanced and is not an ancestor of the cutover branch, classify target drift. Semantic target drift requires forward-port/reconciliation before PR creation.

- [ ] **Step 2: Verify migration invariants**

Verify all of these directly:

```text
source cutover commit is ancestor of target branch through history bridge
AI-ControlTower project_uuid/root binding unchanged
projectframework/migration/v1-baseline/Framework-Source/FRAMEWORK-RELEASE.yaml = Framework 1.14.0 / Schema 1.0.0 / format 3
no ProjectFramework V1 Project Source file became target active Project Source
existing target ACT-017/018/020/021 states preserved
no V2 runtime/API/database/workflow/MULTICA/adapter implementation added
component boundary does not mix separately licensed runtime assets into projectframework migration snapshot
ProjectFramework 2.0 matrix = 2.0.0 / Project Source 2.0.0 / API 1.0.0 / Workflow 1.0.0
canonical-source state remains CANDIDATE before target PR merge
```

- [ ] **Step 3: Run the existing AI-ControlTower repository verification appropriate to documentation-only change**

Read target repository test/tooling instructions first. At minimum run Git hygiene and any configured docs/Project Source validation that exists in the target repository. Do not invent a new executable validator as part of this migration.

- [ ] **Step 4: Request/review the target branch before merge**

Use the repository's current review process. Critical or Important findings must be fixed before merge. Re-run only invalidated verification after corrections; do not reuse stale Base Freshness evidence.

- [ ] **Step 5: Push and create target PR under explicit merge authority**

```powershell
git -C $Target push -u origin projectframework-2-cutover
gh pr create --repo captainhuke-dev/ai-controltower --base main --head projectframework-2-cutover --title "ProjectFramework 2.0 canonical-source cutover foundation" --body-file projectframework/migration/2026-09-05-projectframework-2-ai-controltower-migration.md
```

Expected: exact verified branch head is the PR head; canonical-source state is still candidate until the PR merge is freshly observed.

---

### Task 8: Merge AI-ControlTower cutover candidate and promote canonical-source role

**Files:**
- Target GitHub PR / `main`
- Target Project Source cutover records already in PR

**Interfaces:**
- Consumes: verified target PR and valid merge authority.
- Produces: freshly verified `AI-ControlTower/projectframework/` canonical 2.x development source.

- [ ] **Step 1: Freshly verify target PR head/base/checks immediately before merge**

```powershell
gh pr view --repo captainhuke-dev/ai-controltower --json number,state,baseRefName,baseRefOid,headRefName,headRefOid,mergeable,mergeStateStatus,statusCheckRollup,url
```

Expected: exact candidate head, current `main` base, mergeable/acceptable state, no required failing check.

- [ ] **Step 2: Merge with a merge commit**

```powershell
gh pr merge --repo captainhuke-dev/ai-controltower --merge
```

Do not delete branches/worktrees automatically.

- [ ] **Step 3: Fetch and verify canonical target result**

```powershell
git -C $Target fetch origin
git -C $Target rev-parse origin/main
git -C $Target merge-base --is-ancestor $SourceCommit origin/main
git -C $Target rev-parse origin/main:projectframework/migration/v1-baseline/Framework-Source
```

Also verify the merged Project Source state declares `AI-ControlTower/projectframework/` canonical for ProjectFramework 2.x development and still preserves AI-ControlTower root identity.

- [ ] **Step 4: Mark the canonical-source promotion effective only after this observation**

The authority transition is now:

```text
ProjectFramework <= 1.14 development history = retained source provenance
AI-ControlTower/projectframework/ = ProjectFramework 2.x canonical development source
ProjectFramework public repository = not yet reconciled mirror role until Task 9
```

Target PR merge alone is not enough; this step's fresh observation is the promotion evidence.

---

### Task 9: Reconcile the public ProjectFramework repository into one-way mirror role

**Files:**
- Modify through governed revisions: ProjectFramework active `Project-Source/01/03/09/10/12/13/14/15/91`
- Do not modify: `Framework-Source/` 1.14 baseline during this role reconciliation

**Interfaces:**
- Consumes: exact freshly verified AI-ControlTower canonical cutover commit from Task 8.
- Produces: source repository current truth that no longer claims 2.x development authority.

- [ ] **Step 1: Create a bounded ProjectFramework cutover-reconciliation Goal/authority**

Record exact target repository, target commit, target `projectframework/` content digest, source cutover commit, and target promotion evidence. Authority must explicitly cover the source-side push/reconciliation.

- [ ] **Step 2: Revise ProjectFramework current truth**

Set current semantics to:

```text
Framework 1.14 = retained Last Stable 1.x distribution/history
AI-ControlTower/projectframework/ at exact target commit = ProjectFramework 2.x canonical development source
public ProjectFramework repository = VERIFIED_ONE_WAY_DISTRIBUTION_MIRROR
reverse synchronization = forbidden
Framework-Source 1.14 historical/current 1.x distribution bytes = unchanged by role reconciliation
```

Do not rewrite historical evidence that truthfully recorded the former authority state.

- [ ] **Step 3: Commit, push, and fresh-observe source mirror-role reconciliation**

Use fast-forward publication under current authority. Verify `origin/main` exact commit and unchanged Framework-Source tree.

---

### Task 10: Final cutover verification and handoff to separate V2 implementation plans

**Files:**
- Verify target AI-ControlTower Project Source/module/history
- Verify source ProjectFramework mirror-role Project Source
- Create evidence records in both Projects according to each Project's current owner/routing rules

**Interfaces:**
- Consumes: target canonical promotion and source mirror reconciliation.
- Produces: `CUTOVER_COMPLETE / V2_IMPLEMENTATION_NOT_STARTED` with reconstructable provenance and rollback classification.

- [ ] **Step 1: Verify no dual development authority remains**

Confirm target Project Source says AI-ControlTower is ProjectFramework 2.x canonical development source and source ProjectFramework says one-way mirror. Any simultaneous claim that both are 2.x development authority is a blocking conflict.

- [ ] **Step 2: Verify history and migration baseline preservation**

Confirm exact source cutover commit is reachable from target history and the imported Framework 1.14 migration baseline matches the source Framework-Source tree/digest.

- [ ] **Step 3: Verify runtime non-implementation boundary**

Target cutover diff must show no Control Plane/API/Auth/State Engine/Workflow Engine/MULTICA/adapter application implementation produced by this plan. Existing AI-ControlTower runtime code is preserved unless independently changed by unrelated target work and reconciled through Base Freshness.

- [ ] **Step 4: Classify rollback window**

Record one of these exact states:

```text
PRE_PROMOTION_ROLLBACK = abandon/revert cutover branch; source remains canonical
POST_TARGET_PROMOTION_PRE_2X_ONLY_TRUTH = governed revert of target cutover + source-role restoration may be possible after verification
POST_2X_ONLY_GOVERNANCE = reverse migration/recovery required; branch switch/revert is insufficient
```

- [ ] **Step 5: Create the post-cutover implementation-plan backlog**

Create separate governed plans/spec refinements for these independently testable streams rather than one monolithic implementation plan:

```text
A. ProjectFramework 2.0 Protocol + Project Source Schema 2.0
B. Workflow / Transition / Guard protocol + conformance vectors
C. Control Plane State Engine + Event Log + Materialized State
D. Public API + Auth/Session/Execution contracts
E. MULTICA lease/fencing/claim coordination integration
F. Checkpoint/Outbox + Recovery/Reconciliation
G. Capability Registry + provider adapters
H. 1.x Project Source migration tooling/workflow
I. Verified public mirror release projection
```

These are post-cutover work and require their own current target Project authority. Their existence in the backlog does not authorize implementation.

- [ ] **Step 6: Persist terminal cutover evidence and stop**

Final state for this plan:

```text
ProjectFramework 2.x canonical source = AI-ControlTower/projectframework/
Public ProjectFramework = one-way verified mirror
Framework 1.14 = retained Last Stable 1.x baseline
V2 runtime implementation = NOT_STARTED by this plan
Next work = select/authorize one post-cutover implementation stream
```

Commit/publish evidence according to each Project's current governance and verify resulting commits before declaring cutover complete.

---

## Rollback Contract

1. **Before any AI-ControlTower branch mutation:** no rollback needed; ProjectFramework remains canonical.
2. **After ancestry bridge/import commits but before target PR merge:** abandon the isolated target branch/worktree after explicit cleanup approval; target `main` is unchanged.
3. **After target PR merge but before source mirror-role reconciliation:** AI-ControlTower target is the promoted 2.x canonical source once fresh promotion evidence exists; a rollback requires a governed target revert and verification before restoring source 2.x authority.
4. **After source mirror-role reconciliation but before any 2.0-only governance/resource state:** a coordinated governed rollback may restore the old role only if both Projects are reconciled and verified; never create dual active authority.
5. **After any 2.0-only governance state that cannot be represented in 1.x:** rollback is a reverse migration/recovery project, not a Git branch switch.

## Initial Compatibility / Version Matrix

| Contract | Initial 2.0 value | Rule |
|---|---|---|
| ProjectFramework | `2.0.0` | Major protocol generation |
| Project Source Schema | `2.0.0` | Typed Governance Resources + Active Resource Registry generation |
| API Protocol | `1.0.0` | First public Query/Transition/Event protocol contract; independent from Framework version |
| Workflow Schema | `1.0.0` | First declarative workflow/transition schema generation; independent from API/Framework |
| AI-ControlTower application | current target release at execution | Independently governed by AI-ControlTower; this plan does not assign/bump it |

Compatibility is explicit. An incompatible mutation client fails closed; broader read compatibility is allowed only where the API contract explicitly declares it.

## Licensing Boundary

| Component | Classification at cutover |
|---|---|
| `projectframework/` protocol/specification assets | public-domain intent; exact dedication instrument selected at legal/release packaging gate |
| `projectframework/migration/v1-baseline/` | retains source provenance/notices and is not evidence that runtime licensing changed |
| AI-ControlTower runtime / existing `src/` / future `control-plane/` | separately governed software license; not made public domain by ProjectFramework import |
| `adapters/` | provider-compatible software licensing; provider terms remain independently binding |
| `apps/` | target software license governance |

No public release projection occurs until the exact legal/publication package has its own approval and verification.

## Plan Self-Review Acceptance

The plan is acceptable only when a fresh self-review confirms:

```text
architecture spec sections covered by merge/cutover tasks or explicitly delegated to named post-cutover plans
no unresolved placeholder language
source and target repository identities exact
V1 baseline and Framework-Source tree exact
AI-ControlTower current router/classifier architecture conflict explicitly reconciled
full source Git history preservation mechanism explicit
Project Source authority separation explicit
no dual active governance authority
existing target actions preserved
initial independent version matrix explicit
component licensing boundary explicit
rollback windows explicit
fresh isolated target worktree required
actual runtime implementation excluded
public mirror direction one-way
```

## Self-Review Result

`PF2_PLAN_MANIFEST_SELF_REVIEW 36/36 PASS` — `2026-09-05T12:42:18+07:00`.

The review covered spec/cutover coverage, no-placeholder rules, task/command consistency, source/target identities, history bridge, target architecture reconciliation, independent version matrix, licensing boundary, rollback, runtime decomposition, and the no-target-mutation preparation boundary.