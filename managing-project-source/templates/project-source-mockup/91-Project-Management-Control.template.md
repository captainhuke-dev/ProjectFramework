---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<PROJECT_MANAGEMENT_CONTROL_DOCUMENT_ID>"
document_type: "PROJECT_MANAGEMENT_CONTROL"
semantic_slot: "91"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "<CLASS>"
project_source_framework_version: "1.3.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 91 — Project Management Control

> **CONDITIONAL / STANDARD IN FRAMEWORK 1.2.0+:** Create when at least one management-control object is materially applicable.

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

## RISK-<NNN> — <TITLE>
Risk Statement; Category; Probability; Impact; Trigger/Early Warning; Mitigation; Contingency; Owner; Review Trigger/By; Status; Related IDs/Evidence; Materialized Issue when applicable.

Statuses may include `IDENTIFIED / OPEN / MITIGATING / MONITORING / ACCEPTED / MATERIALIZED / CLOSED / SUPERSEDED`.

## ASM-<NNN> — <TITLE>
Statement; Basis; Why It Matters; Impact If False; Verification Method/Owner; Review Trigger/By; Status; Evidence; Related IDs.

Statuses: `UNVERIFIED / VALIDATED / INVALIDATED / SUPERSEDED`.

## MS-<NNN> — <TITLE>
Milestone; Success/Exit Criteria; Target Window/Trigger; Owner; Status; Dependencies; Required Evidence; Related IDs; Reached At.

## OUT-<NNN> — <TITLE>
Outcome Statement; Success Measure/Evidence; Baseline; Target; Measurement Method; Owner; Status; Related IDs; Last Evaluated.

## DEP-<NNN> — <TITLE>
Dependency Type; Depends On; Required For; Owner; Expected Availability/Trigger; Current State; Fallback; Failure Impact; Related IDs; Status. `AVAILABLE ≠ SATISFIED`.

## CR-<NNN> — <TITLE>
Requested Change; Reason/Trigger; Requester; Affected Scope; Impact Assessment; affected REQ/DEC/Architecture/Technical/Deployment/MS/OUT/RISK/DEP; Authority/Approval; Decision; Implementation/Migration refs; Verification; Status.

## GATE-<NNN> — <TITLE>
Purpose; Affected Scope; Entry Criteria; Pass Criteria; Required Evidence; Related IDs; Review Owner; Required Authority; Status; Findings; Exception/Waiver; Next Action; Reviewed At.

`WAIVED` requires explicit rationale plus authority/Decision reference. `ACT DONE ≠ MS REACHED ≠ OUT ACHIEVED`.
