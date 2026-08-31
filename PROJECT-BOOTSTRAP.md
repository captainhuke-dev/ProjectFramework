# Project Bootstrap

This file is the stable Project-root discovery entrypoint for Projects created or upgraded to ProjectFramework `1.7.0+`.

It is a **discovery/locator artifact only**. It is not a Project Source semantic slot, has no Stable ID, and never replaces or overrides active `Project-Source/00` / `FRAMEWORK-001`.

## Canonical Project Source

```text
Project Source Root: Project-Source/
First Read: Project-Source/00-Project-Source-Framework-r002-260829-1901.md
```

If this Project uses a different approved relative Project Source path, replace the two values above during governed creation/upgrade. Do not infer a different path from recency, search ranking, active workspace IDs, mounts, or similarly named directories.

## Active Project Source Files

```text
00 / FRAMEWORK-001 -> Project-Source/00-Project-Source-Framework-r002-260829-1901.md
01 / Project Source Index -> Project-Source/01-Project-Source-Index-r022-260831-2130.md
03 / Current State -> Project-Source/03-Current-State-r022-260831-2130.md
09 / Handoff -> Project-Source/09-Handoff-r022-260831-2130.md
```

## Required Read Order

Once the Project root is accessible:

```text
PROJECT-BOOTSTRAP.md
→ 00 / FRAMEWORK-001
→ 01 / Project Source Index
→ 03 / Current State
→ task-specific routing from current authoritative sources
→ 09 / Handoff when continuation/resume is applicable
```

Validate the referenced `00` as the active `FRAMEWORK-001` for this Project before treating it as governance authority. After that validation, active Project Source governs.

## Authority Boundary

Keep these concepts separate:

```text
PROJECT-BOOTSTRAP.md = discovery/locator only
FRAMEWORK-001        = Project governance authority
Project Location Binding
≠ current branch/worktree
≠ Canonical Integration Target
≠ Canonical Implementation Source
≠ Runtime Location
≠ AUTH / Risk authority
```

Correct discovery location grants no permission to mutate, approve Risk, push, deploy, or change bindings.

## Failure Handling

Read-only inspection may continue far enough to diagnose a problem, but affected Material mutation fails closed when:

- the declared Project Source root is missing;
- the referenced `00` is not a valid active `FRAMEWORK-001` for this Project;
- multiple root bootstrap locations claim canonical status;
- this locator materially contradicts the active root binding;
- a vendor adapter or optional `PROJECT-CONFIG.md` materially conflicts with resolved active Project Source.

Do not silently rewrite either side and do not choose by recency.

## GREENFIELD / Brownfield

- **NEW Framework `1.7.0+` Project:** this root file is mandatory in the resulting approved Project.
- **Existing initialized Project:** do not create or update this file automatically. Adopt it only through governed `[Project Upgrade]` or another explicitly authorized root migration/repair flow.

## Optional Adapters and Location Reference

ChatGPT Project Settings, Claude Project Settings, `AGENTS.md`, `CLAUDE.md`, and similar vendor surfaces may point here as optional thin discovery adapters. They are not Project authority.

`PROJECT-CONFIG.md`, when present, remains an optional Bootstrap Location reference only. It does not replace this root discovery entrypoint or active `FRAMEWORK-001`.

## Safety

Do not store passwords, tokens, access keys, secret-bearing URLs, or other secret values here. Do not persist a concrete current branch/worktree, runtime endpoint, or mutable status as authority; fresh-observe volatile state from its canonical source when material.
