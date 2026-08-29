# Core Project Source Document Skeletons

Use these skeletons only after creating active `00-Project Source Framework` (`FRAMEWORK-001`). Every governed descendant inherits from that Framework. They are structural recipes, not authoritative Project facts. Replace placeholders only with verified/user-confirmed data; otherwise use explicit `UNKNOWN`, `ASSUMED`, `STALE`, or `VERIFICATION_REQUIRED` state.

For concrete slot/file starters, read `project-source-mockup/README.md`. Mockup and skeletons must remain aligned; Core Governance is authoritative on conflict. Conditional templates exist for discoverability and do not require empty active documents.

Framework `1.2.0` treats exact Git provenance as optional assurance. If provenance is tracked, active `00` and `14 Project Source Manifest` must agree on observed values. Never invent tag/SHA values merely to make records look complete.

Framework `1.2.3` adds Development Workspace / Runtime Authority semantics without changing Schema `1.0.0`, slot ownership, or Framework `1.2.2` Git Base Freshness vocabulary.

Framework `1.2.4` adds **Project Location Binding** and Chat Closure Consistency without changing Schema `1.0.0`. Active `00 / FRAMEWORK-001` is the canonical home of GitHub/Drive binding. `03` and `09` may carry references/pointers for current-state and continuation purposes but MUST NOT duplicate location authority. Before Material GitHub/Drive mutation, resolve the active binding state and fail closed when it is `VERIFICATION_REQUIRED` or `NOT_APPLICABLE` as defined by Core Governance.

Framework `1.2.6` adds a Project-specific **Bootstrap Location Block** for pre-`FRAMEWORK-001` discovery plus governed non-Drive **File Storage Binding** under active `FRAMEWORK-001`, while Schema stays `1.0.0`. Framework Source / Remote / File Storage / MCP / Local Workspace / current branch-worktree remain distinct; current Git state is dynamic. Google Drive remains canonical in the dedicated root Drive binding; generic File Storage covers non-Drive content scopes. Existing Projects remain pinned and migration invents no locations/provider applicability.

Framework `1.2.5` adds environment-scoped **Local Workspace Binding**, **Verified Task Completion Checkpoint**, progressive/risk-scoped verification with evidence reuse, and the **Response Close Completeness Gate**. `00 / FRAMEWORK-001` remains the routing authority; `09`, `15`, and `40` reference observed workspace/commit/verification state without becoming competing location, branch, or implementation authority.

Framework `1.3.0` adds registered bracketed `[Project Status]` / `[Project Path]` commands, Markdown-safe response-close presentation, and Direct-to-Latest cumulative upgrades using `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`. Existing Projects remain pinned; intermediate release execution is not mandatory, but current truth/Stable IDs/Project-specific rules/history/approval/rollback/validation remain preserved.

Framework `1.3.1` adds registered `[Project Upgrade]` as a read-only fresh comparator between the active local Framework pin and canonical upstream target evidence. It reports `UP_TO_DATE | UPGRADE_AVAILABLE | SOURCE_DIVERGENCE | VERIFICATION_REQUIRED`; a detected difference asks whether to prepare an upgrade, and a positive answer authorizes assessment/Preview only—not mutation. Schema remains `1.0.0` and existing Direct-to-Latest approval/preservation rules remain unchanged.

Framework `1.6.0` standardizes conditional `92 Project Graph` as the canonical home of current `REL-*` Project-relation assertions. Endpoints use immutable `project_uuid`; AI-ControlTower/OpenViking indexing is `DERIVED_ONLY` and rebuildable; relation topology remains distinct from Project Location Binding, Git integration, implementation, and runtime authority.

Framework `1.7.0` standardizes root `PROJECT-BOOTSTRAP.md` for NEW Projects. It is outside Project Source, has no Stable ID, and routes `PROJECT-BOOTSTRAP.md → 00 → 01 → 03`, with `09` for continuation. Active `FRAMEWORK-001` remains authority; Brownfield adoption is `[Project Upgrade]`-only; vendor settings and `PROJECT-CONFIG.md` remain optional adapters/location references.

Framework `1.8.0` registers persistent `[Goal]` without a `GOAL-*` family: Goal outcome uses `OUT-*` in conditional `91`, durable authority uses `AUTH-*` in `12`, execution uses `ACT-* / ENV-*` in `15`, `03` summarizes Goal state, and `09` carries references only with `authority_transfer: false`. No active Goal is synthesized during GREENFIELD initialization; `[Goal]` materializes `91` only when a persistent Goal becomes applicable.
## Common YAML Header Pattern

```yaml
---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<DOCUMENT_ID>"
document_type: "<DOCUMENT_TYPE>"
semantic_slot: "<NN>"
revision: 1
document_status: "ACTIVE"
inherits_from:
  - "FRAMEWORK-001"
created_at: "<ISO8601>"
updated_at: "<ISO8601>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "<CLASS>"
project_source_framework_version: "1.8.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
```

## 01 — Project Source Index

Required sections:

```text
Project Identity
Bootstrap Read Order
Active Document Registry (DERIVED)
Task Routing
Active Warnings / Drift / Conflict
Current Handoff
Current Manifest
```

When active, route:

```text
40 Technical Design → Tech Stack / components / source / workspace / config / runtime / deployment-mode architecture
60 Deployment Plan → installation / source-runtime mapping / persistence-recreation / startup / verification / operations / rollback / backup
91 Project Management Control → RISK / ASM / MS / OUT / DEP / CR / GATE
92 Project Graph → REL-* current Project relation assertions when active
```

Do not manually treat the derived registry as authoritative.

## 02 — Project Overview

Required sections:

```text
Project Identity
Purpose / Objective
In Scope
Out of Scope
Stakeholders / Systems
Known Constraints
Current High-Level Architecture/Context
Authoritative External Sources
Project Lineage
Project-Specific Terminology
```

## 03 — Current State

Pure current snapshot only:

```text
Lifecycle State
Execution State
Current Phase
Current Scope
Current Owner/Actor
Current Source-of-Truth references

Project Location Binding Reference (FRAMEWORK-001; includes applicable Local Workspace Binding; no duplicate authority)
Active Actions (ACT refs)
Active Issues / DRIFT / CONFLICT refs
Active RISK / ASM / DEP / MS / OUT / CR / GATE refs when applicable
Current Blockers
Freshness Warnings
Exact Next Action
Last Verified

Persistent Goal view when applicable:
  Active Goal OUT-*
  Goal Status: ACTIVE | BLOCKED | ACHIEVED | CANCELLED | SUPERSEDED
  Success Criteria Progress
  Authorization AUTH-* validity
  Current / Next ACT-*
  Push / Destructive / Root-Binding / External-Disclosure inclusion flags
  Current Goal Blocker
  Continuation Freshness
```

### Project Health

Use applicable dimensions only:

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

State vocabulary:

```text
GREEN AMBER RED UNKNOWN
```

Each dimension records/resolves:

```text
State
Reason
Supporting Stable IDs / Evidence
Owner
Last Reviewed
Next Review / Trigger when applicable
```

Do not average away critical RED dimensions with an opaque aggregate score.

### Review Cadence

Review cadence may be:

```text
TIME_BASED
EVENT_BASED
```

Possible governed reviews include Current State, Risk, Assumption, Milestone/Outcome, Decision Revalidation, Technical Design, Deployment Readiness, and Handoff Refresh. This is documentation semantics, not a scheduler/runtime.

## 04 — Decision Log

Canonical home of `DEC-*`.

Each major Decision records:

```text
DEC-ID
Status
Decision
Reason
Alternatives / Rejections when material
Approved By
Approved At
Validity Basis
Review Trigger
Review By
Last Revalidated
Revalidation Status
Revalidation Evidence
Related REQ / ACT / RISK / ASM / DEP / CR / GATE / EVD
Supersedes / Superseded By
```

Recommended Revalidation Status:

```text
NOT_DUE REVIEW_DUE REVALIDATED SUPERSEDED
```

A Decision previously approved is not assumed valid forever if its stated validity basis no longer holds.

In an active revision, each current `DEC-*` record must materialize current Decision/Status semantics or link to an active/current canonical Detail Document. Archive-dependent shorthand is insufficient.

## 05 — Requirements

Canonical home of `REQ-*`.

Each requirement records:

```text
REQ-ID
Status
Requirement
Acceptance / Verification Criteria
Priority / Scope when relevant
Epistemic Status
Related DEC / ACT / RISK / ASM / DEP / MS / OUT / CR / GATE / EVD
Supersedes / Superseded By
```

Active current requirements must materialize current Requirement/Status/Acceptance semantics without archive dependency.

## 06 — Architecture [CONDITIONAL]

Create when Project has meaningful systems/components/interfaces.

```text
Architecture Scope
Components
Interfaces
Data Flow
Dependencies
Security / Authority Boundaries
Runtime / Deployment Boundaries
Key Architecture Decisions
Known Constraints
```

`06` is the major architecture view. Use `40 Technical Design` when deeper implementation-facing detail is needed; do not duplicate/fork authoritative payload.

## 07 — Implementation Plan [CONDITIONAL]

Create when implementation work exists.

```text
Goal
Approved Scope
Prerequisites
Task / Action Mapping (ACT refs)
Milestone references (MS)
Dependency references (DEP)
Risk references (RISK)
Change Request references (CR)
Review Gate references (GATE)
Implementation Sequence
Risk Classification
Verification Strategy
Rollback / Reversibility
Completion Criteria
```

Technical planning does not silently authorize application code, Dockerfile/Compose, scripts, CI, or automation when user requested documentation/governance only.

## 08 — Open Issues [CONDITIONAL]

Canonical home of `ISS-*`, `DRIFT-*`, `CONFLICT-*`.

Each entry records type, status, affected scope, owner, evidence, blocking semantics, and resolution/next action.

Knowledge/documentation debt uses:

```text
issue_type: KNOWLEDGE_DEBT
```

Record Missing/Stale Knowledge, Affected Scope, Impact, Owner, Required Source Update, related implementation/runtime observation, related REQ/DEC/CR/EVD, Next Action, Status. Material Knowledge Debt makes `08` applicable if it was previously absent.

A material Canonical Implementation Source / Runtime mismatch that should align is also `DRIFT-*`; do not invent a workspace/runtime-specific Stable-ID family.

## 09 — Handoff

Required sections:

```text
Handoff From / To
Previous Handoff
Trigger
Current Phase / State
Completed Work
Pending Work
Formal Drafts / WIP
Active ACT / ISS / DRIFT / CONFLICT
Active RISK / ASM / DEP / MS / OUT / CR / GATE when applicable
Technical / Deployment health warnings
Source/Docker known variance when applicable
Knowledge Debt affecting continuation
Material Persistence State: PERSISTED | PERSISTENCE_PENDING | NOT_APPLICABLE

Project Location Binding Reference / Pointers (FRAMEWORK-001; no independent binding copy)
External Working Source / Pointers
Unpersisted Material State when applicable
Required Read Order
Authority References
Active Goal: OUT-* when applicable
Goal Status
Goal Authorization: AUTH-*
Current Goal Action: ACT-*
Goal Envelope: ENV-* or none
Last Verified Goal Authorization At
Next Safe Goal Action
Goal Blocker when applicable
authority_transfer: false
Freshness Warnings
Exact Next Action
Chat Continuity: CONTINUE_CURRENT_CHAT | START_NEW_CHAT
Chat Continuity Reason
Required Read Before Continue
```

Handoff is a continuation contract, not an MCP transcript or execution log. Persist current usable state/pointers and unresolved material state; do not dump raw connector payloads or repetitive intermediate activity.

Chat closure invariants:

```text
Exact Next Action = ไม่มีขั้นตอนถัดไป → Chat Continuity = START_NEW_CHAT
Chat Continuity = CONTINUE_CURRENT_CHAT → one concrete Exact Next Action required
Material Persistence State = PERSISTENCE_PENDING → CONTINUE_CURRENT_CHAT + concrete persistence/recovery action
```

`START_NEW_CHAT` may still carry a concrete Next Action when state is durably persisted and fresh-chat continuation is safe.
Lifecycle: `DRAFT → OFFERED → ACKNOWLEDGED → ACCEPTED → SUPERSEDED`.

## 10 — Change Log

Canonical home of logical append-only `CHG-*` history.

```text
CHG-ID
Timestamp
Actor / Instance
Object / Document
Previous State
New State
Reason / Trigger
Related User Instruction / DEC / CR / EVD
```

`CR-*` is proposed/material change control in `91`; `CHG-*` records applied/observed historical change.

## 11 — Actor Registry

Canonical home of `ACTOR-*` and `INST-*`.

Record actor type, display name, platform, role, status, and instance relation. Role is descriptive only; authority is in `12`.

### Responsibility Mapping

Responsibility rows are keyed by governed scope such as Stable ID, semantic document, workstream, or explicit Project scope:

```text
Scope
Responsible
Accountable
Consulted
Informed
```

**Responsibility ≠ Authority.** RACI-style mapping grants no mutation/approval permission.

## 12 — Authorization Registry

Canonical home of `AUTH-*` and `DEL-*`.

`AUTH-*` records grantor, grantee, actions, scope/paths, forbidden actions/effects, risk ceiling, start, expiry/termination, status. Goal-related `AUTH-*` additionally records related `OUT-*`, explicitly included shared/external effects, revocation trigger, and approval/evidence reference.

For persistent `[Goal]`, terminal `OUT-*` state `ACHIEVED | CANCELLED | SUPERSEDED` terminates/supersedes dependent Goal authority. Handoff references never transfer that authority. Unless explicitly narrowed, Goal authority may cover bounded local development; push/destructive/Root-Binding/external-disclosure effects retain exact opt-in rules and actual secret values are forbidden.

`DEL-*` references parent authorization and never exceeds parent scope/risk/actions/duration.

## 13 — Evidence Registry

Canonical home of `EVD-*`.

```text
EVD-ID
Evidence Type
Captured At
Captured By Actor/Instance
Source Reference
Artifact Path
Artifact Hash
Supports (Stable IDs)
Epistemic Status
```

Never store actual secrets as evidence.

### External AI Council / `[Meeting]` Evidence Specialization

When a Meeting materially informs governed Project truth, use existing `EVD-*` rather than a new Meeting family. Record only minimum reconstructable advisory evidence:

```text
Evidence Type: EXTERNAL_AI_COUNCIL / ADVISORY
Meeting Question
Context Scope / Disclosure Basis
Provider/Profile + observed version when material
Participating models / Chairman when reported
Stage completeness
Independent views / disagreement / synthesis bounded summary or source-native pointer
Provider/runtime failures
Supports
Epistemic Status
Advisory-only notice
```

Transient exploratory Meetings require no synthetic evidence record. Provider conversation JSON is provider-local state and never canonical Project history or authority.

## 14 — Project Source Manifest

Current Reconstructable Snapshot inventory.

Track active documents, continuation-relevant formal drafts, registered evidence, pinned schema/validation assets, required generated assets, and every active/current Detail Document required to interpret referenced current Stable IDs.

When active/current `40`, `60`, or `91` is required to interpret current truth, include it in Manifest and `CURRENT` export scope.

When source provenance is tracked, continuation metadata may include:

```text
Repository
Source Ref
Optional Release Tag when observed
Optional Resolved Commit SHA when observed
Framework Version
Schema Version
Captured At
Provenance Status: VERIFIED / PARTIAL / UNVERIFIED
```

Never invent exact provenance. Manifest does not recursively hash its own raw bytes.

## 15 — Action Registry

Canonical home of `ACT-*`.

```text
TODO → IN_PROGRESS → DONE
side states: BLOCKED / CANCELLED
```

Each Action has an exact executable next step. For Material Git-backed mutation, record affected verification/completion criteria, verification result/evidence pointer, completion commit(s), and remaining working-tree state when relevant. `DONE` is prohibited while required completed state exists only uncommitted. Read-only/no-mutation Actions need no synthetic commit. `ACT DONE` does not automatically mean `MS REACHED` or `OUT ACHIEVED`.

Goal-derived `ACT-*` records parent Goal `OUT-*` and parent `AUTH-*`. Goal-derived `ENV-*` records the same parent references and MUST remain equal to or narrower than current valid parent `AUTH-*`; it may be derived/refreshed without new user approval only inside that boundary. `ENV-*` never expands authority or waives higher-level controls.

All linked Goal Actions becoming `DONE` still does not prove Goal `OUT-*` `ACHIEVED`; success criteria/evidence are evaluated separately.

## 16 — Migration Registry

Canonical home of `MIG-*`.

Record source/target versions or structure, compatibility assessment, affected docs/objects, steps, reversibility/rollback, approval, validation, evidence, lifecycle.

Framework `1.2.0` migration checks explicitly include:

```text
slot 91 occupancy/collision
preserve custom 91 identity/history/references
approved relocation before standard 91 activation
no automatic promotion of old free-text into new management Stable IDs
```

Framework `1.2.3` migration does not invent workspace topology. Unknown Canonical Implementation Source, workspace durability, Source-to-Runtime Mapping, Runtime Mutability Boundary, or Persistent-State Boundary remains explicit uncertainty until verified from actual source/runtime evidence.

## 17 — Secret Reference Registry

Canonical home of `SECRET-*` metadata only.

```text
SECRET-ID
Secret Type
System / Environment
External Storage Reference
Required Authority
Status
secret_value_present: false
```

Actual secret values are forbidden.

# Extended Conditional Skeletons

## 40 — Technical Design [CONDITIONAL]

Create when technical design depth is needed beyond `06 Architecture`.

Required/expected sections when applicable:

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

### Tech Stack Contract

Each material technology records:

```text
Technology
Role / Responsibility
Version or Supported Range
Required / Optional
Why Used / Decision Reference
Used By Component(s)
Operational Dependency
Lifecycle / Support Constraint when material
Replacement Boundary when material
Epistemic / Verification State
```

### Source Structure Blueprint

Document responsibilities/ownership of source areas; do not prescribe directory names when Project differs. Example roles:

```text
src/          application implementation responsibility
config/       non-secret configuration responsibility
tests/        verification-asset responsibility
migrations/   schema/data migration responsibility
scripts/      operational-helper responsibility
```

### Development Workspace Contract

When material, document/resolve:

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

Descriptive workspace types may include:

```text
LOCAL_WORKSPACE
GIT_WORKTREE
REMOTE_DURABLE_WORKSPACE
DEV_CONTAINER_DURABLE_WORKSPACE
OTHER_DECLARED_WORKSPACE
```

Descriptive mappings may include:

```text
DIRECT_EXECUTION
BIND_MOUNT
WORKSPACE_VOLUME
IMAGE_OR_ARTIFACT_BUILD
REMOTE_SYNC
OTHER_DECLARED_MAPPING
```

These are blueprint vocabulary, not Project states or Stable-ID families. Canonical source durability is lifecycle/recovery semantics and does not impose physical host-local storage.

### File Storage / Content Ownership Mapping

When material, reference active `FRAMEWORK-001` File Storage Binding by `storage_key` / content scope and document `content scope → provider → canonical durable locator → environment access path/mount`. Do not copy independent binding authority into `40`. File Storage Binding does not become Canonical Implementation Source or Development Workspace authority merely because source files are accessible there; any such implementation role must be separately declared/verified. Mounted/synced/cache paths are mapping evidence only.

### Configuration Contract

```text
Application Settings
Environment-specific Settings
External Service Endpoints
Persistence Settings
Feature / Capability Settings when material
Secret References
```

Semantic configuration meaning stays consistent across packaging modes. Actual secrets remain external.

### Deployment Support

```text
SOURCE_ONLY
DOCKER_ONLY
SOURCE_AND_DOCKER
NOT_APPLICABLE
```

If `SOURCE_AND_DOCKER`, document shared application/configuration/data/security/persistence contract plus explicit Deployment Mode Variance for intentional differences. Unexpected mismatch is `DRIFT-*`.

## 60 — Deployment Plan [CONDITIONAL]

Create when installation/deployment/operation is in Project scope.

Required/expected sections:

```text
Deployment Scope
Deployment Support
Common Prerequisites
Supported OS / Platform / Architecture
Deployment Source / Artifact Acquisition
Required Runtime / Container Runtime
External Services
Required Permissions
Configuration / Secret References
Source-to-Runtime Mapping
Runtime Mutability Expectation
Persistent-State Boundary
Data / Storage Authority
Replacement / Recreation Expectation
Development-only vs Production Mapping Differences
Data / Storage Initialization
Source Installation View
Docker Installation View
Startup / Shutdown
Verification / Health
Logs / Diagnostics
Upgrade
Rollback
Backup / Restore
Uninstall / Cleanup
Troubleshooting
Known Limitations / Deployment Mode Variance
Related REQ / DEC / RISK / DEP / CR / GATE / EVD
```

When Project File Storage is relevant to deployment, reference the active `FRAMEWORK-001` storage scope rather than redefining it. `File Storage Binding ≠ Runtime Data / Storage Authority ≠ Persistent-State Boundary`. The same physical target may serve multiple roles only when each role is explicitly declared; backup/mirror/mount/sync accessibility does not transfer current authority.

A real Project may record concrete verified commands/paths. A synthetic/template context must not invent executable commands for nonexistent software.

Installation/start command success alone is not operational readiness; verification must examine resulting state appropriate to the Project/risk, including survival of state required by the declared replacement/recreation lifecycle.

Runtime-only mutation does not become canonical Implementation Truth merely because execution succeeds. If runtime and Canonical Implementation Source should align but differ materially, use `DRIFT-*`.

## 91 — Project Management Control [CONDITIONAL / STANDARD IN 1.2.0+]

Canonical home of exactly:

```text
RISK-* Risk
ASM-*  Assumption
MS-*   Milestone
OUT-*  Outcome
DEP-*  Dependency
CR-*   Change Request
GATE-* Review / Phase Gate
```

Persistent `[Goal]` specializes ordinary `OUT-*` rather than replacing it. A Goal `OUT-*` records Outcome Statement, Success Criteria/Measure, Evidence Required, Scope, Prohibited Zones, Owner, `ACTIVE | BLOCKED | ACHIEVED | CANCELLED | SUPERSEDED`, related `AUTH-*`, related `ACT-*`, applicable REQ/DEC/RISK/DEP/GATE refs, approval metadata, Last Evaluated, and Terminal Evidence. `[Goal]` makes conditional `91` applicable only when such Goal truth is material; initialization never fabricates one.


### RISK-* Recipe

```text
RISK-ID
Title
Risk Statement
Category
Probability
Impact
Exposure / Severity when used
Trigger / Early Warning
Mitigation
Contingency
Owner
Review Trigger / Review By
Status
Related REQ / DEC / ASM / DEP / MS / OUT / CR / EVD
Materialized Issue when applicable
```

Statuses may include `IDENTIFIED / OPEN / MITIGATING / MONITORING / ACCEPTED / MATERIALIZED / CLOSED / SUPERSEDED`.

### ASM-* Recipe

```text
ASM-ID
Statement
Basis
Why It Matters
Impact If False
Verification Method
Verification Owner
Review Trigger / Review By
Status
Evidence
Related REQ / DEC / RISK / DEP / MS / CR
```

Statuses: `UNVERIFIED / VALIDATED / INVALIDATED / SUPERSEDED`.

### MS-* Recipe

```text
MS-ID
Milestone
Success / Exit Criteria
Target Window or Trigger when applicable
Owner
Status
Dependencies
Required Evidence
Related REQ / ACT / RISK / ASM / DEP / GATE
Reached At when applicable
```

### OUT-* Recipe

```text
OUT-ID
Outcome Statement
Success Measure / Evidence
Baseline when applicable
Target
Measurement Method
Owner
Status
Related REQ / DEC / MS / EVD
Last Evaluated
```

### DEP-* Recipe

```text
DEP-ID
Dependency Type
Depends On
Required For
Owner
Expected Availability / Trigger
Current State
Fallback / Workaround
Failure Impact
Related RISK / ASM / MS / ACT / CR / EVD
Status
```

`AVAILABLE` and `SATISFIED` have distinct meanings.

### CR-* Recipe

```text
CR-ID
Requested Change
Reason / Trigger
Requester
Affected Scope
Impact Assessment
Affected REQ / DEC / Architecture / Technical Design / Deployment / MS / OUT / RISK / DEP
Authority / Approval Requirement
Decision
Implementation / Migration References when applicable
Verification Requirement
Status
```

### GATE-* Recipe

```text
GATE-ID
Purpose
Affected Scope
Entry Criteria
Exit / Pass Criteria
Required Evidence
Related REQ / DEC / RISK / ASM / DEP / MS / CR
Review Owner
Required Authority
Status
Findings
Exceptions / Waiver
Next Action
Reviewed At
```

`WAIVED` requires explicit rationale plus authority/Decision reference.

**Resume Block (latest checkpoint):**

```text
Task: <TASK/ACT id> | Done: <last completed step> | Next: <exact next step> | Blockers: <none or list> | Envelope: <ENV-* or none>
```

## 92 — Project Graph [CONDITIONAL / STANDARD IN 1.6.0+]

Create only when Project relation truth is applicable. Canonical home of current `REL-*` records.

Minimum relation fields:

```text
Relation ID: REL-*
Source Project UUID
Target Project UUID
Relation Type
Direction
Assertion State
Related Stable IDs
Evidence / Source Pointers
Last Verified / Reviewed
Notes when material
```

Core relation types are exactly `PARENT_OF | CHILD_OF | PEER_OF | DEPENDS_ON | SUPPORTS | RELATED_TO`. Project/domain extensions use `X-<PROJECT_OR_DOMAIN_NAMESPACE>:<RELATION_TOKEN>` and must not redefine a core token.

Assertion state is exactly `ASSERTED | CORROBORATED | CONFLICTED | RETIRED`. Reciprocal corroboration requires verified compatible authoritative assertions with matching endpoint UUIDs: `PARENT_OF ↔ CHILD_OF`, `CHILD_OF ↔ PARENT_OF`, `PEER_OF ↔ PEER_OF`, `RELATED_TO ↔ RELATED_TO`. Derived inverse edges are traversal aids only and never become another Project's assertion.

`REL-*` stores graph linkage/pointers, not duplicated authoritative payload from `DEP-*` in `91`, `DEC-*` in `04`, `REQ-*` in `05`, or `ISS-* / DRIFT-* / CONFLICT-*` in `08`.

Project relation endpoints use immutable `project_uuid`. `PARENT_OF` / `CHILD_OF` is semantic topology and does not imply nested folders/repositories/workspaces or transfer Repository/File Storage/Local Workspace Binding, current branch/worktree, Canonical Integration Target, Canonical Implementation Source, Runtime Location, Authority, or Risk approval.

AI-ControlTower owns cross-Project indexing/orchestration. OpenViking is `DERIVED_ONLY` and `REBUILDABLE`; it may normalize/query/correlate/index and surface stale/orphan/conflicting derived state, but Project Source wins on disagreement. Reuse existing `DRIFT-*`, `CONFLICT-*`, and `MIG-*` families. No OpenViking credentials/runtime configuration belongs in this document.
