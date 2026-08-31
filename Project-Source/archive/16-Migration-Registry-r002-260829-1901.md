---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "MIGRATION-REGISTRY-001"
document_type: "MIGRATION_REGISTRY"
semantic_slot: "16"
revision: 2
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-08-29T19:01:09+07:00"
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

- **Status:** IN_PROGRESS
- **Source Version / Structure:** reusable upstream Framework `1.7.0` distribution at `managing-project-source/`; ProjectFramework local Project Source pin `1.7.0`
- **Target Version / Structure:** reusable upstream Framework `1.8.0` distribution at `Framework-Source/`; ProjectFramework local Project Source pin intentionally remains `1.7.0`
- **Compatibility Assessment:** backward-compatible upstream repository/distribution-path migration; no Project Source schema/Stable-ID/slot change; external consumers with hard-coded old deep paths require explicit update; no live old-root alias
- **Upgrade Strategy:** NOT_APPLICABLE_TO_LOCAL_PROJECT_PIN — this is repository structural migration, not a `[Project Upgrade]` of ProjectFramework's active Framework pin
- **Upgrade Path Class:** ASSESSED_PATH
- **Cumulative Target Delta:** REQUIRED for current upstream distribution/routing; NOT_APPLICABLE to ProjectFramework local Framework pin
- **Preservation Mapping:** Project identity, Project Location Binding, Project Source Framework pin 1.7.0, Stable IDs, Project-specific/current truth, historical amendments/specs/plans/evidence, capture-time old-path evidence, `PROJECT-BOOTSTRAP.md → Project-Source/` authority routing
- **Affected Documents / Objects:** reusable Framework distribution tree, current README/Core/SKILL/release/starter/launcher routing, Project Source slots `00/01/02/03/09/10/13/14/15/16`, `ACT-002`, `CHG-003`, `EVD-003`
- **Steps:** define scenarios/baselines → rename tree → update current Framework 1.8.0 identity/routing → propagate starters/launchers → reconcile Project Source current truth → affected verification → final unchanged-candidate RELEASE_FULL → completion evidence
- **Reversibility / Rollback:** Git history before TASK-038 and checkpoint commits preserve the old tree/path; rollback requires governed history-safe reversal to the pre-migration commit state and revalidation of current routing/Project Source
- **Approval:** ACTOR-001 user explicitly selected `Framework-Source/` vs `Project-Source/` naming and authorized continuous development on 2026-08-29; higher-level tool/platform gates and push separation remain binding
- **Validation:** Task 2 structural PASS 13/13; Task 3 starter/launcher PASS; scenarios 181–188 affected verification PENDING; final unchanged-candidate RELEASE_FULL PENDING
- **Evidence:** `EVD-003`; checkpoint commits `80ac496`, `fb24141`, `5757660`
