# ProjectFramework

`captainhuke-dev/ProjectFramework` is the **canonical public upstream bootstrap source for new Project Source creation**. The `main` branch is the mutable discovery/release branch; reproducible NEW-project bootstrap resolves the stable release reference declared by `managing-project-source/FRAMEWORK-RELEASE.yaml`.

## Current Release

- Project Source Framework: **1.1.4**
- Project Source Schema: **1.0.0**
- Distributable package root: `managing-project-source/`
- Release descriptor: `managing-project-source/FRAMEWORK-RELEASE.yaml`
- Declared stable release tag: `v1.1.4`

The descriptor declares the release tag expected by this distribution. **Do not infer that the Git tag exists merely because it is declared in the file.** Release completion requires the tag to be created after merge and verified to resolve to the exact Framework `1.1.4` release commit.

## Platform Project Instructions

For a platform Project, use the matching canonical bootstrap instruction artifact:

- **ChatGPT Projects:** copy `managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md` into **Project settings → Instructions**.
- **Claude Projects:** copy `managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md` into **Set project instructions**.

The two platform files contain the same shared governance contract. Their platform instructions are **bootstrap/continuation launchers, not a competing governance root**. For a NEW project they route the agent through the release descriptor and immutable bootstrap ref. After a valid local `Project-Source/` is initialized, the locally pinned Project Source becomes authoritative for that project and upstream is not a live replacement.

## Reproducible New-Project Bootstrap

For every NEW Project Source:

1. Start from the matching platform Project instruction artifact when using ChatGPT Projects or Claude Projects.
2. Read this `README.md` from the canonical repository discovery branch.
3. Read `managing-project-source/FRAMEWORK-RELEASE.yaml`.
4. Resolve `stable_release_tag` from the descriptor and verify the tagged source declares the expected Framework/Schema version.
5. Read the bootstrap source at that immutable tagged ref in this order:
   - `managing-project-source/SKILL.md`
   - latest Framework governance amendment
   - `managing-project-source/references/core-governance-rules.md`
   - `managing-project-source/templates/00-project-source-framework.md`
   - `managing-project-source/templates/core-document-skeletons.md`
   - `managing-project-source/templates/project-source-mockup/README.md`
6. Preview the proposed Project Source and obtain explicit user approval before writing.
7. Create active `00-Project Source Framework` first, then mandatory `01–05` and `09–17`; evaluate conditional `06–08`; do not materialize reserved `18–19`.
8. Record the **actually resolved release tag and commit SHA** in local `framework_source_provenance` and corresponding Manifest continuation metadata.
9. Pin the imported Framework/Schema locally. The repository is not a live dependency after bootstrap.

### If the stable tag cannot be resolved

Mutable `main` is **not** equivalent to immutable release provenance. If the declared stable release tag or tagged source cannot be resolved:

- state the access/resolution limitation explicitly;
- do not fabricate an immutable tag or SHA;
- mutable-`main` bootstrap requires explicit user approval;
- record degraded provenance such as `VERIFICATION_REQUIRED` / mutable-source warning until independently verified.

## Existing Projects

Existing projects **do not auto-upgrade** when this repository changes. Their project-local approved Framework/Schema pins remain authoritative. Do not retroactively invent a historical release SHA for an older Project that did not observe one. Upgrade to a newer Framework uses the governed `MIG-*` assessment, explicit approval, validation, promotion, supersede/archive, and postflight process defined by the Project Source Framework.

## Framework 1.1.4 Release Provenance

`FRAMEWORK-RELEASE.yaml` is distribution metadata, not a Project Source semantic document. It declares the canonical repository, release channel, stable tag, entrypoints, latest amendment, and provenance policy. It intentionally does **not** embed the SHA of its own containing release commit; exact commit provenance is recorded by a consuming Project after resolving the Git ref it actually used.

Canonical provenance identity is:

```text
Framework semantic version
+ stable release tag
+ resolved Git commit SHA observed by the consuming Project
```

## Framework 1.1.3 Platform Bootstrap Instructions

`CHATGPT-PROJECT-INSTRUCTIONS.md` and `CLAUDE-PROJECT-INSTRUCTIONS.md` are official distribution entrypoints for platform Projects. They share a byte-identical governance core between explicit shared-contract markers so platform wrappers cannot silently diverge on bootstrap, local authority, migration, or scope rules.

If required upstream/local Project Source content cannot be accessed, the platform instruction contract requires the agent to state the limitation and stop the affected governance mutation rather than reconstruct Framework rules or project facts from memory.

## Framework 1.1.2 Bootstrap Mockup

`templates/project-source-mockup/` is the concrete starter representation of the Project Source namespace. It shows which semantic slot maps to which document, supplies `.template.md` starter files for slots `00–17`, and documents the extended `20–99` taxonomy.

The mockup is **executable documentation, not normative authority**. `references/core-governance-rules.md` remains authoritative if a mismatch ever appears. The presence of a conditional template does not mean an active project must create that document: `06 Architecture`, `07 Implementation Plan`, and `08 Open Issues` are instantiated only when applicable. Slots `18–19` remain reserved and have no active-document templates.

## Framework 1.1.1 Integrity Clarification

Active canonical registries are materialized current projections, not delta chains. Current Stable IDs must resolve from the Current Reconstructable Snapshot without requiring archived revisions. Archive remains Historical Truth; it must not become a dependency for determining Current Truth.

Framework `1.1.4` still does not add the Phase-B Framework integrity validator, GitHub Actions enforcement, Golden Reference Project, or fresh-agent certification claim. Those remain separate later phases.

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
