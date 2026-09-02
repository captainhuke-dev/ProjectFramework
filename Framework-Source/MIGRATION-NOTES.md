# MIGRATION-NOTES

Per-release migration guidance for upgrading an initialized Project's Framework pin. These notes are routing/documentation aids, **not** normative authority — Core Governance and the latest amendment win on any conflict. Absence of a section for a transition means no notes exist yet; do not invent them.

---

## 1.12.2 → 1.13.0 (current)

### Affected distribution surfaces

- Framework identity becomes `1.13.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-028 + TASK-032 Integrity & Remediation Suite.
- `[Project Audit]` is added as a Registered Command and Strict Governed Interface with exact top-level order `Scope → Health → Categories → Findings → Unknowns → Evidence → Repair Routes → Continuity`.
- Audit health reuses `GREEN | AMBER | RED | UNKNOWN`; current/volatile evidence follows existing freshness rules and unresolved evidence remains `UNKNOWN / VERIFICATION_REQUIRED`.
- Audit findings are presentation only and reuse existing canonical homes/routes; no `AUDIT-*` / `FINDING-*` family is created and `Audit finds ≠ Audit fixes`.
- TASK-032 remediation workflow is dependency-ordered after TASK-028 and requires an explicit remediation request/Goal or other applicable authorization; audit findings alone do not activate mutation.
- Remediation resolves canonical owner/home, `R0–R3`, applicable authority, prerequisites/freshness, ordered actions, rollback/reversibility, direct resulting-state verification, affected re-audit/result confirmation, and evidence/lifecycle updates. Existing `ISS/DRIFT/CONFLICT/MIG/CR/ACT/AUTH/ENV/DEC/REQ` homes are reused.
- Semantic conflicts are routed to Decision/Change/Conflict governance rather than auto-repaired; `ACT DONE ≠ repair outcome verified`; R2/R3 and other explicit gates remain independent.
- No issue/repair object, remediation ID family, repair command, validator/scanner/CLI, daemon, repair bot, auto-fix, or runtime enforcement is generated.

### Upgrade checklist

1. Preserve the initialized Project's valid local pin and current truth; adopt 1.13.0 only through governed `[Project Upgrade]` / Direct-to-Latest promotion.
2. Add `[Project Audit]` to current command discovery and preserve the exact strict dimension order and read-only/no-auto-fix boundary.
3. Keep optional audit categories applicability-driven; do not synthesize missing `92`, Project Knowledge, or Execution-profile surfaces solely for audit completeness.
4. Treat findings as bounded command results; durable issues/drift/conflicts/migrations/changes use their existing canonical homes only through separately authorized work.
5. For an authorized repair, classify the canonical owner and Risk before mutation; declare rollback/reversibility; verify direct resulting state plus affected references; then re-audit/confirm the affected category before closure.
6. Preserve TASK-042 response-close and TASK-043 command-gate semantics unchanged.
7. Verify scenarios `1–380`, current starter stamps, command registry, historical TASK-042/TASK-043 artifacts, local-pin/history preservation, no-runtime expansion, cumulative AFFECTED, and one final unchanged-candidate `RELEASE_FULL`.

---

## 1.12.1 → 1.12.2

### Affected distribution surfaces

- Framework identity becomes `1.12.2`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-043 Registered Command Strict-Interface & Contract Completeness Hardening.
- Core Governance and SKILL define recognized Registered Commands as Strict Governed Interfaces: semantic equivalence alone does not satisfy governed structure/order/tokens/freshness/fail-closed representation.
- A new semantic Command Contract Completeness Gate validates recognized-command bodies before the existing TASK-042 Response Close Completeness Gate; TASK-042 remains the final global pre-emit close validation.
- Current `[Project Status]` Core/SKILL/root-template summaries align on `Identity → Health → Remain Tasks → Git Sync → Working Tree → Verification → Blockers → Continuity`.
- Scenarios `351–356` cover correct-information/wrong-protocol, narrative replacement, missing evidence, style conflict, ordered gates, and Core/SKILL alignment.
- No command identity, semantic slot, Stable-ID family, lifecycle/authority family, parser, runtime interceptor/middleware, validator/CLI, hook, bot, scheduler, watcher, or daemon is introduced.

### Upgrade checklist

1. Preserve the initialized Project's valid local Framework pin until governed `[Project Upgrade]` promotion; upstream movement does not silently harden Brownfield command behavior.
2. Adopt the Strict Governed Interface rule for commands registered by the selected target Framework; do not promote unbracketed ordinary language into command identity.
3. Preserve governed command dimensions/order/tokens/freshness and explicit `UNKNOWN` / `VERIFICATION_REQUIRED` representation when evidence is unavailable.
4. Run Command Contract Completeness Gate before TASK-042 Response Close Completeness Gate; preserve the existing mandatory close format and exceptional-path invariant.
5. Align current `[Project Status]` summaries through `Continuity`; preserve historical older wording as provenance rather than rewriting archives.
6. Keep prose flexibility only where the active command contract does not define stricter structure.
7. Verify scenarios `1–356`, current starter stamps, unchanged command registry, TASK-042 preservation, local-pin/history preservation, no-runtime expansion, affected checks, and one final unchanged-candidate `RELEASE_FULL`.
8. Direct-to-Latest remains valid.

---

## 1.12.0 → 1.12.1

### Affected distribution surfaces

- Framework identity becomes `1.12.1`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-042 Response Finalization Hardening forward-port.
- ChatGPT/Claude thin launchers bootstrap before the first Project-governed response in each chat; read-only/status/diagnostic/failure-report responses are not exempt; full Core Governance is not duplicated into launchers.
- Core Governance / SKILL make Response Close Completeness Gate an unskippable final-response control-flow invariant across early-return, tool/MCP failure, connector unavailable, timeout, partial-result, refusal/blocked action, persistence failure, and exception-recovery paths.
- Original TASK-042 scenarios `269–280` are historical to the 1.9.x branch; cumulative 1.12.x integration uses scenarios `339–350` to avoid collision with TASK-025/Set 1 scenarios `269–338`.
- Maintained Project Source starter stamps become Framework `1.12.1` / Schema `1.0.0`; TASK-025 Project Knowledge and Set 1 Project Execution / release / trust semantics remain intact.
- No runtime middleware/interceptor, transport hook, validator service/CLI, daemon, scheduler, watcher, UI automation, or vendor runtime component is introduced.

### Upgrade checklist

1. Preserve the initialized Project's valid local pin until governed `[Project Upgrade]` promotion; upstream movement never auto-upgrades Brownfield Projects.
2. Update thin adapter wording so Project Bootstrap resolves before the first Project-governed response when available; non-Material diagnostics are not exempt.
3. Preserve exact mandatory response-close headings, fields, order, lifecycle tokens, and coupling; TASK-042 changes timing/control-flow coverage, not the close format.
4. Preserve all Framework 1.12.0 Task dependency, Tool/MCP, capability, publication, trust, Project Knowledge, disclosure, secret, and authority boundaries.
5. Verify cumulative scenarios `1–350`, current starter stamps, launcher parity/size, historical evidence, and one final unchanged-candidate `RELEASE_FULL`.
6. Direct-to-Latest remains valid.

---

## 1.10.0 → 1.12.0

### Affected distribution surfaces

- Framework identity becomes `1.12.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-037 Security & Trust Boundary Contract.
- TASK-033 adds explicit Task dependency/readiness/priority metadata without creating Project-management `DEP-*`, scheduling, or execution authority.
- TASK-027 adds optional `Project-Execution/README.md` + `tools.md` for deterministic Tool/MCP eligibility/fallback/failure policy; Tool policy ≠ Location ≠ Authority.
- TASK-034 adds optional `Project-Execution/capabilities.md` for vendor-neutral capability/provider/review eligibility; Capability ≠ Authority and external use still follows TASK-026.
- TASK-035 adds orthogonal Implementation/Integration/Repository Publication/Release/Artifact Publication/Deployment dimensions plus RC/evidence/integration semantics; `commit ≠ push` and publication authority remains separate.
- TASK-037 adds optional `Project-Execution/trust.md` for trust/crossing/privileged/UNKNOWN fail-closed governance; TASK-026 and `17 Secret Reference Registry` remain canonical for disclosure/secrets.
- Scenarios `289–338` cover Set 1 behavior; maintained Project Source starter stamps become Framework `1.12.0` / Schema `1.0.0`.
- ChatGPT/Claude thin launchers remain unchanged; no scheduler/router/provider/CI-CD/scanner/policy-engine/runtime enforcement is added.

### Upgrade checklist

1. Run `[Project Upgrade]`; preserve the initialized Project's local Framework/Schema pin until governed promotion.
2. Assess Task dependency metadata separately from Project-management `DEP-*`; do not infer Task edges from numbering/proximity.
3. Evaluate whether `Project-Execution/` is applicable. Do not create default allow-all/restrictive tools, model capability, or trust profiles without approved facts.
4. If tool policy is adopted, verify Project authority/location first; then apply deterministic PRIMARY/allow/disallow/fallback/failure behavior. Store no credentials/secrets.
5. If capability policy is adopted, keep Tool eligibility, model capability, provider/disclosure eligibility, and authority separate. Required independent review remains evidence-backed.
6. Map existing release practices to orthogonal publication dimensions without rewriting historical facts or inventing RC identities/tags/approvals.
7. If trust policy is adopted, classify only evidenced surfaces; UNKNOWN sensitive crossings fail closed. Prior successful use never proves trust.
8. Preserve TASK-026 disclosure/minimization/secret prohibitions and `17 Secret Reference Registry` reference-only semantics across external/tool/model/trust flows.
9. Do not auto-create routers, schedulers, CI/CD, release bots, deployment automation, scanners, policy engines, secret stores, or runtime enforcement.
10. Verify current starter stamps, Project-Execution templates, scenario coverage, local pin/history preservation, and affected Framework surfaces; run one final unchanged-candidate `RELEASE_FULL`.
11. Direct-to-Latest remains valid: older Projects assess cumulative current→1.12.0 semantics without mandatory replay of intermediate releases.

---

## 1.9.0 → 1.10.0

### Affected distribution surfaces

- Framework identity becomes `1.10.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-025 Project Knowledge Layer.
- Core Governance / SKILL / README define optional `Project-Knowledge/` outside Project Source authority, exact maintenance states, provenance, index/log operations, promotion gate, disclosure/Meeting/Evidence/Project Graph/OpenViking boundaries.
- `templates/project-knowledge/` adds maintained starter source for Knowledge README/index/log/page representation.
- Project Source starter templates remain semantic-slot starters but their current Framework stamps become 1.10.0; no new semantic slot is added.
- scenarios `269–288` cover authority separation, provenance, maintenance operations/states, promotion, integration boundaries, optionality, and no-runtime/no-secret behavior.
- ChatGPT/Claude thin vendor launchers are unchanged by TASK-025.

### Upgrade checklist

1. Run `[Project Upgrade]`; preserve the initialized Project's local Framework pin and current Project Source until governed promotion.
2. Evaluate whether a Project Knowledge layer is actually useful. Absence remains valid; do not create it merely because target 1.10.0 supports it.
3. If adoption is desired, Preview root `Project-Knowledge/` creation and any Project Source routing pointer after active authority resolution.
4. Do not bulk-migrate historical notes, chats, Meeting transcripts, or files as accepted Knowledge. Candidate material requires provenance review and may remain source-native.
5. Maintain `Project Knowledge ≠ Project Authority`. Knowledge page state, retrieval rank, model consensus, or recency never changes Requirements/Decisions/Risks/Relations automatically.
6. Knowledge→Governance promotion identifies the canonical Project Source owner, verifies evidence, obtains applicable authority, then mutates only that owner.
7. External use of Knowledge still follows TASK-026 disclosure/provider/minimization/secret rules. Project Knowledge maintenance authority grants no external disclosure.
8. Knowledge cross-links do not create `REL-*`; OpenViking keeps `PROJECT_SOURCE_AUTHORITY` separate from `PROJECT_KNOWLEDGE_ADVISORY` and remains derived/rebuildable.
9. No wiki engine, vector DB, embedding service, watcher, crawler, MCP wiki service, validator/CLI, scheduler, or runtime daemon is required or authorized by this migration.
10. Verify Knowledge template integrity, optionality, local pin/promotion result, current starter stamps, pressure scenarios, and affected current Framework surfaces; run one final unchanged-candidate `RELEASE_FULL` under existing evidence rules.
11. Direct-to-Latest remains valid: older Projects assess cumulative current→1.10.0 target semantics without mandatory replay of intermediate releases while preserving applicable migration constraints/history.

---

## 1.8.0 → 1.9.0

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
