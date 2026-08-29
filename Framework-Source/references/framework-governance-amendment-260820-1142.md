# Project Source Framework Governance Amendment — 1.2.0

```yaml
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.1.5"
project_source_framework_version: "1.2.0"
project_source_schema_version: "1.0.0"
approved_at: "2026-08-20T11:42:00+07:00"
approval_basis: "USER_EXPLICIT_APPROVAL"
compatibility: "BACKWARD_COMPATIBLE_PROJECT_MANAGEMENT_AND_TECHNICAL_BLUEPRINT_EXPANSION"
```

## Purpose

Framework `1.2.0` expands ProjectFramework as a conceptual Project governance and planning framework in two areas: stronger Project-management control and clearer technical/install/deployment documentation for Projects that contain software. It does not turn ProjectFramework into an application-development, container-build, CI/CD, or automation system.

## Binding Changes

1. `91 Project Management Control` becomes a **STANDARD CONDITIONAL** extended semantic document in Framework `1.2.0+`.
2. Current canonical homes in `91` are:

```text
RISK-*   Risk
ASM-*    Assumption
MS-*     Milestone
OUT-*    Outcome
DEP-*    Dependency
CR-*     Change Request
GATE-*   Review / Phase Gate
```

3. `40 Technical Design` is a **CONDITIONAL** extended document for Tech Stack, component/interface responsibilities, source-structure responsibility, configuration semantics, runtime requirements, deployment-mode architecture, and Source/Docker parity/variance.
4. `60 Deployment Plan` is a **CONDITIONAL** extended document for installation/operations semantics, including Source installation, Docker installation, startup/shutdown, verification/health, logs/diagnostics, upgrade, rollback, backup/restore, cleanup, troubleshooting, and known deployment variance.
5. Deployment-support vocabulary is:

```text
SOURCE_ONLY
DOCKER_ONLY
SOURCE_AND_DOCKER
NOT_APPLICABLE
```

6. `SOURCE_AND_DOCKER` requires one declared application/configuration/data/security/persistence contract. Intentional differences must be represented as explicit Deployment Mode Variance; unexpected divergence is `DRIFT-*`.
7. `03 Current State` may carry multi-dimensional Project Health using `GREEN / AMBER / RED / UNKNOWN`, with supporting reason/evidence and no opaque automatic aggregate score.
8. Review Cadence may be `TIME_BASED` or `EVENT_BASED` for current state, risks, assumptions, milestones/outcomes, decision revalidation, technical design, deployment readiness, and handoff. Framework `1.2.0` does not create a scheduler/reminder service.
9. `DEC-*` remains canonical in `04 Decision Log`; Framework `1.2.0` adds Decision Revalidation semantics without creating a new Decision registry.
10. `11 Actor Registry` may contain responsibility mapping (`Responsible / Accountable / Consulted / Informed`) keyed by governed scope. **Responsibility is not Authority**; authorization remains canonical in `12 Authorization Registry` through `AUTH-*` / `DEL-*`.
11. Knowledge/documentation debt remains an `ISS-*` in `08 Open Issues` using `issue_type: KNOWLEDGE_DEBT`; it does not get a separate registry.
12. `90` remains the general/special governance-extension anchor. `91` is standardized as described above. `92–99` remain Project-specific / Governance Extension space unless a future Framework revision governs them otherwise.
13. Brownfield migration MUST NOT overwrite a pre-existing custom document in semantic slot `91`. Upgrade must assess the collision through `MIG-*`, preserve identity/history/references, obtain explicit approval for any relocation, and activate standard `91` only after the collision is resolved.
14. Existing free-text notes MUST NOT be automatically promoted into `RISK-*`, `ASM-*`, `MS-*`, `OUT-*`, `DEP-*`, `CR-*`, or `GATE-*`. Promotion requires enough current semantics, status, ownership, and epistemic/evidence state to avoid fabrication.
15. A Golden Reference Project Source is an illustrative composition example only. Core Governance and the active Framework remain normative on conflict.
16. Project Source Schema remains `1.0.0`.
17. Existing Projects remain locally pinned and never auto-upgrade. Adoption of Framework `1.2.0` uses governed `MIG-*` assessment plus explicit approval.
18. Canonical NEW-project bootstrap remains repository `main`; exact Git tag/SHA and branch protection remain optional assurance rather than operational prerequisites.

## Project Management Semantics

### Risk vs Issue

`RISK-*` represents a material uncertain future event or condition. `ISS-*` represents a materialized/current problem. Materialization preserves the Risk record and links the resulting Issue rather than deleting or silently rewriting the Risk.

Risk statuses may include:

```text
IDENTIFIED
OPEN
MITIGATING
MONITORING
ACCEPTED
MATERIALIZED
CLOSED
SUPERSEDED
```

`ACCEPTED` risk exposure identifies the applicable decision/authority and review trigger when material.

### Assumption

`ASM-*` represents a proposition relied upon without sufficient verification. Recommended lifecycle:

```text
UNVERIFIED
VALIDATED
INVALIDATED
SUPERSEDED
```

Invalidation triggers impact assessment and may require `DRIFT-*`, `CR-*`, replanning, Decision revalidation, Requirement revision, Risk update, or Issue creation.

### Action, Milestone, Outcome

```text
ACT-* DONE ≠ MS-* REACHED ≠ OUT-* ACHIEVED
```

Actions are work. Milestones are significant checkpoints/states. Outcomes are intended results/benefits and require independent evaluation/evidence when measurable.

### Dependency

`DEP-*` may represent people, teams, approvals, decisions, vendors, systems, APIs, data, contracts, Projects, infrastructure, or other material dependencies. `AVAILABLE` means obtainable; `SATISFIED` means the governed dependency requirement is fulfilled.

### Change Request vs Change Log

```text
CR-*  = proposed/material change + impact assessment + decision path
CHG-* = historical record of applied/observed change
```

### Review Gate

`GATE-*` represents a governed checkpoint with entry/pass criteria, required evidence, review owner, authority, findings, exception/waiver, and exact next action. `WAIVED` requires rationale and the applicable decision/authority reference.

## Technical Blueprint Semantics

`06 Architecture` remains the major architecture view. `40 Technical Design` is the deeper implementation-facing documentation blueprint when applicable.

`07 Implementation Plan` remains the planned-work/action view. `60 Deployment Plan` is the installation/operations view when applicable.

A material Tech Stack entry identifies at least Technology, Role/Responsibility, Version or Supported Range, Required/Optional state, reason/Decision reference, component usage, operational dependency, support/lifecycle constraint when material, replacement boundary when material, and epistemic/verification state.

The Configuration Contract separates semantic configuration meaning from packaging mode and includes application settings, environment-specific settings, external-service endpoints, persistence settings, capability settings when material, and `SECRET-*` references. Actual secret values remain forbidden.

For Source and Docker modes, the Project may document concrete commands/paths when those are verified Project truth. ProjectFramework itself does not invent implementation commands or produce implementation artifacts for nonexistent software.

## Concept-First Implementation Boundary

Framework `1.2.0` does **not** authorize or require creation of:

```text
application source code
Dockerfile
Compose / Kubernetes / Helm runtime artifacts
install scripts
package-manager tooling
validator / CLI
GitHub Actions / CI/CD
deployment automation
scheduler / reminder runtime
dashboard / project-management application
background automation
runtime enforcement service
```

A separate explicit implementation request is required before designing or creating those artifacts.

## Golden Reference

Framework `1.2.0` includes a synthetic software Project Source under:

```text
examples/golden-reference-software-project/Project-Source/
```

It demonstrates `00–17` plus applicable `40`, `60`, and `91`, coherent synthetic Stable IDs, Tech Stack responsibility, `SOURCE_AND_DOCKER`, parity/variance, installation/operations blueprint, Project Health, Review Cadence, migration safety, and handoff. It contains no application code, Dockerfile, Compose, install script, CI workflow, binary artifact, or real secret.

## Precedence

This amendment is the latest binding clarification for Framework `1.2.0` Project-management and Technical Blueprint semantics. Earlier amendments remain binding for non-conflicting subjects, including concept-first scope, canonical-main bootstrap, optional release assurance, platform-launcher equivalence, semantic-slot invariants, Materialized Current State, archive-independent current truth, authority, secrets, and historical preservation.
