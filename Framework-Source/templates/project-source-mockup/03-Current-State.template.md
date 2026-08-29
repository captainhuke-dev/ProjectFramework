---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<CURRENT_STATE_DOCUMENT_ID>"
document_type: "CURRENT_STATE"
semantic_slot: "03"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "CHANGEABLE"
project_source_framework_version: "1.8.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 03 — Current State

Framework `1.7.0+` root `PROJECT-BOOTSTRAP.md` carries no current status. Current state remains here after `00 → 01 → 03` routing.

Pure snapshot of now. No historical timeline.

## Current State

```text
Lifecycle State: <STATE>
Execution State: <STATE>
Current Phase: <PHASE>
Current Scope: <SCOPE>
Current Owner / Actor: <ACTOR_REF>
Active ACT / ISS / DRIFT / CONFLICT: <REFS>
Active RISK / ASM / DEP / MS / OUT / CR / GATE: <REFS_OR_NONE>
Current Blockers: <BLOCKERS>
Exact Next Action: <NEXT_ACTION>
Last Verified: <ISO8601>
```

## Project Health

Use applicable dimensions with `GREEN / AMBER / RED / UNKNOWN`; omit non-applicable optional dimensions.

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

Each dimension records State, Reason, Supporting Stable IDs/Evidence, Owner, Last Reviewed, Next Review/Trigger.

## Review Cadence

Use `TIME_BASED` and/or `EVENT_BASED`; this does not create a scheduler.