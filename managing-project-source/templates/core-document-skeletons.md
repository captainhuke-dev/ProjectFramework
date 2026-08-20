# Core Project Source Document Skeletons

Use these skeletons only after creating the active `00-Project Source Framework` (`FRAMEWORK-001`). Every governed descendant inherits from that Framework. They are structural recipes, not authoritative project facts. Replace placeholders only with verified/user-confirmed data; otherwise use explicit `UNKNOWN`, `ASSUMED`, `STALE`, or `VERIFICATION_REQUIRED` state.

For a concrete slot/file starter view, read `project-source-mockup/README.md`. The mockup and these skeletons must remain aligned; Core Governance is authoritative on conflicts. Conditional `06–08` templates are discoverability aids and do not require empty active documents.

Framework `1.1.4` provenance is recorded in the active `00` body and mirrored as continuation metadata in `14-Project Source Manifest`; do not invent missing release tag/SHA values merely to make the Manifest look complete.

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
project_source_framework_version: "1.1.4"
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

Pure snapshot only:

```text
Lifecycle State
Execution State
Current Phase
Current Scope
Current Owner/Actor
Current Source of Truth references
Active Actions (ACT refs)
Active Issues / DRIFT / CONFLICT refs
Current Blockers
Freshness Warnings
Exact Next Action
Last Verified
```

No historical timeline here.

## 04 — Decision Log

Canonical home of `DEC-*`.

Each major decision records:

```text
DEC-ID
Status
Decision
Reason
Alternatives / Rejections when material
Approved By
Approved At
Related REQ / ACT / EVD
Supersedes / Superseded By
```

In an active revision, each current `DEC-*` record must materialize the current Decision/Status semantics, or link to an active/current canonical Detail Document that contains them. Do not use archive-dependent shorthand such as `retain previous status`, `unchanged from rNNN`, or `see archived revision` as the authoritative current record. Any required Detail Document must be included in the Current Reconstructable Snapshot and in `CURRENT` export when needed to interpret the Decision.

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
Related DEC / ACT / EVD
Supersedes / Superseded By
```

In an active revision, each current `REQ-*` record must materialize the current Requirement/Status/Acceptance semantics, or link to an active/current canonical Detail Document that contains them. Do not use archive-dependent shorthand such as `retain previous status`, `unchanged from rNNN`, or `see archived revision` as the authoritative current record. Any required Detail Document must be included in the Current Reconstructable Snapshot and in `CURRENT` export when needed to interpret the Requirement.

## 06 — Architecture [CONDITIONAL]

Create when the project has meaningful system/components/interfaces.

```text
Architecture Scope
Components
Interfaces
Data Flow
Dependencies
Security/Authority Boundaries
Runtime/Deployment Boundaries
Key Architecture Decisions (DEC refs)
Known Constraints
```

## 07 — Implementation Plan [CONDITIONAL]

Create when implementation work exists.

```text
Goal
Approved Scope
Prerequisites
Task/Action Mapping (ACT refs)
Implementation Sequence
Risk Classification
Verification Strategy
Rollback/Reversibility
Completion Criteria
```

Do not silently turn this into software tooling work when the user requested documentation only.

## 08 — Open Issues [CONDITIONAL]

Canonical home of `ISS-*`, `DRIFT-*`, `CONFLICT-*`.

Each entry records type, status, affected scope, owner, evidence, blocking semantics, and resolution/next action.

## 09 — Handoff

Required sections:

```text
Handoff From / To
Previous Handoff
Trigger
Current Phase/State
Completed Work
Pending Work
Formal Drafts / WIP
Active ACT / ISS / DRIFT / CONFLICT
Required Read Order
Authority References
authority_transfer: false
Freshness Warnings
Exact Next Action
```

Lifecycle: `DRAFT → OFFERED → ACKNOWLEDGED → ACCEPTED → SUPERSEDED`.

## 10 — Change Log

Canonical home of logical append-only `CHG-*` history.

Each substantive change records:

```text
CHG-ID
Timestamp
Actor / Instance
Object / Document
Previous State
New State
Reason / Trigger
Related User Instruction / DEC / EVD
```

Do not rewrite historical CHG entries to change history.

## 11 — Actor Registry

Canonical home of `ACTOR-*` and `INST-*`.

Record actor type, display name, platform, role, status, and instance relation. Role is descriptive only; authority is in `12`.

## 12 — Authorization Registry

Canonical home of `AUTH-*` and `DEL-*`.

`AUTH-*` must record grantor, grantee, actions, scope/paths, forbidden actions/effects, risk ceiling, start, expiry/termination, and status.

`DEL-*` must reference parent authorization and never exceed parent scope/risk/actions/duration.

## 13 — Evidence Registry

Canonical home of `EVD-*`.

Record:

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

Track active documents, continuation-relevant formal drafts, registered evidence, pinned schema/validation assets, required generated assets, and every active/current canonical Detail Document required to interpret referenced current Stable IDs. The Current Reconstructable Snapshot must resolve current authoritative semantics without requiring archived revisions.

Required continuation metadata also includes **Framework Source Provenance**:

```text
Framework Source Provenance
- Repository
- Release Tag / Mutable Ref State
- Resolved Commit SHA when observed
- Framework Version
- Schema Version
- Captured At
- Provenance Verification State
```

The Manifest must preserve the same observed provenance as active `00-Project Source Framework`. If `00` lacks verified immutable provenance, `14` must preserve that degraded/unknown state rather than inventing values. A mismatch between `00` and `14` is integrity drift.

Manifest does not recursively hash its own raw bytes.

## 15 — Action Registry

Canonical home of `ACT-*`.

Lifecycle:

```text
TODO → IN_PROGRESS → DONE
side states: BLOCKED / CANCELLED
```

Each action must have an exact, executable next step rather than vague wording.

## 16 — Migration Registry

Canonical home of `MIG-*`.

Record source/target versions or structure, compatibility assessment, affected docs/objects, steps, reversibility/rollback, approval, validation, evidence, and lifecycle.

## 17 — Secret Reference Registry

Canonical home of `SECRET-*` metadata only.

Each entry records:

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
