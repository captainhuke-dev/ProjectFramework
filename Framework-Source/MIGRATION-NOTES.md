# MIGRATION-NOTES

Per-release migration guidance for upgrading an initialized Project's Framework pin. These notes are routing/documentation aids, **not** normative authority — Core Governance and the latest amendment win on any conflict. Absence of a section for a transition means no notes exist yet; do not invent them.

---

## 1.8.0 → 1.9.0 (current)

### Affected distribution surfaces

- `FRAMEWORK-RELEASE.yaml` — Framework version becomes `1.9.0`; latest amendment points to TASK-041 Portable Installation Bootstrap & Project Settings Handoff; Schema remains `1.0.0` and release format remains `3`
- `CHATGPT-PROJECT-INSTRUCTIONS.md` / `CLAUDE-PROJECT-INSTRUCTIONS.md` — current maintained vendor launchers become thin two-binding adapters instead of five-field/full-governance copies
- `templates/project-location-bootstrap.md` — user-facing Project Settings layer becomes `ProjectFramework Upstream` + verified absolute `Project Bootstrap`; internal `framework_source`, `remote_location`, `file_storage_locations`, `mcp_location`, `local_workspace`, and dynamic branch/worktree semantics remain available
- `templates/PROJECT-BOOTSTRAP.md` — documents Project Settings primary entry plus consuming README managed fallback and preserves locator-only / active-`FRAMEWORK-001` authority boundary
- upstream `README.md` — canonical GREENFIELD installation documentation, exact response-close pattern, and one repository-local managed bootstrap fallback
- consuming Project root `README.md` — governed adoption creates or maintains exactly one `PROJECTFRAMEWORK-BOOTSTRAP` managed block with relative `Project Bootstrap: ./PROJECT-BOOTSTRAP.md`; Project content outside markers remains Project-owned
- root/skeleton/mockup starters — Framework `1.9.0` GREENFIELD resulting state, descriptive Project Settings handoff guidance, and current starter stamps
- `tests/pressure-scenarios.md` — scenarios `249–268` cover install intent, two-binding handoff, absolute-path verification, README marker integrity, fallback portability, authority separation, thin launchers, Brownfield safety, and no-runtime/no-authority synthesis
- historical 1.8.0 amendments/specs/plans/evidence/full launcher captures remain provenance and are not globally rewritten

### Upgrade checklist

1. Run `[Project Upgrade]`; fresh-compare the initialized Project's valid local `FRAMEWORK-001` pin with target Framework `1.9.0`. `ProjectFramework Upstream: https://github.com/captainhuke-dev/ProjectFramework` is upstream discovery/upgrade input only, not consuming Project repository or authority.
2. Preserve current truth, Stable IDs, Project-specific rules, Project Location Binding, Local Workspace Binding, history, authorization, and local Framework/Schema pin until governed promotion. Upstream movement never auto-adopts 1.9.0.
3. Preview the portable-bootstrap adoption effects: thin vendor adapter, root `PROJECT-BOOTSTRAP.md` relationship, and consuming managed README block. Existing README content outside the managed marker pair must be preserved.
4. For a consuming README with no managed block, append exactly one block; for exactly one valid block, update only the managed body. Duplicate or malformed marker structures fail closed to repair; never choose by recency/position/similarity.
5. Project Settings uses a **verified absolute** `Project Bootstrap` path for the current environment. The consuming README uses portable relative `./PROJECT-BOOTSTRAP.md`. If the absolute path cannot be verified, report `VERIFICATION_REQUIRED`; do not fabricate a copy-ready value.
6. Preserve internal Git/Drive/File Storage/MCP/Workspace semantics and `[Project Path]`. Thin Project Settings removes legacy five labels only as mandatory current vendor fields; it does not delete location governance.
7. Apply local Project Source/root/README mutations only after the applicable upgrade Preview and approval. Do not claim GPT/Claude/Hermes/other vendor settings were changed unless an external settings action was actually executed and verified.
8. After governed adoption, regenerate and present the copy-ready Project Settings block:

```text
ProjectFramework Upstream: https://github.com/captainhuke-dev/ProjectFramework
Project Bootstrap: <VERIFIED_ABSOLUTE_PROJECT_BOOTSTRAP_PATH>

ProjectFramework Bootstrap Rule:
Read Project Bootstrap before Material Project work.
If Project Bootstrap cannot be resolved, use the Project README managed bootstrap block as fallback.
ProjectFramework Upstream is for Framework discovery/upgrade only; it never replaces local Project Source authority.
```

9. Keep active local `FRAMEWORK-001` as Project governance authority. Settings, managed README, fixed upstream, and root bootstrap remain discovery/locator surfaces and never transfer `AUTH-*`, Risk, branch/integration, implementation, runtime, publication, secret, or disclosure authority.
10. Do not synthesize Goal/OUT/AUTH/ENV/Meeting/provider/disclosure/secret-value/runtime/daemon state from adoption. Actual secret values remain forbidden.
11. Verify README marker integrity, locator chain, local pin/promotion result, maintained adapter semantics, and affected Project truth. Use one final `RELEASE_FULL` on the unchanged target candidate per existing evidence rules.
12. Direct-to-Latest remains valid; Projects pinned before 1.8.0 assess cumulative current→1.9.0 target state without mandatory intermediate replay while preserving applicable migration constraints/history.

---

## 1.7.0 → 1.8.0

### Affected distribution surfaces

- repository package root — canonical upstream distribution path changes from `managing-project-source/` to `Framework-Source/`; no live old-root alias remains
- `FRAMEWORK-RELEASE.yaml` — Framework version `1.8.0`; latest amendment pointer moves through TASK-038 distribution-root migration, TASK-039 persistent `[Goal]`, TASK-024 `[Meeting]`, TASK-026 External AI Context & Disclosure Governance, and TASK-040 canonical `[Session]` command naming
- current Core Governance / SKILL / README / launcher and maintained starter routing — current reusable Framework path is `Framework-Source/`; bounded session/task pre-approval uses canonical command `[Session]` backed by unchanged `ENV-*` semantics
- `12 Authorization Registry`, `15 Action Registry`, conditional `91 Project Management Control`, `03 Current State`, and `09 Handoff` starters — persistent Goal uses `OUT-* / AUTH-* / ACT-* / ENV-*` with `authority_transfer: false`; no `GOAL-*` family
- `13 Evidence Registry` and command/help surfaces — material Meeting use may persist as advisory `EVD-*`; no `MEETING-*` family, provider JSON authority, automatic conversation, credential, runtime, or disclosure authority is introduced
- `12 Authorization Registry`, `13 Evidence Registry`, and `17 Secret Reference Registry` starter guidance — external-AI disclosure reuses bounded `AUTH-* / EVD-* / SECRET-*`; classes are `EXTERNAL_OK | EXTERNAL_REVIEW | DO_NOT_DISCLOSE | UNCLASSIFIED`; provider eligibility is separate; no `DISC-*` family/slot is introduced
- historical amendments/specs/plans/evidence — old-path text remains historical provenance when it was true at capture time; do not globally rewrite it
- ProjectFramework's own current Project Source — reconcile current distribution-location statements through governed revisions without auto-upgrading its local Framework pin
- `tests/pressure-scenarios.md` — scenarios 181–188 cover distribution-root migration; 189–211 persistent Goal; 212–227 `[Meeting]`; 228–245 external-AI disclosure classification/authorization/provider/secret/minimization/redaction/consumer/Brownfield boundaries

### Upgrade checklist

1. Run `[Project Upgrade]`; fresh-compare the initialized Project's local pin with target `1.8.0` using Direct-to-Latest assessment/Preview rules.
2. Preserve local `FRAMEWORK-001`, Project-specific rules, bindings, Stable IDs, current truth, and history. The upstream directory rename does not itself rewrite an initialized Project.
3. Treat `Framework-Source/` as the target release's canonical reusable upstream package root. Do not infer a live fallback at `managing-project-source/`.
4. Update only current references that actually depend on the canonical upstream distribution path. Do not cosmetically rewrite historical amendments, completed evidence, or archived revisions.
5. Keep deployed `<Project-Root>/PROJECT-BOOTSTRAP.md` routing to the Project's active `Project-Source/00 → 01 → 03`, with `09` continuation. The Framework distribution root is not Project authority.
6. External scripts, bookmarks, deep links, or vendor configuration that hard-code `managing-project-source/...` require explicit update when applicable; the Framework does not mutate external consumers automatically.
7. If the consuming Project maintains repository-local current provenance/routing that names the upstream package root, migrate that current truth through its normal governed revision/MIG/evidence flow.
9. Do **not** synthesize a persistent Goal from old free-text goals, backlog items, Handoff prose, an existing `OUT-*`, or prior “continue” messages. A persistent Goal exists only after explicit `[Goal]` invocation/adoption under the active contract.
10. Preserve existing `OUT-*`, `AUTH-*`, `ACT-*`, and `ENV-*` records. TASK-039 adds composition semantics; it does not migrate them into a `GOAL-*` family.
11. If `[Goal]` is explicitly adopted, materialize/resolve Goal `OUT-*` and `AUTH-*` through their canonical homes; conditional `91` becomes applicable only when Goal/outcome truth is material.
12. Default local Goal authority may cover bounded local development unless narrowed; push, destructive actions, Root/Binding mutation, and external disclosure remain exact opt-ins and higher-level controls still apply.
13. Do **not** synthesize a Meeting from prior AI transcripts, backlog, Handoff, existing `EVD-*`, or provider conversation JSON. `[Meeting]` begins only from an explicit bracketed invocation under the active contract.
14. Treat the explicit Meeting question as the default outbound payload. Additional Project context remains minimum-necessary and separately disclosure-authorized; actual secret values remain prohibited.
15. Preserve existing external-AI/evidence records. Material Meeting use may reference/persist advisory `EVD-*`; do not migrate provider JSON into Project Source or create `MEETING-*` records.
16. Council majority/ranking/Chairman synthesis remains advisory and never becomes automatic approval, `AUTH-*`, `DEC-*`, `REQ-*`, Risk acceptance, or mutation authority.
17. Governance adoption does not require installing/running llm-council, provisioning OpenRouter credentials, or creating conversations. Provider runtime remains optional/applicability-driven.
18. `[Goal]` / `ENV-*` execution authority does not imply outbound Project-context disclosure authority for `[Meeting]`.
19. Preserve existing `AUTH-*`, `EVD-*`, and `SECRET-*`; do not create `DISC-*`, mass-classify historical content as `EXTERNAL_OK`, or synthesize standing disclosure authority from prior AI usage, credentials, chats, Meetings, Goals, or “continue” wording.
20. Use `[Session]` as the current registered command for bounded session/task `ENV-*` scope. The older longer command name is historical provenance only and is not a current registered alias.
20. Reassess external provider/tool eligibility prospectively when next used. `UNCLASSIFIED` protected Project context and materially unresolved provider policy/identity fail closed for automatic external disclosure.
21. Governance adoption does not require a runtime redactor/router/proxy, DLP scanner, disclosure gateway, provider credential setup, or automatic outbound calls.
8. Verify affected scope and run one final `RELEASE_FULL` on the unchanged target candidate before promoting the upgrade.

---

## 1.6.0 → 1.7.0

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
