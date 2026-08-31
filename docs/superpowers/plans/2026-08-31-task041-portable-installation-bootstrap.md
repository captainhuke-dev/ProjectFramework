# TASK-041 Portable Installation Bootstrap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Release Project Source Framework `1.9.0` with a vendor-neutral two-binding Project Settings bootstrap, mandatory consuming-README fallback, deterministic GREENFIELD post-install handoff, and canonical upstream response-close documentation while preserving local `FRAMEWORK-001` authority and existing internal location semantics.

**Architecture:** Project Settings becomes a thin discovery adapter carrying only the fixed ProjectFramework upstream URL plus the verified absolute Project Bootstrap path. Root/consuming `README.md` provides a managed relative fallback to `./PROJECT-BOOTSTRAP.md`, which remains locator-only and resolves active local `FRAMEWORK-001`; the existing Git/Drive/File Storage/MCP/Local Workspace semantics remain internal governance/discovery inputs rather than mandatory vendor-setting fields. Framework `1.9.0` is documentation/governance only: no installer runtime, UI automation, CLI, bot, watcher, scheduler, daemon, or secret storage.

**Tech Stack:** Markdown/YAML governance artifacts; Python structural verification in ignored `.worktrees/.task041-scratch`; Git local commits; no application/runtime dependencies.

**Spec:** `docs/superpowers/specs/2026-08-31-task041-portable-installation-bootstrap-design.md`

## Global Constraints

- Target exactly Framework `1.9.0` / Project Source Schema `1.0.0` / release format `3`.
- Canonical upstream is exactly `https://github.com/captainhuke-dev/ProjectFramework`.
- User-facing Project Settings interface is exactly two bindings: `ProjectFramework Upstream` + verified absolute `Project Bootstrap`, followed by the canonical three-line Bootstrap Rule.
- Consuming README fallback uses exactly one managed `PROJECTFRAMEWORK-BOOTSTRAP:START/END` block and relative `./PROJECT-BOOTSTRAP.md`.
- Managed README maintenance owns only bytes inside its marker pair; duplicate/malformed markers fail closed.
- Active `00 / FRAMEWORK-001` remains Project governance authority; README, Project Settings, upstream, and `PROJECT-BOOTSTRAP.md` are locator/discovery only.
- Existing `remote_location`, `file_storage_locations`, `mcp_location`, `local_workspace`, and dynamic branch/worktree semantics remain available internally.
- GREENFIELD installation remains read canonical source → Preview → explicit approval → active `00` first → mandatory Project Source → root bootstrap/README fallback → verification → core DONE → user Project Settings handoff.
- Core installation DONE is independent from vendor Project Settings copy/paste confirmation.
- Brownfield Projects do not auto-adopt the new adapter/README contract; adoption is governed `[Project Upgrade]` work.
- Never fabricate a ready-to-paste absolute Project Bootstrap path; unresolved path is `VERIFICATION_REQUIRED`.
- No new semantic slot, Stable-ID family, authority family, lifecycle family, `PROJECT_SETTINGS_*` state family, runtime, CLI, UI automation, bot, hook, CI/CD, watcher, scheduler, daemon, or secret storage.
- Actual secret values remain forbidden.
- **Security / Secret boundary:** Project Settings, README fallback, root bootstrap, Project Source, plans, evidence, and logs never store actual secret values; routing paths/URLs are not credentials or disclosure authority.
- Logical Checkpoint persistence failure uses existing `PERSISTENCE_PENDING` semantics with a concrete recovery action; never continue as if durable continuation succeeded.
- Historical amendments/specs/plans/evidence remain provenance and are not globally rewritten.
- Current ProjectFramework local Project Source pin remains `1.7.0 / 1.0.0`; implementing upstream 1.9.0 does not auto-upgrade it.
- Push/publication is outside `AUTH-001`; implementation stops at verified/committed local Task completion unless separately authorized.

---

### Task 1: Establish the TASK-041 RED contract and pressure scenarios

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`
- Create (ignored scratch): `.worktrees/.task041-scratch/task041_red_verify.py`

**Interfaces:**
- Consumes: approved TASK-041 spec and current Framework `1.8.0` surfaces.
- Produces: scenarios `249–268` and a structural verifier that fails before implementation because Framework `1.9.0` portable-bootstrap behavior is absent.

- [ ] **Step 1: Append pressure scenarios 249–268**

Add exact scenario headings covering:

```text
249  Install Request Means Governance Bootstrap, Not Framework Repo Clone
250  Existing Active FRAMEWORK-001 Blocks GREENFIELD Recreation
251  Fixed Framework Upstream Never Becomes Consuming Project Repository
252  One Approved GREENFIELD Preview Covers Resulting Bootstrap Files
253  Post-Install Handoff Emits Exact Two-Binding Block
254  Unverified Absolute Project Bootstrap Path Fails Closed
255  Missing Consuming README Is Created With Managed Fallback
256  Existing README Content Outside Managed Markers Is Preserved
257  Duplicate README Bootstrap Markers Fail Closed
258  Malformed README Bootstrap Markers Fail Closed
259  Stale Absolute Project Settings Path Falls Back Through Relative README
260  README Discovery Never Silently Rewrites Local Workspace Binding
261  Thin ChatGPT/Claude Launchers Carry Only Canonical Bootstrap Adapter
262  Internal Git/Drive/File Storage/MCP/Workspace Semantics Remain Available
263  Upstream README Carries Exact Mandatory Response-Close Pattern
264  Consuming README Remains Thin And Does Not Duplicate Governance
265  Vendor Settings Mutation Is Never Claimed Without Observation
266  Brownfield Does Not Auto-Adopt Thin Adapter Or README Block
267  Installation Does Not Synthesize Goal/Auth/ENV/Meeting/Disclosure/Secrets/Runtime
268  Bootstrap Locator Chain Preserves Active FRAMEWORK-001 Authority
```

Each scenario MUST contain Prompt / Temptation / Pass / Fail / GREEN expectation and preserve scenario numbering continuity.

- [ ] **Step 2: Write the failing structural verifier**

Create ignored scratch verifier with checks equivalent to:

```python
from pathlib import Path
import re

root = Path('.')
read = lambda p: (root / p).read_text(encoding='utf-8')
rel = read('Framework-Source/FRAMEWORK-RELEASE.yaml')
readme = read('README.md')
chat = read('Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md')
claude = read('Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md')
core = read('Framework-Source/references/core-governance-rules.md')
loc = read('Framework-Source/templates/project-location-bootstrap.md')
sc = read('Framework-Source/tests/pressure-scenarios.md')

assert 'framework_version: "1.9.0"' in rel
assert 'ProjectFramework Upstream: https://github.com/captainhuke-dev/ProjectFramework' in chat
assert 'Project Bootstrap:' in chat
assert 'Framework Remote Path:' not in chat
assert '<!-- PROJECTFRAMEWORK-BOOTSTRAP:START -->' in readme
assert 'Every response MUST end with:' in readme
assert '**[Required Read]:** <canonical locations or ไม่มี>' in readme
assert 'remote_location' in loc and 'file_storage_locations' in loc and 'mcp_location' in loc and 'local_workspace' in loc
nums=[int(x) for x in re.findall(r'^## Scenario (\d+) — ', sc, re.M)]
assert nums == list(range(1,269))
```

Add equivalent checks for canonical thin-block wording, managed README mutation rules, core installation vs vendor handoff, authority separation, Brownfield behavior, no runtime scope, launcher parity, and current starter identity.

- [ ] **Step 3: Run RED verifier and observe expected failure**

Run:

```bash
python E:/GitHub/ProjectFramework/.worktrees/.task041-scratch/task041_red_verify.py
```

Expected: FAIL because release identity is still 1.8.0, launchers still expose the old 5-field/full-contract interface, and current upstream README lacks the new managed fallback/full installation contract.

- [ ] **Step 4: Commit pressure scenarios only**

```bash
git add Framework-Source/tests/pressure-scenarios.md
git diff --cached --check
git commit -m "test: define portable bootstrap scenarios"
```

---

### Task 2: Add Framework 1.9.0 release identity and normative portable-bootstrap contract

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260831-task041.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/SKILL.md`
- Modify: `Framework-Source/references/core-governance-rules.md`

**Interfaces:**
- Consumes: scenarios 249–268, approved spec, existing 1.8.0 Goal/Session/Meeting/disclosure semantics.
- Produces: canonical 1.9.0 normative rules used by launchers, README, templates, migration, and verification tasks.

- [ ] **Step 1: Add the 1.9.0 amendment**

The amendment MUST declare:

```yaml
previous_project_source_framework_version: "1.8.0"
project_source_framework_version: "1.9.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_APPROVED_TASK_041_DESIGN_AND_GOAL_2026-08-31"
compatibility: "BACKWARD_COMPATIBLE_PORTABLE_INSTALLATION_BOOTSTRAP"
```

Normative sections must cover exactly:

```text
1. Canonical two-binding Project Settings contract
2. ProjectFramework Upstream role/boundary
3. Verified absolute Project Bootstrap path rule
4. Thin vendor launcher contract
5. Consuming README managed fallback + marker integrity
6. GREENFIELD install algorithm and one Preview/approval cycle
7. Core installation DONE vs required user handoff
8. Future-agent Settings→README→PROJECT-BOOTSTRAP→FRAMEWORK-001 fallback order
9. Internal bootstrap-location semantics retained
10. Brownfield governed adoption through Project Upgrade
11. Upstream README exact response-close documentation
12. No runtime/CLI/UI automation/new state family/secret-value behavior
```

- [ ] **Step 2: Update release descriptor**

Set exactly:

```yaml
framework_version: "1.9.0"
latest_framework_amendment: "references/framework-governance-amendment-260831-task041.md"
```

Keep schema `1.0.0`, release format `3`, canonical repository/branch, entrypoints, and upgrade policy unchanged unless TASK-041 explicitly requires wording alignment.

- [ ] **Step 3: Update Core Governance**

Add/replace current bootstrap/adapter semantics so Core Governance contains the canonical thin block:

```text
ProjectFramework Upstream: https://github.com/captainhuke-dev/ProjectFramework
Project Bootstrap: <VERIFIED_ABSOLUTE_PROJECT_BOOTSTRAP_PATH>

ProjectFramework Bootstrap Rule:
Read Project Bootstrap before Material Project work.
If Project Bootstrap cannot be resolved, use the Project README managed bootstrap block as fallback.
ProjectFramework Upstream is for Framework discovery/upgrade only; it never replaces local Project Source authority.
```

Also define managed README markers and resolution/failure/Brownfield rules from the spec without weakening existing Project Location Binding or `[Project Path]` semantics.

- [ ] **Step 4: Update SKILL current identity/reference/workflow**

Make current distribution exactly `1.9.0 / 1.0.0`, point latest amendment to TASK-041, retain prior amendments as history, and add operational GREENFIELD install/handoff/fallback guidance matching Core Governance.

- [ ] **Step 5: Run RED verifier**

Expected: still FAIL because user-facing launchers/README/templates have not yet been migrated.

- [ ] **Step 6: Run normative consistency checks**

Use a scratch Python check asserting release/SKILL/amendment/Core all agree on 1.9.0, exact upstream URL, two-binding semantics, locator/authority boundary, managed README markers, core-DONE-vs-handoff, and Brownfield behavior.

- [ ] **Step 7: Commit normative contract**

```bash
git add Framework-Source/FRAMEWORK-RELEASE.yaml Framework-Source/SKILL.md Framework-Source/references/core-governance-rules.md Framework-Source/references/framework-governance-amendment-260831-task041.md
git diff --cached --check
git commit -m "docs: define portable installation bootstrap contract"
```

---

### Task 3: Replace vendor launchers with the thin two-binding adapter and preserve internal location semantics

**Files:**
- Modify: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md`
- Modify: `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md`
- Modify: `Framework-Source/templates/project-location-bootstrap.md`
- Modify: `Framework-Source/templates/PROJECT-BOOTSTRAP.md`

**Interfaces:**
- Consumes: normative TASK-041 contract from Task 2.
- Produces: copy-ready thin vendor wrappers, canonical pre-authority internal location reference, and root-bootstrap fallback relationship used by future Agents.

- [ ] **Step 1: Add launcher-specific failing checks to the verifier**

Checks MUST require both launchers to contain exactly the shared semantic body:

```text
ProjectFramework Upstream: https://github.com/captainhuke-dev/ProjectFramework
Project Bootstrap: <PROJECT_BOOTSTRAP_ABSOLUTE_PATH>

ProjectFramework Bootstrap Rule:
Read Project Bootstrap before Material Project work.
If Project Bootstrap cannot be resolved, use the Project README managed bootstrap block as fallback.
ProjectFramework Upstream is for Framework discovery/upgrade only; it never replaces local Project Source authority.
```

and MUST reject mandatory user-facing fields:

```text
Framework Remote Path:
Git Remote Path:
Storage Path:
MCP Path:
Workspace Path:
```

The two maintained launchers must remain semantically equivalent and compact.

- [ ] **Step 2: Rewrite ChatGPT and Claude launchers as thin adapters**

Keep only a short vendor heading/instruction plus the identical shared thin-bootstrap contract. Do not duplicate Core Governance, response-close body, command registry, or location-binding details in the launchers.

- [ ] **Step 3: Split project-location-bootstrap into user-facing vs internal layers**

Top-level Project Settings Representation becomes the two-binding block. Retain the canonical internal representation for:

```text
framework_source
remote_location
file_storage_locations
mcp_location
local_workspace
current_branch_worktree
```

Retain `[Project Path]` verification and no-fallback/no-secret semantics.

- [ ] **Step 4: Update PROJECT-BOOTSTRAP template**

State that the root file is reached primarily through Project Settings and portably through the consuming README managed fallback; preserve locator-only status, active `FRAMEWORK-001` precedence, failure handling, and GREENFIELD/Brownfield rules.

- [ ] **Step 5: Run launcher/location/root tests**

Expected: PASS for launcher parity/two-binding/no-five-fields and retained internal location semantics; overall RED verifier may still fail on upstream README/starter propagation.

- [ ] **Step 6: Commit thin adapter surfaces**

```bash
git add Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md Framework-Source/templates/project-location-bootstrap.md Framework-Source/templates/PROJECT-BOOTSTRAP.md
git diff --cached --check
git commit -m "docs: make project launchers thin bootstrap adapters"
```

---

### Task 4: Implement upstream/consuming README fallback and GREENFIELD starter propagation

**Files:**
- Modify: `README.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: `Framework-Source/templates/project-source-mockup/README.md`
- Modify: all current `Framework-Source/templates/project-source-mockup/*.template.md` frontmatter carrying `project_source_framework_version`

**Interfaces:**
- Consumes: normative contract and thin adapter from Tasks 2–3.
- Produces: canonical upstream installation documentation, exact managed README fallback pattern, exact response-close documentation, and 1.9.0 starter metadata/continuation semantics.

- [ ] **Step 1: Add README/starter failing checks**

Require upstream `README.md` to contain exactly one managed block:

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

Require full canonical response-close documentation:

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

- [ ] **Step 2: Update upstream README installation documentation**

Document: install request ≠ clone Framework repo; GREENFIELD classification/read order; one Preview/approval; local Project Source creation; managed README fallback; resulting verification; core DONE; required Project Settings user handoff; two-binding authority separation; Brownfield upgrade path; exact response-close/lifecycle coupling.

- [ ] **Step 3: Update root Framework template**

Make GREENFIELD resulting state explicitly require root `PROJECT-BOOTSTRAP.md` plus exactly one valid managed consuming README block, verified absolute post-install handoff output, and no auto-created Goal/Auth/ENV/Meeting/disclosure/runtime/secret state.

- [ ] **Step 4: Update core skeletons**

Add concise 03/09 descriptive guidance for Project Settings handoff without introducing a new lifecycle family or mandatory ACT; ensure 14 Manifest can describe root README/bootstrap as external Project-root discovery artifacts without fake semantic slots.

- [ ] **Step 5: Update mockup README GREENFIELD recipe**

Add managed README creation/update and post-install thin-block handoff steps to the canonical recipe; preserve conditional slot rules and concept-first boundary.

- [ ] **Step 6: Bump maintained starter metadata**

For every current mockup/template file containing:

```yaml
project_source_framework_version: "1.8.0"
```

change only the current maintained starter stamp to:

```yaml
project_source_framework_version: "1.9.0"
```

Do not rewrite historical specs/amendments/evidence.

- [ ] **Step 7: Run the structural verifier**

Expected: near-GREEN; remaining failures should be migration/Task lifecycle/release evidence only, not contract behavior.

- [ ] **Step 8: Commit user-facing/starter propagation**

```bash
git add README.md Framework-Source/templates/00-project-source-framework.md Framework-Source/templates/core-document-skeletons.md Framework-Source/templates/project-source-mockup
git diff --cached --check
git commit -m "docs: add portable project readme bootstrap fallback"
```

---

### Task 5: Add Brownfield migration guidance and complete affected verification

**Files:**
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Create (ignored scratch): `.worktrees/.task041-scratch/affected_verify.py`

**Interfaces:**
- Consumes: completed 1.9.0 contract candidate from Tasks 1–4.
- Produces: Direct-to-Latest migration guidance and a comprehensive affected verification result suitable for candidate commit creation.

- [ ] **Step 1: Add migration-notes section `1.8.0 → 1.9.0`**

Document affected surfaces and checklist covering:

```text
thin Project Settings adapter
managed consuming README fallback
absolute Settings path vs relative README path
existing full launcher preservation/history
Root/Binding authority preservation
no automatic vendor UI mutation
no Brownfield auto-adoption
regenerate copy-ready Settings block during governed upgrade
internal location semantics retained
exact response-close documentation
```

- [ ] **Step 2: Update TASK-041 implementation lifecycle**

Set plan path/state to executing, record implementation commits as they become known, and keep Task `IN_PROGRESS` until affected + RELEASE_FULL + evidence + completion reconciliation are durable.

- [ ] **Step 3: Build comprehensive affected verifier**

The verifier MUST cover at least all 24 spec acceptance requirements plus:

```text
Framework/Schema/release-format identity
latest amendment routing
scenario 1–268 continuity/uniqueness
current starter stamps 1.9.0 / schema 1.0.0
mandatory/conditional/reserved slot integrity
thin launcher equivalence and no legacy 5-field interface
exact fixed upstream URL
managed README block uniqueness
README response-close exact tokens/order/lifecycle vocabulary
internal location semantics retained
PROJECT-BOOTSTRAP locator authority boundary
no PROJECT_SETTINGS_* family
no new runtime/code/CI executable artifacts
historical amendment/spec/evidence preservation sentinels
git diff --check
ProjectFramework local Project Source pin still 1.7.0
```

- [ ] **Step 4: Run affected verifier**

Run until exactly all checks PASS. Any semantic failure is fixed in the relevant implementation surface; checker-only defects are corrected only when evidence proves the implementation is already correct.

- [ ] **Step 5: Commit migration + verified implementation candidate**

```bash
git add Framework-Source/MIGRATION-NOTES.md docs/superpowers/PROJECT-TASKS.md
git diff --cached --check
git commit -m "docs: complete portable bootstrap implementation"
```

Record candidate commit/tree/Framework-Source tree after this commit. No Framework contract file may change after state-bound release verification starts.

---

### Task 6: Run one final RELEASE_FULL, persist evidence, and complete TASK-041 locally

**Files:**
- Create: `docs/superpowers/evidence/2026-08-31-task-041-portable-installation-bootstrap-release-full.md`
- Modify through governed revisions: active Project Source `01`, `03`, `09`, `10`, `12`, `13`, `14`, `15`, `91`, plus root `PROJECT-BOOTSTRAP.md` and `docs/superpowers/PROJECT-TASKS.md`
- Create (ignored scratch): `.worktrees/.task041-scratch/release_full.py`

**Interfaces:**
- Consumes: unchanged verified Task-041 implementation candidate and affected verification from Task 5.
- Produces: state-bound release evidence, `ACT-010 DONE`, `OUT-001 ACHIEVED`, terminated Goal authority/envelope, TASK-041 DONE, clean local branch, and no push/publication.

- [ ] **Step 1: Build RELEASE_FULL verifier bound to the candidate**

Capture and assert exact:

```text
candidate HEAD
candidate tree
Framework-Source tree
Framework 1.9.0 / Schema 1.0.0 / release format 3
AFFECTED verifier PASS
all 1–268 scenarios
all current starter stamps
all registered commands and canonical response-close tokens in normative sources
thin launcher semantics
managed README/fallback contract
migration notes
historical integrity
no runtime executable scope
ProjectFramework local pin 1.7.0
git diff --check
clean candidate tree
```

- [ ] **Step 2: Run RELEASE_FULL exactly once on the unchanged candidate**

Expected: all checks PASS. If the candidate changes after this run, invalidate the evidence and rerun on the new unchanged candidate; never reuse mismatched tree evidence.

- [ ] **Step 3: Commit release evidence**

Evidence document records RED observation, affected result, RELEASE_FULL result, candidate/tree identities, Framework-Source tree, scenario range, launcher result, managed README/response-close result, migration/Brownfield result, scope boundary, and `Publication: NOT_PUSHED`.

```bash
git add docs/superpowers/evidence/2026-08-31-task-041-portable-installation-bootstrap-release-full.md
git diff --cached --check
git commit -m "docs: record portable bootstrap release evidence"
```

- [ ] **Step 4: Evaluate Goal success criteria separately from Action completion**

Verify each `OUT-001` success criterion has evidence. Only then set:

```text
ACT-010: DONE
OUT-001: ACHIEVED
AUTH-001: terminal/revoked for future execution because parent outcome achieved
ENV-001: expired/closed with TASK-041 completion
TASK-041: DONE
```

Do not equate `ACT-010 DONE` alone with `OUT-001 ACHIEVED`.

- [ ] **Step 5: Promote completion Project Source revisions**

Use revision → draft validate → promote → archive → postflight. Record release evidence, completion/evidence commits, exact next roadmap action, no publication authorization, and clean/explained working-tree state. `91` remains active as historical/current terminal OUT-001 truth unless a later governed rule makes it inapplicable; do not delete terminal Goal history.

- [ ] **Step 6: Commit lifecycle completion**

```bash
git add PROJECT-BOOTSTRAP.md Project-Source docs/superpowers/PROJECT-TASKS.md
git diff --cached --check
git commit -m "docs: complete task 041 lifecycle"
```

- [ ] **Step 7: Run final post-completion verification**

Freshly verify:

```text
working tree clean
TASK-041 DONE
ACT-010 DONE
OUT-001 ACHIEVED
AUTH-001 no longer permits future work
ENV-001 terminal/expired
release evidence resolves
Framework-Source tree equals RELEASE_FULL evidence tree
ProjectFramework local Project Source pin remains 1.7.0
publication remains NOT_PUSHED
next roadmap action is explicit
```

Stop at the publication boundary. Do not push or create/merge a PR without separate explicit publish intent.
