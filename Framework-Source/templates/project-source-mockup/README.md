# Project Source Bootstrap Mockup

This directory is the concrete starter representation of the Project Source semantic namespace for **Framework 1.12.0 / Schema 1.0.0**. Use it to answer: **“เลขไหน คือเรื่องอะไร และ starter file ชื่ออะไร?”**

> **Authority:** This mockup is executable documentation. `../../references/core-governance-rules.md`, active `00 Project Source Framework`, and `../core-document-skeletons.md` are normative. If this mockup disagrees with Core Governance, Core Governance wins and the mockup must be corrected.

> **Maintenance invariant:** `templates/project-source-mockup/` is the **single maintained concrete starter representation** in the current Framework distribution. Do not maintain a second full Project Source example/template tree alongside it; historical composition examples remain available through Git history.

## Framework 1.10.0 Project Knowledge Semantics

Optional consuming-Project `Project-Knowledge/` is maintained outside Project Source semantic slots and never becomes Project authority. When applicable/approved after `FRAMEWORK-001` resolves, use the separate `../project-knowledge/` starter source for Knowledge `README.md`, `index.md`, `log.md`, and page template. Material synthesis requires provenance; Knowledge states are maintenance states; promotion into governance requires canonical-owner evidence/authority. Knowledge links are not `REL-*`, external use follows TASK-026, and OpenViking preserves `PROJECT_SOURCE_AUTHORITY` vs `PROJECT_KNOWLEDGE_ADVISORY` while remaining `DERIVED_ONLY`.

## Framework 1.9.0 Portable Installation Bootstrap Semantics

GREENFIELD installation materializes active `00` first, mandatory Project Source, root `PROJECT-BOOTSTRAP.md`, and exactly one valid consuming README `PROJECTFRAMEWORK-BOOTSTRAP` managed fallback using relative `./PROJECT-BOOTSTRAP.md`. The installing Agent verifies the locator chain, declares Core Installation DONE when local state is durable, then emits the resolved two-binding Project Settings handoff: fixed `ProjectFramework Upstream` plus verified absolute `Project Bootstrap` and the canonical Bootstrap Rule.

Project Settings / consuming README / root bootstrap remain discovery or locator layers; active local `FRAMEWORK-001` is authority. Duplicate/malformed README markers fail closed; existing Project README content outside the managed pair is preserved. Internal Git/Drive/File Storage/MCP/Local Workspace semantics remain governed even though current vendor Project Settings are thinner.

## Framework 1.8.0 Persistent `[Goal]` Semantics

`[Goal]` is a persistent command backed by existing canonical objects: Goal outcome `OUT-*` in conditional `91`, durable user authorization `AUTH-*` in `12`, execution `ACT-* / ENV-*` in `15`, status in `03`, and continuation pointers in `09` with `authority_transfer: false`. It creates no `GOAL-*` family.

When the user does not narrow the Goal, bounded local design/plan/edit/test/fix/verify/commit/checkpoint work is pre-authorized. Push, destructive actions, Root/Binding mutation, and external disclosure remain explicit opt-ins under current governance. GREENFIELD starter materialization does not create an active Goal/`OUT-*`/Goal `AUTH-*`; `91` becomes applicable only when Goal/other management-control truth is actually material.

## Framework 1.8.0 `[Meeting]` Advisory Council Semantics

`[Meeting]` sends the explicit question as the default payload to a verified multi-model advisory provider. Extra Project context is minimum-necessary and separately disclosure-authorized; secret values remain prohibited. Council/majority/Chairman output is advice/evidence only and never automatic `AUTH-*`, `DEC-*`, `REQ-*`, Risk acceptance, or mutation permission.

Material Meeting use may be preserved as `EVD-*` in `13 Evidence Registry`; transient exploratory Meetings need no synthetic record. No `MEETING-*` family exists, provider JSON is not Project history, and GREENFIELD creates no council conversation, provider credential/runtime, Meeting evidence, or disclosure authority automatically.

## Framework 1.8.0 External AI Context & Disclosure Semantics

Outbound Project context uses `EXTERNAL_OK | EXTERNAL_REVIEW | DO_NOT_DISCLOSE | UNCLASSIFIED`; provider/tool eligibility is separately `ELIGIBLE | LIMITED | INELIGIBLE | VERIFICATION_REQUIRED`. `Classification ≠ Authorization`, provider eligibility is not Project authority, and unknown/protected context fails closed for automatic external use. Standing disclosure permission reuses bounded `AUTH-*`; exact one-off instructions remain action-scoped; material disclosure evidence uses `EVD-*`; `SECRET-*` remains reference-only.

Minimum-necessary context, mixed-sensitivity partitioning, and redaction adequacy apply to `[Meeting]`, Project Knowledge, OpenViking and other external-AI consumers. GREENFIELD creates no standing disclosure grant, provider eligibility grant, credential, blanket `EXTERNAL_OK`, `DISC-*` family/slot, or runtime redactor/router/proxy. Brownfield does not retroactively classify historical content safe or synthesize disclosure authority from prior AI use.

## Framework 1.7.0 Self-Bootstrapping Project Semantics
## Framework 1.8.0 Framework-Source Naming Semantics

Framework `1.8.0` keeps Project Source Schema `1.0.0` and makes the reusable upstream distribution root `Framework-Source/`. This distribution root is distinct from a consuming Project's authoritative `Project-Source/`; root `PROJECT-BOOTSTRAP.md` continues to route into that consuming Project Source. The historical pre-1.8 name `managing-project-source/` is not maintained as a live alias.


Framework `1.7.0` keeps Schema `1.0.0` and makes the resulting NEW Project self-discoverable from its root. `<Project-Root>/PROJECT-BOOTSTRAP.md` is mandatory for NEW `1.7.0+` Projects, stays outside `Project-Source/`, has no Stable ID, and routes `PROJECT-BOOTSTRAP.md → 00 → 01 → 03`, with `09` for continuation. Active `FRAMEWORK-001` remains authority. Existing Projects adopt the file only through governed `[Project Upgrade]`; `PROJECT-CONFIG.md` and vendor settings remain optional location/discovery adapters.

## Framework 1.6.0 Federated Project Graph Semantics

Framework `1.6.0` adds standard conditional `92 Project Graph`, canonical current `REL-*` assertions keyed by immutable `project_uuid`, late binding, Brownfield custom-slot-92 migration safety, and an AI-ControlTower/OpenViking boundary where the external index is `DERIVED_ONLY` and rebuildable. Project relation topology never transfers repository/workspace/binding/integration/implementation/runtime authority. Generic extension space is now `93–99`.

## Framework 1.3.1 Project Upgrade Command Semantics

Framework `1.3.1` adds registered `[Project Upgrade]` while keeping Schema `1.0.0` and existing slots/Stable-ID/state families unchanged. The command fresh-resolves the active local Framework pin as current Project authority and canonical upstream as target evidence, then reports `UP_TO_DATE | UPGRADE_AVAILABLE | SOURCE_DIVERGENCE | VERIFICATION_REQUIRED`. A verified difference asks whether the user wants to prepare an upgrade; “yes” starts cumulative assessment/Preview only and does not authorize Project mutation. Existing Direct-to-Latest `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`, preservation, rollback, explicit mutation approval, and final verification semantics remain unchanged.

## Framework 1.3 Command & Direct-to-Latest Upgrade Semantics

Framework `1.3.0` keeps Schema `1.0.0` and existing semantic slots/Stable-ID families while adding registered bracketed `[Project Status]` / `[Project Path]` commands, Markdown-safe mandatory response-close presentation, and cumulative current→target upgrades. Brackets are required; registered command-name matching is case-insensitive. Command discovery lists only registered commands. `[Project Status]` fresh-observes Project/Task/Git/verification/blocker state and keeps Task count distinct from Git changes. `[Project Path]` treats angle-bracket placeholders as unset and adds no location mutation authority.

Initialized Projects remain locally pinned. An approved upgrade compares current reconstructable truth directly with the selected target, classifies `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`, preserves Stable IDs/current truth/Project-specific rules/bindings/history, and does not mechanically execute every intermediate release. Affected verification is proportional and one `RELEASE_FULL` is run on the final unchanged candidate. The maintained starter remains the current NEW-Project representation, not a default destructive rebuild mechanism.

## Framework 1.2.6 Bootstrap Location & File Storage Semantics

Framework `1.2.6` keeps Schema `1.0.0` and existing Stable-ID/state families. A Project-specific Bootstrap Location Block supplies Framework Source, Remote Location, optional File Storage Location(s), MCP Location, Local Workspace, and `DYNAMIC / VERIFY_EACH_SESSION` current branch/worktree intent before authority resolves. It is not a second root; active `FRAMEWORK-001` remains initialized-Project authority.

Generic `file_storage_locations` in active `FRAMEWORK-001` govern non-Drive S3/NAS/SMB/NFS/SharePoint/object/file/filesystem scopes by content ownership. Dedicated `google_drive` remains canonical for Drive and must not be duplicated generically. `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED` and `VERIFIED | USER_CONFIRMED | VERIFICATION_REQUIRED` are reused; unresolved/absent storage never authorizes fallback. File Storage does not automatically become Local Workspace, Canonical Implementation Source, or Runtime/Persistent-State authority. Existing Projects remain pinned; migration invents no provider applicability.

## Framework 1.2.5 Agent Continuity, Progressive Verification & Local Workspace Semantics

Framework `1.2.5` keeps Schema `1.0.0` and existing Stable-ID families while adding:

- environment-scoped **Local Workspace Binding** under active `FRAMEWORK-001`, reusing `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED`;
- local/MCP routing that fails closed when the environment/path is unresolved; MCP/tool workspace IDs remain evidence only;
- **Verified Task Completion Checkpoint** for Material Git-backed Tasks: affected verification PASS + durable observed completion commit before `DONE`; read-only Tasks need no synthetic commit; `WIP commit ≠ DONE`; `commit ≠ push`;
- progressive verification: Task-level affected/risk checks, Logical Checkpoint continuity integrity, one `RELEASE_FULL` per unchanged completed candidate, and `INTEGRATION_GATE` evidence validity/Base Freshness;
- state-bound verification evidence reuse with selective invalidation;
- lightweight **Response Close Completeness Gate** before every governed assistant response emit.

Repository Location Binding, Local Workspace Binding, current branch/worktree, Canonical Integration Target, Canonical Implementation Source, and Runtime Location remain semantically distinct. Existing Projects remain locally pinned and do not auto-upgrade.

## Framework 1.2.4 Project Location Binding & Chat Closure Semantics

Framework `1.2.4` adds a durable **Project Location Binding** in active local `FRAMEWORK-001` for GitHub/Google Drive routing while keeping Schema `1.0.0` and all Stable-ID families unchanged.

- GitHub and Drive independently use `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED`.
- `VERIFICATION_REQUIRED` is fail-closed for Material mutation; `NOT_APPLICABLE` blocks Material Project work through that connector.
- `BOUND` requires durable routing identity, not chat memory, recent activity, display path, or search ranking.
- Persistent binding changes require User Explicit Approval plus governed `FRAMEWORK-001` revision/promotion; one-off exact-target instructions do not rewrite the persistent binding.
- Repository binding remains distinct from current branch/worktree, Canonical Integration Target, and Canonical Implementation Source; no new branch authority is introduced.
- `09 Handoff` references the root binding and preserves source-native GitHub/Drive pointers rather than duplicating authoritative content.
- Chat Closure Consistency requires `ไม่มีขั้นตอนถัดไป → START_NEW_CHAT`; `CONTINUE_CURRENT_CHAT` requires one concrete Next Action; `PERSISTENCE_PENDING` requires `CONTINUE_CURRENT_CHAT` plus a persistence/recovery action.
- Mandatory response-close display uses `[Next Action]:`, `[Chat]:`, `[Reason]:`, `[Required Read]:` as separate Markdown paragraphs.

Existing initialized Projects remain locally pinned and do not auto-upgrade.
## Framework 1.2.3 Development Workspace & Runtime Authority Semantics

Framework `1.2.3` adds the missing governance boundary between **Canonical Implementation Source** and **Runtime Truth** without changing semantic slots, Stable-ID families, or Schema `1.0.0`.

When material:

- `40 Technical Design` captures a **Development Workspace Contract**: canonical source identity, workspace type/location/durability, Human/Agent edit location, execution environment, Source-to-Runtime Mapping, dependency isolation, Runtime Mutability Boundary, and Persistent-State Boundary;
- runtime-only code/config mutation does not silently become canonical Implementation Truth;
- material source/runtime mismatch that should align reuses `DRIFT-*`;
- `60 Deployment Plan` captures source/artifact acquisition, source-to-runtime mapping, runtime mutability, persistent-state/data authority, replacement/recreation expectation, and material development/production differences;
- state required to survive expected runtime replacement needs a declared persistent authority/mechanism, while rebuildable cache/temp state may remain ephemeral;
- durable Dev Container, remote, VM, host Git, and Git-worktree source topologies can all be valid; physical host-folder source and Docker are not universal requirements;
- production source mounts and image/artifact deployment are evaluated by the Project contract rather than blanket rules.

Framework `1.2.3` does **not** replace Framework `1.2.2` Git Base Freshness. Existing `STACKED_WORK`, `BASE_STALE`, `REBASE_REQUIRED`, `FORWARD_PORT_REQUIRED`, and Pre-Merge Base Freshness semantics remain authoritative.

## Framework 1.2.2 Git Base Freshness Semantics

Framework `1.2.2` adds **Git Base Freshness and Forward-Port** governance without changing semantic slots or Schema `1.0.0`. Independent branch/worktree work begins from a freshly verified canonical integration target; feature-on-feature ancestry is explicit `STACKED_WORK`; semantic base drift uses `BASE_STALE` / `FORWARD_PORT_REQUIRED`; and the current target head is rechecked before acceptance/merge. `Mergeable ≠ Acceptable`.

The complete binding contract is carried by Core Governance and the full root `00` template. The mockup starter points to those semantics rather than duplicating them.

## Framework 1.2.1 Continuation Semantics

Framework `1.2.1` adds **Externalized Working Memory and Chat Lifecycle** governance without changing the semantic-slot namespace or Schema `1.0.0`. Material connector/MCP work persists at logical checkpoints to source-native durable state; transient reads/searches do not require persistence by default. `PERSISTENCE_PENDING` blocks a safe `START_NEW_CHAT` recommendation until continuation state is durable outside Chat.

## Core Slot Map

| Slot | Document | Applicability | Distribution starter |
|---|---|---|---|
| `00` | Project Source Framework | **MANDATORY / NON-REMOVABLE ROOT** | `00-Project-Source-Framework.template.md` |
| `01` | Project Source Index | **MANDATORY** | `01-Project-Source-Index.template.md` |
| `02` | Project Overview | **MANDATORY** | `02-Project-Overview.template.md` |
| `03` | Current State | **MANDATORY** | `03-Current-State.template.md` |
| `04` | Decision Log | **MANDATORY** | `04-Decision-Log.template.md` |
| `05` | Requirements | **MANDATORY** | `05-Requirements.template.md` |
| `06` | Architecture | **CONDITIONAL** | `06-Architecture.template.md` |
| `07` | Implementation Plan | **CONDITIONAL** | `07-Implementation-Plan.template.md` |
| `08` | Open Issues | **CONDITIONAL** | `08-Open-Issues.template.md` |
| `09` | Handoff | **MANDATORY** | `09-Handoff.template.md` |
| `10` | Change Log | **MANDATORY** | `10-Change-Log.template.md` |
| `11` | Actor Registry | **MANDATORY** | `11-Actor-Registry.template.md` |
| `12` | Authorization Registry | **MANDATORY** | `12-Authorization-Registry.template.md` |
| `13` | Evidence Registry | **MANDATORY** | `13-Evidence-Registry.template.md` |
| `14` | Project Source Manifest | **MANDATORY** | `14-Project-Source-Manifest.template.md` |
| `15` | Action Registry | **MANDATORY** | `15-Action-Registry.template.md` |
| `16` | Migration Registry | **MANDATORY** | `16-Migration-Registry.template.md` |
| `17` | Secret Reference Registry | **MANDATORY** | `17-Secret-Reference-Registry.template.md` |

## Standard Extended Starters

| Slot | Document | Applicability | Distribution starter |
|---|---|---|---|
| `40` | Technical Design | **CONDITIONAL** | `40-Technical-Design.template.md` |
| `60` | Deployment Plan | **CONDITIONAL** | `60-Deployment-Plan.template.md` |
| `91` | Project Management Control | **CONDITIONAL / STANDARD IN 1.2.0+** | `91-Project-Management-Control.template.md` |
| `92` | Project Graph | **CONDITIONAL / STANDARD IN 1.6.0+** | `92-Project-Graph.template.md` |

`91` canonically owns `RISK-* / ASM-* / MS-* / OUT-* / DEP-* / CR-* / GATE-*`. `92` canonically owns current `REL-*` Project-relation assertions when active.

## Reserved and Extended Taxonomy

| Range | Meaning | Bootstrap behavior |
|---|---|---|
| `18–19` | RESERVED | **DO NOT CREATE** default/active files |
| `20–29` | Research / Discovery | Create only when needed |
| `30–39` | Business / Process / UX Design | Create only when needed |
| `40–49` | Architecture / Technical / Integration | `40` standardized conditional; others when needed |
| `50–59` | Testing / QA / Validation | Create only when needed |
| `60–69` | Deployment / Operations / Infrastructure | `60` standardized conditional; others when needed |
| `70–79` | Data / Migration / Analytics | Create only when needed |
| `80–89` | Audit / Review / Assessment / Reports | Create only when needed |
| `90` | General / Special Governance Extension anchor | Create only when needed |
| `91` | Project Management Control | Standard conditional in `1.2.0+` |
| `92` | Project Graph | Standard conditional in `1.6.0+` |
| `93–99` | Project-specific / Governance Extension | Create only when needed |

## GREENFIELD Bootstrap Recipe

```text
1. Start from canonical Framework repository `main`; vendor ChatGPT/Claude instructions are optional discovery adapters when applicable
2. Read repository README.md on canonical main
3. Read ../../FRAMEWORK-RELEASE.yaml
4. Read SKILL.md + latest amendment + Core Governance
5. Read `../PROJECT-BOOTSTRAP.md`, 00 template, and core-document-skeletons.md
6. Read this mockup mapping
7. Read `../project-location-bootstrap.md` when Project/environment bootstrap configuration is being prepared; resolve Framework Source / Remote / Local / MCP / File Storage locators read-only as applicable
8. Preview proposed Project Source plus resulting root `PROJECT-BOOTSTRAP.md`, including governed GitHub/Drive/local-workspace/generic-file-storage states/identities → obtain explicit user approval
9. Create active 00 first with the approved Project Location Binding
10. Create mandatory 01–05 and 09–17
11. Evaluate 06–08, 40, 60, 91, 92; create only when applicable
12. Keep 18–19 reserved
13. Use 93–99 only for real Project-specific/governance-extension needs
14. Build/verify Index + Manifest + readiness
15. Materialize `<Project-Root>/PROJECT-BOOTSTRAP.md` from the maintained template
16. Create/update exactly one consuming README `PROJECTFRAMEWORK-BOOTSTRAP` managed block; preserve content outside markers and fail closed on duplicate/malformed markers
17. Verify Project Settings/README → `PROJECT-BOOTSTRAP.md → 00 → 01 → 03` plus `09` continuation routing
18. Pin Framework/Schema locally; do not auto-upgrade later
19. After durable verification declare Core Installation DONE and emit `Project Settings — Required User Handoff` with fixed upstream + verified absolute Project Bootstrap path
20. Optionally record exact Git provenance only when actually observed/material
```

When Git branch/worktree integration is later used inside an initialized Project, apply the locally pinned root `00` Base Freshness contract. Upstream Framework movement does not auto-upgrade that Project.

When implementation/workspace/runtime mapping is material, route the deep blueprint to `40`, deployment/recreation behavior to `60`, and any expected-alignment mismatch to existing `DRIFT-*` semantics.

## Framework 1.2.0 Management and Technical Routing

```text
03 → Project Health + Review Cadence
04 → Decision Revalidation
08 → KNOWLEDGE_DEBT through ISS-*
11 → Responsibility Mapping; Responsibility ≠ Authority
40 → Tech Stack / source / workspace / config / runtime / Source-Docker technical blueprint
60 → Source/Docker installation / source-runtime mapping / persistence-recreation / verification / operations
91 → Risk / Assumption / Milestone / Outcome / Dependency / Change Request / Gate
```

`SOURCE_AND_DOCKER` uses one declared application/configuration/data/security/persistence contract. Intentional variance is explicit; unexpected mismatch is DRIFT.

## Concept-First Boundary

Tech Stack/install/Docker/workspace/persistence planning does not authorize source code, Dockerfile/Compose, scripts, CI, or automation. Concrete commands belong only to a real Project when verified as Project truth.

## Template vs Active Filename

Do not copy `.template.md` names verbatim into active Project Source. Active governed files use revision + timestamp naming, e.g. `40-Technical Design-r001-YYMMDD-HHMM.md`.

Template placeholders are not Project facts. Replace them only with verified/user-confirmed values or explicit uncertainty.

## Brownfield Slot 91 Safety

A pre-1.2.0 Project may already use slot `91`. Never overwrite it. Use `MIG-*`, preserve identity/history/references, relocate only with approval, then activate standard `91` if applicable. Old prose is not automatically promoted into new management Stable IDs.

Framework `1.12.0` optional Project Execution Profile: when applicable, `Project-Execution/` is a governed root-level policy surface outside Project Source slots. TASK-027 `tools.md` declares eligible execution tools/fallback/failure behavior only after active Project authority resolves; Tool policy ≠ Location ≠ Authority and Brownfield never auto-adopts. No credentials or runtime router are created.

Framework `1.12.0` Agent / Model Capability Profile: optional `Project-Execution/capabilities.md` constrains required reasoning/coding/research/review/council capability and local/external/review eligibility after authority resolution. Capability ≠ Authority; Brownfield never infers policy from prior model use and no model router/runtime is created.

Framework `1.12.0` Release / Publication Contract: current reporting keeps Implementation/Integration/Repository Publication/Release/Artifact Publication/Deployment orthogonal; Task DONE ≠ MERGED ≠ PUSHED ≠ RELEASED. RC evidence is state-bound; RELEASE_FULL verifies candidates and INTEGRATION_GATE checks mutable targets. Publication authority remains separate and no CI/CD is created.

## Framework 1.12.0 Set 1 Foundation Semantics

Set 1 adds explicit Task dependency/readiness metadata, optional `Project-Execution/tools.md` + `capabilities.md` + `trust.md`, and orthogonal release/publication dimensions. These policies remain outside Project Source authority; capability/tool/trust/publication state never grants authority. Brownfield adoption is governed and no runtime router/scheduler/CI/security engine is implied.
