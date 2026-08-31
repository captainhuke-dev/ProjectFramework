---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.8.0"
project_source_framework_version: "1.9.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_APPROVED_TASK_041_DESIGN_AND_GOAL_2026-08-31"
compatibility: "BACKWARD_COMPATIBLE_PORTABLE_INSTALLATION_BOOTSTRAP"
---

# Framework 1.9.0 Amendment — Portable Installation Bootstrap & Project Settings Handoff

Framework `1.9.0` preserves Framework `1.8.0` semantics except where refined here. Project Source Schema remains `1.0.0`; release format remains `3`. No new semantic slot, Stable-ID family, authority family, lifecycle family, or runtime implementation is introduced.

## 1. Canonical Two-Binding Project Settings Contract

The target user-facing Project Settings / Project Instructions adapter contains exactly two bootstrap locators plus one bootstrap rule:

```text
ProjectFramework Upstream: https://github.com/captainhuke-dev/ProjectFramework
Project Bootstrap: <VERIFIED_ABSOLUTE_PROJECT_BOOTSTRAP_PATH>

ProjectFramework Bootstrap Rule:
Read Project Bootstrap before Material Project work.
If Project Bootstrap cannot be resolved, use the Project README managed bootstrap block as fallback.
ProjectFramework Upstream is for Framework discovery/upgrade only; it never replaces local Project Source authority.
```

`ProjectFramework Upstream` is fixed Framework source/discovery input. `Project Bootstrap` is environment-specific and MUST be a verified absolute path before it is presented as ready to paste. Unverified location is `VERIFICATION_REQUIRED`; never fabricate a path from memory, recent/active workspaces, MCP IDs, mounts, search ranking, or similar names.

The adapter may be placed anywhere in a vendor's Project Settings / Project Instructions surface. Vendor UI wording/location is not Framework authority.

## 2. Authority Boundary

The bootstrap chain is:

```text
Project Settings / Project Instructions = discovery adapter only
consuming Project README managed block  = portable discovery fallback only
PROJECT-BOOTSTRAP.md                     = Project-root locator only
active Project-Source/00 / FRAMEWORK-001 = Project governance authority
```

Binding separations remain:

```text
ProjectFramework Upstream ≠ consuming Project repository
ProjectFramework Upstream ≠ Project authority
Project Bootstrap ≠ Project authority
README fallback ≠ Project authority
Project Settings ≠ Project authority
```

Correct discovery grants no `AUTH-*`, Risk acceptance, branch/integration, implementation, runtime, publication, destructive-operation, secret, or external-disclosure authority.

## 3. Thin Vendor Launchers

Current maintained ChatGPT/Claude launcher targets are thin wrappers of the two-binding contract. They MUST NOT duplicate the full Core Governance contract or require the legacy five user-facing path fields as the current Project Settings interface.

Legacy/existing full launchers remain historical/compatible inputs for Projects that are already initialized; they are not silently rewritten by upstream movement. Brownfield adoption uses governed `[Project Upgrade]`.

## 4. Consuming README Managed Fallback

A GREENFIELD Project adopting Framework `1.9.0` MUST finish core installation with a root `README.md` containing exactly one valid managed block:

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

ProjectFramework owns only the bytes inside the marker pair. Existing content outside the pair MUST be preserved when bootstrap maintenance is the only authorized change.

Managed mutation behavior:

```text
README absent                  → create README with managed block
README present / block absent  → append managed block, preserve other content
exactly one valid block        → update only managed body when required
duplicate marker pairs         → fail closed; governed repair required
missing/malformed marker pair  → fail closed; governed repair required
```

Never choose a block by recency, position, similarity, or search ranking when marker ownership is ambiguous.

## 5. GREENFIELD Installation Algorithm

An explicit request to install `captainhuke-dev/ProjectFramework` into a new/current Project is governance-bootstrap intent, not an instruction to make the Framework repository the consuming Project repository.

For genuine GREENFIELD:

```text
fresh canonical upstream main
→ README
→ FRAMEWORK-RELEASE.yaml
→ SKILL.md
→ latest amendment
→ Core Governance
→ PROJECT-BOOTSTRAP template
→ 00 template
→ core skeletons
→ mockup README
→ project-location bootstrap when applicable
→ resolve Project/environment read-only
→ one GREENFIELD Preview
→ explicit user approval
→ create active 00 first
→ mandatory 01–05 + 09–17
→ applicable conditional docs only
→ root PROJECT-BOOTSTRAP.md
→ consuming README managed fallback
→ pin Framework/Schema locally
→ resulting-state verification
→ Core Installation DONE
→ mandatory copy-ready Project Settings user handoff
```

The approved GREENFIELD Preview covers the resulting bounded creation scope. Do not re-prompt separately for ordinary mandatory files already inside that approved scope unless the scope materially changes or a higher-level system/tool/platform gate applies.

If valid active local `FRAMEWORK-001` already exists, GREENFIELD recreation is prohibited. Route to initialized-Project / `[Project Upgrade]` semantics and preserve local pin, Stable IDs, bindings, Project-specific rules, and history.

## 6. Core Installation Completion vs User Handoff

Core Installation is DONE when the durable local Project Source, root `PROJECT-BOOTSTRAP.md`, consuming README managed fallback, and required resulting-state verification are complete. Vendor Project Settings copy/paste confirmation is a separate external fact and is NOT a prerequisite for core Project Source completion.

Every successful GREENFIELD installation MUST nevertheless emit a `Project Settings — Required User Handoff` with the resolved copy-ready two-binding block. Do not claim vendor Project Settings were modified unless that external mutation was independently executed and verified.

Do not create `PROJECT_SETTINGS_HANDOFF_REQUIRED`, `PROJECT_SETTINGS_HANDOFF_DONE`, or another lifecycle/state family. Descriptive `03/09` handoff wording or applicability-driven existing `ACT-*` is sufficient when tracking is useful.

## 7. Future-Agent Bootstrap Resolution

A fresh Agent resolves Project bootstrap in this order:

```text
1. Applicable Project Settings contains a resolvable Project Bootstrap
   → read it
2. Settings missing/unusable
   → inspect root README managed block
   → resolve ./PROJECT-BOOTSTRAP.md
3. root bootstrap resolves
   → validate active FRAMEWORK-001
   → local Project Source governs
4. neither Settings nor README fallback resolves safely
   → stop affected Material Project work
   → report bootstrap repair requirement
```

A stale absolute Project Settings path after clone/move may fall back through the root-relative README block. Successful discovery at a new local path does not silently rewrite Local Workspace Binding; binding reconciliation remains governed Root/Location work.

## 8. Internal Bootstrap Location Semantics Remain

The simplified Project Settings adapter does not remove internal location semantics. `framework_source`, `remote_location`, `file_storage_locations`, `mcp_location`, `local_workspace`, dynamic `current_branch_worktree`, and `[Project Path]` remain available for pre-authority discovery, Preview, binding construction, diagnostics, and verification.

The legacy five labels `Framework Remote Path`, `Git Remote Path`, `Storage Path`, `MCP Path`, and `Workspace Path` are no longer mandatory fields of the target current vendor adapter. Their underlying semantic roles remain governed.

## 9. Brownfield Adoption and Upgrade

Existing initialized Projects remain locally pinned and do not auto-adopt Framework `1.9.0` merely because upstream changes.

Governed `[Project Upgrade]` adoption MUST preserve current truth, Stable IDs, Project-specific rules, bindings, history, authority, and rollback. It may Preview/update applicable local Project Source/root bootstrap/managed README surfaces and MUST regenerate the current environment's absolute copy-ready Project Settings block. It MUST NOT claim external vendor settings were changed without execution evidence.

Historical full launchers/specs/amendments/evidence remain provenance and are not globally rewritten.

## 10. Upstream README Response-Close Documentation

The canonical upstream `README.md` MUST display the complete mandatory Framework response-close pattern, not merely name the fields:

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

Lifecycle coupling remains: `ไม่มีขั้นตอนถัดไป → START_NEW_CHAT`; `CONTINUE_CURRENT_CHAT` requires a concrete Next Action; `PERSISTENCE_PENDING` requires `CONTINUE_CURRENT_CHAT` plus a concrete persistence/recovery action; nothing follows `[Required Read]`.

The consuming Project README remains a thin locator and does not duplicate this full governance contract.

## 11. Security and Non-Goals

Project Settings, README fallback, `PROJECT-BOOTSTRAP.md`, Project Source, plans, evidence, and handoff never store actual secret values. The fixed upstream URL and local bootstrap path are routing information, not credentials or disclosure permission.

Framework `1.9.0` adds no installer executable, parser service, CLI, UI automation, Git hook, bot, CI/CD workflow, watcher, scheduler, daemon, background relay, secret store, new authority state, or automatic vendor-settings writer.

GREENFIELD installation does not synthesize a persistent Goal, standing `AUTH-*`, `ENV-*`, Meeting/provider config, disclosure permission, actual secret values, Git repository, external storage, runtime, or daemon merely because ProjectFramework was installed.

## 12. Verification Boundary

Affected verification and one final unchanged-candidate `RELEASE_FULL` MUST prove the two-binding adapter, README marker integrity/content-preservation rules, future-agent fallback, absolute-path failure behavior, retained internal location semantics, thin-launcher parity, upstream response-close documentation, Brownfield safety, scenario coverage, historical integrity, schema/slot stability, and no-runtime/no-secret expansion.
