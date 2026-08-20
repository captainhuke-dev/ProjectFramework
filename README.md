# ProjectFramework

`captainhuke-dev/ProjectFramework` is the **canonical public upstream bootstrap source for new Project Source creation**. The `main` branch represents the current approved starting Framework for NEW projects.

## Current Release

- Project Source Framework: **1.2.0**
- Project Source Schema: **1.0.0**
- Distributable package root: `managing-project-source/`
- Release descriptor: `managing-project-source/FRAMEWORK-RELEASE.yaml`

## Framework Intent

ProjectFramework is a **conceptual Project governance and planning framework**. It defines how a Project should represent current truth, authority, requirements, decisions, evidence, risks, assumptions, milestones, outcomes, dependencies, change control, handoff, migration, technical blueprint, installation/deployment knowledge, readiness, and continuation context across agents.

It is intentionally **documentation/governance first**. Integrity and technical rules are semantic contracts that a Human/Agent can evaluate from Framework sources. They do not imply that this repository must contain application code, a validator, CLI, Docker runtime artifacts, CI/CD, migration engine, scheduler, background automation, or other enforcement software.

Executable implementation remains a separate explicit scope.

## Operational Use vs Optional Release Assurance

Framework usability and repository/release assurance are independent dimensions:

```text
OPERATIONALLY_USABLE
REPRODUCIBLY_RELEASED
REPOSITORY_HARDENED
```

- **OPERATIONALLY_USABLE** — the Framework can correctly bootstrap and govern a Project.
- **REPRODUCIBLY_RELEASED** — optional assurance that an immutable source identity such as a Git tag/commit was preserved.
- **REPOSITORY_HARDENED** — optional assurance such as branch protection or repository rulesets.

A Framework may be operationally usable without an immutable tag, exact commit provenance, or branch protection. Those assurance gaps are not prerequisites for normal bootstrap unless a Project-Specific Rule explicitly requires them.

## Framework 1.2.0 Additions

Framework `1.2.0` adds three standard **conditional** extended documents:

```text
40 Technical Design              CONDITIONAL
60 Deployment Plan               CONDITIONAL
91 Project Management Control    CONDITIONAL / STANDARD IN 1.2.0+
```

### 91 — Project Management Control

`91` is the canonical home for:

```text
RISK-*   Risk
ASM-*    Assumption
MS-*     Milestone
OUT-*    Outcome
DEP-*    Dependency
CR-*     Change Request
GATE-*   Review / Phase Gate
```

It supports explicit Risk/Assumption management, Milestone vs Outcome distinction, dependency control, scope/change assessment, and review gates without changing the mandatory core `00–17` set.

### 40 — Technical Design

`40` is the deeper technical blueprint for Projects with meaningful software/technical implementation. It may document:

```text
Tech Stack
system/component responsibilities
interfaces and dependencies
source-structure responsibilities
configuration contract
runtime requirements
Source/Docker architecture
Source/Docker parity and variance
```

It does **not** authorize creation of application source code, Dockerfile, Compose/Kubernetes/Helm artifacts, scripts, CI, or automation.

### 60 — Deployment Plan

`60` is the installation/operations blueprint. It may document:

```text
prerequisites
Source installation
Docker installation
configuration and secret references
startup / shutdown
verification / health
logs / diagnostics
upgrade / rollback
backup / restore
cleanup / troubleshooting
```

A real Project may record concrete commands/paths in `60` when they are verified Project truth. ProjectFramework itself does not invent executable commands for nonexistent software.

### Deployment Support Vocabulary

Software Projects may declare:

```text
SOURCE_ONLY
DOCKER_ONLY
SOURCE_AND_DOCKER
NOT_APPLICABLE
```

`SOURCE_AND_DOCKER` requires one declared application/configuration/data/security/persistence contract. Intentional differences must be explicit Deployment Mode Variance; unexpected differences are `DRIFT-*`.

## Project Operating Model

Framework `1.2.0` also adds:

- multi-dimensional Project Health in `03 Current State` using `GREEN / AMBER / RED / UNKNOWN` with reason/evidence;
- `TIME_BASED` and `EVENT_BASED` review cadence semantics without creating a scheduler;
- Decision Revalidation fields in `04 Decision Log`;
- Responsibility Mapping in `11 Actor Registry` while preserving **Responsibility ≠ Authority**;
- `ISS-* issue_type: KNOWLEDGE_DEBT` in `08 Open Issues` for material stale/missing operational knowledge.

## Platform Project Instructions

For a platform Project, use the matching canonical bootstrap instruction artifact:

- **ChatGPT Projects:** copy `managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md` into **Project settings → Instructions**.
- **Claude Projects:** copy `managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md` into **Set project instructions**.

The two platform files contain the same shared governance contract. They are **bootstrap/continuation launchers, not competing governance roots**. After a valid local `Project-Source/` is initialized, the locally pinned Project Source becomes authoritative for that Project.

## New-Project Bootstrap Read Order

For every NEW Project Source:

1. Start from the matching platform Project instruction artifact when using ChatGPT Projects or Claude Projects.
2. Read this `README.md` from canonical repository `main`.
3. Read `managing-project-source/FRAMEWORK-RELEASE.yaml`.
4. Read `managing-project-source/SKILL.md`.
5. Read the latest Framework governance amendment and `managing-project-source/references/core-governance-rules.md`.
6. Read `managing-project-source/templates/00-project-source-framework.md`, `templates/core-document-skeletons.md`, and `templates/project-source-mockup/README.md`.
7. Preview the proposed Project Source and obtain explicit user approval before writing.
8. Create active `00-Project Source Framework` first, then mandatory `01–05` and `09–17`.
9. Evaluate `06–08`, `40`, `60`, and `91` by applicability; do not create empty conditional documents merely to make a tree look complete.
10. Keep `18–19` reserved; use `92–99` as Project-specific/Governance Extension space unless a later Framework revision governs them otherwise.
11. Pin the imported Framework/Schema locally. The repository is not a live dependency after bootstrap.
12. If exact Git tag/SHA provenance is actually observed and useful, record it. If unavailable, do not invent it and do not block otherwise valid bootstrap solely for that reason.

## Existing Projects and Migration Safety

Existing Projects **do not auto-upgrade** when this repository changes. Their project-local approved Framework/Schema pins remain authoritative. Upgrade to Framework `1.2.0` uses governed `MIG-*` assessment, explicit approval, validation, promotion, supersede/archive, and postflight.

A Brownfield Project may already use semantic slot `91` for a custom document. Framework `1.2.0` must not overwrite it: assess through `MIG-*`, preserve identity/history/references, relocate only with approval, then activate standard `91` if applicable.

Old free-text notes are not automatically converted into new `RISK-*`, `ASM-*`, `MS-*`, `OUT-*`, `DEP-*`, `CR-*`, or `GATE-*` objects. Promotion requires sufficient current semantics, ownership, status, and epistemic/evidence state.

## Concept-First Integrity Contract

At minimum, Framework integrity means:

- current Framework/Schema declarations agree across current distribution artifacts;
- semantic slots `00–17` retain their governed meanings;
- `06–08` remain **CONDITIONAL**;
- `18–19` remain **RESERVED**;
- `40`, `60`, and `91` are applicability-driven conditional documents;
- `91` owns `RISK / ASM / MS / OUT / DEP / CR / GATE` current records;
- `92–99` remain extension space unless governed otherwise;
- ChatGPT and Claude shared governance semantics remain equivalent;
- active/current Stable IDs resolve without archive dependency;
- existing Projects never silently auto-upgrade;
- platform launchers never override active local `FRAMEWORK-001`;
- missing facts, authority, source, or provenance are never fabricated.

These requirements may be reviewed manually or by an Agent. **The existence of an Integrity Contract is not authorization to build enforcement software.**

## Optional Source Provenance

`FRAMEWORK-RELEASE.yaml` identifies the canonical repository and bootstrap branch. Exact Git provenance is enhanced assurance, not a bootstrap prerequisite.

When exact provenance is actually observed, a Project may record source ref/tag and resolved commit SHA. When it is not observed, use an explicit `UNKNOWN` / `UNVERIFIED` state only when provenance tracking is material. Never fabricate or retroactively backfill an unobserved Git identity merely to make records look complete.

## Bootstrap Mockup

`templates/project-source-mockup/` is the concrete starter representation of the Project Source namespace. It contains `.template.md` starters for `00–17` and Framework `1.2.0` conditional starters for `40`, `60`, and `91`.

The mockup is **executable documentation, not normative authority**. `references/core-governance-rules.md` remains authoritative if a mismatch appears. The presence of a conditional template does not mean an active Project must create that document.

## Golden Reference

Framework `1.2.0` includes a synthetic composition example at:

```text
examples/golden-reference-software-project/Project-Source/
```

It demonstrates `00–17 + 40 + 60 + 91`, Project Health, management-control objects, a fictional Tech Stack, `SOURCE_AND_DOCKER`, parity/variance, installation/operations blueprint, migration safety, and handoff. It contains **no application code, Dockerfile, Compose, install script, CI workflow, binary/runtime artifact, or real secret**.

The Golden Reference is illustrative only. Core Governance, active Framework, templates, and Project-specific approved truth remain authoritative over the example.

## Current-Truth Integrity

Active canonical registries are materialized current projections, not delta chains. Current Stable IDs must resolve from the Current Reconstructable Snapshot without requiring archived revisions. Archive remains Historical Truth; it must not become a dependency for determining Current Truth.

## Repository Layout

```text
ProjectFramework/
├── README.md
├── LICENSE
├── examples/
│   └── golden-reference-software-project/
│       └── Project-Source/
├── managing-project-source/
│   ├── FRAMEWORK-RELEASE.yaml
│   ├── CHATGPT-PROJECT-INSTRUCTIONS.md
│   ├── CLAUDE-PROJECT-INSTRUCTIONS.md
│   ├── SKILL.md
│   ├── references/
│   ├── templates/
│   │   └── project-source-mockup/
│   └── tests/
└── docs/
    └── superpowers/
        ├── specs/
        └── plans/
```

Use `managing-project-source/` as the reusable framework package. Files under `docs/superpowers/` document development of this repository and are not automatically copied into each Project Source.

## Supersession Note

Framework `1.2.0` extends the concept-first direction established in `1.1.5`. Git tags, exact commit provenance, branch protection, executable validators, and CI enforcement remain optional assurance or separate explicitly requested implementation scope rather than prerequisites for normal Framework usability.
