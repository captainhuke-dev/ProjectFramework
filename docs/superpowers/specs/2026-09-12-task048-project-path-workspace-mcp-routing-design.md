# TASK-048 `[Project Path]` Workspace & MCP Routing — Design

Date: `2026-09-12` (Asia/Bangkok)
Task: `TASK-048`
Design state: `USER_APPROVED_FINAL_DESIGN / WRITTEN_SPEC_SELF_REVIEWED / AWAITING_USER_REVIEW`
Implementation state: `NOT_STARTED`
Approval basis: user approved Architecture Option 1, Auto Fallback (A), Production deploy/run-only boundary, append-only fallback log (A), Checkpoint Failback (B), and Design Sections 1–4 in chat on `2026-09-12`; during written-spec review the user additionally requested a Local ↔ Remote Durable Develop Workspace Relocation Contract before final spec approval.
Base repository: `captainhuke-dev/ProjectFramework`
Design baseline: `main@a1da22d64ff8e30658a4aaf8b675705a0e043dc9`
Target release: Framework `1.16.0` / Schema `1.0.0` / release format `3`

## 1. Purpose

Extend the registered `[Project Path]` strict interface so an Agent can determine, without inference:

1. where development source is edited, built, and tested;
2. where production is deployed and run;
3. which Local or Remote Durable workspace is the one active Develop Workspace for the affected scope and how development relocates safely between them;
4. which MCP/tool is the exact Primary execution path;
5. which explicitly declared MCPs may be used as ordered fallback;
6. how fallback, unknown-result recovery, and failback behave; and
7. where fallback incidents are durably recorded.

The design must preserve existing ProjectFramework authority separation. Correct location and an eligible MCP do not grant mutation, deployment, push, Root/Binding, secret, disclosure, or other authority.

## 2. Problem

Current `[Project Path]` surfaces Framework/Git/Storage/MCP/Workspace location semantics, but three operational ambiguities remain material:

- one Project may have separate **Develop Workspace** and **Production Workspace** roles, and an Agent must know where source may be edited/built versus where an artifact may only be deployed/run;
- the active Develop Workspace may move between a local durable workspace and a remote durable development workspace, but Git Remote itself is not an interactive workspace and promotion must not lose or fork required implementation state; and
- an MCP path/selection must be exact. An Agent must never select an undeclared substitute merely because another MCP is connected, recent, similar, or available.

Existing contracts already provide most foundations:

- Development Workspace and Runtime Authority separation;
- Project Tool / MCP Execution Profile with `primary_tool`, `fallback_mode`, `fallback_order`, and failure policy;
- MCP continuity/idempotent resume semantics;
- strict Registered Command interfaces; and
- Project Location Binding and `[Project Path]` verification behavior.

TASK-048 composes and tightens these existing contracts rather than creating a parallel authority model.

## 3. Approved Architecture

Chosen architecture: **Extend `[Project Path]` and compose existing canonical owners.**

```text
FRAMEWORK-001 / Project Location Binding
  → canonical repository + environment-scoped Local Workspace binding/routing truth

40 Technical Design / Development Workspace Contract
  → canonical Develop Workspace role/type/location/durability, active-workspace semantics,
    Canonical Implementation Source relationship, and workspace mutation-policy semantics

60 Deployment Plan when applicable
  → canonical deployment/runtime target and build/deployment mapping semantics

Project-Execution/tools.md
  → exact MCP execution-selection policy

Project-Execution/fallback-log.md
  → append-only history of actual fallback/recovery events

[Project Path]
  → fresh unified read/verification view over the above canonical owners
  → fail closed for affected Material work when those owners materially contradict one another
```

Rejected alternatives:

- placing all MCP routing policy into `FRAMEWORK-001`, because volatile operational selection would make Root mutation unnecessarily frequent; and
- introducing a new `Project-Execution/routing.md`, because it would duplicate truth already owned by Project Location Binding and `tools.md`.

TASK-048 also rejects moving Develop/Production workspace-role or source-mutation semantics into `FRAMEWORK-001`. Project Location Binding continues to own location/routing bindings only; `40 Technical Design` owns Development Workspace Contract semantics, and `60 Deployment Plan` owns deployment/runtime mapping when applicable.

## 4. Existing Contracts Reused

TASK-048 preserves and composes:

- `Project Location Binding ≠ current branch/worktree ≠ Canonical Integration Target ≠ Canonical Implementation Source ≠ Runtime authority ≠ AUTH/Risk authority`;
- Implementation Truth comes from the declared canonical implementation source;
- Runtime Truth comes from fresh runtime observation;
- runtime-only edits do not silently become implementation authority;
- Tool selection policy ≠ Tool availability ≠ Location ≠ Authority;
- `fallback_mode: NONE` means no undeclared/automatic substitute;
- `ORDERED_ALLOW_LIST` permits only declared fallback entries in declared order;
- unknown execution outcome must be verified before retry to avoid duplicate effects;
- Registered Commands are Strict Governed Interfaces;
- existing workspace vocabulary includes `LOCAL_WORKSPACE`, `GIT_WORKTREE`, and `REMOTE_DURABLE_WORKSPACE`;
- Git Remote/repository publication/synchronization identity remains distinct from an actual durable Develop Workspace where edits/build/tests execute; and
- Brownfield Projects do not silently adopt new bindings/policy merely because the Framework distribution evolves.

## 5. Workspace Role Contract

### 5.1 Develop Workspace

The Develop Workspace is the implementation workspace for the declared scope.

Canonical role:

```text
EDIT
BUILD
TEST
PACKAGE
VERIFY
```

Source mutation is `ALLOWED` only when the workspace is valid for the active Canonical Implementation Source, required binding/source identity checks pass, and independent action authority permits the mutation. Workspace role never creates `AUTH-*` by itself.

The Agent must not infer a Develop Workspace from recency, an active editor, MCP workspace list, mounted folders, search ranking, or similarly named directories.

### 5.2 Production Workspace

The Production Workspace is a deployment/runtime target only.

Canonical role:

```text
DEPLOY
RUN
HEALTH_CHECK
OBSERVE_RUNTIME
```

Hard invariant:

```text
Production Workspace direct source mutation = FORBIDDEN
```

The Agent must not treat direct Production source edits, interactive runtime hotfixes, or writable runtime layers as governed implementation changes.

If Production requires a code/config correction:

```text
observe/diagnose Production
→ change canonical source in Develop Workspace
→ test/build/package
→ deploy a verified artifact
→ verify Production runtime result
```

### 5.3 Canonical Ownership and Binding Representation

`FRAMEWORK-001` / Project Location Binding remains a location/routing authority. It does not become the owner of Develop/Production role semantics or source-mutation permission.

When a local filesystem workspace binding is applicable, existing `project_location_binding.local_workspaces` stays location-focused:

```yaml
local_workspaces:
  - environment_scope: "<USER_CONFIRMED_ENVIRONMENT_SCOPE>"
    binding_state: "<BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED>"
    canonical_path: "<ABSOLUTE_LOCAL_PATH_OR_UNKNOWN>"
    repository: "<OWNER/REPOSITORY_OR_UNKNOWN_OR_NOT_APPLICABLE>"
    repository_url: "<CANONICAL_REPOSITORY_URL_OR_UNKNOWN_OR_NOT_APPLICABLE>"
    verification_status: "<VERIFIED | USER_CONFIRMED | VERIFICATION_REQUIRED>"
    last_verified_at: "<ISO8601_OR_UNKNOWN>"
```

Do not add `workspace_role`, `source_mutation`, active-Develop ownership, Canonical Implementation Source, or Production runtime authority to `project_location_binding.local_workspaces`. Location correctness and binding state never grant source-mutation authority.

When material, `40 Technical Design` / Development Workspace Contract owns the semantic workspace profile, for example:

```text
Develop Workspace
  Logical Role: DEVELOPMENT
  Workspace Type: LOCAL_WORKSPACE | GIT_WORKTREE | REMOTE_DURABLE_WORKSPACE | OTHER_DECLARED_WORKSPACE
  Active Workspace Locator: <DECLARED_LOCATOR>
  Workspace Durability: <DECLARED_DURABILITY>
  Repository / Source Identity: <VERIFIED_IDENTITY>
  Canonical Implementation Source Relationship: <DECLARED_RELATIONSHIP>
  Human / Agent Edit Location: <DECLARED_LOCATION>
  Source Mutation Policy: ALLOWED only when separately authorized
```

For a Local Develop Workspace, `40` references the applicable environment-scoped Local Workspace Binding rather than creating a competing local binding. A Remote Durable workspace may use a declared durable remote locator in `40` because Git Remote/repository identity and Remote Develop Workspace identity are distinct concepts.

Production role/source-mutation semantics are likewise technical/deployment semantics rather than Location Binding authority. `40 Technical Design` describes the role/boundary and `60 Deployment Plan` resolves the concrete deployment/runtime target and mapping when deployment is applicable.

Non-filesystem deployment/runtime targets remain represented through existing applicable Technical Design / Deployment Plan semantics; `[Project Path]` must surface the resolved target without fabricating a filesystem path.

`[Project Path]` composes these owners. A material contradiction among Project Location Binding, `40 Technical Design`, `60 Deployment Plan`, repository/source identity, or fresh observation is `MISMATCH`/`NOT_VERIFIED` for the affected dimension and fails closed for affected Material mutation; the command must not choose an owner by recency.

### 5.4 Develop Workspace Relocation Contract

TASK-048 explicitly supports relocation of the active Develop Workspace between a verified Local workspace and a verified Remote Durable workspace.

Supported directional pattern:

```text
LOCAL_WORKSPACE ↔ REMOTE_DURABLE_WORKSPACE
```

Git Remote such as `origin` is the repository synchronization/publication target. It is **not** itself a Develop Workspace. Remote development requires an actual durable remote workspace (for example a governed remote VM/Codespaces-like/durable cloud workspace) that can prove the bound repository/source identity and execute the declared development workflow.

For one affected implementation scope, exactly one Develop Workspace is the active edit/build/test location at a time. Multiple durable copies may exist for recovery/synchronization, but ambiguous concurrent active development ownership fails closed for Material source mutation until the active workspace/scope is resolved.

Minimum relocation preconditions:

```text
current active Develop Workspace resolved
→ repository/source identity verified
→ current required implementation state durably checkpointed in Git/source authority
→ no required completed work exists only as uncommitted state in the source workspace
→ Git Remote/source synchronization target freshly observed when Git-backed
→ relocation target durability and recovery assumptions verified
→ target workspace repository/source identity verified
→ target workspace synchronized to the intended source revision
→ target working-tree/source state verified and understood
→ applicable authority for any persistent Project Source / binding change satisfied
```

Canonical relocation flow:

```text
freeze relocation boundary
→ checkpoint/commit required source state
→ fresh-observe repository remote and intended source revision
→ prepare/access target durable workspace
→ fetch/sync target to intended source revision
→ verify repository identity + source revision + target workspace integrity
→ determine separately whether relocation changes `40` workspace semantics, `FRAMEWORK-001` Local Workspace Binding, or both
→ update/promote the governed `40 Technical Design` workspace contract under applicable Project authority
→ Preview and obtain/apply explicit approval only when a persistent `FRAMEWORK-001` Local Workspace Binding change is also required
→ promote target as the one active Develop Workspace for the affected scope in the governed workspace contract
→ demote prior workspace from active development routing
→ verify source mutation/build/test now resolve only to the promoted workspace
```

Reverse relocation from Remote Durable → Local follows the same contract and does not receive weaker checks.

Relocation safety rules:

1. Do not infer the target workspace from recency, active editor state, MCP workspace lists, mounts, search ranking, or similarly named folders.
2. Do not treat a repository URL or Git Remote name as a workspace locator.
3. Do not promote a target whose repository identity, intended source revision, durability, or working-tree state is unresolved.
4. Do not abandon required uncommitted implementation state in the source workspace; commit/checkpoint or explicitly reconcile it before promotion.
5. Do not create two simultaneously active Develop Workspaces for the same affected scope unless a separately governed multi-writer architecture explicitly defines that model; TASK-048 does not create one.
6. A persistent Local Workspace Binding/Project Location Binding change retains existing User Explicit Approval plus `FRAMEWORK-001` revision/validation/promotion/history rules; a Remote Durable active-workspace change does not invent a Root binding when no Local Workspace Binding delta exists.
7. Relocation changes development routing only. It does not transfer Git integration authority, push/publication authority, deployment authority, MCP/tool authority, or other `AUTH-*` scope.

`[Project Path]` must be able to show the active workspace type/locator and source identity without fabricating a remote filesystem path when the remote platform uses a non-filesystem stable locator.

## 6. Exact MCP Execution Policy

`Project-Execution/tools.md` remains the canonical execution-selection policy surface.

The target policy shape extends the existing profile with explicit failback semantics:

```yaml
profile_name: "default"
profile_state: "ACTIVE"
primary_tool: "<PRIMARY_MCP_ID>"
allowed_tools:
  - "<PRIMARY_MCP_ID>"
disallowed_tools: []
fallback_mode: "NONE | ORDERED_ALLOW_LIST"
fallback_order:
  - "<FALLBACK_MCP_ID_1>"
  - "<FALLBACK_MCP_ID_2>"
failure_policy: "FAIL_CLOSED | READ_ONLY_DIAGNOSTIC_ONLY"
failback_policy: "CHECKPOINT_FAILBACK"
review_trigger: "<EVENT_OR_NOT_APPLICABLE>"
```

Rules:

1. `primary_tool` is the default execution MCP/tool.
2. `fallback_mode: NONE` means no execution fallback is permitted.
3. `ORDERED_ALLOW_LIST` permits only `fallback_order`, first eligible entry wins.
4. An undeclared MCP/tool is never eligible merely because it is available.
5. `disallowed_tools` wins over allowed/fallback declarations.
6. Availability never creates authority or policy eligibility.
7. `CHECKPOINT_FAILBACK` means recovery to Primary occurs only after the current bounded action/logical checkpoint is safely completed and persisted.

## 7. MCP ACTIVE / Eligibility Contract

An MCP is `ACTIVE` and execution-eligible only when all applicable checks succeed:

```text
endpoint/capability reachable
+ authentication/session usable when applicable
+ required capability/tool available
+ allowed by active Project-Execution policy
+ bound Project/workspace/repository target identity verified
= ACTIVE / ELIGIBLE
```

Command-facing MCP state is limited to:

```text
ACTIVE
UNAVAILABLE
VERIFICATION_REQUIRED
```

A reason may refine the observation, for example:

```text
CONNECTION_FAILED
AUTH_FAILED
CAPABILITY_UNAVAILABLE
TARGET_MISMATCH
POLICY_DISALLOWED
```

These are diagnostic/presentation values, not Project lifecycle or Stable-ID families.

## 8. Auto Fallback Lifecycle

Approved behavior: **Auto Fallback**.

Before a Material execution action:

```text
resolve Primary MCP
→ fresh-check policy + availability + target identity
```

If Primary is eligible:

```text
Primary executes action
```

If Primary is not eligible and `fallback_mode: ORDERED_ALLOW_LIST`:

```text
observe Primary failure
→ evaluate fallback_order from first to last
→ choose first ACTIVE + eligible fallback
→ persist FALLBACK_STARTED event
→ execute bounded action via fallback
```

If no declared fallback is eligible:

```text
FAIL_CLOSED
```

The Agent stops the affected Material execution and waits until an explicitly declared Primary or fallback becomes eligible. It must not select another tool by recency, similarity, ranking, connected state, or convenience.

For Material mutation through fallback, durable fallback-event persistence is part of the safety contract. If the Agent cannot persist the required fallback incident record, the affected Material mutation fails closed.

## 9. Unknown-Result / Mid-Action Failure Safety

If the MCP connection fails after an action may have been submitted and the result is unknown:

```text
RESULT_VERIFICATION_REQUIRED
→ inspect resulting state through an eligible declared MCP/tool
→ if already applied: checkpoint result; do not repeat
→ if proven not applied: resume/retry under valid authority
→ if outcome cannot be proven: FAIL_CLOSED
```

The Agent must never assume an unknown-result operation failed and blindly repeat it.

This protects non-idempotent or side-effecting operations such as writes, commits, deployments, record creation, or external actions.

`RESULT_VERIFICATION_REQUIRED` is operational workflow vocabulary only, not a new lifecycle/Stable-ID state.

## 10. Checkpoint Failback Lifecycle

Approved behavior: **Checkpoint Failback**.

When Primary recovers while fallback is executing:

```text
Primary observed ACTIVE again
→ do not switch in the middle of the current bounded action
→ complete and verify current action/checkpoint via fallback
→ persist/checkpoint result
→ verify Primary availability + capability + target identity again
→ append recovery/failback event
→ next action uses Primary
```

If Primary becomes reachable but target identity or another eligibility check remains unresolved, failback does not occur.

If the current fallback fails before the checkpoint completes, the Agent applies the same unknown-result verification rules and may evaluate the next declared fallback in order only after resulting-state safety is established.

## 11. Fallback Log Contract

New applicability-driven artifact:

```text
Project-Execution/fallback-log.md
```

Purpose: append-only, reconstructable history of actual MCP fallback/recovery events.

It is:

- outside the `Project-Source/00–99` semantic-slot namespace;
- not Root Governance;
- not an authority registry;
- not a new Stable-ID family;
- not a credential/secret store; and
- not required for Projects that never enable ordered fallback until applicable.

A correlation label such as `MCP-FB-20260912-001` is a log identifier only, not a Project Stable ID.

Minimum incident/event fields when applicable:

```text
Incident
Timestamp
Event Type
Primary MCP
Observed Primary State
Failure / Recovery Reason
From MCP
To MCP
Affected Action
Target Identity / Scope
Checkpoint
Result Verification
Recovery State
Failback Policy
Failback At
Incident State
```

Expected event progression may include:

```text
FALLBACK_STARTED
FALLBACK_TRANSITION
PRIMARY_RECOVERED
FAILBACK_COMPLETED
INCIDENT_CLOSED
```

Corrections are appended as correction/superseding events; prior incident history is not silently rewritten.

If an incident materially affects governed Project truth, completion evidence, release/deployment result, or another canonical domain, the normal applicable `EVD-*`/change/lifecycle rules may additionally apply. Routine fallback history itself does not require one `EVD-*` per event.

## 12. Build / Deployment Mapping

`[Project Path]` must make the distinction explicit:

```text
Build Source/Target ≠ Run/Production Target
```

The canonical operational flow is:

```text
Develop Workspace
→ edit source
→ test
→ build/package artifact/image
→ verify source/artifact identity
→ deploy to Production Workspace/target
→ run / health-check / observe runtime
```

When material, the Project should be able to identify the deployed unit sufficiently to answer which source revision produced the running artifact.

Typical identity fields may include:

```text
source_commit
build_id
artifact_name
artifact_hash_or_digest
target_environment
deployed_at
```

Not every Project needs every field, but unsupported identity must remain explicit as `VERIFICATION_REQUIRED` rather than being inferred.

The canonical design/deployment mapping remains owned by existing `40 Technical Design` / `60 Deployment Plan` when applicable. `[Project Path]` reads/verifies the mapping; it does not become deployment-plan authority.

## 13. Production Drift Rule

If Production source/config/runtime state materially differs from what the governed artifact/source mapping says should be running:

```text
Implementation Truth = canonical source / verified artifact lineage
Runtime Truth        = fresh Production observation
Unexpected mismatch  = DRIFT candidate when material
```

The Agent must not repair this by direct Production source editing.

Normal repair path:

```text
observe drift
→ diagnose
→ repair canonical source/build/deployment flow
→ rebuild/redeploy
→ verify resulting Production state
```

## 14. Strict `[Project Path]` Interface

`[Project Path]` remains a literal-bracket, case-insensitive Registered Command and a Strict Governed Interface.

Required top-level order:

```text
1. Framework Path
2. Git Path
3. Storage Path
4. Develop Workspace
5. Production Workspace
6. MCP Execution
7. Build / Deployment Mapping
8. Continuity
```

Canonical structure:

```text
[Project Path]

Framework Path
  Upstream: ...
  Status: MATCH | MISMATCH | NOT_VERIFIED

Git Path
  Repository: ...
  Project Source: ...
  Status: MATCH | MISMATCH | NOT_VERIFIED

Storage Path
  ...

Develop Workspace
  Workspace Type: LOCAL_WORKSPACE | REMOTE_DURABLE_WORKSPACE | OTHER_DECLARED_WORKSPACE
  Active Develop Workspace: ...
  Path/Locator: ...
  Role: EDIT / BUILD / TEST / PACKAGE
  Source Mutation: ALLOWED
  Repository Remote: ...
  Repository / Source Identity: ...
  Source Revision: ...
  Status: MATCH | MISMATCH | NOT_VERIFIED

Production Workspace
  Applicability: APPLICABLE | NOT_APPLICABLE | VERIFICATION_REQUIRED
  Path/Locator: ... | NOT_APPLICABLE
  Role: DEPLOY / RUN / HEALTH_CHECK | NOT_APPLICABLE
  Source Mutation: FORBIDDEN
  Runtime Target: ... | NOT_APPLICABLE
  Status: MATCH | MISMATCH | NOT_VERIFIED | NOT_APPLICABLE

MCP Execution
  Primary MCP: ...
  Primary Status: ACTIVE | UNAVAILABLE | VERIFICATION_REQUIRED
  Fallback Mode: NONE | ORDERED_ALLOW_LIST
  Fallback Order: ...
  Active Execution MCP: ...
  Failback Policy: CHECKPOINT_FAILBACK

Build / Deployment Mapping
  Build Source: DEVELOPMENT
  Deployment Applicability: APPLICABLE | NOT_APPLICABLE | VERIFICATION_REQUIRED
  Artifact Identity: ... | NOT_APPLICABLE
  Run Target: PRODUCTION | NOT_APPLICABLE
  Status: MATCH | MISMATCH | NOT_VERIFIED | NOT_APPLICABLE

Continuity
  Execution State: PRIMARY | FALLBACK_ACTIVE | FAIL_CLOSED
  Latest Fallback Event: ...
  Fallback Log: Project-Execution/fallback-log.md | NOT_APPLICABLE
```

If a required/applicable value cannot be verified, the field remains present and uses explicit unknown/not-verified representation. Strict-interface compliance must not hide a field simply because evidence is unavailable.

`Source Mutation: ALLOWED` in the Develop Workspace section is derived from the governed `40 Technical Design` workspace role and means only that source mutation is compatible with that workspace role; it never grants mutation authority. Production remains `FORBIDDEN` for direct source mutation regardless of action authority.

For Production Workspace and deployment mapping, applicability has exact semantics:

- `APPLICABLE` — Project truth declares a Production/runtime target; unresolved target details use `NOT_VERIFIED` and affected deploy/run mutation fails closed.
- `NOT_APPLICABLE` — authoritative Project truth explicitly establishes that no Production/runtime target is applicable; exact strict output uses `Path/Locator: NOT_APPLICABLE`, `Role: NOT_APPLICABLE`, `Runtime Target: NOT_APPLICABLE`, and `Status: NOT_APPLICABLE`.
- `VERIFICATION_REQUIRED` — available Project truth is insufficient to establish whether Production is applicable; do not infer `NOT_APPLICABLE` merely from absence. Use `Status: NOT_VERIFIED` and fail closed only for actions that require the unresolved Production/runtime dimension.

`NOT_APPLICABLE` here is a command-facing diagnostic/applicability label for the new strict sections. It does not alter existing Project Location Binding state families or create a Stable-ID/lifecycle state. `PRIMARY | FALLBACK_ACTIVE | FAIL_CLOSED` likewise remain command-facing execution-state labels only.

## 15. Fail-Closed Matrix

| Condition | Required result |
|---|---|
| Develop Workspace not verified | block source mutation/build for affected scope |
| More than one unresolved active Develop Workspace for the same scope | block source mutation/build until one active workspace is resolved |
| Relocation target repository/source identity or intended revision not verified | do not promote target; keep relocation fail-closed |
| Required implementation state exists only as uncommitted source-workspace state | do not relocate until checkpoint/commit/reconciliation preserves it |
| Persistent relocation changes Project Location Binding without required approval/promotion | block persistent relocation |
| Project truth explicitly says Production is not applicable | show exact `NOT_APPLICABLE` representation; do not invent a target; no Production-specific blocker exists |
| Production applicability itself cannot be established | show `Applicability: VERIFICATION_REQUIRED` + `Status: NOT_VERIFIED`; block only actions that require Production/runtime resolution |
| Production Applicability is `APPLICABLE` but Workspace/target is not verified | block deploy/run mutation for affected scope |
| Direct source edit in Production | `FORBIDDEN` |
| Primary unavailable + `fallback_mode: NONE` | `FAIL_CLOSED` |
| Primary unavailable + eligible ordered fallback | auto-select first eligible fallback |
| MCP target identity mismatch | MCP is ineligible |
| Undeclared MCP is online | do not use it |
| Connection lost with action result unknown | `RESULT_VERIFICATION_REQUIRED` |
| Result cannot be proven | `FAIL_CLOSED` |
| Primary recovers mid-action | complete checkpoint before failback |
| Required fallback event cannot be persisted before Material fallback mutation | `FAIL_CLOSED` |

## 16. Brownfield Compatibility

Existing initialized Projects remain pinned to their local Framework and do not silently adopt TASK-048 semantics.

When a Brownfield Project upgrades to the adopting Framework release:

- an existing verified implementation `Workspace Path` may be Previewed/migrated as the Develop Workspace when evidence supports that classification;
- an existing Local Develop Workspace remains active until a governed relocation explicitly promotes a verified Remote Durable workspace (or another declared target); a connected remote workspace is never auto-promoted;
- Local ↔ Remote Durable relocation uses Section 5.4 and never treats Git Remote alone as a workspace;
- Production Workspace must never be inferred solely from an existing workspace/path. Explicit no-Production truth becomes `NOT_APPLICABLE`; an expected-but-unresolved Production target is `APPLICABLE` + `NOT_VERIFIED`; insufficient evidence to decide applicability is `VERIFICATION_REQUIRED` + `NOT_VERIFIED`;
- existing `mcp_location` remains routing/location evidence, not execution-selection policy;
- existing `Project-Execution/tools.md` remains the execution policy owner;
- connected/recent tools do not become fallback entries automatically;
- Projects without an explicit fallback list remain `fallback_mode: NONE`;
- `fallback-log.md` is introduced only when ordered fallback is applicable; and
- persistent Root/Location Binding changes retain Preview/approval/revision/validation/promotion/history requirements.

The current ProjectFramework initialized Project remains pinned to Framework `1.15.0` until a separate governed `[Project Upgrade]` adopts the released `1.16.0` distribution. Developing the Framework distribution does not silently upgrade the local Project Source pin.

## 17. GREENFIELD Behavior

For a new Project created under the adopting release:

- Develop Workspace may be configured when implementation development is applicable;
- Develop Workspace may be Local or Remote Durable, but the active workspace for an affected scope must be unambiguous;
- later Local ↔ Remote Durable relocation follows the same Section 5.4 checkpoint/identity/promotion contract;
- Production Workspace is optional/applicability-driven. A Project that explicitly has no production/runtime target reports `NOT_APPLICABLE`; absence alone does not prove non-applicability;
- Primary MCP/tool policy is optional unless a durable execution profile is useful;
- no default broad fallback is invented;
- if a Project chooses ordered fallback, the list/order is explicit and `fallback-log.md` becomes applicable; and
- Production source mutation remains forbidden whenever a Production Workspace/target role is declared.

## 18. Authority Boundary

`[Project Path]` remains read/verify/routing presentation.

It does not grant:

```text
mutation authority
deployment authority
push/publication authority
Root/Binding mutation authority
secret access/disclosure authority
Decision/Requirement authority
runtime privilege
```

A correct Production target plus an ACTIVE MCP is still insufficient to deploy without applicable Goal/AUTH/ENV/Risk/tool/platform authority.

Auto fallback changes only which already-eligible declared execution tool carries an already-authorized action. It never expands the action's authority or scope.

Likewise, Develop Workspace relocation changes execution/edit routing only. The active Develop Workspace semantic owner remains `40 Technical Design`; if a relocation also changes persistent Local Workspace Binding, the existing Root/Binding approval and promotion flow remains independently mandatory.

## 19. No Runtime Router / Watcher

TASK-048 is a Framework governance/documentation feature.

It does not create:

- a background MCP watcher;
- a daemon/service that continuously polls MCPs;
- an automatic network router;
- a credential store;
- a runtime deployment engine;
- a validator/CLI/parser/interceptor;
- CI/CD or deployment automation; or
- an implicit fallback discovered from currently connected tools.

"Auto fallback" means the Agent follows the declared ordered policy at action time when Primary is unavailable, subject to health/target/authority checks and durable logging.

## 20. Affected Framework Surfaces

Expected implementation surfaces include, subject to implementation-plan confirmation:

- `Framework-Source/references/core-governance-rules.md`
- latest applicable Framework amendment/release guidance
- `Framework-Source/SKILL.md`
- `Framework-Source/templates/project-location-bootstrap.md`
- `Framework-Source/templates/project-execution/README.md`
- `Framework-Source/templates/project-execution/tools.md`
- new `Framework-Source/templates/project-execution/fallback-log.md`
- applicable `Framework-Source/templates/project-source-mockup/00-Project-Source-Framework.template.md`
- applicable `40 Technical Design` / `60 Deployment Plan` starter guidance
- `Framework-Source/tests/pressure-scenarios.md`
- root `README.md` and migration/release guidance as applicable
- `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Task/evidence/release surfaces required by normal Framework development lifecycle

Current Project Source must not be silently upgraded as part of Framework distribution implementation.

## 21. Versioning

Target:

```text
Framework 1.15.0 → 1.16.0
Schema 1.0.0 unchanged
release format 3 unchanged
```

Classification:

```text
BACKWARD_COMPATIBLE_REGISTERED_COMMAND_AND_EXECUTION_ROUTING_FEATURE
```

Rationale:

- `[Project Path]` strict interface gains materially new required dimensions/behavior;
- workspace-role, workspace-relocation, and MCP fallback/failback semantics are additive Framework interfaces;
- no semantic slot is added;
- no Project Stable-ID family is added;
- existing canonical homes are reused; and
- Brownfield adoption remains governed rather than automatic.

## 22. Verification Strategy

Implementation must follow TDD/progressive verification appropriate to Framework work.

Pressure scenarios must cover at minimum:

1. Develop and Production workspaces both configured and verified.
2. Develop workspace unresolved blocks edit/build.
3. Production target unresolved blocks deploy mutation.
4. Direct Production source edit is rejected.
5. Primary MCP ACTIVE uses Primary.
6. Primary unavailable + fallback NONE fails closed.
7. Ordered fallback selects only first eligible declared fallback.
8. Connected but undeclared MCP is rejected.
9. Fallback target identity mismatch makes fallback ineligible.
10. Auto fallback writes the required incident record before Material fallback mutation.
11. Fallback-log persistence failure blocks Material fallback mutation.
12. Primary recovery mid-action does not switch until checkpoint completion.
13. Checkpoint failback returns next action to Primary after re-verification.
14. Fallback MCP fails with unknown result; Agent verifies resulting state before retry.
15. Unprovable result fails closed.
16. Fallback-to-next-fallback transition respects declared order and logs transition.
17. Brownfield existing Workspace may become Develop only with evidence; Production is not inferred.
18. Brownfield connected/recent MCP does not become fallback automatically.
19. Project without ordered fallback need not materialize `fallback-log.md`.
20. `[Project Path]` required section order/fields are preserved under unavailable evidence.
21. `[Project Path]` remains read-only and grants no deployment/root/push authority.
22. Existing strict-command and response-close completeness gates remain intact.
23. Framework version becomes 1.16.0 while Schema remains 1.0.0.
24. No runtime router/watcher/credential store/CLI is introduced.
25. Local → Remote Durable relocation succeeds only after required source state is checkpointed, repository identity/source revision match, and target durability is verified.
26. Remote Durable → Local relocation applies the same checks and does not receive a weaker reverse path.
27. Git Remote URL/name alone is rejected as a Develop Workspace locator.
28. Remote relocation target with repository identity or source revision mismatch is not promoted.
29. Required implementation work that exists only as uncommitted state blocks relocation until preserved/reconciled.
30. Two unresolved active Develop Workspace candidates for the same scope block Material source mutation.
31. Persistent relocation that changes Project Location Binding requires the existing approval/revision/validation/promotion/history flow.
32. After promotion, `[Project Path]` resolves the new active workspace and source mutation/build/test routing no longer targets the demoted workspace for that scope.
33. Project Location Binding remains location/routing-only; `workspace_role`, `source_mutation`, and active Develop Workspace semantics are not moved into `FRAMEWORK-001`.
34. `40 Technical Design` is the canonical owner of active Develop Workspace role/type/location/durability semantics; `[Project Path]` fails closed on material contradiction with Local Workspace Binding or fresh repository evidence.
35. Explicit no-Production Project truth renders the complete Production Workspace section as `NOT_APPLICABLE` rather than `NOT_VERIFIED`.
36. Unknown Production applicability renders `Applicability: VERIFICATION_REQUIRED` + `Status: NOT_VERIFIED` and is not silently converted to `NOT_APPLICABLE`.

Use `TASK_LOCAL_FAST` / focused affected verification during implementation checkpoints, `CHECKPOINT_INTEGRITY` at logical checkpoints, and one final `RELEASE_FULL` on the final unchanged release candidate as applicable under the active Framework contract.

## 23. Acceptance Criteria

TASK-048 implementation is complete only when:

- `[Project Path]` has the approved strict eight-section order;
- Develop vs Production roles are explicit and verifiable;
- canonical ownership is preserved: `FRAMEWORK-001` owns repository/local binding, `40 Technical Design` owns Develop Workspace semantics, and `60 Deployment Plan` owns applicable deployment/runtime mapping;
- Project Location Binding does not acquire `workspace_role`, `source_mutation`, or active-workspace authority;
- Local ↔ Remote Durable Develop Workspace relocation is deterministic, preserves required source state, verifies repository/revision/durability, and promotes exactly one active Develop Workspace per affected scope;
- Production direct source mutation is forbidden;
- Production applicability is exact: explicit no-Production truth uses `NOT_APPLICABLE`, unresolved applicability uses `VERIFICATION_REQUIRED`, and absence is never silently interpreted as either;
- build source and run target are explicitly distinguishable;
- Primary MCP is exact and no implicit fallback exists;
- ordered auto-fallback uses only declared eligible entries;
- every Material fallback incident is durably recorded in `fallback-log.md` when fallback is applicable;
- unknown-result retry safety is explicit;
- `CHECKPOINT_FAILBACK` is implemented and verified;
- Brownfield/Greenfield rules prevent silent inference/adoption;
- authority separation remains intact;
- Framework 1.16.0 / Schema 1.0.0 release surfaces are aligned;
- applicable pressure/AFFECTED/final release verification passes; and
- publication remains separately governed from local implementation completion.

## 24. Spec Self-Review

Result: `PASS`.

- Placeholder scan: no unresolved `TBD`/`FIXME` implementation requirement; angle-bracket values are intentional configuration examples.
- Internal consistency: approved Architecture Option 1, canonical owner separation (`FRAMEWORK-001` binding vs `40` workspace semantics vs `60` deployment mapping), Auto Fallback, Production no-edit boundary, Local ↔ Remote Durable Develop Workspace relocation, append-only fallback log, Checkpoint Failback, strict command order, Brownfield behavior, and 1.16.0 classification are mutually aligned.
- Scope check: one architectural feature; no background router/watcher, deployment engine, validator/CLI, credential store, or Project Source auto-upgrade was introduced.
- Ambiguity check: execution policy, workspace relocation/promotion, local binding ownership, Develop Workspace semantic ownership, deployment ownership, authority separation, Production applicability, unknown-result handling, logging, and recovery conditions each have explicit canonical homes/behavior.
- Repository-path correction: README propagation points to root `README.md`; no nonexistent `Framework-Source/README` is required.
- Relocation review: Git Remote is explicitly not a workspace; Local ↔ Remote Durable relocation is symmetrical, fail-closed on source-state/identity/durability uncertainty, and retains existing Root/Binding approval when persistent binding changes.
- Location-vs-authority review: `project_location_binding.local_workspaces` remains location/routing-only and does not carry `workspace_role` or `source_mutation` semantics.
- Production applicability review: explicit non-applicability, unresolved applicability, and applicable-but-unverified targets have distinct strict representations; missing data alone never becomes `NOT_APPLICABLE`.

## 25. Implementation Gate

This written spec records the user-approved architecture, but implementation does not start until the user reviews this materialized spec and explicitly approves proceeding to implementation planning.

Next architectural workflow step after written-spec approval: invoke the implementation-planning workflow and create the detailed TASK-048 plan. No implementation mutation is authorized by this spec materialization alone.
