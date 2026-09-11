---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "EVIDENCE-REGISTRY-001"
document_type: "EVIDENCE_REGISTRY"
semantic_slot: "13"
revision: 83
document_status: "ACTIVE"
supersedes: "13-Evidence-Registry-r082-260910-2220.md"
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
# 13 — Evidence Registry

Historical evidence through `EVD-085` remains preserved in `archive/13-Evidence-Registry-r082-260910-2220.md` and Git history. This active projection materializes the evidence required for current `MIG-002 / OUT-014` truth.

## EVD-086 — Framework 1.15 Project Upgrade comparison, Preview, and mutation approval

- **Evidence Type:** GOVERNED_UPGRADE_PREVIEW_AND_USER_APPROVAL
- **Observed / Approved At:** 2026-09-11T14:59:00+07:00
- **Actor:** ACTOR-001 explicit post-Preview approval; ACTOR-002 / INST-001 executor
- **Current Pin Observed:** Framework `1.7.0` / Schema `1.0.0` from active predecessor `FRAMEWORK-001`
- **Target Observed:** Framework `1.15.0` / Schema `1.0.0` / release format `3`
- **Canonical Publication Baseline:** `main@6e3dd6c987eacdbe8430dbd906c59f5678a07843`; parent `c21145e1efe56bdc03791249e11c8ba42b84f93b`
- **Target Framework-Source Tree:** `835c5a24c909ef7de2d413c46a6451746ed5fbf0`
- **Comparison Result:** `UPGRADE_AVAILABLE`
- **Path Class:** `ASSESSED_PATH`
- **Strategy:** Direct-to-Latest cumulative `1.7.0 → 1.15.0`; no mandatory intermediate release execution
- **Preview Scope Approved:** promote `FRAMEWORK-001` pin; reconcile OUT-014 publication truth; repair `PROJECT-BOOTSTRAP.md`; successor/promote/archive affected Project Source; preserve Stable IDs, identity, bindings, history and Framework-Source; no optional-surface synthesis; verification + rollback plan.
- **Mutation Approval:** user explicitly approved the exact Preview outcome on 2026-09-11; approval does not cover the separate MCP/Git-native architecture migration.
- **Rollback Basis:** pre-upgrade canonical baseline and archived predecessor revisions; no force/history rewrite.

## EVD-087 — ProjectFramework 1.15 corrected terminal candidate / resulting-state verification

- **Evidence Type:** STATE_BOUND_UPGRADE_VERIFICATION
- **Verification Scope:** approved `MIG-002` cumulative Project upgrade plus corrections required to make the active Project Source coherently pinned to Framework 1.15.0.
- **Pre-promotion Base:** canonical `main@6e3dd6c987eacdbe8430dbd906c59f5678a07843`.
- **Framework-Source Expected Unchanged Tree:** `835c5a24c909ef7de2d413c46a6451746ed5fbf0`.
- **Rejected Initial Candidate:** `3df92a407e1170e238d6b8c6171ac5492032b188` was created from the correct baseline but **NOT_PROMOTED**. Verification found active `02` still asserting Project pin `1.7.0` / upstream `1.8.0` and active `04/05/11/17` still carrying Framework `1.7.0` header stamps. Promotion was stopped before any branch/main ref update.
- **Corrected Successor Blob Set Prepared / Immutable:**
  - `PROJECT-BOOTSTRAP.md` → `3d878d2f4a22769ab0ce8a4d6ee4fee61057cc68`
  - `00 r003` → `ddefde7d763bd09c0adbf35d88b4390d48375570`
  - `01 r090` → `68856d29441c183b4ff0c2b2619fe874d2e8541d`
  - `02 r003` → `0d93bffe434c1a2442cda3a0eba5dd5a4ca27575`
  - `03 r086` → `a3f1d190e49830900e760ab95ae425ae194db86d`
  - `04 r002` → `d1fe7cad4bcc351069ca79a8d02dd007d6949d60`
  - `05 r002` → `0117e1d5ace27112f414ef3b7453fd0a5344780d`
  - `09 r086` → `e087a6efe82469c1838fa2747302f0d94063cc4f`
  - `10 r084` → `fbbe949f7041ca5c906948b13b27b82ff0a5b502`
  - `11 r002` → `03721861ffb0b86f7007a4f02fa2d5d524f0954a`
  - `12 r031` → `5f0828b298b701519650f3d8ce2f803a3bafd30d`
  - `14 r090` → `ae59aa93fba996e34bd585574228c045881a2043`
  - `15 r084` → `aeb51cdcb80c63feaf7617dc27e865887cfdc9a1`
  - `16 r004` → `88c79872cccd5385edc829b7c7e7730c6ff309ff`
  - `17 r002` → `e9bbca4a8a59140a75cb0e1ee2f39f6dfbde2998`
  - `91 r048` → `e7b9104903e851d5bdd15f1fce766420bc74c002`
  - `13 r083` → this active evidence revision; exact blob identity is established by Git object creation/final tree observation rather than self-referentially embedded here.
- **Predecessors Required in Archive:**
  - `00 r002` blob `88a6e8296fdbb1ec5b4a9fec7b9ee78eb366dd5d`
  - `01 r089` blob `6d1e0c9580d8168ef770f9dd54a537f8d07103d2`
  - `02 r002` blob `cfaf107aad2beedf9f3d9bcad23e12c7adbf1c86`
  - `03 r085` blob `006e95d2452a6eed95dfbf38a36208f3b269cb19`
  - `04 r001` blob `5eeb87f9e39b8864b51813f79ffb65d08ab3092a`
  - `05 r001` blob `7eaba01486c310b7b6cc415d92119cd3dd4f15d2`
  - `09 r085` blob `6da2d5dc7234a09c7958f2a3050a705232cc01e0`
  - `10 r083` blob `cf382977662c86715a970a96f7a6b205bf1f4c41`
  - `11 r001` blob `1343ca6dcdaa3afd7948676b42bbcc158f455909`
  - `12 r030` blob `c5fe5a49849cb434161189ef640817a2a4766cfd`
  - `13 r082` blob `dc3da38a3ded04e09c6a54a38068f34150bd9e4a`
  - `14 r089` blob `536965de8b22b140290fa161f7010091478886ae`
  - `15 r083` blob `3c5e5df878b3f6038328c9628eb9c9717303e560`
  - `16 r003` blob `ee0be99921bf153a70a3aed349450778fa4adfa0`
  - `17 r001` blob `8b0d17eadbc7ad7864735ab259d59101e4e804f2`
  - `91 r047` blob `7c0ca30983f04f35cdd9efe7ec7273c1de55c5fb`.
- **Affected Verification Contract:** verify target pin/schema on every active mandatory Project Source document plus active `91`; stable `FRAMEWORK-001`/Project UUID; binding values preserved; bootstrap first-read active 00 and no stale `01/03/09` revision pointers; Index/Manifest exact active routing; revision monotonicity/supersedes; `MIG-002/EVD-086/EVD-087/CHG-087/OUT-014/AUTH-014/ACT-026/ENV-014` resolve from active current homes; `02` no longer carries stale 1.7/1.8 current truth; no optional surface synthesis; all 16 predecessors archived; no duplicate active predecessor paths.
- **Release-Level Verification Contract:** corrected final candidate diff contains only approved root/bootstrap/Project Source/archive paths; Framework-Source subtree remains exact; canonical target has not moved before promotion; history update is non-force fast-forward; exact terminal commit is freshly observable on canonical `main`; no prohibited binding/runtime/disclosure/secret/AI-ControlTower/Git-native-MCP migration effects.
- **Verification Method:** deterministic Git object/tree/ref inspection and current Project Source structural/content checks on the exact corrected candidate. ProjectFramework has no application runtime and this upgrade adds no executable runtime test surface; the release-level gate is therefore governance/documentation resulting-state verification, not an invented runtime test suite.
- **Result Claim Boundary:** this record is prepared before the self-containing corrected terminal commit exists. `UPGRADE_AFFECTED` / `UPGRADE_RELEASE_FULL` PASS and `OUT-014 ACHIEVED` become externally claimable only after the corrected final tree/commit is created, all assertions above are fresh-checked against it, canonical `main` is fast-forwarded non-force, and the same terminal commit is freshly observed there. Failure of any assertion leaves completion unclaimed and requires repair rather than inference.
- **Related:** `MIG-002`, `CHG-087`, `OUT-014`, `AUTH-014`, `ACT-026`, `ENV-014`.

No evidence record stores secret values or private chain-of-thought.
