# TASK-048 `[Project Path]` Workspace & MCP Routing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver ProjectFramework `1.16.0` with a strict `[Project Path]` view that resolves Develop/Production workspace roles, deterministic Local ↔ Remote Durable Develop Workspace relocation, exact MCP Primary/ordered fallback/checkpoint-failback semantics, and an applicability-driven append-only fallback log without collapsing location, implementation, deployment, or authority domains.

**Architecture:** Preserve existing canonical owners instead of creating a new routing authority. `FRAMEWORK-001` keeps repository/environment-scoped Local Workspace binding truth; `40 Technical Design` owns Develop Workspace role/type/location/durability/active-workspace semantics; `60 Deployment Plan` owns applicable production/runtime mapping; `Project-Execution/tools.md` owns exact MCP selection policy; `Project-Execution/fallback-log.md` records actual fallback/recovery incidents. `[Project Path]` becomes the fresh strict read/verification composition over those owners and fails closed only for the affected Material scope when required evidence or owner alignment is unresolved.

**Tech Stack:** Markdown, YAML, Git, ripgrep, Python scratch verification via `uv run python`; no Framework runtime/parser/daemon/router dependency.

**Spec:** `docs/superpowers/specs/2026-09-12-task048-project-path-workspace-mcp-routing-design.md`

## Global Constraints

- Target Framework exactly `1.16.0`; Schema remains `1.0.0`; release format remains `3`.
- Registered command set remains exactly seven commands; TASK-043 Strict Governed Interface and Command Contract Completeness Gate remain intact.
- `[Project Path]` top-level order is exactly `Framework Path → Git Path → Storage Path → Develop Workspace → Production Workspace → MCP Execution → Build / Deployment Mapping → Continuity`.
- `FRAMEWORK-001` / Project Location Binding owns repository and environment-scoped Local Workspace binding/routing only; it must not gain `workspace_role`, `source_mutation`, active Develop Workspace, Canonical Implementation Source, or Production runtime authority.
- `40 Technical Design` / Development Workspace Contract owns Develop Workspace role/type/location/durability, active workspace, Canonical Implementation Source relationship, Human/Agent edit location, and role-compatible source-mutation semantics.
- `60 Deployment Plan` owns applicable deployment/runtime target and build/deployment mapping semantics.
- Develop Workspace may be `LOCAL_WORKSPACE | GIT_WORKTREE | REMOTE_DURABLE_WORKSPACE | OTHER_DECLARED_WORKSPACE`; exactly one active Develop Workspace exists per affected implementation scope unless a separately governed multi-writer design explicitly exists.
- Git Remote such as `origin` is repository synchronization/publication identity, never a Develop Workspace locator by itself.
- Local ↔ Remote Durable relocation preserves required source state, verifies repository/source identity + intended revision + target durability, applies the same checks in both directions, and changes `FRAMEWORK-001` only when an actual persistent Local Workspace Binding delta exists.
- Production direct source mutation is always `FORBIDDEN`; Production correction flows through canonical Develop source → verify/build/package → deploy → runtime verify.
- Production applicability is exact: `APPLICABLE | NOT_APPLICABLE | VERIFICATION_REQUIRED`; absence alone never means `NOT_APPLICABLE`.
- `Project-Execution/tools.md` remains exact selection policy with `primary_tool`, `allowed_tools`, `disallowed_tools`, `fallback_mode`, `fallback_order`, `failure_policy`, new `failback_policy: CHECKPOINT_FAILBACK`, and `review_trigger`.
- `fallback_mode: NONE` means no substitute. `ORDERED_ALLOW_LIST` evaluates only declared fallback entries, in order. Availability/recency/similarity never creates eligibility.
- An MCP/tool is execution-eligible only after applicable reachability/authentication/capability/policy/target-identity checks succeed.
- Unknown mid-action result becomes `RESULT_VERIFICATION_REQUIRED`; never blindly retry a possibly-applied side effect; unprovable result fails closed.
- Material fallback mutation requires the incident record to be durably appendable before the fallback mutation proceeds.
- `Project-Execution/fallback-log.md` is applicability-driven, append-only incident history outside `Project-Source/00–99`, not Root Governance, not authority, not credentials, and not a Stable-ID family.
- `[Project Path]` is read/verify/presentation; correct location/tool status never grants mutation, deployment, push/publication, Root/Binding, secret/disclosure, Decision/Requirement, or runtime privilege.
- Current initialized ProjectFramework Project Source remains pinned to Framework `1.15.0` unless a separate governed `[Project Upgrade]` later adopts `1.16.0`.
- Historical specs/amendments/evidence remain provenance and are not globally rewritten.
- `commit ≠ push`; this plan contains no publication authorization.
- No background MCP watcher, network router, credential store, runtime deployment engine, validator/CLI/parser/interceptor, CI/CD, scheduler, daemon, or automatic provider discovery is introduced.

---

## File Structure Map

**Normative release/command contract**
- Create: `Framework-Source/references/framework-governance-amendment-260912-task048-project-path-workspace-mcp-routing.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`

**Location/workspace/deployment ownership**
- Modify: `Framework-Source/templates/project-location-bootstrap.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: `Framework-Source/templates/project-source-mockup/00-Project-Source-Framework.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/40-Technical-Design.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/60-Deployment-Plan.template.md`

**Project Execution MCP policy/logging**
- Modify: `Framework-Source/templates/project-execution/README.md`
- Modify: `Framework-Source/templates/project-execution/tools.md`
- Create: `Framework-Source/templates/project-execution/fallback-log.md`

**User-facing/migration/current starter propagation**
- Modify: `README.md`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `Framework-Source/templates/project-source-mockup/README.md`
- Modify: all 22 maintained current `Framework-Source/templates/project-source-mockup/*.template.md` version stamps from `1.15.0` to `1.16.0`
- Inspect and modify only if current release identity requires it: `Framework-Source/templates/PROJECT-BOOTSTRAP.md`
- Inspect only; preserve thin-body semantics unless a concrete current-reference change is required: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md`, `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md`
- Do **not** update root `PROJECT-BOOTSTRAP.md` or active `Project-Source/*` merely because Framework distribution advances; those belong to the initialized Project's still-pinned `1.15.0` state.

**Verification/lifecycle**
- Modify first: `Framework-Source/tests/pressure-scenarios.md`
- Scratch only, outside repository: `E:\GitHub\.task048-scratch\verify_task048.py`
- Modify during implementation checkpoints: `docs/superpowers/PROJECT-TASKS.md`
- Create after final verification: `docs/superpowers/evidence/2026-09-12-task-048-project-path-workspace-mcp-routing-release-full.md`

---

### Task 1: Establish the TDD RED contract for TASK-048

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`
- Create outside repository: `E:\GitHub\.task048-scratch\verify_task048.py`

**Interfaces:**
- Consumes: approved TASK-048 spec, current Framework `1.15.0`, existing scenarios `1–432`, existing TASK-027 tool profile and TASK-043 strict-command semantics.
- Produces: scenarios `433–468` plus a deterministic verifier that fails before production semantics change and later drives structural/AFFECTED/RELEASE_FULL checks.

- [ ] **Step 1: Append scenarios 433–468 before editing production contract files**

Use these exact scenario identities and intended behavior:

```text
433 — Develop and Production workspaces both configured and verified
434 — Unverified Develop Workspace blocks source mutation/build
435 — Applicable but unresolved Production target blocks deploy/run mutation
436 — Direct Production source edit is forbidden
437 — ACTIVE eligible Primary MCP executes the action
438 — Primary unavailable + fallback NONE fails closed
439 — Ordered fallback selects first eligible declared entry only
440 — Connected but undeclared MCP is ineligible
441 — Fallback target identity mismatch makes fallback ineligible
442 — Material fallback persists FALLBACK_STARTED before mutation
443 — Fallback-log persistence failure blocks Material fallback mutation
444 — Primary recovery mid-action does not switch before checkpoint completion
445 — Checkpoint failback returns the next action to verified Primary
446 — Unknown mid-action result requires resulting-state verification before retry
447 — Unprovable unknown result fails closed
448 — Fallback-to-next-fallback transition preserves declared order and logs transition
449 — Brownfield workspace classification needs evidence and never infers Production
450 — Brownfield connected/recent MCP does not become fallback automatically
451 — fallback_mode NONE requires no fallback-log materialization
452 — Strict eight-section Project Path survives unavailable evidence
453 — Project Path remains read-only and grants no deploy/root/push authority
454 — TASK-048 introduces no router/watcher/credential/runtime/CLI subsystem
455 — Local to Remote Durable relocation requires checkpoint + identity/revision/durability verification
456 — Remote Durable to Local relocation uses the same checks
457 — Git Remote URL/name is not a Develop Workspace locator
458 — Relocation target repository/revision mismatch cannot be promoted
459 — Required uncommitted implementation state blocks relocation until preserved
460 — Ambiguous multiple active Develop Workspace candidates block Material source mutation
461 — Persistent Local Workspace Binding delta keeps FRAMEWORK-001 approval/revision/promotion flow
462 — Successful relocation routes edit/build/test only to the promoted Develop Workspace
463 — Project Location Binding remains role/mutation-authority free
464 — 40 Technical Design owns active Develop Workspace semantics and owner contradictions fail closed
465 — Explicit no-Production truth renders exact NOT_APPLICABLE Production/deployment sections
466 — Unknown Production applicability renders VERIFICATION_REQUIRED + NOT_VERIFIED
467 — Framework becomes 1.16.0 while Schema stays 1.0.0 and release format stays 3
468 — Seven registered commands + TASK-043/TASK-045 response protocol remain unchanged
```

Each scenario must contain Prompt, Temptation, Pass, Fail, and GREEN expectation blocks consistent with the existing pressure-scenario style.

- [ ] **Step 2: Create the scratch verifier with explicit production-surface assertions**

Create `E:\GitHub\.task048-scratch\verify_task048.py` with this executable structure:

```python
from __future__ import annotations

from pathlib import Path
import re
import sys

MODE = sys.argv[1] if len(sys.argv) > 1 else "structural"
ROOT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(r"E:\GitHub\ProjectFramework")
FS = ROOT / "Framework-Source"


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def must(name: str, condition: bool) -> tuple[str, bool]:
    return name, bool(condition)


def scenario_numbers(text: str) -> list[int]:
    return [int(x) for x in re.findall(r"^## Scenario (\d+)\b", text, flags=re.M)]


def run() -> int:
    core = read("Framework-Source/references/core-governance-rules.md")
    skill = read("Framework-Source/SKILL.md")
    release = read("Framework-Source/FRAMEWORK-RELEASE.yaml")
    scenarios = read("Framework-Source/tests/pressure-scenarios.md")
    loc = read("Framework-Source/templates/project-location-bootstrap.md")
    root_template = read("Framework-Source/templates/00-project-source-framework.md")
    exec_readme = read("Framework-Source/templates/project-execution/README.md")
    tools = read("Framework-Source/templates/project-execution/tools.md")
    tech = read("Framework-Source/templates/project-source-mockup/40-Technical-Design.template.md")
    deploy = read("Framework-Source/templates/project-source-mockup/60-Deployment-Plan.template.md")
    fallback_path = ROOT / "Framework-Source/templates/project-execution/fallback-log.md"
    nums = scenario_numbers(scenarios)
    local_block_match = re.search(
        r"(?ms)^  local_workspaces:\n.*?(?=^  file_storage_locations:)",
        root_template,
    )
    local_block = local_block_match.group(0) if local_block_match else ""
    strict_sections = ["Framework Path", "Git Path", "Storage Path", "Develop Workspace", "Production Workspace", "MCP Execution", "Build / Deployment Mapping", "Continuity"]

    checks = [
        must("scenarios-433-468", all(n in nums for n in range(433, 469))),
        must("scenarios-1-468-contiguous", nums == list(range(1, 469))),
        must("release-1.16", 'framework_version: "1.16.0"' in release),
        must("schema-1.0", 'schema_version: "1.0.0"' in release),
        must("release-format-3", "release_format_version: 3" in release),
        must("project-path-eight-sections", all(x in core for x in [
            "Framework Path", "Git Path", "Storage Path", "Develop Workspace",
            "Production Workspace", "MCP Execution", "Build / Deployment Mapping", "Continuity"
        ])),
        must("strict-order-in-skill", all(x in skill for x in strict_sections)),
        must("location-binding-no-role-authority", bool(local_block) and "workspace_role:" not in local_block and "source_mutation:" not in local_block),
        must("40-owns-development-workspace", "Development Workspace Contract" in tech and "REMOTE_DURABLE_WORKSPACE" in tech),
        must("production-applicability", "VERIFICATION_REQUIRED" in deploy and "NOT_APPLICABLE" in deploy),
        must("tools-checkpoint-failback", 'failback_policy: "CHECKPOINT_FAILBACK"' in tools),
        must("tools-ordered-fallback", 'fallback_mode: "NONE | ORDERED_ALLOW_LIST"' in tools),
        must("fallback-log-created", fallback_path.is_file()),
        must("execution-readme-lists-log", "fallback-log.md" in exec_readme),
        must("project-path-location-command-preserved", "[Project Path]" in loc),
        must("unknown-result-contract", "RESULT_VERIFICATION_REQUIRED" in core and "RESULT_VERIFICATION_REQUIRED" in skill),
        must("no-implicit-fallback", "recency" in core.lower() and "similarity" in core.lower()),
        must("no-runtime-router", "background MCP watcher" in core or "background MCP watcher" in skill),
    ]

    passed = sum(ok for _, ok in checks)
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    print(f"TASK048_{MODE.upper()} {passed}/{len(checks)}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(run())
```

Do not weaken a failing assertion just to obtain GREEN; change production documentation/templates only after the expected RED is observed.

- [ ] **Step 3: Run RED and confirm it fails for missing TASK-048 production semantics**

Run:

```text
uv run python E:\GitHub\.task048-scratch\verify_task048.py red <CURRENT_WORKTREE_ABSOLUTE_PATH>
```

Expected: non-zero exit. Scenario checks pass after Step 1; Framework `1.16.0`, strict eight-section production contract, `failback_policy`, fallback-log template, and other not-yet-implemented assertions fail for the expected reason.

- [ ] **Step 4: Verify scenario numbering is exactly contiguous and unique through 468**

Use the verifier's `scenario_numbers` check and additionally inspect duplicate headings with:

```text
rg -n "^## Scenario (43[3-9]|4[4-5][0-9]|46[0-8])\b" Framework-Source/tests/pressure-scenarios.md
```

Expected: exactly 36 TASK-048 headings, one each for 433–468.

- [ ] **Step 5: Commit RED contract only**

```text
git add Framework-Source/tests/pressure-scenarios.md
git diff --cached --check
git commit -m "test(task048): define project path routing scenarios"
```

---

### Task 2: Implement the normative Framework 1.16 `[Project Path]` and execution-routing contract

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260912-task048-project-path-workspace-mcp-routing.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`

**Interfaces:**
- Consumes: TASK-048 spec + RED scenarios 433–468 + existing TASK-027/TASK-043/TASK-045 contracts.
- Produces: authoritative Framework 1.16 command structure, canonical-owner boundaries, workspace relocation rules, Production applicability, MCP health/fallback/unknown-result/checkpoint-failback semantics, and release identity.

- [ ] **Step 1: Create the cumulative TASK-048 amendment**

The amendment must state all of the following as current Framework `1.16.0` semantics:

```text
Framework 1.16.0 / Schema 1.0.0 / release format 3
[Project Path] exact eight-section order
FRAMEWORK-001 = repository + environment-scoped Local Workspace binding/routing only
40 Technical Design = Develop Workspace semantic owner
60 Deployment Plan = applicable deployment/runtime mapping owner
Project-Execution/tools.md = exact MCP execution-selection owner
Project-Execution/fallback-log.md = append-only actual fallback/recovery history
Git Remote ≠ Develop Workspace
Local ↔ Remote Durable relocation contract
one active Develop Workspace per affected scope
Production direct source mutation FORBIDDEN
Production applicability = APPLICABLE | NOT_APPLICABLE | VERIFICATION_REQUIRED
Primary MCP exact eligibility checks
fallback NONE / ORDERED_ALLOW_LIST only
RESULT_VERIFICATION_REQUIRED before retry when result is unknown
CHECKPOINT_FAILBACK
fallback-log persistence required before Material fallback mutation
[Project Path] read/verify only; no new authority
Brownfield no silent adoption/inference
no runtime router/watcher/credential store/CLI/deployment automation
```

- [ ] **Step 2: Update release descriptor exactly**

Set:

```yaml
release_format_version: 3
framework_version: "1.16.0"
schema_version: "1.0.0"
latest_framework_amendment: "references/framework-governance-amendment-260912-task048-project-path-workspace-mcp-routing.md"
```

Preserve canonical repository/branch, entrypoints, bootstrap policy, upgrade policy, and assurance policy unless a direct TASK-048 requirement proves otherwise.

- [ ] **Step 3: Replace/extend Core Governance `[Project Path]` semantics**

Core must define the exact eight-section order and exact command-facing values from the approved spec. It must also state owner composition and contradiction handling:

```text
FRAMEWORK-001 local binding + 40 workspace contract + 60 deployment mapping + Project-Execution policy + fresh observation
→ compose in [Project Path]
→ MISMATCH / NOT_VERIFIED for affected unresolved dimension
→ fail closed only for Material actions that require that dimension
```

Core must explicitly prohibit putting `workspace_role`, `source_mutation`, active Develop ownership, Canonical Implementation Source, or Production runtime authority into Project Location Binding.

- [ ] **Step 4: Add normative relocation and Production applicability semantics**

Core must include:

```text
LOCAL_WORKSPACE ↔ REMOTE_DURABLE_WORKSPACE
Git Remote is not a workspace
checkpoint/commit required source state before relocation
verify source repository identity + intended revision + target durability
symmetric reverse relocation
40 owns active Develop Workspace promotion/demotion
FRAMEWORK-001 revision flow only when Local Workspace Binding actually changes
APPLICABLE = Production declared; unresolved details NOT_VERIFIED
NOT_APPLICABLE = authoritative no-Production truth
VERIFICATION_REQUIRED = applicability itself unresolved; absence never implies NOT_APPLICABLE
```

- [ ] **Step 5: Add normative MCP health/fallback/failback semantics**

Core must define MCP eligibility as applicable reachability + authentication/session + required capability/tool + allowed policy + bound target identity. It must preserve `Tool selection policy ≠ availability ≠ location ≠ authority`, define `RESULT_VERIFICATION_REQUIRED`, ordered auto fallback, append-before-Material-fallback requirement, and `CHECKPOINT_FAILBACK`.

- [ ] **Step 6: Align SKILL exactly with Core**

Update the `[Project Path]` operational summary, Development Workspace/Runtime section, Project Tool/MCP execution guidance, strict-command behavior, and required-reference routing to the new latest amendment. Preserve the exact seven Registered Commands and TASK-045 visible footer semantics.

- [ ] **Step 7: Run focused verifier after normative implementation**

```text
uv run python E:\GitHub\.task048-scratch\verify_task048.py structural <CURRENT_WORKTREE_ABSOLUTE_PATH>
```

Expected after Task 2: release/Core/SKILL assertions pass; template/fallback-log/propagation assertions may remain failing until Tasks 3–5.

- [ ] **Step 8: Commit normative implementation**

```text
git diff --check
git add Framework-Source/FRAMEWORK-RELEASE.yaml Framework-Source/references/core-governance-rules.md Framework-Source/SKILL.md Framework-Source/references/framework-governance-amendment-260912-task048-project-path-workspace-mcp-routing.md
git diff --cached --check
git commit -m "feat(framework): add project path routing contract"
```

---

### Task 3: Implement canonical workspace ownership, relocation, and Production applicability templates

**Files:**
- Modify: `Framework-Source/templates/project-location-bootstrap.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: `Framework-Source/templates/project-source-mockup/00-Project-Source-Framework.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/40-Technical-Design.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/60-Deployment-Plan.template.md`

**Interfaces:**
- Consumes: Task 2 canonical owner/strict-command contract.
- Produces: starter/template representation that preserves location-vs-workspace-vs-deployment ownership and carries exact relocation/applicability semantics without creating a new Stable-ID family or Root authority.

- [ ] **Step 1: Keep Project Location Binding location-focused**

In root and mockup `00` representations, retain the existing Local Workspace shape:

```yaml
local_workspaces:
  - environment_scope: "<USER_CONFIRMED_ENVIRONMENT_SCOPE>"
    binding_state: "<BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED>"
    canonical_path: "<ABSOLUTE_LOCAL_PATH_OR_UNKNOWN>"
    repository: "<OWNER/REPOSITORY_OR_UNKNOWN_OR_NOT_APPLICABLE>"
    repository_url: "<CANONICAL_REPOSITORY_URL_OR_UNKNOWN_OR_NOT_APPLICABLE>"
    verification_status: "<VERIFIED | USER_CONFIRMED | VERIFICATION_REQUIRED>"
    last_verified_at: "<ISO8601_OR_UNKNOWN>"
```

Do not add `workspace_role`, `source_mutation`, active Develop Workspace, Canonical Implementation Source, or Production runtime fields to this block.

- [ ] **Step 2: Extend `project-location-bootstrap.md` `[Project Path]` read/verify composition**

Document that `[Project Path]` reads:

```text
bootstrap + active FRAMEWORK-001 repository/local bindings
+ applicable active 40 Development Workspace Contract
+ applicable active 60 Deployment Plan
+ applicable Project-Execution/tools.md and fallback-log.md
+ fresh Git/MCP/runtime observations required by the requested dimensions
```

Keep bootstrap placeholders unset/fail-closed and preserve one-off-vs-persistent binding semantics.

- [ ] **Step 3: Materialize the Development Workspace Contract in skeletons/40 starter**

Add an explicit current blueprint with these required concepts when material:

```text
Logical Role: DEVELOPMENT
Workspace Type
Active Workspace Locator
Workspace Durability
Repository / Source Identity
Canonical Implementation Source Relationship
Human / Agent Edit Location
Source-to-Runtime Mapping
Source Mutation Policy: role-compatible only; independent AUTH still required
Relocation State / Prior Active Workspace when a relocation is material
Verification / Drift Notes
```

State that a Local Develop Workspace references the applicable `FRAMEWORK-001` Local Workspace Binding; a Remote Durable workspace may use its own declared durable remote locator in `40` and must not be represented as a Git Remote URL alone.

- [ ] **Step 4: Add exact relocation contract to maintained technical guidance**

The relocation flow must be represented exactly as:

```text
resolve active Develop Workspace
→ checkpoint/commit required source state
→ fresh-observe repository remote + intended source revision
→ prepare/access target durable workspace
→ sync/fetch intended revision
→ verify repository/source identity + revision + durability + working-tree state
→ determine whether 40 only or 40 + FRAMEWORK-001 changes are required
→ update/promote governed 40 workspace contract under applicable authority
→ use Root revision/validation/promotion only for actual persistent Local Workspace Binding delta
→ promote one active Develop Workspace; demote prior active routing
→ verify edit/build/test route to the promoted workspace
```

- [ ] **Step 5: Extend `60 Deployment Plan` with exact Production applicability/mapping**

Add explicit fields/sections that can represent:

```text
Production Applicability: APPLICABLE | NOT_APPLICABLE | VERIFICATION_REQUIRED
Production Runtime Target / Locator
Production Role: DEPLOY / RUN / HEALTH_CHECK / OBSERVE_RUNTIME
Direct Source Mutation: FORBIDDEN
Deployment Source / Artifact Identity
Source-to-Runtime Mapping
Resulting-State / Health Verification
```

If `NOT_APPLICABLE`, do not invent a runtime target. If `VERIFICATION_REQUIRED`, leave affected deployment details unresolved and fail closed only for actions requiring them.

- [ ] **Step 6: Focused ownership check**

Run:

```text
rg -n "workspace_role:|source_mutation:" Framework-Source/templates/00-project-source-framework.md Framework-Source/templates/project-source-mockup/00-Project-Source-Framework.template.md
```

Expected: no hits.

Then run:

```text
rg -n "REMOTE_DURABLE_WORKSPACE|Active Workspace|Production Applicability|NOT_APPLICABLE|VERIFICATION_REQUIRED" Framework-Source/templates/core-document-skeletons.md Framework-Source/templates/project-source-mockup/40-Technical-Design.template.md Framework-Source/templates/project-source-mockup/60-Deployment-Plan.template.md
```

Expected: the new workspace and Production contracts are present.

- [ ] **Step 7: Commit workspace/deployment templates**

```text
git add Framework-Source/templates/project-location-bootstrap.md Framework-Source/templates/00-project-source-framework.md Framework-Source/templates/core-document-skeletons.md Framework-Source/templates/project-source-mockup/00-Project-Source-Framework.template.md Framework-Source/templates/project-source-mockup/40-Technical-Design.template.md Framework-Source/templates/project-source-mockup/60-Deployment-Plan.template.md
git diff --cached --check
git commit -m "docs(framework): define workspace relocation and production applicability"
```

---

### Task 4: Implement Project-Execution ordered fallback, checkpoint failback, and fallback incident template

**Files:**
- Modify: `Framework-Source/templates/project-execution/README.md`
- Modify: `Framework-Source/templates/project-execution/tools.md`
- Create: `Framework-Source/templates/project-execution/fallback-log.md`

**Interfaces:**
- Consumes: Task 2 normative MCP contract.
- Produces: exact optional Project-Execution policy representation and incident-log starter used by `[Project Path]`/Continuity.

- [ ] **Step 1: Extend `tools.md` with exact failback field**

The YAML profile must be exactly compatible with the existing fields and add:

```yaml
failback_policy: "CHECKPOINT_FAILBACK"
```

The rules immediately below must state:

```text
primary_tool is the default when ACTIVE + eligible
fallback NONE = no automatic substitute
ORDERED_ALLOW_LIST = fallback_order only, in order
undeclared tool is never eligible by availability/recency/similarity
DISALLOWED wins
eligibility requires applicable tool availability + policy + target identity
READ_ONLY_DIAGNOSTIC_ONLY never authorizes mutation through an undeclared tool
CHECKPOINT_FAILBACK never switches mid-action
```

- [ ] **Step 2: Extend Project-Execution README with `fallback-log.md` applicability**

The maintained tree becomes:

```text
Project-Execution/
├── README.md
├── tools.md
├── fallback-log.md   # only when ordered fallback is applicable
├── capabilities.md
└── trust.md
```

Explain that `fallback-log.md` is actual incident history rather than selection policy, authority, credentials, or a Stable-ID registry.

- [ ] **Step 3: Create the fallback-log starter with exact append-only record shape**

Use this template body:

````markdown
# MCP Fallback Log

This file is applicability-driven append-only operational incident history. It is not Project Source authority, AUTH, credential storage, or a Stable-ID registry.

## Incident Record

```yaml
incident: "MCP-FB-<YYYYMMDD>-<SEQ>"
timestamp: "<ISO8601_WITH_TIMEZONE>"
event_type: "<FALLBACK_STARTED | FALLBACK_TRANSITION | PRIMARY_RECOVERED | FAILBACK_COMPLETED | INCIDENT_CLOSED | CORRECTION>"
primary_mcp: "<DECLARED_PRIMARY_MCP_ID>"
observed_primary_state: "<ACTIVE | UNAVAILABLE | VERIFICATION_REQUIRED>"
reason: "<CONNECTION_FAILED | AUTH_FAILED | CAPABILITY_UNAVAILABLE | TARGET_MISMATCH | POLICY_DISALLOWED | OTHER_OBSERVED_REASON>"
from_mcp: "<MCP_ID_OR_NONE>"
to_mcp: "<MCP_ID_OR_NONE>"
affected_action: "<BOUNDED_ACTION_DESCRIPTION>"
target_identity_scope: "<VERIFIED_TARGET_OR_SCOPE>"
checkpoint: "<CHECKPOINT_OR_NOT_APPLICABLE>"
result_verification: "<VERIFIED_APPLIED | VERIFIED_NOT_APPLIED | VERIFICATION_REQUIRED | NOT_APPLICABLE>"
recovery_state: "<PRIMARY | FALLBACK_ACTIVE | FAIL_CLOSED>"
failback_policy: "CHECKPOINT_FAILBACK"
failback_at: "<ISO8601_OR_NOT_APPLICABLE>"
incident_state: "<OPEN | CLOSED>"
```

Corrections append a `CORRECTION` event; prior event text is not silently rewritten. Never store passwords, tokens, secret-bearing URLs, or credential material.
````

- [ ] **Step 4: Run focused MCP/template verification**

```text
rg -n "failback_policy|CHECKPOINT_FAILBACK|ORDERED_ALLOW_LIST|fallback-log.md|RESULT_VERIFICATION_REQUIRED|FALLBACK_STARTED|FAILBACK_COMPLETED" Framework-Source/templates/project-execution Framework-Source/SKILL.md Framework-Source/references/core-governance-rules.md
```

Expected: policy, lifecycle and log terms are aligned; no alternate implicit fallback rule appears.

- [ ] **Step 5: Commit Project-Execution changes**

```text
git add Framework-Source/templates/project-execution
git diff --cached --check
git commit -m "docs(framework): add MCP fallback and failback profile"
```

---

### Task 5: Propagate Framework 1.16 to README, migration guidance, maintained starters, and strict command presentation

**Files:**
- Modify: `README.md`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `Framework-Source/templates/project-source-mockup/README.md`
- Modify: all 22 maintained `Framework-Source/templates/project-source-mockup/*.template.md` Framework-version stamps
- Modify if current-release text is present: `Framework-Source/templates/PROJECT-BOOTSTRAP.md`
- Inspect only unless a concrete current-reference delta is required: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md`, `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md`

**Interfaces:**
- Consumes: Tasks 2–4 normative/template state.
- Produces: public migration/install/starter representation of Framework 1.16 without silently upgrading this repository's active Project Source pin.

- [ ] **Step 1: Add README Framework 1.16 `[Project Path]` summary**

README must explain the eight-section command, canonical owners, Local ↔ Remote Durable relocation, Production direct-edit prohibition/applicability, exact Primary/ordered fallback, `CHECKPOINT_FAILBACK`, and fallback log boundary. Keep the seven-command registry unchanged.

- [ ] **Step 2: Add top migration section `1.15.0 → 1.16.0 (current)`**

The section must include:

```text
Framework identity 1.16.0 / Schema 1.0.0 / release format 3
[Project Path] strict interface expands to eight sections
FRAMEWORK-001 location ownership remains narrow
40 Development Workspace Contract gains explicit active Local/Remote Durable workspace semantics
60 Deployment Plan gains explicit Production applicability/mapping representation
Project-Execution/tools.md adds CHECKPOINT_FAILBACK
ordered fallback requires explicit fallback_order; no implicit substitution
fallback-log.md is optional/applicability-driven append-only incident history
Brownfield existing workspace may become Develop only with evidence
Production is never inferred from an existing path
connected/recent tools never become fallback automatically
current initialized Projects remain pinned until governed upgrade
no runtime/router/watcher/CLI/deployment automation
```

The migration checklist must explicitly preserve no-auto-inference and Direct-to-Latest behavior.

- [ ] **Step 3: Update maintained starter Framework stamps**

Change exactly the 22 current files under `Framework-Source/templates/project-source-mockup/*.template.md` from:

```text
project_source_framework_version: "1.15.0"
```

to:

```text
project_source_framework_version: "1.16.0"
```

Keep `project_source_schema_version: "1.0.0"` unchanged.

Also update `Framework-Source/templates/00-project-source-framework.md` and `Framework-Source/templates/core-document-skeletons.md` current Framework stamps where they represent the current maintained distribution.

- [ ] **Step 4: Preserve thin launchers and the initialized Project pin**

Inspect the two vendor launchers. If they contain no duplicated `[Project Path]` body and no hard-coded Framework release that requires update, leave them byte-unchanged. Do not expand them with the eight-section command contract.

Explicitly verify that root `PROJECT-BOOTSTRAP.md` and active `Project-Source/*` still identify the initialized Project's Framework `1.15.0` pin; upstream distribution development does not rewrite them.

- [ ] **Step 5: Run structural GREEN**

```text
uv run python E:\GitHub\.task048-scratch\verify_task048.py structural <CURRENT_WORKTREE_ABSOLUTE_PATH>
```

Expected: all structural checks PASS.

- [ ] **Step 6: Search for stale current `1.15.0` distribution references in maintained Framework starter surfaces**

Search current mutable surfaces only and classify historical references instead of globally replacing them:

```text
rg -n "1\.15\.0|Workspace Path|MCP Path" README.md Framework-Source/FRAMEWORK-RELEASE.yaml Framework-Source/MIGRATION-NOTES.md Framework-Source/SKILL.md Framework-Source/references/core-governance-rules.md Framework-Source/templates
```

Every remaining `1.15.0` hit must be either intentional migration/history text or a still-pinned consuming-Project statement; no current Framework 1.16 starter stamp may remain at 1.15.

- [ ] **Step 7: Commit propagation**

```text
git add -- README.md Framework-Source/MIGRATION-NOTES.md Framework-Source/templates/00-project-source-framework.md Framework-Source/templates/core-document-skeletons.md Framework-Source/templates/project-source-mockup/README.md Framework-Source/templates/project-source-mockup/*.template.md
# If and only if Step 4 produced a justified current-reference edit, add only that exact optional file:
# git add -- Framework-Source/templates/PROJECT-BOOTSTRAP.md
# git add -- Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md
git diff --cached --name-only
git diff --cached --check
git commit -m "docs(framework): propagate project path routing release"
```

---

### Task 6: Run cumulative AFFECTED verification and freeze the final Framework 1.16 candidate

**Files:**
- Modify as corrections only: TASK-048 affected current Framework surfaces.
- Modify: `docs/superpowers/PROJECT-TASKS.md` with implementation/verification state before candidate freeze.
- Scratch-only: `E:\GitHub\.task048-scratch\verify_task048.py`

**Interfaces:**
- Consumes: Tasks 1–5 GREEN state.
- Produces: clean, state-bound final implementation candidate ready for exactly one `RELEASE_FULL`.

- [ ] **Step 1: Expand scratch verifier to AFFECTED mode**

Add exact assertions for:

```text
scenario numbers exactly 1..468 contiguous and unique
Framework 1.16.0 / Schema 1.0.0 / release format 3
latest amendment is TASK-048
seven registered commands unchanged
TASK-043 Command Contract Completeness Gate still precedes TASK-045 response-close gate
[Project Path] eight top-level sections/order aligned across Core/SKILL/location template
FRAMEWORK-001 local_workspaces contains no workspace_role/source_mutation/active-Develop authority
40 starter/skeleton owns active Develop semantics and REMOTE_DURABLE_WORKSPACE
60 starter/skeleton contains exact Production applicability representation
Git Remote explicitly distinct from Remote Durable Develop Workspace
relocation is symmetric and blocks uncommitted/identity/revision/durability uncertainty
Project-Execution/tools has CHECKPOINT_FAILBACK and deterministic ordered fallback
fallback-log template exists, append-only, no secret values, not a Stable-ID family
RESULT_VERIFICATION_REQUIRED before retry for unknown side-effect result
22/22 maintained Project Source starter stamps at 1.16.0 / 1.0.0
README + MIGRATION-NOTES aligned
thin launchers unchanged unless a proven current-reference edit was required
root PROJECT-BOOTSTRAP.md + active Project-Source pin remain 1.15.0
no runtime/code artifact introduced by TASK-048
full branch `git diff --check` against execution base passes
publication remains NOT_AUTHORIZED / NOT_PUSHED
```

- [ ] **Step 2: Run AFFECTED**

```text
uv run python E:\GitHub\.task048-scratch\verify_task048.py affected <CURRENT_WORKTREE_ABSOLUTE_PATH>
```

Expected: PASS all assertions.

- [ ] **Step 3: Fix bounded findings and rerun AFFECTED until PASS**

Any correction changes candidate identity and invalidates prior candidate assumptions. Do not run `RELEASE_FULL` before AFFECTED is clean.

- [ ] **Step 4: Update TASK-048 lifecycle to candidate-ready state**

Record implementation commits, RED result, structural GREEN result, AFFECTED result, scenario range `1–468`, and publication `NOT_AUTHORIZED / NOT_PUSHED`. Do not synthesize a persistent `[Goal]` lineage if none was explicitly created for execution.

- [ ] **Step 5: Freeze candidate commit**

```text
git diff --name-only
# Fail closed if any path is outside the TASK-048 File Structure Map.
# All new TASK-048 files are already tracked by Tasks 1–5, so candidate corrections are tracked-file updates only.
git add -u -- README.md Framework-Source docs/superpowers/PROJECT-TASKS.md
git diff --cached --name-only
git diff --cached --check
git commit -m "chore(task048): freeze framework 1.16 candidate"
git status --short --branch
git rev-parse HEAD
git rev-parse HEAD^{tree}
git rev-parse HEAD:Framework-Source
```

Expected: clean worktree after commit. Record candidate commit/tree/Framework-Source tree for release evidence.

---

### Task 7: Run exactly one RELEASE_FULL, persist evidence, and close local TASK-048 implementation

**Files:**
- Create: `docs/superpowers/evidence/2026-09-12-task-048-project-path-workspace-mcp-routing-release-full.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Modify Project Source lifecycle records only if an explicit persistent Goal/authority lineage was created for TASK-048 execution; otherwise do not invent Goal/OUT/AUTH/ACT/ENV records.

**Interfaces:**
- Consumes: frozen unchanged Task 6 candidate.
- Produces: one state-bound release result, durable local TASK-048 completion evidence, and explicit publication boundary.

- [ ] **Step 1: Confirm the candidate is unchanged before RELEASE_FULL**

```text
git status --short
git rev-parse HEAD
git rev-parse HEAD^{tree}
git rev-parse HEAD:Framework-Source
```

Expected: clean and exact frozen candidate identities from Task 6.

- [ ] **Step 2: Run RELEASE_FULL exactly once on that candidate**

Run the scratch verifier in release mode plus the established release invariants:

```text
uv run python E:\GitHub\.task048-scratch\verify_task048.py release_full <CURRENT_WORKTREE_ABSOLUTE_PATH>
git diff --check <EXECUTION_BASE>...HEAD
```

Release mode must include every AFFECTED assertion, candidate cleanliness/identity, current starter integrity, historical provenance preservation, local Project pin preservation, and no-runtime scope.

Expected: PASS on run 1. Do not rerun an unchanged passing candidate. If it fails, invalidate the candidate, correct the finding, rerun AFFECTED, freeze a new candidate, then run RELEASE_FULL exactly once on the new candidate.

- [ ] **Step 3: Write release evidence**

Evidence must record:

```text
TASK-048
Framework 1.16.0 / Schema 1.0.0 / release format 3
candidate commit / tree / Framework-Source tree
RED result
structural GREEN result
AFFECTED result
RELEASE_FULL result + run count
scenario range 1–468
canonical owner preservation
Local ↔ Remote Durable relocation contract
Production applicability contract
ordered fallback / unknown-result / CHECKPOINT_FAILBACK contract
fallback-log template and secret prohibition
seven-command registry preservation
TASK-043/TASK-045 preservation
22/22 starter stamps
current ProjectFramework local pin still 1.15.0
no runtime expansion
publication NOT_AUTHORIZED / NOT_PUSHED
```

- [ ] **Step 4: Update TASK-048 to local verified completion**

Set `TASK-048` to `DONE` only after the evidence proves every acceptance criterion. Record exact implementation/candidate/evidence commits and `NOT_PUSHED / NOT_AUTHORIZED`. If a persistent Goal was explicitly created for implementation, terminalize only that governed Goal lineage through its normal Project Source lifecycle; if no persistent Goal exists, do not synthesize one after the fact.

- [ ] **Step 5: Commit evidence/lifecycle reconciliation**

```text
git add -- docs/superpowers/evidence/2026-09-12-task-048-project-path-workspace-mcp-routing-release-full.md docs/superpowers/PROJECT-TASKS.md
# If a legitimate TASK-048 Goal lineage exists, inspect `git diff --name-only -- Project-Source` and add only the exact revised successor files for that lineage; never stage the whole Project-Source directory.
git diff --cached --check
git commit -m "docs(evidence): record TASK-048 framework 1.16 release"
```

If `Project-Source` has no legitimate TASK-048 execution-authority lifecycle changes, stage none of it; an empty/synthetic Project Source edit or broad `git add Project-Source` is forbidden.

- [ ] **Step 6: Freshly verify local completion and stop before publication**

```text
git status --short --branch
git log -5 --oneline
rg -n "TASK-048|1\.16\.0|NOT_PUSHED|NOT_AUTHORIZED" docs/superpowers/PROJECT-TASKS.md docs/superpowers/evidence/2026-09-12-task-048-project-path-workspace-mcp-routing-release-full.md
```

Expected: clean worktree, TASK-048 locally DONE with state-bound evidence, no required local result uncommitted, and no push/PR/merge performed.

---

## Plan Self-Review Checklist

Before implementation starts, confirm:

- [x] Every approved spec section 1–25 maps to at least one implementation task above.
- [x] Scenario allocation `433–468` has no collision; baseline `1–432` remains preserved.
- [x] No plan step moves workspace role/mutation semantics into Project Location Binding.
- [x] `40` / `60` ownership and `FRAMEWORK-001` binding ownership stay distinct.
- [x] Local ↔ Remote relocation is symmetric and does not equate Git Remote with workspace identity.
- [x] Production `APPLICABLE | NOT_APPLICABLE | VERIFICATION_REQUIRED` states are represented explicitly.
- [x] MCP fallback uses only declared ordered entries and no similarity/recency substitution.
- [x] Unknown-result verification and checkpoint failback are both covered by RED scenarios + normative + template + verifier tasks.
- [x] Fallback incident logging is required before Material fallback mutation but is not authority/credential/state-family expansion.
- [x] Current Project Source local Framework pin remains 1.15.0 during distribution development.
- [x] No plan step creates runtime/router/watcher/CLI/deployment automation.
- [x] Candidate/evidence staging commands are bounded and do not use broad `git add -A` / `git add Project-Source`.
- [x] Exactly one final `RELEASE_FULL` runs on an unchanged final candidate.
- [x] Publication remains separate and unauthorized unless the Human later grants it explicitly.
