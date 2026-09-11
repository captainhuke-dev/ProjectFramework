# Project Bootstrap

This file is the stable Project-root discovery entrypoint for ProjectFramework under ProjectFramework `1.15.0`.

It is a **discovery/locator artifact only**. It is not a Project Source semantic slot, has no Stable ID, and never replaces or overrides active `Project-Source/00` / `FRAMEWORK-001`.

## Canonical Project Source

```text
Project Source Root: Project-Source/
First Read: Project-Source/00-Project-Source-Framework-r003-260911-1459.md
```

Do not infer another Project Source root from recency, search ranking, active workspace IDs, mounts, or similarly named directories.

## Project Settings and README Entry

Project Settings / Project Instructions may use `Project Bootstrap: <VERIFIED_ABSOLUTE_PROJECT_BOOTSTRAP_PATH>` to reach this file. When an environment-specific path is unavailable, this repository's managed README bootstrap block provides the portable fallback `Project Bootstrap: ./PROJECT-BOOTSTRAP.md`.

Project Settings and README are discovery adapters only. They never replace this file, active `FRAMEWORK-001`, Project Location Binding, branch/integration/implementation authority, or `AUTH-*`.

## Required Read Order

```text
PROJECT-BOOTSTRAP.md
→ active 00 / FRAMEWORK-001
→ active 01 / Project Source Index
→ active 03 / Current State
→ task-specific routing from current authoritative sources
→ active 09 / Handoff when continuation/resume is applicable
```

Validate the referenced `00` as active `FRAMEWORK-001`; after validation, active Project Source governs. `01`, `03`, and `09` are resolved from active Project Source routing rather than hard-coded revision pointers here.

## Authority Boundary

```text
PROJECT-BOOTSTRAP.md = discovery/locator only
FRAMEWORK-001        = Project governance authority
Project Location Binding
≠ current branch/worktree
≠ Canonical Integration Target
≠ Canonical Implementation Source
≠ AUTH / Risk authority
```

Correct discovery location grants no permission to mutate, approve Risk, push, deploy, or change bindings.

## Failure Handling

Read-only inspection may continue far enough to diagnose a problem, but affected Material mutation fails closed when the declared Project Source root is missing, the referenced `00` is not valid active `FRAMEWORK-001`, multiple canonical root bootstraps conflict, or this locator materially contradicts active Root/Location Binding. Do not silently choose by recency.

## Safety

Do not store passwords, tokens, access keys, secret-bearing URLs, or other secret values here. Do not persist a concrete current branch/worktree or mutable status as authority; fresh-observe volatile Git state when material.
