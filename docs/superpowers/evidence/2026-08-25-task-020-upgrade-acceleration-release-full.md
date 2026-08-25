# TASK-020 Upgrade Acceleration (Framework 1.4.0) — RELEASE_FULL Evidence

Captured: `2026-08-25` (Asia/Bangkok)

Branch: `task-020-upgrade-acceleration`
Base: `main` at `1bf59be` (TASK-019 merge + design spec)

## Release identity

- Framework: **1.4.0** (previous 1.3.1) · Schema: **1.0.0** (unchanged) · release format **3** (unchanged)
- Latest amendment: `references/framework-governance-amendment-260825-task020.md` (approval basis: USER_EXPLICIT_IMPLEMENTATION_APPROVAL_2026-08-25, recorded in amendment frontmatter)

## Implemented scope (all five design items)

1. `MIGRATION-NOTES.md` — per-release upgrade guidance starting at `1.3.1 → 1.4.0`; older transitions explicitly `UNKNOWN`. Descriptor gains optional `migration_notes:` / `upgrade_preview_template:` fields.
2. FAST_PATH verification scope rule in Core Governance + SKILL: proportional resulting-state confirmation allowed only when recorded evidence tree SHA exactly matches the freshly observed target tree; post-evidence changes fail closed; `ASSESSED_PATH` / `MAJOR_MIGRATION_REQUIRED` never eligible for substitution.
3. `templates/upgrade-preview.md` — standardized Preview structure (identity, comparison result, affected surfaces, preservation checklist, rollback plan, verification plan, approvals).
4. Launcher compaction policy in SKILL — ceiling stays `<=4,500`; prose compactable, tokens/commands/lifecycle values/report labels/close fields never; shared marker bodies byte-identical.
5. `[Project Upgrade]` `UPGRADE_AVAILABLE` reports cite the target's migration-notes pointer when notes exist and state absence explicitly otherwise.

## Commits

- `c0bb174` — docs: define framework 1.4.0 upgrade acceleration amendment
- `63c7306` — feat: add migration notes and upgrade preview template
- `d6cd6e0` — feat: register fast-path scope rule and compaction policy governance
- `dbd2fc9` — docs: propagate framework 1.4.0 across surfaces
- `f370eb3` — test: add upgrade acceleration pressure scenarios 153–157

## Verification results (actual runs on the unchanged candidate)

- Affected verification: `PASS 24/25` → the single failure was an incorrect check expectation (24 vs a miscounted ≥24 file threshold); re-audit confirmed template metadata bumped **23/23 files** carrying the field — no product change required.
- Final full verification: `RELEASE_FULL PASS 25/25`, covering release identity, amendment pointer + SKILL first-amendment alignment, MIGRATION-NOTES content rules, FAST_PATH scope rule + fail-closed semantics, preview-template completeness, compaction policy with unchanged ceiling, migration-notes citation contract, launchers (4,497/4,496 chars ≤4,500, byte-identical markers, F`1.4.0`, all canonical tokens intact), registered commands across all four normative surfaces, README identity/section, template metadata 23/23, reserved slots `18–19` and slot `91` ownership intact, scenarios 136–157 present exactly once, md/yaml-only scope, historical amendments untouched, `git diff --check` clean, clean worktree.

Candidate HEAD/tree observed during final run: `f370eb3` / tree `fbb22ca`. The evidence file itself is committed after verification per established convention.

`commit ≠ push`: no push performed by this task. `INTEGRATION_GATE: NOT_APPLICABLE` — no branch/worktree integration performed in this execution.
