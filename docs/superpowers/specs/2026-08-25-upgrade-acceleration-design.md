# TASK-020 Design Spec — Upgrade Acceleration (Framework 1.4.0)

Date: 2026-08-25 · Status: `DRAFT — AWAITING USER APPROVAL`

## Problem

Upgrading an initialized Project from an older ProjectFramework version to a newer one is slow for reasons unrelated to safety:

1. The agent must re-discover, from scratch, which distribution surfaces a release touches (no per-release migration guidance exists).
2. Even `FAST_PATH` upgrades end in an unconditional full `RELEASE_FULL` rerun, even when the target tree already carries state-bound evidence.
3. Upgrade Previews are composed ad hoc from prose rules each time.
4. Launchers sit at/near the 4,500-char ceiling (now 4,481), forcing risky compaction every release.
5. `UPGRADE_AVAILABLE` reports give no pointer to what the target release actually changes.

## Proposed changes (5 items, all Markdown/YAML)

### 1. Per-release MIGRATION-NOTES
- New file `managing-project-source/MIGRATION-NOTES.md` — one section per release starting at `1.3.x → 1.4.0`, listing affected surfaces + short upgrade checklist.
- `FRAMEWORK-RELEASE.yaml` gains optional field `migration_notes:` pointing at the current notes section.
- Historical releases are not retro-documented; unknown stays explicit.

### 2. FAST_PATH RELEASE_FULL scope rule
- Normative rule added to Core Governance (upgrade/verification sections) + SKILL: when the exact target candidate tree already has committed state-bound evidence (tree SHA match), a FAST_PATH upgrade may use proportional resulting-state confirmation instead of rerunning full verification; any post-evidence change to the candidate invalidates reuse (fail-closed).
- ASSESSED_PATH / MAJOR_MIGRATION_REQUIRED keep the existing one-final-RELEASE_FULL requirement unchanged.

### 3. Upgrade Preview template
- New `templates/upgrade-preview.md`: standardized sections — current vs target identity, path classification, affected surfaces (from MIGRATION-NOTES), preservation checklist, rollback plan, approval block.

### 4. Launcher compaction policy
- Policy text in SKILL (launcher maintenance rules): what may be compacted (prose) vs never compacted (tokens, commands, close fields); ceiling remains **4,500** (not raised — current files fit with headroom after TASK-019; raising it would remove the discipline pressure that caught the recent over-limit drift).

### 5. `[Project Upgrade]` report references migration notes
- Command contract extended: an `UPGRADE_AVAILABLE` report must include the target release's migration-notes pointer so the user sees affected surfaces before deciding to prepare.

## Constraints (unchanged)

- Markdown/YAML only; no validator/CLI/auto-updater/runtime artifact.
- Schema stays `1.0.0`; release format `3`.
- Backward compatible: locally pinned Projects unaffected until they choose to upgrade.
- Canonical tokens never renamed; historical amendments untouched.

## Verification plan

1. Pressure scenarios 153–157 (one per item above).
2. Structural checks: descriptor field present and consistent; template exists with required sections; scope-rule wording present in normative sources; launchers still ≤4,500 + byte-identical markers.
3. AFFECTED verification → one RELEASE_FULL on the unchanged candidate → evidence file + task reconciliation.

## Release identity

Framework **1.4.0** / Schema `1.0.0` (minor bump: new governance capability, backward compatible).
