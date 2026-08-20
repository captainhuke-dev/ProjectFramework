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
project_source_framework_version: "1.1.4"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 00 — Project Source Framework

> **Starter pointer:** Instantiate the full root document from `../00-project-source-framework.md`. This mockup file exists to make slot `00` concrete and must not replace the authoritative full Framework template.

## Bootstrap Requirement

Create this document first as active `FRAMEWORK-001`; descendants inherit from it. For a NEW Project, read `../../FRAMEWORK-RELEASE.yaml`, resolve the declared stable release tag, and record only the provenance actually observed from the source used.

## Framework Source Provenance

```yaml
framework_source_provenance:
  repository: "captainhuke-dev/ProjectFramework"
  release_tag: "<RESOLVED_RELEASE_TAG_OR_MUTABLE_REF_STATE>"
  resolved_commit_sha: "<OBSERVED_40_HEX_SHA_OR_VERIFICATION_REQUIRED>"
  framework_version: "1.1.4"
  schema_version: "1.0.0"
  captured_at: "<ISO8601_WITH_TIMEZONE>"
```

Do not invent a tag or SHA. If immutable resolution is unavailable and mutable-source bootstrap is explicitly approved, keep the provenance visibly degraded / `VERIFICATION_REQUIRED`.
