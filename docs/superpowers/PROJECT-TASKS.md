# ProjectFramework Project Task Source

This file is the durable Workspace source for ProjectFramework development Task lifecycle state, including backlog, in-progress, blocked, cancelled, and completed Tasks. Design specs, implementation plans, and evidence are referenced from each Task rather than duplicated here.

Task numbers in this file are backlog sequence numbers. They are **not** Project Source semantic document slots; Framework slots `18–19` remain RESERVED.

## Status vocabulary

- `TODO` — accepted into the Project backlog; implementation has not started.
- `IN_PROGRESS` — implementation work has started.
- `DONE` — required scope is complete and applicable verification/completion evidence exists.
- `BLOCKED` — work cannot proceed until a stated blocker is resolved.
- `CANCELLED` — work was intentionally closed without implementation completion.

## Task #18 — `[Project Upgrade]`

- **ID:** `TASK-018`
- **Status:** `DONE`
- **Type:** Framework command / upgrade workflow improvement
- **Scope:** Add a `[Project Upgrade]` Project command/workflow that fresh-checks which Project Framework version the current Workspace uses, compares it with the canonical upstream Framework, and reports whether there is a difference.
- **Required behavior:** If Workspace and upstream differ, ask the user whether to upgrade. Do not auto-upgrade merely because a newer/different upstream state exists.
- **Upgrade rule:** If the user later approves an upgrade, preserve the active Project's local pin/history and follow the current Direct-to-Latest cumulative upgrade governance rather than mechanically replaying every intermediate release.
- **Design Spec:** `docs/superpowers/specs/2026-08-24-project-upgrade-command-design.md`
- **Design State:** `USER_APPROVED_DESIGN / SPEC_APPROVED`
- **Implementation Plan:** `docs/superpowers/plans/2026-08-24-project-upgrade-command.md`
- **Plan State:** `IMPLEMENTATION_PLAN_EXECUTED`
- **Implementation Release:** Framework `1.3.1` / Schema `1.0.0`
- **Release Evidence:** `docs/superpowers/evidence/2026-08-24-framework-1.3.1-project-upgrade-release-full.md`
- **Verification Result:** `AFFECTED 57/57 PASS; RELEASE_FULL 65/65 PASS`
- **Implementation Commit(s):** `2086e0d`, `01f56dd`, `8853f43`, `d34d323`, `f06e3be`, `c8c66d2`
- **Completion Evidence Commit:** `70c5026978f8a1cd4c9328a2c3ea4c73088c3f41`
- **Final Review Fixes:** `d971ac0` (Task-source lifecycle wording), `c8c66d2` (latest-amendment Required Read alignment)
- **Completion Working Tree:** `CLEAN`
- **Publication State:** `MERGED_TO_MAIN`
- **Pull Request:** `#20` — `https://github.com/captainhuke-dev/ProjectFramework/pull/20` (`MERGED`)
- **Merge Commit:** `ba817a6c4a6ccbe5a33cab63868e90330095b5e6`
- **Canonical Main Verification:** local `main` = `origin/main` = remote `main` at merge commit `ba817a6c4a6ccbe5a33cab63868e90330095b5e6`
- **Execution Note:** `SUBAGENT_DRIVEN_REQUESTED / INLINE_FALLBACK_RECORDED_IN_RELEASE_EVIDENCE`
- **Completion criteria:** Command semantics, comparison inputs, difference reporting, approval boundary, preservation behavior, affected Framework surfaces, and verification expectations are explicitly designed and implemented; applicable tests/pressure scenarios pass.
- **Exact Next Step:** Proceed to `TASK-019` by identifying the user-facing Framework surfaces affected by its simpler-language rule and preparing a scoped design/change proposal before implementation.

## Task #19 — Simpler user-facing language

- **ID:** `TASK-019`
- **Status:** `DONE`
- **Type:** Framework interaction / language usability improvement
- **Scope:** Make user-facing explanations and Project interaction guidance easier to understand, using plain language by default and avoiding unnecessarily advanced technical jargon.
- **Required behavior:** Keep canonical Framework tokens, Stable IDs, lifecycle/status values, commands, filenames, and other exact technical identifiers unchanged where exact wording is required; simplify the explanation around them rather than renaming governed terms.
- **Completion criteria:** Applicable user-facing Framework guidance is reviewed, unnecessary jargon is reduced, explanations remain technically accurate, and required canonical terms remain intact.
- **Implementation Commit(s):** `3754476`, `69fbcc3`, `8c6c08d`
- **Release Evidence:** `docs/superpowers/evidence/2026-08-25-task-019-simpler-language-release-full.md`
- **Verification Result:** `AFFECTED 10/10 PASS; RELEASE_FULL 24/24 PASS`
- **Completion criteria met:** launchers simplified and restored to `<=4,500` (both 4,481 chars, byte-identical marker bodies); README TL;DR added; SKILL Required References annotated; canonical tokens preserved verbatim; pressure scenarios 151–152 added.
- **Exact Next Step:** Proceed to `TASK-020` design spec.

## Task #20 — Upgrade Acceleration (Framework 1.4.0)

- **ID:** `TASK-020`
- **Status:** `TODO`
- **Type:** Framework release / upgrade-workflow improvement
- **Scope:** Reduce the time cost of upgrading an initialized Project from an older ProjectFramework version to a newer one. Five bounded changes:
  1. Per-release `MIGRATION-NOTES.md` + `migration_notes` field in `FRAMEWORK-RELEASE.yaml` listing affected surfaces and a per-release checklist.
  2. FAST_PATH `RELEASE_FULL` scope rule — state-bound confirmation against exact tree SHA evidence instead of unconditional full rerun.
  3. Standard Upgrade Preview template (`templates/upgrade-preview.md`).
  4. Launcher compaction policy + ceiling raised from 4,500 to 5,000 Unicode characters.
  5. `[Project Upgrade]` `UPGRADE_AVAILABLE` report references the target release's MIGRATION-NOTES.
- **Constraints:** Markdown/YAML only; no validator/CLI/auto-updater/runtime artifact; Schema stays `1.0.0`; release format `3`; backward compatible with locally pinned Projects; historical amendments unchanged; `commit ≠ push`.
- **Completion criteria:** All five items implemented across descriptor, normative sources, templates, launchers, README; pressure scenarios added for the new upgrade-scope rules; affected verification passes; one final `RELEASE_FULL` on the unchanged candidate; release evidence committed as Framework `1.4.0` / Schema `1.0.0`.
- **Exact Next Step:** Prepare scoped design spec for TASK-020 covering the five items, obtain user design approval before implementation.
