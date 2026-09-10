# ProjectFramework 2.0 + AI-ControlTower — Architecture Design

Date: `2026-09-04` (Asia/Bangkok)
Major target: `ProjectFramework 2.0.0`
Design class: `ARCHITECTURAL / MAJOR_VERSION`
Design state: `WRITTEN_SPEC_APPROVED_BY_GOAL / FORWARD_PORTED_TO_CANONICAL_V1_BASELINE / PREMERGE_PLANNING_ACTIVE`
Goal basis: user explicitly approved the architecture choices throughout the design dialogue and then invoked `[Goal] ยืนยัน จบจบ Design` to complete the consolidated written design without further section-by-section questions.
Original design branch: `design/projectframework-2-controltower` / design commit `6c9fd543c34e939db914c80e4c3354b3b36a0906`
Current forward-port branch: `v2-premerge-readiness`
Original STACKED_WORK design base: `9f5a6fb1f8d26b80049a4a9521e50c38a99126be` (V1.14 TASK-031 completion checkpoint).
Forward-port baseline: canonical Last Stable 1.x `origin/main@aae65796a8d4ad5f23323889b65b060bd36302c1`; Framework-Source tree `d5d04e4563157246872b1e02c791b94a6c564d95`.
Written-spec approval: user `[Goal]` on `2026-09-05` explicitly authorized continuous execution through the V2 Pre-Merge Readiness Gate; this satisfies the written-spec review gate for planning without authorizing the actual AI-ControlTower merge/cutover or V2 runtime implementation.

## 1. Purpose and problem statement

ProjectFramework 1.x is documentation-first governance. Its strength is portability and human/agent readability, but a material amount of execution correctness still depends on an AI reading Markdown, resolving current truth, remembering workflow state, interpreting authority boundaries, and deciding which lifecycle transition should happen next.

ProjectFramework 2.0 is a deliberate major change intended to reduce that interpretation variance. The design moves deterministic concerns out of AI memory/prose interpretation and into explicit protocol concepts:

```text
State
Workflow
Typed Transitions
Mandatory Guards
Concurrency
Leases
Evidence
Recovery
Checkpoint persistence
API contracts
```

The central operating principle is:

```text
AI = workflow participant
AI ≠ workflow/state controller
```

The AI remains responsible for reasoning, analysis, writing, investigation, implementation work, and other capability-appropriate tasks. It does not directly set canonical workflow state, invent transition legality, bypass authority, or declare persistence complete.

## 2. Final architecture decision summary

The approved design choices are:

| Area | Selected design |
|---|---|
| Project/runtime relationship | AI-ControlTower is the main Project/platform; `ProjectFramework 2.0` remains a named Protocol/Core module inside it |
| Logical separation | ProjectFramework Protocol is distinct from Control Plane Runtime even when stored in one repository |
| Authority | Split Authority / Hybrid State |
| Runtime persistence | Immutable Event Log + Materialized Current State |
| Workflow | Typed State Machine + Declarative Workflow |
| Authentication | Client Identity + Scoped Short-Lived Session Token |
| Multi-agent coordination | Scoped Lease + Versioned Transition + Fencing Token |
| Agent execution | Session Envelope + Immutable Execution Runs |
| Failure/recovery | Recovery State Machine + Reconciliation |
| Governance persistence bridge | Material Checkpoint Protocol + Durable Outbox |
| Public API | CQRS-style Query API + Transition Command API + read-only Event Stream |
| Project Source 2.0 | Typed Governance Resources + Human Views |
| Governance revisions | Immutable Resource Revisions + Active Resource Registry |
| Governance state | Common Resource Envelope + Typed Domain State |
| Resource taxonomy | Tiered Resource Model |
| Transition policy | Mandatory Framework Guards + Declarative Project Policies |
| Tool integration | Typed Capability Contract + Pluggable Adapters |
| 1.x migration | Side-by-Side Migration Workspace + Verified Promotion |
| Distribution | ProjectFramework protocol is public-domain-intent; runtime/adapters use separate component-scoped software licensing |
| Versioning | AI-ControlTower, ProjectFramework, Project Source Schema, API Protocol, and Workflow Schema version independently |
| Repository layout | `projectframework/`, `control-plane/`, `adapters/`, and `apps/` are separate top-level boundaries |
| Future canonical source | after governed 2.0 cutover, `AI-ControlTower/projectframework/` becomes canonical development source |
| Public ProjectFramework repository | one-way verified release distribution mirror, never reverse-sync/development authority |
| Publication | Verified Release Projection bound to exact canonical candidate identity/digest |

## 3. System architecture and repository boundary

The target post-cutover repository shape is:

```text
AI-ControlTower/
│
├─ projectframework/
│  ├─ protocol/
│  ├─ schemas/
│  ├─ workflows/
│  ├─ transitions/
│  ├─ capabilities/
│  ├─ migration/
│  └─ conformance/
│
├─ control-plane/
│  ├─ api/
│  ├─ auth/
│  ├─ state-engine/
│  ├─ workflow-engine/
│  ├─ multica/
│  ├─ execution/
│  ├─ recovery/
│  └─ checkpoint/
│
├─ adapters/
│  ├─ openviking/
│  ├─ graphify/
│  ├─ nexusrag/
│  ├─ gitnexus/
│  ├─ serena/
│  ├─ emif/
│  └─ provider-specific-or-future-adapters/
│
└─ apps/
```

Dependency direction is one-way:

```text
control-plane/ ───────► projectframework/
adapters/ ────────────► projectframework/ capability contracts
apps/ ────────────────► control-plane/ and/or public API

projectframework/ ─X─► control-plane/
projectframework/ ─X─► product-specific adapters
```

`projectframework/` is Protocol/Core authority. It may contain documentation, declarative schemas, protocol definitions, workflow/transition schemas, capability contracts, migration rules, conformance scenarios/test vectors, and other non-runtime protocol assets. Runtime services and executable enforcement belong outside the Protocol/Core boundary.

## 4. Authority model

Authority is deliberately split by truth domain:

```text
Project Source 2.0
= Governance Authority

AI-ControlTower Control Plane
= Workflow / Execution State Authority

Source-native external systems
= authority for factual state they own

Derived/context systems
= advisory/discovery/evidence assistance only
```

Examples of Project Source governance truth include Project identity, Requirements, Decisions, Risk, Authority, Outcomes, governed Relations, material Tasks/Goals, and durable evidence references.

Examples of Control Plane truth include workflow instance state, state version, session state, execution state, lease/fencing state, retry/recovery state, event cursor, transition result, and checkpoint delivery state.

The following remain distinct:

```text
Authentication ≠ Authority
Authority ≠ Transition eligibility
Transition eligibility ≠ Execution success
Execution success ≠ Verified outcome
Verified outcome ≠ Task DONE
Task DONE ≠ OUT achieved
PUSHED ≠ MERGED ≠ RELEASED ≠ DEPLOYED
Responsibility ≠ Authority
Capability availability ≠ capability eligibility ≠ authority
Derived result ≠ Governance truth
```

## 5. Runtime state and persistence

The Control Plane uses two complementary representations:

```text
Immutable Transition/Event Log
            │
            ├──► Materialized Current State
            ├──► Audit
            ├──► Replay
            └──► Recovery/Reconciliation
```

The Event Log records committed runtime/protocol events. Committed events are append-only and are never silently rewritten to make history look cleaner.

Materialized Current State is optimized for fast API reads and deterministic workflow decisions. It may be rebuilt/reconciled from the Event Log plus authoritative external facts when required.

Every mutable workflow aggregate carries a monotonic `state_version`. Mutation commands supply `expected_state_version`. A stale request fails closed instead of overwriting a newer state.

Example:

```text
Agent A reads version 18
Agent B reads version 18
Agent A commits → version 19
Agent B submits against version 18 → STATE_VERSION_CONFLICT
```

Every mutation request also carries an idempotency key. Repeating the same intent with the same key returns/reconciles the prior result rather than duplicating a material side effect.

## 6. State-domain separation

ProjectFramework 2.0 forbids one overloaded generic state field from representing unrelated lifecycle dimensions.

The architecture keeps at least these concepts distinct:

```text
Governance Revision State
Governance Typed Domain State
Epistemic Status
Workflow State
Execution State
Coordination State
Checkpoint State
```

Example:

```yaml
resource_id: TASK-031
revision_state: ACTIVE
domain_state: IN_PROGRESS
epistemic_status: VERIFIED
```

with Control Plane state such as:

```text
workflow_state: VERIFYING
execution_state: RUNNING
coordination_state: LEASED
checkpoint_state: CHECKPOINTED
state_version: 241
```

A transition names the state domain it changes. Generic `SET STATE = DONE` behavior is non-conformant.

## 7. Typed State Machine and declarative workflows

ProjectFramework defines canonical state/transition protocol rules. A Project declares its applicable workflow within that protocol.

Example Task flow:

```text
TODO → READY → IN_PROGRESS → VERIFYING → DONE
```

Transitions are named operations such as:

```text
START_TASK
SUBMIT_VERIFICATION
RETURN_TO_IMPLEMENTATION
COMPLETE_TASK
CANCEL_TASK
```

AI clients request transitions. They do not write canonical state directly.

A Query response SHOULD expose the current state plus currently allowed transitions so an agent does not need to infer the next legal step from prose.

Workflow definition versions are independent from runtime state versions. A material workflow-definition change affecting an active execution requires explicit re-evaluation/migration; active work never silently starts obeying a different definition.

## 8. Transition guards and Project policy

A transition commits only after applicable guards resolve.

Framework-level mandatory guards include categories equivalent to:

```text
STATE_VERSION_VALID
LEASE_VALID_WHEN_REQUIRED
FENCING_TOKEN_CURRENT
AUTHORITY_VALID
RISK_GATE_SATISFIED
DEPENDENCIES_SATISFIED
REQUIRED_EVIDENCE_PRESENT
NO_UNRESOLVED_BLOCKING_CONFLICT
CHECKPOINT_REQUIREMENT_KNOWN
```

Exact guard names are versioned protocol vocabulary defined by ProjectFramework 2.0 schemas/contracts.

Projects may add declarative policy guards such as security review, legal review, staging verification, customer acceptance, or Project-specific release conditions.

Invariant:

```text
Project policy may strengthen Framework mandatory guards
Project policy may not weaken/bypass Framework mandatory guards
```

Guards are evaluators, not executors. A guard may inspect evidence or authoritative state but does not itself push, deploy, send, mutate, or perform the side effect it is deciding about.

Mandatory guard result semantics are explicit and fail closed on unresolved material state. The protocol supports result classes equivalent to `PASS | FAIL | UNKNOWN | NOT_APPLICABLE` with `UNKNOWN` on an applicable mandatory guard blocking the affected transition.

## 9. Identity, authentication, sessions, and executions

Identity is separated into:

```text
ACTOR
= governed human/organizational responsibility identity

CLIENT
= software/AI integration identity

SESSION
= short-lived authenticated interaction envelope

EXECUTION
= immutable bounded work/run record
```

A long-lived client credential authenticates a client and is exchanged for a short-lived, scoped session token. The long-lived credential is not a standing Project authority token.

Session token scopes control which API operations may be called, for example state read, event read, transition request, or evidence submission. Token scope does not cause a transition guard to pass.

Actual secret values remain outside Project Source and Protocol assets. Project Source stores only governed secret references/metadata where applicable.

A session may own many immutable execution runs. Execution states are operational, with semantics equivalent to:

```text
PENDING
RUNNING
WAITING
SUCCEEDED
FAILED
CANCELLED
EXPIRED
OUTCOME_UNKNOWN
```

Execution success does not automatically complete a Task or achieve a Goal.

Chat/session context is never Project truth. A fresh session re-queries current authoritative/materialized state rather than trusting memory from a previous session.

## 10. MULTICA and multi-agent coordination

MULTICA coordination uses scoped leases instead of indefinite ownership locks.

A lease carries at least:

```text
lease_id
scope
holder session/client
expiry
fencing_token
state_version at grant/renewal context
```

The default rule is least-scope coordination: claim the smallest scope required (`RESOURCE`, `TASK`, `WORKSTREAM`, `GOAL`, or `PROJECT` as applicable) rather than blocking an entire Project.

Lease expiry makes work claimable/recoverable according to workflow policy. A newly granted lease increments/advances its fencing token. An older holder returning later cannot commit using a stale token.

Example:

```text
Agent A gets fencing token 47
A disappears / lease expires
Agent B gets token 48
A returns with token 47
→ STALE_EXECUTION / mutation rejected
```

Dependency/parallelism metadata determines claimable work. Agents do not infer safe parallelism solely from Task numbering, proximity, chat context, or personal judgement.

Lease release, execution success, and Task completion are separate events/transitions.

## 11. Public API model

The public protocol is CQRS-style:

```text
QUERY SIDE
= read materialized/current resources/state

COMMAND SIDE
= request typed governed transitions

EVENT STREAM
= read-only observation of committed state/events
```

The public API MUST NOT expose arbitrary canonical state mutation such as `PATCH status`, `PUT state`, or `SET DONE` for governed state.

Representative Query resource families include Projects, Governance Resources, Tasks, Goals, Workflows, Executions, Leases, Checkpoints, and allowed transitions.

Representative transition request envelope includes:

```text
request_id
client_id
session_id
project_uuid
subject_ref
workflow_ref
requested_transition
expected_state_version
lease_id when required
fencing_token when required
idempotency_key
authority context/reference
evidence_refs
timestamp
```

A transition response distinguishes acceptance/rejection, resulting state/version, checkpoint requirement/state, and structured failure reason.

The Event Stream is transport-neutral at protocol level. Polling, SSE, WebSocket, or another transport may implement the same event semantics without becoming a different governance model.

## 12. Typed capability contracts and adapters

AI clients request a capability, not a preferred vendor by default.

Example:

```text
REQUEST CAPABILITY: CODE_IMPACT_ANALYSIS
        ↓
Capability Registry
        ↓
eligible provider/adapter
```

Canonical capability classes include categories such as:

```text
DISCOVERY
CONTEXT_RETRIEVAL
RELATION_ANALYSIS
EVIDENCE_COLLECTION
CODE_ANALYSIS
SEMANTIC_ANALYSIS
PROJECT_MUTATION
REPOSITORY_MUTATION
EXTERNAL_COMMUNICATION
DEPLOYMENT
CUSTOM
```

Each capability contract declares input/output schemas, read/mutation mode, side-effect class, trust requirements, evidence/provenance policy, and applicable authorization/guard requirements.

Provider examples include OpenViking, Graphify, NexusRAG, GitNexus, Serena, EMIF, and future systems. No named provider is ProjectFramework authority or a universal Framework requirement.

Invariant:

```text
Tool available
≠ Capability eligible
≠ Capability authorized
≠ Transition authorized
```

Adapter results are typed with provenance and limitations. Derived systems remain derived/advisory unless authoritative verification promotes a material claim through the governed workflow.

## 13. Project Source 2.0 data model

Project Source 2.0 changes from document-centric canonical payloads to Typed Governance Resources plus Human Views.

Illustrative structure:

```text
Project-Source/
│
├─ resources/
│  ├─ governance-core/
│  ├─ work-control/
│  └─ evidence-reference/
│
├─ registry/
│  └─ active-resources.*
│
└─ views/
   ├─ current-state.*
   ├─ requirements.*
   ├─ decisions.*
   ├─ handoff.*
   └─ management.*
```

`PROJECT-BOOTSTRAP.md` remains a thin locator/bootstrap concept in the 2.0 family, but exact 2.0 bootstrap routing is defined by the Schema 2.0 contract and points to the active registry/root Project resource rather than requiring agents to infer active revisions by filename recency.

Typed resource tiers are:

### Tier 1 — Governance Core

```text
PROJECT
ACTOR
REQUIREMENT
DECISION
AUTHORITY
RISK
OUTCOME
RELATION
```

### Tier 2 — Work / Control

```text
GOAL
TASK
DEPENDENCY
CHANGE_REQUEST
ISSUE
MILESTONE
GATE
```

### Tier 3 — Evidence / Reference

```text
EVIDENCE
SECRET_REFERENCE
MIGRATION
ARTIFACT_REFERENCE
EXTERNAL_RESOURCE_REFERENCE
```

Runtime-only objects such as Session, Execution, Lease, fencing state, heartbeat, retry, event cursor, and outbox attempt do not become Project Source governance resources merely because they exist in the Control Plane.

The root `PROJECT` resource is the 2.0 governance identity/root object. It preserves immutable `project_uuid`, protocol/schema binding, Project Location/authority references as defined by Schema 2.0, and migration provenance from the 1.x `FRAMEWORK-001` root where applicable. Human views may render a familiar root/current-state representation but do not become a second authority.

## 14. Immutable resource revisions and Active Resource Registry

A governance resource has stable identity and immutable material revisions:

```text
REQ-021
├─ r001
├─ r002
├─ r003
└─ r004 ← active
```

Changing material governance payload creates a new candidate revision, validates it, promotes it, and retains prior revisions as historical truth. Last-write-wins is forbidden for semantic conflicts.

The Active Resource Registry resolves the active revision and digest for each governed resource. Consumers do not choose current truth by file timestamp, directory order, or search ranking.

The architecture distinguishes:

```text
resource_id
≠ resource_revision
≠ Control Plane state_version
≠ workflow_definition_version
```

A resource revision may carry a deterministic content digest. Base revision/digest mismatch during a governed update yields an explicit resource revision conflict rather than overwriting unseen changes.

## 15. Human Views and object/view drift

Human Views summarize/render canonical typed resources and selected checkpoint state. They are readable projections, not independent duplicate authority.

```text
Typed Resources + Active Registry
              ↓
         Human Views
```

A view that lags the Active Registry is stale. A view whose semantic claim contradicts active typed resources is `OBJECT_VIEW_DRIFT` (or the exact 2.0 drift vocabulary defined by the protocol) and blocks affected material use until reconciled.

Narrative remains supported. A typed resource may contain a concise structured payload plus a `detail_ref` to a governed Markdown design/analysis narrative, or use structured frontmatter with a narrative body where the schema permits it. ProjectFramework 2.0 is not YAML-only.

## 16. Material Checkpoint Protocol and Durable Outbox

Control Plane runtime commits and Project Source governance persistence are not one atomic database transaction.

The design therefore forbids pretending that runtime state + Git/Project Source are a synchronous atomic dual write.

A runtime transition first commits to the Event Log/materialized state. If governance materiality requires Project Source persistence, the transition creates a durable checkpoint intent/outbox record.

```text
Transition commit
      ↓
Event Log + Materialized State
      ↓
Governance-material?
   no │ yes
      │   ↓
      │ Durable Outbox
      │   ↓
      │ Project Source adapter/write
      │   ↓
      │ Result verification
      │   ↓
      │ CHECKPOINTED | PERSISTENCE_PENDING | CONFLICT/RECONCILIATION
```

Transition materiality is typed conceptually as:

```text
TRANSIENT
OPERATIONAL
GOVERNANCE_MATERIAL
```

Heartbeat, lease renewal, execution start/wait, and retry scheduling are normally operational/runtime state and do not each create Project Source revisions.

Examples of governance-material events include material Requirement/Decision/Risk/Authority changes, Task/Goal governance completion, material relation truth changes, and publication/deployment governance transitions when their canonical owners require persistence.

A durable checkpoint intent records source transition identity, Project UUID, source state version, governance owner/target resource refs, payload digest, checkpoint state, attempts, and verification refs as applicable.

AI may propose governance content. AI does not self-declare `CHECKPOINTED`. Resulting Project Source state must be independently observed/verified according to the protocol.

## 17. Failure, retry, and recovery

ProjectFramework 2.0 uses an explicit Recovery State Machine + Reconciliation model.

Key invariants:

```text
Timeout ≠ Failure
Retry ≠ Safe by default
External call success ≠ Verified outcome
Execution SUCCEEDED ≠ workflow transition committed
Workflow transition committed ≠ Project Source checkpoint persisted
Unknown material outcome must reconcile before retry
Recovery never invents authority
```

Material side effects that time out or lose transport acknowledgement become `OUTCOME_UNKNOWN` (or equivalent protocol state), not automatically `FAILED`.

Example Git push recovery:

```text
push issued
→ network timeout
→ OUTCOME_UNKNOWN
→ query authoritative remote
→ expected commit present? YES → verified success
→ definitely absent?          → safe/idempotent retry path
→ cannot determine?           → VERIFICATION_REQUIRED / manual recovery route
```

On Control Plane restart, materialized state/Event Log are loaded/replayed as necessary, active/expired leases are reconciled, in-flight/unknown executions are identified, and source-native outcomes are inspected before allowing duplicate material effects.

A session may expire while an earlier execution still requires read-only reconciliation. Expired authentication does not grant new mutation authority; recovery uses narrowly authorized reconciliation semantics.

## 18. 1.x → 2.0 major migration

Migration uses Side-by-Side Migration Workspace + Verified Promotion.

```text
Project Source 1.x (authoritative)
        ↓
DISCOVER
→ ASSESS
→ MAP
→ MATERIALIZE 2.0 CANDIDATE
→ VALIDATE
→ RECONCILE
→ APPROVE
→ PROMOTE
→ VERIFY
→ RETAIN 1.x HISTORY
```

Until promotion:

```text
1.x = Governance Authority
2.0 candidate ≠ authority
```

The migration maps existing Stable IDs and canonical payloads explicitly into typed resources when supported. Unresolved/ambiguous material mapping remains explicit and blocks affected promotion; the process never fabricates a typed object merely to make migration appear complete.

1.x source/history remains provenance. 2.0 Human Views are generated from promoted typed resources rather than becoming copied prose authorities.

A Control Plane bootstrap for the migrated Project occurs only after the 2.0 governance candidate is sufficiently valid. Initial materialized state/workflow instances are derived from the promoted governance truth under a recorded bootstrap checkpoint.

Only one Governance Authority is active at a time:

```text
DUAL ACTIVE 1.x + 2.0 GOVERNANCE AUTHORITY = FORBIDDEN
```

Rollback before promotion is simply candidate rejection. After promotion but before any non-representable 2.0-only governance change, a governed rollback may be possible if explicitly designed/verified. Once 2.0-only truth exists, returning to 1.x is a reverse migration/recovery problem, not a branch switch.

## 19. AI-ControlTower merge and canonical-source cutover

The current ProjectFramework repository remains the 1.x canonical development source until the 1.x closure/cutover gate is satisfied.

The target 2.0 cutover is:

```text
close verified Last Stable 1.x baseline
        ↓
prepare ProjectFramework 2.0 protocol candidate
        ↓
merge/migrate protocol source into AI-ControlTower/projectframework/
        ↓
verify module boundary + protocol candidate
        ↓
explicitly promote AI-ControlTower/projectframework/ as 2.x canonical development source
        ↓
ProjectFramework public repository becomes one-way release distribution mirror
```

The canonical-source role changes only through an explicit governed cutover. Merely creating a copy inside AI-ControlTower does not automatically transfer authority.

After cutover:

```text
AI-ControlTower/projectframework/
= canonical ProjectFramework 2.x development source

ProjectFramework public repository
= public verified distribution mirror
= not development authority
= not reverse-sync authority
```

Public issues/PRs may be accepted as contribution input. Accepted semantic changes are applied/reconciled in canonical AI-ControlTower source, verified, and later projected to the public mirror. A direct mirror edit never becomes canonical solely by being newer.

## 20. Release projection, licensing, and independent versioning

ProjectFramework public releases are Verified Release Projections bound to exact canonical source identity.

A release projection records or makes reconstructable:

```text
ProjectFramework version
canonical AI-ControlTower source repository/ref
canonical source commit
ProjectFramework protocol subtree/content digest
Project Source Schema version
API Protocol version
Workflow Schema version
compatibility/conformance evidence
publication target/mode
```

Publication is one-way and includes only intended ProjectFramework protocol assets.

Licensing is component-scoped:

```text
AI-ControlTower/projectframework/
= public-domain protocol/specification intent

AI-ControlTower/control-plane/
= separately licensed runtime software

AI-ControlTower/adapters/
= separately/provider-compatible licensed software

AI-ControlTower/apps/
= separately licensed software
```

The exact legal instrument for public-domain dedication and exact software license names are release/legal-packaging decisions, deliberately outside this architecture decision. Their selection must preserve the component boundary and must not silently change protocol/runtime ownership.

Versioning is independent:

```text
AI-ControlTower Version
≠ ProjectFramework Version
≠ Project Source Schema Version
≠ API Protocol Version
≠ Workflow Schema Version
```

A compatible runtime update therefore does not require a ProjectFramework version bump, and an API compatibility change does not imply a Project Source Schema change unless the relevant contracts actually change.

## 21. Conformance and public ecosystem

ProjectFramework 2.0 is implementation-neutral. AI-ControlTower is the official/current implementation platform, but third-party/local/enterprise Control Planes may implement the protocol.

Conformance areas include at least:

```text
STATE_MODEL_CONFORMANCE
TRANSITION_PROTOCOL_CONFORMANCE
AUTHORITY_BOUNDARY_CONFORMANCE
CHECKPOINT_PROTOCOL_CONFORMANCE
API_PROTOCOL_CONFORMANCE
RECOVERY_CONFORMANCE
PROJECT_SOURCE_SCHEMA_CONFORMANCE
CAPABILITY_CONTRACT_CONFORMANCE
MIGRATION_CONFORMANCE when applicable
```

`projectframework/conformance/` contains declarative conformance rules, scenarios, schemas, and test vectors. Executable conformance tooling belongs in runtime/tooling scope outside the no-runtime Protocol/Core boundary.

Conformance proves protocol behavior/representation to its declared scope. It does not grant Project authority, trust, deployment approval, or public certification beyond the evidence actually observed.

## 22. Security and trust boundaries

Security principles inherited/evolved from 1.x remain mandatory:

- no actual secret values in Project Source, public protocol assets, evidence narratives, or public release projection;
- authentication is separate from authorization;
- session token scope is separate from Project Authority;
- provider/tool availability is separate from trust and capability eligibility;
- external disclosure remains purpose- and authority-bounded;
- stale/unknown material trust or authority fails closed for the affected action;
- leases/fencing prevent stale actors from committing after ownership has moved;
- event/checkpoint histories preserve material provenance rather than rewriting failure history;
- public mirror publication cannot include runtime secrets, credentials, private adapter configuration, or differently licensed runtime assets by accident.

The public API protocol defines security-relevant fields/semantics without embedding real credentials or forcing one identity provider implementation.

## 23. V1.14 closure and V2 implementation gate

Design of 2.0 may proceed before V1.14 release closure. V2 implementation/canonical-source merge may not.

Framework 1.14 is designated the intended **Last Stable 1.x Baseline** unless a narrowly justified 1.x hotfix release is required before cutover.

Before V2 implementation or merge into AI-ControlTower:

```text
TASK-036 DONE
TASK-030 DONE
TASK-029 DONE
TASK-031 DONE
Framework 1.14 starter/distribution propagation complete
cumulative AFFECTED PASS
one final unchanged-candidate RELEASE_FULL PASS
release evidence committed
OUT-008 terminal reconciliation complete
verified 1.14 stable source/candidate identity available for migration baseline
```

Remaining 1.x backlog is triaged instead of blindly completed:

```text
COMPLETE_BEFORE_2X
= prerequisite/integrity work required for trustworthy 1.x baseline or migration

CARRY_FORWARD_TO_2X
= valuable intent whose implementation belongs on the 2.0 architecture

SUPERSEDED_BY_2X
= backlog made obsolete/redundant by the new state/workflow/control-plane model
```

This avoids wasting effort implementing 1.x mechanisms that 2.0 intentionally replaces, while preserving a clean migration source.

## 24. Scope boundaries and non-goals of this design Goal

This Goal completes architecture/design only.

It does NOT authorize or perform:

```text
ProjectFramework 2.0 runtime implementation
AI-ControlTower runtime/code changes
ProjectFramework → AI-ControlTower repository merge
canonical-source cutover
Project Source 1.x → 2.0 migration
API server/token service creation
state/event database creation
MULTICA runtime changes
adapter implementation
public-domain legal instrument selection
software license selection
public mirror publication
push/merge/publication
Framework 1.14 cumulative acceptance/release closure
```

Those require subsequent governed work after the written design review and, for implementation/cutover, after the V1.14 closure gate.

## 25. Design acceptance and verification strategy

The written design is complete when it contains no unresolved architectural placeholder, preserves the approved decisions above, keeps logical authority domains distinct, defines deterministic behavior for state/workflow/concurrency/recovery/persistence, explains 1.x migration/cutover, and states implementation/non-goal boundaries.

Future implementation acceptance must include scenario coverage for at least:

- arbitrary state mutation rejected in favor of typed transitions;
- stale `state_version` rejected;
- duplicate idempotency key does not duplicate a material effect;
- expired/stale lease/fencing token cannot commit;
- agent/session expiration does not silently cancel unrelated governance state;
- mandatory guards cannot be weakened by Project policy;
- `UNKNOWN` applicable mandatory guard fails closed;
- runtime event does not automatically create a governance revision;
- governance-material checkpoint failure becomes explicit persistence/reconciliation state;
- timeout/external unknown outcome reconciles before retry;
- Event Log can reconstruct/reconcile materialized state within declared scope;
- Human View cannot outrank conflicting active typed resource;
- Active Resource Registry resolves current revision without recency guessing;
- 1.x remains authoritative until verified 2.0 promotion;
- dual 1.x/2.0 active governance authority is rejected;
- public mirror projection matches exact canonical protocol candidate/digest;
- differently licensed runtime/adapters cannot leak into the public protocol projection;
- third-party capability output remains advisory/typed until governed evidence/transition rules permit promotion;
- authentication/token scope cannot bypass Project Authority or transition guards.

The original design Goal created no implementation plan. That gate is now satisfied: Framework 1.14 is the canonical Last Stable 1.x Baseline and the user's 2026-09-05 `[Goal]` approves this written spec for pre-merge planning. The current workflow is to prepare the governed implementation/migration plan, merge manifest, target verification, and Pre-Merge Readiness evidence; actual AI-ControlTower merge/canonical-source cutover remains a later explicit execution step.

## 26. Forward-port and Pre-Merge planning status — 2026-09-05

The architecture above is unchanged. This section records the state transition from design-only work to merge preparation.

```text
Original design checkpoint: 6c9fd543c34e939db914c80e4c3354b3b36a0906
Original design base: 9f5a6fb1f8d26b80049a4a9521e50c38a99126be
Canonical Last Stable 1.x baseline: aae65796a8d4ad5f23323889b65b060bd36302c1
Canonical Framework-Source tree: d5d04e4563157246872b1e02c791b94a6c564d95
Framework 1.14 publication: MERGED_TO_MAIN / PERSISTED / NOT_PENDING
Current branch: v2-premerge-readiness
```

The first direct Git merge of the old design branch was intentionally invalidated before publication because branch-local `EVD-071 / CHG-071` collided with canonical V1 release IDs allocated after the design checkpoint. The valid forward-port imports the design/spec payload with provenance while allocating new current evidence/change IDs. Stable IDs are never silently rebound across merged history.

The current Goal is bounded to preparation through `PRE_MERGE_READY`: forward-port/reconcile design truth, write and self-review the implementation/migration plan, produce the merge manifest, verify the AI-ControlTower target/bindings/current architecture, define rollback and compatibility/version/licensing boundaries, and run the Pre-Merge Readiness Gate. It does not itself mutate AI-ControlTower Project Source/code, perform the ProjectFramework repository merge, promote `AI-ControlTower/projectframework/` as canonical, implement Control Plane runtime, or publish a public mirror.