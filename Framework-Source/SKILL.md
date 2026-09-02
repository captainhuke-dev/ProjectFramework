---
name: managing-project-source
description: Use when creating, adopting, importing, updating, reviewing, handing off, or exporting a Project Source; when a project needs consistent governance, naming, source-of-truth handling, continuation context, project-management control, or technical/install documentation.
---

# Managing Project Source

## Overview

Maintain a consistent `Project-Source/` governance layer. Make **current truth, current authority, Project health, and exact next action** explicit without inventing facts.

Current distribution: **Framework 1.10.0 / Schema 1.0.0**.

ProjectFramework is **conceptual governance/planning first**. Technical and integrity requirements are semantic contracts. **Do not expand Tech Stack, installation, Docker, governance, or integrity work into application code, Dockerfile/Compose, scripts, validator/CLI, CI/CD, scheduler, background automation, or other implementation unless the user explicitly requests a separate implementation scope.**

## Required References

Before creating or materially changing Project Source, read (each entry notes what it is for):

- `FRAMEWORK-RELEASE.yaml` — release identity and bootstrap policy
- `references/framework-governance-amendment-260901-task025.md` — latest amendment: Project Knowledge Layer / Compounding Knowledge Contract (current authority)
- `references/framework-governance-amendment-260831-task041.md` — previous amendment: Portable Installation Bootstrap & Project Settings Handoff (current authority)
- `references/framework-governance-amendment-260831-task040.md` — previous amendment: canonical `[Session]` command rename
- `references/framework-governance-amendment-260830-task026.md` — previous amendment: External AI Context & Disclosure Governance
- `references/framework-governance-amendment-260829-task024.md` — previous amendment: `[Meeting]` LLM Council Advisory Command
- `references/framework-governance-amendment-260829-task039.md` — previous amendment: Persistent `[Goal]` Continuous Execution Command
- `references/framework-governance-amendment-260829-task038.md` — previous amendment: Framework Source Distribution-Root Migration
- `references/framework-governance-amendment-260829-task023.md` — previous amendment: Self-Bootstrapping Project Contract
- `references/framework-governance-amendment-260828-task022.md` — previous amendment: Federated Project Graph + OpenViking relation governance
- `references/framework-governance-amendment-260825-task021.md` — previous amendment: ChatGPT→MCP Continuity
- `references/framework-governance-amendment-260823-1439.md` — Direct-to-Latest upgrade semantics
- `references/framework-governance-amendment-260823-0816.md` — Framework 1.3.0 command contract
- `references/framework-governance-amendment-260822-1835.md` — bootstrap location and file storage
- `references/framework-governance-amendment-260822-1424.md` — local workspace binding and checkpoints
- `references/framework-governance-amendment-260821-1934.md` — workspace/runtime authority
- `references/framework-governance-amendment-260821-1505.md` (historical approved amendment)
- `references/framework-governance-amendment-260821-1254.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-1142.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-1024.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0821.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0735.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0707.md` (historical approved amendment)
- `references/framework-governance-amendment-260820-0646.md` (historical approved amendment)
- `references/framework-governance-amendment-260814-0808.md` (historical approved amendment)
- `references/core-governance-rules.md` — the full normative rulebook (deepest authority below amendments)
- `MIGRATION-NOTES.md` — per-release upgrade guidance (routing aid, not normative authority)
- `templates/PROJECT-BOOTSTRAP.md` — maintained Project-root discovery template for Framework `1.7.0+` GREENFIELD/adoption
- `templates/project-location-bootstrap.md` — pre-authority environment/location locator template; distinct from Project-root bootstrap
- `templates/00-project-source-framework.md` — root template for document `00`
- `templates/core-document-skeletons.md` — skeletons for mandatory documents
- `templates/project-source-mockup/README.md` — starter tree overview
- `templates/upgrade-preview.md` — standard structure for upgrade preparation Previews

Historical spec/design files are rationale only. Latest Framework amendment wins on conflict.

## Project Bootstrap Entrypoints

Framework `1.7.0+` NEW Projects use stable `<Project-Root>/PROJECT-BOOTSTRAP.md` as the vendor-neutral discovery entrypoint. The Framework template is `templates/PROJECT-BOOTSTRAP.md`; it routes `PROJECT-BOOTSTRAP.md → 00 → 01 → 03`, then task-specific sources, and `09` when continuation applies. It is a locator only; valid active `FRAMEWORK-001` remains authority.

Existing initialized Projects do not acquire the file automatically. Brownfield adoption is through governed `[Project Upgrade]`. Optional `PROJECT-CONFIG.md` remains a Bootstrap Location reference only.

Official platform adapters are:

- `CHATGPT-PROJECT-INSTRUCTIONS.md`
- `CLAUDE-PROJECT-INSTRUCTIONS.md`

Once Project-root access exists, platform Project Settings plus `AGENTS.md` / `CLAUDE.md` are optional thin discovery adapters. The official launchers retain legacy/pre-1.7 discovery compatibility. Text between `PROJECTFRAMEWORK-SHARED-CONTRACT:START` and `PROJECTFRAMEWORK-SHARED-CONTRACT:END` MUST remain byte-identical. Each complete launcher stays `<=4,500` Unicode characters; canonical tokens, registered commands, lifecycle values, report labels, response-close fields, and marker identity must never be renamed or dropped. Launchers never outrank Root Governance.

If active local `FRAMEWORK-001` exists, local pinned Project Source is authoritative. NEW Project Framework bootstrap begins from canonical repository `main`, and the approved resulting `1.7.0+` Project materializes the root bootstrap. Exact Git tag/SHA and branch protection remain optional assurance.

## Framework 1.2.4 Project Location Binding

For initialized Projects, active local `FRAMEWORK-001` is the canonical home of **Project Location Binding**. Resolve it before Material GitHub/Google Drive work. The binding answers **where Project work belongs**; Authority/Risk rules independently answer **who may mutate what**.

Keep these concepts distinct:

```text
Repository Location Binding
  ≠ current work branch/worktree
  ≠ Canonical Integration Target
  ≠ Canonical Implementation Source
```

Do not add or infer `canonical_branch` from Location Binding. Framework `1.2.2` Canonical Integration Target/Base Freshness and Framework `1.2.3` Canonical Implementation Source/Runtime Authority remain independently authoritative.

GitHub and Drive each resolve to exactly one state:

```text
BOUND
NOT_APPLICABLE
VERIFICATION_REQUIRED
```

Operational rules:

1. `BOUND` requires durable routing identity: GitHub owner/repository or canonical repository URL; Drive project-root folder ID or canonical folder URL. Display names, Drive text paths, recent activity, chat memory, ranking, and discovery hits do not establish authority by themselves.
2. `BOUND` → compare the intended Material target to the durable routing identity when possible; a material mismatch stops the affected mutation and is surfaced.
3. `VERIFICATION_REQUIRED` → discovery/read/search and candidate comparison may continue; Material mutation is blocked by default.
4. A User Explicit Instruction naming one exact target may authorize that one otherwise-permitted action; it does not persistently rewrite Root Governance or promote the binding to `BOUND`.
5. `NOT_APPLICABLE` → no Material Project work through that connector until an explicitly approved binding/scope revision.
6. Persistent binding change → User Explicit Approval + governed `FRAMEWORK-001` revision/validate/promote/supersede/archive flow. Connector discovery, recent activity, or search ranking never transfers Project authority.
7. `03`/`09` may reference the active root binding; they do not keep independent authoritative repository/folder copies.
8. Project-specific repository/Drive/progress pointers belong in local `FRAMEWORK-001`, not platform launchers.

GREENFIELD has no active local binding. Use read-only candidate discovery as needed → include proposed GitHub/Drive states and durable identities in Preview → obtain explicit approval → first Material Project-Source write creates active `00 / FRAMEWORK-001` with the approved binding → subsequent Material connector work resolves that active binding. Unresolved applicable systems remain `VERIFICATION_REQUIRED` and fail-closed for Material mutation.

## Framework 1.2.5 Agent Continuity, Progressive Verification, and Local Workspace Binding

Framework `1.2.5` composes with `1.2.1–1.2.4` and adds no new slot, Stable-ID family, lifecycle state, Git freshness state, or authority family.

### Local Workspace Binding

Before Material local/MCP work, resolve the applicable environment-scoped **Local Workspace Binding** from active `FRAMEWORK-001`. Reuse exactly `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED`. `BOUND` requires a verified/user-confirmed absolute path for that environment; for Git-backed work, cross-check repository identity when practical. `VERIFICATION_REQUIRED` allows read/list/search/inspect needed to resolve the workspace but blocks Material mutation by default. `NOT_APPLICABLE` blocks Material local scope. MCP `workspaceId`, editor handles, active/recent workspace lists, and similar tool identifiers are routing evidence only, not canonical Project identity.

Keep the separation explicit:

```text
Repository Location Binding
  ≠ Local Workspace Binding
  ≠ current branch/worktree
  ≠ Canonical Integration Target
  ≠ Canonical Implementation Source
  ≠ Runtime Location
```

A one-off exact local target instruction is action-specific and does not persistently rewrite Root Governance. Persistent Local Workspace Binding changes require User Explicit Approval plus `FRAMEWORK-001` revision/validate/promote/supersede/archive.

### Verified Task Completion Checkpoint

For a Material Task / `ACT-*` that materially mutates a Git-backed Canonical Implementation Source or another authoritative repository artifact, durable `DONE` requires a **Verified Task Completion Checkpoint**: affected/risk-appropriate verification passed; required completed state is represented by observed Git commit(s); no required completed result remains only uncommitted; remaining working-tree state is understood. Read-only/no-mutation Tasks require no synthetic commit. `WIP commit ≠ Task DONE`. One Task may use multiple commits. **commit ≠ push**; remote publication remains a separate shared-state/authority action.

### Progressive Verification and Evidence Reuse

Choose the minimum sufficient verification from changed scope → affected dependencies/invariants → `R0 / R1 / R2 / R3` risk. Operational labels are:

```text
TASK_LOCAL_FAST
CHECKPOINT_INTEGRITY
RELEASE_FULL
INTEGRATION_GATE
```

These are workflow vocabulary only. `TASK_LOCAL_FAST` verifies affected scope before Task completion. `CHECKPOINT_INTEGRITY` verifies durable continuation; **Logical Checkpoint ≠ RELEASE_FULL**. `RELEASE_FULL` runs once on the completed release/candidate state. `INTEGRATION_GATE` re-resolves Canonical Integration Target/Base Freshness and prior evidence validity. Fresh state-bound evidence may be reused while candidate/dependency/target assumptions remain materially unchanged; selectively invalidate affected evidence when assumptions change, and escalate when impact cannot be bounded safely. Exact fast-forward to an already verified candidate normally needs resulting-state confirmation rather than an unconditional full rerun.

### Response Close Completeness Gate

Before every Framework-governed assistant response emit, run the lightweight **Response Close Completeness Gate** on the assistant final-response representation: two mandatory headings exactly once and in order; exactly one visible semantic `[Next Action]:`, `[Chat]:`, `[Reason]:`, `[Required Read]:` field as separate Markdown paragraphs in that order; lifecycle-consistent `[Chat]`; and nothing after `[Required Read]`. For Markdown output, render the labels safely, e.g. `**[Chat]:** CONTINUE_CURRENT_CHAT`, so a bare reference-definition-like line cannot disappear. Bold/wrapping is presentation-only; semantic labels and canonical lifecycle tokens remain unchanged. Missing/duplicate/malformed/hidden/out-of-order/contradictory close content is incomplete and must be corrected before emit. Do not claim visibility into downstream app rendering; a user-visible omission is regression evidence while its generation/transport/rendering layer remains unverified unless independently observed.


## Framework 1.9.0 Portable Installation Bootstrap & Project Settings Handoff

The target Project Settings / Project Instructions adapter is a **thin discovery wrapper**. Its canonical copy-ready form is:

```text
ProjectFramework Upstream: https://github.com/captainhuke-dev/ProjectFramework
Project Bootstrap: <VERIFIED_ABSOLUTE_PROJECT_BOOTSTRAP_PATH>

ProjectFramework Bootstrap Rule:
Read Project Bootstrap before Material Project work.
If Project Bootstrap cannot be resolved, use the Project README managed bootstrap block as fallback.
ProjectFramework Upstream is for Framework discovery/upgrade only; it never replaces local Project Source authority.
```

`ProjectFramework Upstream` is fixed Framework read-through/upgrade source only. `Project Bootstrap` is the verified absolute environment-specific path to the consuming Project's root `PROJECT-BOOTSTRAP.md`. Never emit an unresolved/guessed path as ready to paste.

A Framework `1.9.0` GREENFIELD resulting Project has exactly one valid root README managed fallback block using markers `<!-- PROJECTFRAMEWORK-BOOTSTRAP:START -->` / `<!-- PROJECTFRAMEWORK-BOOTSTRAP:END -->` and relative `./PROJECT-BOOTSTRAP.md`. Create README when absent; append/update only the managed body when exactly one valid block exists; duplicate/malformed markers fail closed to repair. Content outside markers is Project-owned and is not rewritten merely for bootstrap maintenance.

Bootstrap resolution is Project Settings → root README managed fallback when Settings are unusable → `PROJECT-BOOTSTRAP.md` → active `00 / FRAMEWORK-001` → `01 → 03`, with `09` for continuation. Project Settings, README, upstream, and root bootstrap remain locator/discovery surfaces; active local `FRAMEWORK-001` remains Project governance authority.

GREENFIELD install flow is canonical upstream read-through → environment discovery → one Preview → explicit approval → active `00` first → mandatory Project Source → applicable conditionals → root bootstrap + README fallback → verify → **Core Installation DONE** → mandatory `Project Settings — Required User Handoff`. Core completion does not depend on later external vendor copy/paste confirmation, and no `PROJECT_SETTINGS_*` lifecycle family is created.

The thin user-facing adapter does not remove internal `framework_source`, `remote_location`, `file_storage_locations`, `mcp_location`, `local_workspace`, dynamic branch/worktree, Project Location Binding, or `[Project Path]` semantics. Existing initialized Projects remain pinned and adopt this contract only through governed `[Project Upgrade]`.

Framework installation never synthesizes Goal/Auth/ENV/Meeting/disclosure/secret-value/runtime state merely for convenience and never claims vendor settings were mutated without observation.

## Framework 1.10.0 Project Knowledge Layer

Framework `1.10.0` adds optional root-level `Project-Knowledge/` only when materially useful and approved. Resolve active Project authority first; Knowledge is advisory/derived and never replaces Project Source.

```text
Project Knowledge ≠ Project Authority
Derived synthesis ≠ Evidence ≠ Governed Project truth
```

Maintained Project Knowledge uses `README.md`, `index.md`, append-only `log.md`, and pages under `pages/`. Page frontmatter includes `knowledge_page_id`, `knowledge_state`, `source_refs`, `related_project_source_refs`, `related_knowledge`, and `review_trigger`. Exact maintenance states are `CURRENT | REVIEW_DUE | STALE | CONTRADICTED | SUPERSEDED | RETIRED`; state is maintenance status, not claim truth certainty.

Material synthesis requires source provenance. Raw/source material remains source-native by default. `index.md` is navigation, not ranking authority. `log.md` records bounded material `ingest | query-file | lint | maintain` operations and never becomes a raw MCP/tool transcript or private reasoning store.

Knowledge operations:

```text
ingest     → source/provenance → page/link/index/log maintenance
query-file → file reusable synthesis with the same provenance/index/log contract
lint       → advisory maintenance findings only
```

Knowledge→Governance promotion always resolves the existing canonical Project Source home, verifies evidence, obtains applicable authority, mutates only that owner through normal governed flow, then links the governed result back to Knowledge. No automatic promotion is permitted.

Integration boundaries:

- `[Meeting]` output remains advisory and needs provenance/limitations before Knowledge filing.
- `EVD-*` remains evidence; Knowledge remains reusable synthesis.
- TASK-026 disclosure applies independently before external model/provider use of Knowledge.
- `03` / `09` carry pointers only when Knowledge is material to current work.
- Knowledge cross-links are not `REL-*`; Project Graph remains canonical in `92`.
- OpenViking keeps `PROJECT_SOURCE_AUTHORITY` separate from `PROJECT_KNOWLEDGE_ADVISORY`, remains `DERIVED_ONLY` and rebuildable, and never promotes content by retrieval rank/similarity/recency/centrality.

GREENFIELD Project Knowledge is optional/applicability-driven; Brownfield adoption is governed and never automatic. Actual secret values remain forbidden. This Framework contract creates no wiki engine, vector database, UI, watcher, crawler, auto-ingest daemon, embedding pipeline, MCP wiki service, validator/CLI, scheduler, or runtime automation.

## Framework 1.3.1 Registered Project Commands

Registered Project command identity requires literal brackets; matching inside brackets is case-insensitive. Canonical display forms are:

```text
[Project Status] : fresh Project/Task/Git/verification/blocker dashboard
[Project Path]   : show/verify configured bootstrap paths and route explicit path-change requests through existing governance
[Project Upgrade] : fresh-compare the active Project Framework with canonical upstream and offer governed upgrade preparation when they differ
[Goal] : create/show/change/cancel a persistent outcome and its bounded continuous-execution authorization
[Meeting] : convene a multi-model advisory council for a question using minimum authorized context; results are evidence/advice, never Project authority
[Session] : declare, show, or close the user-pre-approved scope of operations for the current session/task
```

Natural-language command-help requests list only commands registered by the active Framework/Project as `[XXX] : purpose`; do not invent commands.

`[Project Status]` is read-only and fresh-observation driven. Report applicable dimensions in order: Identity → Health → Remain Tasks → Git Sync → Working Tree → Verification → Blockers. Health reuses `GREEN | AMBER | RED | UNKNOWN`. Read Task count from the Task source; never infer Tasks from changed-file count. Working Tree reports Waiting Commit Yes/No plus changed/staged/unstaged/untracked counts. A verified remote-sync claim requires fresh remote evidence; unavailable dimensions stay `UNKNOWN / VERIFICATION_REQUIRED`.

`[Project Path]` surfaces Framework Remote Path, Git Remote Path, Storage Path, MCP Path, and Workspace Path. Angle-bracket placeholders such as `<STORAGE>` or `<WS>` mean unset/not configured and are never literal paths or permission to infer fallback locations. An explicit requested path may be used as action input, but persistent Bootstrap/Project Location changes retain existing approval and `FRAMEWORK-001` revision/validation/promotion/history rules.

`[Project Upgrade]` is read-only through comparison. For an initialized Project, current Framework identity comes from the valid active local `FRAMEWORK-001` pin; canonical upstream is a freshly observed target candidate, never silent replacement authority. Compare Framework/Schema plus observable source identity/freshness and report `UP_TO_DATE | UPGRADE_AVAILABLE | SOURCE_DIVERGENCE | VERIFICATION_REQUIRED` as presentation-only labels. Equal version strings do not override material source divergence, and unresolved evidence fails closed. When `UPGRADE_AVAILABLE`, ask whether the user wants to **prepare** an upgrade. A positive answer starts cumulative current→target assessment/Preview only; mutation still requires separate explicit approval after `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED` classification, preservation/rollback planning, affected verification, one final `RELEASE_FULL`, and governed promotion/history preservation. The command adds no path/binding, branch, implementation-source, runtime, or persistent-state authority.
## Framework 1.8.0 Persistent `[Goal]` Command

`[Goal]` is persistent across chats and composes existing Project Source homes rather than creating a `GOAL-*` family: `OUT-*` in `91` is the desired outcome/success evidence; `AUTH-*` in `12` is durable Goal authority; `ACT-* / ENV-*` in `15` are execution; `03` summarizes current status; `09` stores pointers only with `authority_transfer: false`.

Goal `OUT-*` status is `ACTIVE | BLOCKED | ACHIEVED | CANCELLED | SUPERSEDED`. `ACT DONE ≠ OUT ACHIEVED`: evaluate all explicit success criteria/evidence separately before `ACHIEVED`. Cancellation/revocation/supersession stops future Goal-authorized work while preserving completed history.

Unless explicitly narrowed, persistent Goal authority includes the normal bounded local development workflow: local read/inspect/research → design/architecture → plan → non-destructive in-scope edits/moves → tests/lint/typecheck/build/validation → debug/fix → local Git add/commit → Logical Checkpoints and required continuation/evidence updates. Do not ask again solely for Framework-level approval when the exact operation is already covered by current valid Goal `AUTH-*`.

Opt-in boundaries remain exact:

```text
push/publication       → explicit Goal publish/push intent + governed target + fresh integration/evidence preflight
destructive operation  → explicit operation + target/conditions only
Root/Binding mutation  → explicit mutation + target; normal Root revision/validate/promote/archive/sync/verify lifecycle remains mandatory
external disclosure    → separate disclosure authorization; Goal authority does not imply outbound AI/provider disclosure
```

Never store/reveal actual secret values; use `SECRET-*` references when otherwise authorized. `ENV-*` may be derived/refreshed without new approval only when equal to or narrower than valid parent Goal `AUTH-*`; it never expands authority.

Goal execution/resume order:

```text
[Goal] invocation → resolve CREATE/SHOW/CHANGE/CANCEL intent
→ materialize/resolve Goal OUT-* + Goal AUTH-*
→ derive ACT-* / bounded ENV-*
→ persist 03/09 pointers when material
→ fresh chat: PROJECT-BOOTSTRAP → 00 → 01 → 03 → 09 → OUT/AUTH/ACT/ENV
→ fresh-check mutable prerequisites/bindings/evidence
→ continue exact safe next action without redundant Framework approval
→ evaluate OUT success criteria separately from ACT completion
```

Block only an unauthorized/blocked action when independent safe Goal work remains; use Goal `BLOCKED` only for a global blocker. Goals never silently rewrite `REQ-*`/`DEC-*`/accepted Risk/architecture to make completion easier and never resolve conflicts by recency. System/developer/product/MCP/tool/authentication controls remain higher-level gates and cannot be waived by `[Goal]`.
## Framework 1.8.0 `[Meeting]` Advisory Council Command

`[Meeting]` sends the explicit bracketed question as the default outbound payload to a verified Meeting-capable advisory provider. Extra Project context is added only when materially relevant, minimum necessary, and covered by applicable disclosure authority; actual secret values are never sent or persisted merely because they are relevant. `[Goal]`/`ENV-*` execution authority does not imply outbound disclosure authority.

Current TASK-024 provider profile evidence is `captainhuke-dev/llm-council` at observed `master` commit `92e1fccb1bdcf1bab7221aa9ed90f9dc72529131` / tree `221d8afb6eca87537282d509971c505119390e0b`, with FastAPI/OpenRouter Stage 1 independent responses → Stage 2 anonymized peer ranking → Stage 3 Chairman synthesis. Provider profile/version/availability is fresh evidence, not Project authority or a permanent Framework invariant.

Operational flow:

```text
[Meeting] invocation
→ resolve bracketed command + explicit question
→ identify any additional Project context needed
→ minimize + verify disclosure authority + remove secret values
→ fresh-resolve provider profile/availability when material
→ execute available council stages through runtime capability
→ normalize COMPLETE/PARTIAL/FAILED/UNAVAILABLE
→ preserve independent views/agreement/disagreement/peer signal/synthesis/limitations
→ present advisory result
→ persist EVD-* only when materially used by governed Project truth
→ route any adopted recommendation through its normal owning governance
```

Council/majority/Chairman output is advisory only: it is not User Approval, `AUTH-*`, `DEC-*`, `REQ-*` change, Risk acceptance, or mutation permission. Missing Stage 2 leaves ranking incomplete; Chairman failure returns available material with `SYNTHESIS_UNAVAILABLE` rather than fabricated consensus; provider/auth/network failures remain provider failures. TASK-024 creates no `MEETING-*` family/slot and never treats provider `data/conversations/*.json` as Project history.

## Framework 1.8.0 External AI Context & Disclosure Governance

TASK-026 composes existing `AUTH-*`, `EVD-*`, and `SECRET-*` homes. It creates no `DISC-*` family/slot. Canonical disclosure classes: `EXTERNAL_OK | EXTERNAL_REVIEW | DO_NOT_DISCLOSE | UNCLASSIFIED`. Provider/tool eligibility: `ELIGIBLE | LIMITED | INELIGIBLE | VERIFICATION_REQUIRED`.

`Classification ≠ Authorization`; `Provider Eligibility ≠ Authority`; `Disclosure Permission ≠ Decision Authority ≠ Mutation Authority ≠ Binding Authority ≠ Runtime Authority`; `Secret Reference ≠ Secret Value Disclosure Permission`; `Unknown ≠ Safe`. `UNCLASSIFIED` and materially unresolved provider eligibility fail closed for protected outbound context. Actual secret values remain excluded.

Standing disclosure permission reuses provider/purpose/content-scoped `AUTH-*`; an exact User Explicit Instruction may authorize only one sufficiently bounded disclosure action without becoming standing authority. Availability, model capability, Tool/MCP/repository access, Goal/ENV execution authority, Meeting invocation, Project Knowledge advisory status, or OpenViking relation visibility never imply disclosure authority.

Outbound flow:

```text
external-AI consumer requests context
→ identify purpose + provider/tool
→ identify candidate sources
→ classify each portion
→ remove secrets / DO_NOT_DISCLOSE
→ minimize + sufficiently redact/generalize
→ resolve provider eligibility
→ resolve AUTH-* or exact one-off basis
→ partition mixed sensitivity
→ send authorized eligible subset only
→ surface blocked/omitted portions when material
→ persist EVD-* only when governance-relevant
```

Redaction uncertainty fails closed; whole-Project/repository disclosure is exceptional exact scope. Material `EVD-*` records reconstruct the boundary without duplicating sensitive payload. GREENFIELD creates no blanket grant/classification/provider/runtime; Brownfield does not retroactively classify content safe or synthesize disclosure authority. No runtime redactor/router/proxy/gateway/DLP/secret manager is implied.

## Framework 1.2.6 Bootstrap Location Semantics and File Storage Binding

Framework `1.2.6` composes with `1.2.1–1.2.5`. It adds deterministic pre-`FRAMEWORK-001` bootstrap locators and generalized governed non-Drive File Storage without creating a second Project authority.

When Project-specific Bootstrap Location configuration is present, use this order:

```text
valid active local FRAMEWORK-001 already resolved? → local pin remains authoritative
otherwise read Bootstrap Location Block
→ Framework Source = Framework read-through only
→ declared Local Workspace = first read-only attempt to resolve local Project/active FRAMEWORK-001
→ Remote Location = deterministic remote Project Source discovery start when local authority does not resolve
→ MCP Location = verify intended execution adapter/boundary for the current environment
→ File Storage Location(s) = bootstrap locators for declared non-repository artifact scopes
→ current branch/worktree = fresh Git observation; never trust static text as current state
→ once FRAMEWORK-001 resolves, its Project Location Binding governs steady-state routing
→ then apply Scope / AUTH / DEL / Risk / REQ / DEC / Git integration / implementation / runtime gates
```

Keep these meanings distinct even when values align:

```text
Framework Source
≠ Remote Location
≠ File Storage Location
≠ MCP Location
≠ Local Workspace
≠ current branch/worktree
≠ Repository Location Binding
≠ File Storage Binding
≠ Local Workspace Binding
≠ Canonical Integration Target
≠ Canonical Implementation Source
≠ Runtime Location
```

Operational rules:

1. Bootstrap locators help find/route authority; they never silently become authority. A valid active local `FRAMEWORK-001` wins for initialized Project Location state.
2. Remote Location may be an explicit discovery/index indirection; string inequality with final governed repository is not automatic DRIFT. A direct contradictory identity that would route Material work elsewhere stops the affected mutation and is surfaced.
3. MCP Location and Local Workspace may use different host/container/mount syntax when an explicit verified mapping proves the same governed Project/source identity. MCP `workspaceId`, editor handles, focus/recent lists, and local mount letters remain evidence only.
4. Bootstrap/Root mismatch is fail-closed for the affected Material mutation. Do not silently rewrite either layer.
5. `current branch/worktree` is `DYNAMIC / VERIFY_EACH_SESSION`: fresh-observe repository identity, worktree, branch/ref, HEAD, status, and tracking state when material. Never persist a concrete current branch as bootstrap authority or infer Canonical Integration Target from it.
6. Generic **File Storage Binding** lives under active local `FRAMEWORK-001` Project Location Binding for non-Google-Drive external scopes. Supported descriptive provider vocabulary may include `S3 | NAS | SMB | NFS | SHAREPOINT | OBJECT_STORAGE | FILE_SERVER | FILESYSTEM | OTHER`.
7. Google Drive remains governed by the dedicated `project_location_binding.google_drive` block in Framework `1.2.6`. A bootstrap `GOOGLE_DRIVE` locator maps there. Never duplicate the same Drive target/content scope in generic `file_storage_locations`.
8. File Storage binding states are exactly `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED`; verification is exactly `VERIFIED | USER_CONFIRMED | VERIFICATION_REQUIRED`. `BOUND` pairs only with `VERIFIED` or `USER_CONFIRMED` and requires provider-appropriate durable identity.
9. Known-applicable unresolved storage = `VERIFICATION_REQUIRED`; discovery/read-only resolution may proceed, Material mutation does not. A Project with no external storage may omit generic entries entirely; do not synthesize provider `NOT_APPLICABLE` rows. Missing/unresolved storage never authorizes recent/search-ranked fallback.
10. Multiple storage locations are allowed for distinct content scopes; one governed content scope has one declared authoritative owner at a time. Mirrors, backups, archives, mounts, sync/cache paths, or copies do not gain current authority by accessibility or recency.
11. File Storage Binding does not automatically become Local Workspace, Canonical Implementation Source, Runtime/Data/Persistent-State authority, backup authority, or deployment authority. The same physical target may serve multiple roles only when each role is independently declared. Source-code presence alone does not grant IMPLEMENTATION Truth.
12. Never store storage credentials in location metadata. Use existing `SECRET-*` external-reference metadata; no actual access keys, passwords, tokens, SAS tokens, or secret-bearing signed URLs.
13. Correct location never grants `AUTH-*`, `DEL-*`, Risk approval, scope expansion, branch/integration authority, implementation authority, or runtime authority.
14. One-off exact targets remain action-specific. Persistent bootstrap/governed location change requires explicit approval and coordinated propagation; active `FRAMEWORK-001` binding changes use normal Root Governance revision/validate/promote/supersede/archive flow.
15. Existing initialized Projects remain pinned and do not auto-upgrade to 1.2.6. Migration invents no provider applicability, identities, paths, mappings, branch state, roles, or verification status.

No new semantic slot, Stable-ID family, lifecycle/freshness/Epistemic state, authority family, executable selector, storage sync, validator, hook, bot, CI/CD, scheduler, watcher, credential mechanism, or runtime enforcement is introduced.

## Framework 1.6.0 Federated Project Graph

Framework `1.6.0` standardizes conditional `92 Project Graph` and current `REL-*` relation assertions while keeping Schema `1.0.0` and release format `3`.

Current extended routing is:

```text
40 Technical Design               CONDITIONAL
60 Deployment Plan                CONDITIONAL
90 General / Special Governance Extension anchor
91 Project Management Control     CONDITIONAL / STANDARD IN 1.2.0+
92 Project Graph                  CONDITIONAL / STANDARD IN 1.6.0+
93–99 Project-specific / Governance Extension
```

`92` is the canonical home of `REL-*`. It does not duplicate authoritative payloads owned by `DEP-*` in `91`, `DEC-*` in `04`, `REQ-*` in `05`, `ISS-* / DRIFT-* / CONFLICT-*` in `08`, or existing identity/lineage semantics.

Relation endpoints use immutable `project_uuid`. Core relation types are exactly `PARENT_OF | CHILD_OF | PEER_OF | DEPENDS_ON | SUPPORTS | RELATED_TO`; namespaced extensions use `X-<PROJECT_OR_DOMAIN_NAMESPACE>:<RELATION_TOKEN>`. Assertion state is exactly `ASSERTED | CORROBORATED | CONFLICTED | RETIRED`. `CORROBORATED` requires verified compatible authoritative assertions; a derived inverse edge or central confidence score is insufficient.

A Project may begin without `92` and bind relations later. `PARENT_OF` / `CHILD_OF` is semantic Project topology and does not imply nested folders, repositories, workspaces, bindings, integration targets, implementation sources, or runtime locations. Merge/split/absorption preserve existing `project_uuid`/lineage rules and reassess relations rather than cloning edges blindly.

AI-ControlTower owns cross-Project indexing/orchestration. OpenViking is `DERIVED_ONLY` and **REBUILDABLE** from current authoritative Project Sources. It may normalize/query/correlate/index and surface stale/orphan/conflicting derived state, but it must never overwrite Project Source, synthesize another Project's authoritative assertion, or become required to reconstruct current relation truth. Reuse existing `DRIFT-*`, `CONFLICT-*`, and `MIG-*`; do not create graph-specific parallel families.

Brownfield Projects pinned before `1.6.0` may already occupy custom slot `92`. Never overwrite it: open/route `MIG-*`, preserve identity/history/references, relocate only through governed approval to a suitable free `93–99` or other semantic slot, then activate standard `92` only when applicable.

This contract adds no OpenViking runtime, graph database, Graphify integration, crawler, watcher, scheduler, sync daemon, validator/CLI, MCP graph service, or automatic conflict resolution.

## Framework 1.2.0 Namespace and Routing — Historical Base

Mandatory core remains `00–05` and `09–17`; `06–08` remain conditional; `18–19` remain reserved.

Framework `1.2.0` standardizes:

```text
40 Technical Design               CONDITIONAL
60 Deployment Plan                CONDITIONAL
90 General / Special Governance Extension anchor
91 Project Management Control     CONDITIONAL / STANDARD IN 1.2.0+
92–99 Project-specific / Governance Extension
```

Current routing on that historical base:

```text
40 → Tech Stack / components / source structure / workspace / config / runtime / Source-Docker technical blueprint
60 → installation / startup-shutdown / verification / diagnostics / runtime-persistence-recreation / upgrade-rollback / backup-restore / cleanup
92 → REL-* current Project-relation assertions when active
91 → RISK-* / ASM-* / MS-* / OUT-* / DEP-* / CR-* / GATE-*
```

Do not create conditional documents merely to make the Project tree look complete.

## Canonical Project-Management Homes

```text
RISK-* → 91 Project Management Control
ASM-*  → 91 Project Management Control
MS-*   → 91 Project Management Control
OUT-*  → 91 Project Management Control
DEP-*  → 91 Project Management Control
CR-*   → 91 Project Management Control
GATE-* → 91 Project Management Control
```

Existing canonical homes remain unchanged for `DEC-*`, `REQ-*`, `ISS-*`, `DRIFT-*`, `CONFLICT-*`, `CHG-*`, actors, authority, evidence, actions, migrations, and secret references.

Key distinctions:

```text
RISK-* future uncertainty ≠ ISS-* materialized/current problem
ACT DONE ≠ MS REACHED ≠ OUT ACHIEVED
DEP AVAILABLE ≠ DEP SATISFIED
CR-* proposed/material change control ≠ CHG-* applied/observed history
Responsibility ≠ Authority
```

Risk materialization preserves the Risk and links an Issue. Accepted material Risk records applicable decision/authority and review trigger.

## Project Health and Review Cadence

`03 Current State` may summarize applicable dimensions:

```text
Scope
Progress / Schedule
Risk
Quality / Validation
Dependencies
Authority
Knowledge
Readiness
Technical / Deployment when applicable
```

Use `GREEN / AMBER / RED / UNKNOWN`, each with Reason, supporting Stable IDs/evidence, Owner, Last Reviewed, Next Review/Trigger. Omit non-applicable optional dimensions rather than marking them GREEN. Do not invent an opaque automatic aggregate score.

Review Cadence modes:

```text
TIME_BASED
EVENT_BASED
```

Cadence may cover Current State, Risk, Assumption, Milestone/Outcome, Decision Revalidation, Technical Design, Deployment Readiness, and Handoff Refresh. Framework semantics do not create a scheduler/reminder runtime.

## Decision Revalidation

`DEC-*` remains canonical in `04`. When material, record:

```text
Validity Basis
Review Trigger
Review By
Last Revalidated
Revalidation Status
Revalidation Evidence
```

Use `NOT_DUE / REVIEW_DUE / REVALIDATED / SUPERSEDED`. Revalidate when the stated basis changes, including invalidated assumptions, changed dependencies/requirements/Tech Stack/deployment mode, approved material Change Request, external change, review date, or contradicting runtime evidence.

## Responsibility and Authority

`11 Actor Registry` may contain scope-keyed `Responsible / Accountable / Consulted / Informed` mapping. It grants no authorization. Actual permission remains in `12 Authorization Registry` through `AUTH-* / DEL-*` plus risk/approval rules.

## Knowledge Debt

Material stale/missing operational knowledge remains canonical in `08 Open Issues`:

```text
ISS-* with issue_type: KNOWLEDGE_DEBT
```

Runtime success does not erase Knowledge Debt. If material it may degrade Knowledge/Readiness and makes `08` applicable if no active `08` exists.

## Technical Blueprint Boundary

### `40 Technical Design`

Use when deeper technical detail is needed beyond `06 Architecture`. Document material Tech Stack entries with Technology, Role/Responsibility, Version/Supported Range, Required/Optional state, reason/Decision reference, component usage, operational dependency, lifecycle/support constraint, replacement boundary, and epistemic/verification state.

May also document component interfaces, source-area responsibilities, **Development Workspace Contract**, Configuration Contract, Runtime Requirements, deployment-mode architecture, and parity/variance.

When material, Development Workspace Contract resolves Canonical Implementation Source, repository/source identity, workspace type/location/durability, Human/Agent edit location, execution environment, Source-to-Runtime Mapping, dependency isolation, Runtime Mutability Boundary, Persistent-State Boundary, and verification/drift notes.

Descriptive workspace/mapping labels such as `LOCAL_WORKSPACE`, `GIT_WORKTREE`, `REMOTE_DURABLE_WORKSPACE`, `DEV_CONTAINER_DURABLE_WORKSPACE`, `DIRECT_EXECUTION`, `BIND_MOUNT`, `WORKSPACE_VOLUME`, `IMAGE_OR_ARTIFACT_BUILD`, and `REMOTE_SYNC` are blueprint vocabulary only; they are not Project states or Stable-ID families.

### `60 Deployment Plan`

Use when install/deployment/operation is in scope. Deployment support vocabulary:

```text
SOURCE_ONLY
DOCKER_ONLY
SOURCE_AND_DOCKER
NOT_APPLICABLE
```

For `SOURCE_AND_DOCKER`, preserve one declared application/configuration/data/security/persistence contract. Intentional differences are explicit Deployment Mode Variance; unexpected mismatch is `DRIFT-*`.

`60` may document prerequisites, Source installation, Docker installation, configuration/secret refs, deployment source/artifact acquisition, Source-to-Runtime Mapping, Runtime Mutability Expectation, Persistent-State Boundary, Data/Storage Authority, Replacement/Recreation Expectation, development/production mapping differences, data initialization, start/stop, health verification, logs, upgrade, rollback, backup/restore, cleanup, troubleshooting. A real Project may include concrete commands/paths only when verified as actual Project truth.

**Planning is not implementation authorization:** a request to define Tech Stack, installation, Docker topology, ports/volumes, workspace mapping, persistence, or verification does not authorize creation of source code, Dockerfile, Compose/Kubernetes/Helm, package manifests, install scripts, CI, or automation.

## Development Workspace and Runtime Authority

Apply this contract when implementation exists and workspace/runtime distinction is material. It composes with, but does not replace, Framework 1.2.2 Git Base Freshness.

Operational sequence:

```text
resolve Canonical Implementation Source / durable workspace
→ if Git branch/worktree integration is in scope, apply existing Base Freshness contract
→ mutate canonical durable source / valid worktree
→ execute/test through declared Source-to-Runtime Mapping
→ compare Implementation Truth with Runtime Truth when material
→ DRIFT-* for mismatch that should align
→ ensure required-survival state has declared persistent authority/mechanism
→ verify resulting Implementation/Runtime state appropriate to risk
```

Required behavior:

1. **Canonical Implementation Source:** identify the durable declared source location whose verified state determines affected `IMPLEMENTATION` Truth. For Git-backed Projects this is normally verified Git/source tree under the Project's repository/workspace contract.
2. **Durability, not host-only:** source must be durable enough for the Project's declared development/recovery lifecycle. Host Git repo, worktree, remote/VM durable workspace, and Dev Container backed by durable bind/workspace storage are all valid when declared. Do not require a physical host folder merely because development is containerized.
3. **Runtime Authority:** fresh runtime observation determines `RUNTIME` Truth only. Editing/running code in an otherwise disposable runtime does not silently transfer Implementation authority.
4. **Runtime-only hotfix:** diagnosis/emergency runtime edits may be observed as runtime state, but canonical implementation completion requires accepted intent to be transferred through the governed change path into Canonical Implementation Source and reverified.
5. **DRIFT reuse:** if canonical implementation and runtime should align but differ materially, use existing `DRIFT-*`; do not invent a workspace/runtime drift family.
6. **Persistence boundary:** state required by REQ/DEC/Technical/Deployment contracts to survive expected runtime replacement must have a declared persistent-state authority/mechanism. Rebuildable cache/temp/scratch state may remain ephemeral when survival is not required.
7. **Production mapping:** production source mounts and image/artifact deployment are evaluated against declared lifecycle, recovery, authority, security, and persistence requirements. Do not blanket-forbid source mounts or universally require immutable images.
8. **Docker optional:** this contract applies equally to native/non-Docker Projects. Do not require Docker merely because software development exists.
9. **Git semantics unchanged:** workspace governance never replaces `FRESH / STALE_NON_SEMANTIC / STALE_SEMANTIC / UNKNOWN`, `BASE_STALE`, `REBASE_REQUIRED`, `FORWARD_PORT_REQUIRED`, `STACKED_WORK`, or the Pre-Merge Base Freshness Gate.

## Materialized Current State Invariant

Every referenced current Stable ID must resolve from Current Reconstructable Snapshot to current authoritative semantics without archive traversal. Archive is Historical Truth only. Delta-only shorthand cannot substitute for current payload.

This applies equally to current `DEC-*`, `REQ-*`, and `RISK/ASM/MS/OUT/DEP/CR/GATE` records. Active `40`, `60`, `91`, or `92` required to interpret current truth belong in `14 Manifest` and `CURRENT` export.

## Migration Safety

Existing Projects never auto-upgrade. Framework `1.3.0` uses **Direct-to-Latest / Cumulative Target-State Upgrade** by default for explicitly approved initialized-Project upgrades: compare the current reconstructable locally pinned Project directly with the selected target Framework and migrate only the affected cumulative semantic delta. Historical amendments/releases remain preserved rationale/history; do not execute each intermediate migration merely because its version existed.

Classify exactly `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`. `FAST_PATH` requires bounded compatible delta; `ASSESSED_PATH` uses one cumulative `MIG-*` assessment/plan; `MAJOR_MIGRATION_REQUIRED` applies when breaking schema/namespace/root semantics, non-reconstructable current truth, or material unresolved conflicts/unknowns prevent safe bounded direct migration. Skipping intermediate execution never skips Preview/approval, compatibility assessment, Stable-ID/current-truth/Project-Specific-Rule/binding/history preservation, rollback, validation, evidence, or promotion. The maintained starter is not the default destructive upgrade path for initialized Projects.

Use affected/risk-scoped verification during migration, `CHECKPOINT_INTEGRITY` at logical checkpoints, one `RELEASE_FULL` on the final unchanged target candidate, and `INTEGRATION_GATE` for current Base Freshness/evidence validity. Do not run full release verification once per skipped historical version.

For Framework `1.2.0` migration:

- if Brownfield slot `91` is already occupied, open `MIG-*`, preserve identity/history/references, relocate only with approval, then activate standard `91` when applicable;
- never automatically convert old prose into new management Stable IDs; promotion requires sufficient current semantics, status, ownership, and evidence/epistemic state;
- preserve local Project-specific rules unless explicitly resolved otherwise.

Framework `1.2.3` migration does not invent workspace topology. Unknown Canonical Implementation Source, workspace durability, Source-to-Runtime Mapping, or persistence boundary remains explicit `UNKNOWN / VERIFICATION_REQUIRED` until verified from actual Project sources/runtime.

## Maintained Starter Representation

`templates/project-source-mockup/` is the **single maintained concrete starter representation** for the current Framework distribution. It covers the governed semantic namespace and current starter surfaces used during GREENFIELD bootstrap.

Do not maintain a second full Project Source example/template tree in the current distribution. Historical composition examples remain available through Git history; current bootstrap and maintenance use Core Governance, the root `00` template, core skeletons, and `templates/project-source-mockup/`.

## MCP Material Persistence and Chat Lifecycle

Connector activity is classified as **Material Project Work** or **Transient MCP Activity**. Chat is temporary interaction/execution state, not canonical Project memory merely because MCP/connectors are available.

Operational sequence:

1. Inspect/read/search as needed; keep intermediate connector detail transient.
2. Classify the outcome as Material Project Work or Transient MCP Activity.
3. If Material, determine the source-native canonical owner.
4. Batch related connector activity until a Logical Checkpoint.
5. Persist current usable state/pointers once at the checkpoint; CHECKPOINT_INTEGRITY verifies continuation state and only affected cross-surface integrity, not full release regression by default.
6. If persistence fails, report `PERSISTENCE_PENDING` and identify what remains unpersisted.
7. Return a compact Chat result; do not replay the connector transcript.
8. Recommend exactly `CONTINUE_CURRENT_CHAT` or `START_NEW_CHAT`.
9. Recommend `START_NEW_CHAT` only after the persistence gate passes: durable current state, pending/blocker state, Exact Next Action, and Required Read location exist outside Chat.
10. If `[Next Action]` is exactly `ไม่มีขั้นตอนถัดไป`, `[Chat]` MUST be `START_NEW_CHAT`.
11. `CONTINUE_CURRENT_CHAT` requires one concrete Next Action and MUST NOT pair with `ไม่มีขั้นตอนถัดไป`.
12. `PERSISTENCE_PENDING` requires `CONTINUE_CURRENT_CHAT` plus one concrete persistence/recovery Next Action; it cannot pair with `START_NEW_CHAT` or `ไม่มีขั้นตอนถัดไป`.
13. `START_NEW_CHAT` may carry a concrete Next Action when state is durably persisted and continuation is safe from Required Read locations.

Mandatory Framework response close (Markdown-safe presentation; semantic labels unchanged):

```text
### ทำอะไรไป?

<concise statement of what was done or determined>

### และถัดไปคืออะไร?

**[Next Action]:** <one exact next action or ไม่มีขั้นตอนถัดไป>

**[Chat]:** CONTINUE_CURRENT_CHAT | START_NEW_CHAT

**[Reason]:** <concise reason>

**[Required Read]:** <canonical locations or ไม่มี>
```

The four semantic fields are separate Markdown paragraphs. Bold/wrapping is presentation-only; canonical labels remain `[Next Action]:`, `[Chat]:`, `[Reason]:`, `[Required Read]:` and lifecycle tokens stay unescaped.

GitHub routing examples:

```text
03 → current state / current phase / current blocker
04 → DEC-* current decision state
05 → REQ-* current requirement state
08 → ISS-* / DRIFT-* / CONFLICT-* / Knowledge Debt
09 → continuation contract and exact next action
10 → applied/observed historical change
13 → material evidence references
15 → ACT-* current action state
92 → REL-* current Project-relation assertions when active
91 → RISK-* / ASM-* / MS-* / OUT-* / DEP-* / CR-* / GATE-*
```

If the natural owner is a normal repository artifact outside Project Source (for example implementation code, README, config, or an approved plan), persist there rather than duplicating the whole state into Project Source. Cross-system GitHub/Drive continuation uses pointers to each source-native owner.

For Google Drive, update the existing designated Project progress `.md` when one already exists. Only when no designated progress Markdown exists and durable continuation state is required, use one stable `PROJECT-PROGRESS.md` as a continuation cache. It references authoritative Drive artifacts and MUST NOT become a duplicate source of truth or MCP transcript.

Do not persist raw tool payloads, long search results, full diffs, repetitive intermediate state, or private intermediate reasoning merely for audit convenience. `09 Handoff` remains a continuation contract, not an execution log. A new chat must be able to continue from persisted state and Required Read pointers without the old transcript.

## Git Base Freshness and Worktree/Branch Integration

Apply this section only when Git branches/worktrees are actually in scope. It operationalizes the binding Core Governance contract; it does not replace it.

Operational sequence:

```text
resolve verified Canonical Integration Target
→ fresh-read/fetch current target
→ classify Independent Work vs STACKED_WORK
→ create work from verified current base
→ check Base Freshness at material checkpoints
→ classify STALE_NON_SEMANTIC vs STALE_SEMANTIC
→ BASE_STALE while unresolved
→ update/rebase appropriately OR FORWARD_PORT_REQUIRED
→ re-resolve target head immediately before acceptance/merge
```

Required behavior:

1. **Independent Work:** create the new branch/worktree from current observed canonical target, not from whichever feature branch is checked out. For ProjectFramework use repository `main` / local `origin/main` semantics. Never assume local `main` is current without a fresh target check.
2. **STACKED_WORK:** feature-on-feature ancestry is allowed only when deliberate and discoverable. Preserve parent branch/ref or commit, dependency reason, what becomes invalid if parent changes, and expected integration order. Material parent movement requires child re-evaluation.
3. **Base Snapshot:** when material, record only observed repository/ref/SHA/version/time values. Never fabricate Git identity merely to complete metadata.
4. **Checkpoint:** re-evaluate base before new independent work, before a new material implementation phase when upstream may have moved, before material PR/integration updates, and immediately before merge if target head moved after review.
5. **STALE_NON_SEMANTIC:** mark the work `BASE_STALE` until its base is updated appropriately and affected verification passes. Use `REBASE_REQUIRED` for private/rewritable work when appropriate; for shared/public branches, prefer a history-preserving merge/update rather than rewriting published history. Return to `FRESH` only after the update and affected verification succeed.
6. **STALE_SEMANTIC:** mark `BASE_STALE`, stop affected new implementation scope, inspect changed Framework/governance/schema/authority/REQ/DEC/interface/contracts, and use `FORWARD_PORT_REQUIRED` by default.
7. **Forward-Port:** create a clean branch/worktree from the current target, treat the stale branch as source material/evidence, and carry only still-valid accepted changes. Cherry-pick only when boundaries are clean; otherwise re-implement accepted intent on the current base. Exclude temporary staging/transport artifacts, obsolete workflow/version metadata, superseded assumptions, and unrelated experiments.
8. **Pre-Merge Base Freshness Gate:** re-resolve current target head and classify `FRESH | STALE_NON_SEMANTIC | STALE_SEMANTIC | UNKNOWN`. `UNKNOWN` or unresolved semantic drift blocks affected acceptance.
9. `git conflict = 0`, `mergeable = true`, or successful rebase is not semantic approval. **Mergeable ≠ Acceptable.**
10. Use existing `DRIFT-* / CONFLICT-* / MIG-* / CR-*` only when base staleness becomes material Project truth; do not invent a parallel Stable-ID family.

Commit count alone never decides semantic freshness. One Root Governance change can matter more than many unrelated commits.

### Framework 1.2.5 Integration Evidence Behavior

Immediately before integration, `INTEGRATION_GATE` re-resolves the current Canonical Integration Target, applies Framework `1.2.2` Base Freshness, and checks whether prior `RELEASE_FULL`/Task evidence remains valid. Reuse fresh evidence when its bound state/assumptions remain unchanged; selectively rerun invalidated/newly affected checks. Candidate/tree changes, semantic/unknown target movement, conflict resolution, rebase result, merge-time edits, or unbounded impact require affected/full reverification. `Mergeable ≠ Acceptable` remains binding.

## Workflow

1. Classify `GREENFIELD`, `BROWNFIELD`, or `IMPORT` and detect whether valid local Project Source already exists.
2. NEW Project: read canonical `main` in governed order: README → descriptor → SKILL → latest amendment → Core Governance → `templates/PROJECT-BOOTSTRAP.md` → Framework template → skeletons → mockup → project-location bootstrap when applicable; resolve the actual Project root before presenting any absolute Project Bootstrap handoff path.
3. Resolve explicit `FAST/GRILL`; otherwise `ADAPTIVE`.
4. Confirm active `FRAMEWORK-001`; if missing in an existing Project, stop affected work and propose governed repair.
5. Existing Project: read `00 → 01 → 03`, follow `01` routing, preserve local pin.
6. Before Material GitHub/Drive work in an initialized Project, resolve the applicable Project Location Binding from active `FRAMEWORK-001`; enforce `BOUND / NOT_APPLICABLE / VERIFICATION_REQUIRED` fail-closed routing and do not infer authority from recency/ranking/chat memory.
7. Before Material local/MCP work, resolve the environment-scoped Local Workspace Binding; tool/MCP workspace IDs are evidence only and unresolved applicable local execution is fail-closed.
8. For each Material Task, derive minimum sufficient verification from affected scope/dependencies/risk; a Git-backed Material Task becomes durably DONE only after a Verified Task Completion Checkpoint.
9. At Logical Checkpoints use CHECKPOINT_INTEGRITY, not RELEASE_FULL by default; run RELEASE_FULL once on a completed release/candidate and reuse valid state-bound evidence until invalidated.
10. Before integration run INTEGRATION_GATE with current Base Freshness + evidence-validity review.
11. Before every governed response emit run Response Close Completeness Gate.
12. Inspect accessible sources before asking; do not ask for facts that can be verified.
13. Classify material claims by Truth Domain, Epistemic Status, Freshness; use DRIFT/CONFLICT instead of silent reconciliation.
14. Initial creation/major structural migration requires Preview → explicit user approval → write; GREENFIELD Preview includes proposed Project Location Binding states/identities.
15. For GREENFIELD create active `00` first, then mandatory `01–05`, `09–17`; evaluate `06–08`, `40`, `60`, `91`, `92`; keep `18–19` reserved; then materialize root `PROJECT-BOOTSTRAP.md` plus exactly one valid consuming README managed fallback, verify the resulting locator chain, declare Core Installation DONE, and emit the resolved two-binding Project Settings user handoff.
16. Route management objects to `91`; current Project relations (`REL-*`) to `92`; technical blueprint to `40`; install/operations to `60` when applicable.
17. Pin imported Framework/Schema locally; upgrades use direct current→target assessment plus `MIG-*`/approval as required; classify `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`; never invent repository/Drive/local-workspace identities, commit provenance, verification evidence, or `canonical_branch`.
18. When `[Project Upgrade]` reports `UPGRADE_AVAILABLE`, the report includes the target release's migration-notes pointer when notes exist (`MIGRATION-NOTES.md`) and states their absence explicitly when they do not; comparison vocabulary and approval boundaries are unchanged. Upgrade preparation uses `templates/upgrade-preview.md` as the standard Preview structure. FAST_PATH scope rule: when the exact target candidate tree already carries committed state-bound evidence (recorded tree SHA matches the observed target tree exactly), proportional resulting-state confirmation may replace rerunning one full verification; any post-evidence candidate change invalidates reuse and fails closed. `ASSESSED_PATH` and `MAJOR_MIGRATION_REQUIRED` keep the existing one-final-`RELEASE_FULL` requirement. Continuity rule: every Logical Checkpoint on Material work persists a Resume Block into `09 Handoff` (task ID, last completed step, next step, blockers, active `ENV-*`) so any fresh session resumes within one read; Material MCP mutations are idempotent where possible, and non-idempotent calls record pre-execution intent first. `[Session]` lets the user pre-approve a bounded operation scope (`ENV-*` in `15 Action Registry`, with expiry and prohibited zones); it never overrides fail-closed governance — location/binding changes, Root Governance, schema authority, secrets, and push keep their own approval gates. `[Project Upgrade]` remains read-only through comparison; `UPGRADE_AVAILABLE` may ask to prepare an upgrade, but upgrade-intent approval authorizes assessment/Preview only and is never mutation approval.
    Persistent `[Goal]` rule: on invocation resolve intent → `OUT-* + AUTH-*` → `ACT-* / bounded ENV-*` → persist `03/09` pointers when material; on fresh-session resume read `PROJECT-BOOTSTRAP → 00 → 01 → 03 → 09 → OUT/AUTH/ACT/ENV`, fresh-check mutable prerequisites, continue the exact safe covered action without redundant Framework-level approval, then evaluate `OUT-*` success criteria separately from `ACT-*` completion. Push/destructive/Root-Binding/disclosure boundaries remain exact opt-ins and higher-level platform/tool gates still apply.
    `[Meeting]` rule: explicit bracketed question is the default outbound payload; extra Project context is minimum-necessary + separately disclosure-authorized; secrets never leak; normalize partial/provider failures without false consensus; Council/majority/Chairman are advisory only; persist material use through `EVD-*`; Goal/ENV authority never implies external disclosure.
    External-AI disclosure rule: purpose/provider → candidate context → classify portions as `EXTERNAL_OK|EXTERNAL_REVIEW|DO_NOT_DISCLOSE|UNCLASSIFIED` → remove secrets/restricted material → minimize/redact → resolve `ELIGIBLE|LIMITED|INELIGIBLE|VERIFICATION_REQUIRED` provider eligibility → resolve bounded `AUTH-*` or exact one-off instruction → partition mixed sensitivity → send only authorized eligible subset; uncertainty fails closed and material disclosure evidence uses bounded `EVD-*` without duplicating sensitive payload.
    Project Knowledge rule: after active Project authority resolves, use optional `Project-Knowledge/` only when applicable; maintain provenance/index/log/page state; keep Knowledge advisory; route promotion through canonical Project Source + authority; external use still follows TASK-026; OpenViking preserves `PROJECT_SOURCE_AUTHORITY` vs `PROJECT_KNOWLEDGE_ADVISORY` and remains `DERIVED_ONLY`.

19. If exact Git provenance is observed/material, record consistently in `00`/`14`; otherwise never fabricate it.
20. If Git branch/worktree integration is in scope, resolve the canonical integration target, classify Independent vs `STACKED_WORK`, enforce Base Freshness checkpoints, and route semantic staleness to Forward-Port before integration.
21. If implementation/runtime mapping is material, resolve Canonical Implementation Source, workspace durability, Source-to-Runtime Mapping, Runtime Mutability Boundary, and required persistent-state authority before implementation-completion/readiness claims.
22. Verify referenced current Stable IDs resolve without archive traversal before readiness/CURRENT export claims.
23. Never store actual secrets; use `SECRET-*` metadata references only.
24. Preserve history and finish with completion/readiness/exact-next-action summary using the mandatory bracketed response close; enforce Chat Closure Consistency and Response Close Completeness Gate.

## Quick Reference

| Situation | Required behavior |
|---|---|
| New Project | canonical main → Preview → approval → mandatory core; conditionals only when applicable |
| Project-management control | use `91`; canonical `RISK/ASM/MS/OUT/DEP/CR/GATE` |
| Project relations | use conditional `92`; canonical `REL-*` assertions keyed by `project_uuid`; late binding allowed |
| Cross-Project OpenViking index | AI-ControlTower scope; `DERIVED_ONLY` / rebuildable; never Project authority |
| Project Knowledge | optional Markdown-first advisory layer; provenance required; promotion uses canonical governance; never Project authority |
| Existing custom slot 92 | `MIG-*`; preserve identity/history/references; approved relocation before standard `92` |
| Technical design | use `40` when deeper than `06`; include workspace contract when material; do not silently code |
| Install/deployment | use `60`; document source/runtime/persistence/recreation and resulting-state verification when material |
| Source + Docker | shared contract + explicit variance; unexpected mismatch = DRIFT |
| Runtime-only hotfix | Runtime Truth only; preserve accepted intent through governed update to Canonical Implementation Source before canonical completion |
| Host Git/worktree + bind-mounted Docker | Git/worktree = Canonical Implementation Source; Docker = execution/runtime environment |
| Durable Dev Container workspace | valid when source identity/durability/recovery are declared; host-folder source not required |
| Required-survival runtime state | declare persistent-state authority/mechanism compatible with expected recreation |
| Rebuildable cache/temp state | may remain ephemeral when no survival requirement exists |
| Production source mount | evaluate declared lifecycle/recovery/authority/security/persistence contract; no blanket prohibition |
| Non-Docker software Project | apply workspace/runtime authority semantics without requiring Docker |
| Project Health | dimensional `GREEN/AMBER/RED/UNKNOWN` in `03`, evidence-backed |
| Decision changed basis | mark/review revalidation in `04` |
| Responsibility | mapping in `11`; permission still comes from `12` |
| Knowledge Debt | `ISS-* issue_type: KNOWLEDGE_DEBT` in `08` |
| Existing custom slot 91 | `MIG-*`; never overwrite; approved relocation first |
| Initialized Project + Material GitHub/Drive work | resolve active `FRAMEWORK-001` Project Location Binding before mutation |
| `BOUND` connector | require durable routing identity and compare intended Material target when possible |
| `VERIFICATION_REQUIRED` connector | discovery/read-only allowed; Material mutation blocked by default |
| `NOT_APPLICABLE` connector | Material Project work blocked until approved Root Governance binding/scope revision |
| One-off exact target instruction | may govern that action only; never silently persist as new binding authority |
| Persistent binding change | User Explicit Approval + governed `FRAMEWORK-001` revision/promotion |
| Repository binding | never substitute for current branch/worktree, Canonical Integration Target, or Canonical Implementation Source |
| `[Project Status]` | fresh read-only Identity → Health → Remain Tasks → Git Sync → Working Tree → Verification → Blockers; Task count ≠ Git change count |
| `[Project Path]` | show/verify configured path values; `<...>` means unset; persistent changes keep existing approval/root-governance rules |
| `[Project Upgrade]` | fresh local-pin vs canonical-upstream comparison; report `UP_TO_DATE/UPGRADE_AVAILABLE/SOURCE_DIVERGENCE/VERIFICATION_REQUIRED`; yes to upgrade = prepare Preview, not mutation approval |
| Command discovery | list registered commands only as `[XXX] : purpose`; bracketed command matching is case-insensitive and brackets are required |
| Framework upgrade | direct current→target cumulative assessment; `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`; preserve history; no mandatory intermediate execution |
| `ไม่มีขั้นตอนถัดไป` | pair with `START_NEW_CHAT` |
| `CONTINUE_CURRENT_CHAT` | requires one concrete Next Action |
| `PERSISTENCE_PENDING` | `CONTINUE_CURRENT_CHAT` + concrete persistence/recovery Next Action |
| Old free text | never auto-promote into new Stable IDs |
| Exact Git provenance unavailable | normal bootstrap continues if canonical source accessible; never fabricate |
| Independent Git worktree/branch | fresh canonical target first; do not inherit current feature branch by default |
| Feature depends on unmerged feature | explicit `STACKED_WORK` with parent/dependency/integration order |
| `STALE_NON_SEMANTIC` base | `BASE_STALE` → update safely; rebase private/rewritable or preserve shared history → reverify → `FRESH` |
| `STALE_SEMANTIC` base | `BASE_STALE` → reassess → `FORWARD_PORT_REQUIRED` into clean current-base work |
| Pre-merge Git acceptance | re-resolve current target head; `Mergeable ≠ Acceptable` |
| Material MCP work | batch to Logical Checkpoint; persist usable state/pointers to source-native owner; compact Chat result |
| Persistence failure / chat switch | `PERSISTENCE_PENDING` → `CONTINUE_CURRENT_CHAT`; `START_NEW_CHAT` only after durable continuation state exists |
| Handoff | authority does not transfer |
| R2/R3 mutation | fresh authority + required postflight/evidence |

## Red Flags

- removing/bypassing/demoting `FRAMEWORK-001`;
- creating empty conditional `06–08`, `40`, `60`, `91`, `92` merely for completeness;
- materializing reserved `18–19`;
- storing `RISK/ASM/MS/OUT/DEP/CR/GATE` as authoritative current truth outside `91`;
- treating Action completion as Milestone/Outcome success;
- treating responsibility as authority;
- hiding material Knowledge Debt because runtime works;
- overwriting a Brownfield custom slot `91`;
- overwriting a Brownfield custom slot `92` instead of governed `MIG-*` relocation;
- storing authoritative `REL-*` Project relation truth outside standard `92` when active;
- treating OpenViking, graph ranking, recency, or confidence as authority over Project-local relation assertions;
- synthesizing a reciprocal Project assertion from a derived inverse edge;
- treating `PARENT_OF` / `CHILD_OF` as permission to rewrite repository/workspace/binding/runtime topology;
- using unrestricted free-text relation types instead of core vocabulary or namespaced `X-<PROJECT_OR_DOMAIN_NAMESPACE>:<RELATION_TOKEN>` extensions;
- auto-promoting old prose into Stable IDs;
- Source/Docker divergence without declared variance or DRIFT;
- turning Tech Stack/install/Docker/workspace/persistence planning into unrequested source code/Dockerfile/Compose/scripts/CI/automation;
- claiming implementation DONE after editing only an otherwise disposable runtime;
- silently promoting a runtime hotfix into Implementation Truth;
- assuming every container filesystem is ephemeral without checking the declared workspace durability/source contract;
- requiring Canonical Implementation Source to live on a physical host filesystem;
- requiring Docker for all software/AI-assisted Projects;
- blanket-forbidding production source mounts or universally requiring immutable images;
- storing state that must survive expected recreation only in a disposable runtime layer while claiming recreation/readiness support;
- inventing `WORKSPACE_STALE`, `RUNTIME_STALE`, or another parallel freshness/Stable-ID family instead of reusing 1.2.2 and `DRIFT-*`;
- inferring Project GitHub/Drive authority from chat memory, recent activity, search ranking, display names, or another accessible Project instead of resolving active Project Location Binding;
- treating `VERIFICATION_REQUIRED` or `NOT_APPLICABLE` as permission for Material connector mutation;
- accepting `BOUND` without minimum durable routing identity;
- silently rewriting Project Location Binding from connector discovery or a one-off exact-target instruction;
- adding `canonical_branch` or other parallel Git branch authority to Location Binding;
- pairing `ไม่มีขั้นตอนถัดไป` with `CONTINUE_CURRENT_CHAT`, or `PERSISTENCE_PENDING` with `START_NEW_CHAT`;
- omitting one of `[Next Action] / [Chat] / [Reason] / [Required Read]` from the mandatory Framework response close;
- maintaining a second full Project Source example/template tree alongside `templates/project-source-mockup/` in the current distribution;
- creating unrelated Independent Work from the currently checked-out feature branch by default;
- assuming local `main` is current without verifying the canonical integration target;
- using commit count alone as proof of semantic staleness/freshness;
- continuing or merging a `STALE_SEMANTIC` branch merely because Git reports no conflict;
- treating `mergeable = true` as semantic acceptance;
- rewriting shared/public branch history merely to satisfy a rebase preference;
- hiding feature-on-feature ancestry instead of declaring `STACKED_WORK`;
- carrying temporary staging/transport or obsolete metadata into a Forward-Port merely to preserve branch history;
- merging after the canonical target moves materially without rechecking Base Freshness;
- reconstructing inaccessible Framework/project facts from memory;
- archive-dependent Current Truth;
- guessing facts/secrets/provenance;
- claiming completion without risk-appropriate verification.
