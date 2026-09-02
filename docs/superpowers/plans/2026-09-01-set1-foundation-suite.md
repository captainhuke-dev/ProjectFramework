# Set 1 Foundation Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement TASK-033, TASK-027, TASK-034, TASK-035, and TASK-037 in dependency order as one cumulative Framework 1.12.0 / Schema 1.0.0 local release candidate.

**Architecture:** TASK-033 first defines canonical Task dependency/readiness metadata. TASK-027 then creates the optional `Project-Execution/` policy surface with `tools.md`; TASK-034 adds `capabilities.md`; TASK-035 defines orthogonal publication dimensions; TASK-037 adds `trust.md` and integrates tools/models/releases/trust boundaries. Task-specific RED/GREEN/AFFECTED evidence is captured along the way, but only one final cumulative `RELEASE_FULL` runs on the unchanged Framework 1.12.0 candidate.

**Tech Stack:** Markdown, YAML, Git, Python scratch verification scripts only; no runtime services.

**Specs:**
- `docs/superpowers/specs/2026-09-01-task033-task-dependency-portfolio-design.md`
- `docs/superpowers/specs/2026-09-01-task027-project-tool-execution-profile-design.md`
- `docs/superpowers/specs/2026-09-01-task034-agent-model-capability-profile-design.md`
- `docs/superpowers/specs/2026-09-01-task035-release-publication-contract-design.md`
- `docs/superpowers/specs/2026-09-01-task037-security-trust-boundary-design.md`

## Global Constraints

- Final target is Framework `1.12.0` / Schema `1.0.0` / release format `3`.
- Work is deliberate `STACKED_WORK` on TASK-025 completion `45a0fffc6b9040464bf24de7f6245d70465b0165`; integration order is TASK-025 before Set 1.
- Preserve ProjectFramework local Project Source pin `1.7.0` / Schema `1.0.0`.
- Keep `Project-Execution/` outside Project Source semantic slots; it is governed policy, not Root Governance or mutation authority.
- Preserve `Task dependency metadata ≠ DEP-*`, `Tool policy ≠ Authority/Location`, `Capability ≠ Authority`, and `Trust classification ≠ Authority`.
- Preserve `Task DONE ≠ MERGED ≠ PUSHED ≠ RELEASED ≠ ARTIFACT_PUBLISHED ≠ DEPLOYED` and `commit ≠ push`.
- No scheduler, agent orchestrator, MCP router, model router, provider integration, CI/CD, release bot, package publisher, deployment automation, scanner, sandbox enforcement, policy engine, secret store, or runtime security system.
- Vendor launchers remain unchanged unless a task-specific verifier proves a launcher change is unavoidable; default plan is no launcher expansion.
- Existing initialized Projects remain pinned; Brownfield adoption never invents dependencies, tool policy, model capability, release state, or trust classification.
- Use TDD: pressure scenarios/verifiers before production contract changes.
- Run task-specific AFFECTED checks after each implementation checkpoint.
- Run exactly one final cumulative `RELEASE_FULL` on the frozen unchanged candidate; bind evidence to candidate HEAD/tree/Framework-Source tree.
- Push/publication is excluded from `AUTH-004`.

---

### Task 1: Define Set 1 Regression Contract (RED)

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`
- Scratch: `.worktrees/.set1-scratch/set1_red_verify.py`

**Interfaces:**
- Consumes: current Framework 1.10.0 TASK-025-complete parent state.
- Produces: scenarios `289–338` and structural expectations consumed by Tasks 2–7.

- [ ] **Step 1: Append scenarios 289–338 before production Framework changes**

Use 10 scenarios per Set 1 Task:

```text
289–298 TASK-033: explicit dependencies, no number inference, readiness/lifecycle separation, priority, cycle/unknown, parallelism, DEP-* separation, no scheduler
299–308 TASK-027: PRIMARY/allow/disallow, FALLBACK_NONE, ordered fallback, fail-closed/diagnostic-only, location/authority separation, stale identity, no credentials, Brownfield, no router
309–318 TASK-034: capability classes, FULL/DEGRADED/UNAVAILABLE/UNKNOWN, capability≠authority/tool, local/external, TASK-026, independent review, Meeting, reviewer unavailable, Brownfield, no model router
319–328 TASK-035: orthogonal publication dimensions, commit≠push, RC identity, evidence invalidation, RELEASE_FULL vs INTEGRATION_GATE, partial publication, persistence pending, rollback/retraction/supersession, optional assurance, no CI/CD
329–338 TASK-037: trust classes, privileged semantics, unknown fail-closed, secrets/disclosure, tool/capability composition, repository/artifact/runtime crossing, publication integration, Brownfield, no scanner/policy engine
```

- [ ] **Step 2: Create structural RED verifier**

Assert at least:

```text
Framework 1.12.0 / Schema 1.0.0 / release format 3
latest amendment ends at TASK-037 after GREEN
all five amendments exist
scenarios 1–338 contiguous/unique
Core/SKILL contain each task's canonical vocabulary
Project-Execution templates README/tools/capabilities/trust exist after GREEN
22 Project Source starter stamps at 1.12.0/1.0.0 after GREEN
launchers unchanged from Set 1 parent
```

- [ ] **Step 3: Run RED and confirm expected failure**

Expected: FAIL only because Set 1 contract is absent; scenario numbering itself passes.

- [ ] **Step 4: Run `git diff --check` and commit RED contract**

```text
git add Framework-Source/tests/pressure-scenarios.md
git commit -m "test: define set 1 foundation scenarios"
```

- [ ] **Step 5: Persist Logical Checkpoint**

Update Project Source/Task metadata with RED result and exact next Task 2.

---

### Task 2: Implement TASK-033 Task Dependency & Portfolio Planning

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260901-task033.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`
- Modify: `README.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`

**Interfaces:**
- Produces canonical `depends_on`, `blocks`, `enables`, `parallelizable_with`, `priority`, `readiness` semantics for all remaining Set 1 Tasks.

- [ ] **Step 1: Set release descriptor to Framework 1.12.0 and latest TASK-033 amendment**
- [ ] **Step 2: Implement Task planning contract in amendment/Core/SKILL**

Canonical values:

```text
priority: CRITICAL | HIGH | NORMAL | LOW | UNSET
readiness: READY | WAITING | BLOCKED | UNKNOWN
```

Keep Task lifecycle independent and preserve `DEP-*` in 91.

- [ ] **Step 3: Add explicit dependency metadata to Set 1 Task registry**

```text
TASK-033: readiness READY
TASK-027: depends_on TASK-033
TASK-034: depends_on TASK-027
TASK-035: depends_on TASK-034
TASK-037: depends_on TASK-035; consumes TASK-027/TASK-034
```

- [ ] **Step 4: Run TASK-033 focused verifier and Set 1 structural verifier**

Expected: TASK-033 checks PASS; remaining tasks still RED.

- [ ] **Step 5: Commit and persist checkpoint**

```text
git commit -m "docs: define task dependency planning contract"
```

Mark TASK-033 DONE only after focused verification + observed commit; move TASK-027 to active/READY.

---

### Task 3: Implement TASK-027 Tool / MCP Execution Profile

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260901-task027.md`
- Create: `Framework-Source/templates/project-execution/README.md`
- Create: `Framework-Source/templates/project-execution/tools.md`
- Modify: release latest amendment/Core/SKILL/README/migration/current starter guidance/task metadata

**Interfaces:**
- Consumes TASK-033 dependency metadata.
- Produces shared `Project-Execution/` root + tool policy consumed by TASK-034/TASK-037.

- [ ] **Step 1: Add TASK-027 amendment and advance release latest-amendment pointer**
- [ ] **Step 2: Add `Project-Execution/README.md` and `tools.md` templates**

Template vocabulary must include:

```text
PRIMARY
allowed_tools
disallowed_tools
fallback_mode: NONE | ORDERED_ALLOW_LIST
failure_policy: FAIL_CLOSED | READ_ONLY_DIAGNOSTIC_ONLY
```

- [ ] **Step 3: Propagate authority/location/bootstrap/Brownfield boundaries**
- [ ] **Step 4: Run TASK-027 focused AFFECTED verifier**
- [ ] **Step 5: Commit/checkpoint**

```text
git commit -m "docs: add project tool execution profile"
```

Mark TASK-027 DONE; TASK-034 becomes active/READY.

---

### Task 4: Implement TASK-034 Agent / Model Capability Profile

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260901-task034.md`
- Create: `Framework-Source/templates/project-execution/capabilities.md`
- Modify: release latest pointer/Core/SKILL/README/migration/current starter guidance/task metadata

**Interfaces:**
- Consumes TASK-027 tools profile.
- Produces capability constraints consumed by TASK-037.

- [ ] **Step 1: Add TASK-034 amendment/latest pointer**
- [ ] **Step 2: Add `capabilities.md` template**

Required vocabulary:

```text
REASONING | CODING | RESEARCH | REVIEW | COUNCIL
FULL | DEGRADED | UNAVAILABLE | UNKNOWN
LOCAL_ONLY | LOCAL_OR_EXTERNAL | EXTERNAL_ALLOWED
REQUIRED | OPTIONAL | NOT_REQUIRED independent review
```

- [ ] **Step 3: Propagate TASK-026/TASK-024/tool-profile boundaries**
- [ ] **Step 4: Run TASK-034 focused AFFECTED verifier**
- [ ] **Step 5: Commit/checkpoint**

```text
git commit -m "docs: add agent model capability profile"
```

Mark TASK-034 DONE; TASK-035 becomes active/READY.

---

### Task 5: Implement TASK-035 Release / Publication Contract

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260901-task035.md`
- Modify: release latest pointer/Core/SKILL/README/migration/current starter guidance/task metadata

**Interfaces:**
- Produces publication dimensions and RC/evidence semantics consumed by TASK-037.

- [ ] **Step 1: Add TASK-035 amendment/latest pointer**
- [ ] **Step 2: Implement orthogonal publication dimensions**

```text
Implementation: NOT_DONE | DONE
Integration: NOT_APPLICABLE | NOT_MERGED | MERGED
Repository Publication: NOT_APPLICABLE | NOT_PUSHED | PUSHED
Release: NOT_APPLICABLE | NOT_RELEASED | RELEASED
Artifact Publication: NOT_APPLICABLE | NOT_PUBLISHED | PUBLISHED
Deployment: NOT_APPLICABLE | NOT_DEPLOYED | DEPLOYED
```

- [ ] **Step 3: Implement RC identity, evidence invalidation, RELEASE_FULL/INTEGRATION_GATE, partial publication, PERSISTENCE_PENDING, rollback/retraction/supersession, optional assurance**
- [ ] **Step 4: Run TASK-035 focused AFFECTED verifier**
- [ ] **Step 5: Commit/checkpoint**

```text
git commit -m "docs: define release publication contract"
```

Mark TASK-035 DONE; TASK-037 becomes active/READY.

---

### Task 6: Implement TASK-037 Security & Trust Boundary + Final 1.12.0 Propagation

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260901-task037.md`
- Create: `Framework-Source/templates/project-execution/trust.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml` latest pointer
- Modify: Core/SKILL/README/MIGRATION-NOTES/root/skeleton/mockup/current starter stamps/task metadata

**Interfaces:**
- Consumes tools/capabilities/publication contracts.
- Produces final cumulative Framework 1.12.0 contract.

- [ ] **Step 1: Add TASK-037 amendment/latest pointer**
- [ ] **Step 2: Add `trust.md` template**

Canonical trust classes:

```text
TRUSTED | LIMITED_TRUST | UNTRUSTED | PRIVILEGED | EXTERNAL | UNKNOWN
```

- [ ] **Step 3: Implement crossing rules for data/code/artifact/execution; TASK-026 secrets/disclosure; tool/capability/publication integration; UNKNOWN fail-closed**
- [ ] **Step 4: Add cumulative `1.10.0 → 1.12.0` migration notes and update maintained current starter stamps to 1.12.0/1.0.0**
- [ ] **Step 5: Verify vendor launchers unchanged and historical prior amendments/evidence preserved**
- [ ] **Step 6: Run TASK-037 focused verifier and full structural GREEN**
- [ ] **Step 7: Commit/checkpoint**

```text
git commit -m "docs: complete set 1 trust foundation"
```

Mark TASK-037 implementation complete pending cumulative acceptance.

---

### Task 7: Cumulative Acceptance, Evidence, and Terminal Reconciliation

**Files:**
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Create: `docs/superpowers/evidence/2026-09-01-set1-foundation-suite-release-full.md`
- Revise/promote Project Source `01/03/09/10/12/13/14/15/91`
- Modify: `PROJECT-BOOTSTRAP.md`
- Scratch verification only under `.worktrees/.set1-scratch/`

**Interfaces:**
- Consumes all five completed task implementations.
- Produces frozen Framework 1.12.0 candidate and terminal Set 1 Goal state.

- [ ] **Step 1: Run comprehensive cumulative AFFECTED verifier**

Cover at least:

```text
Framework 1.12.0/schema/format/latest TASK-037 amendment
all five amendments + specs
scenarios 1–338 contiguous/unique
TASK-033 dependency/readiness/priority/cycle/DEP-* contract
TASK-027 tools profile + fail/fallback/authority-location separation
TASK-034 capability/local-external/review/Meeting/disclosure contract
TASK-035 publication dimensions + RC/evidence/integration semantics
TASK-037 trust/crossing/privileged/unknown/secret/disclosure contract
Project-Execution README/tools/capabilities/trust templates
22 Project Source starter stamps 1.12.0/1.0.0
vendor launchers unchanged from Set 1 parent
no runtime/CI/CD/router/scanner/policy-engine artifacts
historical provenance preserved
local Project Source pin 1.7.0/1.0.0
STACKED_WORK parent/integration order preserved
git diff --check on current/non-archive surfaces + byte-preserved archive handling
```

- [ ] **Step 2: Update final task metadata and rerun AFFECTED**
- [ ] **Step 3: Commit final implementation candidate and freeze identities**

Capture exact candidate HEAD, candidate tree, Framework-Source tree, clean working tree.

- [ ] **Step 4: Run exactly one final cumulative RELEASE_FULL on frozen candidate**

Bind verifier to exact candidate identities and require cumulative AFFECTED PASS.

- [ ] **Step 5: Write/commit release evidence**

Record per-task design/RED/GREEN/AFFECTED commits/results, scenario range, template counts, candidate identities, RELEASE_FULL result, STACKED_WORK parent, and `Publication: NOT_PUSHED`.

- [ ] **Step 6: Prepare/validate/promote terminal Project Source**

Set:

```text
TASK-033 DONE
TASK-027 DONE
TASK-034 DONE
TASK-035 DONE
TASK-037 DONE
ACT-014 DONE
OUT-004 ACHIEVED
AUTH-004 TERMINATED
ENV-004 EXPIRED
Execution State READY
Publication NOT_PUSHED
Exact Next Action ไม่มีขั้นตอนถัดไป
Chat START_NEW_CHAT
```

- [ ] **Step 7: Commit terminal lifecycle and fresh final verification**

Verify completion→evidence→candidate chain, Framework-Source tree, current routing, clean worktree, terminal states, preserved STACKED_WORK parent, and remote Set 1 branch absent.

- [ ] **Step 8: Finish branch without publication**

Keep `set1-foundation-suite` worktree/branch intact; do not push/create PR/merge without later explicit publication intent.
