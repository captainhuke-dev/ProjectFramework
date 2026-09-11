---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "MIGRATION-REGISTRY-001"
document_type: "MIGRATION_REGISTRY"
semantic_slot: "16"
revision: 4
document_status: "ACTIVE"
supersedes: "16-Migration-Registry-r003-260829-1916.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-11T14:59:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.15.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
# 16 — Migration Registry

Canonical home of current `MIG-*` semantics. Historical `MIG-001` remains preserved in `archive/16-Migration-Registry-r003-260829-1916.md` and Git history.

## MIG-002 — ProjectFramework Direct-to-Latest Framework 1.7.0 → 1.15.0

- **Status:** COMPLETED subject to fresh canonical observation of the promoted terminal commit; externally claimable only after that observation.
- **Adoption Mode:** BROWNFIELD / initialized Project
- **Source Version / Schema:** Framework `1.7.0` / Schema `1.0.0`
- **Target Version / Schema:** Framework `1.15.0` / Schema `1.0.0`
- **Target Release Format:** `3`
- **Target Distribution Root:** `Framework-Source/`
- **Target Framework-Source Tree:** `835c5a24c909ef7de2d413c46a6451746ed5fbf0`
- **Pre-upgrade Canonical Baseline:** `main@6e3dd6c987eacdbe8430dbd906c59f5678a07843`
- **Upgrade Strategy:** DIRECT_TO_LATEST_CUMULATIVE; intermediate release execution not required
- **Upgrade Path Class:** `ASSESSED_PATH`
- **Comparison Result:** `UPGRADE_AVAILABLE`
- **Compatibility Assessment:** bounded cumulative governance/documentation migration; Schema remains `1.0.0`; no 2.0 cutover, namespace break, application-runtime migration, or non-reconstructable current truth detected. Cumulative semantics include Framework 1.8 persistent Goal/Meeting/disclosure and distribution-root behavior; 1.9 portable bootstrap; 1.10 optional Project Knowledge; 1.12 execution/capability/release/trust plus finalization/strict-command hardening; 1.13 Project Audit/remediation governance; 1.14 federated change intelligence; 1.15 response-close/Next Goal semantics.
- **Project-Specific Assessment:** ProjectFramework contains no application runtime; this migration does not create runtime state. Optional `Project-Knowledge/`, `Project-Execution/`, `Project-Change-Feed/`, `06–08`, `40`, `60`, and `92` remain unmaterialized unless separately applicable/approved.
- **Bootstrap Assessment:** root `PROJECT-BOOTSTRAP.md` had stale hard-coded `01/03/09` revision pointers. The upgrade repairs the locator to point to active `00` only and resolve `01/03/09` through active routing.
- **Current-Truth/Stamp Assessment:** verification found active `02` still reporting Project pin `1.7.0` / upstream `1.8.0`, while `04/05/11/17` retained Framework `1.7.0` header stamps. The corrected target therefore promotes successors for all active mandatory slots plus active `91`; `02` repairs stale current version truth, while `04/05/11/17` preserve semantic payload and only reconcile the Framework stamp/current wording needed for coherent target pinning.
- **Preservation Mapping:** immutable `project_uuid`; `FRAMEWORK-001` Stable ID; existing canonical Stable-ID families; Project Location Binding values; Project-specific/current truth; source-native task/history; Git history; every superseded active Project Source predecessor archived under `Project-Source/archive/`; Framework-Source tree unchanged.
- **Affected Active Slots:** `00`, `01`, `02`, `03`, `04`, `05`, `09`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `91`.
- **Root Artifact:** `PROJECT-BOOTSTRAP.md` repaired in place as a locator artifact outside semantic slots.
- **Approval:** Upgrade preparation covered by `AUTH-014`; ACTOR-001 explicitly approved the post-Preview Root/Project Source mutation on 2026-09-11T14:59:00+07:00. The stamp/current-truth correction is required to realize the approved target pin coherently and does not add a new binding, optional surface, runtime, or execution-architecture scope.
- **Applied Steps:** fresh canonical baseline check → materialize 1.15 successors for all active Project Source documents → repair stale `02` current version truth → repair bootstrap locator → copy every affected predecessor to archive → remove superseded active predecessor paths → verify active routing/uniqueness/pin/bindings/unchanged Framework-Source → promote history-preserving terminal commit → fresh canonical observation.
- **Reversibility / Rollback:** preserve all predecessors and the pre-upgrade baseline in Git history; rollback is a separately governed history-preserving successor/revert to the pre-upgrade semantics. Force push/history rewrite and predecessor deletion are not part of the approved rollback.
- **Verification Plan / Result:** `EVD-087` records the exact corrected final successor blob set, archive preservation, affected checks, release-level resulting-state checks, and canonical post-promotion observation.
- **Related:** `OUT-014`, `AUTH-014`, `ACT-026`, `ENV-014`, `EVD-086`, `EVD-087`, `CHG-087`.

`MIG-002` does not authorize or perform the separate MCP → Git-native/GitHub-direct execution-architecture migration.
