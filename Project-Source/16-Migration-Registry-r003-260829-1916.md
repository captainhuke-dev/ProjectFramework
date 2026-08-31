---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "MIGRATION-REGISTRY-001"
document_type: "MIGRATION_REGISTRY"
semantic_slot: "16"
revision: 3
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-08-29T19:16:56+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.7.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 16 — Migration Registry

Canonical home of `MIG-*`.

## MIG-001 — Canonical Framework distribution-root rename

- **Status:** COMPLETED
- **Source Version / Structure:** reusable upstream Framework `1.7.0` distribution at `managing-project-source/`; ProjectFramework local Project Source pin `1.7.0`
- **Target Version / Structure:** reusable upstream Framework `1.8.0` distribution at `Framework-Source/`; ProjectFramework local Project Source pin intentionally remains `1.7.0`
- **Compatibility Assessment:** backward-compatible upstream repository/distribution-path migration; no Project Source schema/Stable-ID/slot change; external consumers with hard-coded old deep paths require explicit update; no live old-root alias
- **Upgrade Strategy:** NOT_APPLICABLE_TO_LOCAL_PROJECT_PIN — this is repository structural migration, not a `[Project Upgrade]` of ProjectFramework's active Framework pin
- **Upgrade Path Class:** ASSESSED_PATH
- **Cumulative Target Delta:** SATISFIED for current upstream distribution/routing; NOT_APPLICABLE to ProjectFramework local Framework pin
- **Preservation Mapping:** Project identity, Project Location Binding, Project Source Framework pin 1.7.0, Stable IDs, Project-specific/current truth, historical amendments/specs/plans/evidence, capture-time old-path evidence, `PROJECT-BOOTSTRAP.md → Project-Source/` authority routing
- **Affected Documents / Objects:** reusable Framework distribution tree, current README/Core/SKILL/release/starter/launcher routing, Project Source slots `00/01/02/03/09/10/13/14/15/16`, `ACT-002`, `CHG-003`, `CHG-004`, `EVD-003`, `EVD-004`
- **Steps:** define scenarios/baselines → rename tree → update current Framework 1.8.0 identity/routing → propagate starters/launchers → reconcile Project Source current truth → AFFECTED 74/74 PASS → RELEASE_FULL 198/198 PASS → commit completion evidence
- **Reversibility / Rollback:** Git history before TASK-038 and checkpoint commits preserve the old tree/path; rollback requires governed history-safe reversal to the pre-migration commit state and revalidation of current routing/Project Source
- **Approval:** ACTOR-001 user explicitly selected `Framework-Source/` vs `Project-Source/` naming and authorized continuous development on 2026-08-29; higher-level tool/platform gates and push separation remain binding
- **Validation:** AFFECTED `74/74 PASS`; final unchanged-candidate `RELEASE_FULL 198/198 PASS` on candidate `d068914e5fdc12eb9055ff5bae28cf57962495b4` / tree `f6c6bba9113308d60354112245f4d7574a350191`
- **Evidence:** `EVD-003`, `EVD-004`; release evidence `docs/superpowers/evidence/2026-08-29-task-038-framework-source-rename-release-full.md`; release evidence commit `3c053be7b754b02855657168aced89223af30e88`
- **Publication State:** NOT_PUSHED
