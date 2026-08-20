---
project_uuid: "12000000-0000-4000-8000-000000000001"
project_id: "GOLDEN-SW-001"
project_name: "HarborDesk Reference Service"
document_id: "TECH-001"
document_type: "TECHNICAL_DESIGN"
semantic_slot: "40"
revision: 1
document_status: "ACTIVE"
inherits_from: ["FRAMEWORK-001"]
created_at: "2026-08-20T11:45:00+07:00"
updated_at: "2026-08-20T11:45:00+07:00"
created_by: "ACTOR-002"
created_by_instance: "INST-GOLDEN-001"
epistemic_status: "VERIFIED"
freshness_class: "STABLE"
project_source_framework_version: "1.2.0"
project_source_schema_version: "1.0.0"
synthetic_reference: true
---

# 40 — Technical Design

> **Synthetic / Documentation-only:** This file is a technical blueprint for a fictional service. It does not correspond to application source code, package manifests, Docker images, or a running system in this repository.

## Technical Design Scope

Demonstrate Framework `1.2.0` Tech Stack, component responsibility, source-structure responsibility, configuration semantics, runtime requirements, `SOURCE_AND_DOCKER`, and explicit deployment-mode variance without implementing HarborDesk.

## Tech Stack Contract

| Technology | Role / Responsibility | Version / Range | Required | Why / Related Decision | Used By | Operational Dependency | Lifecycle / Replacement Boundary | Epistemic State |
|---|---|---|---|---|---|---|---|---|
| Python | Fictional application runtime/language | 3.12 | Yes for Source mode | Synthetic reference choice | Application service | Compatible 64-bit Linux runtime | Runtime boundary; replace only through governed technical change | VERIFIED_AS_SYNTHETIC_BLUEPRINT |
| FastAPI | Fictional HTTP application framework | 0.115 | Yes | Demonstrate framework responsibility | Application service | Python runtime | Application-framework boundary | VERIFIED_AS_SYNTHETIC_BLUEPRINT |
| Uvicorn | Fictional application server responsibility | 0.30 | Yes | Demonstrate serving/runtime responsibility | Application service | Python runtime + application package | Server/runtime boundary | VERIFIED_AS_SYNTHETIC_BLUEPRINT |
| PostgreSQL | Primary relational datastore | 16 | Yes | DEC-001 | Application persistence | DEP-001 | Data-store boundary; data semantics remain stable across deployment modes | VERIFIED_AS_SYNTHETIC_BLUEPRINT |
| Docker Engine | Container runtime for Docker mode | 26+ | Required only for Docker mode | DEC-002 / REQ-002 | Docker deployment | Supported 64-bit Linux host | Packaging/runtime boundary | VERIFIED_AS_SYNTHETIC_BLUEPRINT |
| 64-bit Linux | Supported host platform | Current supported distribution | Yes | Synthetic operating constraint | Source and Docker modes | Host platform | Platform boundary | VERIFIED_AS_SYNTHETIC_BLUEPRINT |

No package file, dependency lockfile, image, or executable artifact is provided.

## System / Component Blueprint

### Fictional HarborDesk Application Service

- **Responsibility:** expose the conceptual application/API surface and coordinate persistence.
- **Inputs:** application requests; non-secret configuration; secret references resolved externally.
- **Outputs:** conceptual responses and persistence operations.
- **Interfaces:** application port `8080` in the blueprint; datastore connection contract.
- **Dependencies:** Python/FastAPI/Uvicorn responsibilities in Source mode; container runtime/image responsibility in Docker mode; `DEP-001` PostgreSQL.
- **Data Ownership:** application-domain relational data is persisted through PostgreSQL.
- **Security Boundary:** secret material remains external; `SECRET-001` is metadata only.

### PostgreSQL Service

- **Responsibility:** relational data persistence under DEC-001 / REQ-003.
- **Persistence:** durable storage is required.
- **Dependency:** availability represented by `DEP-001`.
- **Risk:** persistent-volume/storage misconfiguration represented by `RISK-001`.

## Source Structure Blueprint

These paths are **conceptual responsibility examples only; the directories are not created in this repository**:

```text
src/             application implementation responsibility
config/          non-secret configuration responsibility
tests/           verification-asset responsibility
migrations/      schema/data migration responsibility
Project-Source/  governance/current-truth/continuation responsibility
```

An actual HarborDesk repository may choose different paths if responsibility boundaries remain clear and governed.

## Configuration Contract

| Configuration semantic | Meaning | Sensitivity | Source-mode mapping | Docker-mode mapping | Current state |
|---|---|---|---|---|---|
| `APP_ENV` | Select conceptual environment/profile | Non-secret | Environment/config source | Environment/config mount | DEFINED_AS_BLUEPRINT |
| `APP_PORT` | Application listening-port semantic; conceptual default `8080` | Non-secret | Runtime/config setting | Container/service port mapping | DEFINED_AS_BLUEPRINT |
| `DATABASE_URL` | Database connection-reference semantic | Sensitive connection metadata; actual value external | External config/secret resolution | External config/secret mechanism | VALUE_NOT_PRESENT |
| `DB_PASSWORD` | Database credential semantic | Secret | Resolve externally via SECRET-001 | Resolve externally via approved container secret mechanism | VALUE_NOT_PRESENT |

Semantic meaning remains the same across modes even when packaging mechanics differ. No actual credential or connection string is stored here.

## Runtime Requirements

```text
Supported host: 64-bit Linux
Source runtime: Python 3.12
Docker runtime: Docker Engine 26+ when Docker mode is used
Application port semantic: 8080
Datastore: PostgreSQL 16
Persistent database storage: required
External credential resolution: required
Startup dependency: datastore availability before persistence-dependent application readiness
```

CPU/memory/storage sizing is intentionally `UNKNOWN / PROJECT_SPECIFIC` in this synthetic reference rather than fabricated.

## Deployment Support Model

```text
SOURCE_AND_DOCKER
```

## Source-Mode Architecture

```text
Operator
  ↓
Fictional Source Tree
  ↓
Python 3.12 + FastAPI/Uvicorn responsibilities
  ↓
HarborDesk application responsibility on port semantic 8080
  ↓
External PostgreSQL 16 service
```

## Docker-Mode Architecture

```text
Operator / Client
      ↓
Fictional HarborDesk application container/service responsibility
      ↓
Separate PostgreSQL 16 container/service responsibility

Application port semantic → 8080
Database persistence → named/durable volume responsibility
Configuration → environment/config mount semantics
Secrets → external approved secret mechanism / SECRET-001 reference
```

No image, Dockerfile, Compose file, network, volume, or container is actually created.

## Source / Docker Parity Contract

| Capability / Contract | Source Mode | Docker Mode | Variance |
|---|---|---|---|
| Core application semantics | Same declared HarborDesk behavior | Same declared HarborDesk behavior | None |
| Application port meaning | `APP_PORT`, conceptual default 8080 | Same semantic mapped to service/container | Packaging mechanics only |
| Database engine/data semantics | PostgreSQL 16 | PostgreSQL 16 | None |
| Configuration meaning | APP_ENV / APP_PORT / database reference semantics | Same semantics | Delivery mechanics may differ |
| Secret policy | External resolution; no Project Source secret | External approved container secret mechanism | Mechanism differs, policy same |
| Data compatibility | Same PostgreSQL relational contract | Same PostgreSQL relational contract | None |
| Persistence requirement | External PostgreSQL durable storage | Docker database-service durable volume responsibility | Persistence mechanics differ |
| Upgrade compatibility | Must preserve declared data/application contract | Must preserve same contract | Procedure may differ |
| Backup / Restore | External PostgreSQL operational responsibility | Docker database-volume/service operational responsibility | Procedure/mechanics differ |

## Deployment Mode Variance — Database Placement and Persistence Mechanics

> **Local descriptive sub-record:** This heading is not a new Framework Stable-ID object type. Canonical management-object types remain those defined by Framework `1.2.0`.

- **Affected Capability:** Database placement and persistence/backup mechanics.
- **Source Behavior:** PostgreSQL is an external service managed outside the application source runtime.
- **Docker Behavior:** The reference topology may place PostgreSQL in a separate container/service with durable volume responsibility.
- **Reason:** Packaging convenience for the Docker blueprint.
- **Impact:** Persistence preparation, backup/restore, startup ordering, and operational procedure differ; data semantics and required PostgreSQL version remain the same.
- **Related:** DEC-001, DEC-002, REQ-002, REQ-003, RISK-001
- **Owner:** ACTOR-002
- **Acceptance / Resolution State:** ACCEPTED_AS_DOCUMENTED_SYNTHETIC_VARIANCE

Any future real implementation/runtime difference beyond declared variance would be evaluated as `DRIFT-*` rather than silently normalized.

## Related

`DEC-001`, `DEC-002`, `REQ-001`, `REQ-002`, `REQ-003`, `RISK-001`, `ASM-001`, `DEP-001`, `CR-001`, `EVD-001`.

## Verification / Drift Notes

EVD-001 verifies documentation completeness only. No source tree, process, port listener, database, image, container, volume, or runtime parity was executed.
