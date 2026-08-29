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
- **Publication State:** `MERGED_TO_MAIN` — merge commit `0bdf6e5` (included in the same push as TASK-020); `main` = `origin/main` at `faf3406`.
- **Exact Next Step:** Proceed to `TASK-020` design spec.

## Task #20 — Upgrade Acceleration (Framework 1.4.0)

- **ID:** `TASK-020`
- **Status:** `DONE`
- **Type:** Framework release / upgrade-workflow improvement
- **Scope:** Reduce the time cost of upgrading an initialized Project from an older ProjectFramework version to a newer one. Five bounded changes:
  1. Per-release `MIGRATION-NOTES.md` + `migration_notes` field in `FRAMEWORK-RELEASE.yaml` listing affected surfaces and a per-release checklist.
  2. FAST_PATH `RELEASE_FULL` scope rule — state-bound confirmation against exact tree SHA evidence instead of unconditional full rerun.
  3. Standard Upgrade Preview template (`templates/upgrade-preview.md`).
  4. Launcher compaction policy + ceiling raised from 4,500 to 5,000 Unicode characters.
  5. `[Project Upgrade]` `UPGRADE_AVAILABLE` report references the target release's MIGRATION-NOTES.
- **Constraints:** Markdown/YAML only; no validator/CLI/auto-updater/runtime artifact; Schema stays `1.0.0`; release format `3`; backward compatible with locally pinned Projects; historical amendments unchanged; `commit ≠ push`.
- **Completion criteria:** All five items implemented across descriptor, normative sources, templates, launchers, README; pressure scenarios added for the new upgrade-scope rules; affected verification passes; one final `RELEASE_FULL` on the unchanged candidate; release evidence committed as Framework `1.4.0` / Schema `1.0.0`.
- **Design Spec:** `docs/superpowers/specs/2026-08-25-upgrade-acceleration-design.md` (`USER_APPROVED_DESIGN / SPEC_APPROVED`)
- **Implementation Release:** Framework `1.4.0` / Schema `1.0.0`
- **Implementation Commit(s):** `c0bb174`, `63c7306`, `d6cd6e0`, `dbd2fc9`, `f370eb3`
- **Release Evidence:** `docs/superpowers/evidence/2026-08-25-task-020-upgrade-acceleration-release-full.md`
- **Verification Result:** `RELEASE_FULL 25/25 PASS`
- **Completion criteria met:** all five items implemented; scenarios 153–157 added; launchers remain ≤4,500 with byte-identical markers; Schema/release format unchanged.
- **Publication State:** `MERGED_TO_MAIN` — merged locally and pushed; `main` = `origin/main` at `faf3406bec9d16d676ec9406ecc4a13dc2b14a6d`. No PR by user decision (direct merge).
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป


## Task #21 — ChatGPT→MCP Continuity (Continuous System Management)

- **ID:** `TASK-021`
- **Status:** `DONE`
- **Type:** Framework continuity / interaction reliability improvement
- **Problem:** System management driven through ChatGPT → MCP stops frequently for three distinct reasons: (1) ChatGPT session/conversation expiry losing in-chat context, (2) MCP connection drops mid-task forcing step restarts, (3) per-step approval gates interrupting otherwise continuous flows.
- **Scope:**
  1. **Continuation Contract** — normative rule that every Logical Checkpoint writes MCP-readable continuation state (`09 Handoff` + `03 Current State`) sufficient for any fresh session/agent to resume within one read.
  2. **Pre-Approved Action Envelope** — new registered `[Session Envelope]` command: user pre-approves a bounded scope of operations for a session/task; fail-closed governance still applies outside the envelope; envelope never grants location/binding/root authority.
  3. **MCP Resume Semantics** — governed requirement that Material MCP operations be designed idempotent with declared resume checkpoints, so connection drops resume from the last checkpoint instead of restarting.
  4. **Continuity health fields in `[Project Status]`** — expose which handoff/checkpoint links are stale or repeatedly breaking.
- **Constraints:** Documentation/governance scope only — ProjectFramework defines the contracts; no relay/runtime implementation, validator, CLI, or automation artifact. The actual persistent outbound relay runtime remains lnwjud project scope and must stay contract-compatible. Schema stays `1.0.0`; canonical tokens unchanged; `commit ≠ push`.
- **Design State:** problem framing discussed and user-approved direction ("ลง Task ได้เลย"); scoped design spec still required before implementation.
- **Completion criteria:** Continuation Contract, `[Session Envelope]` command contract, MCP Resume Semantics, and `[Project Status]` continuity fields implemented across normative sources + templates + launchers; pressure scenarios added; AFFECTED verification passes; one final `RELEASE_FULL` on unchanged candidate; evidence committed (target release Framework `1.5.0` / Schema `1.0.0`, pending design confirmation).
- **Design Spec:** `docs/superpowers/specs/2026-08-25-task021-mcp-continuity-design.md` (`USER_APPROVED_DESIGN / SPEC_APPROVED`)
- **Implementation Release:** Framework `1.5.0` / Schema `1.0.0` (user-approved minor bump)
- **Implementation Commit(s):** `e9c65f2`, `bbf82d2`
- **Release Evidence:** `docs/superpowers/evidence/2026-08-25-task-021-mcp-continuity-release-full.md`
- **Verification Result:** `RELEASE_FULL 23/23 PASS` (first run 23/24 — SKILL latest-amendment alignment finding corrected in `bbf82d2`)
- **Completion criteria met:** all four items implemented; scenarios 158–162 added; launchers ≤4,500 byte-identical; Schema/format unchanged.
- **Publication State:** `MERGED_TO_MAIN` — `main` = `origin/main` at `5834a3eab03215f2350e369f48673186f2d0a98c` (direct merge, no PR per established pattern).
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป

## Task #22 — Project Graph + OpenViking Relation Governance

- **ID:** `TASK-022`
- **Status:** `DONE`
- **Type:** Framework architecture / cross-Project knowledge-relation governance
- **Problem:** A Project may begin independently and only later become related to other Projects, or become a parent/child/nested Project. The Framework needs a durable relation model that does not require all relationships to be known at Project creation time and does not make one Project's local truth depend on a central knowledge index.
- **Scope:**
  1. **Project-local Project Graph semantics** — define the Project-level graph/relation records needed to describe this Project's known links to other Projects while preserving each Project's local `.md` governance/current truth as authoritative for that Project.
  2. **AI-ControlTower OpenViking ownership** — define OpenViking as a cross-Project knowledge/index layer owned at AI-ControlTower scope rather than by any single Project; Projects publish/update the minimum relation/index information needed by that layer without transferring Project authority to it.
  3. **Late binding** — allow Projects created with no relation to bind new parent/child/peer/dependency or other governed relations later without requiring destructive Project reconstruction.
  4. **Rebuild / re-index semantics** — when Project structure or relations change materially, allow derived Project Graph/OpenViking relation indexes to be rebuilt from current authoritative Project sources; stale derived relations must not override source truth.
  5. **Tooling boundary** — do not require a graph database or a specific graph product for the initial Framework contract. Tooling such as Graphify or another graph/index engine is optional implementation choice only if later requirements justify it.
- **Constraints:** Documentation/governance design first; no OpenViking runtime, graph database, sync daemon, crawler, validator, CLI, scheduler, or automation implementation is authorized by this Task registration. Preserve current Framework authority/location/binding rules, Stable IDs, Project-local pins, and `commit ≠ push`.
- **Design Spec:** `docs/superpowers/specs/2026-08-28-task022-project-graph-openviking-design.md`
- **Design State:** `USER_APPROVED_DESIGN / SPEC_APPROVED`
- **Implementation Plan:** `docs/superpowers/plans/2026-08-28-task022-project-graph-openviking.md`
- **Plan State:** `IMPLEMENTATION_PLAN_EXECUTED`
- **Implementation Release:** Framework `1.6.0` / Schema `1.0.0`
- **Target Release:** Framework `1.6.0` / Schema `1.0.0` / release format `3`
- **Implementation Commit(s):** `9f32f72`, `ea43867`, `0d9978b`, `2240cec`, `6eb8790`
- **Release Evidence:** `docs/superpowers/evidence/2026-08-28-task-022-project-graph-release-full.md`
- **Verification Result:** `RELEASE_FULL 73/73 PASS`
- **Candidate Commit:** `6eb87904374f1fb3034db572e3773238e4ed0e14`
- **Candidate Distribution Tree:** `9d1d06916b944f8169477c220777ee5874e689bf`
- **Completion criteria met:** federated Project-authoritative graph; standard conditional slot `92`; canonical `REL-*`; immutable `project_uuid` endpoints; late binding; semantic nesting/location separation; evidence-based corroboration/conflict; merge/split reassessment; AI-ControlTower/OpenViking `DERIVED_ONLY` + `REBUILDABLE` boundary; Brownfield custom-slot-92 migration; 22 starter templates; scenarios `1–171`; documentation-only scope.
- **Publication State:** `PUBLISHED_TO_ORIGIN_MAIN` — verified TASK-022 implementation and completion through `9a34b49` were pushed to `origin/main` on `2026-08-28` under explicit user publication approval; this publication-state reconciliation record is included in the same approved publication operation.
- **Completion Working Tree:** `CLEAN`
- **Execution Note:** isolated worktree was prepared but host Active Workspace mutation routing blocked writes/commits there; implementation continued inline on local `main` under the user's explicit continuous approval. Remote publication was performed only after the user's separate explicit push approval.
- **Completion criteria:** A user-approved design specifies relation ownership, canonical-vs-derived truth boundaries, Project Graph representation, AI-ControlTower/OpenViking integration contract, late-binding lifecycle, rebuild/re-index behavior, failure/drift handling, and affected Framework surfaces; implementation proceeds under the user's explicit continuous approval with proportional verification and a final unchanged-candidate `RELEASE_FULL` before completion.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป

## Task #23 — Self-Bootstrapping Project Contract

- **ID:** `TASK-023`
- **Status:** `DONE`
- **Type:** Framework architecture / vendor-neutral Project bootstrap
- **Problem:** Framework bootstrap currently depends too heavily on vendor/product-specific Project Settings. Existing Projects may be used without those settings being configured, causing an LLM/agent to miss the intended bootstrap contract before reading authoritative Project Source.
- **Approved direction:** Move bootstrap discovery into the Project itself through one stable vendor-neutral root entrypoint: `<Project-Root>/PROJECT-BOOTSTRAP.md`.
- **Scope:**
  1. Define `PROJECT-BOOTSTRAP.md` at Project root as the canonical discovery/locator entrypoint for Framework versions that adopt this feature.
  2. Define one vendor-neutral read pattern beginning `PROJECT-BOOTSTRAP.md → 00 FRAMEWORK-001 → 01 Project Source Index → 03 Current State → task-specific routing`; continuation additionally resolves `09 Handoff` when relevant.
  3. Make `PROJECT-BOOTSTRAP.md` mandatory for NEW Projects created under the adopting Framework release.
  4. Existing initialized Projects receive the bootstrap file only through governed `[Project Upgrade]`; no automatic creation or automatic upgrade.
  5. Reclassify ChatGPT Project Settings, `AGENTS.md`, `CLAUDE.md`, and other vendor-specific instruction surfaces as optional thin discovery adapters/pointers rather than canonical Framework authority.
  6. Preserve `FRAMEWORK-001` as Project governance authority. `PROJECT-BOOTSTRAP.md` is a discovery/locator contract only and must never become a second source of Project truth.
  7. Keep bootstrap discovery distinct from Repository/File Storage/Local Workspace Binding, current branch/worktree, Canonical Integration Target, Canonical Implementation Source, and Runtime authority.
  8. Keep the filename stable as `PROJECT-BOOTSTRAP.md`; do not use revision/date suffixes for the discovery entrypoint.
- **Design constraints:** The Framework must not claim that every LLM can discover a Project without filesystem/repository access. The success boundary is: once an agent can access the Project root, Project contents alone are sufficient to discover and follow the canonical bootstrap path without requiring vendor-specific Project Settings.
- **Implementation boundary:** Framework governance/documentation implementation only. Do not add filesystem watchers, discovery daemons, MCP runtime/tool routing, automatic Brownfield upgrades, secret storage, CI/CD, or deployment automation.
- **Design Spec:** `docs/superpowers/specs/2026-08-29-task023-self-bootstrapping-project-design.md`
- **Design State:** `USER_APPROVED_DESIGN / SPEC_APPROVED`
- **Implementation Plan:** `docs/superpowers/plans/2026-08-29-task023-self-bootstrapping-project.md`
- **Plan State:** `IMPLEMENTATION_PLAN_EXECUTED`
- **Implementation Release:** Framework `1.7.0` / Schema `1.0.0`
- **Target Release:** Framework `1.7.0` / Schema `1.0.0` / release format `3`
- **Implementation Commit(s):** `ee4b088`, `094e9a4`, `e67ac2f`, `c1496b0`, `e2caa5e`
- **Release Evidence:** `docs/superpowers/evidence/2026-08-29-task-023-self-bootstrapping-project-release-full.md`
- **Verification Result:** `RELEASE_FULL 146/146 PASS`
- **Candidate Commit:** `e2caa5e68f037104cf7ca41756690daf03ede576`
- **Candidate Distribution Tree:** `100338b4186e5ccbe0502b92a85e38555e40db3c`
- **Completion criteria met:** stable vendor-neutral `PROJECT-BOOTSTRAP.md`; canonical `00 → 01 → 03` discovery with `09` continuation; active `FRAMEWORK-001` authority preserved; GREENFIELD mandatory root bootstrap; Brownfield governed adoption only; vendor adapters optional; `PROJECT-CONFIG.md` remains optional Bootstrap Location reference; volatile execution state excluded from bootstrap authority; 22 concrete starters aligned to 1.7.0; scenarios `1–180`; documentation-only scope.
- **Publication State:** `PUBLISHED_TO_ORIGIN_MAIN` — verified Framework 1.7.0 implementation and completion through `94661bb` were pushed to `origin/main` on `2026-08-29` under the user's explicit continuous completion approval; this publication-state reconciliation record is committed and published in the same approved release sequence.
- **Completion Working Tree:** `CLEAN` after completion commit verification.
- **Execution Note:** a linked TASK-023 worktree was prepared, but host Active Workspace mutation routing blocked writes there; implementation therefore continued inline on local `main` under the user's explicit continuous approval through Framework 1.7.0 completion.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป

## Task #24 — `[Meeting]` LLM Council Command

- **ID:** `TASK-024`
- **Status:** `TODO`
- **Type:** Framework command / multi-model advisory council integration
- **Source Repository:** `https://github.com/captainhuke-dev/llm-council`
- **Problem:** ProjectFramework currently has no standard Project command for convening a multi-model LLM council when a decision benefits from independent perspectives, structured peer review, disagreement surfacing, and a synthesized recommendation.
- **Approved direction:** Register `[Meeting]` as the user-facing command for convening the LLM Council associated with the referenced repository.
- **Scope:**
  1. Define `[Meeting]` command semantics for providing a meeting topic/question plus the minimum relevant Project context.
  2. Define the council workflow and result contract so outputs distinguish individual/independent views, areas of agreement, disagreements, blind spots/risks, and the final synthesized recommendation.
  3. Treat council output as **ADVISORY evidence only**. A council recommendation does not become Project Authority, Decision, approval, or permission to mutate Project state automatically.
  4. Preserve existing ProjectFramework governance: any recommendation that would change requirements, architecture, implementation, bindings, risk posture, or other governed truth still follows the applicable approval/Decision workflow.
  5. Before implementation, inspect and verify the current `captainhuke-dev/llm-council` fork directly and bind the design to its observed interfaces/workflow; do not infer implementation details solely from upstream or prior knowledge.
  6. Define failure behavior for unavailable council models/services, partial responses, disagreement, and inability to reach a synthesized recommendation without fabricating consensus.
  7. Define what meeting artifacts, if any, should be persisted or referenced as evidence without duplicating canonical Project truth.
- **Implementation boundary:** Task registration only. Do not add `[Meeting]` to Framework commands, launchers, templates, MCP/runtime integration, or automation until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** Framework `1.8.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines command syntax, council input/context boundary, verified llm-council integration contract, advisory-authority separation, result structure, failure/partial-response behavior, persistence/evidence rules, affected Framework surfaces, and verification strategy before implementation begins.
- **Exact Next Step:** Wait for further requirements; when TASK-024 is selected for development, inspect the referenced llm-council repository directly and prepare its architectural design spec before implementation.

## Task #25 — Project Knowledge Layer / Compounding Knowledge Contract

- **ID:** `TASK-025`
- **Status:** `TODO`
- **Type:** Framework architecture / persistent LLM-maintained Project knowledge
- **Source Concept:** `https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f` (`llm-wiki`)
- **Problem:** ProjectFramework has strong governed current truth and continuity, but much research, synthesis, comparison, meeting insight, and learned context that should not become authoritative `REQ-*` / `DEC-*` / other Project Source records is otherwise likely to remain fragmented across chats or be recomputed repeatedly.
- **Approved direction:** Adapt the compounding-knowledge pattern from `llm-wiki` into a distinct **Project Knowledge Layer** that is Markdown-first, vendor-neutral, provenance-aware, and explicitly separate from authoritative Project Source.
- **Scope:**
  1. Define the boundary `Project Knowledge ≠ Project Authority`. LLMs may maintain/synthesize knowledge, but may not automatically promote knowledge into governed Project truth.
  2. Define the relationship among raw sources/evidence, synthesized knowledge pages, governed Project Source, and explicit Knowledge→Governance promotion gates.
  3. Define knowledge identity/indexing, cross-links, chronological ingest/query/maintenance log behavior, provenance/source pointers, staleness/review state, contradiction handling, and knowledge-lint expectations.
  4. Reuse existing ProjectFramework governance when knowledge becomes materially governance-relevant; do not create parallel authoritative families that duplicate `REQ-*`, `DEC-*`, `ISS-*`, `DRIFT-*`, `CONFLICT-*`, `RISK-*`, or other canonical homes.
  5. Define integration boundaries with TASK-023 bootstrap discovery, TASK-024 `[Meeting]` council outputs, `13 Evidence`, `03 Current State`, `09 Handoff`, and `92 Project Graph` without merging their authorities or purposes.
  6. Define the AI-ControlTower/OpenViking boundary so cross-Project indexing can distinguish authoritative Project Source from advisory/derived Project Knowledge and never rank or retrieve knowledge as if it were Project authority.
  7. Define GREENFIELD and Brownfield applicability/migration behavior, including whether a physical `Project-Knowledge/` directory or another representation is appropriate; do not lock physical layout before design review.
  8. Preserve source-derived terminology and provenance from the `llm-wiki` concept where adopted, but do not copy its implementation assumptions blindly into ProjectFramework governance.
- **Implementation boundary:** Task registration only. Do not create a wiki engine, vector database, UI, watcher, crawler, auto-ingest daemon, embedding pipeline, MCP wiki service, runtime automation, or Project Knowledge files until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** Framework `1.9.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines authority separation, knowledge schema/lifecycle, provenance, indexing/log/lint behavior, contradiction/staleness handling, promotion gates, TASK-023/TASK-024/OpenViking integration boundaries, Brownfield behavior, affected Framework surfaces, and verification strategy before implementation begins.
- **Exact Next Step:** Wait for further requirements; when TASK-025 is selected for development, prepare its architectural design spec before implementation.

## Task #26 — External AI Context & Disclosure Governance

- **ID:** `TASK-026`
- **Status:** `TODO`
- **Type:** Framework architecture / outbound AI-context governance
- **Problem:** TASK-024 `[Meeting]`, TASK-025 Project Knowledge, and other future external-model workflows may send Project context outside the local authority boundary. ProjectFramework needs a governed rule for what context may be disclosed, minimized, redacted, provider-scoped, or prohibited before any external AI call occurs.
- **Approved direction:** Define an outbound AI Context/Disclosure contract that classifies Project information by disclosure eligibility, applies minimum-necessary context and redaction, and fails closed when classification or permission is unresolved.
- **Scope:**
  1. Define disclosure classes and provider/tool eligibility without weakening `17 Secret Reference Registry` or existing secret handling.
  2. Define context minimization, redaction, secret-reference-only behavior, and `DO_NOT_DISCLOSE`-equivalent policy semantics.
  3. Define how `[Meeting]`, Project Knowledge, OpenViking, and other external-model consumers request context through the disclosure boundary rather than reading/sending unrestricted Project content.
  4. Preserve Authority: permission to disclose context does not grant Decision, mutation, binding, runtime, or implementation authority.
  5. Define provenance/evidence sufficient to know what category of information was disclosed and under which rule without persisting secrets unnecessarily.
  6. Define failure behavior for unknown classification, mixed-sensitivity context, unavailable provider policy, and redaction uncertainty.
- **Implementation boundary:** Task registration only. Do not add disclosure automation, provider routing, redaction runtime, external calls, or new secret storage until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** Framework `1.8.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines disclosure vocabulary, context-minimization/redaction rules, provider/tool eligibility, integration boundaries, fail-closed behavior, provenance/evidence requirements, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** Wait for further requirements; when TASK-026 is selected for development, prepare its architectural design spec before implementation.

## Task #27 — Project Tool / MCP Execution Profile

- **ID:** `TASK-027`
- **Status:** `TODO`
- **Type:** Framework architecture / Project-scoped execution-tool governance
- **Problem:** Project tool/MCP preferences such as `CEO-only` can currently exist only as transient chat instructions or product-specific configuration. The Project needs a durable vendor-neutral contract declaring which execution tools are primary, allowed, disallowed, or eligible as fallback.
- **Approved direction:** Define a Project Tool / MCP Execution Profile that can express a primary MCP/tool, fallback policy, fail-closed behavior, and allowed/disallowed execution capabilities without depending on a vendor UI setting.
- **Scope:**
  1. Define durable Project-scoped execution-tool selection semantics including `PRIMARY`, allowed alternatives, `FALLBACK_NONE`-equivalent behavior, and failure policy.
  2. Keep Tool/MCP Execution Profile distinct from MCP Location Binding, Project authority, current branch/worktree, Canonical Integration Target, Canonical Implementation Source, and Runtime authority.
  3. Define how TASK-023 `PROJECT-BOOTSTRAP.md` discovers or routes to the active execution profile without making bootstrap a second authority.
  4. Define behavior when the preferred MCP/tool is unavailable, unauthenticated, stale, renamed, or cannot prove it is operating on the bound Project.
  5. Define GREENFIELD defaults and Brownfield migration so existing Projects do not silently acquire restrictive or permissive tool policy.
  6. Preserve explicit user/shared-state gates such as push, destructive actions, secrets, and governed approvals regardless of tool profile.
- **Implementation boundary:** Task registration only. Do not modify `.lnwjud`, MCP runtime, project profiles, tool routing, launchers, or existing Projects until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** Framework `1.7.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines execution-profile schema, authority/location separation, primary/fallback/fail behavior, bootstrap integration, Brownfield rules, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** Wait for further requirements; when TASK-027 is selected for development, prepare its architectural design spec before implementation.

## Task #28 — `[Project Audit]` Integrity & Drift Command

- **ID:** `TASK-028`
- **Status:** `TODO`
- **Type:** Framework command / Project integrity assessment
- **Problem:** `[Project Status]` is a current dashboard, but ProjectFramework lacks one standard read-only command for deeper integrity, consistency, stale-reference, drift, and governance-health assessment across Project surfaces.
- **Approved direction:** Define `[Project Audit]` as a read-only integrity command that evaluates Project Source, bootstrap, continuity, Git/binding evidence, Stable-ID routing, Project Graph, migration/drift/conflict state, and future Knowledge/Tool-profile surfaces when applicable.
- **Scope:**
  1. Define audit categories, severity/health vocabulary, evidence requirements, and bounded output suitable for human review.
  2. Check cross-surface consistency such as `00 / 01 / 03 / 09 / 14`, current Stable-ID resolvability, stale evidence, broken references, binding/freshness problems, and active conditional documents.
  3. Include `REL-*`/Project Graph consistency and future TASK-023/025/027 surfaces only when applicable under their adopted contracts.
  4. Reuse existing `ISS-*`, `DRIFT-*`, `CONFLICT-*`, and `MIG-*` rather than inventing parallel authoritative issue families.
  5. Preserve `Audit finds ≠ Audit fixes`: default audit is read-only and cannot mutate Project truth, resolve conflicts, migrate, push, or repair automatically.
  6. Define partial/unknown behavior when required sources or runtime evidence cannot be read.
- **Implementation boundary:** Task registration only. Do not register `[Project Audit]`, add validators/CLI/runtime scanners, or mutate existing Framework surfaces until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** Framework `1.10.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines command syntax, audit scope/categories, health vocabulary, evidence/unknown handling, no-auto-fix boundary, integration with existing governance families, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** Wait for further requirements; when TASK-028 is selected for development, prepare its command/design spec before implementation.

## Task #29 — Cross-Project Impact Analysis

- **ID:** `TASK-029`
- **Status:** `TODO`
- **Type:** Framework architecture / federated Project-change impact reasoning
- **Problem:** Framework 1.6.0 can represent Project relations through `92 Project Graph` / `REL-*`, but the Framework does not yet define how to reason about which other Projects may require review when one Project changes materially.
- **Approved direction:** Define a cross-Project impact-analysis contract that uses authoritative Project relation assertions plus relevant governed dependency/requirement/evidence pointers to surface direct and potential impacts without propagating changes automatically.
- **Scope:**
  1. Define direct versus potential/indirect impact semantics and the minimum evidence/provenance needed to report each.
  2. Use `REL-*` as Project relation input while preserving canonical homes such as `DEP-*`, `REQ-*`, `DEC-*`, and other relevant records; do not duplicate their payload into the graph.
  3. Define review-required outputs for affected Projects, reasons/pointers, unresolved/unknown impact state, and conflict behavior.
  4. Keep impact analysis **ADVISORY**: a change in Project A must never auto-edit, auto-upgrade, approve, or mutate Project B/C.
  5. Define AI-ControlTower/OpenViking use as derived traversal/index assistance only; Project-local authoritative sources remain the basis for material impact claims.
  6. Define behavior for stale/orphan/conflicted relations, unavailable target Projects, merges/splits, and Brownfield Projects without `92`.
- **Implementation boundary:** Task registration only. Do not add `[Impact]` or another command, graph traversal runtime, OpenViking automation, cross-Project mutation, or notification mechanism until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** Framework `1.11.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines impact vocabulary, evidence/provenance, direct/indirect reasoning, advisory boundary, Project Graph/OpenViking integration, stale/conflict/unknown behavior, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** Wait for further requirements; when TASK-029 is selected for development, prepare its architectural design spec before implementation.

## Task #30 — Cross-Project Relation Reconciliation

- **ID:** `TASK-030`
- **Status:** `TODO`
- **Type:** Framework architecture / federated Project-relation lifecycle governance
- **Problem:** Framework 1.6.0 defines `REL-*` assertions and `ASSERTED | CORROBORATED | CONFLICTED | RETIRED`, but it does not yet define a complete workflow for discovering, requesting, validating, and revalidating compatible reciprocal assertions across Projects.
- **Approved direction:** Define a relation-reconciliation contract that preserves each Project's authority while allowing evidence-based corroboration and explicit conflict handling.
- **Scope:**
  1. Define counterpart discovery and reciprocal-compatibility checks for applicable core relation types.
  2. Define corroboration request/review semantics without synthesizing another Project's authoritative assertion.
  3. Define endpoint UUID, evidence, freshness, and review requirements for `CORROBORATED`.
  4. Define `CONFLICTED` behavior when authoritative assertions cannot be reconciled.
  5. Define stale/unavailable counterpart behavior without auto-retiring valid local assertions.
  6. Preserve OpenViking/AI-ControlTower as `DERIVED_ONLY` traversal/index assistance, never relation authority.
  7. Reuse existing `DRIFT-*`, `CONFLICT-*`, and `MIG-*` families when material.
- **Implementation boundary:** Task registration only. Do not add reconciliation runtime, cross-Project writes, graph sync, notifications, or automatic reciprocal assertions until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** Framework `1.11.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines counterpart discovery, reciprocal compatibility, corroboration/conflict lifecycle, evidence/freshness, unavailable/stale handling, authority boundaries, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** When TASK-030 is selected, prepare its architectural design spec before implementation.

## Task #31 — Project Event & Notification Contract

- **ID:** `TASK-031`
- **Status:** `TODO`
- **Type:** Framework architecture / governed Project event and notification semantics
- **Problem:** Audit, impact analysis, dependency failures, relation changes, risks, and other material events may require attention, but ProjectFramework does not yet define when an event is notification-worthy, who should be informed, or how delivery/acknowledgement relates to Project authority.
- **Approved direction:** Define a vendor-neutral event/notification governance contract while keeping notification delivery separate from approval and mutation authority.
- **Scope:**
  1. Define notification-worthy event categories and severity/urgency semantics.
  2. Define recipient/owner resolution, acknowledgement, escalation, and deduplication behavior.
  3. Define notification provenance/evidence sufficient to know what was signaled and why.
  4. Define failure behavior for unresolved recipients, unavailable delivery channels, repeated events, and stale notifications.
  5. Preserve `notification ≠ approval` and `notification ≠ authority`.
  6. Define integration boundaries with TASK-028 Audit, TASK-029 Impact Analysis, TASK-030 Relation Reconciliation, and existing `RISK-* / ISS-* / DRIFT-* / CONFLICT-*` semantics.
- **Implementation boundary:** Task registration only. Do not create email/Slack/webhook delivery, schedulers, watchers, or notification automation until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** Framework `1.11.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines event eligibility, severity, recipient/ack/escalation semantics, deduplication, failure handling, evidence, authority separation, integration boundaries, and verification strategy.
- **Exact Next Step:** When TASK-031 is selected, prepare its architectural design spec before implementation.

## Task #32 — Governed Project Repair / Remediation

- **ID:** `TASK-032`
- **Status:** `TODO`
- **Type:** Framework workflow / integrity remediation governance
- **Problem:** TASK-028 intentionally preserves `Audit finds ≠ Audit fixes`; ProjectFramework therefore needs a separate governed workflow for proposing and executing repairs after integrity, drift, stale-reference, binding, or continuity findings.
- **Approved direction:** Define a repair/remediation contract that converts findings into bounded, reversible, authority-checked remediation work without automatic semantic repair.
- **Scope:**
  1. Define remediation proposal structure, affected scope, risk classification, prerequisites, and ownership.
  2. Define authority/approval requirements and sequencing for repair actions.
  3. Define rollback/reversibility and post-repair verification.
  4. Define when semantic conflicts require explicit Decision/approval instead of repair automation.
  5. Define post-remediation re-audit or resulting-state confirmation behavior.
  6. Reuse existing `ISS-*`, `DRIFT-*`, `CONFLICT-*`, `MIG-*`, `CR-*`, and `ACT-*` homes rather than creating parallel authoritative issue families.
- **Implementation boundary:** Task registration only. Do not register a repair command, auto-fix Project Source, migrate automatically, push, or mutate external/shared state until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** Framework `1.10.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines repair proposal/lifecycle, authority/risk gates, sequencing, rollback, semantic-conflict boundaries, post-repair verification, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** When TASK-032 is selected, prepare its workflow/design spec before implementation.

## Task #33 — Task Dependency & Portfolio Planning

- **ID:** `TASK-033`
- **Status:** `TODO`
- **Type:** Framework development workflow / backlog dependency and prioritization contract
- **Problem:** The durable Task source records lifecycle state but does not yet provide a standard model for Task-to-Task dependencies, blockers, enablers, parallelism, priority, or readiness across the ProjectFramework roadmap.
- **Approved direction:** Define a bounded Task planning contract so agents can determine sequencing and safe parallel work without conflating development-task relationships with Project Source `DEP-*` management objects.
- **Scope:**
  1. Define Task relationship semantics such as Depends On, Blocks, Enables, and Parallelizable With.
  2. Define priority/readiness and dependency-resolution rules without inventing dependencies from proximity or numbering.
  3. Distinguish Task/backlog dependency metadata from canonical Project-management `DEP-*` semantics.
  4. Define behavior for circular, stale, cancelled, superseded, or unknown dependencies.
  5. Define how planning should expose a recommended execution order while preserving user authority to reprioritize.
  6. Keep scheduling/automation out of scope unless separately authorized.
- **Implementation boundary:** Task registration only. Do not add schedulers, automatic task execution, agent orchestration, or rewrite existing Task history until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** Framework `1.7.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines Task relationship vocabulary, priority/readiness, dependency validation, parallelism, stale/cycle handling, `DEP-*` separation, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** When TASK-033 is selected, prepare its workflow/design spec before implementation.

## Task #34 — Agent / Model Capability Profile

- **ID:** `TASK-034`
- **Status:** `TODO`
- **Type:** Framework architecture / agent and model capability governance
- **Problem:** TASK-027 can govern which tools/MCPs a Project prefers, but ProjectFramework does not yet define which agent/model capability classes are appropriate for different work, context, disclosure, or review requirements.
- **Approved direction:** Define a vendor-neutral Agent/Model Capability Profile while preserving the invariant `Capability ≠ Authority`.
- **Scope:**
  1. Define capability classes for reasoning, coding, research, review, council participation, and other applicable roles without binding to one vendor.
  2. Define local/external provider distinctions and relevant context/tool/disclosure constraints.
  3. Define capability eligibility and required review for sensitive or high-risk work.
  4. Preserve `Capability ≠ Authority`: model fitness never grants mutation, approval, deployment, disclosure, or binding authority.
  5. Define unavailable/degraded capability and fallback behavior.
  6. Define integration boundaries with TASK-024 `[Meeting]`, TASK-026 Disclosure Governance, and TASK-027 Tool/MCP Execution Profile.
- **Implementation boundary:** Task registration only. Do not add model routing, provider calls, automatic delegation, runtime selection, or permission grants until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** Framework `1.8.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines capability vocabulary, eligibility/review rules, local/external distinctions, fallback/degraded behavior, authority separation, integration boundaries, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** When TASK-034 is selected, prepare its architectural design spec before implementation.

## Task #35 — Project Release / Publication Contract

- **ID:** `TASK-035`
- **Status:** `TODO`
- **Type:** Framework release / publication lifecycle governance
- **Problem:** ProjectFramework distinguishes `commit ≠ push` and has verification/integration semantics, but it does not yet define one standard lifecycle separating implementation completion, merge, remote publication, release, artifact publication, and deployment.
- **Approved direction:** Define a release/publication contract that makes each publication state explicit and evidence-backed without making immutable tags or deployment universal prerequisites.
- **Scope:**
  1. Define distinctions among Task DONE, MERGED, PUSHED/PUBLISHED, RELEASED, artifact publication, and DEPLOYED states.
  2. Define Release Candidate identity, required evidence, approval, and resulting-state confirmation.
  3. Define optional tag/artifact/repository assurance without fabricating provenance or making optional assurance mandatory.
  4. Define release rollback, retraction/supersession, and failed/partial publication behavior.
  5. Define relationship with `RELEASE_FULL`, `INTEGRATION_GATE`, Change Log, and Task completion evidence.
  6. Preserve release/publication authority as separate from implementation authority.
- **Implementation boundary:** Task registration only. Do not create CI/CD, release bots, package publishers, deployment automation, tags, or remote pushes until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** Framework `1.12.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines release/publication states, candidate identity, evidence/approval, assurance, partial/failure/rollback behavior, verification integration, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** When TASK-035 is selected, prepare its release/publication design spec before implementation.

## Task #36 — Project Change/Event History Feed

- **ID:** `TASK-036`
- **Status:** `TODO`
- **Type:** Framework architecture / bounded derived Project change projection
- **Problem:** Cross-Project indexing, Project Knowledge, and impact reasoning should not need to rescan the entire Project to determine what changed since a prior observation, while `10 Change Log` and authoritative Git/Project Source must remain the real history sources.
- **Approved direction:** Define a rebuildable bounded change/event feed as a derived projection with durable source pointers, never as a new authority.
- **Scope:**
  1. Define change-feed entries for changed Stable IDs, documents/surfaces, relation records, lifecycle state, and evidence pointers when material.
  2. Define incremental `since`/checkpoint semantics and ordering without replacing authoritative history.
  3. Define rebuildability from Project Source/history and behavior when feed state is stale, missing, or corrupted.
  4. Define integration boundaries with TASK-025 Project Knowledge, AI-ControlTower/OpenViking, and TASK-029 Impact Analysis.
  5. Preserve derived-feed data as non-authoritative routing/index evidence.
  6. Define retention/bounding behavior sufficient for incremental consumers without creating an unbounded execution log.
- **Implementation boundary:** Task registration only. Do not create watchers, crawlers, webhooks, change daemons, indexing runtimes, or background automation until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** Framework `1.9.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines feed identity/schema, delta/checkpoint semantics, rebuildability, stale/corrupt handling, bounded retention, authority separation, integration boundaries, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** When TASK-036 is selected, prepare its architectural design spec before implementation.

## Task #37 — Security & Trust Boundary Contract

- **ID:** `TASK-037`
- **Status:** `TODO`
- **Type:** Framework architecture / Project security and trust-boundary governance
- **Problem:** TASK-026 governs outbound AI disclosure, but Project security also spans repositories, runtimes, external services, MCPs, artifacts, code execution, supply-chain inputs, and privileged environments.
- **Approved direction:** Define a Project-level Security & Trust Boundary contract that complements existing secret/disclosure/authority rules without introducing a security runtime by implication.
- **Scope:**
  1. Define trust-boundary vocabulary for trusted, limited-trust, untrusted, privileged, and external surfaces as appropriate to design review.
  2. Define rules for data, code, artifacts, and execution crossing trust boundaries.
  3. Define provenance, review, approval, and evidence expectations for material boundary crossings.
  4. Preserve `17 Secret Reference Registry` and TASK-026 disclosure rules; do not duplicate secret values or disclosure authority.
  5. Define integration with Repository/Local Workspace/Runtime authority, external services, MCP/tool profiles, and agent/model capability profiles.
  6. Define unknown/unclassified trust behavior as fail-closed for materially sensitive actions.
- **Implementation boundary:** Task registration only. Do not add scanners, sandbox enforcement, policy engines, supply-chain automation, runtime isolation, or external security services until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** Framework `1.8.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines trust vocabulary, crossing rules, provenance/evidence, approval/fail-closed behavior, secret/disclosure separation, integration boundaries, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** When TASK-037 is selected, prepare its architectural design spec before implementation.

## Task #38 — Framework Source Naming & Distribution-Root Migration

- **ID:** `TASK-038`
- **Status:** `DONE`
- **Type:** Framework architecture / distribution-root naming and migration governance
- **Problem:** The Framework distribution currently lives under `managing-project-source/`, while governed Project truth lives under `Project-Source/`. Once ProjectFramework itself adopts its own `Project-Source/`, those names are too easy for Humans/Agents to conflate, weakening the distinction between Framework distribution source and Project-specific governance source.
- **Approved direction:** Rename the canonical Framework distribution root to `Framework-Source/` so the repository has an explicit paired distinction: `Framework-Source/` = reusable Framework distribution; `Project-Source/` = authoritative governance/current truth for one Project.
- **Scope:**
  1. Define exact canonical naming/casing as `Framework-Source/` and preserve `Project-Source/` for Project-specific governance.
  2. Define the authority boundary: `Framework-Source/` is upstream/distribution source and does not become the consuming Project's Project Source or Root Governance; `Project-Source/00 / FRAMEWORK-001` remains Project authority after bootstrap.
  3. Inventory current active references to `managing-project-source/` and classify which current distribution/bootstrap/documentation surfaces must move or be rewritten versus which historical specs/evidence/amendments must remain byte/provenance preserving.
  4. Define repository-path migration for `FRAMEWORK-RELEASE.yaml`, launchers, templates, README/bootstrap instructions, migration notes, tests, and other current entrypoints without silently breaking deterministic discovery.
  5. Define compatibility behavior for external/Brownfield consumers that still reference `managing-project-source/`; no automatic rewrite of initialized Projects, external repositories, local Project pins, or user environments.
  6. Preserve `PROJECT-BOOTSTRAP.md` as the stable Project-root entrypoint introduced in Framework `1.7.0`; directory renaming must not create a second Project bootstrap or authority root.
  7. Define verification for stale-path detection, current-reference alignment, historical provenance preservation, launcher constraints, release descriptor routing, and Direct-to-Latest migration guidance.
  8. Sequence this migration before other Framework `1.8.0` Tasks that would otherwise add new references to the old distribution-root name.
- **Implementation boundary:** Task registration only. Do not rename/move `managing-project-source/`, rewrite current paths, alter historical evidence/specs, create compatibility aliases, or update external Projects until a separate design spec is completed and explicitly approved.
- **Design Spec:** `docs/superpowers/specs/2026-08-29-task038-framework-source-rename-design.md`
- **Design State:** `USER_APPROVED_DESIGN / SPEC_APPROVED`
- **Implementation Plan:** `docs/superpowers/plans/2026-08-29-task038-framework-source-rename.md`
- **Plan State:** `IMPLEMENTATION_PLAN_EXECUTED`
- **Design Approval:** User explicitly selected `Framework-Source/` vs `Project-Source/` naming and authorized continuous development without repeated approval prompts on `2026-08-29`; push/publication remains separately governed.
- **Target Release:** Framework `1.8.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if repository-path compatibility requires a different release classification)
- **Completion criteria:** A user-approved design defines canonical directory naming, Framework-vs-Project authority separation, current/historical path classification, migration/backward-compatibility behavior, affected surfaces, sequencing within 1.8.0, rollback, and verification strategy before any rename occurs.
- **Implementation Release:** Framework `1.8.0` / Schema `1.0.0` / release format `3`
- **Implementation Commit(s):** `80ac496`, `fb24141`, `5757660`, `d068914`, `3c053be`
- **Release Evidence:** `docs/superpowers/evidence/2026-08-29-task-038-framework-source-rename-release-full.md`
- **Verification Result:** `AFFECTED 74/74 PASS; RELEASE_FULL 198/198 PASS`
- **Candidate Commit:** `d068914e5fdc12eb9055ff5bae28cf57962495b4`
- **Candidate Tree:** `f6c6bba9113308d60354112245f4d7574a350191`
- **Framework-Source Tree:** `5e254140867195c37a2eef9ce6aadb03890af858`
- **Completion criteria met:** one canonical `Framework-Source/`; no live old-root alias; current routes/starter/launcher surfaces aligned; historical path provenance preserved; ProjectFramework active Project Source reconciled without auto-upgrading its local Framework `1.7.0` pin; scenarios `1–188`; AFFECTED and final unchanged-candidate RELEASE_FULL passed.
- **Publication State:** `NOT_PUSHED`
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป

## Task #39 — `[Goal]` Persistent Continuous Goal Execution Command

- **ID:** `TASK-039`
- **Status:** `DONE`
- **Type:** Framework command / persistent goal authorization and continuous execution governance
- **Problem:** GPT-Web/Agents can repeatedly stop for approval even after the user has clearly asked for continuous work. `[Session Envelope]` pre-approves bounded operations only for a session and intentionally keeps several fail-closed gates. ProjectFramework needs a durable Project-level command that captures one user-authorized outcome and the exact authorization boundary needed to resume across chats without re-requesting approval for already-authorized work.
- **Approved direction:** Register `[Goal]` as a **PERSISTENT** goal command. A Goal persists in Project Source across chats until terminal state and allows continuous in-scope execution without repeated Framework-level approval prompts. Goal authorization is bounded user authorization, never Agent self-approval and never a bypass of higher-level platform/tool/safety confirmation requirements.
- **Canonical composition:** Do not create a parallel `GOAL-*` Stable-ID family. Represent the Goal's intended result as `OUT-*` in `91 Project Management Control`; persist user-granted execution authority as `AUTH-*` in `12 Authorization Registry`; decompose execution into `ACT-*` plus session-bounded `ENV-*` in `15 Action Registry`; persist continuation pointers in `09 Handoff` with `authority_transfer: false`.
- **Scope:**
  1. Define literal bracketed `[Goal]` command syntax, case-insensitive registered-name matching, goal statement parsing, bounded scope, success criteria, prohibited zones, and terminal behavior.
  2. Define persistent lifecycle/resume semantics so a new chat can bootstrap `PROJECT-BOOTSTRAP.md → 00 → 01 → 03 → 09`, resolve the active `OUT-* / AUTH-* / ACT-*`, fresh-check mutable prerequisites, and continue without asking the user to re-authorize already-covered work.
  3. Pre-authorize normal **local development workflow** within the Goal scope: design, planning, file edits, tests, debugging/fixes, local verification, commits, and Logical Checkpoints. Framework-level approval must not be requested again solely for an operation already covered by the active Goal authorization.
  4. Keep `ACT DONE ≠ OUT ACHIEVED`. Goal completion requires explicit success criteria plus sufficient evidence before the related `OUT-*` is marked achieved; completing implementation Tasks alone does not prove the Goal outcome.
  5. **Push/publication policy:** push is not included by default. It may be pre-authorized only when the Goal explicitly includes publish/push and identifies the intended governed target. Target mismatch, changed/unresolved binding, or stale integration evidence fails closed. `commit ≠ push` remains true.
  6. **Destructive-action policy:** destructive actions are not included by default. They may be pre-authorized only when the Goal explicitly names the destructive operation and target. Authorization must not be generalized to other destructive effects.
  7. **Root Governance / Project Location Binding policy:** Root/binding mutation is not included by default. It may be pre-authorized only when the Goal explicitly identifies the intended governance/location change and target; normal revision/validate/promote/supersede/archive and resulting-state verification still apply.
  8. **Secrets / disclosure policy:** a Goal may authorize use of governed secret references when otherwise allowed, but never storage or disclosure of actual secret values in Project Source. External AI/provider disclosure remains subject to TASK-026 disclosure governance or equivalent explicit authorization; `[Goal]` does not create blanket outbound-disclosure authority.
  9. Define out-of-scope behavior: block only the affected unauthorized action when independent in-scope work can safely continue; stop the whole Goal only when the blocker is global, authority is unresolved, required evidence conflicts, success criteria require material requirement change, or safe continuation is impossible.
  10. Define conflict behavior for multiple active Goals/authorizations. A later Goal must not silently override another active Goal, `REQ-*`, `DEC-*`, `AUTH-*`, Root Governance, or Project Location Binding; material semantic conflicts use existing `CONFLICT-*` handling and fail closed for affected work.
  11. Define cancellation/supersession/revocation so user withdrawal immediately prevents future execution under the revoked Goal while preserving history and completed evidence.
  12. Compose with `[Session Envelope]`: persistent `AUTH-*` is the durable cross-chat authority basis; session/task `ENV-*` may be created/refreshed from that authority without new user approval, but must remain within the Goal and parent authorization scope.
  13. Preserve higher-level constraints: ProjectFramework may remove redundant **Framework-level** approval prompts, but `[Goal]` cannot override system/developer instructions, product safety policy, MCP/tool confirmation rules, authentication requirements, or other mandatory platform controls.
  14. Define command help/discovery, Project Status visibility, Handoff representation, launcher compaction, GREENFIELD/Brownfield behavior, migration compatibility, and pressure scenarios covering overreach, stale authority, new-chat resume, push/destructive/root/secret boundaries, conflict, cancellation, and outcome verification.
  15. Sequence implementation after TASK-038 distribution-root migration so new Framework `1.8.0` command surfaces are authored against canonical `Framework-Source/` rather than adding new current references to `managing-project-source/`. Design work may proceed before TASK-038 implementation when it does not create current distribution-path dependencies.
- **Implementation boundary:** Task registration/design only. Do not register `[Goal]` in current Framework commands, create active Goal/OUT/AUTH records for ordinary work, weaken current approval gates, alter `[Session Envelope]`, or implement launcher/template/runtime behavior until a separate architectural design spec is completed and explicitly approved.
- **Design Spec:** `docs/superpowers/specs/2026-08-29-task039-persistent-goal-command-design.md`
- **Design State:** `USER_APPROVED_DESIGN / SPEC_APPROVED`
- **Design Approval:** User explicitly authorized continuous TASK-039 development without repeated approval prompts on `2026-08-29`; higher-level system/tool/platform gates and TASK-038 sequencing remain binding.
- **Implementation Plan:** `docs/superpowers/plans/2026-08-29-task039-persistent-goal-command.md`
- **Plan State:** `IMPLEMENTATION_PLAN_EXECUTED`
- **Target Release:** Framework `1.8.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if the final authorization/lifecycle contract requires a breaking schema change)
- **Completion criteria:** A user-approved design defines command syntax, persistent Goal representation, OUT/AUTH/ACT/ENV/09 composition, local-development pre-authorization, push/destructive/root-binding/secret-disclosure boundaries, lifecycle/resume/revocation/conflict behavior, outcome evidence, platform-boundary limitations, affected Framework surfaces, migration behavior, and verification strategy before implementation begins.
- **Implementation Commit(s):** `47aadac`, `25b335d`, `4b3ce45`, `0f2ecfd`, `b7f63bb`
- **Release Evidence:** `docs/superpowers/evidence/2026-08-29-task-039-persistent-goal-command-release-full.md`
- **Verification Result:** `AFFECTED 43/43 PASS; RELEASE_FULL 220/220 PASS`
- **Candidate Commit:** `0f2ecfde7112a7d7d101e316fc0c3069c8ece5db`
- **Candidate Tree:** `a3adaeef91d3a729f9d14d570400ed73b47ee3a2`
- **Framework-Source Tree:** `2101c2d22b9d23d0bae3517a6462c4895edecf15`
- **Completion criteria met:** `[Goal]` registered with literal brackets/case-insensitive matching; persistent OUT/AUTH/ACT/ENV/09 composition; default bounded local development authority; exact push/destructive/Root-Binding/disclosure opt-ins; cancellation/conflict/outcome-evidence semantics; Brownfield no-auto-Goal; scenarios 1–211; launcher parity/size; historical integrity; final verification PASS.
- **ProjectFramework active Goal record:** `NOT_MATERIALIZED` — ordinary continuous-work wording was not retroactively converted into `[Goal]` authority.
- **Publication State:** `NOT_PUSHED`
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
