---
project_uuid: "12000000-0000-4000-8000-000000000001"
project_id: "GOLDEN-SW-001"
project_name: "HarborDesk Reference Service"
document_id: "FRAMEWORK-001"
document_type: "PROJECT_SOURCE_FRAMEWORK"
semantic_slot: "00"
revision: 1
document_status: "ACTIVE"
framework_root: true
inherits_from: []
created_at: "2026-08-20T11:45:00+07:00"
updated_at: "2026-08-20T11:45:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-GOLDEN-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.2.0"
project_source_schema_version: "1.0.0"
compatible_framework_range: ">=1.0,<2.0"
compatible_schema_range: ">=1.0,<2.0"
synthetic_reference: true
---

# 00 — Project Source Framework

> **Synthetic Golden Reference:** This is a fictional Project Source used only to demonstrate Framework `1.2.0` composition. No HarborDesk application, Docker image, database, or runtime exists in this repository.

## Root Governance

`FRAMEWORK-001` is the non-removable Root Governance. Every governed descendant inherits from it. User Explicit Approval is required to revise Root Governance; descendants may specialize but never weaken it.

Required read order begins:

```text
00 → 01 → 03
```

Current Stable IDs must resolve from the Current Reconstructable Snapshot without archive traversal. Archive is Historical Truth only.

## Namespace Used by This Reference

```text
00–05 and 09–17   mandatory core documents
06–08             conditional and applicable in this synthetic Project
40 Technical Design        conditional and applicable
60 Deployment Plan         conditional and applicable
91 Project Management Control conditional and applicable
18–19              RESERVED / not materialized
```

`91` canonically owns `RISK-* / ASM-* / MS-* / OUT-* / DEP-* / CR-* / GATE-*`.

## Concept-First Technical Boundary

The Project may document a fictional Tech Stack, Source/Docker topology, installation responsibilities, ports, volumes, configuration semantics, and verification criteria. This example MUST NOT be interpreted as executable implementation. It contains no application source code, Dockerfile, Compose file, install script, CI workflow, runtime artifact, or real secret.

## Authority and Secret Invariants

Responsibility does not grant authority. Authority is canonical in `12` through `AUTH-* / DEL-*`. Handoff does not transfer authority.

Actual secrets are forbidden. `SECRET-*` stores external-reference metadata only.

## Framework Source Provenance

This synthetic reference demonstrates semantic version pinning only:

```yaml
framework_source_provenance:
  repository: "captainhuke-dev/ProjectFramework"
  source_ref: "main"
  release_tag: null
  resolved_commit_sha: null
  framework_version: "1.2.0"
  schema_version: "1.0.0"
  captured_at: "2026-08-20T11:45:00+07:00"
  provenance_status: "UNVERIFIED"
```

No exact tag/SHA is invented for this synthetic snapshot.
