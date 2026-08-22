# Core Project Source Document Skeletons

Use these skeletons only after creating active `00-Project Source Framework` (`FRAMEWORK-001`). Every governed descendant inherits from that Framework. They are structural recipes, not authoritative Project facts. Replace placeholders only with verified/user-confirmed data; otherwise use explicit `UNKNOWN`, `ASSUMED`, `STALE`, or `VERIFICATION_REQUIRED` state.

For concrete slot/file starters, read `project-source-mockup/README.md`. Mockup and skeletons must remain aligned; Core Governance is authoritative on conflict. Conditional templates exist for discoverability and do not require empty active documents.

Framework `1.2.0` treats exact Git provenance as optional assurance. If provenance is tracked, active `00` and `14 Project Source Manifest` must agree on observed values. Never invent tag/SHA values merely to make records look complete.

Framework `1.2.3` adds Development Workspace / Runtime Authority semantics without changing Schema `1.0.0`, slot ownership, or Framework `1.2.2` Git Base Freshness vocabulary.

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
project_source_framework_version: "1.2.3"
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
Active Actions (ACT refs)
Active Issues / DRIFT / CONFLICT refs
Active RISK / ASM / DEP / MS / OUT / CR / GATE refs when applicable
Current Blockers
Freshness Warnings
Exact Next Action
Last Verified
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
External Working Source / Pointers
Unpersisted Material State when applicable
Required Read Order
Authority References
authority_transfer: false
Freshness Warnings
Exact Next Action
Chat Continuity: CONTINUE_CURRENT_CHAT | START_NEW_CHAT
Chat Continuity Reason
Required Read Before Continue
```

Handoff is a continuation contract, not an MCP transcript or execution log. Persist current usable state/pointers and unresolved material state; do not dump raw connector payloads or repetitive intermediate activity.

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

`AUTH-*` records grantor, grantee, actions, scope/paths, forbidden actions/effects, risk ceiling, start, expiry/termination, status.

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

Each Action has an exact executable next step. `ACT DONE` does not automatically mean `MS REACHED` or `OUT ACHIEVED`.

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