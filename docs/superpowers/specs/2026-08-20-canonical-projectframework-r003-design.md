# Canonical ProjectFramework r003 Design

## Status

- Design status: APPROVED IN CHAT FOR SPECIFICATION
- Date: 2026-08-20
- Repository: `captainhuke-dev/ProjectFramework`
- Source input: `ProjectSourceFramework-r002-260814-1213.zip`
- Target source package revision: `r003`
- Target Project Source Framework version: `1.1.1`
- Project Source schema version: `1.0.0` (unchanged)

## 1. Purpose

Make the public GitHub repository `captainhuke-dev/ProjectFramework` the canonical upstream bootstrap source for every new Project Source, import the complete r002 framework package without flattening its package root, and incorporate the governance improvement identified during r003 usage: current canonical objects must be resolvable from the current snapshot without depending on archived revisions.

The repository becomes the source to read first when starting a new project. Once a project is created, that project pins its imported Framework/Schema version and does not silently auto-upgrade when the upstream repository changes.

## 2. Existing State

The input ZIP contains this package:

```text
managing-project-source/
├── SKILL.md
├── references/
│   ├── approved-design-spec-historical-260813-2140.md
│   ├── core-governance-rules.md
│   └── framework-governance-amendment-260814-0808.md
├── templates/
│   ├── 00-project-source-framework.md
│   └── core-document-skeletons.md
└── tests/
    └── pressure-scenarios.md
```

The current template pins `project_source_framework_version: "1.1.0"` and `project_source_schema_version: "1.0.0"`.

The GitHub repository currently contains only `LICENSE` and a minimal `README.md` on `main`.

## 3. Repository Architecture

Preserve the package root from the ZIP rather than flattening its contents:

```text
ProjectFramework/
├── README.md
├── LICENSE
├── managing-project-source/
│   ├── SKILL.md
│   ├── references/
│   ├── templates/
│   └── tests/
└── docs/
    └── superpowers/
        └── specs/
```

`managing-project-source/` is the distributable/copyable framework package. `docs/superpowers/specs/` contains repository-development design records and is not part of the Project Source bootstrap package unless explicitly imported.

## 4. Canonical Upstream Bootstrap Contract

The repository `main` branch is the canonical upstream source for **new-project bootstrap**.

For a new project:

1. Read the repository `README.md`.
2. Read `managing-project-source/SKILL.md` and its required references/templates.
3. Bootstrap the new Project Source from the current approved framework on `main`.
4. Record/pin the imported Framework and Schema versions inside that project.

For an existing project:

- Its pinned Framework/Schema remains authoritative.
- A newer upstream repository version does not auto-upgrade that project.
- Upgrade uses the existing governed `MIG-*` assessment, explicit approval, validation, promotion, supersede, and archive flow.

This keeps the upstream repository authoritative for new-project starting source while preserving project-local version pinning and historical reconstructability.

## 5. r003 Governance Improvement

### 5.1 Problem

A later active revision can currently use shorthand such as:

```text
DEC-005 — retain previous status
REQ-008 — retain previous status
```

while the complete semantic record remains only in an archived earlier revision.

History remains preserved, but current truth is no longer self-contained. An agent resolving an active Stable ID may need to inspect archive to know the current Decision or Requirement. This conflicts with the existing model in which:

- canonical object homes contain authoritative objects;
- archive represents historical truth;
- `14-Project Source Manifest` represents the current reconstructable snapshot; and
- `CURRENT` export is intended to support continuation without the full archive.

### 5.2 New Root Invariant — Materialized Current State

Active canonical registries are **materialized current projections, not delta chains**.

For every Stable ID that is active/current and referenced by the current Project Source:

- its current authoritative record MUST resolve from the Current Reconstructable Snapshot;
- the current record MUST contain sufficient current semantic payload to identify what is true now, or link to an active/current canonical Detail Document containing that payload;
- archived revisions MAY provide historical rationale/evolution but MUST NOT be required to resolve current truth;
- phrases such as `retain previous status`, `unchanged from r002`, or `see archived revision` MUST NOT substitute for the authoritative current payload.

This invariant applies to current-state-bearing canonical object homes generally. The r003 templates explicitly clarify it for `DEC-*` and `REQ-*`, where the observed ambiguity occurred.

### 5.3 Archive Independence

Archive is Historical Truth, not a runtime dependency for Current Truth.

A current Stable ID resolver—manual, derived, or future automated—must be able to locate the current authoritative record without traversing archived revisions.

No executable resolver, CLI, validator, migration engine, or automation is added in r003. That remains future scope requiring separate explicit approval.

### 5.4 CURRENT Export Integrity

A `CURRENT` export MUST include the current canonical record and any active Detail Document required to interpret every active Stable ID referenced by the exported snapshot.

It MUST NOT require omitted archive content to determine current Decision/Requirement semantics.

### 5.5 Referential Validation Rule

Add a governance-level validation requirement:

> Every Stable ID referenced from the Active/Current snapshot must resolve to a current authoritative record within the Current Reconstructable Snapshot, without requiring an archived revision.

Failure is a Project Source integrity/readiness defect. Severity depends on operational impact; if an agent cannot determine current truth from the current snapshot, the affected scope is not operationally ready.

## 6. Framework Versioning

Target version:

```text
Project Source Framework: 1.1.0 → 1.1.1
Project Source Schema:    1.0.0 → 1.0.0
```

Rationale: this is a backward-compatible clarification/fix of existing Current Truth, canonical-home, Manifest, archive, and CURRENT-export invariants. It does not require a new mandatory document type or machine schema structure.

The previous `framework-governance-amendment-260814-0808.md` is preserved unchanged as historical approved governance. A new dated amendment for 1.1.1 will be added rather than rewriting the earlier approved amendment.

## 7. Files to Import and Modify

### Import unchanged from r002 initially

- `managing-project-source/references/approved-design-spec-historical-260813-2140.md`

### Import then update for r003

- `managing-project-source/SKILL.md`
  - point required reading to the latest 1.1.1 amendment;
  - add materialized-current-state / archive-independence red flag and operational rule;
  - preserve the explicit anti-scope-expansion rule against unrequested software tooling.

- `managing-project-source/references/core-governance-rules.md`
  - add Materialized Current State, archive independence, Stable-ID resolvability, and CURRENT export integrity rules.

- `managing-project-source/templates/00-project-source-framework.md`
  - update Framework version to `1.1.1`;
  - add the new root invariant and validation/export implications.

- `managing-project-source/templates/core-document-skeletons.md`
  - update Framework version to `1.1.1`;
  - clarify that Decision and Requirement records in active revisions must contain materialized current semantics, not delta-only placeholders;
  - clarify current Manifest coverage of any required active detail documents.

- `managing-project-source/tests/pressure-scenarios.md`
  - add a pressure scenario where r003 contains `retain previous status` but complete semantics exist only in archived r002;
  - pass condition requires materializing current records or using active Detail Documents;
  - fail condition requires opening archive to resolve current truth.

### Add

- `managing-project-source/references/framework-governance-amendment-260820-0638.md`
  - records the approved 1.1.1 amendment and its compatibility intent.

- root `README.md`
  - declare this public repository as the canonical upstream bootstrap source for new projects;
  - define new-project read order;
  - distinguish new-project bootstrap from existing-project governed upgrades;
  - identify current Framework/Schema versions.

## 8. Git Workflow

Use branch:

```text
framework-r003-materialized-current-state
```

Workflow:

1. Commit this approved design spec.
2. After user review of the committed spec, import r002 and implement r003 changes on the same branch.
3. Verify repository tree and semantic changes.
4. Open a PR to `main` with a concise migration/change summary.
5. Check PR diff and available status checks.
6. Merge to `main` after verification.

No force push to `main`; preserve existing repository history and `LICENSE`.

## 9. Verification Strategy

Verification must include:

1. **Source inventory** — all seven files from the r002 ZIP are represented in the repository package.
2. **Path preservation** — package remains under `managing-project-source/`.
3. **Version scan** — active templates/guidance use Framework `1.1.1`; Schema remains `1.0.0`; intentional historical documents may retain `1.1.0`.
4. **Governance scan** — the new materialized-current-state rule appears consistently in SKILL, Core Governance, Framework template, skeletons, amendment, and pressure test.
5. **No scope expansion** — no executable resolver/CLI/validator/automation files are introduced.
6. **Pressure scenario** — Scenario 9 (or next available number) explicitly rejects archive-dependent current truth.
7. **README bootstrap contract** — clearly states that new projects read/bootstrap from this public repository while existing projects remain version-pinned until approved migration.
8. **PR diff review** — confirm only intended files change and historical approved material is preserved.
9. **GitHub status** — inspect available checks before merge; absence of CI must be reported rather than interpreted as automated validation.

The existing pressure-scenario file notes that this ChatGPT harness cannot run independent fresh-agent GREEN tests. That limitation remains explicit; r003 adds the scenario but does not falsely claim an independent fresh-agent pass.

## 10. Success Criteria

The change is complete when:

- `main` contains the full framework package under `managing-project-source/`;
- root README establishes `captainhuke-dev/ProjectFramework` as canonical upstream bootstrap source for every new project;
- current Framework version is `1.1.1`, Schema remains `1.0.0`;
- Active current records cannot rely on archive-only semantic payload;
- CURRENT snapshot/export can resolve current Stable IDs without the archive;
- no unrequested software resolver/automation has been implemented;
- changes have been reviewed through a PR and merged into `main`.
