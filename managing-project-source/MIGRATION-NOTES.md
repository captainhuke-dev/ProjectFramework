# MIGRATION-NOTES

Per-release migration guidance for upgrading an initialized Project's Framework pin. These notes are routing/documentation aids, **not** normative authority — Core Governance and the latest amendment win on any conflict. Absence of a section for a transition means no notes exist yet; do not invent them.

---

## 1.3.1 → 1.4.0 (current)

### Affected distribution surfaces

- `FRAMEWORK-RELEASE.yaml` — version bump; new optional `migration_notes` / `upgrade_preview_template` fields
- `references/framework-governance-amendment-260825-task020.md` — new latest amendment
- `MIGRATION-NOTES.md`, `templates/upgrade-preview.md` — new files
- `SKILL.md` / `core-governance-rules.md` — FAST_PATH scope rule, launcher compaction policy, `[Project Upgrade]` report content contract
- `README.md` — current release identity

### Upgrade checklist

1. Run `[Project Upgrade]`; confirm `UPGRADE_AVAILABLE` with target `1.4.0`.
2. Classify: projects pinned at `1.3.x` are normally `FAST_PATH` (additive governance only; Schema unchanged).
3. Preview using `templates/upgrade-preview.md`; preservation checklist must show local pin, Stable IDs, Project rules, bindings, history all preserved.
4. Obtain explicit mutation approval after Preview.
5. Apply: update the local pin/amendment pointer to the target release; add nothing else.
6. Verify per the FAST_PATH scope rule: if the exact target tree carries committed state-bound evidence, proportional confirmation suffices; otherwise one full verification.
7. Record outcome in `16 Migration Registry` (`MIG-*`) with evidence.

### Notes for older transitions

- `1.3.0 → 1.3.1`: additive `[Project Upgrade]` command registration; FAST_PATH typical.
- Earlier transitions: no migration notes exist (`UNKNOWN`); use governed Direct-to-Latest assessment from current sources.
