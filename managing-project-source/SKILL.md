---
name: managing-project-source
description: Use when creating, adopting, importing, updating, reviewing, handing off, or exporting a Project Source; when a project needs consistent governance, naming, source-of-truth handling, continuation context, project-management control, or technical/install documentation.
---

# Managing Project Source

## Overview

Maintain a consistent `Project-Source/` governance layer. Make **current truth, current authority, Project health, and exact next action** explicit without inventing facts.

Current distribution: **Framework 1.2.1 / Schema 1.0.0**.

ProjectFramework is **conceptual governance/planning first**. Technical and integrity requirements are semantic contracts. **Do not expand Tech Stack, installation, Docker, governance, or integrity work into application code, Dockerfile/Compose, scripts, validator/CLI, CI/CD, scheduler, background automation, or other implementation unless the user explicitly requests a separate implementation scope.**

## Required References

Before creating or materially changing Project Source, read:

- `FRAMEWORK-RELEASE.yaml` for current distribution identity/bootstrap policy
- `references/framework-governance-amendment-260821-1254.md`
- `references/framework-governance-amendment-260820-1142.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-1024.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0821.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0735.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0707.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0646.md` (historical approved amendment)
- `references/framework-governance-amendment-260814-0808.md` (historical approved amendment)
- `references/core-governance-rules.md`
- `templates/00-project-source-framework.md`
- `templates/core-document-skeletons.md`
- `templates/project-source-mockup/README.md`

Historical spec/design files are rationale only. Latest Framework amendment wins on conflict.

## Platform Project Bootstrap Entrypoints

Official platform launchers:

- `CHATGPT-PROJECT-INSTRUCTIONS.md`
- `CLAUDE-PROJECT-INSTRUCTIONS.md`

Their text between `PROJECTFRAMEWORK-SHARED-CONTRACT:START` and `PROJECTFRAMEWORK-SHARED-CONTRACT:END` MUST remain byte-identical. Platform wrappers may differ only in placement instructions. Launchers are bootstrap/continuation helpers, never a competing governance root.

If active local `FRAMEWORK-001` exists, local pinned Project Source is authoritative. NEW Project bootstrap begins from canonical repository `main`. Exact Git tag/SHA and branch protection are optional assurance, not normal-use prerequisites.

## Framework 1.2.0 Namespace and Routing

Mandatory core remains `00–05` and `09–17`; `06–08` remain conditional; `18–19` remain reserved.

Framework `1.2.0` standardizes:

```text
40 Technical Design               CONDITIONAL
60 Deployment Plan                CONDITIONAL
90 General / Special Governance Extension anchor
91 Project Management Control     CONDITIONAL / STANDARD IN 1.2.0+
92–99 Project-specific / Governance Extension
```

When active, route:

```text
40 → Tech Stack / components / source structure / config / runtime / Source-Docker technical blueprint
60 → installation / startup-shutdown / verification / diagnostics / upgrade-rollback / backup-restore / cleanup
91 → RISK-* / ASM-* / MS-* / OUT-* / DEP-* / CR-* / GATE-*
```

Do not create conditional documents merely to make the Project tree look complete.

## Canonical Project-Management Homes

```text
RISK-* → 91 Project Management Control
ASM-*  → 91 Project Management Control
MS-*   → 91 Project Management Control
OUT-*  → 91 Project Management Control
DEP-*  → 91 Project Management Control
CR-*   → 91 Project Management Control
GATE-* → 91 Project Management Control
```

Existing canonical homes remain unchanged for `DEC-*`, `REQ-*`, `ISS-*`, `DRIFT-*`, `CONFLICT-*`, `CHG-*`, actors, authority, evidence, actions, migrations, and secret references.

Key distinctions:

```text
RISK-* future uncertainty ≠ ISS-* materialized/current problem
ACT DONE ≠ MS REACHED ≠ OUT ACHIEVED
DEP AVAILABLE ≠ DEP SATISFIED
CR-* proposed/material change control ≠ CHG-* applied/observed history
Responsibility ≠ Authority
```

Risk materialization preserves the Risk and links an Issue. Accepted material Risk records applicable decision/authority and review trigger.

## Project Health and Review Cadence

`03 Current State` may summarize applicable dimensions:

```text
Scope
Progress / Schedule
Risk
Quality / Validation
Dependencies
Authority
Knowledge
Readiness
Technical / Deployment when applicable
```

Use `GREEN / AMBER / RED / UNKNOWN`, each with Reason, supporting Stable IDs/evidence, Owner, Last Reviewed, Next Review/Trigger. Omit non-applicable optional dimensions rather than marking them GREEN. Do not invent an opaque automatic aggregate score.

Review Cadence modes:

```text
TIME_BASED
EVENT_BASED
```

Cadence may cover Current State, Risk, Assumption, Milestone/Outcome, Decision Revalidation, Technical Design, Deployment Readiness, and Handoff Refresh. Framework semantics do not create a scheduler/reminder runtime.

## Decision Revalidation

`DEC-*` remains canonical in `04`. When material, record:

```text
Validity Basis
Review Trigger
Review By
Last Revalidated
Revalidation Status
Revalidation Evidence
```

Use `NOT_DUE / REVIEW_DUE / REVALIDATED / SUPERSEDED`. Revalidate when the stated basis changes, including invalidated assumptions, changed dependencies/requirements/Tech Stack/deployment mode, approved material Change Request, external change, review date, or contradicting runtime evidence.

## Responsibility and Authority

`11 Actor Registry` may contain scope-keyed `Responsible / Accountable / Consulted / Informed` mapping. It grants no authorization. Actual permission remains in `12 Authorization Registry` through `AUTH-* / DEL-*` plus risk/approval rules.

## Knowledge Debt

Material stale/missing operational knowledge remains canonical in `08 Open Issues`:

```text
ISS-* with issue_type: KNOWLEDGE_DEBT
```

Runtime success does not erase Knowledge Debt. If material it may degrade Knowledge/Readiness and makes `08` applicable if no active `08` exists.

## Technical Blueprint Boundary

### `40 Technical Design`

Use when deeper technical detail is needed beyond `06 Architecture`. Document material Tech Stack entries with Technology, Role/Responsibility, Version/Supported Range, Required/Optional state, reason/Decision reference, component usage, operational dependency, lifecycle/support constraint, replacement boundary, and epistemic/verification state.

May also document component interfaces, source-area responsibilities, Configuration Contract, Runtime Requirements, deployment-mode architecture, and parity/variance.

### `60 Deployment Plan`

Use when install/deployment/operation is in scope. Deployment support vocabulary:

```text
SOURCE_ONLY
DOCKER_ONLY
SOURCE_AND_DOCKER
NOT_APPLICABLE
```

For `SOURCE_AND_DOCKER`, preserve one declared application/configuration/data/security/persistence contract. Intentional differences are explicit Deployment Mode Variance; unexpected mismatch is `DRIFT-*`.

`60` may document prerequisites, Source installation, Docker installation, configuration/secret refs, data initialization, start/stop, health verification, logs, upgrade, rollback, backup/restore, cleanup, troubleshooting. A real Project may include concrete commands/paths only when verified as actual Project truth.

**Planning is not implementation authorization:** a request to define Tech Stack, installation, Docker topology, ports/volumes, or verification does not authorize creation of source code, Dockerfile, Compose/Kubernetes/Helm, package manifests, install scripts, CI, or automation.

## Materialized Current State Invariant

Every referenced current Stable ID must resolve from Current Reconstructable Snapshot to current authoritative semantics without archive traversal. Archive is Historical Truth only. Delta-only shorthand cannot substitute for current payload.

This applies equally to current `DEC-*`, `REQ-*`, and `RISK/ASM/MS/OUT/DEP/CR/GATE` records. Active `40`, `60`, `91` required to interpret current truth belong in `14 Manifest` and `CURRENT` export.

## Migration Safety

Existing Projects never auto-upgrade.

For Framework `1.2.0` migration:

- if Brownfield slot `91` is already occupied, open `MIG-*`, preserve identity/history/references, relocate only with approval, then activate standard `91` when applicable;
- never automatically convert old prose into new management Stable IDs; promotion requires sufficient current semantics, status, ownership, and evidence/epistemic state;
- preserve local Project-specific rules unless explicitly resolved otherwise.

## Golden Reference

`examples/golden-reference-software-project/Project-Source/` is a synthetic composition example. It illustrates `00–17 + 40 + 60 + 91`, management objects, Health/Review Cadence, Tech Stack, `SOURCE_AND_DOCKER`, installation/operations blueprints, migration safety, and handoff.

It is **illustrative, not normative**. Core Governance/templates win on conflict. It contains no actual application code, Dockerfile/Compose, install scripts, CI, binary/runtime artifact, or real secret.

## MCP Material Persistence and Chat Lifecycle

Connector activity is classified as **Material Project Work** or **Transient MCP Activity**. Chat is temporary interaction/execution state, not canonical Project memory merely because MCP/connectors are available.

Operational sequence:

1. Inspect/read/search as needed; keep intermediate connector detail transient.
2. Classify the outcome as Material Project Work or Transient MCP Activity.
3. If Material, determine the source-native canonical owner.
4. Batch related connector activity until a Logical Checkpoint.
5. Persist current usable state/pointers once at the checkpoint.
6. If persistence fails, report `PERSISTENCE_PENDING` and identify what remains unpersisted.
7. Return a compact Chat result; do not replay the connector transcript.
8. Recommend exactly `CONTINUE_CURRENT_CHAT` or `START_NEW_CHAT`.
9. Recommend `START_NEW_CHAT` only after the persistence gate passes: durable current state, pending/blocker state, Exact Next Action, and Required Read location exist outside Chat.

GitHub routing examples:

```text
03 → current state / current phase / current blocker
04 → DEC-* current decision state
05 → REQ-* current requirement state
08 → ISS-* / DRIFT-* / CONFLICT-* / Knowledge Debt
09 → continuation contract and exact next action
10 → applied/observed historical change
13 → material evidence references
15 → ACT-* current action state
91 → RISK-* / ASM-* / MS-* / OUT-* / DEP-* / CR-* / GATE-*
```

If the natural owner is a normal repository artifact outside Project Source (for example implementation code, README, config, or an approved plan), persist there rather than duplicating the whole state into Project Source. Cross-system GitHub/Drive continuation uses pointers to each source-native owner.

For Google Drive, update the existing designated Project progress `.md` when one already exists. Only when no designated progress Markdown exists and durable continuation state is required, use one stable `PROJECT-PROGRESS.md` as a continuation cache. It references authoritative Drive artifacts and MUST NOT become a duplicate source of truth or MCP transcript.

Do not persist raw tool payloads, long search results, full diffs, repetitive intermediate state, or private intermediate reasoning merely for audit convenience. `09 Handoff` remains a continuation contract, not an execution log. A new chat must be able to continue from persisted state and Required Read pointers without the old transcript.

## Workflow

1. Classify `GREENFIELD`, `BROWNFIELD`, or `IMPORT` and detect whether valid local Project Source already exists.
2. NEW Project: read canonical `main` in governed order: README → descriptor → SKILL → latest amendment → Core Governance → Framework template → skeletons → mockup.
3. Resolve explicit `FAST/GRILL`; otherwise `ADAPTIVE`.
4. Confirm active `FRAMEWORK-001`; if missing in an existing Project, stop affected work and propose governed repair.
5. Existing Project: read `00 → 01 → 03`, follow `01` routing, preserve local pin.
6. Inspect accessible sources before asking; do not ask for facts that can be verified.
7. Classify material claims by Truth Domain, Epistemic Status, Freshness; use DRIFT/CONFLICT instead of silent reconciliation.
8. Initial creation/major structural migration requires Preview → explicit user approval → write.
9. For GREENFIELD create mandatory `00–05`, `09–17`; evaluate `06–08`, `40`, `60`, `91`; keep `18–19` reserved.
10. Route management objects to `91`; technical blueprint to `40`; install/operations to `60` when applicable.
11. Pin imported Framework/Schema locally; upgrades use `MIG-*` and approval.
12. If exact Git provenance is observed/material, record consistently in `00`/`14`; otherwise never fabricate it.
13. Verify referenced current Stable IDs resolve without archive traversal before readiness/CURRENT export claims.
14. Never store actual secrets; use `SECRET-*` metadata references only.
15. Preserve history and finish with completion/readiness/exact-next-action summary.

## Quick Reference

| Situation | Required behavior |
|---|---|
| New Project | canonical main → Preview → approval → mandatory core; conditionals only when applicable |
| Project-management control | use `91`; canonical `RISK/ASM/MS/OUT/DEP/CR/GATE` |
| Technical design | use `40` when deeper than `06`; document blueprint, do not silently code |
| Install/deployment | use `60`; support Source/Docker model and resulting-state verification |
| Source + Docker | shared contract + explicit variance; unexpected mismatch = DRIFT |
| Project Health | dimensional `GREEN/AMBER/RED/UNKNOWN` in `03`, evidence-backed |
| Decision changed basis | mark/review revalidation in `04` |
| Responsibility | mapping in `11`; permission still comes from `12` |
| Knowledge Debt | `ISS-* issue_type: KNOWLEDGE_DEBT` in `08` |
| Existing custom slot 91 | `MIG-*`; never overwrite; approved relocation first |
| Old free text | never auto-promote into new Stable IDs |
| Exact Git provenance unavailable | normal bootstrap continues if canonical source accessible; never fabricate |
| Material MCP work | batch to Logical Checkpoint; persist usable state/pointers to source-native owner; compact Chat result |
| Persistence failure / chat switch | `PERSISTENCE_PENDING` → `CONTINUE_CURRENT_CHAT`; `START_NEW_CHAT` only after durable continuation state exists |
| Handoff | authority does not transfer |
| R2/R3 mutation | fresh authority + required postflight/evidence |

## Red Flags

- removing/bypassing/demoting `FRAMEWORK-001`;
- creating empty conditional `06–08`, `40`, `60`, `91` merely for completeness;
- materializing reserved `18–19`;
- storing `RISK/ASM/MS/OUT/DEP/CR/GATE` as authoritative current truth outside `91`;
- treating Action completion as Milestone/Outcome success;
- treating responsibility as authority;
- hiding material Knowledge Debt because runtime works;
- overwriting a Brownfield custom slot `91`;
- auto-promoting old prose into Stable IDs;
- Source/Docker divergence without declared variance or DRIFT;
- turning Tech Stack/install/Docker planning into unrequested source code/Dockerfile/Compose/scripts/CI/automation;
- reconstructing inaccessible Framework/project facts from memory;
- archive-dependent Current Truth;
- guessing facts/secrets/provenance;
- claiming completion without risk-appropriate verification.
