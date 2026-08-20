---
project_uuid: "12000000-0000-4000-8000-000000000001"
project_id: "GOLDEN-SW-001"
project_name: "HarborDesk Reference Service"
document_id: "MANIFEST-001"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-20T11:45:00+07:00"
updated_at: "2026-08-20T11:45:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-GOLDEN-001"
epistemic_status: "VERIFIED"
freshness_class: "CHANGEABLE"
project_source_framework_version: "1.2.0"
project_source_schema_version: "1.0.0"
synthetic_reference: true
---

# 14 — Project Source Manifest

> **Synthetic Golden Reference Manifest:** This inventory demonstrates Current Reconstructable Snapshot semantics. It does not claim runtime verification or invent content hashes that were not independently computed.

## Snapshot Identity

```text
Project UUID: 12000000-0000-4000-8000-000000000001
Project ID: GOLDEN-SW-001
Framework: 1.2.0
Schema: 1.0.0
Snapshot Time: 2026-08-20T11:45:00+07:00
Profile Semantics: CURRENT
Archive Required For Current Truth: false
Actual Secret Values Present: false
Executable HarborDesk Runtime Artifacts Present: false
```

## Content-Identity Policy for This Synthetic Reference

The repository provides Git blob identities for committed files. This synthetic Manifest does **not** label Git blob SHA-1 identities as SHA-256 and does not fabricate a separate SHA-256 value.

For the rows below:

```text
Git Blob Identity: AVAILABLE_FROM_REPOSITORY_TREE
SHA-256 State: UNVERIFIED_NOT_COMPUTED_IN_SYNTHETIC_MANIFEST
```

`14-Project Source Manifest` does not recursively hash its own raw bytes.

## Active Document Inventory

| Slot | Active document | Revision | Applicability | Content identity state |
|---|---|---:|---|---|
| 00 | `00-Project Source Framework-r001-260820-1145.md` | 1 | MANDATORY ROOT | Git blob available; SHA-256 not asserted |
| 01 | `01-Project Source Index-r001-260820-1145.md` | 1 | MANDATORY | Git blob available; SHA-256 not asserted |
| 02 | `02-Project Overview-r001-260820-1145.md` | 1 | MANDATORY | Git blob available; SHA-256 not asserted |
| 03 | `03-Current State-r001-260820-1145.md` | 1 | MANDATORY | Git blob available; SHA-256 not asserted |
| 04 | `04-Decision Log-r001-260820-1145.md` | 1 | MANDATORY | Git blob available; SHA-256 not asserted |
| 05 | `05-Requirements-r001-260820-1145.md` | 1 | MANDATORY | Git blob available; SHA-256 not asserted |
| 06 | `06-Architecture-r001-260820-1145.md` | 1 | CONDITIONAL / APPLICABLE IN REFERENCE | Git blob available; SHA-256 not asserted |
| 07 | `07-Implementation Plan-r001-260820-1145.md` | 1 | CONDITIONAL / APPLICABLE IN REFERENCE | Git blob available; SHA-256 not asserted |
| 08 | `08-Open Issues-r001-260820-1145.md` | 1 | CONDITIONAL / APPLICABLE IN REFERENCE | Git blob available; SHA-256 not asserted |
| 09 | `09-Handoff-r001-260820-1145.md` | 1 | MANDATORY | Git blob available; SHA-256 not asserted |
| 10 | `10-Change Log-r001-260820-1145.md` | 1 | MANDATORY | Git blob available; SHA-256 not asserted |
| 11 | `11-Actor Registry-r001-260820-1145.md` | 1 | MANDATORY | Git blob available; SHA-256 not asserted |
| 12 | `12-Authorization Registry-r001-260820-1145.md` | 1 | MANDATORY | Git blob available; SHA-256 not asserted |
| 13 | `13-Evidence Registry-r001-260820-1145.md` | 1 | MANDATORY | Git blob available; SHA-256 not asserted |
| 14 | `14-Project Source Manifest-r001-260820-1145.md` | 1 | MANDATORY | Self inventory only; no recursive raw-byte hash |
| 15 | `15-Action Registry-r001-260820-1145.md` | 1 | MANDATORY | Git blob available; SHA-256 not asserted |
| 16 | `16-Migration Registry-r001-260820-1145.md` | 1 | MANDATORY | Git blob available; SHA-256 not asserted |
| 17 | `17-Secret Reference Registry-r001-260820-1145.md` | 1 | MANDATORY | Git blob available; SHA-256 not asserted |
| 40 | `40-Technical Design-r001-260820-1145.md` | 1 | CONDITIONAL / APPLICABLE IN REFERENCE | Git blob available; SHA-256 not asserted |
| 60 | `60-Deployment Plan-r001-260820-1145.md` | 1 | CONDITIONAL / APPLICABLE IN REFERENCE | Git blob available; SHA-256 not asserted |
| 91 | `91-Project Management Control-r001-260820-1145.md` | 1 | CONDITIONAL / APPLICABLE IN REFERENCE | Git blob available; SHA-256 not asserted |

No `18` or `19` active document exists. No archive or formal draft is required to interpret the current snapshot.

## Current Stable-ID Resolution Map

| Stable ID | Canonical current home | Current state / meaning |
|---|---|---|
| FRAMEWORK-001 | 00 | ACTIVE Root Governance |
| DEC-001 | 04 | APPROVED — PostgreSQL 16 primary datastore |
| DEC-002 | 04 | APPROVED — SOURCE_AND_DOCKER blueprint |
| REQ-001 | 05 | ACTIVE — operator-verifiable health-signal requirement |
| REQ-002 | 05 | ACTIVE — Source/Docker parity/variance requirement |
| REQ-003 | 05 | ACTIVE — persistence across expected restart requirement |
| ISS-001 | 08 | OPEN / KNOWLEDGE_DEBT — rollback procedure revalidation |
| CHG-001 | 10 | Synthetic Framework 1.2.0 reference composition history |
| ACTOR-001 | 11 | ACTIVE Project Owner reference |
| ACTOR-002 | 11 | ACTIVE Technical Lead reference |
| ACTOR-003 | 11 | ACTIVE Operator reference |
| INST-GOLDEN-001 | 11 | CLOSED_AFTER_SNAPSHOT synthetic authoring instance |
| AUTH-001 | 12 | ACTIVE R1 documentation/reference maintenance authority only |
| EVD-001 | 13 | VERIFIED_AS_DOCUMENTATION_REVIEW_ONLY |
| ACT-001 | 15 | IN_PROGRESS documentation evidence review |
| MIG-001 | 16 | ASSESSMENT_COMPLETE_SYNTHETIC_EXAMPLE / NO_COLLISION_IN_SYNTHETIC_REFERENCE |
| SECRET-001 | 17 | SYNTHETIC_REFERENCE_ONLY / `secret_value_present: false` |
| RISK-001 | 91 | OPEN / MONITORING |
| ASM-001 | 91 | UNVERIFIED |
| MS-001 | 91 | IN_PROGRESS |
| OUT-001 | 91 | TARGETED |
| DEP-001 | 91 | WAITING |
| CR-001 | 91 | CLOSED — documentation-blueprint change only |
| GATE-001 | 91 | READY_FOR_REVIEW |

The Deployment Mode Variance in `40` is a local technical sub-record, not a new Framework Stable-ID type.

## Cross-Reference Verification

Current references resolve without archive traversal:

```text
03 → ACT-001 / ISS-001 / RISK-001 / ASM-001 / MS-001 / OUT-001 / DEP-001 / GATE-001
04 → REQ / RISK / DEP / CR / GATE / EVD current homes
05 → DEC / ACT / RISK / DEP / CR / GATE current homes
07 → ACT / MS / OUT / DEP / RISK / CR / GATE / EVD current homes
08 → DEC-002 / REQ-002 / CR-001 / EVD-001 / GATE-001
09 → AUTH-001 and active management controls
11 → MS-001 / GATE-001 / ISS-001 plus ACTOR records
12 → ACTOR-001 / ACTOR-002
13 → REQ-001 / REQ-002 / REQ-003 / ACT-001 / GATE-001
15 → REQ / ISS / MS / OUT / GATE / EVD
16 → Framework version migration semantics and EVD-001
17 → AUTH-001 only; no secret value
40 → DEC / REQ / RISK / ASM / DEP / CR / EVD / SECRET current homes
60 → DEC / REQ / RISK / DEP / CR / GATE / ISS / EVD / SECRET current homes
91 → DEC / REQ / ACT / ISS / ACTOR / AUTH / EVD / CHG current homes
```

No archived revision is required to determine current meaning of any listed current Stable ID.

## Framework Source Provenance — Optional Assurance

This matches active `00`:

```yaml
repository: "captainhuke-dev/ProjectFramework"
source_ref: "main"
release_tag: null
resolved_commit_sha: null
framework_version: "1.2.0"
schema_version: "1.0.0"
captured_at: "2026-08-20T11:45:00+07:00"
provenance_status: "UNVERIFIED"
```

The missing optional exact tag/SHA is explicit and is not a readiness defect for this synthetic documentation example.

## Readiness / Evidence Boundary

This snapshot is structurally useful as a **Golden Reference composition example**, but its fictional HarborDesk runtime is not deployed or verified. `EVD-001` is documentation-review evidence only; `GATE-001` remains `READY_FOR_REVIEW`; `ISS-001` remains open; `ASM-001` remains unverified.

Therefore this Manifest does not claim HarborDesk runtime readiness, Docker functionality, database availability, or production deployment.
