# TASK-039 `[Goal]` Persistent Continuous Goal Execution Command — Design

Date: `2026-08-29` (Asia/Bangkok)
Task: `TASK-039`
Design state: `USER_APPROVED_DESIGN / SPEC_APPROVED`
Approval basis: the user selected persistent Goal semantics and explicitly authorized continuous TASK-039 development without repeated approval prompts on `2026-08-29`. This approval covers design/spec/plan work for TASK-039 and the in-scope local development workflow defined below. It does not override higher-level system/tool/platform confirmation requirements or TASK-039's sequencing dependency on TASK-038 implementation.
Target release: Framework `1.8.0` / Schema `1.0.0` / release format `3`

## 1. Problem

ProjectFramework already provides `[Session Envelope]` to pre-approve bounded execution within a session/task, but long-running GPT-Web/Agent work still stops unnecessarily when the user has already authorized a broader outcome and expects the Agent to continue across chat boundaries.

The missing abstraction is not another task list or another authority family. It is a durable command contract that captures:

1. the outcome the user wants;
2. the evidence required to prove that outcome;
3. the exact execution authority the user grants in advance;
4. the operations explicitly excluded from that authority;
5. the continuation state needed for a new chat/Agent to resume without asking for the same approval again.

Framework `1.8.0` therefore introduces `[Goal]` as a persistent goal-execution command. `[Goal]` reduces redundant Framework-level approval prompts while preserving Root Governance, Authority, Risk, location, secret/disclosure, Git integration, verification, and higher-level platform/tool gates.

Core invariant:

```text
Goal authorization ≠ unlimited authorization
```

Operational invariant:

```text
Do not request Framework-level approval again solely for an action already covered by the active Goal authorization.
```

## 2. Chosen architecture: compose existing canonical objects

TASK-039 MUST NOT create a `GOAL-*` Stable-ID family. The command is an interaction layer over existing Project Source object homes:

```text
[Goal] command        = user-facing command/workflow
OUT-* in 91           = intended Goal outcome and success evidence
AUTH-* in 12          = persistent user-granted execution authority
ACT-* in 15           = executable work decomposition
ENV-* in 15           = session/task execution envelope derived from AUTH-*
09 Handoff            = cross-chat continuation pointers; authority_transfer: false
03 Current State      = active Goal summary / blocker / next action
13 Evidence           = material evidence supporting authorization and outcome claims
10 Change Log         = durable lifecycle history when material
```

This preserves existing canonical ownership:

```text
Outcome ≠ Action ≠ Authority ≠ Handoff
```

and keeps the existing distinction:

```text
ACT DONE ≠ OUT ACHIEVED
```

## 3. Registered command identity

Canonical command display form:

```text
[Goal]
```

Literal `[` and `]` are required. Registered-name matching inside brackets is case-insensitive, following existing Project command rules.

Supported user intents are natural-language variants of four operations:

```text
CREATE / SET      — establish a new persistent Goal
SHOW / STATUS     — show active Goal, authority boundary, progress, blockers, evidence
CHANGE            — explicitly revise Goal scope/success criteria/authorization
CANCEL / STOP     — revoke future execution under the Goal while preserving history
```

The Framework need not require literal subcommand keywords. The Agent resolves intent from the bracketed `[Goal]` invocation plus the user's text. Ambiguity that changes material scope or authority fails closed to clarification or a bounded no-mutation report.

Unbracketed use of the word "goal" is ordinary language and does not invoke the registered command automatically.

## 4. Persistent Goal representation

A new persistent Goal materializes or updates an `OUT-*` record in `91 Project Management Control`. Because `91` is conditional, `[Goal]` makes `91` applicable when no active `91` exists.

The Goal `OUT-*` record MUST resolve at least:

```text
Outcome Statement
Success Criteria / Success Measure
Evidence Required
Scope
Prohibited Zones
Owner
Status
Related AUTH-*
Related ACT-*
Related REQ-* / DEC-* / RISK-* / DEP-* / GATE-* when applicable
Created/Approved By
Created/Approved At
Last Evaluated
Terminal Evidence when achieved/cancelled/superseded
```

TASK-039 defines Goal-specific `OUT-*` statuses:

```text
ACTIVE
BLOCKED
ACHIEVED
CANCELLED
SUPERSEDED
```

Semantics:

- `ACTIVE` — outcome remains valid and at least one safe in-scope action can proceed or is ready to proceed.
- `BLOCKED` — outcome remains desired but no safe next action can currently progress because a global blocker applies. This is non-terminal and may return to `ACTIVE` after fresh verification.
- `ACHIEVED` — all explicit success criteria have sufficient evidence. Task completion alone is insufficient.
- `CANCELLED` — user withdrew the Goal; future Goal-authorized execution stops immediately.
- `SUPERSEDED` — a later explicitly approved Goal replaces this outcome rather than silently modifying it in place.

A Goal is persistent across chat/session boundaries until it reaches `ACHIEVED | CANCELLED | SUPERSEDED`.

## 5. Persistent authorization representation

A Goal's durable execution authority materializes as an `AUTH-*` record in `12 Authorization Registry` rather than being inferred from Handoff, chat memory, task status, or the existence of the `OUT-*` record.

The Goal-related `AUTH-*` MUST identify:

```text
Grantor
Grantee / eligible Agent role or execution actor scope
Related OUT-*
Allowed Actions
Scope / Paths / Surfaces
Explicitly Included Shared/External Effects
Forbidden Actions / Effects
Risk Ceiling
Start
Expiry / Termination
Revocation Trigger
Status
Evidence / user-approval reference
```

The Goal's terminal state MUST terminate or supersede its dependent authorization. An Agent MUST NOT continue using Goal authority after the related Goal is `ACHIEVED`, `CANCELLED`, or `SUPERSEDED` unless another independent valid `AUTH-*` covers the action.

The persistent authorization survives a chat change because it is Project Source truth, not because authority transfers through Handoff. `09` only points to the active `AUTH-*`; it continues to carry `authority_transfer: false`.

## 6. Default local-development authorization

When the user creates a persistent `[Goal]` without narrowing the execution boundary, the Goal MUST by default pre-authorize the normal local development workflow needed to pursue the stated outcome within the governed Project target. The user may explicitly narrow this default grant when creating or changing the Goal:

```text
read / inspect / research local Project sources
architecture/design work
implementation planning
create/edit/move non-destructive in-scope Project files
tests / lint / typecheck / build / validation
debugging and corrective edits
local Git add/commit
Logical Checkpoints
Project Source continuation/evidence updates required by the work
```

This local-development grant is bounded by the Goal scope, existing REQ/DEC/Root Governance, applicable risk ceiling, current bindings, Canonical Integration Target/Base Freshness, Canonical Implementation Source, and tool/platform policy.

The Agent MUST NOT stop merely to request user approval for an operation that is clearly within this active authorization. It SHOULD continue to the next safe in-scope action, persisting Logical Checkpoints as required.

## 7. Push and publication boundary

`push` / remote publication is NOT included in a Goal by default.

It becomes pre-authorized only when the user's Goal explicitly includes publish/push semantics and the intended governed target is sufficiently identified or can be resolved uniquely from active Project governance. Examples:

```text
[Goal] finish Framework 1.8.0
→ local commits allowed; push remains outside Goal authority

[Goal] finish Framework 1.8.0 and publish it to origin/main
→ push may be covered after verification/integration gates pass
```

Before an authorized push, the Agent MUST fresh-resolve repository identity, binding compatibility, current branch/worktree, Canonical Integration Target/Base Freshness, remote target, verification/evidence validity, and working-tree state.

The Goal's push authority becomes unusable for the affected operation when:

- the resolved repository/remote target materially differs from the approved target;
- binding is `VERIFICATION_REQUIRED` or materially contradictory;
- integration/base evidence is stale or conflicts;
- publication would include unrelated/unapproved work;
- another required higher-level tool/platform confirmation remains mandatory.

`commit ≠ push` remains binding.

## 8. Destructive-action boundary

Destructive actions are NOT included by default, regardless of the Goal's local-development or push authority.

A destructive action may be pre-authorized only when the Goal explicitly identifies both:

```text
operation
+ target
```

Example:

```text
Delete branch task-x after merge and verification succeeds.
```

Such authorization is exact-scope only. It MUST NOT be generalized to deleting other branches, files, environments, data, tags, histories, resources, or state.

The Agent still performs normal preflight/result verification and obeys mandatory tool/platform confirmations that cannot be waived by ProjectFramework.

## 9. Root Governance and Project Location Binding boundary

Root Governance / Project Location Binding mutation is NOT included by default.

It may be pre-authorized only when the Goal explicitly identifies the intended governance/location change and target, for example a named repository migration or named Project Source binding change.

Even when pre-authorized, the existing governed lifecycle remains mandatory:

```text
fresh current root
→ bounded proposed revision
→ validate
→ promote
→ supersede/archive prior revision
→ sync Index/Manifest/Change Log
→ verify resulting binding/state
```

A broad Goal such as "finish Framework 1.8.0" MUST NOT be interpreted as permission to change repository binding, Local Workspace Binding, File Storage Binding, Project identity, Root Governance invariants, or schema authority.

## 10. Secrets and external disclosure boundary

A Goal may authorize use of governed `SECRET-*` references for otherwise-authorized work, but TASK-039 never permits actual secret values to be persisted in Project Source, Evidence, Handoff, Goal records, plans, logs, or exports.

Secret access/use remains subject to the applicable secret provider/tool boundary. A Goal does not convert a secret reference into disclosure permission.

External AI/provider disclosure remains governed by TASK-026 External AI Context & Disclosure Governance once implemented, or by explicit current authorization before that contract exists. `[Goal]` does not create blanket outbound-context authority.

Unknown or mixed-sensitivity disclosure requirements fail closed for the affected outbound action while independent safe local work may continue.

## 11. Goal execution decomposition

The Agent decomposes the persistent `OUT-*` into one or more `ACT-*` records as needed. `ACT-*` retains its existing lifecycle:

```text
TODO | IN_PROGRESS | DONE | BLOCKED | CANCELLED
```

Each Material Git-backed action still requires its own completion evidence/commit semantics. Completing all known `ACT-*` does not automatically mark the Goal `ACHIEVED`; the Agent must evaluate the Goal's success criteria separately.

The Agent may create or refresh `ENV-*` session/task envelopes from the parent Goal `AUTH-*` without obtaining new user approval when:

- the `AUTH-*` is current and valid;
- the generated Envelope is equal to or narrower than the parent authorization;
- expiry is bounded to the current session/task/time window;
- prohibited zones remain preserved;
- no tool/platform confirmation requirement is being represented as waived.

`ENV-*` never expands the parent `AUTH-*`.

## 12. Cross-chat resume algorithm

When a new chat/Agent resumes a Project with a persistent Goal:

```text
PROJECT-BOOTSTRAP.md
→ validate 00 / FRAMEWORK-001
→ read 01
→ read 03
→ read 09 when continuation applies
→ resolve active Goal OUT-* in 91
→ resolve related AUTH-* in 12
→ resolve active/pending ACT-* and ENV-* in 15
→ fresh-check volatile prerequisites and bindings
→ continue the exact safe next action without asking for already-covered approval
```

Resume MUST NOT rely on old chat text as authority. If `09` points to stale/missing objects, canonical registries win and the stale Handoff is repaired through normal continuation governance.

The receiving Agent MUST verify that the Goal is still `ACTIVE | BLOCKED`, the authorization is still valid, and no user revocation/supersession or material conflicting truth has appeared.

## 13. Partial blocker behavior

TASK-039 distinguishes action-local blockers from Goal-global blockers.

If one requested operation is unauthorized or blocked but independent in-scope work can safely proceed, the Agent MUST:

1. block only the affected operation;
2. record/surface the blocker when material;
3. continue other safe Goal work without requesting broad re-approval.

The whole Goal moves to `BLOCKED` only when no safe in-scope next action can progress or when a global prerequisite/authority/evidence conflict prevents meaningful continuation.

Examples of global blockers include unresolved Project identity/binding for all affected work, required success criteria becoming impossible without material requirement change, active authority revocation, or a conflict that changes the Goal's accepted semantics.

## 14. Requirement/decision change boundary

A Goal authorizes execution toward an approved outcome; it does not authorize the Agent to rewrite the meaning of that outcome or silently alter Project requirements/decisions to make completion easier.

If achievement would require a material change to `REQ-*`, `DEC-*`, accepted Risk, architecture contract, or another governed truth outside the Goal's explicit authorization, the Agent MUST stop the affected path and route the change through its existing governance/authority process.

If another safe path can still achieve the same Goal without changing governed intent, work may continue on that path.

## 15. Multiple Goals and conflict handling

Multiple persistent Goals MAY coexist only when their scopes and authorizations are compatible.

A later `[Goal]` invocation MUST NOT silently override an active Goal or its authorization. The Agent must determine whether the new request is:

```text
independent compatible Goal
explicit change to existing Goal
explicit supersession
material conflict
```

Material conflicts use existing `CONFLICT-*` semantics in `08` when applicable and fail closed for the conflicting scope. Recency alone never decides which Goal wins.

No Goal may override active `REQ-*`, `DEC-*`, Root Governance, Project Location Binding, or another valid `AUTH-*` without the explicit governed change/authority required for that object.

## 16. Cancellation, revocation, and supersession

User cancellation has immediate prospective effect:

```text
Goal OUT-* → CANCELLED
related Goal AUTH-* → revoked/terminated
future Goal-authorized execution → prohibited
completed commits/evidence/history → preserved
```

Supersession preserves the old Goal and authority history and creates/updates the replacement records explicitly. It is never implemented as silent in-place rewriting that makes prior authorization irreconstructable.

If cancellation arrives while an external/tool operation is already executing, ProjectFramework cannot guarantee runtime interruption; after control returns, the Agent MUST fresh-check resulting state, persist evidence, and perform no further Goal-authorized action.

## 17. Goal achievement and evidence

A Goal may transition to `ACHIEVED` only when every declared success criterion has sufficient evidence or an explicitly approved criterion revision.

Minimum final evaluation:

```text
Success criterion
Observed/resulting state
Evidence pointer
Pass / fail / unknown
Residual blocker/risk if any
```

For Git-backed development Goals, relevant evidence may include completion commits, working-tree state, affected verification, `RELEASE_FULL` when required, integration/base freshness, and remote publication evidence when publication is part of the Goal.

The Framework must prevent the shortcut:

```text
all ACT-* DONE → automatically OUT-* ACHIEVED
```

## 18. `[Project Status]` and command discovery integration

Framework command help/discovery adds:

```text
[Goal] : create/show/change/cancel a persistent outcome and its bounded continuous-execution authorization
```

`[Project Status]` gains a bounded Goal view when a persistent Goal is active or blocked:

```text
Active Goal OUT-*
Goal Status
Success Criteria Progress
Authorization AUTH-* validity
Current/next ACT-*
Push/destructive/root/disclosure inclusion flags
Current blocker
Continuation freshness
```

Status remains read-only and must not activate, extend, cancel, or reinterpret Goal authority.

## 19. Handoff integration

When a persistent Goal exists, `09 Handoff` SHOULD include compact references, not duplicate canonical payload:

```text
Active Goal: OUT-*
Goal Status
Authorization: AUTH-*
Current Action: ACT-*
Envelope: ENV-* or none
Last Verified Authorization At
Next Safe Action
Goal Blocker when applicable
authority_transfer: false
```

The Handoff does not copy the full Goal statement/authorization and does not grant authority to the next Agent. The new Agent resolves the referenced canonical objects.

## 20. GREENFIELD and Brownfield behavior

Framework `1.8.0` GREENFIELD starter surfaces include `[Goal]` command semantics, relevant `91/12/15/09/03` starter guidance, and command discovery. They do NOT create an active Goal automatically.

Brownfield upgrade to the release containing TASK-039 MUST NOT synthesize a Goal from free-text backlog, an old Handoff, an existing `OUT-*`, or prior "continue" messages. Existing `OUT-*`, `AUTH-*`, `ACT-*`, and `ENV-*` records are preserved. A persistent Goal exists only when the user invokes/explicitly adopts `[Goal]` under the new contract.

Direct-to-Latest migration assesses current custom `91/12/15` content and slot collision rules normally. No new semantic slot or Stable-ID family is introduced.

## 21. TASK-038 sequencing and distribution path

TASK-039 design/spec/plan may be completed before TASK-038 implementation because it does not require current distribution-path mutation.

TASK-039 implementation MUST occur after TASK-038 migrates the current Framework distribution root from:

```text
managing-project-source/
```

to:

```text
Framework-Source/
```

This prevents Framework `1.8.0` `[Goal]` implementation from adding new current references to the old distribution root. Historical TASK-039 design/plan text may mention the pre-migration path when describing the dependency, but implementation surfaces use canonical `Framework-Source/` after TASK-038.

## 22. Higher-level platform/tool boundary

ProjectFramework governs Project-level behavior only. `[Goal]` cannot waive or override:

```text
system instructions
developer instructions
product safety policy
MCP/tool confirmation requirements
authentication/authorization enforced by external systems
platform rate/capability limits
mandatory user-interaction controls imposed above ProjectFramework
```

If GPT-Web, an MCP tool, or another platform requires a confirmation that ProjectFramework would otherwise consider pre-authorized, the Agent must comply with the higher-level requirement. The Framework should report this as a platform/tool gate rather than incorrectly claiming the Goal authorization failed.

## 23. Framework surfaces affected

After TASK-038, TASK-039 implementation affects at least:

- `Framework-Source/FRAMEWORK-RELEASE.yaml`
- new Framework `1.8.0` amendment or the release amendment selected by the implementation sequence
- `Framework-Source/references/core-governance-rules.md`
- `Framework-Source/SKILL.md`
- root `README.md`
- `Framework-Source/MIGRATION-NOTES.md`
- `Framework-Source/templates/00-project-source-framework.md`
- `Framework-Source/templates/core-document-skeletons.md`
- mockup starters for `03`, `09`, `12`, `15`, `91` and mockup README
- maintained starter release stamps as required
- ChatGPT/Claude launchers with shared marker-body parity and size ceiling preserved
- `Framework-Source/tests/pressure-scenarios.md`
- Task registry, design/plan/evidence records

Conditional `91` remains conditional except when an active persistent Goal materializes an `OUT-*`.

## 24. Release classification

TASK-039 is designed as a backward-compatible Framework minor semantic expansion:

```text
Framework 1.8.0
Schema 1.0.0
release format 3
```

Rationale: it registers a new command and specializes existing `OUT-* / AUTH-* / ACT-* / ENV-* / Handoff` semantics without adding a semantic slot, metadata-schema field requirement, or Stable-ID family.

If implementation reveals that current object schemas cannot represent the required authorization or Goal lifecycle without an incompatible change, stop and reclassify rather than silently forcing Schema `1.0.0`.

## 25. Verification strategy

Affected verification must prove at minimum:

1. `[Goal]` is registered consistently across Core Governance, SKILL, starters, README, launchers, and command-help tests.
2. Literal brackets and case-insensitive registered-name matching are preserved.
3. No `GOAL-*` Stable-ID family is created.
4. Goal representation uses `OUT-*`; authorization uses `AUTH-*`; execution uses `ACT-* / ENV-*`; continuation uses `09` references only.
5. Persistent new-chat resume resolves canonical objects and does not rely on chat history.
6. Already-covered local development operations do not trigger redundant Framework-level approval prompts.
7. Push is blocked by default and allowed only when explicitly included with a valid governed target and fresh integration evidence.
8. Destructive actions are blocked by default and allowed only for explicitly named operation+target.
9. Root/binding changes are blocked by default and allowed only for explicitly named mutation+target with normal root revision lifecycle.
10. Secret values remain prohibited; external disclosure is not implicitly authorized.
11. `ENV-*` derived from Goal authority cannot exceed parent `AUTH-*`.
12. `authority_transfer: false` remains true in Handoff; a new Agent fresh-resolves authority.
13. Partial blockers do not unnecessarily stop independent safe Goal work; global blockers move Goal to `BLOCKED`.
14. Goal cancellation/revocation stops future Goal-authorized execution while preserving history.
15. Goal conflict does not resolve by recency/last-write-wins.
16. `ACT DONE ≠ OUT ACHIEVED`; evidence is required for all success criteria.
17. Brownfield upgrade never synthesizes a persistent Goal from existing prose or records.
18. Higher-level system/tool/platform confirmation requirements remain binding.
19. Launchers preserve byte-identical shared marker bodies and the current character ceiling.
20. Historical Framework amendments/evidence outside the selected current implementation surfaces remain unchanged.
21. `git diff --check` passes and one final `RELEASE_FULL` runs on the unchanged Framework `1.8.0` candidate according to current release rules.

Pressure scenarios MUST include at least: unbracketed invocation, case-insensitive invocation, new-chat resume, stale/revoked AUTH, local edit/commit without re-approval, default push denial, explicit push authorization, changed remote target, destructive overreach, exact destructive authorization, Root/Binding overreach, explicit Root/Binding authorization, secret-value request, external disclosure request, narrower ENV derivation, ENV attempted expansion, partial blocker continuation, global blocker, Goal cancellation, conflicting active Goals, silent requirement rewrite attempt, all-actions-done-but-outcome-not-proven, and higher-level tool confirmation still required.

## 26. Non-goals

TASK-039 does not create autonomous background agents, schedulers, watchers, daemons, silent execution after the user is offline, model/tool routing, new secret storage, an external authorization service, CI/CD automation, deployment automation, a new `GOAL-*` registry, or authority to bypass product/tool safety controls.

It also does not implement TASK-026 disclosure runtime, TASK-027 MCP/tool profile, TASK-034 model capability routing, or TASK-035 release automation.

## 27. Acceptance criteria

TASK-039 is acceptable when a user can invoke one persistent `[Goal]`, explicitly or by default authorize the bounded local development workflow, close or open specific push/destructive/root/disclosure boundaries, leave the chat, return through a fresh Agent, and have that Agent resume from Project Source without requesting the same Framework-level approval again; while Project truth/authority remain reconstructable, Goal authority terminates correctly, actions remain separate from outcomes, material conflicts fail closed, and higher-level platform/tool rules remain enforceable.
