# TASK-041 — Portable Installation Bootstrap & Project Settings Handoff Design

**Status:** USER_APPROVED_ARCHITECTURAL_DESIGN / WRITTEN_SPEC_PENDING_USER_REVIEW
**Target:** Project Source Framework `1.9.0` / Schema `1.0.0`
**Scope:** Documentation/governance contract only; no installer runtime, CLI, watcher, daemon, UI automation, or secret storage
**Source:** User-approved design dialogue on 2026-08-31, Sections 1–3

## 1. Problem

ProjectFramework can already bootstrap a GREENFIELD Project into a local `Project-Source/` plus root `PROJECT-BOOTSTRAP.md`, but the post-install user experience remains incomplete and vendor-coupled:

1. after Project Source creation, the Agent does not have a canonical requirement to return one copy-ready Project Settings block containing the actual Project bootstrap path;
2. current Project Settings launchers expose five bootstrap/location fields and duplicate a large shared governance contract even though active local `FRAMEWORK-001` becomes authoritative after initialization;
3. a consuming Project does not have a mandatory managed `README.md` fallback block that lets a new Agent discover `./PROJECT-BOOTSTRAP.md` when vendor Project Settings are missing, stale, unsupported, or inaccessible;
4. upstream `README.md` names the response-close fields but does not display the complete mandatory response-close pattern required to reconstruct the contract from upstream documentation alone.

The result is avoidable friction when moving among GPT, Claude, Hermes, Codex, or another Agent and when cloning/moving a Project to another environment.

## 2. Goals

TASK-041 defines a vendor-neutral installation-completion and bootstrap-adapter contract that:

- keeps `https://github.com/captainhuke-dev/ProjectFramework` as the fixed Framework upstream locator;
- makes the consuming Project's verified absolute `PROJECT-BOOTSTRAP.md` path the second Project Settings locator;
- reduces Project Settings to a thin two-binding bootstrap adapter rather than a duplicate governance root;
- makes a managed relative bootstrap block in consuming `README.md` the portable fallback;
- preserves active `00 / FRAMEWORK-001` as Project governance authority;
- preserves existing Git/Drive/File Storage/MCP/Local Workspace semantics internally without exposing all of them as mandatory Project Settings fields;
- requires every successful GREENFIELD installation to return a resolved copy-ready Project Settings block to the user;
- documents the exact mandatory response-close format in upstream `README.md`;
- keeps existing initialized Projects pinned and non-destructively migratable through `[Project Upgrade]` only.

## 3. Non-Goals

TASK-041 does **not**:

- clone the ProjectFramework repository into every consuming Project;
- make the ProjectFramework upstream repository the consuming Project repository;
- create a new semantic slot, Stable-ID family, authority family, or lifecycle family;
- create `PROJECT_SETTINGS_*` lifecycle states;
- remove Project Location Binding or Bootstrap Location semantics from Core Governance;
- grant branch, integration, implementation, runtime, Risk, secret, publication, or disclosure authority from a locator;
- automatically edit GPT/Claude/Hermes/other vendor Project Settings through UI automation;
- build an installer executable, CLI, bot, hook, CI/CD workflow, watcher, scheduler, daemon, or runtime bootstrap service;
- auto-upgrade Brownfield Projects or rewrite their README/Project Settings outside governed upgrade/adoption.

## 4. Authority Model

The authority chain remains:

```text
Project Settings / Project Instructions
        = discovery adapter only
                |
                v
<Project-Root>/README.md managed fallback
        = discovery fallback only
                |
                v
<Project-Root>/PROJECT-BOOTSTRAP.md
        = Project-root locator only
                |
                v
Project-Source/00 / FRAMEWORK-001
        = Project governance authority
                |
                v
01 -> 03 -> task-specific routing -> 09 when continuation applies
```

The following separations are binding:

```text
ProjectFramework Upstream != Project Repository
ProjectFramework Upstream != Project authority
Project Bootstrap          != Project authority
README fallback            != Project authority
Project Settings           != Project authority
active FRAMEWORK-001       = Project governance authority
```

A correct locator grants no `AUTH-*`, Risk acceptance, branch/integration, implementation, runtime, publication, destructive-operation, secret, or external-disclosure authority.

## 5. Canonical Two-Binding Project Settings Contract

After successful installation, the Agent MUST generate the following user-facing Project Settings block with a verified absolute Project Bootstrap path:

```text
ProjectFramework Upstream: https://github.com/captainhuke-dev/ProjectFramework
Project Bootstrap: <VERIFIED_ABSOLUTE_PROJECT_ROOT>/PROJECT-BOOTSTRAP.md

ProjectFramework Bootstrap Rule:
Read Project Bootstrap before Material Project work.
If Project Bootstrap cannot be resolved, use the Project README managed bootstrap block as fallback.
ProjectFramework Upstream is for Framework discovery/upgrade only; it never replaces local Project Source authority.
```

### 5.1 ProjectFramework Upstream

Canonical value:

```text
https://github.com/captainhuke-dev/ProjectFramework
```

Its permitted role is limited to:

- GREENFIELD Framework source read-through;
- current release/descriptor discovery;
- `[Project Upgrade]` upstream target resolution;
- migration-notes and target Framework source lookup.

It is not the consuming Project's repository binding, Git remote, Project Source, Canonical Integration Target, Canonical Implementation Source, Runtime Location, or authority.

### 5.2 Project Bootstrap

The value supplied to Project Settings MUST be the actual verified absolute path in the installation environment, for example:

```text
D:\Projects\MyNewApp\PROJECT-BOOTSTRAP.md
/Users/example/Projects/MyNewApp/PROJECT-BOOTSTRAP.md
```

The Agent MUST NOT emit an unresolved placeholder as if it were ready to paste. If the absolute Project root cannot be verified, report `VERIFICATION_REQUIRED`; do not fabricate a path.

### 5.3 Placement

The block may be inserted anywhere in the vendor's Project Settings / Project Instructions surface. ProjectFramework does not require a specific UI position. Vendor-specific UI wording is not Framework authority.

## 6. Thin Vendor Launchers

Current maintained ChatGPT and Claude launcher artifacts transition from full duplicated governance payloads to thin wrappers of the canonical two-binding contract.

The target launcher responsibilities are only to:

1. expose `ProjectFramework Upstream`;
2. expose `Project Bootstrap`;
3. instruct the Agent to read the Project Bootstrap before Material Project work;
4. point to consuming `README.md` fallback when the absolute path is unusable;
5. preserve the authority boundary: upstream and adapter never override active local `FRAMEWORK-001`.

GPT, Claude, Hermes, Codex, or another Agent may use the same generic thin block. A vendor-specific launcher is an optional convenience adapter, not a separate governance copy.

Existing full launchers remain historical/compatible inputs for already initialized Projects and are not silently replaced. Brownfield replacement is upgrade/adoption work.

## 7. Internal Bootstrap Location Semantics Remain

`templates/project-location-bootstrap.md` remains the canonical pre-authority location/discovery reference, but its roles are split conceptually:

```text
User-facing Project Settings bootstrap
--------------------------------------
ProjectFramework Upstream
Project Bootstrap

Internal/pre-authority discovery semantics
------------------------------------------
framework_source
remote_location
file_storage_locations
mcp_location
local_workspace
current_branch_worktree = DYNAMIC / VERIFY_EACH_SESSION
```

Git/Drive/File Storage/MCP/Local Workspace semantics are not deleted. They remain available for discovery, Preview, Project Location Binding construction, diagnostics, and `[Project Path]`. They are simply no longer all required as vendor Project Settings fields.

## 8. Consuming Project README Managed Fallback

Every GREENFIELD Project adopting this contract MUST end installation with a root `README.md` containing exactly one valid managed bootstrap block:

```md
<!-- PROJECTFRAMEWORK-BOOTSTRAP:START -->
## ProjectFramework Bootstrap

ProjectFramework Upstream:
https://github.com/captainhuke-dev/ProjectFramework

Project Bootstrap:
./PROJECT-BOOTSTRAP.md

AI / Agent:
Read `PROJECT-BOOTSTRAP.md` before Material Project work.
<!-- PROJECTFRAMEWORK-BOOTSTRAP:END -->
```

The consuming README uses a relative Project Bootstrap path for portability across clones and moved workspaces.

### 8.1 Ownership Boundary

ProjectFramework owns only the bytes inside the managed marker pair. Content outside the markers belongs to the consuming Project and MUST NOT be rewritten merely to maintain bootstrap metadata.

### 8.2 Mutation Rules

| README state | GREENFIELD / governed upgrade behavior |
|---|---|
| no `README.md` | create `README.md` containing the managed block |
| README exists, no managed block | append the managed block while preserving existing content |
| exactly one valid managed block | update only the managed body when required |
| duplicate START/END pairs | fail closed; require repair before automatic rewrite |
| missing/malformed marker pair | fail closed; require repair before automatic rewrite |
| content outside managed markers | preserve byte-for-byte unless separately authorized Project work changes it |

Do not choose a canonical block by recency, position, similarity, or search ranking when markers are ambiguous.

## 9. Upstream README Canonical Documentation

The canonical upstream `README.md` MUST document enough of this contract that an Agent starting only from the repository URL can reconstruct the governed GREENFIELD installation path without chat memory.

At minimum upstream README covers:

- the distinction between installing ProjectFramework governance and cloning the ProjectFramework repository;
- GREENFIELD detection and read-only canonical source discovery;
- Preview -> explicit approval -> Material Project Source creation;
- two-binding Project Settings output;
- consuming README managed fallback;
- authority chain and failure boundaries;
- Brownfield `[Project Upgrade]` behavior;
- exact mandatory response-close format.

## 10. Mandatory Response-Close Pattern in Upstream README

Upstream `README.md` MUST display the complete canonical pattern:

```text
Every response MUST end with:

### ทำอะไรไป?

### และถัดไปคืออะไร?

**[Next Action]:** <one exact next action or ไม่มีขั้นตอนถัดไป>

**[Chat]:** CONTINUE_CURRENT_CHAT | START_NEW_CHAT

**[Reason]:** <concise reason>

**[Required Read]:** <canonical locations or ไม่มี>

Separate paragraphs; tokens unescaped.
```

It MUST also preserve the lifecycle coupling:

```text
ไม่มีขั้นตอนถัดไป -> START_NEW_CHAT
CONTINUE_CURRENT_CHAT -> concrete Next Action required
PERSISTENCE_PENDING -> CONTINUE_CURRENT_CHAT + concrete persistence/recovery action
nothing after Required Read
```

The consuming Project README does not duplicate this full response contract. After bootstrap resolution, the locally pinned Project governance owns response behavior.

## 11. Exact GREENFIELD Installation Algorithm

When a user requests installation of `captainhuke-dev/ProjectFramework` into the current Project, the Agent executes:

### Phase A — Classify and discover

1. Inspect the current Project root read-only.
2. Check for root `PROJECT-BOOTSTRAP.md` and valid active local `FRAMEWORK-001`.
3. If active Project Source already exists, do not use GREENFIELD creation; route to initialized-Project / `[Project Upgrade]` semantics.
4. For genuine GREENFIELD, use canonical upstream `https://github.com/captainhuke-dev/ProjectFramework` and fresh `main` as the discovery start.
5. Read in order: upstream `README.md` -> `FRAMEWORK-RELEASE.yaml` -> `SKILL.md` -> latest amendment -> Core Governance -> `templates/PROJECT-BOOTSTRAP.md` -> root Framework template -> skeletons -> mockup README -> project-location bootstrap.
6. Resolve the actual Project root and applicable environment/location evidence without inventing authority from recent workspaces, MCP IDs, mounts, or lookalikes.

### Phase B — Preview and approval

7. Present one GREENFIELD Preview covering Project identity, target Framework/Schema, Project Source root, local workspace, repository/Drive/File Storage applicability and proposed binding state, root bootstrap, README managed fallback, conditional documents, and verification plan.
8. Obtain explicit user approval for the resulting creation scope.
9. Do not ask for redundant per-file Framework approval after the approved Preview unless scope materially changes or a higher-level gate applies.

### Phase C — Materialize

10. Create active `00 / FRAMEWORK-001` first with approved Project identity and Location Binding.
11. Create mandatory `01–05` and `09–17`.
12. Evaluate `06–08`, `40`, `60`, `91`, and `92`; create only when applicable.
13. Keep `18–19` reserved.
14. Materialize root `PROJECT-BOOTSTRAP.md` from the maintained template and route it to the actual active files.
15. Create/update the consuming README managed block.
16. Pin imported Framework/Schema locally.
17. Do not create standing Goal, `AUTH-*`, `ENV-*`, Meeting, disclosure permission, provider credential, secret value, runtime, Git repository, or external storage merely because Framework installation occurred.

### Phase D — Verify and complete core installation

18. Verify `PROJECT-BOOTSTRAP.md -> active 00 -> 01 -> 03`, plus `09` continuation routing.
19. Verify Project UUID consistency, active Index/Manifest, mandatory/conditional/reserved slots, binding values, Framework/Schema pin, managed README marker integrity, and absence of secret values.
20. For Git-backed Material creation, satisfy existing Verified Task Completion Checkpoint requirements including an observed completion commit. For a genuinely non-Git Project, do not initialize Git merely to manufacture a completion commit.
21. Once durable resulting state and required verification pass, declare **Core Installation DONE**.

### Phase E — Mandatory user handoff

22. Resolve the actual verified absolute `PROJECT-BOOTSTRAP.md` path.
23. Emit a `Project Settings — Required User Handoff` section containing the exact copy-ready thin block.
24. State that the block may be inserted anywhere in the applicable Project Settings/Instructions surface.
25. State that core installation is already complete and that Project Settings is a discovery adapter, not authority.
26. Do not claim the external vendor settings were modified unless that modification was independently executed and verified.

## 12. Installation Completion vs Project Settings Handoff

Core installation completion and vendor adapter installation are separate facts.

Core installation is DONE when the local Project Source, root bootstrap, README fallback, and verification are durable. User copy/paste into Project Settings is a required **handoff output**, not a prerequisite to core Project Source completion.

Do not create a new lifecycle/state family such as `PROJECT_SETTINGS_HANDOFF_REQUIRED`.

When useful, `03`/`09` may describe:

```text
Project Settings Adapter: user handoff generated; confirmation not observed
```

Formal `ACT-*` tracking is optional and applicability-driven; GREENFIELD does not create one merely to track a copy/paste step.

## 13. Required Post-Install Response Content

Before the mandatory Framework response close, a successful installation response includes:

```text
Installation Result
- Framework / Schema
- active FRAMEWORK-001 path
- Project Bootstrap absolute path
- README fallback state
- verification result

Project Settings — Required User Handoff
- resolved copy-ready two-binding Thin Bootstrap Block

Authority Note
- Core installation is complete
- Project Settings is discovery only
- active FRAMEWORK-001 is Project governance authority
```

The Project Bootstrap line MUST contain the verified absolute path, not a placeholder.

## 14. Bootstrap Resolution Algorithm for Future Agents

A future Agent resolves bootstrap in this order:

```text
1. Applicable Project Settings has resolvable Project Bootstrap
   -> read it

2. Project Settings missing/unusable
   -> inspect root README managed block
   -> resolve ./PROJECT-BOOTSTRAP.md

3. PROJECT-BOOTSTRAP.md resolves
   -> validate active FRAMEWORK-001
   -> active local Project Source governs

4. Neither Settings nor README fallback resolves safely
   -> stop affected Material Project work
   -> report bootstrap repair requirement
```

Never choose a Project through chat memory, recent/active editor workspace, MCP workspace ID, mounted path, search result ordering, or similar name.

## 15. Failure and Contradiction Handling

- **Upstream unreadable during GREENFIELD:** stop affected governance mutation; do not reconstruct Framework from memory.
- **Existing valid active Project Source:** do not overwrite through GREENFIELD installation; use initialized-Project semantics.
- **Absolute Project Bootstrap path unresolved:** report `VERIFICATION_REQUIRED`; do not emit a fake ready-to-paste path.
- **README managed markers duplicate/malformed:** fail closed for automatic marker rewrite and offer governed repair.
- **Project Settings absolute path stale after clone/move:** fallback through root README relative path when the Project root is available; do not treat the stale absolute path as binding authority.
- **Settings/README/bootstrap/root contradiction:** inspect enough read-only evidence to diagnose; active valid `FRAMEWORK-001` remains authority after resolution, while affected Material mutation fails closed until the contradiction is safely reconciled.
- **New environment workspace differs from bound workspace:** README fallback may find the Project, but Local Workspace Binding still follows normal Root Governance verification/change semantics; discovery never silently rewrites binding.

## 16. Brownfield and Upgrade Behavior

Existing initialized Projects remain pinned and do not receive this contract automatically.

On governed `[Project Upgrade]` to a Framework release containing TASK-041:

1. preserve active local truth, bindings, Stable IDs, history, and Project-specific rules;
2. assess adopting the thin vendor adapter and consuming README managed fallback;
3. Preview README managed-block creation/update and root-bootstrap effects;
4. obtain applicable mutation approval;
5. update only governed local Project Source/root/bootstrap/managed README surfaces;
6. generate a refreshed absolute Project Settings block for the user;
7. do not claim external vendor settings were changed unless actually executed and verified;
8. preserve historical full launchers/specs/evidence as provenance.

The migration is direct-to-latest and does not require replaying every intermediate release.

## 17. Compatibility and Release Classification

TASK-041 is a **minor Framework interface evolution** targeting Framework `1.9.0` while keeping Project Source Schema `1.0.0`.

Rationale:

- no semantic slot changes;
- no Stable-ID family changes;
- no Project Source object-schema expansion required;
- authority model is preserved;
- new GREENFIELD installation/adapter behavior is materially user-visible;
- maintained launchers and README/bootstrap flows change;
- Brownfield remains explicit upgrade/adoption rather than silent rewrite.

Existing Framework `1.8.0` Projects remain valid and locally authoritative until upgraded.

## 18. Affected Framework Surfaces

Expected implementation surfaces include, subject to implementation-plan refinement:

- `README.md` — canonical installation flow, two-binding handoff, managed fallback, full response-close pattern;
- `Framework-Source/FRAMEWORK-RELEASE.yaml` — target release/latest amendment when implementation reaches release stage;
- new Framework amendment for TASK-041;
- `Framework-Source/SKILL.md` — installation/handoff semantics;
- `Framework-Source/references/core-governance-rules.md` — normative bootstrap/adapter/README contract;
- `Framework-Source/templates/PROJECT-BOOTSTRAP.md` — fallback relationship and authority boundary as needed;
- `Framework-Source/templates/project-location-bootstrap.md` — two-binding user-facing layer plus retained internal location semantics;
- `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md` and `CLAUDE-PROJECT-INSTRUCTIONS.md` — thin vendor launchers;
- `Framework-Source/templates/00-project-source-framework.md` — GREENFIELD resulting-state contract;
- `Framework-Source/templates/core-document-skeletons.md` — 03/09 descriptive handoff guidance where needed;
- `Framework-Source/templates/project-source-mockup/README.md` — GREENFIELD recipe;
- maintained mockup surfaces affected by README/root-bootstrap representation;
- `Framework-Source/MIGRATION-NOTES.md` — Brownfield adoption guidance;
- `Framework-Source/tests/pressure-scenarios.md` — scenarios covering installation, fallback, path, marker, authority, and response-close behavior;
- `docs/superpowers/PROJECT-TASKS.md` — TASK-041 lifecycle/evidence.

Historical amendments/specs/plans/evidence are not globally rewritten.

## 19. Verification Contract

Implementation acceptance MUST demonstrate at least:

1. GREENFIELD install creates/updates the consuming README managed block.
2. Existing README content outside managed markers is preserved.
3. No README causes a valid README + managed block to be created.
4. Duplicate/malformed markers fail closed rather than being guessed.
5. Project Settings output contains exact upstream URL and verified absolute Project Bootstrap path.
6. Placeholder/unresolved Project Bootstrap path is never presented as ready-to-paste.
7. Project Settings may be missing while bootstrap still succeeds through consuming README.
8. A stale absolute adapter path after clone/move may fall back through relative root README without rewriting authority.
9. Upstream is used for Framework discovery/upgrade and never inferred as the consuming Project repository.
10. `PROJECT-BOOTSTRAP.md` remains locator-only; active `FRAMEWORK-001` remains authority.
11. Internal Git/Drive/File Storage/MCP/Local Workspace semantics remain available despite the two-binding vendor interface.
12. ChatGPT and Claude thin launcher semantics remain equivalent.
13. Generic Hermes/other-Agent instructions can use the same thin block without a new governance copy.
14. upstream README contains the exact mandatory response-close pattern and lifecycle coupling.
15. consuming README remains thin and does not duplicate full governance.
16. GREENFIELD unreadable upstream stops mutation rather than using memory.
17. Existing active Project Source prevents destructive GREENFIELD recreation.
18. Brownfield does not auto-adopt thin launchers/README mutation outside `[Project Upgrade]`.
19. installation does not synthesize Goal/OUT/AUTH/ENV/Meeting/disclosure/secret/runtime objects.
20. no new runtime/CLI/bot/hook/CI/watcher/scheduler/daemon is introduced.
21. launcher size/parity requirements applicable to the target release pass.
22. `git diff --check` passes.
23. affected verification passes before Task completion.
24. one final `RELEASE_FULL` passes on the unchanged release candidate with state-bound evidence.

## 20. Security and Secret Boundary

Neither Project Settings, consuming README, `PROJECT-BOOTSTRAP.md`, nor installation handoff may contain passwords, tokens, API keys, secret-bearing URLs, or actual secret values. Use canonical `SECRET-*` references only where otherwise applicable and authorized.

The fixed upstream URL and local Project Bootstrap path are routing information, not credentials and not disclosure authority.

## 21. Design Decisions Approved by User

The user explicitly approved the following architectural choices on 2026-08-31:

1. **Fallback location = both upstream and consuming README (Choice C).** Upstream README is canonical installation documentation; every adopting consuming Project has a thin managed README bootstrap fallback.
2. **Existing consuming README behavior = managed markers (Choice 1).** Create README when absent; otherwise append/update only the managed marker block and preserve all other Project content.
3. **Path strategy = environment-specific Project Settings + portable README (Choice C).** Project Settings receives a verified absolute `PROJECT-BOOTSTRAP.md` path; README uses `./PROJECT-BOOTSTRAP.md`.
4. **Project Settings interface = Thin Bootstrap Block (Choice A).** Two bindings plus bootstrap rule replace the large duplicated governance launcher as the target interface.
5. **Core install vs vendor handoff = separate facts (Choice A).** Core installation may be DONE before user copy/paste confirmation; the Agent must still emit the handoff block.
6. **Design Section 1 approved.** Installation Completion & Adapter Handoff.
7. **Design Section 2 approved.** Exact GREENFIELD Installation Flow & Post-Install Output Contract.
8. **Design Section 3 approved.** README Canonical Contract, Thin Launchers & Response-Close Propagation.

## 22. Success Criteria

TASK-041 design is successful when implementation can make the following statement true without hidden assumptions:

> A user may open any capable AI Agent in a new Project folder and ask it to install `captainhuke-dev/ProjectFramework`. After one governed GREENFIELD Preview/approval cycle, the resulting Project contains durable local Project Source, root bootstrap, and a portable README fallback. The Agent verifies the result, declares core installation complete, and returns one copy-ready two-binding Project Settings block containing the fixed Framework upstream and the actual absolute Project Bootstrap path. Any future Agent can enter through Project Settings or README fallback, while active local `FRAMEWORK-001` remains the sole Project governance authority.

No implementation begins until the user reviews and approves this written specification, after which a separate implementation plan is required.
