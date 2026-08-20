# ProjectFramework

`captainhuke-dev/ProjectFramework` is the **canonical public upstream bootstrap source for new Project Source creation**. The `main` branch represents the current approved starting Framework for new projects.

## Current Release

- Project Source Framework: **1.1.2**
- Project Source Schema: **1.0.0**
- Distributable package root: `managing-project-source/`

## New-Project Bootstrap Read Order

For every new Project Source:

1. Read this `README.md`.
2. Read `managing-project-source/SKILL.md`.
3. Read the references/templates required by that skill, especially the latest Framework governance amendment, Core Governance Rules, `templates/00-project-source-framework.md`, `templates/core-document-skeletons.md`, and `templates/project-source-mockup/README.md`.
4. Use the mockup template set to understand the `00–17` semantic-slot layout; instantiate mandatory documents, evaluate conditional `06–08`, and do not materialize reserved `18–19`.
5. Bootstrap the new Project Source from the current approved Framework on `main`.
6. Record and pin the imported Project Source Framework and Schema versions inside the new project.

The repository is the upstream **starting source**, not a live dependency after project creation.

## Existing Projects

Existing projects **do not auto-upgrade** when this repository changes. Their project-local approved Framework/Schema pins remain authoritative. Upgrade to a newer Framework uses the governed `MIG-*` assessment, explicit approval, validation, promotion, supersede/archive, and postflight process defined by the Project Source Framework.


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
