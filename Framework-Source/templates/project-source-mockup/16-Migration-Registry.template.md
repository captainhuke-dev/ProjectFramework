---
project_uuid: "<PROJECT_UUID>"
project_id: "<PROJECT_ID>"
project_name: "<PROJECT_NAME>"
document_id: "<MIGRATION_REGISTRY_DOCUMENT_ID>"
document_type: "MIGRATION_REGISTRY"
semantic_slot: "16"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "<ISO8601_WITH_TIMEZONE>"
updated_at: "<ISO8601_WITH_TIMEZONE>"
created_by: "<ACTOR_ID>"
created_by_instance: "<INSTANCE_ID>"
epistemic_status: "<STATUS>"
freshness_class: "<CLASS>"
project_source_framework_version: "1.13.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 16 — Migration Registry

Brownfield adoption of Framework `1.7.0` root `PROJECT-BOOTSTRAP.md` is governed upgrade/migration work. Preserve prior Project truth/bindings/history and record material adoption through `MIG-*`; never auto-create the root file merely because upstream advanced.

Canonical home of `MIG-*`.

## MIG-<NNN> — <TITLE>
- **Status:** <STATUS>
- **Source Version / Structure:** <SOURCE>
- **Target Version / Structure:** <TARGET>
- **Compatibility Assessment:** <CONTENT>
- **Upgrade Strategy:** <DIRECT_TO_LATEST_CUMULATIVE | SEPARATELY_GOVERNED_LEGACY_CASE>
- **Upgrade Path Class:** <FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED>
- **Cumulative Target Delta:** <ALREADY_SATISFIED / REQUIRED / NOT_APPLICABLE / VERIFICATION_REQUIRED / CONFLICT_REVIEW assessment>
- **Preservation Mapping:** <STABLE_IDS / PROJECT_SPECIFIC_RULES / BINDINGS / CURRENT_TRUTH / HISTORY refs>
- **Affected Documents / Objects:** <REFS>
- **Steps:** <CURRENT_TO_TARGET_REQUIRED_STEPS_ONLY>
- **Reversibility / Rollback:** <CONTENT>
- **Approval:** <AUTHORITY / USER_APPROVAL>
- **Validation:** <AFFECTED_VERIFICATION + FINAL_UNCHANGED_CANDIDATE_RELEASE_FULL_AS_APPLICABLE>
- **Evidence:** <EVD_REFS>

## Framework 1.6.0 custom-slot-92 collision safety

If Brownfield slot `92` already contains a custom document, never overwrite it. Route through `MIG-*`; preserve custom identity/history/references/current semantics; relocate only with governed approval to a suitable free `93–99` or other semantically correct slot; activate standard `92 Project Graph` only after collision resolution. Do not invent `REL-*`, reciprocal assertions, relation applicability, or OpenViking configuration during migration.
