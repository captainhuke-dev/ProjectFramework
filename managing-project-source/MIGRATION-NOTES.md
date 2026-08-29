# MIGRATION-NOTES

Per-release migration guidance for upgrading an initialized Project's Framework pin. These notes are routing/documentation aids, **not** normative authority — Core Governance and the latest amendment win on any conflict. Absence of a section for a transition means no notes exist yet; do not invent them.

---

## 1.6.0 → 1.7.0 (current)

### Affected distribution surfaces

- `FRAMEWORK-RELEASE.yaml` — Framework version `1.7.0`; latest amendment pointer moves to TASK-023; root bootstrap template becomes a declared entrypoint
- `references/framework-governance-amendment-260829-task023.md` / `core-governance-rules.md` / `SKILL.md` — vendor-neutral Project-root discovery contract and authority/failure boundaries
- `templates/PROJECT-BOOTSTRAP.md`, `templates/project-location-bootstrap.md`, root/skeleton/mockup templates — GREENFIELD root bootstrap, legacy `PROJECT-CONFIG.md` separation, and canonical `00 → 01 → 03` routing with `09` continuation
- `CHATGPT-PROJECT-INSTRUCTIONS.md` / `CLAUDE-PROJECT-INSTRUCTIONS.md` — optional thin adapters that prefer `PROJECT-BOOTSTRAP.md` when Project-root access exists
- `tests/pressure-scenarios.md` — root discovery, authority, GREENFIELD/Brownfield, contradiction, no-filesystem, stable-filename, volatile-state, and vendor-independence coverage
- `README.md` — current release identity and self-bootstrapping Project explanation

### Upgrade checklist

1. Run `[Project Upgrade]`; fresh-compare the active local pin with target `1.7.0` using Direct-to-Latest classification/Preview rules.
2. Preserve Project-specific rules, bindings, Stable IDs, history, current semantic slots, existing optional `PROJECT-CONFIG.md`, and all current authority homes.
3. Include creation of `<Project-Root>/PROJECT-BOOTSTRAP.md` in the upgrade Preview; do not create it merely because upstream `main` advanced.
4. Apply only with the mutation authority required by the existing upgrade contract. Materialize the root file from the `1.7.0` template using the Project's real relative Project Source root.
5. Verify the new root bootstrap resolves the existing active `00 / FRAMEWORK-001`, then `01`, then `03`; resolve `09 Handoff` for continuation when applicable.
6. Treat `PROJECT-BOOTSTRAP.md` as discovery/locator only. It does not replace Project Location Binding, current branch/worktree, Integration Target, Implementation Source, Runtime authority, or `AUTH-*`/Risk authority.
7. If root bootstrap, vendor adapter, `PROJECT-CONFIG.md`, or active root binding contradict materially, fail closed for affected mutation and route resolution through existing governance; do not choose by recency.
8. Verify affected scope and run one final `RELEASE_FULL` on the unchanged target candidate; record material adoption in `16 Migration Registry` when applicable.

---

## 1.5.0 → 1.6.0

### Affected distribution surfaces

- `FRAMEWORK-RELEASE.yaml` — Framework version `1.6.0`; latest amendment pointer moves to TASK-022
- `references/framework-governance-amendment-260828-task022.md` / `core-governance-rules.md` / `SKILL.md` — standard conditional `92 Project Graph`, `REL-*`, late-binding and AI-ControlTower/OpenViking derived-index contract
- `templates/00-project-source-framework.md`, `templates/core-document-skeletons.md`, `templates/project-source-mockup/` — Project Graph applicability/routing and new `92-Project-Graph.template.md`
- `tests/pressure-scenarios.md` — relation authority, late-binding, rebuild, collision, merge/split, and extension-type pressure coverage
- `README.md` — release identity and Federated Project Graph explanation

### Upgrade checklist

1. Run `[Project Upgrade]`; fresh-compare the active local pin with target `1.6.0` and use Direct-to-Latest classification/Preview rules.
2. Preserve Project-specific rules, bindings, Stable IDs, history, and current authoritative homes; `REL-*` does not absorb `DEP-*`, `DEC-*`, `REQ-*`, `DRIFT-*`, or `CONFLICT-*` payloads.
3. Inspect active slot `92`. If custom content already occupies it, fail closed to `MIG-*`; preserve identity/history/references and relocate only through approved migration before standard `92` activation.
4. Do not create `92` merely for completeness. Materialize it only when Project relation truth is applicable; Projects may bind relations later.
5. Preserve immutable `project_uuid` as relation endpoint identity. Relation topology does not rewrite repository/workspace/runtime/integration/implementation bindings.
6. Treat AI-ControlTower/OpenViking as derived/rebuildable indexing only; do not migrate canonical Project relation truth into OpenViking.
7. Verify affected scope and run one final `RELEASE_FULL` on the unchanged target candidate; record the upgrade in `16 Migration Registry` when material.

---

## 1.3.1 → 1.4.0

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

- `1.4.0 → 1.5.0`: additive ChatGPT→MCP continuity governance; use governed Direct-to-Latest assessment from current sources.
- `1.3.0 → 1.3.1`: additive `[Project Upgrade]` command registration; FAST_PATH typical.
- Earlier transitions: no migration notes exist (`UNKNOWN`); use governed Direct-to-Latest assessment from current sources.
