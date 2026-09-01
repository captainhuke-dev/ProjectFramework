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
epistemic_status: "USER_CONFIRMED"
freshness_class: "STABLE"
project_source_framework_version: "1.9.1"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
---

# 00 — Project Source Framework

> **Starter pointer:** Instantiate the full root document from `../00-project-source-framework.md`. This mockup file makes slot `00` concrete and does not replace the authoritative full Framework template.

## Bootstrap Requirement

Create this document first as active `FRAMEWORK-001`; descendants inherit from it. NEW Projects bootstrap from canonical repository `main`, then create mandatory `01–05` and `09–17`; evaluate conditional `06–08`, `40`, `60`, `91`, `92`; keep `18–19` reserved. For resulting Framework `1.7.0+` Projects, materialize `<Project-Root>/PROJECT-BOOTSTRAP.md` from `../PROJECT-BOOTSTRAP.md` and verify it routes back to this active root. The root file is a locator only.

## Project Location Binding Pointer

The full root template `../00-project-source-framework.md` carries the authoritative current Framework Project Location Binding contract. A GREENFIELD starter records approved states/identities in active `FRAMEWORK-001`, for example:

```yaml
project_location_binding:
  github:
    binding_state: "<BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED>"
    repository: "<OWNER/REPOSITORY_OR_UNKNOWN>"
    repository_url: "<CANONICAL_REPOSITORY_URL_OR_UNKNOWN>"
  google_drive:
    binding_state: "<BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED>"
    project_root_id: "<FOLDER_ID_OR_UNKNOWN>"
    project_root_url: "<CANONICAL_FOLDER_URL_OR_UNKNOWN>"
  local_workspaces:
    - environment_scope: "<USER_CONFIRMED_ENVIRONMENT_SCOPE>"
      binding_state: "<BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED>"
      canonical_path: "<ABSOLUTE_LOCAL_PATH_OR_UNKNOWN>"
      repository: "<OWNER/REPOSITORY_OR_UNKNOWN_OR_NOT_APPLICABLE>"
  file_storage_locations:
    - storage_key: "<PROJECT_DEFINED_STORAGE_KEY>"
      binding_state: "<BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED>"
      storage_type: "<S3 | NAS | SMB | NFS | SHAREPOINT | OBJECT_STORAGE | FILE_SERVER | FILESYSTEM | OTHER>"
      canonical_locator: "<PROVIDER_APPROPRIATE_DURABLE_LOCATOR_OR_UNKNOWN_OR_NOT_APPLICABLE>"
      content_scope: "<DECLARED_CONTENT_SCOPE>"
      authoritative_scope: "<OWNED_PROJECT_FILE_OBJECT_SCOPE>"
      verification_status: "<VERIFIED | USER_CONFIRMED | VERIFICATION_REQUIRED>"
      last_verified_at: "<ISO8601_OR_UNKNOWN>"
```

Use the full root contract for Bootstrap Location precedence, minimum durable identity, generic non-Drive File Storage Binding, dedicated non-duplicated Google Drive authority, fail-closed behavior, verification metadata, designated progress-file pointers, Root Governance mutation approval, and environment-scoped local routing, MCP/tool IDs as evidence only, and separation from current branch/worktree / Canonical Integration Target / Canonical Implementation Source / Runtime Location. `03`/`09` reference this binding; they do not become an independent authority. Do not add `canonical_branch` to Project Location Binding.
## Framework 1.3.1 Command / Direct Upgrade Pointer

The full root template carries registered `[Project Status]` / `[Project Path]` / `[Project Upgrade]` semantics, Markdown-safe mandatory response-close presentation, and Direct-to-Latest cumulative upgrade governance. `[Project Upgrade]` fresh-compares the active local pin with canonical upstream target evidence, reports `UP_TO_DATE | UPGRADE_AVAILABLE | SOURCE_DIVERGENCE | VERIFICATION_REQUIRED`, and treats a positive upgrade choice as assessment/Preview authorization only—not mutation. Brackets are required and command-name matching inside them is case-insensitive. `<...>` Project Path placeholders mean unset. Initialized Projects remain pinned and, when explicitly upgraded, classify `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`; direct current→target migration preserves Stable IDs, Project-Specific Rules, bindings, current truth, and history without mandatory intermediate-release execution.

## Framework 1.2.0 Extended Semantics

```text
40 Technical Design               CONDITIONAL
60 Deployment Plan                CONDITIONAL
91 Project Management Control     CONDITIONAL / STANDARD IN 1.2.0+
92 Project Graph                  CONDITIONAL / STANDARD IN 1.6.0+
93–99 Project-specific / Governance Extension
```

`91` canonically owns `RISK-* / ASM-* / MS-* / OUT-* / DEP-* / CR-* / GATE-*`. Framework `1.6.0` standardizes conditional `92 Project Graph` as canonical home of current `REL-*` assertions; AI-ControlTower/OpenViking indexing remains `DERIVED_ONLY` / rebuildable and relation topology never transfers location/implementation/runtime authority. Technical planning remains documentation/blueprint scope and does not authorize source code, Dockerfile/Compose, scripts, CI, or automation.

## Framework 1.2.3 Workspace / Runtime Authority Pointer

The full root template carries the binding `Canonical Implementation Source and Runtime Authority` contract. When material, `40` documents Development Workspace Contract semantics and `60` documents source-to-runtime, runtime mutability, persistent-state, and replacement/recreation semantics. Runtime-only edits do not silently become canonical Implementation Truth; material mismatch that should align reuses `DRIFT-*`. Durable Dev Container/remote workspaces remain valid and Docker/host-local source are not universal requirements.

## Externalized Working Memory / Chat Lifecycle Pointer

The full root template `../00-project-source-framework.md` carries the binding `Externalized Working Memory and Chat Lifecycle` contract, including Material vs Transient connector activity, Logical Checkpoint persistence, `PERSISTENCE_PENDING`, and `CONTINUE_CURRENT_CHAT | START_NEW_CHAT`. Keep those semantics in the full root template; do not duplicate or weaken the normative contract in this starter.

## Git Base Freshness / Forward-Port Pointer

The full root template also carries the binding `Git Work Base Freshness and Forward-Port` contract. Independent Git work starts from a freshly verified canonical integration target; feature-on-feature ancestry must be explicit `STACKED_WORK`; semantic base drift uses `BASE_STALE` / `FORWARD_PORT_REQUIRED`; and pre-merge acceptance is rechecked against the current target head. `Mergeable ≠ Acceptable`. Framework 1.2.3 does not replace this contract.

## Framework Source Provenance — Optional Assurance

```yaml
framework_source_provenance:
  repository: "captainhuke-dev/ProjectFramework"
  source_ref: "<OBSERVED_REF_OR_MAIN>"
  release_tag: "<OPTIONAL_OBSERVED_TAG_OR_NONE>"
  resolved_commit_sha: "<OPTIONAL_OBSERVED_SHA_OR_UNKNOWN>"
  framework_version: "1.3.1"
  schema_version: "1.0.0"
  captured_at: "<ISO8601_WITH_TIMEZONE>"
  provenance_status: "<VERIFIED | PARTIAL | UNVERIFIED>"
```

Never invent exact Git identity. Absence of optional exact provenance does not by itself block normal Framework use.