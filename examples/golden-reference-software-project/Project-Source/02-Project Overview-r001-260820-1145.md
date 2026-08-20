---
project_uuid: "12000000-0000-4000-8000-000000000001"
project_id: "GOLDEN-SW-001"
project_name: "HarborDesk Reference Service"
document_id: "OVERVIEW-001"
document_type: "PROJECT_OVERVIEW"
semantic_slot: "02"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-20T11:45:00+07:00"
updated_at: "2026-08-20T11:45:00+07:00"
created_by: "ACTOR-001"
created_by_instance: "INST-GOLDEN-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.2.0"
project_source_schema_version: "1.0.0"
synthetic_reference: true
---

# 02 — Project Overview

## Purpose

HarborDesk Reference Service is a **fictional software Project used only as executable documentation in the governance sense**. It demonstrates how Framework `1.2.0` Project-management and Technical Blueprint concepts compose in a realistic Project Source.

## In Scope

- coherent Project Source `00–17 + 40 + 60 + 91`;
- fictional operator-facing API/service architecture;
- fictional Tech Stack and deployment assumptions;
- `SOURCE_AND_DOCKER` documentation blueprint;
- management controls, Health, Review Cadence, migration, evidence, authority, and handoff semantics.

## Out of Scope

- application source code;
- working API/server/database;
- Dockerfile/Compose/Kubernetes/Helm;
- package manifests/install scripts;
- CI/CD or automation;
- runtime verification claims;
- real credentials/secrets.

## Stakeholders / Systems

```text
ACTOR-001 Project Owner
ACTOR-002 Technical Lead
ACTOR-003 Operator
Fictional application service
Fictional PostgreSQL service
```

## Known Constraints

- Reference is synthetic and must not claim runtime execution.
- Source and Docker deployment descriptions must preserve one application/data/security/configuration contract.
- Actual secrets remain external references only.

## Project Lineage

Synthetic example designed directly for Framework `1.2.0`; `MIG-001` demonstrates how a real `1.1.5 → 1.2.0` assessment would be represented without asserting a real migration occurred.
