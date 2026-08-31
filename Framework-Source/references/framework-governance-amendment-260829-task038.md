---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.7.0"
project_source_framework_version: "1.8.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_EXPLICIT_CONTINUOUS_APPROVAL_2026-08-29"
compatibility: "BACKWARD_COMPATIBLE_PROJECT_PIN_WITH_UPSTREAM_DISTRIBUTION_ROOT_MIGRATION"
---

# Framework 1.8.0 Amendment — Framework Source Distribution-Root Migration

Framework `1.8.0` preserves Framework `1.7.0` semantics unless refined here. Project Source Schema remains `1.0.0`; release format remains `3`. This amendment changes the canonical reusable Framework distribution directory from `managing-project-source/` to `Framework-Source/` and makes the distinction from Project-specific `Project-Source/` explicit.

## 1. Canonical distribution root

The canonical reusable Framework distribution root is exactly:

```text
Framework-Source/
```

`managing-project-source/` is the historical pre-1.8.0 root name. Framework `1.8.0` does not maintain it as a live alias, duplicate distribution tree, symlink, or fallback root.

## 2. Framework Source versus Project Source

The two roots have distinct roles:

```text
Framework-Source/ = reusable Framework distribution / upstream read-through source
Project-Source/   = authoritative governance/current truth for one initialized Project
```

Access to `Framework-Source/` grants no Project mutation, approval, binding, Risk, implementation, integration, runtime, or persistent-state authority. A newer Framework distribution does not silently override an initialized Project's active local `Project-Source/00 / FRAMEWORK-001` pin.

## 3. Project-root bootstrap remains Project-facing

Framework `1.7.0` self-bootstrap semantics remain unchanged. A deployed `<Project-Root>/PROJECT-BOOTSTRAP.md` continues to route:

```text
PROJECT-BOOTSTRAP.md
→ Project-Source/00 / FRAMEWORK-001
→ Project-Source/01
→ Project-Source/03
→ task-specific routing
→ Project-Source/09 when continuation applies
```

The maintained template now resides at `Framework-Source/templates/PROJECT-BOOTSTRAP.md`, but the deployed root file remains a locator for Project Source, not Framework distribution authority.

## 4. Current versus historical path references

Current mutable Framework routing, README guidance, launchers, release metadata, maintained starters, and current Project truth that answer where the reusable Framework lives now use `Framework-Source/`.

Historical amendments, completed specs/plans/evidence, archived Project Source revisions, and capture-time evidence may retain `managing-project-source/` when that path was true at the recorded time. Migration verification classifies remaining old-path strings by role rather than requiring zero textual matches.

Historical content MUST NOT be cosmetically rewritten merely to match the current directory name.

## 5. Brownfield and external compatibility

Existing initialized Projects remain locally pinned and are not automatically rewritten because upstream `main` changes its distribution directory. Adoption of Framework `1.8.0` remains governed through `[Project Upgrade]` / Direct-to-Latest assessment and normal approval/migration rules.

External scripts, bookmarks, deep links, vendor settings, or tooling that hard-code the old upstream path may require explicit update. The Framework does not infer authority to mutate those external consumers and provides no old-root live alias as fallback.

## 6. ProjectFramework self-governance boundary

ProjectFramework's own repository may reconcile current Project Source statements that reference the reusable distribution path through governed Project Source revisions and `MIG-*`/evidence/history records. That repository-path reconciliation does not by itself upgrade ProjectFramework's active local `FRAMEWORK-001` pin from `1.7.0` to `1.8.0`.

Project Location Binding, `project_uuid`, current branch/worktree, Canonical Integration Target, Canonical Implementation Source, Runtime authority, and File Storage authority remain distinct from the Framework distribution directory name.

## 7. Release and starter behavior

Framework `1.8.0` current maintained distribution surfaces use the `Framework-Source/` repository root and carry Framework `1.8.0` / Schema `1.0.0` release identity. Existing semantic slots and Stable-ID families are unchanged; `18–19` remain RESERVED.

The directory migration adds no `GOAL-*` family, no new Project Source slot, no daemon, no filesystem redirect runtime, no CI/CD automation, and no external consumer rewrite engine.

## 8. Verification and failure behavior

Affected mutation fails closed when current Framework routing still resolves the old distribution path, when both old and new roots claim canonical status, when Project bootstrap is repointed to Framework distribution, when historical provenance would be destroyed by cosmetic rewriting, or when an initialized Project is silently upgraded as a side effect of the upstream rename.

Verification must preserve selected historical blob identities, confirm one live `Framework-Source/` root, confirm no live `managing-project-source/` alias, confirm current routing uses the new root, confirm `PROJECT-BOOTSTRAP.md` still enters active Project Source, and distinguish historical old-path text from stale current truth.

## 9. TASK-039 sequencing

TASK-038 is the first Framework `1.8.0` distribution-path implementation. TASK-039 `[Goal]` implementation begins only after this migration is `DONE` and `Framework-Source/` is canonical, so new Framework `1.8.0` command surfaces do not create fresh dependencies on the retired root name.

## 10. Non-goals

This amendment does not rename `Project-Source/`, transfer Project authority to Framework distribution, auto-upgrade initialized Projects, rewrite historical evidence, retain a compatibility alias, or implement TASK-039 or other later Framework `1.8.0` features.
