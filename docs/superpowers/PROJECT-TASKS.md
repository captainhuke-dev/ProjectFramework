# ProjectFramework Project Task Source

This file is the durable Workspace source for ProjectFramework development Task lifecycle state, including backlog, in-progress, blocked, cancelled, and completed Tasks. Design specs, implementation plans, and evidence are referenced from each Task rather than duplicated here.

Task numbers in this file are backlog sequence numbers. They are **not** Project Source semantic document slots; Framework slots `18–19` remain RESERVED.

## Status vocabulary

- `TODO` — accepted into the Project backlog; implementation has not started.
- `IN_PROGRESS` — implementation work has started.
- `DONE` — required scope is complete and applicable verification/completion evidence exists.
- `BLOCKED` — work cannot proceed until a stated blocker is resolved.
- `CANCELLED` — work was intentionally closed without implementation completion.

## Remaining-work reporting policy

- Remaining-work / "what is left" summaries include only Tasks whose current status is `TODO`, `IN_PROGRESS`, or `BLOCKED`.
- `CANCELLED` is historical lifecycle state and is omitted from remaining-work summaries unless the user explicitly asks for cancelled/history.
- A proposed/future scope that was never accepted as an active Task is not backlog. When the user explicitly cancels such unstarted scope, preserve needed history/provenance but do not continue presenting it as pending work.
- Current backlog: `TODO=0 / IN_PROGRESS=0 / BLOCKED=0` (TASK-058 DONE locally 2026-09-16; Framework 1.20 candidate frozen at `63f2640` with RELEASE_FULL PASS_RUN_1; publication and post-1.20 self-host promotion separately governed).

## Cancelled — never-registered scope (2026-09-14, user decision)

- `TASK-053` (Governance Friction Benchmark): never registered as an authorized Project task (reviewer-invented registration, already excluded from terminal truth by TASK-052). Explicitly cancelled by the user on 2026-09-14. No work, branch, or PR exists for it.
- `TASK-056` (Fast Path Reconciliation): proposed but never registered in this file and never present in any commit, branch, or PR. Explicitly cancelled by the user on 2026-09-14. No work, branch, or PR exists for it.

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
- **Status:** `DONE`
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
- **Design Spec:** `docs/superpowers/specs/2026-08-29-task024-meeting-llm-council-design.md`
- **Design State:** `USER_APPROVED_DESIGN / WRITTEN_SPEC_APPROVED`
- **Design Approval:** User approved the presented Thin Council Provider Adapter architecture and, after the written spec was committed, explicitly approved continued execution on `2026-08-29`; implementation planning is now authorized while higher-level system/tool/platform gates remain binding.
- **Verified Provider Snapshot:** `captainhuke-dev/llm-council` public fork, `master` commit `92e1fccb1bdcf1bab7221aa9ed90f9dc72529131`, tree `221d8afb6eca87537282d509971c505119390e0b`; compared parent `karpathy/llm-council` master was the same commit at design capture.
- **Chosen Architecture:** Thin Council Provider Adapter — ProjectFramework owns `[Meeting]` semantics and advisory/evidence boundaries; llm-council remains an external provider/runtime whose UI/JSON storage never becomes Project authority.
- **Spec Self-Review:** `PASS 18/18` — provider provenance, advisory-authority separation, disclosure/secret boundaries, partial-failure semantics, no `MEETING-*`, release classification, and verification scope checked.
- **Implementation Plan:** `docs/superpowers/plans/2026-08-29-task024-meeting-llm-council.md`
- **Plan State:** `IMPLEMENTATION_PLAN_EXECUTED / INLINE_CONTINUOUS_EXECUTION_APPROVED`
- **Plan Self-Review:** `PASS 30/30` — spec coverage, scenario range `212–227`, provider snapshot, no-runtime boundary, starter/launcher/evidence surfaces, and AFFECTED/RELEASE_FULL lifecycle checked.
- **Implementation Provider Freshness:** fork `master` freshly re-observed at `92e1fccb1bdcf1bab7221aa9ed90f9dc72529131` / tree `221d8afb6eca87537282d509971c505119390e0b`; no material provider-profile drift before Task 1 mutation.
- **Implementation Scenario Contract:** RED scenarios `212–227` added; Framework-wide numbering target `1–227` contiguous/unique.
- **Target Release:** Framework `1.8.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines command syntax, council input/context boundary, verified llm-council integration contract, advisory-authority separation, result structure, failure/partial-response behavior, persistence/evidence rules, affected Framework surfaces, and verification strategy before implementation begins.
- **Implementation Release:** Framework `1.8.0` / Schema `1.0.0` / release format `3`
- **Implementation Commit(s):** `d5a0b21`, `c396588`, `c5b21ec`, `ff74ab8`, `e1c8ba0`, `a4ab736`
- **Release Evidence:** `docs/superpowers/evidence/2026-08-29-task-024-meeting-llm-council-release-full.md`
- **Verification Result:** `AFFECTED 55/55 PASS; RELEASE_FULL 314/314 PASS`
- **Candidate Commit:** `e1c8ba0ad40fe956911043ff98239b7682a3d23e`
- **Candidate Tree:** `3cae37a05c97a3efa66ffb6f2e1cf941579187aa`
- **Framework-Source Tree:** `9a959e20723c28c58e7b37be7fd52aef8501d8f1`
- **Completion criteria met:** `[Meeting]` registered with literal brackets/case-insensitive matching; Thin Council Provider Adapter separation; minimum-authorized outbound context; secret-value prohibition; independent views/disagreement/peer signal/Chairman synthesis/limitations; Council/majority/Chairman advisory-only boundary; `COMPLETE | PARTIAL | FAILED | UNAVAILABLE`; material `EVD-*` persistence; no `MEETING-*` family/provider JSON authority/runtime implementation; Goal/ENV disclosure separation; Brownfield no-auto-Meeting; scenarios 1–227; launcher parity/size; final verification PASS.
- **Publication State:** `NOT_PUSHED`

- **Exact Next Step:** Prepare TASK-026 External AI Context & Disclosure Governance architectural design before implementation.
## Task #25 — Project Knowledge Layer / Compounding Knowledge Contract

- **ID:** `TASK-025`
- **Status:** `DONE`
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
- **Design State:** `USER_APPROVED_DESIGN / WRITTEN_SPEC_APPROVED`
- **Design Approval:** User explicitly invoked `[Goal] ทำจนจบ task` on 2026-09-01; committed written spec approved to proceed without changes.
- **Implementation Plan:** `docs/superpowers/plans/2026-09-01-task025-project-knowledge-layer.md`
- **Plan Commit:** `187c802`
- **Plan Self-Review:** `PASS 43/43`
- **Plan State:** `IMPLEMENTATION_PLAN_EXECUTED`
- **Execution Progress:** Tasks 1–4 executed; RED `33/68 FAIL` expected → structural GREEN `68/68 PASS`; Task 2 `62/62 PASS`; Task 3 `77/77 PASS`; AFFECTED `175/175 PASS`; invalidated candidate `2688c995448131b2154b3fa505acaef6352389d3`; corrected candidate `99c2f5a90e0c8f02dd68001d0e22b5362cd45a03`; final RELEASE_FULL `120/120 PASS`; release evidence committed; terminal Goal reconciliation completed locally.
- **Design Spec:** `docs/superpowers/specs/2026-09-01-task025-project-knowledge-layer-design.md`
- **Spec Self-Review:** `TASK025_SPEC_SELF_REVIEW 42/42 PASS`
- **Source Concept Freshness:** `llm-wiki` gist freshly read on `2026-09-01`; adopted concepts are raw sources / LLM-maintained Markdown wiki / schema layer, `index.md`, chronological `log.md`, and ingest/query/lint; implementation assumptions remain non-binding.
- **Chosen Architecture:** `Derived Markdown Knowledge Layer` — optional root `Project-Knowledge/` with `README.md`, `index.md`, `log.md`, and `pages/`; raw/source material remains source-native by default; Knowledge is advisory/derived and cannot auto-promote into Project Source.
- **Design Gate:** SATISFIED — written spec explicitly approved by user `[Goal]`; implementation completed under AUTH-003.
- **Target Release:** Framework `1.10.0` / Schema `1.0.0` / release format `3` — reclassified from the original 1.9.0 roadmap placeholder because the 1.9.0 line is already released and TASK-025 adds a new optional additive Framework interface; no Project Source schema/slot change.
- **Completion criteria:** A user-approved design defines authority separation, knowledge schema/lifecycle, provenance, indexing/log/lint behavior, contradiction/staleness handling, promotion gates, TASK-023/TASK-024/OpenViking integration boundaries, Brownfield behavior, affected Framework surfaces, and verification strategy before implementation begins.
- **Goal State:** `OUT-003 ACHIEVED / AUTH-003 TERMINATED / ACT-013 DONE / ENV-003 EXPIRED`; no future TASK-025 execution authority remains.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป

- **Implementation Commit(s):** RED `64823a9`; normative `1c7be78`; templates/propagation `ed5aa4d`; corrected candidate `99c2f5a90e0c8f02dd68001d0e22b5362cd45a03`.
- **Structural GREEN:** `TASK025_RED 68/68 PASS`; scenarios `1–288` contiguous/unique.
- **Affected Verification:** `TASK025_AFFECTED 175/175 PASS`; 4 Knowledge starter files; 22 maintained Project Source starter stamps at Framework `1.10.0` / Schema `1.0.0`; launchers unchanged; documentation/YAML only.
- **Invalidated Candidate:** `2688c995448131b2154b3fa505acaef6352389d3` — RELEASE_FULL `119/120 FAIL` solely because `git diff --check` found extra EOF blank lines in three branch-created archived Project Source revisions; semantic/AFFECTED checks remained PASS; candidate invalidated before evidence reuse.
- **Candidate Commit:** `99c2f5a90e0c8f02dd68001d0e22b5362cd45a03`
- **Candidate Tree:** `26d1f5354ab0a59616b9fbca28d25c74ac6746ca`
- **Framework-Source Tree:** `d39c4550a4272e3ae2c5f957ec444f93bd514485`
- **Release Evidence:** `docs/superpowers/evidence/2026-09-01-task-025-project-knowledge-release-full.md`
- **Release Evidence Commit:** `e428eaa52de64546138fc4ca46fe84f1aa697e7f`
- **Verification Result:** structural GREEN `68/68 PASS`; Task 2 `62/62 PASS`; Task 3 `77/77 PASS`; AFFECTED `175/175 PASS`; RELEASE_FULL `120/120 PASS`; scenarios `1–288`; 4 Knowledge templates; 22 maintained starter stamps at Framework `1.10.0` / Schema `1.0.0`.
- **Completion Criteria Met:** optional Derived Markdown Project Knowledge layer; Knowledge≠Authority; provenance/index/log/page/lifecycle/promotion contracts; Meeting/EVD/TASK-026/03/09/92/OpenViking boundaries; GREENFIELD optionality/Brownfield safety; no runtime/CLI/vector/wiki/MCP service; final state-bound evidence committed; Goal terminalized locally.
- **Publication State:** `MERGED_TO_MAIN / PERSISTED`
- **Completed-work Integration Evidence:** `docs/superpowers/evidence/2026-09-02-completed-work-main-integration-release-full.md` / `0c8d972`
- **Canonical Main Integration:** `b8697f17c6d5de9835edfb9248229e5e3bf6525f` / Framework-Source tree `993b481c0d36057108df0eb87e41194bead64577` / EVD-042 verified
## Task #26 — External AI Context & Disclosure Governance

- **ID:** `TASK-026`
- **Status:** `DONE`
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
- **Design Spec:** `docs/superpowers/specs/2026-08-30-task026-external-ai-context-disclosure-design.md`
- **Design State:** `USER_APPROVED_DESIGN / WRITTEN_SPEC_APPROVED`
- **Design Approval:** User explicitly approved the presented Compositional Disclosure Boundary architecture and, after the written spec was committed/persisted, explicitly approved continued execution on `2026-08-30`; implementation planning is authorized while higher-level system/tool/platform gates remain binding.
- **Chosen Architecture:** Compositional Disclosure Boundary — reuse `AUTH-*`, `EVD-*`, and `SECRET-*`; classify outbound context as `EXTERNAL_OK | EXTERNAL_REVIEW | DO_NOT_DISCLOSE | UNCLASSIFIED`; provider/tool eligibility remains independent; no `DISC-*` family or new semantic slot.
- **Spec Self-Review:** `PASS 21/21` — classification/authorization separation, provider eligibility, minimum-context/redaction, mixed-sensitivity behavior, secret/EVD boundaries, Meeting/Knowledge/OpenViking/Goal integration, Brownfield/GREENFIELD behavior, release classification, and no-runtime scope checked.
- **Implementation Plan:** `docs/superpowers/plans/2026-08-30-task026-external-ai-context-disclosure.md`
- **Plan State:** `IMPLEMENTATION_PLAN_EXECUTED / INLINE_CONTINUOUS_EXECUTION_APPROVED`
- **Plan Self-Review:** `PASS` — six task checkpoints cover scenarios `228–245`, normative contract, starters, user-facing migration/launcher surfaces, AFFECTED verification, RELEASE_FULL evidence, and final lifecycle reconciliation; placeholder scan and canonical vocabulary checks passed.
- **Implementation Scenario Contract:** RED scenarios `228–245` added; Framework-wide numbering target `1–245` contiguous/unique.
- **Target Release:** Framework `1.8.0` / Schema `1.0.0` (user-approved roadmap target; design must reclassify if a breaking change is explicitly identified and approved)
- **Completion criteria:** A user-approved design defines disclosure vocabulary, context-minimization/redaction rules, provider/tool eligibility, integration boundaries, fail-closed behavior, provenance/evidence requirements, affected Framework surfaces, and verification strategy.
- **Implementation Release:** Framework `1.8.0` / Schema `1.0.0` / release format `3`
- **Implementation Commit(s):** `723ecb1`, `4ad2cef`, `33aad00`, `4c3103d`, `fda8300`
- **Release Evidence:** `docs/superpowers/evidence/2026-08-30-task-026-external-ai-context-disclosure-release-full.md`
- **Verification Result:** `AFFECTED 144/144 PASS; RELEASE_FULL 243/243 PASS`
- **Candidate Commit:** `4c3103dfcf8e454555d234d6b3acc3571c7c2483`
- **Candidate Tree:** `c8d589722a3e404c54f0c5e2351e412712b3927a`
- **Framework-Source Tree:** `d66803fc41c540efcf072e9e45eb98c83d1f1bb5`
- **Completion criteria met:** Compositional Disclosure Boundary implemented with exact disclosure/provider vocabularies; `Classification ≠ Authorization`; standing `AUTH-*` + action-scoped one-off disclosure; minimum-context/redaction/mixed-sensitivity/fail-closed rules; `SECRET-*` reference-only boundary; bounded material `EVD-*`; Meeting/Knowledge/OpenViking/Goal/ENV/tool/model separation; GREENFIELD/Brownfield safety; scenarios 1–245; no `DISC-*` family/slot/runtime disclosure system; launcher change skipped under size gate while parity/ceiling preserved; final verification PASS.
- **Publication State:** `MERGED_TO_MAIN / RECONCILIATION_PERSISTED`
- **Publication Branch:** `task026-external-ai-disclosure`
- **Published Implementation Head at PR Creation:** `ab43da5295ff571c641ed82c2e49bd3e0aa202ce`
- **Pull Request #21:** `MERGED` — merge commit `c729a7b19b7cdc6d4dfdd211437d4a0b2f685da7`; PR head `714108a526db1a492d980690e50b1b484b88f6a1`
- **Main Integration State:** `MERGED`; exact pre-merge gate `PASS 21/21`; merged Framework-Source tree `d66803fc41c540efcf072e9e45eb98c83d1f1bb5`
- **Second-AI Review State:** `WAIVED_BY_USER / NOT_REQUIRED_FOR_PR_21` — action-specific user waiver preserved in `EVD-011`
- **Integration Evidence:** `EVD-009`, `EVD-010`, `EVD-011`, `EVD-012`
- **Post-Merge Reconciliation Pull Request #22:** `MERGED` — merge commit `471debc25ab353b50ace0c43f2533b4d1597d862`; base `c729a7b19b7cdc6d4dfdd211437d4a0b2f685da7`; reconciliation head `a08e774d291deed837c7ad5b5c9e7d8d01faa921`; resulting tree `2867d28b2c25eb9288856deb18ed92a79d415dc1`
- **Reconciliation Publication State:** `PERSISTED / NOT_PENDING`
- **Reconciliation Evidence:** `EVD-013`; Framework-Source tree remains `d66803fc41c540efcf072e9e45eb98c83d1f1bb5`
- **Exact Next Step:** Prepare TASK-025 Project Knowledge Layer / Compounding Knowledge Contract architectural design spec before implementation.

## Task #27 — Project Tool / MCP Execution Profile

- **ID:** `TASK-027`
- **Status:** `DONE`
- **Type:** Framework architecture / Project-scoped execution-tool governance
- **depends_on:** `[TASK-033]`
- **blocks:** `[TASK-034]`
- **enables:** `[TASK-034]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `READY`
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
- **Design State:** `USER_APPROVED_SET1_DIRECTION / WRITTEN_SPEC_APPROVED`
- **Design Spec:** `docs/superpowers/specs/2026-09-01-task027-project-tool-execution-profile-design.md`
- **Design Commit:** `9b0078e`
- **Spec Suite Self-Review:** `PASS 130/130`
- **Suite Implementation Plan:** `docs/superpowers/plans/2026-09-01-set1-foundation-suite.md`
- **Plan Commit:** `8555e09`
- **Plan Self-Review:** `PASS 38/38`
- **Set 1 Suite:** `COMPLETED / OUT-004 ACHIEVED / LOCAL_VERIFIED / PUBLICATION_NOT_PUSHED`
- **Target Release:** Framework `1.12.0` / Schema `1.0.0` / release format `3` — cumulative Set 1 target approved by suite design
- **Completion criteria:** A user-approved design defines execution-profile schema, authority/location separation, primary/fallback/fail behavior, bootstrap integration, Brownfield rules, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
- **Set 1 Completion:** focused `69/69 PASS`; implementation commit `3231695`; completed under OUT-004/AUTH-004.
- **Set 1 Final Acceptance:** structural `159/159 PASS`; cumulative AFFECTED `75/75 PASS`; RELEASE_FULL `108/108 PASS`; candidate `125e10f1d00263ddda0031e02383b179ecd12699`; Framework-Source tree `ce68037371568f98786b62f9afefc47907a91cc6`; evidence `f37a7474235d847f14dca77d54f9c3b217eed11f`.
- **Publication State:** `MERGED_TO_MAIN / PERSISTED`
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
- **Completed-work Integration Evidence:** `docs/superpowers/evidence/2026-09-02-completed-work-main-integration-release-full.md` / `0c8d972`
- **Canonical Main Integration:** `b8697f17c6d5de9835edfb9248229e5e3bf6525f` / Framework-Source tree `993b481c0d36057108df0eb87e41194bead64577` / EVD-042 verified
## Task #28 — `[Project Audit]` Integrity & Drift Command

- **ID:** `TASK-028`
- **Status:** `DONE`
- **Type:** Framework command / Project integrity assessment
- **depends_on:** `[]`
- **blocks:** `[TASK-032]`
- **enables:** `[TASK-032]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `READY`
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
- **Design State:** `USER_APPROVED_DIRECTION / WRITTEN_SPEC_APPROVED_BY_GOAL`
- **Design Spec:** `docs/superpowers/specs/2026-09-02-task028-task032-integrity-remediation-design.md`
- **Spec Self-Review:** `PASS 12/12` — release classification, dependency order, strict audit interface, no-auto-fix boundary, canonical repair routing, Risk/AUTH/rollback/re-audit, scenario range `357–380`, no-runtime/no-new-ID boundaries checked.
- **Implementation Plan:** `docs/superpowers/plans/2026-09-02-task028-task032-integrity-remediation.md`
- **Plan State:** `WRITTEN / SELF_REVIEWED / EXECUTION_AUTHORIZED_BY_GOAL`
- **Plan Self-Review:** `PASS 13/13` — TDD RED ordering, TASK-028→TASK-032 completion gate, exact affected surfaces, cumulative AFFECTED, frozen candidate, one-final-RELEASE_FULL, evidence and terminal reconciliation covered.
- **TDD RED:** scenarios `357–380`; cumulative numbering `1–380`; `TASK028032_STRUCTURAL 14/40 PASS` / expected `26` missing-contract failures on Framework `1.12.2`; no verifier/runtime error.
- **Target Release:** Framework `1.13.0` / Schema `1.0.0` / release format `3` — cumulative Integrity & Remediation Suite target reclassified from the older roadmap placeholder because current canonical Framework is 1.12.2 and TASK-028 adds a Registered Command.
- **Completion criteria:** A user-approved design defines command syntax, audit scope/categories, health vocabulary, evidence/unknown handling, no-auto-fix boundary, integration with existing governance families, affected Framework surfaces, and verification strategy.
- **Implementation State:** `DONE / FOCUSED_VERIFIED` — normative command/release surfaces committed at `a38d514`; `[Project Audit]` focused verifier `23/23 PASS`; suite structural state `32/40 PASS` with only TASK-032/final-propagation checks remaining.
- **Implementation Commit:** `a38d514`
- **Focused Verification:** `TASK028_FOCUSED 23/23 PASS`
- **Completion Checkpoint Evidence:** `EVD-057 / CHG-057`
- **Publication State:** `MERGED_TO_MAIN / PR #28 / merge eda1f2b / PERSISTED / NOT_PENDING`
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป

## Task #29 — Cross-Project Impact Analysis

- **ID:** `TASK-029`
- **Status:** `DONE`
- **Type:** Framework architecture / federated Project-change impact reasoning
- **depends_on:** `[TASK-036, TASK-030]`
- **blocks:** `[TASK-031]`
- **enables:** `[TASK-031]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `READY`
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
- **Design State:** `USER_APPROVED_DIRECTION / WRITTEN_SPEC_APPROVED_BY_GOAL`
- **Design Spec:** `docs/superpowers/specs/2026-09-03-federated-change-intelligence-suite-design.md`
- **Design Commit:** `d061f1f`
- **Spec Self-Review:** `FEDERATED_SPEC_SELF_REVIEW 27/27 PASS`
- **Implementation Plan:** `docs/superpowers/plans/2026-09-03-federated-change-intelligence-suite.md`
- **Plan Commit:** `95c1ca3`
- **Plan Self-Review:** `FEDERATED_PLAN_SELF_REVIEW 23/23 PASS`
- **TDD RED:** scenarios `381–420`; cumulative numbering `1–420`; `FEDERATED_STRUCTURAL 23/40 PASS` / expected `17` missing-contract failures on Framework `1.13.0`; baseline invariants GREEN.
- **Target Release:** Framework `1.14.0` / Schema `1.0.0` / release format `3` — cumulative OUT-008 target reclassified by approved suite design
- **Completion criteria:** A user-approved design defines impact vocabulary, evidence/provenance, direct/indirect reasoning, advisory boundary, Project Graph/OpenViking integration, stale/conflict/unknown behavior, affected Framework surfaces, and verification strategy.
- **Suite:** `OUT-008 Federated Change Intelligence` / waits for both foundation checkpoints before activation
- **Dependency State:** `TASK-036 + TASK-030 SATISFIED` via `5c9ed7c / EVD-066` and `360a1ad / EVD-067`.
- **Implementation State:** `DONE / FOCUSED_VERIFIED` — advisory impact contract implemented without new command/Stable-ID family/runtime; completion commit observed at `daf01eb`.
- **Implementation Commit:** `daf01eb`
- **Focused Verification:** `TASK029_FOCUSED_TEXT 34/34 PASS` — direct context-aware Git/text assertions; no executable verifier artifact.
- **Completion Checkpoint Evidence:** `EVD-068 / CHG-068`
- **Publication State:** `MERGED_TO_MAIN / PR #28 / merge eda1f2b / PERSISTED / NOT_PENDING`
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป

## Task #30 — Cross-Project Relation Reconciliation

- **ID:** `TASK-030`
- **Status:** `DONE`
- **Type:** Framework architecture / federated Project-relation lifecycle governance
- **depends_on:** `[]`
- **blocks:** `[TASK-029]`
- **enables:** `[TASK-029]`
- **parallelizable_with:** `[TASK-036]`
- **priority:** `HIGH`
- **readiness:** `READY`
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
- **Design State:** `USER_APPROVED_DIRECTION / WRITTEN_SPEC_APPROVED_BY_GOAL`
- **Design Spec:** `docs/superpowers/specs/2026-09-03-federated-change-intelligence-suite-design.md`
- **Design Commit:** `d061f1f`
- **Spec Self-Review:** `FEDERATED_SPEC_SELF_REVIEW 27/27 PASS`
- **Implementation Plan:** `docs/superpowers/plans/2026-09-03-federated-change-intelligence-suite.md`
- **Plan Commit:** `95c1ca3`
- **Plan Self-Review:** `FEDERATED_PLAN_SELF_REVIEW 23/23 PASS`
- **TDD RED:** scenarios `381–420`; cumulative numbering `1–420`; `FEDERATED_STRUCTURAL 23/40 PASS` / expected `17` missing-contract failures on Framework `1.13.0`; baseline invariants GREEN.
- **Target Release:** Framework `1.14.0` / Schema `1.0.0` / release format `3` — cumulative OUT-008 target reclassified by approved suite design
- **Completion criteria:** A user-approved design defines counterpart discovery, reciprocal compatibility, corroboration/conflict lifecycle, evidence/freshness, unavailable/stale handling, authority boundaries, affected Framework surfaces, and verification strategy.
- **Suite:** `OUT-008 Federated Change Intelligence` / foundation stream B / cumulative target Framework 1.14.0
- **Implementation State:** `DONE / FOCUSED_VERIFIED` — relation reconciliation workflow implemented over existing REL-* with no cross-Project write/runtime/new family.
- **Implementation Commit:** `360a1ad`
- **Focused Verification:** `TASK030_FOCUSED_TEXT 30/30 PASS` — direct read-only Git/text assertions; no executable verifier artifact.
- **Publication State:** `MERGED_TO_MAIN / PR #28 / merge eda1f2b / PERSISTED / NOT_PENDING`
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป

## Task #31 — Project Event & Notification Contract

- **ID:** `TASK-031`
- **Status:** `DONE`
- **Type:** Framework architecture / governed Project event and notification semantics
- **depends_on:** `[TASK-029, TASK-030]`
- **blocks:** `[]`
- **enables:** `[]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `READY`
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
- **Design State:** `USER_APPROVED_DIRECTION / WRITTEN_SPEC_APPROVED_BY_GOAL`
- **Design Spec:** `docs/superpowers/specs/2026-09-03-federated-change-intelligence-suite-design.md`
- **Design Commit:** `d061f1f`
- **Spec Self-Review:** `FEDERATED_SPEC_SELF_REVIEW 27/27 PASS`
- **Implementation Plan:** `docs/superpowers/plans/2026-09-03-federated-change-intelligence-suite.md`
- **Plan Commit:** `95c1ca3`
- **Plan Self-Review:** `FEDERATED_PLAN_SELF_REVIEW 23/23 PASS`
- **TDD RED:** scenarios `381–420`; cumulative numbering `1–420`; `FEDERATED_STRUCTURAL 23/40 PASS` / expected `17` missing-contract failures on Framework `1.13.0`; baseline invariants GREEN.
- **Target Release:** Framework `1.14.0` / Schema `1.0.0` / release format `3` — cumulative OUT-008 target reclassified by approved suite design
- **Completion criteria:** A user-approved design defines event eligibility, severity, recipient/ack/escalation semantics, deduplication, failure handling, evidence, authority separation, integration boundaries, and verification strategy.
- **Suite:** `OUT-008 Federated Change Intelligence` / downstream notification-governance stage; TASK-028 already DONE prerequisite context
- **Dependency State:** `TASK-029 + TASK-030 SATISFIED` via `daf01eb / EVD-068` and `360a1ad / EVD-067`.
- **Implementation State:** `DONE / FOCUSED_VERIFIED` — notification governance current surfaces/starters implemented; no delivery runtime/new command/new Stable-ID family.
- **Implementation Commit:** `e58c7a0`
- **Focused Verification:** `TASK031_FOCUSED_TEXT 33/33 PASS` — direct context-aware Git/text assertions; no executable verifier artifact.
- **Suite Cumulative AFFECTED:** `FEDERATED_AFFECTED 33/33 PASS` / `EVD-071`; 22/22 maintained starter stamps at Framework 1.14.0.
- **Suite Final Candidate:** `6a9ef8c3439e270c3c02e0721aa416a9b20c305d` / tree `f107e3841e73cc1ff1b147cb753ef9cec28a2f37` / Framework-Source tree `d5d04e4563157246872b1e02c791b94a6c564d95`.
- **Suite Final RELEASE_FULL:** `FEDERATED_RELEASE_FULL 33/33 PASS_RUN_1` — exactly one executed run on the unchanged final candidate.
- **Suite Release Evidence:** `docs/superpowers/evidence/2026-09-03-federated-change-intelligence-suite-release-full.md` / commit `e0646c9` / `EVD-072`.
- **Version 1 Closure:** Framework 1.14.0 verified Last Stable 1.x Baseline; OUT-008 ACHIEVED / AUTH-008 TERMINATED / ACT-020 DONE / ENV-008 EXPIRED; publication `MERGED_TO_MAIN / PR #28 / merge eda1f2b / PERSISTED / NOT_PENDING`.
- **Canonical Publication Reconciliation:** checkpoint `0d7fcd4` freshly verified on `origin/main`; terminal OUT-010/AUTH-010/ACT-022/ENV-010 reconciliation prepared; final terminal commit requires fresh remote observation.
- **Completion Checkpoint Evidence:** `EVD-070 / CHG-070`
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป

## Task #32 — Governed Project Repair / Remediation

- **ID:** `TASK-032`
- **Status:** `DONE`
- **Type:** Framework workflow / integrity remediation governance
- **depends_on:** `[TASK-028]`
- **blocks:** `[]`
- **enables:** `[]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `READY`
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
- **Design State:** `USER_APPROVED_DIRECTION / WRITTEN_SPEC_APPROVED_BY_GOAL`
- **Design Spec:** `docs/superpowers/specs/2026-09-02-task028-task032-integrity-remediation-design.md`
- **Spec Self-Review:** `PASS 12/12` — release classification, dependency order, strict audit interface, no-auto-fix boundary, canonical repair routing, Risk/AUTH/rollback/re-audit, scenario range `357–380`, no-runtime/no-new-ID boundaries checked.
- **Implementation Plan:** `docs/superpowers/plans/2026-09-02-task028-task032-integrity-remediation.md`
- **Plan State:** `WRITTEN / SELF_REVIEWED / EXECUTION_AUTHORIZED_BY_GOAL`
- **Plan Self-Review:** `PASS 13/13` — TDD RED ordering, TASK-028→TASK-032 completion gate, exact affected surfaces, cumulative AFFECTED, frozen candidate, one-final-RELEASE_FULL, evidence and terminal reconciliation covered.
- **TDD RED:** scenarios `357–380`; cumulative numbering `1–380`; `TASK028032_STRUCTURAL 14/40 PASS` / expected `26` missing-contract failures on Framework `1.12.2`; no verifier/runtime error.
- **Target Release:** Framework `1.13.0` / Schema `1.0.0` / release format `3` — cumulative suite target shared with TASK-028; implementation waits for TASK-028 contract completion.
- **Completion criteria:** A user-approved design defines repair proposal/lifecycle, authority/risk gates, sequencing, rollback, semantic-conflict boundaries, post-repair verification, affected Framework surfaces, and verification strategy.
- **Dependency State:** `TASK-028 SATISFIED` via implementation `a38d514` + focused `23/23 PASS` + `EVD-057`.
- **Implementation State:** `DONE / LOCAL_VERIFIED / RELEASE_EVIDENCE_COMMITTED` — TASK-032 remediation semantics implemented and verified within cumulative Framework 1.13.0; no repair command/runtime/new remediation family introduced.
- **Implementation Commit:** `dd20987`
- **Focused Verification:** `TASK032_FOCUSED 23/23 PASS`
- **Prior Structural Verification:** `40/40 PASS`
- **Prior Cumulative Affected Verification:** `58/58 PASS` / `EVD-058`; candidate `5991c9f` later invalidated before RELEASE_FULL for Project Source EOF hygiene.
- **Corrected Cumulative Affected Verification:** `59/59 PASS` / `EVD-060`, including prospective full branch `git diff --check origin/main` PASS.
- **Invalidated Candidate:** `5991c9fe133942703c93a579be26ecafc7c7d59e` / tree `160a36ffe552e2a10cdc98413c2994acc580c856` / Framework-Source tree `61c27afad2bb794e54561e422b928fc777186585` / RELEASE_FULL NOT_RUN.
- **Final Candidate:** `089fc186275b303440b3be236c5e29b39f552cd5`
- **Final Candidate Tree:** `ec50f32ef2d8f063afe98b2c6e07568c3004dd66`
- **Final Framework-Source Tree:** `61c27afad2bb794e54561e422b928fc777186585`
- **Final RELEASE_FULL:** `TASK028032_RELEASE_FULL 49/49 PASS` — exactly one run on the unchanged corrected candidate.
- **Release Evidence:** `docs/superpowers/evidence/2026-09-02-task-028-task-032-integrity-remediation-release-full.md`
- **Release Evidence Commit:** `950bff9`
- **Publication State:** `MERGED_TO_MAIN / PR #28 / merge eda1f2b / PERSISTED / NOT_PENDING`
- **Completion State:** `DONE / LOCAL_VERIFIED`; canonical publication is merged and post-merge reconciliation remains pending.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป

## Task #33 — Task Dependency & Portfolio Planning

- **ID:** `TASK-033`
- **Status:** `DONE`
- **Type:** Framework development workflow / backlog dependency and prioritization contract
- **depends_on:** `[]`
- **blocks:** `[TASK-027]`
- **enables:** `[TASK-027]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `READY`
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
- **Design State:** `USER_APPROVED_SET1_DIRECTION / WRITTEN_SPEC_APPROVED`
- **Design Spec:** `docs/superpowers/specs/2026-09-01-task033-task-dependency-portfolio-design.md`
- **Design Commit:** `9b0078e`
- **Spec Suite Self-Review:** `PASS 130/130`
- **Suite Implementation Plan:** `docs/superpowers/plans/2026-09-01-set1-foundation-suite.md`
- **Plan Commit:** `8555e09`
- **Plan Self-Review:** `PASS 38/38`
- **TDD RED:** `SET1_RED 77/159 FAIL` expected; scenarios `1–338`; RED commit `404a75f`
- **Set 1 Suite:** `COMPLETED / OUT-004 ACHIEVED / LOCAL_VERIFIED / PUBLICATION_NOT_PUSHED`
- **Target Release:** Framework `1.12.0` / Schema `1.0.0` / release format `3` — cumulative Set 1 target approved by suite design
- **Completion criteria:** A user-approved design defines Task relationship vocabulary, priority/readiness, dependency validation, parallelism, stale/cycle handling, `DEP-*` separation, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
- **Set 1 Completion:** focused `54/54 PASS`; implementation commit `7da7e69`; completed under OUT-004/AUTH-004.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
- **Set 1 Final Acceptance:** structural `159/159 PASS`; cumulative AFFECTED `75/75 PASS`; RELEASE_FULL `108/108 PASS`; candidate `125e10f1d00263ddda0031e02383b179ecd12699`; Framework-Source tree `ce68037371568f98786b62f9afefc47907a91cc6`; evidence `f37a7474235d847f14dca77d54f9c3b217eed11f`.
- **Publication State:** `MERGED_TO_MAIN / PERSISTED`
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
- **Completed-work Integration Evidence:** `docs/superpowers/evidence/2026-09-02-completed-work-main-integration-release-full.md` / `0c8d972`
- **Canonical Main Integration:** `b8697f17c6d5de9835edfb9248229e5e3bf6525f` / Framework-Source tree `993b481c0d36057108df0eb87e41194bead64577` / EVD-042 verified
## Task #34 — Agent / Model Capability Profile

- **ID:** `TASK-034`
- **Status:** `DONE`
- **Type:** Framework architecture / agent and model capability governance
- **depends_on:** `[TASK-027]`
- **blocks:** `[TASK-035]`
- **enables:** `[TASK-035, TASK-037]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `READY`
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
- **Design State:** `USER_APPROVED_SET1_DIRECTION / WRITTEN_SPEC_APPROVED`
- **Design Spec:** `docs/superpowers/specs/2026-09-01-task034-agent-model-capability-profile-design.md`
- **Design Commit:** `9b0078e`
- **Spec Suite Self-Review:** `PASS 130/130`
- **Suite Implementation Plan:** `docs/superpowers/plans/2026-09-01-set1-foundation-suite.md`
- **Plan Commit:** `8555e09`
- **Plan Self-Review:** `PASS 38/38`
- **Set 1 Suite:** `COMPLETED / OUT-004 ACHIEVED / LOCAL_VERIFIED / PUBLICATION_NOT_PUSHED`
- **Target Release:** Framework `1.12.0` / Schema `1.0.0` / release format `3` — cumulative Set 1 target approved by suite design
- **Completion criteria:** A user-approved design defines capability vocabulary, eligibility/review rules, local/external distinctions, fallback/degraded behavior, authority separation, integration boundaries, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
- **Set 1 Completion:** focused `75/75 PASS`; implementation commit `c5a3003`; completed under OUT-004/AUTH-004.
- **Set 1 Final Acceptance:** structural `159/159 PASS`; cumulative AFFECTED `75/75 PASS`; RELEASE_FULL `108/108 PASS`; candidate `125e10f1d00263ddda0031e02383b179ecd12699`; Framework-Source tree `ce68037371568f98786b62f9afefc47907a91cc6`; evidence `f37a7474235d847f14dca77d54f9c3b217eed11f`.
- **Publication State:** `MERGED_TO_MAIN / PERSISTED`
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
- **Completed-work Integration Evidence:** `docs/superpowers/evidence/2026-09-02-completed-work-main-integration-release-full.md` / `0c8d972`
- **Canonical Main Integration:** `b8697f17c6d5de9835edfb9248229e5e3bf6525f` / Framework-Source tree `993b481c0d36057108df0eb87e41194bead64577` / EVD-042 verified
## Task #35 — Project Release / Publication Contract

- **ID:** `TASK-035`
- **Status:** `DONE`
- **Type:** Framework release / publication lifecycle governance
- **depends_on:** `[TASK-034]`
- **blocks:** `[TASK-037]`
- **enables:** `[TASK-037]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `READY`
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
- **Design State:** `USER_APPROVED_SET1_DIRECTION / WRITTEN_SPEC_APPROVED`
- **Design Spec:** `docs/superpowers/specs/2026-09-01-task035-release-publication-contract-design.md`
- **Design Commit:** `9b0078e`
- **Spec Suite Self-Review:** `PASS 130/130`
- **Suite Implementation Plan:** `docs/superpowers/plans/2026-09-01-set1-foundation-suite.md`
- **Plan Commit:** `8555e09`
- **Plan Self-Review:** `PASS 38/38`
- **Set 1 Suite:** `COMPLETED / OUT-004 ACHIEVED / LOCAL_VERIFIED / PUBLICATION_NOT_PUSHED`
- **Target Release:** Framework `1.12.0` / Schema `1.0.0` / release format `3` — cumulative Set 1 target approved by suite design
- **Completion criteria:** A user-approved design defines release/publication states, candidate identity, evidence/approval, assurance, partial/failure/rollback behavior, verification integration, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
- **Set 1 Completion:** focused `66/66 PASS`; implementation commit `9a6ac1c`; completed under OUT-004/AUTH-004.
- **Set 1 Final Acceptance:** structural `159/159 PASS`; cumulative AFFECTED `75/75 PASS`; RELEASE_FULL `108/108 PASS`; candidate `125e10f1d00263ddda0031e02383b179ecd12699`; Framework-Source tree `ce68037371568f98786b62f9afefc47907a91cc6`; evidence `f37a7474235d847f14dca77d54f9c3b217eed11f`.
- **Publication State:** `MERGED_TO_MAIN / PERSISTED`
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
- **Completed-work Integration Evidence:** `docs/superpowers/evidence/2026-09-02-completed-work-main-integration-release-full.md` / `0c8d972`
- **Canonical Main Integration:** `b8697f17c6d5de9835edfb9248229e5e3bf6525f` / Framework-Source tree `993b481c0d36057108df0eb87e41194bead64577` / EVD-042 verified
## Task #36 — Project Change/Event History Feed

- **ID:** `TASK-036`
- **Status:** `DONE`
- **Type:** Framework architecture / bounded derived Project change projection
- **depends_on:** `[]`
- **blocks:** `[TASK-029]`
- **enables:** `[TASK-029]`
- **parallelizable_with:** `[TASK-030]`
- **priority:** `HIGH`
- **readiness:** `READY`
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
- **Design State:** `USER_APPROVED_DIRECTION / WRITTEN_SPEC_APPROVED_BY_GOAL`
- **Design Spec:** `docs/superpowers/specs/2026-09-03-federated-change-intelligence-suite-design.md`
- **Design Commit:** `d061f1f`
- **Spec Self-Review:** `FEDERATED_SPEC_SELF_REVIEW 27/27 PASS`
- **Implementation Plan:** `docs/superpowers/plans/2026-09-03-federated-change-intelligence-suite.md`
- **Plan Commit:** `95c1ca3`
- **Plan Self-Review:** `FEDERATED_PLAN_SELF_REVIEW 23/23 PASS`
- **TDD RED:** scenarios `381–420`; cumulative numbering `1–420`; `FEDERATED_STRUCTURAL 23/40 PASS` / expected `17` missing-contract failures on Framework `1.13.0`; baseline invariants GREEN.
- **Target Release:** Framework `1.14.0` / Schema `1.0.0` / release format `3` — cumulative OUT-008 target reclassified by approved suite design
- **Completion criteria:** A user-approved design defines feed identity/schema, delta/checkpoint semantics, rebuildability, stale/corrupt handling, bounded retention, authority separation, integration boundaries, affected Framework surfaces, and verification strategy.
- **Suite:** `OUT-008 Federated Change Intelligence` / foundation stream A / cumulative target Framework 1.14.0
- **Implementation State:** `DONE / FOCUSED_VERIFIED` — optional derived Project Change Feed contract implemented with no executable verifier/runtime/new command/new Stable-ID family.
- **Implementation Commit:** `5c9ed7c`
- **Focused Verification:** `TASK036_FOCUSED_TEXT 30/30 PASS` — direct read-only Git/text assertions; no executable verifier artifact.
- **Publication State:** `MERGED_TO_MAIN / PR #28 / merge eda1f2b / PERSISTED / NOT_PENDING`
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป

## Task #37 — Security & Trust Boundary Contract

- **ID:** `TASK-037`
- **Status:** `DONE`
- **Type:** Framework architecture / Project security and trust-boundary governance
- **depends_on:** `[TASK-035]`
- **blocks:** `[]`
- **enables:** `[]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `READY`
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
- **Design State:** `USER_APPROVED_SET1_DIRECTION / WRITTEN_SPEC_APPROVED`
- **Design Spec:** `docs/superpowers/specs/2026-09-01-task037-security-trust-boundary-design.md`
- **Design Commit:** `9b0078e`
- **Spec Suite Self-Review:** `PASS 130/130`
- **Suite Implementation Plan:** `docs/superpowers/plans/2026-09-01-set1-foundation-suite.md`
- **Plan Commit:** `8555e09`
- **Plan Self-Review:** `PASS 38/38`
- **Set 1 Suite:** `COMPLETED / OUT-004 ACHIEVED / LOCAL_VERIFIED / PUBLICATION_NOT_PUSHED`
- **Target Release:** Framework `1.12.0` / Schema `1.0.0` / release format `3` — cumulative Set 1 target approved by suite design
- **Completion criteria:** A user-approved design defines trust vocabulary, crossing rules, provenance/evidence, approval/fail-closed behavior, secret/disclosure separation, integration boundaries, affected Framework surfaces, and verification strategy.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
- **Set 1 Implementation State:** `COMPLETE_PENDING_CUMULATIVE_ACCEPTANCE`
- **Focused Verification:** `123/123 PASS`
- **Implementation Commit:** `9c7045c`
- **Structural GREEN:** `SET1_RED 159/159 PASS`; scenarios `1–338`.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
- **Cumulative AFFECTED:** `SET1_AFFECTED 75/75 PASS`
- **Candidate State:** `READY_FOR_FINAL_CANDIDATE_COMMIT_AND_FREEZE`
- **Publication State:** `MERGED_TO_MAIN / PERSISTED`
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
- **Set 1 Final Acceptance:** structural `159/159 PASS`; cumulative AFFECTED `75/75 PASS`; RELEASE_FULL `108/108 PASS`; candidate `125e10f1d00263ddda0031e02383b179ecd12699`; Framework-Source tree `ce68037371568f98786b62f9afefc47907a91cc6`; evidence `f37a7474235d847f14dca77d54f9c3b217eed11f`.
- **Publication State:** `MERGED_TO_MAIN / PERSISTED`
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
- **Completed-work Integration Evidence:** `docs/superpowers/evidence/2026-09-02-completed-work-main-integration-release-full.md` / `0c8d972`
- **Canonical Main Integration:** `b8697f17c6d5de9835edfb9248229e5e3bf6525f` / Framework-Source tree `993b481c0d36057108df0eb87e41194bead64577` / EVD-042 verified
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

## Task #40 — Rename `[Session Envelope]` Command to `[Session]`

- **ID:** `TASK-040`
- **Status:** `DONE`
- **Type:** Framework command surface / bounded terminology simplification
- **Problem:** The registered bounded session/task command name `[Session Envelope]` is unnecessarily long for routine use even though its underlying `ENV-*` semantics are already stable.
- **User Instruction:** On `2026-08-31`, user explicitly instructed: rename the command to `[Session]` and make this change first.
- **Approved direction:** Canonical current command becomes exactly `[Session]`; retain `declare | show | close`, `ENV-*` ownership in `15 Action Registry`, expiry/prohibited-zone semantics, Goal-derived narrowing rules, and all fail-closed gates. The historical longer spelling is not a current registered alias.
- **Scope:** current Core Governance, SKILL, ChatGPT/Claude launchers, README/help, maintained starter surfaces, migration guidance, pressure scenarios, release latest-amendment routing, and bounded Project/Task lifecycle evidence. Historical amendments/specs/plans/evidence remain unchanged when their old spelling was true at capture time.
- **Design State:** `USER_APPROVED_BOUNDED_CHANGE / INLINE_DESIGN_APPROVED`
- **Target Release:** Framework `1.8.0` / Schema `1.0.0`; command-name-only amendment, no version/schema bump.
- **Implementation Boundary:** documentation/governance only; no parser/runtime/CLI/alias layer/automation.
- **Verification Contract:** RED first; scenarios `246–248`; current command surfaces contain `[Session]`; historical TASK-021 amendment/evidence preserve the old spelling; launchers remain byte-identical in shared body and `<=4,500`; `ENV-*` semantics/fail-closed boundaries unchanged; `git diff --check`; AFFECTED verification; one final `RELEASE_FULL` on unchanged candidate.
- **Implementation Commit(s):** `5b3d4e309976a88e1e57495b6fdaa049fabb6247`
- **Release Evidence Commit:** `52498bd`
- **Candidate Commit:** `5b3d4e309976a88e1e57495b6fdaa049fabb6247`
- **Candidate Tree:** `9fcdb6b3f0dc8c43f35865ee9155c0521c4e64fc`
- **Framework-Source Tree:** `36804c105604fe8da492a9d71a1f0270e5e035ee`
- **Release Evidence:** `docs/superpowers/evidence/2026-08-31-task-040-session-command-rename-release-full.md`
- **Verification Result:** RED `10/26 FAIL` observed before implementation; GREEN `26/26 PASS`; AFFECTED `54/54 PASS`; RELEASE_FULL `160/160 PASS`
- **Completion criteria met:** canonical current command is `[Session]`; no current legacy alias; declare/show/close and `ENV-*` semantics unchanged; historical provenance preserved; scenarios 1–248; launcher parity/ceiling; AFFECTED and RELEASE_FULL PASS; evidence committed.
- **Publication State:** `MERGED_TO_MAIN` — Pull Request `#24` merged exact branch head `8622ef5ebfb38596ceedddd7dd668f8d9ba48bae` to `main` at merge commit `5a51b105ff4430c04605dcb254d41a8e80faad8b` on `2026-08-31T16:23:57+07:00`; merged Framework-Source tree remained `36804c105604fe8da492a9d71a1f0270e5e035ee`.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป

## Task #41 — Portable Installation Bootstrap & Project Settings Handoff

- **ID:** `TASK-041`
- **Status:** `DONE`
- **Type:** Framework bootstrap architecture / vendor-neutral installation UX and discovery contract
- **Problem:** GREENFIELD installation can create local Project Source and `PROJECT-BOOTSTRAP.md`, but post-install Project Settings handoff is not canonical, current vendor launchers duplicate a large governance payload, consuming Projects lack a mandatory managed README bootstrap fallback, and upstream README does not display the full mandatory response-close pattern.
- **User-approved direction:** installation completes with a fixed `ProjectFramework Upstream` (`https://github.com/captainhuke-dev/ProjectFramework`) plus a verified absolute `Project Bootstrap` path for Project Settings; consuming README carries a managed relative `./PROJECT-BOOTSTRAP.md` fallback; target vendor launchers are thin adapters; core installation completion is independent from later user copy/paste confirmation.
- **Approved choices:** fallback in both upstream + consuming README (`C`); existing README managed-marker update (`1`); absolute Project Settings path + relative README path (`C`); Thin Bootstrap Block (`A`); core install DONE separate from vendor handoff confirmation (`A`); Design Sections 1–3 explicitly approved on `2026-08-31`.
- **Authority boundary:** Project Settings / README / `PROJECT-BOOTSTRAP.md` are discovery only; active local `00 / FRAMEWORK-001` remains Project governance authority. Framework upstream is upgrade/discovery source only and never the consuming Project repository or authority.
- **Design Spec:** `docs/superpowers/specs/2026-08-31-task041-portable-installation-bootstrap-design.md`
- **Design State:** `USER_APPROVED_DESIGN / SPEC_APPROVED`
- **Design Commit:** `da1d2201eead976c4e4ad10e97afb244664dc571`
- **Spec Self-Review:** `PASS 30/30` — placeholders, internal consistency, scope, authority/path lifecycle, approved choices, Task registry alignment, and diff hygiene checked.
- **Target Release:** Framework `1.9.0` / Schema `1.0.0` (minor Framework interface evolution; no semantic-slot or Stable-ID-family change)
- **Implementation Boundary:** approved design is implementation-authorized under persistent `AUTH-001`; implementation remains documentation/governance only and excludes runtime/CLI/bot/hook/CI/watcher/scheduler/daemon scope.
- **Verification/Acceptance direction:** managed README marker integrity/content preservation; resolved absolute Project Settings path; README relative fallback; upstream-vs-Project authority separation; retained internal Git/Drive/File Storage/MCP/Workspace semantics; thin launcher parity; exact upstream README response-close pattern; GREENFIELD/Brownfield fail-closed behavior; no runtime/CLI/automation; affected verification and one final unchanged-candidate `RELEASE_FULL` during implementation.
- **Current Sequencing:** TASK-041 is the user-selected current architectural improvement; TASK-025 remains TODO and is not implemented by this design checkpoint.
- **Goal State:** `OUT-001 ACHIEVED / AUTH-001 TERMINATED / ENV-001 EXPIRED`; persistent Goal completed locally; no future execution authority remains; push/publication was never included.
- **Implementation Plan:** `docs/superpowers/plans/2026-08-31-task041-portable-installation-bootstrap.md`
- **Plan Commit:** `d45949498a6f2b1b5f9af8b3fee5cc4a516a222b`
- **Plan Self-Review:** `PASS 52/52`
- **Plan State:** `IMPLEMENTATION_PLAN_EXECUTED`
- **Execution Progress:** Task 1 RED contract complete — scenarios `249–268`, `TASK041_RED 40/97 FAIL` expected, commit `a14eeb2c476f6de812bd8b3bcd69a551814b3448`; Task 2 normative implementation next. Task 2 normative contract PASS `51/51`, commit `61bfb3724347a4cba988d987604ade92f66cc45d`, RED reduced to `50/97 FAIL`; Task 3 next. Task 3 thin adapters PASS `42/42`, commit `062c20a8bedc002650dd059e65b1fa792db6dd8c`, RED reduced to `73/97 FAIL`; Task 4 next. Task 4 README/starter PASS `53/53`, 24 stamps at 1.9.0, commit `5d2349ab2e89091e7bbf31c5ae2d9a76e7fc1e6e`, RED `93/97 FAIL` migration-only; Task 5 next. Task 5 migration added; structural RED contract GREEN `97/97`; comprehensive AFFECTED `273/273 PASS`; final implementation candidate commit is next. Task 5 candidate `f5cee5fb2f3cb4da7967f56dcb294ce2a1703530`; AFFECTED `273/273 PASS`; RELEASE_FULL `248/248 PASS`; evidence commit `06fe0c0a06d1c6c6a1abcf3c5cb9052471c5d8ef`; Task 6 terminal reconciliation prepared.
- **Implementation Commit(s):** `a14eeb2c476f6de812bd8b3bcd69a551814b3448`, `61bfb3724347a4cba988d987604ade92f66cc45d`, `062c20a8bedc002650dd059e65b1fa792db6dd8c`, `5d2349ab2e89091e7bbf31c5ae2d9a76e7fc1e6e`, candidate `f5cee5fb2f3cb4da7967f56dcb294ce2a1703530`
- **Affected Verification:** `TASK041_AFFECTED 273/273 PASS`; scenarios `1–268`; 24 maintained template stamps at Framework 1.9.0 / Schema 1.0.0; thin launcher lengths 513/512
- **Candidate Commit:** `f5cee5fb2f3cb4da7967f56dcb294ce2a1703530`
- **Candidate Tree:** `71756d53cbbcff54883915f24ef353e40b37bda6`
- **Framework-Source Tree:** `06ce4013473ec014e70d8d3233f6132aa90339fd`
- **Release Evidence:** `docs/superpowers/evidence/2026-08-31-task-041-portable-installation-bootstrap-release-full.md`
- **Release Evidence Commit:** `06fe0c0a06d1c6c6a1abcf3c5cb9052471c5d8ef`
- **Verification Result:** AFFECTED `273/273 PASS`; RELEASE_FULL `248/248 PASS`; scenarios `1–268`; launcher lengths `513/512`; 24 maintained template stamps at Framework 1.9.0 / Schema 1.0.0
- **Completion Criteria Met:** approved spec/plan; portable two-binding adapter; managed README fallback; verified-absolute-path fail-closed behavior; retained internal location semantics; thin launchers; exact upstream response-close; GREENFIELD/Brownfield safety; no runtime/CLI/state-family expansion; affected and final RELEASE_FULL PASS; release evidence committed; terminal Goal reconciliation committed/observed before external completion claim.
- **Publication State:** `MERGED_TO_MAIN` — Pull Request `#26` merged exact head `7d93dab849435c3cc4132af4c8be5fa72d0bbb7b` to `main` at merge commit `2bfe5efbb24480bc44dbd8e949ed632af4d759ee`; merged Framework-Source tree remains `06ce4013473ec014e70d8d3233f6132aa90339fd`.
- **Publication Reconciliation:** `PERSISTED / NOT_PENDING`; `OUT-002 ACHIEVED / AUTH-002 TERMINATED / ACT-011 DONE / ENV-002 EXPIRED`; active checkpoint `c5741ab56799d44cefa39f30da55bd23bf85bf03`; terminal reconciliation `d650513fe01726238f6e59cde1ed7a70b28ae0e4` observed on `origin/main`; remote validation `41/41 PASS`; Framework-Source tree unchanged `06ce4013473ec014e70d8d3233f6132aa90339fd`.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป

## Task #42 — Response Finalization Hardening

- **ID:** `TASK-042`
- **Status:** `DONE`
- **Type:** Framework bootstrap/final-response reliability hardening
- **Problem:** Project-governed read-only/status/diagnostic and exceptional early-return paths could respond before local governance was resolved or bypass the mandatory Response Close Completeness Gate.
- **Approved direction:** First Project-governed response resolves Project Bootstrap when accessible; non-Material diagnostics are not exempt; every final path converges on the pre-emit Response Close Completeness Gate.
- **Design Spec:** `docs/superpowers/specs/2026-09-01-task042-response-finalization-hardening-design.md`
- **Implementation Plan:** `docs/superpowers/plans/2026-09-01-task042-response-finalization-hardening.md`
- **Original Release Evidence:** `docs/superpowers/evidence/2026-09-01-task-042-response-finalization-hardening-release-full.md` — original Framework `1.9.1` branch candidate, AFFECTED `110/110 PASS`, RELEASE_FULL `171/171 PASS`.
- **Original Branch Head:** `c12a1383849bf638df9745111d54958581b22838`
- **Forward-Port Classification:** `STALE_SEMANTIC / FORWARD_PORT_REQUIRED` against cumulative Framework `1.12.0`; direct merge rejected because it would downgrade current release/starter state and collide with existing scenario numbers.
- **Integrated Target Release:** Framework `1.12.1` / Schema `1.0.0` / release format `3`.
- **Integrated Scenario Contract:** original semantics renumbered to scenarios `339–350`; cumulative scenario range `1–350`.
- **Implementation Boundary:** documentation/governance only; no runtime interceptor, UI hook, middleware, validator/CLI, transport enforcement, MCP daemon change, or vendor execution code.
- **Integration State:** `FORWARD_PORTED_AND_INTEGRATED / VERIFIED`
- **Publication State:** `MERGED_TO_MAIN / PERSISTED`
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป
- **Completed-work Integration Evidence:** `docs/superpowers/evidence/2026-09-02-completed-work-main-integration-release-full.md` / `0c8d972`
- **Canonical Main Integration:** `b8697f17c6d5de9835edfb9248229e5e3bf6525f` / Framework-Source tree `993b481c0d36057108df0eb87e41194bead64577` / EVD-042 verified

## Task #43 — Registered Command Strict-Interface & Contract Completeness Hardening

- **ID:** `TASK-043`
- **Status:** `DONE`
- **Type:** Framework command / protocol-compliance reliability hardening
- **depends_on:** `[TASK-042]`
- **blocks:** `[]`
- **enables:** `[]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `READY`
- **Problem:** Registered Commands could return semantically correct information while replacing/omitting governed command structure; Framework 1.12.1 also had Core/SKILL `[Project Status]` `Continuity` drift.
- **Implemented direction:** Registered Commands are Strict Governed Interfaces. Required structure/order/tokens/freshness/fail-closed representation are contract elements; flexible prose remains allowed only where the active command contract leaves presentation open. The Command Contract Completeness Gate runs before TASK-042's Response Close Completeness Gate.
- **Target / Implementation Release:** Framework `1.12.2` / Schema `1.0.0` / release format `3`.
- **Design Spec:** `docs/superpowers/specs/2026-09-02-task043-registered-command-strict-interface-design.md`
- **Design State:** `USER_APPROVED_DIRECTION / WRITTEN_SPEC_APPROVED_BY_GOAL`
- **Implementation Plan:** `docs/superpowers/plans/2026-09-02-task043-registered-command-strict-interface.md`
- **Plan State:** `IMPLEMENTATION_PLAN_EXECUTED`
- **Implementation Commit(s):** registration `5401fe4`; design `f740d16`; Goal checkpoint `53e80f7`; plan `29e63fe`; RED `8584951`; normative `ed9da17`; propagation `c7a7ef4`; candidate `a4a2712ba41c35275401b31ac49b75d45eec8643`.
- **TDD Result:** scenarios `351–356`; RED `TASK043_STRUCTURAL 7/18 PASS` with 11 expected missing-contract failures → GREEN `18/18 PASS`; cumulative scenarios `1–356` contiguous/unique.
- **Affected Verification:** `TASK043_AFFECTED 37/37 PASS`.
- **Release Candidate:** `a4a2712ba41c35275401b31ac49b75d45eec8643` / tree `259db179349e1cdae3b8b6df0a4bec0a947b7fec` / Framework-Source tree `7417f06000e03a4e897e9d812fb0274544777a00`.
- **Release Evidence:** `docs/superpowers/evidence/2026-09-02-task-043-registered-command-strict-interface-release-full.md`.
- **Release Evidence Commit:** `2b7a23e8c5b06a1b9f37f8f2097b06223f5fbd18`.
- **Verification Result:** structural `18/18 PASS`; AFFECTED `37/37 PASS`; final unchanged-candidate RELEASE_FULL `25/25 PASS`; maintained Project Source starter stamps `22/22` at Framework 1.12.2; TASK-042 preserved; Registered Command set unchanged; local Project Source pin remains 1.7.0; no runtime expansion.
- **Completion Criteria Met:** Strict-Interface normative contract; Command Contract Completeness Gate; explicit command-gate → response-close-gate ordering; Core/SKILL/quick-reference/root-template `[Project Status]` `Continuity` alignment; correct-info/wrong-protocol and style/freshness/alignment pressure scenarios; release/migration/starter propagation; backward-compatible patch classification; no new command/slot/state/authority/runtime; release evidence committed and terminal Goal reconciliation prepared.
- **Goal State:** `OUT-005 ACHIEVED / AUTH-005 TERMINATED / ACT-016 DONE / ENV-005 EXPIRED`.
- **Publication State:** `MERGED_TO_MAIN / PERSISTED / NOT_PENDING` — PR #27 merge is canonical; terminal reconciliation `2da8fcbd2b11121db72599d1a6b3d33157619e17` freshly verified on `origin/main`; `OUT-006 ACHIEVED / AUTH-006 TERMINATED / ACT-018 DONE / ENV-006 EXPIRED`.
- **Publication Branch:** `task043-registered-command-strict-interface`
- **Published Head at PR Creation:** `5561ffa987ae62f24458e90f27e84d7ccc1a6a89`
- **Pull Request #27:** `MERGED` — `https://github.com/captainhuke-dev/ProjectFramework/pull/27`; merge `bdae13896ebec08235d5ef7101f189fa6861d801`; parents `40257f7dc97219715070b3764423c17118ecc51b` + `b45a9eaefc44da3f0526a4e865cf2c1c468d9da4`; Framework-Source tree unchanged `7417f06000e03a4e897e9d812fb0274544777a00`.
- **Publication Evidence:** `EVD-049` / `ACT-017`; post-merge reconciliation verified by `EVD-050 / EVD-051 / EVD-052 / OUT-006 / AUTH-006 / ACT-018 / ENV-006`.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป

## Task #44 — ProjectFramework 2.0 / AI-ControlTower Protocol Integration

- **ID:** `TASK-044`
- **Status:** `CANCELLED`
- **Type:** Major-version architecture / governance protocol + state/workflow control-plane integration
- **depends_on:** `[]`
- **blocks:** `[]`
- **enables:** `[]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `CANCELLED_BY_USER / IMPLEMENTATION_NOT_STARTED`
- **Problem:** ProjectFramework 1.x relies materially on AI interpretation of Markdown governance, workflow state, authority boundaries, and continuation context. ProjectFramework 2.0 moves deterministic state/workflow/guard/concurrency/recovery/API semantics into a public Protocol/Core inside AI-ControlTower while preserving governance authority boundaries and reducing agent drift.
- **Approved direction:** Keep `ProjectFramework 2.0` as a named public Protocol/Core module inside the AI-ControlTower Project. AI-ControlTower is the runtime/control-plane platform; ProjectFramework defines governance/state/workflow/API/capability/migration protocol contracts. After governed cutover, `AI-ControlTower/projectframework/` becomes canonical 2.x development source and the existing ProjectFramework repository becomes a one-way verified public distribution mirror.
- **Design Spec:** `docs/superpowers/specs/2026-09-04-projectframework-2-controltower-architecture-design.md`
- **Design State:** `WRITTEN_SPEC_APPROVED_BY_GOAL / FORWARD_PORTED_TO_CANONICAL_V1_BASELINE`
- **Forward-Port Checkpoint:** `aae3cb0a244a46434013c064847563893a752085` / `EVD-075` / `CHG-075`.
- **Implementation/Migration Plan:** `docs/superpowers/plans/2026-09-05-projectframework-2-ai-controltower-migration.md` / SHA256 `24289085cc41e03153a37c3f6298b4251c0ac3864ba2c88aefbd196a7ea366d7`.
- **Merge Manifest:** `docs/superpowers/plans/2026-09-05-projectframework-2-ai-controltower-merge-manifest.md` / SHA256 `cb3a11640ddc7eb7aa7f63a9796a4dde22ee85d6cd94c03d6f5caab89babb0f3`.
- **Plan/Manifest Self-Review:** `PF2_PLAN_MANIFEST_SELF_REVIEW 36/36 PASS`.
- **Target Verification:** `EVD-076` — `captainhuke-dev/ai-controltower` / `origin/main 5abcb8cbd2dde8d241ae74cf1f107721cd8b969a` / target UUID `2ab1b99a-901c-4159-87f1-953db0af5015` / GitHub+Local Workspace BOUND+VERIFIED; target root checkout excluded as merge workspace due divergence.
- **Spec Self-Review:** `PF2_SPEC_SELF_REVIEW 28/28 PASS`
- **Original Design Commit:** `6c9fd543c34e939db914c80e4c3354b3b36a0906`
- **Original Design Base:** `9f5a6fb1f8d26b80049a4a9521e50c38a99126be`
- **Forward-Port Baseline:** canonical Last Stable 1.x `aae65796a8d4ad5f23323889b65b060bd36302c1` / Framework-Source tree `d5d04e4563157246872b1e02c791b94a6c564d95`.
- **V1 Gate:** `SATISFIED` — Framework 1.14 is committed, pushed, merged through PR #28, post-merge reconciled, and canonical on `main`; V1 Task source is 26/26 DONE.
- **Stable-ID Forward-Port Rule:** original isolated design records used branch-local `EVD-071 / CHG-071`; these collide with later canonical V1 release records and are not imported as those IDs. The current canonical forward-port allocates `EVD-075 / CHG-075` while preserving original design commit/spec provenance. `OUT-009 / AUTH-009 / ACT-021 / ENV-009` remain reserved design identities and are promoted without collision.
- **Current Goal:** `OUT-011 ACHIEVED / AUTH-011 TERMINATED / ACT-023 DONE / ENV-011 EXPIRED` — Pre-Merge preparation completed; no execution authority remains.
- **Completed Goal Scope:** forward-port/reconcile design truth; written-spec approval recording; implementation/migration planning; merge manifest; AI-ControlTower read-only target/binding/current-architecture verification; rollback/version/licensing/conformance boundaries; local verification/commits and Pre-Merge Readiness evidence.
- **Explicitly Excluded From Current Goal:** actual ProjectFramework→AI-ControlTower repository merge; AI-ControlTower Project Source/code/runtime mutation; canonical-source cutover; V2 runtime/API/state DB/MULTICA/adapter implementation; public mirror publication; force push/destructive history rewrite; license-instrument selection.
- **Target Release:** ProjectFramework `2.0.0`; Project Source Schema `2.0.0`; initial API Protocol `1.0.0`; initial Workflow Schema `1.0.0`; AI-ControlTower application version independently governed.
- **Completion Criteria For Pre-Merge Goal:** SATISFIED — `PF2_PRE_MERGE_READINESS 35/35 PASS` / `EVD-077`; no target mutation/merge/cutover/runtime implementation occurred.
- **Pre-Merge Readiness Evidence:** `EVD-077 / CHG-077` / `PF2_PRE_MERGE_READINESS 35/35 PASS`.
- **Tool/MCP Execution Policy:** `Project-Execution/tools.md` / CEO PRIMARY / HZM DISALLOWED / fallback NONE / FAIL_CLOSED / `EVD-078`.
- **Cancellation Basis:** Explicit user direction on 2026-09-10: keep Framework 1.15, cancel ProjectFramework 2.0.0; no merge/cutover/runtime implementation occurred.
- **Historical Preservation:** Original V2 head `0ef4e4cb2f4ffcedfc3145e718b7462d76fb3092`; design/migration/merge-manifest preserved; prior PRE_MERGE_READY evidence remains historical, not current execution authority.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป for TASK-044; 2.0 line is cancelled.

## Task #45 — Response Close + Next Goal

- **ID:** `TASK-045`
- **Status:** `DONE`
- **Type:** Framework response protocol / usability and persistent-Goal handoff refinement
- **Collision Note:** `TASK-044` is already allocated to ProjectFramework 2.0 / AI-ControlTower Protocol Integration in the verified V2 `v2-premerge-readiness` line; TASK-045 does not rewrite or absorb it.
- **Problem:** mandatory Framework responses expose `[Chat]` and `[Required Read]` fields that are implementation-facing rather than useful to the Human for routine control, while there is no concise copy-ready suggestion for users who want to turn the next bounded outcome into one persistent `[Goal]` command.
- **User-approved direction:** remove `[Chat]` and `[Required Read]` from the mandatory visible response close; add `[Next Goal]` immediately after `[Next Action]`; preserve two mandatory headings and `[Reason]`; keep continuation/read-routing in Project Source/Handoff rather than forcing them into every response.
- **Next Goal contract:** the field is mandatory but presentation-only. Value is a safe copy-ready `[Goal] ...` or `[Goal] CHANGE ...` command only when a bounded persistent outcome is clearly appropriate and does not synthesize high-risk opt-ins; otherwise `ไม่มี`. It never creates authority until the user actually invokes the command.
- **Target Release:** Framework `1.15.0` / Schema `1.0.0` / release format `3`.
- **Implementation Boundary:** documentation/governance/templates/tests only; no runtime parser/interceptor/UI hook/validator/CLI.
- **Goal:** `OUT-012 / AUTH-012 / ACT-024 / ENV-012`.
- **Design State:** `USER_APPROVED_DIRECTION / WRITTEN_SPEC_APPROVED_BY_GOAL`.
- **Design Spec:** `docs/superpowers/specs/2026-09-06-task045-response-close-next-goal-design.md`
- **Spec Self-Review:** `PASS` — placeholder, consistency, scope, ambiguity, Next Goal authority-safety, continuity separation and scenario coverage checked.
- **Implementation Plan:** `docs/superpowers/plans/2026-09-06-task045-response-close-next-goal.md`
- **Plan State:** `IMPLEMENTATION_PLAN_EXECUTED / CANDIDATE_FREEZE_READY`
- **Plan Self-Review:** `PASS` — spec coverage, no placeholders, dynamic collision checks, TDD RED ordering, AFFECTED/frozen-candidate/one-RELEASE_FULL/terminal reconciliation covered.
- **TDD RED:** scenarios `421–432`; `TASK045_RED 4/13 PASS` with 9 expected missing-production-contract failures; scenario range `1–432` contiguous/unique; commit `ce6e816`.
- **Normative Implementation:** Framework release/amendment/Core/SKILL commit `039fb8f`; post-normative verifier `11/13 PASS` with only README/migration propagation pending.
- **Propagation Implementation:** README/migration/root/skeleton/mockup + 22 maintained starter stamps commit `f0f3416`; structural GREEN `13/13 PASS`.
- **Affected Verification:** `TASK045_AFFECTED 27/27 PASS`; seven commands unchanged; TASK-042/TASK-043 preserved; 22/22 starter stamps at 1.15.0; thin launcher parity/size PASS; no runtime scope; V2 TASK-044 head `0ef4e4c` and Task-source blob `bb4b75f` preserved; full branch diff hygiene PASS.
- **Implementation State:** `DONE / LOCAL_VERIFIED / TERMINAL_RECONCILED`
- **Final Candidate:** `bc7f91c49372ff33e9726da7461288479438b86a` / tree `9170ba8fccbc1bf3f6031441389392d372f8950a` / Framework-Source tree `c095bd6570adb9668755d4598087dee0e4729208`.
- **Final RELEASE_FULL:** `TASK045_RELEASE_FULL 33/33 PASS` / exactly one run on the unchanged final candidate.
- **Release Evidence:** `docs/superpowers/evidence/2026-09-06-task-045-response-close-next-goal-release-full.md`; evidence commit `4278182`.
- **Preservation:** TASK-042/TASK-043 + launcher protected blobs preserved; seven commands unchanged; V2 TASK-044 head `0ef4e4c` and Task-source blob `bb4b75f` preserved; no runtime expansion.
- **Publication State:** `PUBLISHED_TO_ORIGIN_MAIN / PERSISTED / NOT_PENDING`.
- **Published Commits:** `196ddd0d5a2ec7c48c7a9232bafc909b0284522b` (registration) + `bc880c75190f967a3b87c2842b8cc284f8a3bcab` (terminal close), freshly observed on `origin/main` before reconciliation.
- **Publication Reconciliation:** `OUT-016 ACHIEVED / AUTH-016 TERMINATED / ACT-028 DONE / ENV-016 EXPIRED`; evidence `EVD-092 / CHG-092`; this reconciliation is complete when the active successor set is freshly read from canonical `origin/main`.
- **Goal State:** `OUT-012 ACHIEVED / AUTH-012 TERMINATED / ACT-024 DONE / ENV-012 EXPIRED`.
- **Completion Criteria Met:** Framework 1.15 response-close contract, safe Next Goal semantics, internal continuity preservation, scenarios 1–432, structural/AFFECTED/one RELEASE_FULL PASS, evidence committed, V2 TASK-044 preserved, no runtime expansion, terminal Project Source reconciliation.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป; publication/adoption requires a new exact instruction.

## Task #46 — Final Response Close Simplification

- **ID:** `TASK-046`
- **Status:** `CANCELLED`
- **Type:** Framework response-contract / user-facing protocol simplification
- **depends_on:** `[TASK-042, TASK-043]`
- **blocks:** `[]`
- **enables:** `[]`
- **priority:** `HIGH`
- **readiness:** `CANCELLED_BY_USER / SUPERSEDED_BEFORE_IMPLEMENTATION`
- **Identity Note:** `TASK-044` is already allocated to ProjectFramework 2.0 / AI-ControlTower Protocol Integration and `TASK-045` has its own preserved response-close lineage. This registration uses `TASK-046` under explicit user confirmation and does not rewrite either prior Task.

- **User Instruction:** Remove `[Chat]` and `[Required Read]` from the canonical Final Response.

- **Problem:** The current mandatory Final Response close exposes four fields:
  `[Next Action]`, `[Chat]`, `[Reason]`, and `[Required Read]`.
  `[Chat]` and `[Required Read]` expose Framework continuity/routing metadata
  in every user-facing response even when that metadata does not need to be
  presented to the user.

- **Approved direction:** Simplify the canonical Final Response close to exactly:
  1. `### ทำอะไรไป?`
  2. `### และถัดไปคืออะไร?`
  3. `[Next Action]: <one exact next action or ไม่มีขั้นตอนถัดไป>`
  4. `[Reason]: <concise reason>`

  `[Chat]` and `[Required Read]` MUST NOT appear as mandatory Final Response
  fields after this Task is implemented.

- **Continuity boundary:** Removing `[Chat]` from the user-facing close must not
  remove Project continuity semantics. Chat/session continuation state remains
  governed internally through applicable `03 Current State`, `09 Handoff`,
  `OUT-* / AUTH-* / ACT-* / ENV-*`, and related canonical sources.

- **Required-read boundary:** Removing `[Required Read]` from the user-facing
  close must not remove bootstrap/read-routing requirements.
  `PROJECT-BOOTSTRAP.md → 00 → 01 → 03 → task-specific source → 09 when
  applicable` remains an internal governance/read contract rather than a
  mandatory field emitted in every Final Response.

- **Final-close rule after implementation:** `[Next Action]` and `[Reason]`
  render as separate Markdown paragraphs in that order, and nothing follows
  `[Reason]`.

- **Scope:** Update all current normative/distribution surfaces that define,
  validate, reproduce, or test the four-field Final Response contract,
  including Core Governance, SKILL, maintained templates/starters, README and
  migration guidance, Response Close Completeness Gate semantics, and pressure
  scenarios. Preserve historical specs/plans/amendments/evidence when their
  four-field representation was true at capture time.

- **TASK-042 / TASK-043 compatibility:** Preserve their finalization and
  strict-interface guarantees while changing the canonical close shape from
  four fields to two. Completeness validation must validate the new contract,
  not continue requiring removed fields.

- **Brownfield rule:** Existing initialized Projects remain locally pinned and
  do not silently acquire the new Final Response contract. Adoption follows
  governed `[Project Upgrade]`.

- **Release classification:** `BREAKING_RESPONSE_INTERFACE`; target the next
  major Framework line. Exact Framework/Schema version must be confirmed by
  the design before implementation.

- **Implementation boundary:** Task registration only. Do not modify the
  current Final Response contract, Core/SKILL/templates/tests, or release
  descriptor until a separate design is approved.

- **Completion criteria:** Current Framework surfaces unanimously require only
  `[Next Action]` + `[Reason]`; no current normative surface still mandates
  `[Chat]` or `[Required Read]`; internal continuity/read routing remains
  intact; historical provenance is preserved; migration behavior is explicit;
  pressure scenarios cover the new close; applicable verification passes
  before Task completion.

- **Supersession / Cancellation:** On 2026-09-10 the user explicitly required `[Next Goal]` to remain mandatory, selected Framework 1.15 instead of 2.0.0, and invoked OUT-013 reconciliation. The original two-field `BREAKING_RESPONSE_INTERFACE` direction is cancelled before implementation.
- **Current Implementation Baseline:** TASK-045 Framework `1.15.0` (`Next Action -> Next Goal -> Reason`), terminally verified by OUT-013 without changing TASK-045 historical lineage.
- **Design Spec:** `docs/superpowers/specs/2026-09-10-task046-framework115-reconciliation-design.md`
- **Reconciliation Design Self-Review:** initial checkpoint `TASK046_SPEC_SELF_REVIEW 13/13 PASS`; revised spec `OUT013_REVISED_SPEC_SELF_REVIEW 18/18 PASS`; final revised review `OUT013_REVISED_SPEC_FINAL_SELF_REVIEW 20/20 PASS`.
- **Reconciliation Design State:** `USER_APPROVED_FINAL_DESIGN / SPEC_APPROVED` / commit `f5f8ecf3551d3fd3d0adc10def1fd0fe5c0847d2`.
- **Implementation Plan:** `docs/superpowers/plans/2026-09-10-out013-framework115-reconciliation.md`.
- **Plan State:** `WRITTEN / SELF_REVIEWED / EXECUTION_NOT_STARTED`; `OUT013_PLAN_SELF_REVIEW 19/19 PASS`.
- **Goal:** `OUT-013 / AUTH-013 / ACT-025 / ENV-013`
- **Historical Registration:** original registration preserved in commit `b42a2f4a536b851edf46b2b94139a0bc5932ea07` and reconciliation ancestry commit `caf2a19`.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป for TASK-046; its implementation remains cancelled and local OUT-013 is complete.

## OUT-013 — Framework 1.15 Reconciliation Terminal State

- **Status:** `DONE / VERIFIED_COMPLETE / TERMINAL_RECONCILED`
- **Terminal lifecycle:** `OUT-013 ACHIEVED / AUTH-013 TERMINATED / ACT-025 DONE / ENV-013 EXPIRED`
- **Frozen candidate:** commit `16664a8b61d1641a842210773c8f997178502be5`; tree `e2db01ce75fb9c5abf7c442f6d103120c09b8a3d`; Framework-Source tree `835c5a24c909ef7de2d413c46a6451746ed5fbf0`.
- **Verification:** `OUT013_RED 23/27`; `OUT013_AFFECTED 27/27`; `OUT013_RELEASE_FULL 29/29 PASS`; exactly one RELEASE_FULL PASS run on the unchanged candidate.
- **Structural checks:** Registered commands `7/7 PASS`; scenarios `432/432 PASS`; maintained starter stamps `22/22 PASS`; V2 spec/plan/merge-manifest blob equality `3/3 PASS`.
- **Release evidence:** `docs/superpowers/evidence/2026-09-10-out013-framework115-reconciliation-release-full.md`.
- **Release evidence commit:** `009b4dbd5de93f56d5f9eb1c2ce1a1dedc4eedb7`.
- **Preservation:** TASK-044 remains `CANCELLED / IMPLEMENTATION_NOT_STARTED`; TASK-045 remains `DONE / VERIFIED_COMPLETE` with its historical candidate/evidence and byte-semantics preserved; TASK-046 remains `CANCELLED / SUPERSEDED_BEFORE_IMPLEMENTATION`.
- **Publication State:** `NOT_AUTHORIZED / NOT_PUSHED`.
- **Prohibited boundaries:** no push, PR, merge, AI-ControlTower mutation, V2 cutover, runtime/parser/validator/CLI implementation, destructive branch/worktree deletion, Root/Binding mutation, external disclosure, or secret-value persistence.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป for local OUT-013 completion; publication/adoption requires separate authority.

## Task #47 — Response Close UI Rendering Compliance Regression

- **ID:** `TASK-047`
- **Status:** `DONE`
- **Type:** Framework response protocol / UI-visible compliance regression
- **Problem:** a live ChatGPT response after successful `.md` bootstrap emitted bare `[Next Action]:` and `[Next Goal]:` lines; the UI hid those fields while `[Reason]:` remained visible, causing an incorrect `PASS` claim even though the visible response close was incomplete.
- **Root Cause:** execution/compliance failure against an already-correct Framework 1.15 contract. Current `Framework-Source/SKILL.md` requires Markdown-safe wrappers and Scenario 432 explicitly fails hidden/non-visible labels. No missing Framework semantic rule was found.
- **User Goal:** `[Goal] ลงและปิด Task สำหรับ footer rendering/compliance regression ให้ยืนยันว่า [Next Action] → [Next Goal] → [Reason] แสดงครบใน UI`.
- **Design State:** `USER_APPROVED_BOUNDED_CHANGE / INLINE_DESIGN_APPROVED` — ACTOR-001 replied `อนุมัติ` after the bounded design was presented.
- **Goal / Authority / Action / Envelope:** `OUT-015 ACHIEVED / AUTH-015 TERMINATED / ACT-027 DONE / ENV-015 EXPIRED`.
- **Approved Direction:** do not modify Framework semantics/version merely to restate an existing rule; register the regression, verify Scenario 432 and the current Markdown-safe contract, use live ChatGPT UI acceptance as the user-facing acceptance gate, persist evidence/lifecycle, and commit locally without push.
- **Acceptance Criteria:** current SKILL safe-wrapper rule present; Scenario 432 present and hidden-label failure preserved; all three footer fields visibly render in order in live ChatGPT UI; no content follows Reason; bounded structural verification passes; no Framework-Source semantic change; local completion commit observed; Task/Goal terminal state persisted.
- **Evidence:** `EVD-090` / `EVD-091` — regression observation/root cause/TDD RED/design+UI acceptance plus bounded GREEN verification and completion checkpoint.
- **Implementation Boundary:** Project Task/Project Source lifecycle and evidence only unless verification discovers a genuine Framework defect; no runtime/UI hook/parser/validator/CLI; no push/publication; no Root/Binding mutation.
- **Verification Result:** `TASK047_GREEN PASS`; Scenario 432 + Markdown-safe SKILL contract PASS; live UI USER_CONFIRMED; `git diff --check` PASS; Framework-Source unchanged.
- **Completion Checkpoint Commit:** `196ddd0d5a2ec7c48c7a9232bafc909b0284522b`.
- **Publication State:** `PUBLISHED_TO_ORIGIN_MAIN / PERSISTED / NOT_PENDING`.
- **Published Commits:** `196ddd0d5a2ec7c48c7a9232bafc909b0284522b` (registration) + `bc880c75190f967a3b87c2842b8cc284f8a3bcab` (terminal close), freshly observed on `origin/main` before reconciliation.
- **Publication Reconciliation:** `OUT-016 ACHIEVED / AUTH-016 TERMINATED / ACT-028 DONE / ENV-016 EXPIRED`; evidence `EVD-092 / CHG-092`; this reconciliation is complete when the active successor set is freshly read from canonical `origin/main`.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป.

## Task #48 — `[Project Path]` Workspace & MCP Execution Routing

- **ID:** `TASK-048`
- **Status:** `DONE`
- **Type:** Framework command / workspace-role and MCP execution-routing feature
- **depends_on:** `[TASK-027, TASK-043]`
- **blocks:** `[]`
- **enables:** `[]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `VERIFIED_COMPLETE / MERGED_TO_MAIN / RECONCILIATION_PERSISTED`
- **Problem:** `[Project Path]` does not yet distinguish Develop Workspace from Production Workspace or expose one exact MCP execution route with deterministic declared fallback/recovery behavior. Agents therefore need a strict contract for where source may be edited/built/tested, where artifacts may only be deployed/run, and which MCP may execute when Primary is unavailable.
- **User-approved direction:** Extend `[Project Path]` as the unified fresh read/verification view while preserving canonical ownership: `FRAMEWORK-001` / Project Location Binding for repository + environment-scoped Local Workspace binding/routing truth, `40 Technical Design` for Develop Workspace role/type/location/durability and active-workspace semantics, `60 Deployment Plan` for applicable deployment/runtime mapping, `Project-Execution/tools.md` for exact Primary/fallback policy, and `Project-Execution/fallback-log.md` for append-only actual fallback history.
- **Approved Workspace Contract:** Develop Workspace = `EDIT / BUILD / TEST / PACKAGE / VERIFY`; Production Workspace = `DEPLOY / RUN / HEALTH_CHECK / OBSERVE_RUNTIME`; direct Production source mutation is `FORBIDDEN`.
- **Canonical Ownership:** Project Location Binding remains location/routing-only and does not acquire `workspace_role`, `source_mutation`, Canonical Implementation Source, active Develop Workspace, or Production runtime authority. Local ↔ Remote Durable relocation changes governed `40` workspace semantics and changes `FRAMEWORK-001` only when a persistent Local Workspace Binding delta actually exists.
- **Approved MCP Contract:** exact Primary MCP; `ORDERED_ALLOW_LIST` auto fallback only to explicitly declared eligible fallbacks; no fallback by recency/availability/similarity; no eligible declared MCP = `FAIL_CLOSED`.
- **Approved Recovery Contract:** `CHECKPOINT_FAILBACK` — do not switch back to recovered Primary mid-action; finish/persist/verify the current bounded action/checkpoint, re-verify Primary target identity/capability, log recovery/failback, then use Primary for the next action.
- **Unknown-Result Contract:** connection loss after possible submission yields `RESULT_VERIFICATION_REQUIRED`; verify resulting state before retry; unprovable result = `FAIL_CLOSED`.
- **Fallback Log:** applicability-driven `Project-Execution/fallback-log.md`, append-only operational incident history; `MCP-FB-*` is correlation labeling only, not a Project Stable-ID family; no credentials/secrets.
- **Strict `[Project Path]` Order:** Framework Path → Git Path → Storage Path → Develop Workspace → Production Workspace → MCP Execution → Build / Deployment Mapping → Continuity.
- **Production Applicability:** explicit no-Production truth = `NOT_APPLICABLE`; applicable-but-unresolved Production target = `APPLICABLE` + `NOT_VERIFIED`; insufficient evidence to decide applicability = `VERIFICATION_REQUIRED` + `NOT_VERIFIED`; absence alone is never silently interpreted as `NOT_APPLICABLE`.
- **Brownfield Rule:** no silent adoption/inference. Existing verified implementation Workspace may be Previewed as Develop only with evidence; Production is never inferred; connected/recent MCPs never become fallback automatically; Projects without explicit fallback remain `fallback_mode: NONE`.
- **Authority Boundary:** `[Project Path]` remains read/verify/routing presentation. Correct paths and an ACTIVE MCP do not grant mutation, deploy, push/publication, Root/Binding, disclosure, secret, Decision, or runtime privilege.
- **Implementation Boundary:** local TASK-048 implementation is complete and state-bound to verified Framework 1.16 candidate `abc4b5316a7f3bbc9b4a8c0f5b5c509904a26185`. Distribution semantics/templates changed only within approved scope; active Project Source pin remains Framework `1.15.0`; no runtime/router/watcher/validator/CLI/credential/deployment automation was introduced. The user explicitly authorized branch push + PR and then PR merge to `main` on `2026-09-12`; GitHub Release/tag publication and consuming-Project `[Project Upgrade]` remain separately governed and were not performed.
- **Design Spec:** `docs/superpowers/specs/2026-09-12-task048-project-path-workspace-mcp-routing-design.md`
- **Design State:** `USER_APPROVED_FINAL_DESIGN / WRITTEN_SPEC_APPROVED`
- **Written Spec Approval:** `USER_EXPLICIT_APPROVAL — 2026-09-12`
- **Implementation Plan:** `docs/superpowers/plans/2026-09-12-task048-project-path-workspace-mcp-routing.md`
- **Plan State:** `COMPLETE / AFFECTED_PASS / RELEASE_FULL_PASS / EVIDENCE_RECORDED / MERGED_TO_MAIN / RECONCILIATION_PERSISTED / NOT_RELEASED`
- **Plan Self-Review:** `PASS` — approved spec sections mapped to Tasks 1–7; scenario allocation `433–468` freshly collision-checked against current `1–432`; forbidden placeholder scan clean; canonical ownership/Production applicability/relocation/MCP fallback/one-RELEASE_FULL/publication boundaries covered.
- **Execution Mode:** `INLINE_EXECUTION_IN_ISOLATED_WORKTREE` at `E:\GitHub\ProjectFramework\.worktrees\task048-framework116`; no implementation mutation was performed on canonical main checkout.
- **Implementation Commits:** `79843e3` RED scenarios; `90b1e68` normative Framework 1.16 contract; `bb67ef5` workspace relocation + Production applicability templates; `2b88f54` MCP fallback/failback profile + log; `004c631` README/migration/starter propagation.
- **Verification Progress:** TDD RED `TASK048_RED 9/18` expected; structural GREEN `TASK048_STRUCTURAL 18/18 PASS`; cumulative AFFECTED `TASK048_AFFECTED 47/47 PASS`; post-verifier-repair AFFECTED `47/47 PASS`; final replacement candidate RELEASE_FULL `TASK048_RELEASE_FULL 56/56 PASS` on its first and only release-mode run; pressure scenarios `1–468` contiguous/unique.
- **Invalidated Candidate:** `d7876ba288f9f113f831cc4540d5069494f84736` / tree `c01d6a105b40a515e74f16c10a7ea0ec4f025c27` / Framework-Source tree `5e06595f419d21b03ed2ef8e959189594628dbf2`. RELEASE_FULL run #1 exited before semantic release assertions because the scratch verifier decoded `git show` through Windows `cp874` and raised `UnicodeDecodeError`; candidate is not reused as release evidence. Framework-Source semantics were not changed by this finding.
- **Verifier Repair:** scratch-only verifier now forces Git subprocess decoding to UTF-8; post-repair AFFECTED `47/47 PASS`. The verifier file is ignored/non-candidate state.
- **Candidate State:** `VERIFIED_FINAL_CANDIDATE`; commit `abc4b5316a7f3bbc9b4a8c0f5b5c509904a26185`; tree `266b2cf7d03d516c9bcab9f81790a92f3c84d9c7`; Framework-Source tree `5e06595f419d21b03ed2ef8e959189594628dbf2`.
- **Release Evidence:** `docs/superpowers/evidence/2026-09-12-task-048-project-path-workspace-mcp-routing-release-full.md`.
- **Evidence Commit:** `8fbb47cb61d50f81c49979a32863139be64959af`.
- **Pull Request:** `#30` — `https://github.com/captainhuke-dev/ProjectFramework/pull/30` — `MERGED`, base `main`, head `task048-framework116`; merge commit `7dd5b2691dce86dd211c5a58ff4ed6cbe345967f`; merged branch head `07694607e2c4487a9b9572dbead1fe73fab1fd29`; canonical Framework-Source tree `5e06595f419d21b03ed2ef8e959189594628dbf2`.
- **Completion State:** `LOCAL_VERIFIED_COMPLETE / TASK-048 DONE / CANONICAL_MAIN_INTEGRATED`.
- **Goal Lineage:** none created for TASK-048 execution; do not synthesize `OUT-* / AUTH-* / ACT-* / ENV-*` after the fact.
- **Publication State:** `MERGED_TO_MAIN / PR #30 / merge 7dd5b269 / PERSISTED / NOT_PENDING / NOT_RELEASED`.
- **Design Baseline:** `main@a1da22d64ff8e30658a4aaf8b675705a0e043dc9`
- **Target Release:** Framework `1.16.0` / Schema `1.0.0` / release format `3`.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป for TASK-048 integration. GitHub Release/tag publication and consuming-Project `[Project Upgrade]` remain separately governed.
- **Release Classification:** `BACKWARD_COMPATIBLE_REGISTERED_COMMAND_AND_EXECUTION_ROUTING_FEATURE`.
- **Completion Criteria:** approved strict `[Project Path]` interface; preserved canonical ownership; explicit Develop/Production roles; Local ↔ Remote Durable relocation; exact Production applicability representation; Production source-mutation prohibition; exact Primary and ordered declared fallback; durable fallback log; unknown-result verification; checkpoint failback; Brownfield/Greenfield safety; preserved authority separation; applicable TDD/AFFECTED/final release verification; publication separately governed.

## Task #49 — Canonical Self-Hosting Release Reconciliation

- **ID:** `TASK-049`
- **Status:** `DONE`
- **Type:** bounded governance / release-lifecycle correction
- **depends_on:** `[TASK-048]`
- **blocks:** `[]`
- **enables:** `[]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `CANONICAL_MAIN_INTEGRATED / VERIFIED_COMPLETE / RELEASE_NOT_PUBLISHED`
- **Problem:** canonical Framework distribution was `1.16.0` while ProjectFramework self-host Project Source/bootstrap remained `1.15.0` because consuming-Project pin semantics were applied to the canonical upstream repository itself.
- **Implemented Direction:** canonical ProjectFramework has a narrow mandatory governed post-merge self-host reconciliation rule without redundant `[Project Upgrade]`; ordinary consuming Projects remain pinned and use `[Project Upgrade]`; unresolved reconciliation is `RECONCILIATION_REQUIRED`; no runtime automation was introduced.
- **Goal Lifecycle:** `OUT-017 ACHIEVED / AUTH-017 TERMINATED / ACT-029 DONE / ENV-017 EXPIRED`.
- **Design State:** `USER_APPROVED_BOUNDED_CHANGE / INLINE_DESIGN_APPROVED`.
- **Goal Checkpoint:** `EVD-093 / CHG-093`; promotion `EVD-094 / CHG-094 / MIG-003`; local terminal `EVD-095 / CHG-095`; canonical merge readback `EVD-096 / CHG-096`.
- **Implementation Commits:** Goal checkpoint `7895bf9`; RED `e56f409`; normative `9f5471b690df09d1993cb931a653fd85b35a2cd0`; verified self-host promotion `759c7dd29c060888b3ef9c4424cdcb17cd809eed`; branch terminal `76ee6ed`.
- **TDD / Verification:** `TASK049_RED 5/10` expected → `TASK049_STRUCTURAL 8/10` → `TASK049_AFFECTED 25/25 PASS` → `TASK049_RELEASE_FULL 23/23 PASS_RUN_1`.
- **Verified Candidate:** `759c7dd29c060888b3ef9c4424cdcb17cd809eed` / tree `6659e0e8494cbcff5daea89e8af16bf5ff4311b8` / Framework-Source tree `a84e7bd0ed56bd73a7e2cb6c642885d9fefeb24a`.
- **Self-Host State:** canonical active `FRAMEWORK-001`, all active Project Source documents, Framework distribution, and `PROJECT-BOOTSTRAP.md` coherently use Framework `1.16.0` / Schema `1.0.0`; UUID/binding/history preservation verified.
- **Evidence:** `docs/superpowers/evidence/2026-09-12-task-049-canonical-self-hosting-release-full.md`.
- **Completion State:** `VERIFIED_COMPLETE / TASK-049 DONE / CANONICAL_MAIN_INTEGRATED`.
- **Publication State:** `MERGED_TO_MAIN / PR #31 / merge 4039be4 / PERSISTED / NOT_RELEASED`.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป for TASK-049; GitHub Release/tag remains separately governed.

## Task #50 — GitHub Issue Backlog Reconciliation Audit

- **ID:** `TASK-050`
- **Status:** `DONE`
- **Type:** governance / tracker reconciliation / backlog audit
- **depends_on:** `[TASK-049]`
- **blocks:** `[]`
- **enables:** `[TASK-051]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `VERIFIED_COMPLETE / ISSUE_TRACKER_RECONCILED / LOCAL_TERMINAL_PERSISTENCE`
- **User Goal:** audit GitHub Issues #25/#29 against Framework current state and reconcile Issue tracker with TASK ledger.
- **Canonical Baseline:** `origin/main@4039be4` after PR #31 merge; active Framework/Project self-host pin `1.16.0`.
- **Issue #25 Result:** `CLOSED / comments=1 / RESOLVED_BY_STRONGER_EXISTING_CONTRACT`; reconciliation comment records that current TASK-041/TASK-042 bootstrap semantics are stronger than the proposal; backend `closed_at=2026-09-13T03:30:48Z`.
- **Issue #29 Result:** `OPEN / comments=1 / GENUINE_PENDING_BACKLOG`; mapping comment points to `TASK-051 / TODO / DESIGN_REQUIRED / IMPLEMENTATION_NOT_STARTED` and explicitly states TASK-050 does not start implementation.
- **Goal / Authority / Action / Envelope:** `OUT-018 ACHIEVED / AUTH-018 TERMINATED / ACT-030 DONE / ENV-018 EXPIRED`.
- **Evidence / Change:** `EVD-096 / EVD-097 / CHG-096 / CHG-097`.
- **Audit Checkpoint Commit:** `4d1f225ef067d60d4884e54a971214a3281ad304`.
- **Completion Criteria Met:** tracker readback proves #25 CLOSED and #29 OPEN; #29 explicitly references TASK-051; ledger backlog counts are exact (`TODO=1 / IN_PROGRESS=0 / BLOCKED=0`); TASK-049 canonical integration truth is corrected; no TASK-051 implementation or Framework semantic change occurred; terminal successor set requires fresh post-commit readback before external completion claim.
- **Publication Boundary:** issue tracker mutations completed under OUT-018; push/PR/merge of this local ledger reconciliation is separately governed and was not authorized/performed.
- **Exact Next Step:** ไม่มีขั้นตอนถัดไป for TASK-050; TASK-051 remains separate TODO.
## Task #51 — Risk-Tiered Feature Delivery Fast Path

- **ID:** `TASK-051`
- **Status:** `DONE`
- **Type:** Framework architecture / feature-delivery workflow design and implementation
- **Source Issue:** GitHub Issue `#29` — `CLOSED` at `2026-09-13T15:47:48Z` through TASK-055 reconciliation PR #33 `Closes #29`.
- **depends_on:** `[]`
- **blocks:** `[]`
- **enables:** `[]`
- **parallelizable_with:** `[]`
- **priority:** `MEDIUM`
- **readiness:** `DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / ISSUE_CLOSED`
- **Implementation State:** `LOCAL_VERIFIED_COMPLETE / RELEASE_CANDIDATE_VERIFIED / MERGED_TO_MAIN / PR_32`.
- **Goal / Authority / Action / Envelope:** `OUT-019 ACHIEVED / AUTH-019 TERMINATED / ACT-031 DONE / ENV-019 EXPIRED`.
- **Design:** `USER_APPROVED_FINAL_DESIGN / SELF_REVIEWED`; spec `docs/superpowers/specs/2026-09-13-task051-risk-tiered-feature-delivery-fast-path-design.md`.
- **Plan:** `IMPLEMENTATION_PLAN_EXECUTED`; plan `docs/superpowers/plans/2026-09-13-task051-risk-tiered-feature-delivery-fast-path.md`.
- **Implementation Commits:** `bff9d39` RED scenarios; `fc0859e` normative contract; `008fc93` propagation/frozen candidate.
- **Review:** independent reviewer `e289f236-6dee-46fa-83b6-d0335fea12a5`; `10/10 PASS / Critical 0 / Important 0 / Minor 0 / REVIEW_PASS`.
- **Verification:** `RED 13/13 PASS_EXPECTED_MISSING_CONTRACT → STRUCTURAL 34/34 PASS → AFFECTED 48/48 PASS → RELEASE_FULL 49/49 PASS PASS_RUN_1`.
- **Candidate:** HEAD `008fc934a84d595d163a4bc25d974fcd35bac335`; tree `bb77342982cfa7dea0fd60151108cee6463657b8`; Framework-Source tree `5a6a711861bbbc1e6f9315361921e28625cce854`.
- **Evidence:** `EVD-101 / EVD-102 / CHG-101 / CHG-102`; `docs/superpowers/evidence/2026-09-13-task-051-risk-tiered-feature-delivery-fast-path-release-full.md`.
- **Publication State:** `MERGED_TO_MAIN / PR_32 / merge f6330e9 / NOT_RELEASED`.
- **Self-Host Result:** TASK-055 completed canonical Framework 1.18 self-host reconciliation through PR #33 merge `5b067a1c2fcfeab867ba3879a76f675904566e27`; Issue #29 is CLOSED.
- **Pull Request:** `#32` — `https://github.com/captainhuke-dev/ProjectFramework/pull/32` — MERGED to `main` at `f6330e9929c28977d43fc149b864d590df1c2816`.
- **Exact Next Step:** none for TASK-051; tag/GitHub Release remain separately governed.
## Task #52 — Project Upgrade One-Session Fast Path

- **ID:** `TASK-052`
- **Status:** `DONE`
- **Type:** Framework architecture / Project Upgrade workflow acceleration
- **Source:** ACTOR-001 explicit Goal on 2026-09-13 to design and implement a one-session compatible Project Upgrade path.
- **depends_on:** `[TASK-051]`
- **blocks:** `[]`
- **enables:** `[]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN`
- **Problem:** compatible upgrades remained slow because comparison, prepare intent, Preview, approval, mutation persistence, verification, and canonical self-host reconciliation required redundant rounds even when candidate/evidence/authority were unchanged.
- **Approved Architecture:** Single-Preview / Single-Approval Upgrade Transaction; one bounded mutation batch; proof-domain separation between Framework Release Acceptance and Project Upgrade Acceptance; exact release-evidence reuse for FAST_PATH and bounded compatible ASSESSED_PATH; selective recovery; canonical self-host chaining when exact Preview and authority cover integration + Root reconciliation.
- **Target Release:** Framework `1.18.0` / Schema `1.0.0` / release format `3`.
- **Stacked Work:** deliberate child of TASK-051 terminal local commit `26fbb3c0ff298b183f23c7dabe5132dc11002185`; parent Framework 1.17 candidate/evidence remains preserved and unpublished.
- **Goal / Authority / Action / Envelope:** `OUT-020 ACHIEVED / AUTH-020 TERMINATED / ACT-032 DONE / ENV-020 EXPIRED`.
- **Design:** `USER_APPROVED_FINAL_DESIGN / WRITTEN_SPEC_SELF_REVIEWED`; spec `docs/superpowers/specs/2026-09-13-project-upgrade-one-session-fast-path-design.md`; spec commit `5adc2ed`; self-review `15/15 PASS`.
- **Plan:** `IMPLEMENTATION_PLAN_EXECUTED`; plan `docs/superpowers/plans/2026-09-13-project-upgrade-one-session-fast-path.md`; plan commit `07f8026`; self-review `16/16 PASS`; Inline Execution.
- **Implementation Commits:** `27485c2` RED scenarios; `a33ced7` normative contract; `85b98f4` propagation; `e3f1f96` pressure expectation forward-port; `bc36a80` + `48212bb` independent-review fixes/current-surface alignment.
- **Review:** `Codex-Independent-Acceptance-Review`; `15/15 PASS / Critical 0 / Important 0 / Minor 0 / REVIEW_PASS`.
- **Verification:** `RED 13/13 PASS_EXPECTED_MISSING_CONTRACT → STRUCTURAL 31/31 PASS → AFFECTED 43/43 PASS → RELEASE_FULL 44/44 PASS PASS_RUN_1`.
- **Candidate:** HEAD `48212bb4f4b577af482afcf5758424eee2f7e036`; tree `601f9ad5041cec9f53188c19998960b93878c534`; Framework-Source tree `929065ccac7e3ecf25fda09de5326bb40c4f8f9c`.
- **Evidence:** `EVD-104 / CHG-104`; `docs/superpowers/evidence/2026-09-13-task-052-project-upgrade-one-session-fast-path-release-full.md`.
- **Implementation State:** `LOCAL_VERIFIED_COMPLETE / RELEASE_CANDIDATE_VERIFIED / MERGED_TO_MAIN / PR_32`.
- **Publication State:** `MERGED_TO_MAIN / PR_32 / merge f6330e9 / NOT_RELEASED`.
- **Self-Host Result:** TASK-055 completed canonical 1.18 self-host reconciliation through PR #33 merge `5b067a1c2fcfeab867ba3879a76f675904566e27`; AUTH-021 is terminal.
- **Reviewer Side-Effect Handling:** reviewer-invented TASK-053 and residual-latency registration are not authorized Project backlog and are excluded from terminal truth.
- **Pull Request:** `#32` — `https://github.com/captainhuke-dev/ProjectFramework/pull/32` — MERGED to `main` at `f6330e9929c28977d43fc149b864d590df1c2816`.
- **Publication Evidence:** `EVD-105 / CHG-105`; `docs/superpowers/evidence/2026-09-13-task-051-task-052-pr32-publication.md`.
- **Exact Next Step:** none for TASK-052; tag/GitHub Release remain separately governed.

## Task #55 — PR #32 Post-Merge Canonical Self-Host Reconciliation

- **ID:** `TASK-055`
- **Status:** `DONE`
- **Type:** bounded governance / canonical self-host post-merge reconciliation
- **Source Goal:** ACTOR-001 explicit `[Goal]` on 2026-09-13 to reconcile PR #32 through Framework 1.18 self-host convergence, merge evidence persistence, Project Source/Bootstrap reconciliation, and Issue #29 closure.
- **depends_on:** `[TASK-051, TASK-052]`
- **blocks:** `[]`
- **enables:** `[]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_33 / ISSUE_CLOSED`
- **Canonical Release Basis:** PR #32 MERGED at `f6330e9929c28977d43fc149b864d590df1c2816`; Framework-Source tree `929065ccac7e3ecf25fda09de5326bb40c4f8f9c` exactly matches TASK-052 release acceptance.
- **Reconciliation Candidate:** `70ef176be0f07e9ce82aeeceb90b864bc28d8ea2`; `TASK055_AFFECTED 163/163 PASS`; independent HIGH review `12/12 PASS / Critical 0 / Important 0 / Minor 0 / REVIEW_PASS`.
- **Canonical Reconciliation:** PR #33 MERGED to `main` at `5b067a1c2fcfeab867ba3879a76f675904566e27` on `2026-09-13T15:47:47Z`.
- **Issue #29:** `CLOSED` at `2026-09-13T15:47:48Z` through PR #33 exact `Closes #29`; fresh readback verified the closed state.
- **Goal / Authority / Action / Envelope:** `OUT-021 ACHIEVED / AUTH-021 TERMINATED / ACT-033 DONE / ENV-021 EXPIRED`.
- **Migration:** `MIG-004 COMPLETED / PERSISTED / NOT_PENDING` — canonical self-host Framework 1.16.0 → 1.18.0; ordinary consuming Projects remain unaffected.
- **Evidence:** `EVD-106 / EVD-107 / CHG-106 / CHG-107`; `docs/superpowers/evidence/2026-09-13-task-055-pr33-terminal-reconciliation.md`.
- **Implementation Boundary Preserved:** no tag/GitHub Release, binding change, force/history rewrite, destructive cleanup, runtime automation, external AI disclosure, secret persistence, or Framework-Source mutation after release acceptance.
- **Terminal Persistence Contract:** this terminal record is externally claimable when this exact successor set is observed on canonical `origin/main`; that observation does not require another successor solely to restate completion.
- **Exact Next Step:** none for TASK-055.

## Task #57 — ProjectFramework 1.19 AI-ControlTower Governance Support Layer

- **ID:** `TASK-057`
- **Status:** `DONE`
- **Type:** Framework architecture / AI-ControlTower governance support contract layer
- **Source Goal:** ACTOR-001 explicit `[Goal]` on 2026-09-14: `ดำเนิน ProjectFramework 1.19 AI-ControlTower Governance Support Layer ต่อจาก Design Sections 1–2 ที่อนุมัติแล้ว จนถึง verified completion โดยยังไม่ implement AI-ControlTower runtime`.
- **depends_on:** `[TASK-055]`
- **blocks:** `[]`
- **enables:** `[]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `DONE / VERIFIED_COMPLETE / RELEASE_CANDIDATE_VERIFIED / PUSHED_TO_ORIGIN_MAIN / NOT_TAGGED / NOT_RELEASED`
- **Problem:** ProjectFramework 1.18 has strong governance, Task, verification, publication, capability/tool/trust, and continuity semantics, but future AI-ControlTower/Multica consumers need deterministic declarative contracts for Plan/Task/Verify execution without transferring Project authority to a runtime/control plane.
- **Approved Architecture:** Approach A — Schema-first Declarative Contracts; Plan Contract + Task Contract; nested non-authoritative Execution Envelope; mandatory Expected IPOCV; separate Task Record / Actual IPOCV; state-bound Verification Record; `R4_CTX` Current Truth; pure fail-closed Task Ready Gate; separate operational execution state; Multica claim/coordination-only authority; domain-owned source-of-truth reconciliation; declarative Executor Profile + Project Adapter; filter-before-rank execution selection; exact-SHA candidate verification; fresh `INTEGRATION_GATE`; integration/merge reconciliation; canonical Task owner retains Task DONE authority.
- **Target Release:** Framework `1.19.0` / Project Source Schema `1.0.0` / release format `3`.
- **Design Sections:** `1–6 USER_APPROVED / LOCKED` on 2026-09-14.
- **Design Spec:** `docs/superpowers/specs/2026-09-14-task057-ai-controltower-governance-support-layer-design.md`.
- **Design Spec Commit:** `554c449eade42815a2e228d174d4f6e5a8cbb440`.
- **Written Spec Approval:** `ACTOR-001 EXPLICIT_APPROVAL / 2026-09-14`.
- **Implementation Plan:** `docs/superpowers/plans/2026-09-14-task057-ai-controltower-governance-support-layer.md`.
- **Plan State:** `WRITTEN / SELF_REVIEWED / EXECUTED`.
- **Design State:** `WRITTEN_SPEC_APPROVED / USER_APPROVED`; ACTOR-001 explicitly approved the written spec on 2026-09-14; implementation is complete and verified.
- **Planner / Execution Handoff:** execution handoff completed. ACTOR-001 explicitly authorized governed execution (อินาซื้อมั) on 2026-09-15 after a clean fast-forward of `origin/main`; an eligible Executor was selected under the current Task Contract, Execution Envelope, AUTH, `R4_CTX`, capability/tool/trust/executor policy, and Ready Gate. Independent Verifier selection was separate (fresh-context review subagent).
- **Goal Link:** the exact user Goal is persisted above as this Task's durable source. This registration intentionally does not synthesize `OUT-* / AUTH-* / ACT-* / ENV-*` after the fact; any later Project Source Goal lifecycle allocation must follow current Goal governance.
- **Implementation Boundary:** governance/documentation contracts and maintained starters only. Do not implement AI-ControlTower runtime, Multica runtime, Control Plane, scheduler, queue, task database, lease/fencing service, distributed lock, automatic state engine, model/router service, executable Project Adapter, merge bot, CI runner, API server, automatic Task DONE updater, Structured Core, Generated Governance, or Transaction Mode runtime/implementation as part of TASK-057.
- **Completion Criteria:** written spec explicitly approved; implementation plan completed; TDD/pressure scenarios added before normative implementation; Framework 1.19 contract/starters implemented; Plan/Task/Verify, IPOCV, R4_CTX, Ready Gate/state machine, Multica/source-of-truth, Executor/Profile/Adapter, exact-SHA verification and integration reconciliation remain consistent; required independent review passes; AFFECTED passes; one final unchanged-candidate `RELEASE_FULL` passes; evidence and durable completion commit are observed; canonical Task/Goal lifecycle is reconciled truthfully.
- **Publication Boundary:** registration/design persistence on canonical `main` does not by itself authorize future release/tag/deployment or AI-ControlTower runtime mutation; later shared-state actions remain governed by exact current authority.
- **Implementation Commits:** `90f2e50` RED scenarios 529–556; `9f6436a` normative Framework 1.19 declarative execution contracts; `e4b442c` 7 declarative execution contract starters; `a89c3dd` guidance/starter propagation; `bd3b99a` Framework 1.19 release metadata; `f378e0a` Planner/Execution Handoff Boundary in Core projection.
- **Review:** `Hermes-Independent-Review-Subagent` (fresh context, read-only); candidate `f378e0a`; `Critical 0 / Important 0 / Minor 3 / REVIEW_PASS`.
- **Verification:** `TASK057_RED (0 Core-Governance token matches pre-mutation) → TASK057_AFFECTED 96/96 PASS → TASK057_RELEASE_FULL 77/77 PASS PASS_RUN_1`.
- **Candidate:** HEAD `f378e0a0b4796a94ec52ba1286d17d05e6a5c9b2`; tree `f4957c3564f4963bd38f22cf256f3efa5434ff60`; Framework-Source tree `23274ada739c56a10c8edcfc14e6a9a0e46e9a0b`.
- **Evidence:** `docs/superpowers/evidence/2026-09-15-task-057-ai-controltower-governance-support-layer-release-full.md`.
- **Implementation State:** `LOCAL_VERIFIED_COMPLETE / RELEASE_CANDIDATE_VERIFIED / PUSHED_TO_ORIGIN_MAIN`.
- **Publication State:** `PUSHED_TO_ORIGIN_MAIN` (`origin/main = f378e0a`) / `NOT_TAGGED` / `NOT_RELEASED`.
- **Self-Host Result:** active self-host `Project-Source/` (FRAMEWORK-001) and root `PROJECT-BOOTSTRAP.md` remain Framework `1.18.0` / Schema `1.0.0`; no 1.19 self-host promotion occurred.
- **No-Runtime Confirmation:** only `.md`/`.yaml` changed (42 files); no AI-ControlTower/Multica runtime, Control Plane, scheduler, queue, task database, lease/fencing service, distributed lock, automatic state engine, model/router service, executable Project Adapter, merge bot, CI runner, API server, automatic Task DONE updater, Structured Core, Generated Governance, or Transaction Mode runtime introduced.
- **Terminal Persistence Contract:** this terminal record is externally claimable when this exact successor set is observed on canonical `origin/main`; that observation does not require another successor solely to restate completion.
- **Exact Next Step:** none for TASK-057; tag/GitHub Release, self-host 1.19 promotion, and AI-ControlTower runtime mutation remain separately governed.

## Task #58 — AI-ControlTower V4 Interoperability Wave A V2 Deterministic Execution Foundation

- **ID:** `TASK-058`
- **Status:** `DONE`
- **Type:** Framework architecture / AI-ControlTower deterministic execution interoperability contract
- **depends_on:** `[TASK-057]`
- **blocks:** `[]`
- **enables:** `[]`
- **parallelizable_with:** `[]`
- **priority:** `HIGH`
- **readiness:** `DESIGN_SECTIONS_1_TO_6_USER_APPROVED / INTEGRATED_ROLEPLAY_PASS_WITH_CORRECTIONS / WRITTEN_SPEC_USER_APPROVED / IMPLEMENTATION_PLAN_SELF_REVIEWED / SELF_HOST_1_19_RECONCILED / TDD_GREEN / AFFECTED_PASS / INDEPENDENT_REVIEW_ACCEPTED / RELEASE_FULL_PASS_RUN_1 / EVIDENCE_COMMITTED / LOCAL_DONE`
- **Source Direction:** ACTOR-001 on 2026-09-16 instructed creation of Wave A Design V2 from the V4 roleplay, beginning with `Execution State Binding + Operational Transition + Ownership/Fencing + Revision/Input/Result/Verification contracts` while locking the Wave B/C boundary; ACTOR-001 explicitly approved Design Sections 1–6.
- **Problem:** Framework 1.19 provides declarative Plan/Task/Verify, R4 current truth, Task/Verification records, coordination-only Multica semantics and exact-SHA verification, but V4 stress cases require deterministic state binding, versioned/idempotent transition semantics, explicit execution ownership generations/fencing assurance, multi-resource/input identity, non-Git result identity, result acceptance separation, and verification validity without moving runtime authority into ProjectFramework.
- **Approved Architecture:** `Compositional State Binding Hub` — Stable Resource Identity / Revision Set + Execution Input Manifest + state-bound AUTH/R4/workspace/ownership evidence → Execution State Binding; authoritative operational aggregate version + CAS + idempotency; Coordination Claim distinct from Execution Ownership Grant; scoped ownership epoch + `COORDINATION_ONLY < ACCEPTANCE_FENCED < SIDE_EFFECT_FENCED`; Task Record observation distinct from Result Acceptance; Generic Result Identity / Result Set; Verification Result remains `PASS | FAIL | UNKNOWN`; Verification Validity is separate `CURRENT | STALE | INVALIDATED | UNKNOWN`; no mega-record and no new Project authority.
- **Integrated Roleplay Corrections:** (1) canonical order is `claim → ownership grant → finalize State Binding → CAS EXECUTING` because the immutable binding carries ownership epoch/evidence; (2) `VERIFYING → VERIFIED` fresh-revalidates Result Acceptance and requires it still `ELIGIBLE` in addition to Verification `PASS` + validity `CURRENT`. Integrated design roleplay has no unresolved P0 semantic gap after these corrections.
- **Design Spec:** `docs/superpowers/specs/2026-09-16-task058-wave-a-v2-deterministic-execution-foundation-design.md`.
- **Design State:** `SECTIONS_1_TO_6_USER_APPROVED / WRITTEN_SPEC_SELF_REVIEWED / WRITTEN_SPEC_USER_APPROVED`.
- **Compatibility:** additive successor of TASK-057 / Framework 1.19; existing exact-SHA `record_version: 1.0` history remains valid; V2 must not silently reinterpret required v1 record shapes, retrofit Brownfield execution history, add Project Source semantic slots/Stable-ID families, or require AI-ControlTower for Projects that do not use it.
- **Wave Boundary:** Wave A excludes Memory Snapshot/Generation, authenticated event envelope, anti-replay/crypto producer identity, Resume Eligibility/Continuation Controller/Budget (Wave B), and excludes Artifact build lifecycle, Release Transaction, deployment saga, health/migration/rollback-compensation and Project operational lifecycle (Wave C).
- **Implementation Boundary:** governance/documentation contracts and maintained starters only. No AI-ControlTower/Multica runtime, task database, event store, scheduler, queue, lease/heartbeat service, distributed lock, fencing-token generator, CAS datastore, automatic state/acceptance/verification engine, executable adapter, API server, merge bot, release/deployment orchestrator, or automatic Task DONE updater is authorized.
- **Self-Host Precondition:** fresh 2026-09-16 inspection shows Framework distribution `1.19.0` while active ProjectFramework `FRAMEWORK-001`, `PROJECT-BOOTSTRAP.md`, and active Project Source remain pinned to `1.18.0`; TASK-057 explicitly records that no 1.19 self-host promotion occurred. TASK-058 normative implementation must not start until canonical 1.19 self-host reconciliation is completed/verified or an exact separately governed implementation transaction lawfully includes that prerequisite under valid Root authority.
- **Target Version:** planned Framework `1.20.0` / Schema `1.0.0` / release format `3`, conditional on fresh post-self-host baseline remaining exactly Framework `1.19.0` with TASK-057 Framework-Source tree `23274ada739c56a10c8edcfc14e6a9a0e46e9a0b`; material baseline/schema drift requires re-plan before normative mutation.
- **Pressure Contract:** minimum integrated design suite contains 34 scenario classes spanning revision/input identity, CAS/idempotency races, ownership epochs/fencing, result acceptance, non-Git identity, verification evidence/validity, Brownfield compatibility and Wave B/C leakage.
- **Implementation Plan:** `docs/superpowers/plans/2026-09-16-task058-wave-a-v2-deterministic-execution-foundation.md`.
- **Plan State:** `COMPLETE / ALL_10_TASKS_EXECUTED / STOPPED_AT_PUBLICATION_BOUNDARY`; Phase 0 canonical Framework 1.19 self-host reconciliation COMPLETED (MIG-005 / canonical commit `5b08c5c1438aa9898daa13fae4dc00e0bcfc0df5` / terminal `aaddc23760fd1c9657a350fe0c8eebba7da0ef19`); normative implementation proceeds from the reconciled baseline in isolated worktree `task058-wave-a-v2` (branch `task058-wave-a-v2`).
- **AFFECTED verification (2026-09-16):** `AFFECTED PASS 47/47` on the worktree candidate before release freeze — scenario 1–590 contiguous/unique; amendment/Core/SKILL token + semantic alignment; 7 new Wave A V2 starters + required enums; Task Contract 2.0 / Task Record 2.0 / Verification Record 2.0 compatibility rules; 22/22 mockup stamps 1.20.0/1.0.0; release descriptor + latest amendment consistency; no executable/runtime files; no historical amendment edited; git diff --check clean.
- **Independent review (2026-09-16):** fresh-context reviewer (separate context, report-only) completed. All 10 mandatory questions PASS (no authority leak; no silent runtime; no v1 history reinterpretation; grant-before-binding ordering correct; no stale-owner promotion path; no timestamp ordering; no UNKNOWN→PASS; no PASS/validity collapse; no Wave B/C leakage; no Git-only assumption). Cross-cutting checks PASS (scenarios 557–590 contiguous/unique; exact fencing order per path; both corrected cross-section cases present; no new slot/Stable-ID/Command/Risk/lifecycle; TASK-057 files untouched; 0 executable files in diff). Initial verdict CHANGES_REQUIRED with 3 Important + 1 Minor conformance findings, all fixed in `6bd77ed` (REVISION_SET starter aligned to normative nested `revision.exact_identity`; OPERATIONAL_TRANSITION field unified to `result`; `EXECUTION_OWNERSHIP_EVIDENCE` added to §16.3 record-type allocation; `environment_constraints` input class added to amendment §5). Post-fix re-run: `AFFECTED PASS 47/47`.
- **AFFECTED verification (2026-09-16, post-review-fix):** `AFFECTED PASS 47/47` on the exact review-fixed candidate.
- **Execution Role Boundary:** `GPT = PLANNER / LOCAL_LLM_ENGINEER = designated TASK Executor / INDEPENDENT_ENGINEERING_VERIFIER = VERIFY`; `NO_ELIGIBLE_EXECUTOR → FAIL_CLOSED`; no GPT/Codex/generic-shell/undeclared-executor fallback is permitted.
- **Execution Handoff Evaluation (2026-09-16):** `FAIL_CLOSED / NO_ELIGIBLE_EXECUTOR`. Fresh AI-ControlTower readback shows `Project-Execution/tools.md` has `profile_state: ACTIVE`, `primary_tool: VERIFICATION_REQUIRED`, `allowed_tools: []`, `fallback_mode: NONE`, `failure_policy: FAIL_CLOSED`; `Project-Execution/executor-profile.md` remains an unbound template; active AI-ControlTower `03 Current State` also reports `MCP Primary: VERIFICATION_REQUIRED`; Local-LLM/Hermes runtime readiness remains unverified/open under canonical Project issues. No exact eligible/runtime-bound `LOCAL_LLM_ENGINEER` can therefore be activated for TASK-058 at this time.
- **Design Fork Resolution (2026-09-16, ACTOR-001 explicit decision):** a parallel `Design V3` registration (`docs/superpowers/specs/2026-09-16-task058-deterministic-execution-runtime-contract-design.md`, spec commit `dc1353e`) and implementation plan (`docs/superpowers/plans/2026-09-16-task058-deterministic-execution-runtime-contract.md`) were observed on canonical `origin/main` (merge base `38f9993`, canonical head `f819920`), together with implementation branches `task058-framework120` (head `38ed953`, checkpoint `IN_PROGRESS / TOOLING_BLOCKED_BEFORE_CANDIDATE_FREEZE`) and `task058/framework-1.20-deterministic-runtime` (head `c6c47d4`). ACTOR-001 explicitly selected the **Wave A V2 deterministic execution foundation** (this Task's design spec and implementation plan) as the TASK-058 design of record. Design V3 and its branches are recorded `SUPERSEDED / PAUSED / NOT_MERGED`: their files remain on canonical `main` and the two branches as historical provenance only; neither is merged, rebased, or built upon by this Task. Both tracks target Framework `1.20.0`; only the Wave A V2 track is executed.
- **Publication Boundary:** design/planning persistence/local commit does not authorize push, PR/merge, tag/GitHub Release, Project Source Root promotion, AI-ControlTower runtime mutation, Wave B/C implementation, or production/deployment action.
- **Self-Review:** `TASK058_SPEC_SELF_REVIEW PASS`; required semantic tokens, pressure scenarios `1–34`, registration/collision checks, placeholder scan, and diff hygiene passed.
- **Exact Next Step:** ACTOR-001 designated the local execution context as the eligible `LOCAL_LLM_ENGINEER` Executor on 2026-09-16 ("อ่าน .md แล้วดำเนินการ Task-058"), clearing the prior `NO_ELIGIBLE_EXECUTOR` fail-closed state for this exact repository/workspace/task envelope. Phase 0 complete; execution proceeds through Tasks 4–10 of the implementation plan. Independent verification (Task 8) remains a separate `INDEPENDENT_ENGINEERING_VERIFIER / VERIFY` selection and is not self-satisfied by the Executor.
- **Execution Progress (2026-09-16):** Phase 0A local self-host 1.19 candidate (16 successors + MIG-005 + Bootstrap, stamp `260916-1332`); Phase 0B INTEGRATION_GATE fast-forward `f819920..5b08c5c`, fresh canonical readback 16/16 stamps 1.19.0, MIG-005 COMPLETED / PERSISTED / NOT_PENDING terminalized at `aaddc23760fd1c9657a350fe0c8eebba7da0ef19`; isolated implementation worktree `task058-wave-a-v2` from canonical `aaddc23`; Task 4 RED pressure scenarios `557–590` (34 classes, one-to-one with spec §19) appended; cumulative suite `1–590` contiguous/unique; RED structural verifier run recorded (Wave A V2 production-contract assertions FAIL as expected before normative mutation). Task 4 GREEN: Wave A V2 amendment (`references/framework-governance-amendment-260916-task058-wave-a-v2-deterministic-execution-foundation.md`) + Core projection + SKILL guidance (structural 30/30). Task 5 GREEN: 7 single-responsibility starters + V2 shapes (`contract_version`/`record_version: "2.0"`) with v1 compatibility + adapter/README composition (starters 40/40). Task 6 GREEN: Framework 1.20.0 release identity, 1.19→1.20 migration notes, root README, 22/22 mockup stamps 1.20.0/1.0.0, launcher files byte-unchanged (propagation 44/44). Task 7 GREEN: AFFECTED PASS 47/47 + independent fresh-context review accepted (10/10 mandatory questions PASS; 3 Important + 1 Minor findings fixed in `6bd77ed`; post-fix AFFECTED PASS 47/47). Task 8 GREEN: frozen candidate `63f264076becc7910b8d832db61280d064f0fb11` (tree `ee11987864683f1263eb4fd30803c354054707bb`, Framework-Source tree `28b4003cf620f3cb553a1afea4a2b0063e47e845`), exactly one final RELEASE_FULL on the unchanged candidate: `RELEASE_FULL PASS 55/55` = `PASS_RUN_1`; release evidence committed at `b5d983c0cb526d9889a30b6b9427bf2b5b1bce83` (`docs/superpowers/evidence/2026-09-16-task-058-wave-a-v2-deterministic-execution-foundation-release-full.md`).
- **Completion Facts (2026-09-16, fresh local readback):** written spec user-approved; plan executed (Tasks 1–10); Phase 0 canonical self-host 1.19 prerequisite verified (MIG-005 terminal); scenarios 557–590 implemented and GREEN (cumulative 1–590 contiguous/unique); normative/starter/propagation contracts complete; AFFECTED PASS 47/47; independent review accepted (no unresolved Critical/Important finding); one final unchanged-candidate RELEASE_FULL PASS_RUN_1 (55/55); evidence committed; completion commit observed; working tree clean; no unauthorized publication.
- **Publication Dimensions (truthful):** `NOT_PUSHED / NOT_MERGED / NOT_TAGGED / NOT_RELEASED / NOT_DEPLOYED` — local Framework 1.20 candidate only, on local branch `task058-wave-a-v2` in worktree `.worktrees/task058-wave-a-v2`.
- **Completion Criteria Met:** all local completion requirements in the implementation plan Task 10 Step 2 are satisfied and read back; TASK-058 is `DONE` locally. Publication (push/PR/merge/tag/GitHub Release) and canonical post-1.20 self-host promotion remain separately governed: if Framework 1.20 is later integrated to canonical `main`, a fresh post-merge 1.20 self-host reconciliation is required under separate valid Root/shared-state authority.
- **Exact Next Step:** none for TASK-058 local scope. Separately governed follow-ups only: (a) publication decision for the Framework 1.20 candidate (push/PR/merge/tag/Release); (b) post-merge canonical 1.20 self-host reconciliation if integrated; (c) Wave B/C design work remains excluded from this Task.
