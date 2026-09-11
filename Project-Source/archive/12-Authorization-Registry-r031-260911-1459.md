---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "AUTHORIZATION-REGISTRY-001"
document_type: "AUTHORIZATION_REGISTRY"
semantic_slot: "12"
revision: 31
document_status: "ACTIVE"
supersedes: "12-Authorization-Registry-r030-260910-2220.md"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-29T17:07:00+07:00"
updated_at: "2026-09-11T14:59:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-001"
epistemic_status: "USER_CONFIRMED"
freshness_class: "STABLE"
project_source_framework_version: "1.15.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---
# 12 — Authorization Registry

Canonical home of current `AUTH-* / DEL-*` semantics. Historical AUTH records through `AUTH-013` remain preserved in `archive/12-Authorization-Registry-r030-260910-2220.md` and Git history; they are terminal history and grant no current authority.

## AUTH-014 — Framework 1.15 publication and Project upgrade authority

- **Authority Type:** USER_EXPLICIT_PERSISTENT_GOAL_AUTHORIZATION + USER_EXPLICIT_POST_PREVIEW_ROOT_MUTATION_APPROVAL
- **Granted By:** ACTOR-001
- **Initial Goal Authority Granted At:** 2026-09-10T22:20:10+07:00
- **Post-Preview Root/Project Source Mutation Approval:** 2026-09-11T14:59:00+07:00
- **Parent Outcome:** `OUT-014`
- **Purpose / Outcome:** publish the verified Framework 1.15 lineage to canonical `main`/`origin/main`, then upgrade ProjectFramework's initialized Project Source from Framework pin 1.7.0 to 1.15.0 through the governed Direct-to-Latest flow.
- **Authorized Scope Completed:** exact canonical Framework 1.15 publication reconciliation; read-only upgrade comparison/Preview; post-Preview Root/Project Source mutation for the approved `ASSESSED_PATH`; successor promotion/archive of affected Project Source revisions; root bootstrap repair; migration/evidence/change/lifecycle persistence; risk-appropriate resulting-state verification; history-preserving canonical promotion.
- **Explicitly Excluded / Not Granted:** force push; destructive history rewrite; branch deletion; Project Location Binding change; Git-native/MCP execution-architecture migration; AI-ControlTower/V2 cutover; external disclosure; secret-value persistence; unrelated Tasks; application/runtime/CLI/CI-CD implementation.
- **Status:** TERMINATED after `OUT-014` terminal success criteria are satisfied and the terminal upgrade commit is freshly observed on canonical `main`.
- **Validity:** no future action may rely on `AUTH-014` after terminal canonical observation; the authorization record remains historical evidence of the approved upgrade.
- **Verification Requirement:** `EVD-087` plus fresh canonical terminal-commit observation; `ACT DONE ≠ OUT ACHIEVED` remains binding until all outcome criteria are observed.
- **Evidence:** `EVD-086`, `EVD-087`, `MIG-002`, `CHG-087`.

No `DEL-*` record is created. This authorization does not transfer through Handoff (`authority_transfer: false`).
