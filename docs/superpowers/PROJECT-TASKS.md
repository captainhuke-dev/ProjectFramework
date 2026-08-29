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
- **Status:** `TODO`
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
- **Implementation boundary:** Task registration only. Do not modify Framework semantics, root/template files, launchers, schema, runtime, MCP behavior, or existing Projects until a separate design spec is completed and explicitly approved.
- **Design State:** `APPROVED_DIRECTION / DESIGN_SPEC_REQUIRED`
- **Target Release:** `TBD_BY_DESIGN` (architectural change; do not pre-assign release version before design review)
- **Completion criteria:** User-approved design defines bootstrap file schema, authority boundary, discovery/read algorithm, vendor adapter rules, GREENFIELD behavior, Brownfield upgrade/migration behavior, failure handling, affected Framework surfaces, and verification strategy before any implementation begins.
- **Exact Next Step:** Prepare the TASK-023 architectural design spec for `PROJECT-BOOTSTRAP.md`; do not implement until the written spec is reviewed and explicitly approved.

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
- **Target Release:** `TBD_BY_DESIGN`
- **Completion criteria:** A user-approved design defines command syntax, council input/context boundary, verified llm-council integration contract, advisory-authority separation, result structure, failure/partial-response behavior, persistence/evidence rules, affected Framework surfaces, and verification strategy before implementation begins.
- **Exact Next Step:** Wait for further requirements; when TASK-024 is selected for development, inspect the referenced llm-council repository directly and prepare its architectural design spec before implementation.
