# ProjectFramework

<!-- PROJECTFRAMEWORK-BOOTSTRAP:START -->
## ProjectFramework Bootstrap

ProjectFramework Upstream:
https://github.com/captainhuke-dev/ProjectFramework

Project Bootstrap:
./PROJECT-BOOTSTRAP.md

AI / Agent:
Read `PROJECT-BOOTSTRAP.md` before Material Project work.
<!-- PROJECTFRAMEWORK-BOOTSTRAP:END -->

## TL;DR — What this is and how to use it

ProjectFramework is a **documentation-first governance framework** for planning and running Projects with AI agents. It defines where current truth, decisions, requirements, risks, and continuation context live — in a `Project-Source/` folder of numbered Markdown documents (`00–17` mandatory core; `40`, `60`, `91`, `92` conditional). It contains **no software**: rules are written contracts that humans/agents read and follow.

How to use it:

1. **New Project** — start from this repository's `main`, follow the Bootstrap Read Order to create the approved locally pinned `Project-Source/`, then materialize root `PROJECT-BOOTSTRAP.md` from the maintained template. ChatGPT/Claude Project Settings are optional thin discovery adapters.
2. **Existing Project** — your local pinned Framework never auto-upgrades. Run `[Project Upgrade]` to compare against upstream; actual upgrades stay governed (classification → Preview → explicit approval → verification).
3. **Day-to-day** — registered commands `[Project Status]`, `[Project Path]`, `[Project Upgrade]`, `[Project Audit]`, `[Session]`, `[Goal]`, and `[Meeting]` cover status, paths, upgrades, integrity audits, bounded/persistent work, and multi-model advisory review. Every governed response ends with `[Next Action]:`, `[Chat]:`, `[Reason]:`, `[Required Read]:`.

`captainhuke-dev/ProjectFramework` is the **canonical public upstream bootstrap source for new Project Source creation**. The `main` branch represents the current approved starting Framework for NEW projects.

## Current Release

- Project Source Framework: **1.13.0**
- Project Source Schema: **1.0.0**
- Distributable package root: `Framework-Source/`
- Release descriptor: `Framework-Source/FRAMEWORK-RELEASE.yaml`

## Framework 1.13.0 Project Audit + Integrity Remediation Suite

Framework `1.13.0` adds `[Project Audit]` as a fresh read-only integrity/drift command and preserves TASK-043 Strict Governed Interface semantics. Its exact top-level order is `Scope → Health → Categories → Findings → Unknowns → Evidence → Repair Routes → Continuity`; audit category health reuses `GREEN | AMBER | RED | UNKNOWN`. Findings are presentation/evidence routing only: **Audit finds ≠ Audit fixes**. Audit never creates issue/drift/conflict/migration records or grants repair authority.

TASK-032 completes the suite with a separate governed remediation workflow: selected defects resolve their canonical owner/home, `R0–R3`, exact authority/approval, prerequisites, ordered actions, rollback/reversibility, direct resulting-state verification, and affected re-audit/result confirmation. It reuses existing `ISS-* / DRIFT-* / CONFLICT-* / MIG-* / CR-* / ACT-* / AUTH-* / ENV-*` and Decision/Requirement homes. Semantic conflict is Decision/Change/Conflict work, not auto-repair; R2/R3 and other explicit gates remain independent; **ACT DONE ≠ repair outcome verified**.

This cumulative minor release is documentation/governance only: no validator/scanner/CLI, audit daemon, repair bot, auto-fix, new audit/finding/remediation Stable-ID family, or repair command is introduced. Existing initialized Projects adopt the suite only through governed Direct-to-Latest upgrade.

## Framework 1.12.2 Registered Command Strict-Interface Hardening

Framework `1.12.2` makes recognized Registered Commands **Strict Governed Interfaces**. When a command governs dimensions/order/tokens/freshness/fail-closed representation, equivalent narrative information is not enough: the governed command body must remain structurally complete. Missing evidence stays explicit as `UNKNOWN` / `VERIFICATION_REQUIRED` where applicable.

For a recognized command, **Command Contract Completeness Gate → Response Close Completeness Gate → Emit**. The first gate validates the command body; TASK-042 remains the final global close gate. Current `[Project Status]` summaries align through `Continuity`. This is documentation/governance hardening only—no parser, validator/CLI, middleware, runtime interceptor, new command, or new authority/state family is added.

## Framework 1.10.0 Project Knowledge Layer

Framework `1.10.0` adds an optional Markdown-first `Project-Knowledge/` layer for reusable research synthesis and learned context while preserving `Project Knowledge ≠ Project Authority`. It lives outside `Project-Source/00–99`, is materialized only when useful/approved, and never precedes active `FRAMEWORK-001` authority resolution.

Maintained Knowledge uses `README.md`, `index.md`, append-only `log.md`, and pages under `pages/`. Material synthesis requires provenance through `source_refs`; raw/source material remains source-native by default. Exact maintenance states are `CURRENT | REVIEW_DUE | STALE | CONTRADICTED | SUPERSEDED | RETIRED`.

Knowledge→Governance promotion always resolves the existing canonical Project Source owner, verifies evidence, obtains applicable authority, and mutates only that owner. Meeting output remains advisory, Evidence remains distinct, TASK-026 disclosure still governs external use, Knowledge cross-links are not `REL-*`, and OpenViking preserves `PROJECT_SOURCE_AUTHORITY` versus `PROJECT_KNOWLEDGE_ADVISORY` while remaining `DERIVED_ONLY`.

GREENFIELD adoption is optional/applicability-driven; Brownfield adoption is governed and never bulk-imports historical notes/chats as accepted Knowledge. Framework 1.10.0 creates no wiki/vector/runtime/MCP service or secret-value store. Maintained starter source is `Framework-Source/templates/project-knowledge/`.

## Framework 1.9.0 Portable Installation Bootstrap

Framework `1.9.0` keeps Project Source Schema `1.0.0` and release format `3` while making GREENFIELD installation portable across GPT, Claude, Hermes, Codex, and other capable Agents.

An instruction such as “install `captainhuke-dev/ProjectFramework` in this Project” means **bootstrap ProjectFramework governance into the consuming Project**. It does not mean clone the ProjectFramework repository into that Project or make the Framework upstream the consuming Project repository.

GREENFIELD installation follows:

```text
fresh ProjectFramework upstream main
→ README → release descriptor → SKILL → latest amendment → Core Governance
→ root/bootstrap/templates/mockup/location references
→ read-only Project/environment resolution
→ one GREENFIELD Preview
→ explicit user approval
→ active 00 / FRAMEWORK-001 first
→ mandatory Project Source + applicable conditionals
→ PROJECT-BOOTSTRAP.md + managed consuming README fallback
→ local Framework/Schema pin
→ resulting-state verification
→ Core Installation DONE
→ Project Settings — Required User Handoff
```

The approved GREENFIELD Preview covers the ordinary resulting bootstrap files in its bounded scope; the Agent does not ask for redundant Framework-level approval per file unless scope changes or a higher-level gate applies.

### Project Settings — Thin Bootstrap Adapter

After successful installation, the Agent returns a copy-ready block with the actual verified absolute bootstrap path:

```text
ProjectFramework Upstream: https://github.com/captainhuke-dev/ProjectFramework
Project Bootstrap: <VERIFIED_ABSOLUTE_PROJECT_BOOTSTRAP_PATH>

ProjectFramework Bootstrap Rule:
Read Project Bootstrap before the first Project-governed response in each chat.
Read-only, status, diagnostic, and failure-report responses are not exempt.
Before Material Project work, also apply all existing binding, authority, risk, and mutation gates.
If Project Bootstrap cannot be resolved, use the Project README managed bootstrap block as fallback.
ProjectFramework Upstream is for Framework discovery/upgrade only; it never replaces local Project Source authority.
```

`ProjectFramework Upstream` is fixed Framework discovery/upgrade input only. `Project Bootstrap` is environment-specific and must be verified before it is presented as ready to paste. Resolve it before the first Project-governed response in each chat when available; read-only/status/diagnostic responses are not exempt, while Material work still retains all additional mutation gates. The Project Settings block may be placed anywhere in the vendor's Project Settings / Project Instructions surface.

Core installation completion and external vendor-setting copy/paste are separate facts. Once Project Source, root bootstrap, README fallback, and required verification are durable, core installation is DONE; the Agent still MUST emit the handoff block and MUST NOT claim vendor settings were modified without execution evidence.

### Consuming README Portable Fallback

Every adopting GREENFIELD Project has exactly one managed block using `PROJECTFRAMEWORK-BOOTSTRAP:START/END` markers and relative `Project Bootstrap: ./PROJECT-BOOTSTRAP.md`. If README is absent, create it; if it exists without the block, append the block while preserving existing Project content; with one valid block, update only the managed body. Duplicate or malformed markers fail closed to governed repair.

Bootstrap resolution is:

```text
usable Project Settings absolute Project Bootstrap
→ otherwise root README managed ./PROJECT-BOOTSTRAP.md fallback
→ PROJECT-BOOTSTRAP.md
→ active Project-Source/00 / FRAMEWORK-001
→ 01 → 03 → task routing → 09 when continuation applies
```

Project Settings, README, the fixed upstream, and `PROJECT-BOOTSTRAP.md` are discovery/locator surfaces only. Active local `FRAMEWORK-001` remains Project governance authority. Successful README discovery at a moved/cloned path does not silently rewrite Local Workspace Binding.

Existing initialized Projects remain locally pinned and adopt this behavior only through governed `[Project Upgrade]`; upstream movement never silently rewrites Brownfield README, Project Settings, root governance, or bindings.

### Mandatory Response Close

Every response MUST end with:

```text
### ทำอะไรไป?

### และถัดไปคืออะไร?

**[Next Action]:** <one exact next action or ไม่มีขั้นตอนถัดไป>

**[Chat]:** CONTINUE_CURRENT_CHAT | START_NEW_CHAT

**[Reason]:** <concise reason>

**[Required Read]:** <canonical locations or ไม่มี>
```

Separate paragraphs; tokens unescaped.

Lifecycle coupling is mandatory: `ไม่มีขั้นตอนถัดไป → START_NEW_CHAT`; `CONTINUE_CURRENT_CHAT` requires one concrete Next Action; `PERSISTENCE_PENDING` requires `CONTINUE_CURRENT_CHAT` plus a concrete persistence/recovery action; nothing follows `[Required Read]`.

## Framework Intent

ProjectFramework is a **conceptual Project governance and planning framework**. It defines how a Project should represent current truth, authority, requirements, decisions, evidence, risks, assumptions, milestones, outcomes, dependencies, change control, handoff, migration, technical blueprint, installation/deployment knowledge, readiness, and continuation context across agents.

It is intentionally **documentation/governance first**. Integrity and technical rules are semantic contracts that a Human/Agent can evaluate from Framework sources. They do not imply that this repository must contain application code, a validator, CLI, Docker runtime artifacts, CI/CD, migration engine, scheduler, background automation, or other enforcement software.

Executable implementation remains a separate explicit scope.

## Operational Use vs Optional Release Assurance

Framework usability and repository/release assurance are independent dimensions:

```text
OPERATIONALLY_USABLE
REPRODUCIBLY_RELEASED
REPOSITORY_HARDENED
```

- **OPERATIONALLY_USABLE** — the Framework can correctly bootstrap and govern a Project.
- **REPRODUCIBLY_RELEASED** — optional assurance that an immutable source identity such as a Git tag/commit was preserved.
- **REPOSITORY_HARDENED** — optional assurance such as branch protection or repository rulesets.

A Framework may be operationally usable without an immutable tag, exact commit provenance, or branch protection. Those assurance gaps are not prerequisites for normal bootstrap unless a Project-Specific Rule explicitly requires them.

## Framework 1.8.0 Persistent `[Goal]` Command

`[Goal]` keeps one explicitly adopted outcome and its bounded execution authority in Project Source so a fresh Agent can resume without asking for the same Framework-level approval again. It composes existing `OUT-*` (outcome), `AUTH-*` (persistent authority), `ACT-* / ENV-*` (execution), and `03/09` status/continuation; it creates no `GOAL-*` family.

- **Default local workflow** — unless narrowed, bounded local design, planning, edits, tests, fixes, verification, commits, and Logical Checkpoints are covered.
- **Explicit opt-ins** — push/publication, destructive operation+target, Root/Binding mutation+target, and external disclosure are not included by default.
- **Cross-chat resume** — a fresh Agent resolves `PROJECT-BOOTSTRAP → 00 → 01 → 03 → 09 → OUT/AUTH/ACT/ENV`, then fresh-checks mutable prerequisites before continuing.
- **Authority stays canonical** — Handoff has `authority_transfer: false`; actual secret values remain forbidden; higher-level system/tool/platform gates still apply.
- **Outcome evidence** — `ACT DONE ≠ OUT ACHIEVED`; every Goal success criterion needs sufficient evidence.

## Framework 1.8.0 `[Meeting]` Advisory Council Command

`[Meeting]` convenes a verified multi-model advisory council for an explicit question while keeping external-provider reasoning separate from Project authority.

- **Minimum outbound context** — the explicit Meeting question is the default payload; additional Project context is minimum-necessary and separately disclosure-authorized; secret values remain prohibited.
- **Preserve disagreement** — results keep independent views, agreement/disagreement, peer-review signal, synthesis, and limitations instead of manufacturing consensus.
- **Advice, not authority** — council majority/ranking/Chairman output never becomes automatic User Approval, `AUTH-*`, `DEC-*`, `REQ-*`, Risk acceptance, or mutation permission.
- **Partial truth** — missing models/stages, Chairman failure, and provider/auth/network failures remain explicit; no synthesis is fabricated.
- **Material evidence only when needed** — material use may be preserved through existing `EVD-*`; no `MEETING-*` family exists and provider conversation JSON is not Project history.

## Framework 1.8.0 External AI Context & Disclosure Governance

External AI workflows use the smallest necessary Project context and fail closed when disclosure safety is unresolved.

- **Classification** — `EXTERNAL_OK | EXTERNAL_REVIEW | DO_NOT_DISCLOSE | UNCLASSIFIED`; unknown is not safe.
- **Provider eligibility** — `ELIGIBLE | LIMITED | INELIGIBLE | VERIFICATION_REQUIRED` is evaluated separately from classification and authority.
- **Authorization** — `EXTERNAL_REVIEW` requires bounded disclosure authority; standing grants reuse `AUTH-*`, while an exact one-off instruction stays action-scoped.
- **Secrets** — `SECRET-*` is reference metadata only and never authorizes the underlying value; actual secret values remain excluded.
- **Minimum context** — mixed-sensitivity payloads are partitioned and uncertain redaction fails closed; whole-repository export is never the convenience default.
- **Authority boundary** — disclosure permission does not grant Decision, mutation, binding, runtime, publication, or Risk authority.
- **Evidence** — material disclosure may use bounded `EVD-*` evidence without duplicating sensitive payload. No `DISC-*` family/slot or runtime redactor/router/proxy is introduced.

## Framework 1.8.0 Framework-Source Naming

Framework `1.8.0` keeps Schema `1.0.0` and release format `3` while renaming the single canonical reusable Framework distribution root:

- **`Framework-Source/`** — reusable Framework distribution, templates, amendments, launchers, migration notes, and pressure scenarios.
- **`Project-Source/`** — authoritative governance/current truth for one initialized Project; it remains distinct from Framework distribution.
- **No live old-root alias** — `managing-project-source/` is historical pre-1.8.0 migration context, not a second canonical package root.
- **Historical provenance preserved** — completed amendments/specs/plans/evidence keep old path text when that was true at capture time; current routing uses `Framework-Source/`.
- **Brownfield safety** — initialized Projects are not automatically rewritten or upgraded by the upstream directory rename.
- **Bootstrap authority unchanged** — deployed `PROJECT-BOOTSTRAP.md` still enters `Project-Source/00 → 01 → 03`, with `09` continuation; it never makes `Framework-Source/` Project authority.

## Framework 1.7.0 Self-Bootstrapping Project

Framework `1.7.0` keeps Schema `1.0.0` and release format `3` while adding one stable vendor-neutral Project-root discovery contract:

- **`<Project-Root>/PROJECT-BOOTSTRAP.md`** — mandatory for NEW `1.7.0+` Projects; maintained source template is `Framework-Source/templates/PROJECT-BOOTSTRAP.md`.
- **Locator, not authority** — the root file has no semantic slot/Stable ID and routes `PROJECT-BOOTSTRAP.md → 00 / FRAMEWORK-001 → 01 → 03`, with `09 Handoff` for continuation. Active `FRAMEWORK-001` remains Project governance authority.
- **Brownfield safety** — existing initialized Projects do not receive the file automatically. Adoption is governed `[Project Upgrade]`/migration work and preserves current truth, bindings, Stable IDs, and history.
- **Vendor independence** — ChatGPT/Claude Project Settings, `AGENTS.md`, and `CLAUDE.md` are optional thin discovery adapters after Project-root access exists. Optional `PROJECT-CONFIG.md` remains a Bootstrap Location reference only.
- **Fail closed** — missing targets or material contradiction among root bootstrap, active root/binding, vendor adapters, or optional location reference stop affected Material mutation; recency/ranking/workspace IDs never resolve authority.

Framework `1.7.0` adds no watcher, discovery daemon, MCP routing runtime, automatic upgrade, secret store, CI/CD, or deployment automation.

## Framework 1.6.0 Federated Project Graph

Framework `1.6.0` keeps Schema `1.0.0` and release format `3` while adding a federated cross-Project relation contract:

- **`92 Project Graph`** — a new standard conditional Project Source document and canonical home for current `REL-*` Project-relation assertions. Generic extension space is now `93–99`; `18–19` remain RESERVED.
- **Stable Project endpoints** — relations use immutable `project_uuid`, with core types `PARENT_OF | CHILD_OF | PEER_OF | DEPENDS_ON | SUPPORTS | RELATED_TO` and states `ASSERTED | CORROBORATED | CONFLICTED | RETIRED`.
- **Late binding and semantic nesting** — a Project may begin unrelated and materialize `92` only when relation truth becomes applicable. Parent/child topology does not imply nested folders, repositories, workspaces, or runtime locations.
- **AI-ControlTower / OpenViking boundary** — AI-ControlTower owns cross-Project indexing/orchestration; OpenViking is `DERIVED_ONLY` and rebuildable from authoritative Project Sources. It never overrides Project-local relation truth or becomes required to reconstruct it.
- **Brownfield safety** — an existing custom slot `92` is never overwritten. Upgrade uses `MIG-*` to preserve identity/history/references and relocate the custom document to a suitable free `93–99` or other semantic slot before standard `92` activation.

This remains documentation/governance scope. Framework `1.6.0` adds no OpenViking runtime, graph database requirement, Graphify integration, crawler, watcher, scheduler, sync daemon, validator/CLI, or automatic conflict resolution.

## Framework 1.5.0 ChatGPT→MCP Continuity

Framework `1.5.0` keeps Schema `1.0.0` and makes agent-driven system management run continuously instead of stopping:

- **Resume Blocks** — every Logical Checkpoint writes resume state into `09 Handoff` (task, last step, next step, blockers, active envelope) so any fresh session continues within one read.
- **`[Session]`** — pre-approve a bounded operation scope once per session (`ENV-*` entries in `15 Action Registry`, with expiry and prohibited zones); fail-closed gates for location/binding/root/secret/push never lift. The shorter current command name preserves the original Framework 1.5.0 envelope semantics.
- **MCP Resume Semantics** — mutations should be idempotent; non-idempotent calls record intent first; after a drop, work resumes from the last checkpoint, not from memory.
- **`[Project Status]` Continuity dimension** — shows Resume Block freshness (`FRESH | STALE | NONE`), the active Envelope, and repeated handoff breaks.

## Framework 1.4.0 Upgrade Acceleration

Framework `1.4.0` keeps Project Source Schema `1.0.0` and release format `3` and makes upgrading initialized Projects faster without weakening governance:

- **MIGRATION-NOTES.md** documents affected surfaces and an upgrade checklist per release (starting with `1.3.x → 1.4.0`); `FRAMEWORK-RELEASE.yaml` points at the current notes. Notes are routing aids, never normative authority.
- **FAST_PATH verification scope rule**: when the exact target candidate tree carries committed state-bound evidence (matching tree SHA), proportional resulting-state confirmation may replace a full rerun; any post-evidence change fails closed back to the full requirement. `ASSESSED_PATH` and `MAJOR_MIGRATION_REQUIRED` keep one final `RELEASE_FULL`.
- **templates/upgrade-preview.md** standardizes upgrade Previews: identity, classification, affected surfaces, preservation checklist, rollback plan, approvals.
- **Launcher compaction policy** keeps the `<=4,500` character ceiling; prose may be compacted, canonical tokens/commands/labels/close fields never are.
- **`[Project Upgrade]` reports now include the target release's migration-notes pointer** when notes exist, so affected surfaces are visible before preparation.

## Framework 1.3.1 Project Upgrade Command

Framework `1.3.1` adds registered `[Project Upgrade]` behavior while keeping Project Source Schema `1.0.0`, release format `3`, existing semantic slots/Stable-ID families, and the Framework `1.3.0` Direct-to-Latest architecture unchanged.

For initialized Projects, the command treats the active local `FRAMEWORK-001` pin as current authority and fresh-resolves canonical upstream only as a target candidate. It reports `UP_TO_DATE | UPGRADE_AVAILABLE | SOURCE_DIVERGENCE | VERIFICATION_REQUIRED`; equal version strings do not suppress material source divergence, and unavailable freshness evidence fails closed rather than using memory, cached refs, recent workspaces, or similarly named repositories.

When `UPGRADE_AVAILABLE` is verified, the command asks whether the user wants to **prepare** an upgrade. A positive answer starts cumulative current→target assessment and Preview only; actual Project mutation still requires `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED` classification, preservation/rollback planning, separate explicit mutation approval, affected verification, one final `RELEASE_FULL`, and governed promotion/history preservation. The command is not an automatic updater and adds no path/binding, branch, implementation-source, runtime, or persistent-state authority.

## Framework 1.3.0 Command & Direct-to-Latest Upgrade Additions

Framework `1.3.0` adds a small registered bracketed Project command contract, Markdown-safe mandatory response-close rendering, and **Direct-to-Latest / Cumulative Target-State Upgrade** semantics while keeping Project Source Schema `1.0.0`, semantic slots, Stable-ID families, initialized-Project local pinning, and existing authority systems unchanged.

Registered commands require literal brackets and match case-insensitively inside them. `[Project Status]` fresh-observes Project/Task/Git/verification/blocker state as a read-only dashboard; `[Project Audit]` fresh-observes integrity/drift with exact governed dimensions and never auto-fixes Project truth; `[Project Path]` shows/validates configured bootstrap path values and routes explicit change requests through existing location governance. Angle-bracket values such as `<STORAGE>` or `<WS>` mean unset, not literal paths. Natural-language command-help requests list only registered commands as `[XXX] : purpose`.

Mandatory response-close semantic labels remain `[Next Action]:`, `[Chat]:`, `[Reason]:`, and `[Required Read]:`, but Framework `1.3.0` recommends Markdown-safe presentation such as `**[Chat]:** CONTINUE_CURRENT_CHAT` so a renderer cannot hide the field as reference-definition syntax. Lifecycle vocabulary and Chat Closure Consistency are unchanged.

Initialized Project upgrades now compare current reconstructable truth directly with the explicitly selected target Framework instead of mechanically executing every intermediate release migration. The path is classified `FAST_PATH`, `ASSESSED_PATH`, or `MAJOR_MIGRATION_REQUIRED`; cumulative migration still preserves Stable IDs, Project-specific rules, bindings, history, approval, rollback, validation, evidence, and promotion controls. The latest starter remains a NEW-Project target representation, not a default destructive rebuild mechanism for initialized Projects.

Upgrade verification reuses Framework `1.2.5` progressive verification: affected/risk-scoped checks during migration, checkpoint integrity at handoff boundaries, and one `RELEASE_FULL` on the final unchanged target candidate. Historical amendments/migrations remain provenance and rationale; skipping intermediate execution never deletes history or weakens governance. Framework `1.3.0` adds no automatic updater, migration engine, command parser service, CLI, hook, bot, CI/CD, scheduler, watcher, or runtime enforcement.

## Framework 1.2.6 Bootstrap Location & File Storage Additions

Framework `1.2.6` adds deterministic **Bootstrap Location Semantics** before `FRAMEWORK-001` resolution and generalized governed **File Storage Binding** for non-Google-Drive external storage while keeping Project Source Schema `1.0.0`, semantic slots, Stable-ID families, existing authority systems, and initialized-Project pinning unchanged.

The six bootstrap/execution concepts remain distinct: **Framework Source**, **Remote Location**, **File Storage Location**, **MCP Location**, **Local Workspace**, and dynamically observed **current branch/worktree**. Bootstrap locators help find/rout authority but never silently become it. Once valid active `FRAMEWORK-001` resolves, its Project Location Binding governs initialized-Project routing. Material bootstrap/root mismatch fails closed and rewrites neither side silently. Current branch/worktree remains `DYNAMIC / VERIFY_EACH_SESSION`; Remote Location creates no branch authority.

Generic `file_storage_locations` under active `FRAMEWORK-001` govern purpose/content-scoped non-Drive stores such as S3/object storage, NAS/SMB/NFS, SharePoint, file servers, and durable filesystem storage. File Storage reuses `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED`; verification reuses `VERIFIED | USER_CONFIRMED | VERIFICATION_REQUIRED`, with `BOUND` permitted only with `VERIFIED` or `USER_CONFIRMED`. Known-applicable unresolved storage fails closed; Projects with no external storage need no synthetic provider entries; absence never authorizes fallback.

Framework `1.2.6` preserves the dedicated `project_location_binding.google_drive` block as canonical Drive authority. Bootstrap Google Drive locators map to it; generic storage must not duplicate the same Drive target/content scope. File Storage remains distinct from Repository/Local Workspace routing, Canonical Implementation Source, Runtime/Data/Persistent-State, backup, and deployment authority. Actual storage credentials remain external via existing `SECRET-*` reference semantics.

Existing initialized Projects do not auto-upgrade or gain new storage applicability. Migration must preserve the local pin and must not invent locations/providers. This release remains governance/documentation scope and adds no automatic discovery/sync, validator, hook, bot, CI/CD, scheduler, watcher, branch switcher, or runtime enforcement.

## Framework 1.2.5 Additions

Framework `1.2.5` adds **Verified Material Task Completion Checkpoints**, **Progressive / Risk-Scoped Verification with Evidence Reuse**, **Environment-Scoped Local Workspace Binding**, and a **Response Close Completeness Gate** while keeping Project Source Schema `1.0.0`, semantic slots, Stable-ID families, and existing Project-local pinning unchanged.

For Material Git-backed Tasks, durable `DONE` requires affected verification to pass and the required completed result to exist in observed Git commit(s); read-only/no-mutation Tasks require no synthetic commit, `WIP commit ≠ Task DONE`, and `commit ≠ push`. Cross-environment handoff must make the completion commit reachable to the receiving environment before claiming continuation safety.

Verification now scales with affected scope, dependencies, and `R0–R3` risk. Task-level work uses minimum sufficient checks, Logical Checkpoints verify durable continuation rather than full regression, a completed release/candidate receives one full verification per unchanged candidate state, and fresh state-bound evidence may be reused until selectively invalidated. Integration still re-resolves Canonical Integration Target/Base Freshness and evidence validity; exact fast-forward to an already verified tree normally needs proportional resulting-state confirmation rather than an unconditional full rerun.

Project Location Binding now supports environment-scoped **Local Workspace Binding** for local/MCP execution using the existing `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED` states. A bound local environment uses a verified/user-confirmed absolute path and, for Git-backed work, repository identity should be cross-checked when practical. MCP `workspaceId`, active/recent workspace lists, and similar tool identifiers are routing evidence only. Repository Location Binding, Local Workspace Binding, current branch/worktree, Canonical Integration Target, Canonical Implementation Source, and Runtime Location remain distinct semantics.

Every Framework-governed assistant response also performs a lightweight **Response Close Completeness Gate** before emit to ensure the two mandatory headings plus `[Next Action]`, `[Chat]`, `[Reason]`, and `[Required Read]` are present exactly once, ordered, lifecycle-consistent, and final. The gate validates assistant output representation only and does not fabricate claims about downstream UI rendering.

This remains governance/documentation scope. Framework `1.2.5` adds no executable validator, hook, bot, CI/CD workflow, scheduler, filesystem watcher, automatic workspace selector, new semantic slot, or Stable-ID namespace. Existing initialized Projects remain locally pinned and do not auto-upgrade.

## Framework 1.2.4 Additions

Framework `1.2.4` adds **Project Location Binding**, Chat Closure Consistency, and the bracketed Mandatory Response Close without changing Project Source Schema `1.0.0`, semantic slots, or Stable-ID families.

Active local `FRAMEWORK-001` is the canonical home for GitHub/Google Drive Project Location Binding. GitHub and Drive resolve independently as `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED`: `BOUND` requires durable routing identity, `VERIFICATION_REQUIRED` is fail-closed for Material mutation while read/search/discovery may resolve candidates, and `NOT_APPLICABLE` blocks Material Project work through that connector. Connector recency, search ranking, chat memory, or another accessible Project never transfer Project authority.

Persistent binding changes are Root Governance mutations requiring User Explicit Approval plus governed `FRAMEWORK-001` revision/validate/promote/supersede/archive flow. A one-off exact-target instruction may authorize only that otherwise-allowed action and does not persistently rewrite the binding.

Repository Location Binding remains distinct from current branch/worktree, **Canonical Integration Target**, and **Canonical Implementation Source**. Framework `1.2.4` introduces no competing `canonical_branch`; Framework `1.2.2` Base Freshness and integration-target semantics remain authoritative.

GitHub/Drive continuation keeps source-native ownership and durable pointers rather than replicating canonical content. `09 Handoff` references the active root binding instead of becoming a second repo/folder authority.

Chat closure is deterministic: `ไม่มีขั้นตอนถัดไป → START_NEW_CHAT`; `CONTINUE_CURRENT_CHAT` requires one concrete Next Action; `PERSISTENCE_PENDING` requires `CONTINUE_CURRENT_CHAT` plus a concrete persistence/recovery action. Mandatory response-close fields render as `[Next Action]:`, `[Chat]:`, `[Reason]:`, and `[Required Read]:` in separate Markdown paragraphs.

This remains governance/documentation scope. Framework `1.2.4` adds no application/runtime implementation, connector synchronization, validator, scheduler, bot, CI/CD, new semantic slot, or Stable-ID namespace. Existing initialized Projects remain locally pinned and do not auto-upgrade; migration must not invent repository/folder identities.

## Framework 1.2.3 Additions

Framework `1.2.3` adds **Development Workspace and Runtime Authority** governance for software/implementation-bearing Projects without changing Project Source Schema `1.0.0`, semantic slots, or Stable-ID families.

When the distinction is material, a Project identifies a **Canonical Implementation Source**: the durable declared source location whose verified state determines current `IMPLEMENTATION` Truth. Fresh runtime observation remains authoritative for `RUNTIME` Truth. Editing or successfully running code only inside an otherwise disposable runtime does not silently transfer Implementation authority; material expected-alignment mismatch reuses existing `DRIFT-*` semantics.

`40 Technical Design` may now carry a **Development Workspace Contract** covering source identity, workspace type/location/durability, Human/Agent edit location, execution environment, Source-to-Runtime Mapping, dependency isolation, Runtime Mutability Boundary, Persistent-State Boundary, and related verification/drift context. `60 Deployment Plan` may carry runtime mutability, data/storage authority, persistent-state, replacement/recreation, and material development/production mapping semantics.

Durability is about the lifecycle/recovery contract, not physical host placement. Host Git repositories, Git worktrees, remote/VM durable workspaces, and Dev Containers backed by durable source storage can all be valid. Docker, host-local source storage, immutable production images, and production source mounts remain Project-specific/applicability-driven rather than universal requirements or prohibitions.

State that must survive expected runtime replacement requires a declared persistent authority/mechanism; rebuildable cache/temp/scratch state may remain ephemeral when no survival requirement applies.

Framework `1.2.3` composes with and does not replace Framework `1.2.2` Git Base Freshness. `STACKED_WORK`, `FRESH / STALE_NON_SEMANTIC / STALE_SEMANTIC / UNKNOWN`, `BASE_STALE`, `REBASE_REQUIRED`, `FORWARD_PORT_REQUIRED`, and the Pre-Merge Base Freshness Gate retain their existing meanings. **Mergeable ≠ Acceptable.**

This remains documentation/governance scope. Framework `1.2.3` introduces no Dockerfile/Compose/Dev Container runtime artifacts, Git hook, bot, CI workflow, validator, scheduler, merge queue, runtime enforcement, new semantic slot, or new Stable-ID namespace. Existing initialized Projects remain locally pinned and do not auto-upgrade.

## Framework 1.2.2 Additions

Framework `1.2.2` adds **Git Base Freshness and Forward-Port governance** for Projects that use branches/worktrees. New independent work starts from a freshly verified canonical integration target rather than inheriting whichever feature branch happens to be checked out. Feature-on-feature ancestry is explicit `STACKED_WORK`.

Base freshness distinguishes `FRESH`, `STALE_NON_SEMANTIC`, `STALE_SEMANTIC`, and `UNKNOWN`. Non-semantic drift may be updated safely without rewriting shared history; semantic drift uses `BASE_STALE` and normally `FORWARD_PORT_REQUIRED` into clean current-base work. Immediately before acceptance/merge, the target head is rechecked: a conflict-free Git merge is not semantic approval — **Mergeable ≠ Acceptable**.

This remains documentation/governance scope. Framework `1.2.2` introduces no Git hook, bot, CI workflow, validator, branch-protection automation, new semantic slot, or new Stable-ID namespace. Existing initialized Projects remain locally pinned and do not auto-upgrade.

## Framework 1.2.1 Additions

Framework `1.2.1` adds **Externalized Working Memory and Chat Lifecycle** governance. Material connector/MCP work is persisted at logical checkpoints to its source-native durable owner; transient reads/searches stay transient by default. Persistence failure is explicit through `PERSISTENCE_PENDING`, and `START_NEW_CHAT` is continuation-safe only after the minimum continuation state is durable outside Chat.

The Project Source namespace and Schema remain unchanged at `1.0.0`; existing initialized Projects remain locally pinned and do not auto-upgrade.

## Framework 1.2.0 Additions

Framework `1.2.0` adds three standard **conditional** extended documents:

```text
40 Technical Design              CONDITIONAL
60 Deployment Plan               CONDITIONAL
91 Project Management Control    CONDITIONAL / STANDARD IN 1.2.0+
```

### 91 — Project Management Control

`91` is the canonical home for:

```text
RISK-*   Risk
ASM-*    Assumption
MS-*     Milestone
OUT-*    Outcome
DEP-*    Dependency
CR-*     Change Request
GATE-*   Review / Phase Gate
```

It supports explicit Risk/Assumption management, Milestone vs Outcome distinction, dependency control, scope/change assessment, and review gates without changing the mandatory core `00–17` set.

### 40 — Technical Design

`40` is the deeper technical blueprint for Projects with meaningful software/technical implementation. It may document:

```text
Tech Stack
system/component responsibilities
interfaces and dependencies
source-structure responsibilities
configuration contract
runtime requirements
Source/Docker architecture
Source/Docker parity and variance
```

Framework `1.2.3` extends this existing home with Development Workspace Contract semantics; it does not create a new technical slot.

`40` does **not** authorize creation of application source code, Dockerfile, Compose/Kubernetes/Helm artifacts, scripts, CI, or automation.

### 60 — Deployment Plan

`60` is the installation/operations blueprint. It may document:

```text
prerequisites
Source installation
Docker installation
configuration and secret references
startup / shutdown
verification / health
logs / diagnostics
upgrade / rollback
backup / restore
cleanup / troubleshooting
```

Framework `1.2.3` extends this existing home with source-to-runtime, runtime-mutability, persistent-state, and replacement/recreation semantics when material.

A real Project may record concrete commands/paths in `60` when they are verified Project truth. ProjectFramework itself does not invent executable commands for nonexistent software.

### Deployment Support Vocabulary

Software Projects may declare:

```text
SOURCE_ONLY
DOCKER_ONLY
SOURCE_AND_DOCKER
NOT_APPLICABLE
```

`SOURCE_AND_DOCKER` requires one declared application/configuration/data/security/persistence contract. Intentional differences must be explicit Deployment Mode Variance; unexpected differences are `DRIFT-*`.

## Project Operating Model

Framework `1.2.0` also adds:

- multi-dimensional Project Health in `03 Current State` using `GREEN / AMBER / RED / UNKNOWN` with reason/evidence;
- `TIME_BASED` and `EVENT_BASED` review cadence semantics without creating a scheduler;
- Decision Revalidation fields in `04 Decision Log`;
- Responsibility Mapping in `11 Actor Registry` while preserving **Responsibility ≠ Authority**;
- `ISS-* issue_type: KNOWLEDGE_DEBT` in `08 Open Issues` for material stale/missing operational knowledge.

## Platform Project Instructions

Current Framework `1.12.2` maintained ChatGPT/Claude instruction artifacts are **thin vendor bootstrap adapters**. They carry the same two-binding semantics and route into `PROJECT-BOOTSTRAP.md`; they do not duplicate Core Governance.

- **ChatGPT Projects:** copy the resolved thin block (or maintained `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md` after replacing the Project Bootstrap placeholder with the verified absolute path) into **Project settings → Instructions**.
- **Claude Projects:** use the equivalent maintained thin adapter in **Set project instructions**.
- **Hermes / Codex / other Agents:** use the same generic two-binding block in the platform's applicable Project Instructions/settings surface when one exists.

Vendor settings remain optional discovery adapters and never become a competing governance root. After a valid local Project Source resolves, active local `FRAMEWORK-001` is authoritative.

## New-Project Bootstrap Read Order

For every NEW Project Source:

1. When vendor Project Settings are available, use the resolved two-binding Thin Bootstrap Adapter; otherwise start from the Project root README fallback or canonical upstream for genuine GREENFIELD discovery.
2. Read this `README.md` from canonical repository `main`.
3. Read `Framework-Source/FRAMEWORK-RELEASE.yaml`.
4. Read `Framework-Source/SKILL.md`.
5. Read the latest Framework governance amendment and `Framework-Source/references/core-governance-rules.md`.
6. Read `Framework-Source/templates/00-project-source-framework.md`, `templates/core-document-skeletons.md`, and `templates/project-source-mockup/README.md`.
7. Preview the proposed Project Source, including proposed GitHub/Drive Project Location Binding states/identities, and obtain explicit user approval before writing.
8. Create active `00-Project Source Framework` first with the approved Project Location Binding, then mandatory `01–05` and `09–17`.
9. Evaluate `06–08`, `40`, `60`, `91`, and `92` by applicability; do not create empty conditional documents merely to make a tree look complete.
10. Keep `18–19` reserved; `92` is standard conditional Project Graph in Framework `1.6.0+`; use `93–99` as Project-specific/Governance Extension space unless a later Framework revision governs them otherwise.
11. Pin the imported Framework/Schema locally. The repository is not a live dependency after bootstrap.
12. If exact Git tag/SHA provenance is actually observed and useful, record it. If unavailable, do not invent it and do not block otherwise valid bootstrap solely for that reason.

## Existing Projects and Migration Safety

Existing Projects **do not auto-upgrade** when this repository changes. Their project-local approved Framework/Schema pins remain authoritative. Upgrade to a newer Framework uses governed `MIG-*` assessment, explicit approval, validation, promotion, supersede/archive, and postflight.

A Brownfield Project may already use semantic slot `91` for a custom document. Framework `1.2.0` must not overwrite it: assess through `MIG-*`, preserve identity/history/references, relocate only with approval, then activate standard `91` if applicable.

A Project pinned before Framework `1.6.0` may likewise already use slot `92` as a custom extension. Framework `1.6.0` must not overwrite it: open/route `MIG-*`, preserve identity/history/references, relocate only with governed approval to a suitable free `93–99` or other semantic slot, then activate standard `92 Project Graph` only when applicable.

Old free-text notes are not automatically converted into new `RISK-*`, `ASM-*`, `MS-*`, `OUT-*`, `DEP-*`, `CR-*`, or `GATE-*` objects. Promotion requires sufficient current semantics, ownership, status, and epistemic/evidence state.

Framework `1.2.3` migration also does not invent Canonical Implementation Source, workspace durability, source-to-runtime mapping, or persistence topology. Unknown values remain explicit until verified from actual Project sources/runtime.

## Concept-First Integrity Contract

At minimum, Framework integrity means:

- current Framework/Schema declarations agree across current distribution artifacts;
- semantic slots `00–17` retain their governed meanings;
- `06–08` remain **CONDITIONAL**;
- `18–19` remain **RESERVED**;
- `40`, `60`, `91`, and `92` are applicability-driven conditional documents;
- `91` owns `RISK / ASM / MS / OUT / DEP / CR / GATE` current records;
- `92` owns current `REL-*` Project-relation assertions when active;
- `93–99` remain extension space unless governed otherwise;
- Project relations use immutable `project_uuid` endpoints and do not silently rewrite location/binding/runtime/integration/implementation authority;
- AI-ControlTower/OpenViking cross-Project indexing is derived/rebuildable and never replaces Project Source authority;
- ChatGPT and Claude shared governance semantics remain equivalent;
- active/current Stable IDs resolve without archive dependency;
- existing Projects never silently auto-upgrade;
- platform launchers never override active local `FRAMEWORK-001`;
- Canonical Implementation Source and Runtime Truth remain distinct when the distinction is material;
- required-survival state has a declared persistence contract compatible with claimed runtime replacement/recreation;
- missing facts, authority, source, or provenance are never fabricated.

These requirements may be reviewed manually or by an Agent. **The existence of an Integrity Contract is not authorization to build enforcement software.**

## Optional Source Provenance

`FRAMEWORK-RELEASE.yaml` identifies the canonical repository and bootstrap branch. Exact Git provenance is enhanced assurance, not a bootstrap prerequisite.

When exact provenance is actually observed, a Project may record source ref/tag and resolved commit SHA. When it is not observed, use an explicit `UNKNOWN` / `UNVERIFIED` state only when provenance tracking is material. Never fabricate or retroactively backfill an unobserved Git identity merely to make records look complete.

## Bootstrap Mockup

`templates/project-source-mockup/` is the concrete starter representation of the Project Source namespace. It contains `.template.md` starters for `00–17`, conditional starters for `40`, `60`, `91`, and Framework `1.6.0` standard conditional `92 Project Graph`; current starter metadata is stamped to Framework `1.12.2` / Schema `1.0.0`.

The mockup is **the single maintained concrete starter representation in the current distribution** and is executable documentation, not normative authority. `references/core-governance-rules.md` remains authoritative if a mismatch appears. The presence of a conditional template does not mean an active Project must create that document. Historical composition examples remain recoverable from Git history rather than being maintained as a second full Project Source tree.

## Current-Truth Integrity

Active canonical registries are materialized current projections, not delta chains. Current Stable IDs must resolve from the Current Reconstructable Snapshot without requiring archived revisions. Archive remains Historical Truth; it must not become a dependency for determining Current Truth.

## Repository Layout

```text
ProjectFramework/
├── README.md
├── LICENSE
├── Framework-Source/
│   ├── FRAMEWORK-RELEASE.yaml
│   ├── CHATGPT-PROJECT-INSTRUCTIONS.md
│   ├── CLAUDE-PROJECT-INSTRUCTIONS.md
│   ├── SKILL.md
│   ├── references/
│   ├── templates/
│   │   ├── project-source-mockup/
│   │   └── project-knowledge/
│   └── tests/
└── docs/
    └── superpowers/
        ├── specs/
        └── plans/
```

Use `Framework-Source/` as the reusable framework package. Files under `docs/superpowers/` document development of this repository and are not automatically copied into each Project Source.

## Supersession Note

Framework `1.6.0` extends the concept-first direction of earlier releases with federated Project relation governance while preserving Project-local authority. Git tags, exact commit provenance, branch protection, executable validators, graph/index runtimes, CI enforcement, container/runtime enforcement, and other automation remain optional assurance or separate explicitly requested implementation scope rather than prerequisites for normal Framework usability.


## Framework 1.12.0 Task Dependency Planning

Framework 1.12.0 Set 1 starts with explicit Task dependency/readiness metadata so execution order is never inferred from Task number. Durable Task sources may declare `depends_on`, `blocks`, `enables`, `parallelizable_with`, `priority: CRITICAL | HIGH | NORMAL | LOW | UNSET`, and `readiness: READY | WAITING | BLOCKED | UNKNOWN`.

Task readiness is not Task lifecycle, and Task planning metadata is not `DEP-*` Project-management authority. Recommended order remains advisory; no scheduler or automatic Task execution is introduced.

## Framework 1.12.0 Project Tool / MCP Execution Profile

Projects may adopt optional root `Project-Execution/` policy after Project authority resolves. TASK-027 adds `README.md` + `tools.md` to declare a PRIMARY tool/MCP, allow/disallow lists, deterministic `NONE | ORDERED_ALLOW_LIST` fallback, and `FAIL_CLOSED | READ_ONLY_DIAGNOSTIC_ONLY` failure policy.

The profile constrains eligible execution routes; it does not grant authority, change Project Location Binding, identify the current branch/worktree, store credentials, or bypass push/destructive/secret/disclosure gates. GREENFIELD/Brownfield adoption is explicit/applicability-driven. No runtime MCP router or automatic tool switcher is introduced.

## Framework 1.12.0 Agent / Model Capability Profile

Optional `Project-Execution/capabilities.md` defines vendor-neutral capability requirements (`REASONING`, `CODING`, `RESEARCH`, `REVIEW`, `COUNCIL`), execution availability (`FULL | DEGRADED | UNAVAILABLE | UNKNOWN`), local/external provider scope, and independent-review requirements.

Capability eligibility is separate from Tool/MCP eligibility and never grants authority. External providers still follow TASK-026; `[Meeting]` remains advisory. No model router/provider runtime or automatic delegation is introduced.

## Framework 1.12.0 Release / Publication Contract

ProjectFramework now distinguishes implementation, integration, repository publication, release, artifact publication, and deployment as independent facts. `Task DONE ≠ MERGED ≠ PUSHED ≠ RELEASED ≠ ARTIFACT_PUBLISHED ≠ DEPLOYED`; local implementation authority never grants publication/deployment authority.

Release Candidate evidence is bound to actual source/tree/prerequisites. `RELEASE_FULL` verifies candidates; `INTEGRATION_GATE` checks mutable target freshness before shared-state actions. Partial publication and `PERSISTENCE_PENDING` are reported without rewriting observed external truth. No CI/CD or publication automation is introduced.

## Framework 1.12.0 Security & Trust Boundary Contract

Optional `Project-Execution/trust.md` classifies applicable surfaces as `TRUSTED | LIMITED_TRUST | UNTRUSTED | PRIVILEGED | EXTERNAL | UNKNOWN` and constrains data/code/artifact/execution crossings. Trust classification never grants authority or secret disclosure; UNKNOWN materially sensitive crossings fail closed.

Trust policy composes with TASK-027 tools, TASK-034 capabilities, TASK-026 disclosure/secrets, and TASK-035 publication truth. No scanner, sandbox, policy engine, runtime isolation, secret store, or privileged-operation automation is introduced.
