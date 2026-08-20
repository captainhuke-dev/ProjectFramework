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
epistemic_status: "<STATUS>"
freshness_class: "<CLASS>"
project_source_framework_version: "1.1.5"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 00 — Project Source Framework

> **Starter pointer:** Instantiate the full root document from `../00-project-source-framework.md`. This mockup file exists to make slot `00` concrete and must not replace the authoritative full Framework template.

## Bootstrap Requirement

Create this document first as active `FRAMEWORK-001`; descendants inherit from it. For a NEW Project, bootstrap from canonical repository `main` according to `../../FRAMEWORK-RELEASE.yaml` and the current Framework read order. Exact Git tag/SHA provenance is optional assurance, not a prerequisite.

## Framework Source Provenance — Optional Assurance

When exact provenance is actually observed and useful, it may be recorded as:

```yaml
framework_source_provenance:
  repository: "captainhuke-dev/ProjectFramework"
  source_ref: "<OBSERVED_REF_OR_MAIN>"
  release_tag: "<OPTIONAL_OBSERVED_TAG_OR_NONE>"
  resolved_commit_sha: "<OPTIONAL_OBSERVED_SHA_OR_UNKNOWN>"
  framework_version: "1.1.5"
  schema_version: "1.0.0"
  captured_at: "<ISO8601_WITH_TIMEZONE>"
  provenance_status: "<VERIFIED | PARTIAL | UNVERIFIED>"
```

Do not invent a tag or SHA. If exact Git provenance is unavailable, normal bootstrap may still proceed from the accessible canonical Framework source; represent provenance as unknown/unverified only when that state is material.
