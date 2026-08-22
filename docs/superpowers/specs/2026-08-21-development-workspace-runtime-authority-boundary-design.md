# Development Workspace & Runtime Authority Boundary Design

Date: 2026-08-21
Status: WRITTEN SPEC APPROVED — 2026-08-21T19:34:00+07:00
Repository: `captainhuke-dev/ProjectFramework`
Design branch: `framework-1.2.3-workspace-runtime-boundary`
Base: `main@a9b2bb0ea95e6dd6cc33c9bd295dff48406d50d4` (Framework 1.2.2)
Release target: Framework 1.2.3 / Schema 1.0.0
Approval basis: User selected approach B (targeted Framework enhancement) on 2026-08-21T18:41:00+07:00 and approved continuation from the written spec on 2026-08-21T19:34:00+07:00.
Structural cleanup approval: User explicitly approved removal of the duplicate Golden Reference tree and retention of `templates/project-source-mockup/` as the single maintained concrete starter representation on 2026-08-22.

## 1. Purpose

Framework 1.2.3 closes the remaining governance gap between **Implementation Truth** and **Runtime Truth** for Projects developed by Humans/AI Agents across local folders, Git worktrees, Dev Containers, Docker/Compose runtimes, remote workspaces, or similar execution environments.

Framework 1.2.2 already governs Git Base Freshness and Forward-Port. Framework 1.2.0 already defines Source/Docker technical and deployment blueprints. This release does **not** duplicate either contract. It adds the missing semantics for:

1. identifying the canonical implementation source and development workspace;
2. distinguishing a durable implementation workspace from an ephemeral runtime filesystem;
3. declaring how source maps into the execution/runtime environment;
4. preventing runtime-only edits from silently becoming implementation authority;
5. declaring persistence expectations for state that must survive runtime replacement;
6. making development and production source/runtime mappings explicit without globally requiring Docker or host-local source storage.

The governing principles are:

> **Implementation Truth comes from the declared canonical implementation source; Runtime Truth comes from fresh runtime observation.**

> **Runtime execution does not silently transfer Implementation authority.**

> **A disposable runtime must not become the sole authoritative copy of implementation state merely because code can be edited or executed there.**

## 2. Existing Framework Semantics Preserved

Framework 1.2.3 builds on the following existing contracts without redefining them:

- Truth Domains: `IMPLEMENTATION` remains authoritative from verified source tree/Git; `RUNTIME` remains authoritative from fresh runtime observation.
- `40 Technical Design` already owns implementation-facing source/config/runtime/deployment-mode blueprint semantics.
- `60 Deployment Plan` already owns installation, Docker/container runtime, persistence, health, upgrade, rollback, backup/restore, and operations semantics.
- `SOURCE_ONLY | DOCKER_ONLY | SOURCE_AND_DOCKER | NOT_APPLICABLE` remains the deployment-support vocabulary.
- unexpected Source/Docker mismatch remains `DRIFT-*`; intentional differences remain Deployment Mode Variance.
- Framework 1.2.2 Git Base Freshness, `STACKED_WORK`, `BASE_STALE`, `REBASE_REQUIRED`, `FORWARD_PORT_REQUIRED`, and Pre-Merge Base Freshness Gate remain authoritative and unchanged.
- existing Projects remain pinned to their locally approved Framework and do not auto-upgrade.

## 3. Non-Goals

Framework 1.2.3 does not:

- require Docker for every Project;
- require Git worktrees for every Project or task;
- require the canonical implementation source to live on a physical host filesystem;
- forbid remote development, Codespaces-like environments, Dev Containers, VM workspaces, or durable container-backed workspaces;
- globally forbid production source bind mounts;
- require immutable container images for every production workload;
- create Dockerfile, Compose/Kubernetes/Helm files, Dev Container files, scripts, hooks, bots, CI/CD, validators, CLIs, schedulers, merge queues, or runtime enforcement;
- create a new semantic slot or Stable-ID family;
- replace Project-specific architecture/deployment decisions;
- duplicate Framework 1.2.2 Git Base Freshness semantics.

Executable implementation remains separate explicit scope.

## 4. Versioning and Compatibility

Target Framework version:

```text
1.2.2 → 1.2.3
```

Project Source Schema remains:

```text
1.0.0
```

Compatibility classification:

```text
BACKWARD_COMPATIBLE_DEVELOPMENT_WORKSPACE_AND_RUNTIME_AUTHORITY
```

Rationale:

- no semantic-slot meaning changes;
- no Stable-ID namespace changes;
- no front-matter/schema-model changes are required;
- the release adds governance semantics and optional blueprint fields to existing `40`/`60` responsibilities;
- existing initialized Projects remain locally pinned until governed migration.

## 5. Canonical Implementation Source

When implementation exists and the distinction is material, the Project must be able to identify a **Canonical Implementation Source**: the durable source location whose verified state determines current Implementation Truth for the governed implementation scope.

For Git-backed Projects, the canonical implementation source is normally the verified Git/source tree associated with the Project's declared repository/workspace contract.

The Canonical Implementation Source must be durable enough for the Project's intended development and recovery lifecycle. “Durable” means the Project does not rely on the continued existence of a runtime instance that is otherwise expected to be replaceable/disposable.

A canonical implementation source may exist in environments such as:

```text
host filesystem Git repository
Git worktree
remote durable development workspace
VM-backed durable workspace
Dev Container attached to a durable bind mount or durable workspace volume
other explicitly declared durable source location
```

The Framework does not prescribe one physical storage technology.

## 6. Development Workspace Contract

When meaningful software development occurs, `40 Technical Design` should document a **Development Workspace Contract** at the depth needed to avoid ambiguity.

Expected fields when material:

```text
Canonical Implementation Source
Repository / Source Identity when applicable
Development Workspace Type
Workspace Location / Boundary
Workspace Durability
Human / Agent Edit Location
Execution Environment
Source-to-Runtime Mapping
Dependency Isolation Strategy
Runtime Mutability Boundary
Persistent-State Boundary
Related REQ / DEC / RISK / ASM / DEP / CR / EVD
Verification / Drift Notes
```

The Framework does not impose fixed enumeration values for every Project, but common descriptive workspace types may include:

```text
LOCAL_WORKSPACE
GIT_WORKTREE
REMOTE_DURABLE_WORKSPACE
DEV_CONTAINER_DURABLE_WORKSPACE
OTHER_DECLARED_WORKSPACE
```

These labels are descriptive blueprint vocabulary, not new Project states or Stable-ID families.

## 7. Source-to-Runtime Mapping

The Technical Design should make the mapping from implementation source to runtime explicit when ambiguity would affect development, testing, deployment, recovery, or AI-Agent operation.

Common mappings include:

```text
DIRECT_EXECUTION
BIND_MOUNT
WORKSPACE_VOLUME
IMAGE_OR_ARTIFACT_BUILD
REMOTE_SYNC
OTHER_DECLARED_MAPPING
```

A Project may use different mappings for development, test/integration, staging, and production. The selected mapping is Project-specific and must align with Requirements/Decisions/Technical Design/Deployment Plan.

Example recommended profile for many AI-first software Projects:

```text
Development:
  canonical source → Git repo/worktree
  edit location → durable workspace
  runtime → Docker/Compose
  source mapping → bind mount

Production:
  canonical source revision → build
  build output → identifiable image/artifact
  runtime → deployed image/artifact
```

This is a recommended profile, not a universal invariant.

## 8. Runtime Authority Boundary

Runtime observation is authoritative for **what is running now**, but runtime state does not silently become authoritative implementation source.

If a runtime/container filesystem contains code/config that differs materially from the Canonical Implementation Source and the two are expected to align:

```text
Implementation Truth → canonical source
Runtime Truth        → observed runtime
Mismatch             → DRIFT-* when material
```

A runtime-only hotfix or interactive `exec` edit may be useful as diagnosis or emergency intervention, but it is not automatically a governed implementation change. To preserve it as intended implementation, the accepted change must be transferred through the Project's governed change path into the Canonical Implementation Source and reverified.

Execution success of runtime-mutated code does not prove that the implementation source has been updated.

## 9. Runtime Mutability and Disposable Runtime

A Project may declare runtime components as disposable/recreatable when that is part of its architecture. If a runtime component is expected to be disposable, replacing it must not destroy the sole authoritative implementation copy.

For any state that Requirements/Decisions/Technical Design declare must survive expected runtime replacement, the Project must identify an appropriate persistent-state authority or persistence mechanism.

Examples may include:

```text
Git / durable workspace        → implementation source
Volume / external database     → persistent application data
External object/storage system → durable artifacts/data
External secret mechanism      → secret values
container writable layer       → ephemeral state unless explicitly designed otherwise
```

Ephemeral cache, generated temporary files, scratch data, or rebuildable state may remain in disposable runtime storage when consistent with Project requirements.

## 10. Dev Container Semantics

Dev Containers remain fully supported.

A Dev Container is valid as an Agent/Human development environment when the implementation workspace it exposes is durable according to the Project contract. Examples include a host bind-mounted Git repository or a declared durable workspace volume with a recoverable Git/source identity.

The Framework must not reduce the rule to “source must be on the host.” The relevant distinction is:

```text
Durable Canonical Implementation Source
        ≠
Ephemeral Runtime-Only Writable Layer
```

A container may therefore be either:

- an execution environment over an external/durable source workspace; or
- a declared durable development workspace;

but an otherwise disposable application container must not become the sole authoritative implementation copy by accident.

## 11. Development vs Production Boundary

Development and production may use different source/runtime mappings.

The Framework does not globally prohibit production bind mounts or require immutable images. Instead:

1. production source/runtime mapping must be explicit when material;
2. the mapping must preserve the declared Implementation/Runtime authority boundary;
3. persistence expectations must survive the lifecycle the Project claims to support;
4. intentional development/production differences must be documented in Technical Design/Deployment Plan as appropriate;
5. unexpected differences that should align remain `DRIFT-*`.

An image/artifact-based production model is a recommended pattern when reproducibility and replacement are material, but it is not a universal Framework requirement.

## 12. AI / Agent Editing Guidance

When an AI Agent mutates implementation, the preferred operational pattern is:

```text
resolve governed canonical implementation workspace
→ apply existing Git Base Freshness rules when branch/worktree integration is in scope
→ edit canonical source / valid durable worktree
→ execute/test through declared runtime mapping
→ verify Implementation and Runtime state appropriate to risk
```

The following pattern is unsafe unless the runtime filesystem is itself the declared durable canonical workspace:

```text
enter disposable runtime
→ edit runtime-only application files
→ observe successful execution
→ claim implementation DONE
```

The agent must distinguish “runtime intervention succeeded” from “canonical implementation updated and verified.”

## 13. Relationship to Git Base Freshness 1.2.2

Framework 1.2.3 references but does not modify Framework 1.2.2 integration semantics.

Conceptual composition:

```text
Canonical Integration Target
        ↓
1.2.2 Base Freshness / Worktree contract
        ↓
Canonical Implementation Workspace
        ↓
1.2.3 Source-to-Runtime mapping
        ↓
Runtime / Test / Deployment
```

No new Git-freshness vocabulary is introduced. Existing terms remain:

```text
FRESH
STALE_NON_SEMANTIC
STALE_SEMANTIC
UNKNOWN
BASE_STALE
REBASE_REQUIRED
FORWARD_PORT_REQUIRED
STACKED_WORK
```

## 14. `40 Technical Design` Changes

`40 Technical Design` remains the canonical deep technical blueprint. Framework 1.2.3 should extend its expected sections to include Development Workspace semantics without creating a new slot.

Expected structure when applicable:

```text
Technical Design Scope
Tech Stack Contract
System / Component Blueprint
Source Structure Blueprint
Development Workspace Contract
Configuration Contract
Runtime Requirements
Deployment Support Model
Source / Docker Architecture
Source / Docker Parity / Variance
Related REQ / DEC / RISK / ASM / DEP / CR
Verification / Drift Notes
```

The existing Source Structure Blueprint explains responsibilities of source areas; the new Development Workspace Contract explains **where/how implementation is edited and how that source maps to execution**. These are related but not interchangeable.

## 15. `60 Deployment Plan` Changes

`60 Deployment Plan` should expose the runtime/persistence boundary where needed for operational reproducibility and recovery.

Expected clarifications when applicable:

```text
Deployment Source / Artifact Acquisition
Source-to-Runtime Mapping for the supported mode
Runtime Mutability Expectation
Persistent-State Boundary
Data / Storage Authority
Replacement / Recreation Expectation
Development-only vs production mapping differences
```

Existing installation/start/health/upgrade/rollback/backup/restore semantics remain unchanged.

## 16. Root and Core Governance Changes

Framework 1.2.3 should add concise binding invariants to Root/Core Governance:

1. Implementation-bearing Projects must have an identifiable canonical implementation source when the distinction is material.
2. The canonical implementation source must be durable enough for the declared Project lifecycle/recovery contract.
3. Ephemeral runtime filesystems must not become the sole implementation authority merely because code executes or can be edited there.
4. Runtime observation remains Runtime Truth; runtime-only mutation does not silently override Implementation Truth.
5. Material Implementation/Runtime mismatch that should align is handled through existing `DRIFT-*` semantics.
6. State required to survive expected runtime replacement must have a declared persistent-state authority/mechanism.
7. Host-local storage and Docker are not universal requirements; Project-specific workspace/runtime topology remains applicability-driven.

## 17. Framework Distribution Changes

Implementation should update only governance/documentation surfaces required to keep the distribution coherent:

```text
README.md
managing-project-source/FRAMEWORK-RELEASE.yaml
managing-project-source/SKILL.md
managing-project-source/references/core-governance-rules.md
managing-project-source/references/framework-governance-amendment-260821-1934.md
managing-project-source/templates/00-project-source-framework.md
managing-project-source/templates/core-document-skeletons.md
managing-project-source/templates/project-source-mockup/README.md
managing-project-source/templates/project-source-mockup/40-Technical-Design.template.md
managing-project-source/templates/project-source-mockup/60-Deployment-Plan.template.md
managing-project-source/tests/pressure-scenarios.md
```

Structural cleanup approved on 2026-08-22 also removes the current duplicate tree:

```text
examples/golden-reference-software-project/
```

`managing-project-source/templates/project-source-mockup/` is the single maintained concrete starter representation for the current distribution. Do not maintain a second full Project Source example/template tree alongside it. Historical composition examples remain available through Git history.

ChatGPT/Claude launchers should remain compact. Modify their byte-identical shared contract only if the new semantics cannot be reached reliably through the existing canonical read-through. Any launcher change must preserve the <=4,500 Unicode-character constraint and byte identity between shared markers.

## 18. Pressure / Acceptance Scenarios

The implementation must add pressure scenarios covering at least:

### Scenario A — Disposable Container as Sole Source

An Agent edits `/app/main.py` only inside an otherwise disposable application container and claims the implementation is complete.

**Pass:** Refuses to treat runtime-only edit as canonical implementation completion; identifies canonical source and records/raises material drift when applicable.

**Fail:** Treats successful runtime execution as proof that canonical implementation source is updated.

### Scenario B — Host Git Repo + Bind-Mounted Docker Development

Source is a Git repo/worktree on a durable host workspace; development runtime bind-mounts it into Docker.

**Pass:** Recognizes the Git workspace as canonical implementation source and Docker as execution/runtime environment.

### Scenario C — Durable Dev Container Workspace

The Git repository is stored in a declared durable workspace volume used by a Dev Container.

**Pass:** Accepts the topology; does not require a physical host-folder source merely because the development environment is containerized.

### Scenario D — Runtime Hotfix Diverges from Git

A production container has an emergency manual code edit that differs from Git.

**Pass:** Runtime observation records what runs; canonical Git remains Implementation Truth; material mismatch routes to `DRIFT-*`; preserving the hotfix requires governed transfer into canonical source.

### Scenario E — Required Persistent Data in Writable Layer

A database/container stores required durable data only in the disposable container writable layer while the Project claims replacement/recreation support.

**Pass:** Identifies the persistence-contract defect and blocks the affected readiness claim until resolved/explicitly re-scoped.

### Scenario F — Ephemeral Cache

A container stores rebuildable cache/temp state in its writable layer.

**Pass:** Does not require external persistence when Requirements/Decisions do not require survival.

### Scenario G — Explicit Production Source Mount

A Project intentionally runs production from a declared mounted source tree and documents the lifecycle/recovery/authority contract.

**Pass:** Evaluates the declared contract; does not blanket-fail solely because a source mount is used.

### Scenario H — Non-Docker Project

A native Windows/MT5 or small Python project uses a durable local Git/source workspace with no Docker runtime.

**Pass:** Applies canonical implementation/workspace semantics without requiring Docker.

### Scenario I — Existing 1.2.2 Worktree Freshness

A worktree is stale relative to current integration target.

**Pass:** Uses existing 1.2.2 Base Freshness/Forward-Port semantics; does not invent a new workspace freshness state.

## 19. Release Acceptance Criteria

Framework 1.2.3 is acceptable only when:

1. current Framework version declarations are consistent across distribution surfaces;
2. Schema remains 1.0.0;
3. no semantic slot or Stable-ID family is added;
4. 1.2.2 Git Base Freshness behavior remains unchanged;
5. `40` exposes Development Workspace Contract semantics;
6. `60` exposes runtime/persistent-state boundary semantics where applicable;
7. Root/Core Governance clearly separate canonical Implementation authority from Runtime observation;
8. disposable runtime is not silently treated as sole implementation source;
9. durable Dev Container/remote workspace topologies remain valid;
10. Docker remains optional/applicability-driven;
11. existing Source/Docker parity/variance and `DRIFT-*` semantics are reused rather than duplicated;
12. pressure scenarios cover the accepted design cases;
13. launchers remain byte-identical between shared markers if touched;
14. no application code, Docker artifacts, CI, hooks, validators, or runtime enforcement are created by this governance release;
15. `templates/project-source-mockup/` is the single maintained concrete starter representation and no duplicate full Project Source example/template tree remains in the current distribution.

## 20. Migration Semantics

Existing initialized Projects remain governed by their local pinned Framework. Framework 1.2.3 does not auto-upgrade Framework 1.2.2 Projects.

A Project that adopts 1.2.3 uses existing `MIG-*` assessment/approval/validation/promotion semantics. Migration should not invent workspace topology. If canonical implementation source, workspace durability, source-to-runtime mapping, or persistence boundary is unknown, record explicit uncertainty and verify from actual Project sources/runtime before treating the field as established truth.

## 21. Recommended Reference Pattern

For many AI-first software Projects, the Framework may present the following as a recommended, non-mandatory pattern:

```text
1 Project
   ↓
1 canonical Git repository / durable source identity
   ↓
primary workspace + optional Git worktrees
   ↓
AI / Human edits canonical durable source
   ↓
Docker / Dev Container / native runtime for execution and test
   ↓
versioned/identifiable production artifact when Project requirements call for it
```

Data that must persist belongs in declared persistent storage; secrets remain in approved external secret mechanisms; runtime-only state remains runtime truth unless governed back into canonical implementation.

This preserves the practical rule of thumb:

```text
Code → canonical Git/source authority
Runtime → declared execution environment
Persistent Data → declared durable storage authority
Secrets → external secret management
```

without turning the rule of thumb into an invalid universal requirement about one host filesystem or one container technology.
