---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<PROJECT_SOURCE_MANIFEST_DOCUMENT_ID>"
document_type: "PROJECT_SOURCE_MANIFEST"
semantic_slot: "14"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "<CLASS>"
project_source_framework_version: "1.12.1"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 14 — Project Source Manifest

For Framework `1.7.0+` GREENFIELD Projects, `<Project-Root>/PROJECT-BOOTSTRAP.md` is a required external bootstrap artifact outside the semantic-slot manifest. Do not assign it a fake `DOC-*`/slot identity; verify its pointer to active Project Source separately.

Current Reconstructable Snapshot inventory.

```text
Active Documents
Continuation-Relevant Formal Drafts
Registered Evidence
Pinned Schema / Validation Assets
Required Generated Assets
Required Active Detail Documents
Active 40 / 60 / 91 / 92 when required to interpret current truth
```

## Framework Source Provenance — When Tracked

```text
Repository
Source Ref
Optional Release Tag when observed
Optional Resolved Commit SHA when observed
Framework Version: 1.2.3
Schema Version: 1.0.0
Captured At
Provenance Status: VERIFIED / PARTIAL / UNVERIFIED
```

Never invent missing exact provenance. Manifest does not recursively hash its own raw bytes.
