---
project_uuid: "12000000-0000-4000-8000-000000000001"
project_id: "GOLDEN-SW-001"
project_name: "HarborDesk Reference Service"
document_id: "PMCTRL-001"
document_type: "PROJECT_MANAGEMENT_CONTROL"
semantic_slot: "91"
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

# 91 — Project Management Control

> **Synthetic / Current canonical management state:** This file demonstrates all Framework `1.2.0` management-control object types. It does not describe a real deployed service.

## RISK-001 — Persistent-Volume Misconfiguration May Cause Data Loss

- **Risk Statement:** If durable PostgreSQL storage is configured incorrectly in a future deployment, data may be lost across restart/removal operations.
- **Category:** DATA / DEPLOYMENT
- **Probability:** MEDIUM (synthetic assessment)
- **Impact:** HIGH (synthetic assessment)
- **Trigger / Early Warning:** Persistence path/volume responsibility differs from documented contract or restart verification fails.
- **Mitigation:** Keep persistence responsibility explicit in `40/60`; require resulting-state verification in a real implementation.
- **Contingency:** Stop affected mutation, protect available data, restore from verified real backup if one exists, open an Issue when materialized.
- **Owner:** ACTOR-002
- **Review Trigger / By:** TIME_BASED every 14 days and EVENT_BASED on persistence/deployment change
- **Status:** OPEN
- **Handling State:** MONITORING
- **Related:** DEC-001, REQ-003, DEP-001, CR-001, GATE-001
- **Materialized Issue:** NONE — this is future uncertainty; no data-loss event is claimed.

## ASM-001 — Target Host Supports Declared Container / Runtime Architecture

- **Statement:** A future target host supports 64-bit Linux, Python 3.12 for Source mode, and Docker Engine 26+ for Docker mode.
- **Basis:** Synthetic design constraint; no target host was inspected.
- **Why It Matters:** Deployment support depends on compatible runtime/architecture.
- **Impact If False:** Technical Design/Deployment Plan and possibly DEC-002 require reassessment.
- **Verification Method:** Inspect real target host/platform/runtime before real deployment.
- **Verification Owner:** ACTOR-002
- **Review Trigger / By:** EVENT_BASED before real deployment or when target environment changes
- **Status:** UNVERIFIED
- **Evidence:** NONE — EVD-001 does not verify a host.
- **Related:** DEC-002, REQ-002, MS-001, GATE-001

## MS-001 — Deployment Ready

- **Milestone:** Deployment documentation/readiness criteria are sufficiently reviewed to hand to a qualified operator without guessing.
- **Success / Exit Criteria:** GATE-001 PASSED; ISS-001 resolved or explicitly accepted through governed authority; required assumptions/dependencies appropriately verified or explicitly bounded; evidence remains documentation-scoped in this synthetic reference.
- **Target Window / Trigger:** EVENT_BASED after ACT-001 evidence review
- **Owner:** ACTOR-002
- **Status:** IN_PROGRESS
- **Dependencies:** DEP-001 for real deployment applicability; GATE-001 for this reference readiness
- **Required Evidence:** EVD-001 plus gate findings; real runtime evidence would be separate in a real Project
- **Related:** REQ-001, REQ-002, REQ-003, ACT-001, RISK-001, ASM-001, DEP-001, GATE-001
- **Reached At:** NONE

## OUT-001 — Qualified Operator Can Follow Either Supported Installation Blueprint Without Guessing

- **Outcome Statement:** Documentation provides a clear Source and Docker operational blueprint with explicit unknowns and no fabricated implementation details.
- **Success Measure / Evidence:** Qualified reviewer can trace prerequisites, configuration, secrets, persistence, verification, upgrade/rollback/backup responsibilities and declared variance from current Project Source.
- **Baseline:** No Framework `1.2.0` Golden Reference existed before this synthetic example.
- **Target:** Complete, internally consistent documentation blueprint; no claim of runtime execution.
- **Measurement Method:** Documentation review through EVD-001/GATE-001.
- **Owner:** ACTOR-001
- **Status:** TARGETED
- **Related:** MS-001, EVD-001, GATE-001
- **Last Evaluated:** 2026-08-20T11:45:00+07:00 — not yet marked ACHIEVED because GATE-001 is not PASSED.

## DEP-001 — PostgreSQL Service Availability

- **Dependency Type:** SYSTEM
- **Depends On:** PostgreSQL 16 service under a future real deployment environment
- **Required For:** REQ-003 and a future HarborDesk runtime
- **Owner:** ACTOR-002
- **Expected Availability / Trigger:** Before persistence-dependent runtime readiness
- **Current State:** No real service exists in this synthetic reference
- **Fallback / Workaround:** None invented; a real Project must define approved alternatives if needed
- **Failure Impact:** Blocks real persistence-dependent operation and may trigger Health degradation/Risk/Issue handling
- **Related:** DEC-001, REQ-003, RISK-001, MS-001, GATE-001
- **Status:** WAITING

## CR-001 — Add Docker as a Supported Deployment Mode

- **Requested Change:** Expand the synthetic deployment blueprint from Source-only conceptual support to `SOURCE_AND_DOCKER`.
- **Reason / Trigger:** Demonstrate Framework `1.2.0` dual-mode governance.
- **Requester:** ACTOR-001
- **Affected Scope:** DEC-002, REQ-002, `40`, `60`, persistence/secret/configuration responsibilities, Risk/Gate/readiness.
- **Impact Assessment:** Docker packaging adds container-runtime, service/volume/network responsibilities while preserving application/configuration/data/security semantics; database placement/persistence mechanics become explicit variance.
- **Affected REQ / DEC / Architecture / Technical / Deployment / MS / OUT / RISK / DEP:** REQ-002, REQ-003, DEC-002, `06`, `40`, `60`, MS-001, OUT-001, RISK-001, DEP-001
- **Authority / Approval Requirement:** ACTOR-001 synthetic design approval; no external/runtime authority granted
- **Decision:** APPROVED for documentation blueprint only
- **Implementation / Migration References:** DEC-002, CHG-001; no application/Docker runtime implementation
- **Verification Requirement:** EVD-001 documentation review and GATE-001
- **Status:** CLOSED
- **Closure Note:** The governed change was implemented **only as Project Source documentation/blueprint**, not as executable Docker support.

## GATE-001 — Deployment Readiness Review

- **Purpose:** Decide whether the synthetic documentation blueprint is ready as a Golden Reference composition example.
- **Affected Scope:** `40`, `60`, `91`, REQ-001/002/003, DEC-001/002, ISS-001, ACT-001
- **Entry Criteria:** Required documents present; canonical object homes materialized; Source/Docker parity/variance documented; evidence boundary explicit.
- **Exit / Pass Criteria:** Required conceptual sections consistent; `ISS-001` disposition documented; no fabricated runtime/secret claims; Stable IDs resolve current records; authority boundary intact.
- **Required Evidence:** EVD-001 plus direct current-document review
- **Related:** REQ-001, REQ-002, REQ-003, DEC-001, DEC-002, RISK-001, ASM-001, DEP-001, MS-001, CR-001, EVD-001
- **Review Owner:** ACTOR-002
- **Required Authority:** AUTH-001 is sufficient for documentation review only; no production authority involved
- **Status:** READY_FOR_REVIEW
- **Findings:** ISS-001 rollback knowledge debt remains open; ASM-001 unverified; these prevent an unsupported readiness claim.
- **Exceptions / Waiver:** NONE
- **Next Action:** ACT-001 completes documentation review and updates gate finding/disposition.
- **Reviewed At:** NOT_YET_DISPOSITIONED

## Cross-Object Rule Demonstration

```text
RISK-001 remains a Risk until a condition actually materializes; no ISS is created for hypothetical data loss.
ACT-001 completion will not automatically reach MS-001 or achieve OUT-001.
Responsibility rows in 11 do not extend AUTH-001.
CR-001 closure reflects documentation change only.
GATE-001 READY_FOR_REVIEW is not PASSED.
```
