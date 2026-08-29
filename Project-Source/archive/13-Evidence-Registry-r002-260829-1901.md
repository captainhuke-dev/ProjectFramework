---
project_uuid: "00575e76-17ce-4dd3-ad24-377494a4a45b"
project_id: "PROJECTFRAMEWORK"
project_name: "ProjectFramework"
document_id: "EVIDENCE-REGISTRY-001"
document_type: "EVIDENCE_REGISTRY"
semantic_slot: "13"
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

# 13 — Evidence Registry

Canonical home of `EVD-*`.

## EVD-001 — GREENFIELD Initialization Basis

- **Evidence Type:** USER_APPROVAL + REPOSITORY_OBSERVATION
- **Captured At:** 2026-08-29T17:07:00+07:00
- **Captured By Actor / Instance:** ACTOR-001 / INST-001
- **Source Reference:** user-approved Preview; fresh CEO MCP Git/workspace observations
- **Artifact Path:** `PROJECT-BOOTSTRAP.md`, `Project-Source/`, `docs/superpowers/PROJECT-TASKS.md`, `managing-project-source/FRAMEWORK-RELEASE.yaml`
- **Artifact Hash:** NOT_APPLICABLE_BEFORE_FIRST_COMMIT
- **Supports:** FRAMEWORK-001, ACT-001, CHG-001
- **Epistemic Status:** VERIFIED / USER_CONFIRMED by field

Observed facts:

```text
Project Name: ProjectFramework
Project ID: PROJECTFRAMEWORK
Project UUID: 00575e76-17ce-4dd3-ad24-377494a4a45b (user-approved initialization identity)
Repository: captainhuke-dev/ProjectFramework
Remote URL: https://github.com/captainhuke-dev/ProjectFramework
Local Workspace: E:\GitHub\ProjectFramework
Framework: 1.7.0
Schema: 1.0.0
Google Drive: NOT_APPLICABLE (user-confirmed)
External File Storage: NOT_APPLICABLE (user-confirmed)
Pre-write Git: main at 128057da827b2b32098a7ba2b4d70376ad47486f; origin/main d6093e5e98ba4fe2bff8e168bda834037194d24a; clean; ahead 1
```

Never store actual secrets as evidence.

## EVD-002 — Initialization Verification and Completion Commits

- **Evidence Type:** STRUCTURAL_VALIDATION + GIT_COMMIT_OBSERVATION
- **Captured At:** 2026-08-29T17:19:13+07:00
- **Captured By Actor / Instance:** ACTOR-002 / INST-001
- **Source Reference:** maintained Framework 1.7.0 templates plus fresh post-write validation/Git observations
- **Artifact Path:** `PROJECT-BOOTSTRAP.md`, `Project-Source/`
- **Artifact Hash:** completion payload represented by observed Git commits below
- **Supports:** FRAMEWORK-001, ACT-001, CHG-002
- **Epistemic Status:** VERIFIED

```text
Project Source structural validation: PASS 163/163
Initialization payload commit: 06bb77a6db61c01a3ed8a78a23b2fc588a3431ce
Root-governance cleanup commit: 01ef9e5e60d28cc0efcc0c231601c46064467f84
Remote publication: NOT_PERFORMED
```

## EVD-003 — Framework-Source distribution-root migration evidence

- **Evidence Type:** REPOSITORY_MIGRATION + STRUCTURAL_VALIDATION + HISTORICAL_BLOB_PRESERVATION
- **Captured At:** 2026-08-29T19:01:09+07:00
- **Captured By Actor / Instance:** ACTOR-002 / INST-001
- **Source Reference:** TASK-038 design/plan; fresh repository observations; scenarios 181–188 RED contract; migration/starter verification
- **Artifact Path:** `Framework-Source/`, `README.md`, `Project-Source/`, `docs/superpowers/PROJECT-TASKS.md`
- **Artifact Hash:** checkpoint commits and historical blob SHA sentinels below
- **Supports:** FRAMEWORK-001 current routing, `MIG-001`, `ACT-002`, `CHG-003`
- **Epistemic Status:** VERIFIED for recorded checkpoints; final TASK-038 affected/RELEASE_FULL verification pending

```text
Scenario contract commit: 80ac496
Physical rename/release identity commit: fb24141
Starter/launcher propagation commit: 5757660
Canonical distribution root observed: Framework-Source/
Live old-root alias observed: absent
Framework upstream release: 1.8.0 / Schema 1.0.0 / release format 3
Launcher shared body: byte-identical; lengths 4285 / 4284
Maintained starter stamps: 24/24 at Framework 1.8.0 / Schema 1.0.0
Historical blob sentinel — framework-governance-amendment-260820-0735.md: 7f2156f28a031680322e3a4e16cff45bf803cb94
Historical blob sentinel — framework-governance-amendment-260820-0821.md: 5ad06a827829fe5c96ae9a8c8c17e1071b1f4f1d
Historical blob sentinel — framework-governance-amendment-260825-task020.md: e6a074b77fb0165de1c281eabfbab7c6c938d6e3
Historical blob sentinel — TASK-023 design: 9fcf09e3bcc6f2c9c46ae9f2ec98682f87f48f5e
Historical blob sentinel — TASK-023 release evidence: fef1b9d976e9ab227f90fce6258a83743e9532a8
Final affected verification: PENDING
Final RELEASE_FULL: PENDING
Remote publication of TASK-038: NOT_PERFORMED
```

Never store actual secrets as evidence.
