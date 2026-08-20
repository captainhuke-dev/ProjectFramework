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
project_source_framework_version: "1.1.5"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 14 — Project Source Manifest

Current Reconstructable Snapshot inventory.

## Active Documents
<PATHS_HASHES_REVISIONS>

## Continuation-Relevant Formal Drafts
<ENTRIES_OR_NONE>

## Registered Evidence
<EVD_REFS>

## Pinned Schema / Validation Assets
<ENTRIES>

## Required Generated Assets
<ENTRIES_OR_NONE>

## Required Active Detail Documents
<DETAIL_DOCS_REQUIRED_TO_INTERPRET_CURRENT_STABLE_IDS>

## Framework Source Provenance — When Tracked

```text
Repository: <MATCH_ACTIVE_00>
Source Ref: <MATCH_ACTIVE_00>
Optional Release Tag when observed: <MATCH_ACTIVE_00_OR_NONE>
Optional Resolved Commit SHA when observed: <MATCH_ACTIVE_00_OR_UNKNOWN>
Framework Version: 1.1.5
Schema Version: 1.0.0
Captured At: <MATCH_ACTIVE_00_OR_NONE>
Provenance Status: <VERIFIED | PARTIAL | UNVERIFIED>
```

When provenance is tracked, the Manifest preserves the state actually recorded in active `00-Project Source Framework`. It MUST NOT invent missing tag/SHA values to appear complete. A mismatch between tracked values in `00` and `14` is integrity drift requiring root-cause resolution. Missing optional exact Git provenance is not by itself an integrity/readiness defect.

The snapshot must resolve current authoritative semantics without archived revisions. The Manifest does not recursively hash its own raw bytes.
