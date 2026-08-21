---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "FRAMEWORK-001"
document_type: "PROJECT_SOURCE_FRAMEWORK"
semantic_slot: "00"
revision: 1
document_status: "ACTIVE"
framework_root: true
inherits_from: []
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "USER_CONFIRMED"
freshness_class: "STABLE"
project_source_framework_version: "1.2.1"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 00 — Project Source Framework

> **Starter pointer:** Instantiate the full root document from `../00-project-source-framework.md`. This mockup file makes slot `00` concrete and does not replace the authoritative full Framework template.

## Bootstrap Requirement

Create this document first as active `FRAMEWORK-001`; descendants inherit from it. NEW Projects bootstrap from canonical repository `main`, then create mandatory `01–05` and `09–17`; evaluate conditional `06–08`, `40`, `60`, `91`; keep `18–19` reserved.

## Framework 1.2.0 Extended Semantics

```text
40 Technical Design               CONDITIONAL
60 Deployment Plan                CONDITIONAL
91 Project Management Control     CONDITIONAL / STANDARD IN 1.2.0+
92–99 Project-specific / Governance Extension
```

`91` canonically owns `RISK-* / ASM-* / MS-* / OUT-* / DEP-* / CR-* / GATE-*`. Technical planning remains documentation/blueprint scope and does not authorize source code, Dockerfile/Compose, scripts, CI, or automation.

## Externalized Working Memory / Chat Lifecycle Pointer

The full root template `../00-project-source-framework.md` carries the binding `Externalized Working Memory and Chat Lifecycle` contract, including Material vs Transient connector activity, Logical Checkpoint persistence, `PERSISTENCE_PENDING`, and `CONTINUE_CURRENT_CHAT | START_NEW_CHAT`. Keep those semantics in the full root template; do not duplicate or weaken the normative contract in this starter.

## Framework Source Provenance — Optional Assurance

```yaml
framework_source_provenance:
  repository: "captainhuke-dev/ProjectFramework"
  source_ref: "<OBSERVED_REF_OR_MAIN>"
  release_tag: "<OPTIONAL_OBSERVED_TAG_OR_NONE>"
  resolved_commit_sha: "<OPTIONAL_OBSERVED_SHA_OR_UNKNOWN>"
  framework_version: "1.2.1"
  schema_version: "1.0.0"
  captured_at: "<ISO8601_WITH_TIMEZONE>"
  provenance_status: "<VERIFIED | PARTIAL | UNVERIFIED>"
```

Never invent exact Git identity. Absence of optional exact provenance does not by itself block normal Framework use.
