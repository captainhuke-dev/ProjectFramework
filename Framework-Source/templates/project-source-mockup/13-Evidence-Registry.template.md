---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<EVIDENCE_REGISTRY_DOCUMENT_ID>"
document_type: "EVIDENCE_REGISTRY"
semantic_slot: "13"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "<CLASS>"
project_source_framework_version: "1.9.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 13 — Evidence Registry

Canonical home of `EVD-*`.

## EVD-<NNN> — <TITLE>
- **Evidence Type:** <TYPE>
- **Captured At:** <ISO8601>
- **Captured By Actor / Instance:** <ACTOR / INST REFS>
- **Source Reference:** <SOURCE>
- **Artifact Path:** <PATH>
- **Artifact Hash:** <HASH>
- **Supports:** <STABLE_ID_REFS>
- **Epistemic Status:** <STATUS>

Never store actual secrets as evidence.

### Optional `[Meeting]` Advisory Evidence (`EVD-*`)

Material use of a council result may specialize an existing `EVD-*` with:

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

Exploratory Meetings may remain transient; do not create synthetic evidence merely because `[Meeting]` was invoked. Provider `data/conversations/*.json` remains provider-local state, never canonical Project history. No `MEETING-*` family is introduced.

### Optional External-AI Disclosure Evidence (`EVD-*`)

```text
Evidence Type: EXTERNAL_AI_DISCLOSURE / ADVISORY_CONTEXT
Consumer / Workflow
Purpose
Provider / Tool
Provider Eligibility State / Evidence
Source Pointers / Bounded Context Scope
Disclosure Classes
Authorization Basis
Minimization / Redaction Performed
Blocked / Omitted Portions when material
Result / Artifact Pointer
Epistemic Status
```

Persist only the minimum reconstructable boundary evidence. Never duplicate full sensitive payload merely for audit or evidence convenience.
