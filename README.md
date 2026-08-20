# ProjectFramework

`captainhuke-dev/ProjectFramework` is the **canonical public upstream bootstrap source for new Project Source creation**. The `main` branch represents the current approved starting Framework for NEW projects.

## Current Release

- Project Source Framework: **1.1.5**
- Project Source Schema: **1.0.0**
- Distributable package root: `managing-project-source/`
- Release descriptor: `managing-project-source/FRAMEWORK-RELEASE.yaml`

## Framework Intent

ProjectFramework is a **conceptual Project governance and planning framework**. It defines how a Project should represent current truth, authority, requirements, decisions, evidence, handoff, migration, semantic slots, readiness, and continuation context across agents.

It is intentionally **documentation/governance first**. Integrity rules are semantic contracts that a human or Agent can evaluate from the Framework sources. They do not imply that this repository must contain a validator, CLI, GitHub Actions workflow, migration engine, background automation, or other enforcement software.

Executable enforcement tooling is a separate implementation scope and is added only when explicitly requested.

## Operational Use vs Optional Release Assurance

Framework usability and repository/release assurance are separate dimensions:

```text
OPERATIONALLY_USABLE
REPRODUCIBLY_RELEASED
REPOSITORY_HARDENED
```

- **OPERATIONALLY_USABLE** — the Framework can correctly bootstrap and govern a Project.
- **REPRODUCIBLY_RELEASED** — optional assurance that an immutable source identity such as a Git tag/commit was preserved.
- **REPOSITORY_HARDENED** — optional assurance such as branch protection or repository rulesets.

A Framework may be operationally usable without an immutable tag, exact commit provenance, or branch protection. Those assurance gaps may be reported, but they are **not prerequisites for normal bootstrap** unless a Project-Specific Rule explicitly requires them.

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
8. Create active `00-Project Source Framework` first, then mandatory `01–05` and `09–17`; evaluate conditional `06–08`; do not materialize reserved `18–19`.
9. Pin the imported Framework/Schema locally. The repository is not a live dependency after bootstrap.
10. If exact Git tag/SHA provenance is actually observed and useful, record it. If it is unavailable, do not invent it and do not block otherwise valid bootstrap solely for that reason.

## Existing Projects

Existing projects **do not auto-upgrade** when this repository changes. Their project-local approved Framework/Schema pins remain authoritative. Upgrade to a newer Framework uses the governed `MIG-*` assessment, explicit approval, validation, promotion, supersede/archive, and postflight process defined by the Project Source Framework.

## Concept-First Integrity Contract

At minimum, Framework integrity means:

- current Framework/Schema declarations agree across current distribution artifacts;
- semantic slots `00–17` retain their governed meanings;
- `06–08` remain **CONDITIONAL**;
- `18–19` remain **RESERVED**;
- ChatGPT and Claude shared governance semantics remain equivalent;
- active/current Stable IDs resolve without archive dependency;
- existing Projects never silently auto-upgrade;
- platform launchers never override active local `FRAMEWORK-001`;
- missing facts, authority, source, or provenance are never fabricated.

These requirements may be reviewed manually or by an Agent. **The existence of an Integrity Contract is not authorization to build enforcement software.**

## Optional Source Provenance

`FRAMEWORK-RELEASE.yaml` identifies the canonical repository and bootstrap branch. Exact Git provenance is enhanced assurance, not a bootstrap prerequisite.

When exact provenance is actually observed, a Project may record values such as source ref/tag and resolved commit SHA. When it is not observed, use an explicit state such as `UNKNOWN` / `UNVERIFIED` if provenance tracking is material. Never fabricate or retroactively backfill an unobserved Git identity merely to make records look complete.

## Bootstrap Mockup

`templates/project-source-mockup/` is the concrete starter representation of the Project Source namespace. It shows which semantic slot maps to which document, supplies `.template.md` starter files for slots `00–17`, and documents the extended `20–99` taxonomy.

The mockup is **executable documentation, not normative authority**. `references/core-governance-rules.md` remains authoritative if a mismatch appears. The presence of a conditional template does not mean an active project must create that document: `06 Architecture`, `07 Implementation Plan`, and `08 Open Issues` are instantiated only when applicable. Slots `18–19` remain reserved and have no active-document templates.

## Current-Truth Integrity

Active canonical registries are materialized current projections, not delta chains. Current Stable IDs must resolve from the Current Reconstructable Snapshot without requiring archived revisions. Archive remains Historical Truth; it must not become a dependency for determining Current Truth.

## Repository Layout

```text
ProjectFramework/
├── README.md
├── LICENSE
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

Framework `1.1.5` supersedes any interpretation of `1.1.4` that made Git tags, exact commit provenance, branch protection, executable validators, or CI enforcement prerequisites for normal Framework usability. Those mechanisms remain optional assurance or separate explicitly requested implementation scope.
