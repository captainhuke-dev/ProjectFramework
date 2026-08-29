# TASK-039 Persistent `[Goal]` Command Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement Framework `1.8.0` `[Goal]` as a persistent, bounded continuous-execution command that resumes across chats without redundant Framework-level approvals while preserving existing authority, risk, location, secret/disclosure, Git, verification, and platform/tool gates.

**Architecture:** `[Goal]` adds no `GOAL-*` family. It composes `OUT-*` in `91` for the desired outcome, `AUTH-*` in `12` for persistent user-granted authority, `ACT-* / ENV-*` in `15` for execution, `09` for continuation pointers with `authority_transfer: false`, `03` for status, and `13/10` for evidence/history. Normal local development is authorized by default unless narrowed; push, destructive operations, Root/Binding mutation, and external disclosure remain opt-in boundaries exactly as specified.

**Tech Stack:** Markdown/YAML governance sources, Python structural verification scripts used only as test runners, Git.

**Spec:** `docs/superpowers/specs/2026-08-29-task039-persistent-goal-command-design.md`

## Global Constraints

- TASK-038 MUST be `DONE` before TASK-039 implementation mutation begins.
- The current Framework distribution root MUST be `Framework-Source/`; do not add new current implementation references to `managing-project-source/`.
- Framework target remains `1.8.0`; Project Source Schema remains `1.0.0`; release format remains `3` unless implementation proves an incompatible schema change and governance explicitly reclassifies it.
- Do not create a `GOAL-*` Stable-ID family or a new semantic slot.
- Persistent Goal outcome is `OUT-*`; persistent authority is `AUTH-*`; execution is `ACT-* / ENV-*`; Handoff only references those objects and keeps `authority_transfer: false`.
- Default persistent Goal authority includes bounded local design/plan/edit/test/fix/verify/commit/checkpoint work unless explicitly narrowed.
- Push is opt-in and requires explicit Goal publish/push intent plus a valid governed target and fresh integration evidence.
- Destructive action is opt-in and requires exact operation + target.
- Root Governance / Project Location Binding mutation is opt-in and requires exact mutation + target plus the normal root revision lifecycle.
- Actual secret values remain forbidden. External AI/provider disclosure is not implicitly authorized by `[Goal]`.
- Higher-level system/developer/product/tool/authentication confirmation requirements remain binding.
- `ACT DONE ≠ OUT ACHIEVED` and Goal achievement requires success-criterion evidence.
- Historical amendments/evidence remain immutable unless they are explicitly current mutable release surfaces.
- Official ChatGPT/Claude shared marker bodies remain byte-identical and each launcher remains within the current `<=4,500` Unicode-character ceiling.
- `commit ≠ push` remains true unless the active Goal explicitly pre-authorizes the push target.

---

### Task 1: Enforce TASK-038 / `Framework-Source/` prerequisite

**Files:**
- Read: `docs/superpowers/PROJECT-TASKS.md`
- Read: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Read: `Framework-Source/SKILL.md`
- Read: `Framework-Source/references/core-governance-rules.md`
- Read: `Project-Source/00-Project-Source-Framework-r001-260829-1707.md`
- Read: `Project-Source/03-Current-State-r001-260829-1707.md`

**Interfaces:**
- Consumes: TASK-038 completed distribution-root migration and active Project Source routing.
- Produces: verified implementation precondition; no mutation if the precondition fails.

- [ ] **Step 1: Fresh-read TASK-038 lifecycle state and distribution root**

Required observed state:

```text
TASK-038 Status: DONE
Current Framework distribution root: Framework-Source/
Framework-Source/FRAMEWORK-RELEASE.yaml: readable
Framework version: 1.8.0
Schema version: 1.0.0
release_format_version: 3
```

- [ ] **Step 2: Fresh-check Git/base state**

Run:

```bash
git status --short --branch
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

Expected: repository identity matches active binding; worktree state is understood; Base Freshness is classified before mutation.

- [ ] **Step 3: Fail closed if prerequisite is not satisfied**

If TASK-038 is not `DONE` or `Framework-Source/` is not the current canonical distribution root, set TASK-039 execution to `BLOCKED_BY_TASK-038`, make no Framework implementation edits, and return to TASK-038. Do not implement against `managing-project-source/`.

- [ ] **Step 4: Commit**

No commit for a read-only successful prerequisite check. If a material blocker must be persisted, update the existing Project Source/Task state using normal governance and commit only that blocker record.

---

### Task 2: Add RED-first `[Goal]` pressure scenarios 181–203

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`

**Interfaces:**
- Consumes: approved TASK-039 spec.
- Produces: executable semantic acceptance contract for all later implementation tasks.

- [ ] **Step 1: Append scenarios 181–203 with unique numbering**

Add exactly these scenario contracts using the repository's existing `Prompt / Pass / Fail / GREEN expectation` format:

```text
181 Goal Brackets Required
182 Goal Matching Is Case-Insensitive
183 Persistent Goal Resumes In New Chat
184 Revoked Or Stale Goal AUTH Blocks Execution
185 Authorized Local Edit And Commit Need No Repeat Approval
186 Push Is Denied By Default
187 Explicit Goal Push Authorization Is Reusable
188 Changed Remote Target Invalidates Goal Push Authority
189 Destructive Operation Is Denied By Default
190 Exact Destructive Operation And Target May Be Pre-Authorized
191 Root Or Binding Mutation Is Denied By Default
192 Explicit Root Or Binding Mutation Still Uses Governed Revision Lifecycle
193 Goal Never Stores Or Reveals Secret Values
194 External AI Disclosure Is Not Implicitly Authorized
195 ENV May Be Derived Narrower Than Goal AUTH
196 ENV Cannot Expand Parent Goal AUTH
197 Partial Blocker Does Not Stop Independent Safe Goal Work
198 Global Blocker Moves Goal To BLOCKED
199 Goal Cancellation Revokes Future Goal Execution
200 Conflicting Active Goals Do Not Resolve By Recency
201 Goal Cannot Rewrite REQ Or DEC To Make Completion Easier
202 All ACT Done Does Not Prove OUT Achieved
203 Higher-Level Tool Confirmation Still Applies
```

Each PASS assertion must encode the corresponding exact design rule; each FAIL assertion must describe the overreach; each GREEN expectation must name the invariant being protected.

- [ ] **Step 2: Verify numbering and RED state**

Run a Python structural check that asserts scenarios `1–203` are unique and contiguous, then assert current normative Framework sources do not yet register `[Goal]` everywhere. The second assertion must fail before implementation and pass only after later tasks.

Example test logic:

```python
from pathlib import Path
import re
p = Path('Framework-Source/tests/pressure-scenarios.md')
t = p.read_text(encoding='utf-8')
nums = [int(x) for x in re.findall(r'^## Scenario (\d+) —', t, re.M)]
assert nums[-23:] == list(range(181, 204))
assert len(nums) == len(set(nums))
```

- [ ] **Step 3: Commit RED contract**

```bash
git add Framework-Source/tests/pressure-scenarios.md
git commit -m "test: define persistent Goal command pressure scenarios"
```

---

### Task 3: Define Framework 1.8 `[Goal]` normative amendment and command contract

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260829-task039.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`

**Interfaces:**
- Consumes: scenarios 181–203 and TASK-039 design.
- Produces: canonical `[Goal]` semantics used by starters, launchers, README, and tests.

- [ ] **Step 1: Create TASK-039 amendment**

The amendment header must use:

```yaml
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.8.0"
project_source_framework_version: "1.8.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_EXPLICIT_CONTINUOUS_APPROVAL_2026-08-29"
compatibility: "BACKWARD_COMPATIBLE_PERSISTENT_GOAL_COMMAND"
```

The amendment body must normatively include:

```text
[Goal] = persistent command, not Agent self-approval
no GOAL-* family
OUT-* = Goal outcome
AUTH-* = persistent Goal authority
ACT-* / ENV-* = execution
09 = continuation reference only; authority_transfer: false
Goal statuses = ACTIVE | BLOCKED | ACHIEVED | CANCELLED | SUPERSEDED
default local development authorization unless user narrows
push opt-in only
exact destructive operation + target opt-in only
exact Root/Binding mutation + target opt-in only
secret-value prohibition
external disclosure separate
partial blocker vs global blocker
cancellation/revocation/supersession
ACT DONE != OUT ACHIEVED
higher-level platform/tool gates remain binding
```

- [ ] **Step 2: Point the release descriptor at the TASK-039 amendment**

Keep:

```yaml
framework_version: "1.8.0"
schema_version: "1.0.0"
release_format_version: 3
```

Change only the current `latest_framework_amendment` pointer to:

```yaml
latest_framework_amendment: "references/framework-governance-amendment-260829-task039.md"
```

Preserve all TASK-038 distribution-root semantics already present.

- [ ] **Step 3: Add `[Goal]` to Core Governance command registry**

Canonical help line:

```text
[Goal] : create/show/change/cancel a persistent outcome and its bounded continuous-execution authorization
```

Normative Core Governance must include the default-local-work rule and each opt-in boundary from the spec. It must explicitly say that a covered Framework-level operation is not re-prompted solely for approval.

- [ ] **Step 4: Add operational `[Goal]` workflow to `SKILL.md`**

The workflow must implement this read/execute order:

```text
[Goal] invocation
→ resolve command intent
→ materialize/resolve OUT-* + AUTH-*
→ derive ACT-* / bounded ENV-*
→ persist 03/09 pointers when material
→ on resume: PROJECT-BOOTSTRAP → 00 → 01 → 03 → 09 → OUT/AUTH/ACT/ENV
→ fresh-check volatile prerequisites
→ continue exact safe next action
→ evaluate OUT success criteria separately from ACT completion
```

- [ ] **Step 5: Run focused structural checks**

Assert `[Goal]`, `OUT-*`, `AUTH-*`, `ACT-*`, `ENV-*`, `authority_transfer: false`, default local authorization, push/destructive/root/disclosure boundaries, and `ACT DONE ≠ OUT ACHIEVED` appear in the normative sources. Assert no current source introduces a canonical `GOAL-*` home.

- [ ] **Step 6: Commit normative contract**

```bash
git add Framework-Source/FRAMEWORK-RELEASE.yaml Framework-Source/references/framework-governance-amendment-260829-task039.md Framework-Source/references/core-governance-rules.md Framework-Source/SKILL.md
git commit -m "docs: define persistent Goal command contract"
```

---

### Task 4: Propagate Goal semantics to Project Source starters

**Files:**
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: `Framework-Source/templates/project-source-mockup/03-Current-State.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/09-Handoff.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/12-Authorization-Registry.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/15-Action-Registry.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/91-Project-Management-Control.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/README.md`
- Modify: maintained starter version stamps where TASK-038 left them on `1.8.0`

**Interfaces:**
- Consumes: normative TASK-039 contract.
- Produces: concrete starter representation for `[Goal]` without active Goal fabrication.

- [ ] **Step 1: Extend root template command semantics**

Add `[Goal]` to the registered command section with the same exact help line and authority boundaries as Core Governance. Do not make an active Goal a default Project-specific rule.

- [ ] **Step 2: Extend `91` OUT semantics**

Add a Goal-specific `OUT-*` subsection that supports:

```text
Outcome Statement
Success Criteria / Success Measure
Evidence Required
Scope
Prohibited Zones
Related AUTH-*
Related ACT-*
Status: ACTIVE | BLOCKED | ACHIEVED | CANCELLED | SUPERSEDED
Terminal Evidence
```

Retain ordinary non-Goal `OUT-*` use; do not redefine all Outcomes as Goals.

- [ ] **Step 3: Extend `12` AUTH semantics**

Add Goal authorization fields and the rule that terminal Goal state terminates/supersedes dependent Goal authorization. State explicitly that Handoff cannot transfer the authorization.

- [ ] **Step 4: Extend `15` ACT/ENV semantics**

Add parent `AUTH-*` / Goal `OUT-*` references for Goal-derived work and require derived `ENV-*` to be equal to or narrower than the parent authorization. Preserve existing `ACT-*` lifecycle and verified completion rules.

- [ ] **Step 5: Extend `03` and `09` continuation/status fields**

`03` Goal view:

```text
Active Goal OUT-*
Goal Status
Success Criteria Progress
Authorization AUTH-* validity
Current/next ACT-*
Boundary inclusion flags
Current blocker
Continuation freshness
```

`09` compact references:

```text
Active Goal: OUT-*
Goal Status
Authorization: AUTH-*
Current Action: ACT-*
Envelope: ENV-* or none
Last Verified Authorization At
Next Safe Action
Goal Blocker when applicable
authority_transfer: false
```

- [ ] **Step 6: Update core skeletons and mockup README**

Document that `91` becomes applicable when `[Goal]` creates a persistent Goal `OUT-*`, but no active Goal/OUT/AUTH is created during GREENFIELD initialization automatically.

- [ ] **Step 7: Run starter consistency checks**

Assert every current starter uses Framework `1.8.0` / Schema `1.0.0`, `18–19` remain RESERVED, no `GOAL-*` family exists, and the Goal field names/lifecycle match the normative amendment exactly.

- [ ] **Step 8: Commit starter propagation**

```bash
git add Framework-Source/templates
git commit -m "docs: propagate persistent Goal semantics to starters"
```

---

### Task 5: Update README, migration notes, and platform launchers

**Files:**
- Modify: `README.md`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md`
- Modify: `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md`

**Interfaces:**
- Consumes: normative command and starter semantics.
- Produces: user-facing discovery, Brownfield migration guidance, compact vendor adapters.

- [ ] **Step 1: Add README `[Goal]` summary**

Explain in plain language:

```text
[Goal] persists an outcome + bounded authority across chats.
Local design/plan/edit/test/fix/commit work is covered by default unless narrowed.
Push/destructive/Root-Binding/external disclosure are not covered unless explicitly included under their exact rules.
A fresh Agent resumes from Project Source; Handoff does not transfer authority.
```

Update command discovery to include `[Goal]` without removing existing commands.

- [ ] **Step 2: Add 1.8.0 migration guidance**

Brownfield rules must state:

```text
Do not synthesize a Goal from old prose, backlog, Handoff, OUT-*, or prior continue messages.
Preserve existing OUT/AUTH/ACT/ENV records.
A persistent Goal exists only after explicit [Goal] adoption/invocation.
No GOAL-* migration exists.
```

- [ ] **Step 3: Compact both platform launchers**

The shared contract must include a concise rule equivalent to:

```text
[Goal] persists OUT/AUTH-backed continuous work across chats; default local dev is pre-authorized unless narrowed; push/destructive/root/disclosure remain explicit opt-ins; Handoff never transfers authority; higher platform/tool gates still apply.
```

Keep canonical `[Project Status]`, `[Project Path]`, `[Project Upgrade]`, `[Session Envelope]`, `[Goal]`, response-close labels, and lifecycle tokens.

- [ ] **Step 4: Verify launcher parity and size**

Run a Python check that extracts `<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:START -->` through `<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:END -->`, asserts byte-identical bodies, and asserts each full launcher length is `<= 4500` Unicode characters.

- [ ] **Step 5: Commit user-facing propagation**

```bash
git add README.md Framework-Source/MIGRATION-NOTES.md Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md
git commit -m "docs: expose persistent Goal command"
```

---

### Task 6: Make all Goal pressure scenarios GREEN and run affected verification

**Files:**
- Verify: all TASK-039 surfaces from Tasks 2–5
- Modify only the exact source responsible for a failing assertion

**Interfaces:**
- Consumes: implemented TASK-039 candidate.
- Produces: affected verification evidence sufficient to proceed to final candidate verification.

- [ ] **Step 1: Run scenarios 181–203 structural/semantic assertions**

Verify every pressure scenario's PASS condition is represented by current normative/starter/launcher semantics.

- [ ] **Step 2: Run repository-wide TASK-039 structural checks**

Minimum assertions:

```text
Framework 1.8.0 / Schema 1.0.0 / format 3
latest amendment = task039
[Goal] on all required current surfaces
no GOAL-* canonical family
OUT/AUTH/ACT/ENV/09 composition aligned
Goal statuses aligned
push/destructive/root/disclosure opt-in boundaries aligned
default local dev authorization aligned
Brownfield no-auto-Goal aligned
launchers byte-identical and <=4500
historical pre-1.8 amendments unchanged
git diff --check PASS
```

- [ ] **Step 3: Fix root cause only**

For each failing assertion, modify the owning canonical surface first and then propagate only required derived/starter copies. Do not patch tests to accept behavior that contradicts the approved spec.

- [ ] **Step 4: Re-run affected verification until PASS**

Record exact pass count and candidate HEAD/tree identity for release evidence.

- [ ] **Step 5: Commit verification fixes if any**

```bash
git add -u
git commit -m "fix: align persistent Goal command contract"
```

Skip this commit if no verification fix was required.

---

### Task 7: Run final RELEASE_FULL and record TASK-039 completion evidence

**Files:**
- Create: `docs/superpowers/evidence/2026-08-29-task-039-persistent-goal-command-release-full.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Modify as applicable: `Project-Source/03-Current-State-r001-260829-1707.md`
- Modify as applicable: `Project-Source/09-Handoff-r001-260829-1707.md`
- Modify as applicable: `Project-Source/10-Change-Log-r001-260829-1707.md`
- Modify as applicable: `Project-Source/13-Evidence-Registry-r001-260829-1707.md`
- Modify as applicable: `Project-Source/15-Action-Registry-r001-260829-1707.md`

**Interfaces:**
- Consumes: unchanged verified TASK-039 candidate.
- Produces: durable completion evidence; no publication claim unless push is separately authorized/observed.

- [ ] **Step 1: Freeze candidate identity**

Observe and record:

```bash
git rev-parse HEAD
git rev-parse HEAD^{tree}
git status --short --branch
```

The working tree must be clean before the final release verification candidate is declared.

- [ ] **Step 2: Run one `RELEASE_FULL` on the unchanged candidate**

Use the current Framework release verifier after TASK-038. It must include scenarios `1–203`, release identity, amendments, Core Governance, SKILL, starters, migration notes, README, launchers, Task state, and historical-integrity checks.

- [ ] **Step 3: Write release evidence**

Evidence must include:

```text
TASK-039 scope
approved design/spec path
implementation-plan path
candidate commit and tree SHA
AFFECTED verification result
RELEASE_FULL result
scenario range 1–203
launcher character counts + shared-body parity
no GOAL-* family
OUT/AUTH/ACT/ENV/Handoff composition
push/destructive/root/disclosure boundary verification
ACT DONE != OUT ACHIEVED verification
historical-integrity result
working-tree state
publication state = NOT_PUSHED unless fresh remote evidence proves otherwise
```

- [ ] **Step 4: Reconcile Task Registry**

Set TASK-039 to `DONE` only when all completion criteria are met and the required completion commit exists. Record design, plan, implementation commits, verification, evidence path, candidate identity, and publication state separately.

- [ ] **Step 5: Refresh Project Source continuation state**

If TASK-039 completion is material to current Project continuation, update `03/09/10/13/15` with pointers/evidence only. Do not duplicate the full Task Registry or Framework amendment payload.

- [ ] **Step 6: Commit completion evidence**

```bash
git add docs/superpowers/evidence/2026-08-29-task-039-persistent-goal-command-release-full.md docs/superpowers/PROJECT-TASKS.md Project-Source
git commit -m "docs: record persistent Goal command release evidence"
```

- [ ] **Step 7: Postflight**

Fresh-observe local HEAD, working-tree state, and `origin/main`. Do not claim push/publication from commit existence. Push only if current user/Goal authority explicitly includes the resolved target and all higher-level gates permit it.
