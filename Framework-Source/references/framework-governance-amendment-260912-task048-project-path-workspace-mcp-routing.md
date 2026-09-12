# Framework Governance Amendment — TASK-048 Project Path Workspace & MCP Routing

Status: `APPROVED_BY_USER / CURRENT_AMENDMENT`
Framework target: `1.16.0`
Schema: `1.0.0`
Release format: `3`
Task: `TASK-048`

## Purpose

Framework 1.16.0 extends the registered `[Project Path]` Strict Governed Interface so an Agent can read and verify the active development workspace, Production applicability, exact MCP execution route, fallback recovery state, and build/deployment mapping without inferring authority or introducing a runtime router.

This amendment composes existing canonical owners. It does not create a new semantic slot, Stable-ID family, lifecycle state, authority family, credential store, parser, CLI, watcher, daemon, deployment engine, or runtime subsystem.

## Release identity and compatibility

```text
Framework 1.16.0 / Schema 1.0.0 / release format 3
Classification: BACKWARD_COMPATIBLE_REGISTERED_COMMAND_AND_EXECUTION_ROUTING_FEATURE
```

Initialized Projects remain pinned to their local Framework release. Brownfield Projects do not silently adopt this amendment merely because the distribution is updated; adoption uses the governed `[Project Upgrade]` path and preserves Project-specific history and rules.

The registered command set remains exactly seven:

```text
[Project Status]
[Project Path]
[Project Upgrade]
[Session]
[Goal]
[Meeting]
[Project Audit]
```

TASK-043 remains in force: a recognized Registered Command is a Strict Governed Interface and must pass the Command Contract Completeness Gate before the response-close gate. TASK-045 remains in force: the visible response close has exactly the two required headings and the ordered `[Next Action]`, `[Next Goal]`, `[Reason]` fields, with nothing after `[Reason]`. This amendment does not add a command or alter either gate.

## Canonical owners

The command composes fresh observations from these owners:

```text
FRAMEWORK-001 / Project Location Binding
  repository and environment-scoped Local Workspace binding/routing only

40 Technical Design / Development Workspace Contract
  Develop Workspace role, type, locator, durability, active-workspace semantics,
  Canonical Implementation Source relationship, and source-mutation boundary

60 Deployment Plan
  applicable deployment/runtime target and build/deployment mapping

Project-Execution/tools.md
  exact MCP execution-selection policy

Project-Execution/fallback-log.md
  append-only actual fallback/recovery incident history when applicable
```

`FRAMEWORK-001` does not own `workspace_role`, `source_mutation`, active Develop Workspace ownership, Canonical Implementation Source, or Production runtime authority. A material contradiction among the owners or fresh evidence is `MISMATCH`/`NOT_VERIFIED` for the affected dimension and fails closed only for Material actions that require that dimension. The command never chooses an owner by recency.

Git Remote/repository publication is a synchronization or publication target, not a Develop Workspace. A Remote Durable Develop Workspace is an actual declared durable workspace that can prove repository/source identity and execute the declared development workflow.

## Strict `[Project Path]` interface

`[Project Path]` remains literal-bracket, case-insensitive, read/verify-only presentation. It does not grant mutation, deployment, push/publication, Root/Binding, secret, disclosure, Decision/Requirement, runtime, or other authority. Persistent path or binding changes route through their existing governed approval and revision flow; the command itself does not perform them.

The exact eight top-level sections and order are:

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

The strict structure is:

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

Required fields remain present when evidence is unavailable. Use explicit `NOT_VERIFIED`, `VERIFICATION_REQUIRED`, or another value allowed by the strict field. Do not substitute a missing field with inference.

## Develop Workspace and relocation

`40 Technical Design` is the semantic owner of the Develop Workspace. A valid Develop Workspace has a declared type, locator, durability/recovery assumption, repository/source identity, Canonical Implementation Source relationship, source revision, and Human/Agent edit location. Its role is `EDIT`, `BUILD`, `TEST`, and `PACKAGE`; `Source Mutation: ALLOWED` describes workspace compatibility only and never grants an `AUTH-*` permission.

For one affected implementation scope exactly one Develop Workspace is active at a time. Ambiguous concurrent active ownership fails closed for Material source mutation/build/test routing.

The supported relocation contract is symmetric:

```text
LOCAL_WORKSPACE ↔ REMOTE_DURABLE_WORKSPACE
```

Both Local-to-Remote Durable and Remote Durable-to-Local relocation require the same checks:

```text
resolve current active Develop Workspace
→ verify repository/source identity
→ checkpoint/commit required implementation state
→ prove no required completed work remains only as uncommitted state
→ freshly observe Git Remote/source synchronization when Git-backed
→ verify target durability and recovery assumptions
→ verify target repository/source identity, intended revision, and working-tree state
→ synchronize target to the intended revision
→ promote the target as the one active Develop Workspace in 40
→ demote the prior workspace
→ verify edit/build/test routing resolves only to the promoted workspace
```

Do not infer a target from recency, active editor state, MCP workspace lists, mounts, search ranking, or a similarly named directory. A repository URL or Git Remote name is not a workspace locator. If persistent `FRAMEWORK-001` Local Workspace Binding changes, its existing User Explicit Approval plus revision, validation, promotion, and history rules remain mandatory. Relocation does not transfer Git integration, push/publication, deployment, MCP/tool, or other authority.

## Production applicability and mapping

`60 Deployment Plan` owns the concrete deployment/runtime mapping when deployment is applicable. Production has the role `DEPLOY`, `RUN`, `HEALTH_CHECK`, and `OBSERVE_RUNTIME`. Direct Production source mutation is always `FORBIDDEN`; a correction follows canonical source change in Develop, test/build/package, verified artifact deployment, and runtime verification.

Production applicability is exact:

```text
APPLICABLE
  Project truth declares a Production/runtime target. Unresolved target details
  remain NOT_VERIFIED and deploy/run mutation fails closed.

NOT_APPLICABLE
  authoritative Project truth explicitly establishes that no Production/runtime
  target applies. Do not invent a target.

VERIFICATION_REQUIRED
  available truth cannot establish applicability. Absence never implies
  NOT_APPLICABLE; use Status: NOT_VERIFIED and block actions needing the
  unresolved Production/runtime dimension.
```

`Build Source: DEVELOPMENT` and `Run Target: PRODUCTION | NOT_APPLICABLE` remain distinct. No Production filesystem path is fabricated for a non-filesystem target.

## MCP execution, fallback, and recovery

`Project-Execution/tools.md` is the exact execution-selection owner. An MCP is `ACTIVE` and eligible only when all applicable checks succeed:

```text
endpoint/capability reachable
+ authentication/session usable when applicable
+ required capability/tool available
+ allowed by active Project-Execution policy
+ bound Project/workspace/repository target identity verified
= ACTIVE / ELIGIBLE
```

`primary_tool` is the default execution MCP. `disallowed_tools` wins. `fallback_mode: NONE` permits no substitute. `fallback_mode: ORDERED_ALLOW_LIST` permits only the declared `fallback_order`, in order; the first ACTIVE and eligible entry wins. A connected, recent, similar, ranked, or otherwise available undeclared MCP is never eligible.

Before a Material action, fresh-check Primary policy, availability, capability, and target identity. If Primary is unavailable, evaluate only the declared fallback order. Before a Material mutation through fallback, append the required fallback event to `Project-Execution/fallback-log.md`; inability to persist that event is `FAIL_CLOSED`. The log is append-only operational history, not authority, credentials, or a Stable-ID registry.

If an action may have been submitted but its result is unknown, the Agent must enter:

```text
RESULT_VERIFICATION_REQUIRED
→ inspect resulting state through an eligible declared MCP/tool
→ if applied, checkpoint and do not repeat
→ if not applied, retry only under valid authority
→ if unprovable, FAIL_CLOSED
```

When Primary recovers during fallback, `CHECKPOINT_FAILBACK` prevents a mid-action switch. Complete and verify the bounded action/checkpoint through fallback, persist the result, reverify Primary capability and target identity, append recovery/failback history, then use Primary for the next action. If the fallback fails before the checkpoint completes, establish resulting-state safety before evaluating the next declared fallback.

Command-facing execution values remain exactly `ACTIVE | UNAVAILABLE | VERIFICATION_REQUIRED` for MCP status and `PRIMARY | FALLBACK_ACTIVE | FAIL_CLOSED` for continuity. They are not lifecycle or Stable-ID families.

## Brownfield, authority, and implementation boundary

Brownfield Projects do not silently infer a Develop Workspace, Production target, MCP fallback, source identity, or relocation target. An existing verified implementation workspace may be Previewed as Develop only when evidence supports the classification. Production is never inferred from an existing path. Existing Projects without an explicit fallback list remain `NONE`; `fallback-log.md` is applicable only when ordered fallback is declared.

`[Project Path]` is a fresh read/verification view. Correct location, an eligible MCP, or a valid workspace role never grants mutation, deploy/run, Root/Binding, push/publication, secret, disclosure, or runtime authority. No background MCP watcher, automatic router, credential store, validator/CLI, deployment automation, or runtime subsystem is introduced.

`commit` is distinct from `push`; this amendment grants no publication authority.
