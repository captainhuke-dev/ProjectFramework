# ProjectFramework

`captainhuke-dev/ProjectFramework` is the **canonical public upstream bootstrap source for new Project Source creation**. The `main` branch represents the current approved starting Framework for new projects.

## Current Release

- Project Source Framework: **1.1.3**
- Project Source Schema: **1.0.0**
- Distributable package root: `managing-project-source/`

## Platform Project Instructions

For a platform Project, use the matching canonical bootstrap instruction artifact:

- **ChatGPT Projects:** copy `managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md` into **Project settings → Instructions**.
- **Claude Projects:** copy `managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md` into **Set project instructions**.

The two platform files contain the same shared governance contract. Their platform instructions are **bootstrap/continuation launchers, not a competing governance root**. For a NEW project they route the agent to this repository. After a valid local `Project-Source/` is initialized, the locally pinned Project Source becomes authoritative for that project and upstream `main` is not a live replacement.

## New-Project Bootstrap Read Order

For every new Project Source:

1. Start from the matching platform Project instruction artifact when using ChatGPT Projects or Claude Projects.
2. Read this `README.md`.
3. Read `managing-project-source/SKILL.md`.
4. Read the references/templates required by that skill, especially the latest Framework governance amendment, Core Governance Rules, `templates/00-project-source-framework.md`, `templates/core-document-skeletons.md`, and `templates/project-source-mockup/README.md`.
5. Use the mockup template set to understand the `00–17` semantic-slot layout; instantiate mandatory documents, evaluate conditional `06–08`, and do not materialize reserved `18–19`.
6. Bootstrap the new Project Source from the current approved Framework on `main`.
7. Record and pin the imported Project Source Framework and Schema versions inside the new project.

The repository is the upstream **starting source**, not a live dependency after project creation.

## Existing Projects

Existing projects **do not auto-upgrade** when this repository changes. Their project-local approved Framework/Schema pins remain authoritative. Upgrade to a newer Framework uses the governed `MIG-*` assessment, explicit approval, validation, promotion, supersede/archive, and postflight process defined by the Project Source Framework.

## Framework 1.1.3 Platform Bootstrap Instructions

`CHATGPT-PROJECT-INSTRUCTIONS.md` and `CLAUDE-PROJECT-INSTRUCTIONS.md` are official distribution entrypoints for platform Projects. They share a byte-identical governance core between explicit shared-contract markers so platform wrappers cannot silently diverge on bootstrap, local authority, migration, or scope rules.

If the required upstream repository or local Project Source cannot be accessed, the platform instruction contract requires the agent to state the limitation and stop the affected governance mutation rather than reconstruct Framework rules or project facts from memory.

## Framework 1.1.2 Bootstrap Mockup

`templates/project-source-mockup/` is the concrete starter representation of the Project Source namespace. It shows which semantic slot maps to which document, supplies `.template.md` starter files for slots `00–17`, and documents the extended `20–99` taxonomy.

The mockup is **executable documentation, not normative authority**. `references/core-governance-rules.md` remains authoritative if a mismatch ever appears. The presence of a conditional template does not mean an active project must create that document: `06 Architecture`, `07 Implementation Plan`, and `08 Open Issues` are instantiated only when applicable. Slots `18–19` remain reserved and have no active-document templates.

## Framework 1.1.1 Integrity Clarification

Active canonical registries are materialized current projections, not delta chains. Current Stable IDs must resolve from the Current Reconstructable Snapshot without requiring archived revisions. Archive remains Historical Truth; it must not become a dependency for determining Current Truth.

This release intentionally does not add an executable Stable-ID resolver, CLI, validator, migration engine, or automation.

## Repository Layout

```text
ProjectFramework/
├── README.md
├── LICENSE
├── managing-project-source/
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
