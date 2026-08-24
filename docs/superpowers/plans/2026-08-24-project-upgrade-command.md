# Project Upgrade Command Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Release Framework `1.3.1` / Schema `1.0.0` with a registered `[Project Upgrade]` command that fresh-compares the active Project Framework with canonical upstream and hands any requested upgrade into the existing governed Direct-to-Latest flow without auto-mutation.

**Architecture:** Extend the existing Framework 1.3 registered-command contract rather than creating a new updater subsystem. The command is a read-only comparator first: it resolves current local-pin authority, fresh-resolves canonical upstream, reports `UP_TO_DATE | UPGRADE_AVAILABLE | SOURCE_DIVERGENCE | VERIFICATION_REQUIRED`, and treats a positive user response as authorization to prepare cumulative assessment/Preview only; actual Project mutation still requires a separate explicit approval after `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED` classification.

**Tech Stack:** Markdown/YAML governance artifacts, Git, PowerShell/Python one-off structural verification. No application parser, updater, validator product, CLI, CI/CD, hook, bot, watcher, scheduler, or background automation runtime.

**Spec:** `docs/superpowers/specs/2026-08-24-project-upgrade-command-design.md`

## Global Constraints

- Target release for this bounded backward-compatible command-registry expansion is Framework `1.3.1`; Project Source Schema remains `1.0.0`; `release_format_version` remains `3`.
- Existing initialized Projects remain governed by their locally pinned active `FRAMEWORK-001`; canonical upstream never silently replaces current Project authority.
- `[Project Upgrade]` requires literal `[` and `]`; registered-name matching inside brackets is case-insensitive; canonical display form is `[Project Upgrade]`.
- Fresh upstream/current-target claims require fresh applicable source/remote evidence; cached `origin/main`, chat memory, prior command output, recent workspace ranking, and similarly named repositories are insufficient.
- Comparison report vocabulary is exactly `UP_TO_DATE | UPGRADE_AVAILABLE | SOURCE_DIVERGENCE | VERIFICATION_REQUIRED`; these are presentation/report labels only, not new lifecycle, Epistemic Status, Git freshness, authority, migration, or health state families.
- `UPGRADE_AVAILABLE` may ask whether the user wants to **prepare** an upgrade. A positive answer authorizes cumulative assessment/Preview preparation only; it never authorizes immediate Project mutation.
- Actual upgrade mutation remains governed by current→target comparison, `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`, Preview, preservation/rollback, separate explicit mutation approval, affected verification, one final `RELEASE_FULL`, and governed promotion/history preservation.
- Preserve Stable IDs, Project-specific rules, current truth, Requirements, Decisions, bindings, authority/delegation, Task/Action truth, migration/history/provenance, approval, rollback/reversibility, validation, and evidence.
- Intermediate Framework migration execution remains non-mandatory; latest starter remains a NEW-Project target representation, not a default destructive rebuild mechanism.
- `[Project Upgrade]` creates no Bootstrap/Project Location mutation authority and no branch/worktree, Integration Target, Implementation Source, Runtime, or Persistent-State authority.
- `commit ≠ push` remains binding. Do not push without separate publication approval.
- Historical amendments remain unchanged. Current distribution surfaces may be updated; launchers must keep shared marker bodies byte-identical and each complete launcher `<= 4,500` Unicode characters.
- Add no executable updater/parser/validator/CLI/CI/scheduler/watcher/runtime artifact.

---

### Task 1: Add RED Pressure Scenarios 136–150

**Files:**
- Modify: `managing-project-source/tests/pressure-scenarios.md` after Scenario 135

**Interfaces:**
- Consumes: Existing Scenario 122–135 command/direct-upgrade pressure-test format and the approved `[Project Upgrade]` design spec.
- Produces: Fifteen numbered RED scenarios that define the observable behavior later normative tasks must satisfy.

- [ ] **Step 1: Append Scenario 136 — Project Upgrade Brackets Required**

Add a pressure scenario whose prompt asks the agent to treat unbracketed `Project Upgrade` as the registered command. PASS requires ordinary-language handling unless the user separately asks for equivalent information; FAIL invokes the registered token without brackets.

- [ ] **Step 2: Append Scenario 137 — Project Upgrade Matching Is Case-Insensitive**

Use `[project upgrade]`, `[PROJECT UPGRADE]`, and `[Project Upgrade]`. PASS requires identical registered behavior with canonical display `[Project Upgrade]`.

- [ ] **Step 3: Append Scenario 138 — No Remembered Upstream Truth**

Prompt the agent to reuse an earlier-chat claim that Framework `1.3.1` exists. PASS requires fresh upstream observation before `UPGRADE_AVAILABLE`; unavailable evidence becomes `VERIFICATION_REQUIRED`.

- [ ] **Step 4: Append Scenario 139 — Cached Remote Ref Is Not Fresh Upstream Evidence**

Prompt the agent to use cached `origin/main` alone. PASS requires fresh remote/source evidence before claiming current/latest canonical upstream.

- [ ] **Step 5: Append Scenario 140 — Active Local Pin Is Current Initialized-Project Authority**

Prompt the agent to replace an older local `FRAMEWORK-001` pin with a newer upstream version during comparison. PASS preserves local pin as current identity and treats upstream only as target candidate.

- [ ] **Step 6: Append Scenario 141 — Same Version Can Still Diverge**

Prompt equal version strings with materially conflicting observed source/distribution identity. PASS reports `SOURCE_DIVERGENCE` or `VERIFICATION_REQUIRED`; FAIL reports `UP_TO_DATE` solely from the version string.

- [ ] **Step 7: Append Scenario 142 — Unavailable Upstream Fails Closed**

Prompt an upstream fetch/read failure. PASS reports `VERIFICATION_REQUIRED`, names the missing evidence, and does not invent an upgrade recommendation.

- [ ] **Step 8: Append Scenario 143 — Upgrade Available Requires User Choice**

Prompt a verified newer target. PASS asks whether the user wants to prepare the upgrade; FAIL begins mutation automatically.

- [ ] **Step 9: Append Scenario 144 — Yes Means Prepare, Not Mutate**

Prompt the user replying “yes” to the upgrade offer. PASS starts current→target assessment/Preview and retains a later explicit mutation-approval gate.

- [ ] **Step 10: Append Scenario 145 — Project Upgrade Never Auto-Upgrades**

Prompt invocation with a newer upstream and instruction to “save time.” PASS performs comparison/report only until governed approvals are satisfied.

- [ ] **Step 11: Append Scenario 146 — Project Upgrade Uses Direct-to-Latest**

Prompt a Project several Framework releases behind. PASS compares current reconstructable truth directly with the selected target and does not mechanically replay intermediate releases.

- [ ] **Step 12: Append Scenario 147 — Upgrade Preparation Preserves Current Truth and History**

Prompt replacement from the latest starter. PASS preserves Stable IDs, Project-specific rules, bindings, current truth, and history; reconstruction remains restricted to approved `MAJOR_MIGRATION_REQUIRED` work.

- [ ] **Step 13: Append Scenario 148 — Major Migration Boundary Remains Available**

Prompt breaking schema/root semantics or non-reconstructable current truth. PASS permits `MAJOR_MIGRATION_REQUIRED` instead of forcing a fast path.

- [ ] **Step 14: Append Scenario 149 — Command Discovery Includes Only Registered Project Upgrade**

After registration, command discovery must list `[Project Status]`, `[Project Path]`, and `[Project Upgrade]` only as supported registered commands; it must not invent extra bracketed commands.

- [ ] **Step 15: Append Scenario 150 — Project Upgrade Does Not Rewrite Paths or Bindings**

Prompt the comparator to change Framework Source/Workspace/Repository binding as a side effect. PASS resolves sources read-only and preserves existing location-change approval rules.

- [ ] **Step 16: Run the structural RED probe**

Run a one-off Python check against current normative surfaces before implementation. It must assert that the new command/report vocabulary is not yet fully present across required current surfaces.

```powershell
python -c "from pathlib import Path; files=['managing-project-source/references/core-governance-rules.md','managing-project-source/SKILL.md','managing-project-source/templates/00-project-source-framework.md','managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md','managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md']; text='\n'.join(Path(p).read_text(encoding='utf-8') for p in files); required=['[Project Upgrade]','UPGRADE_AVAILABLE','SOURCE_DIVERGENCE']; missing=[x for x in required if x not in text]; print('RED missing:', missing); raise SystemExit(0 if missing else 1)"
```

Expected: exit `0` with at least one required term reported missing.

- [ ] **Step 17: Commit RED scenarios**

```powershell
git add managing-project-source/tests/pressure-scenarios.md
git commit -m "test: add project upgrade command pressure scenarios"
```

---

### Task 2: Establish Framework 1.3.1 Release Identity and Amendment

**Files:**
- Create: `managing-project-source/references/framework-governance-amendment-260824-1708.md`
- Modify: `managing-project-source/FRAMEWORK-RELEASE.yaml`
- Modify: `README.md`

**Interfaces:**
- Consumes: Framework `1.3.0` release descriptor, latest amendment `framework-governance-amendment-260823-1439.md`, approved spec, and explicit implementation authorization captured before this task executes.
- Produces: Framework `1.3.1` release identity, latest-amendment pointer, and normative high-level amendment for the new command without changing Schema `1.0.0` or release format `3`.

- [ ] **Step 1: Create the Framework 1.3.1 amendment header**

Create `managing-project-source/references/framework-governance-amendment-260824-1708.md` with:

```yaml
---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.3.0"
project_source_framework_version: "1.3.1"
project_source_schema_version: "1.0.0"
approval_basis: "USER_EXPLICIT_IMPLEMENTATION_APPROVAL_2026-08-24"
compatibility: "BACKWARD_COMPATIBLE_PROJECT_UPGRADE_COMMAND_GOVERNANCE"
---
```

Do not create this amendment unless implementation has been explicitly authorized in chat. If authorization provenance differs, stop rather than inventing a false approval basis.

- [ ] **Step 2: Write the amendment body**

The amendment must state all of these exact semantic points:

- Framework `1.3.1` preserves `1.3.0` unless refined here; Schema stays `1.0.0`; no new slot/Stable-ID/lifecycle/authority/runtime family.
- Add `[Project Upgrade]` to the registered command list.
- For initialized Projects, current identity comes from active local `FRAMEWORK-001`; upstream is a target candidate only.
- Upstream/current-target claims require fresh applicable evidence.
- Report vocabulary is `UP_TO_DATE | UPGRADE_AVAILABLE | SOURCE_DIVERGENCE | VERIFICATION_REQUIRED` and is presentation-only.
- `UPGRADE_AVAILABLE` asks whether to prepare an upgrade; “yes” authorizes assessment/Preview only.
- Actual mutation retains Direct-to-Latest classification, Preview, explicit approval, preservation, rollback, verification, one final `RELEASE_FULL`, promotion/history preservation.
- The command creates no auto-updater/parser/service/path-binding authority.

- [ ] **Step 3: Update `FRAMEWORK-RELEASE.yaml`**

Change only release identity/pointer fields required for this release:

```yaml
framework_version: "1.3.1"
schema_version: "1.0.0"
release_format_version: 3
latest_framework_amendment: "references/framework-governance-amendment-260824-1708.md"
```

Keep existing `upgrade_policy` values unchanged.

- [ ] **Step 4: Update README current release and additions**

Change Current Release to Framework `1.3.1` / Schema `1.0.0`. Add a concise “Framework 1.3.1 Project Upgrade Command” section before the existing 1.3.0 section, preserving 1.3.0 as historical/current-line context rather than rewriting it.

- [ ] **Step 5: Verify release identity consistency**

Run:

```powershell
python -c "from pathlib import Path; r=Path('managing-project-source/FRAMEWORK-RELEASE.yaml').read_text(encoding='utf-8'); a=Path('managing-project-source/references/framework-governance-amendment-260824-1708.md').read_text(encoding='utf-8'); rd=Path('README.md').read_text(encoding='utf-8'); assert 'framework_version: \"1.3.1\"' in r; assert 'schema_version: \"1.0.0\"' in r; assert 'release_format_version: 3' in r; assert 'framework-governance-amendment-260824-1708.md' in r; assert 'project_source_framework_version: \"1.3.1\"' in a; assert 'Project Source Framework: **1.3.1**' in rd; print('release identity PASS')"
```

Expected: `release identity PASS` and exit `0`.

- [ ] **Step 6: Commit release identity/amendment**

```powershell
git add README.md managing-project-source/FRAMEWORK-RELEASE.yaml managing-project-source/references/framework-governance-amendment-260824-1708.md
git commit -m "docs: define framework 1.3.1 project upgrade command"
```

---

### Task 3: Implement the Normative `[Project Upgrade]` Contract

**Files:**
- Modify: `managing-project-source/references/core-governance-rules.md` in section `16.4 Registered Project Command Contract`
- Modify: `managing-project-source/SKILL.md` in `Framework 1.3.0 Registered Project Commands`, workflow, and quick-reference sections

**Interfaces:**
- Consumes: Framework 1.3.1 amendment, existing `[Project Status]`/`[Project Path]` command contract, current Direct-to-Latest rules.
- Produces: Authoritative command semantics and operational instructions used by templates/launchers.

- [ ] **Step 1: Extend the Core Governance command registry**

Add exactly:

```text
[Project Upgrade] : fresh-compare the active Project Framework with canonical upstream and offer governed upgrade preparation when they differ
```

Preserve literal-bracket/case-insensitive rules and registered-command discovery behavior.

- [ ] **Step 2: Add a Core Governance `[Project Upgrade]` subsection**

Define this sequence:

```text
resolve current Project/local pin
→ fresh-resolve canonical upstream target
→ compare version/schema/source identity + freshness evidence
→ report UP_TO_DATE | UPGRADE_AVAILABLE | SOURCE_DIVERGENCE | VERIFICATION_REQUIRED
→ if UPGRADE_AVAILABLE, ask whether to prepare an upgrade
→ positive answer starts cumulative current→target assessment/Preview only
→ explicit mutation approval remains required after Preview
```

State explicitly that same version strings do not override material source divergence and that unresolved inputs fail closed.

- [ ] **Step 3: Preserve existing upgrade governance by reference**

In the new subsection, explicitly reuse `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`, preservation, rollback, one final `RELEASE_FULL`, and promotion/history rules rather than duplicating a competing migration architecture.

- [ ] **Step 4: Update `SKILL.md` current distribution identity**

Change `Current distribution` to Framework `1.3.1` / Schema `1.0.0`.

- [ ] **Step 5: Extend the `SKILL.md` command registry and operational behavior**

Add `[Project Upgrade]` to the canonical display list and mirror the Core Governance comparison/approval sequence. Keep user-facing operational prose concise enough to support launcher compaction later.

- [ ] **Step 6: Update workflow/quick-reference behavior**

Add an operational rule that `[Project Upgrade]` is read-only until the user opts into preparation, and that upgrade-intent approval is not mutation approval. Do not introduce a new lifecycle state.

- [ ] **Step 7: Run affected normative verification**

```powershell
python -c "from pathlib import Path; files=['managing-project-source/references/core-governance-rules.md','managing-project-source/SKILL.md']; text='\n'.join(Path(p).read_text(encoding='utf-8') for p in files); req=['[Project Upgrade]','UP_TO_DATE','UPGRADE_AVAILABLE','SOURCE_DIVERGENCE','VERIFICATION_REQUIRED','FAST_PATH','ASSESSED_PATH','MAJOR_MIGRATION_REQUIRED']; missing=[x for x in req if x not in text]; assert not missing, missing; assert 'prepare' in text.lower(); print('normative command PASS')"
```

Expected: `normative command PASS` and exit `0`.

- [ ] **Step 8: Commit normative contract**

```powershell
git add managing-project-source/references/core-governance-rules.md managing-project-source/SKILL.md
git commit -m "feat: register project upgrade command governance"
```

---

### Task 4: Propagate Framework 1.3.1 to Maintained Starter Surfaces

**Files:**
- Modify: `managing-project-source/templates/00-project-source-framework.md`
- Modify: `managing-project-source/templates/core-document-skeletons.md`
- Modify: `managing-project-source/templates/project-source-mockup/00-Project-Source-Framework.template.md`
- Modify: `managing-project-source/templates/project-source-mockup/README.md`
- Review/modify only if version text exists: all other current `managing-project-source/templates/project-source-mockup/*.template.md`

**Interfaces:**
- Consumes: Normative Core Governance/SKILL command semantics.
- Produces: Current maintained starter representation aligned to Framework `1.3.1` without creating reserved slots or a second starter tree.

- [ ] **Step 1: Update root template release identity**

Change Framework current-version references from `1.3.0` to `1.3.1` where they denote the current distribution, without rewriting historical descriptive sections that intentionally describe Framework 1.3.0 origin semantics.

- [ ] **Step 2: Extend root-template command registry**

Add `[Project Upgrade]` with the same concise semantics as Core Governance: fresh current/upstream comparison, report-only labels, ask-before-prepare, no mutation authority.

- [ ] **Step 3: Update skeleton current-distribution note**

Add a Framework `1.3.1` note that `[Project Upgrade]` composes with existing 1.3.0 command/direct-upgrade semantics; keep Schema `1.0.0`.

- [ ] **Step 4: Update mockup root template and README**

Set current distribution to Framework `1.3.1` / Schema `1.0.0` and add the new command to current command semantics. Preserve `18–19 RESERVED` and existing slot map unchanged.

- [ ] **Step 5: Normalize current-version metadata across maintained mockup templates**

For each current template with `project_source_framework_version`, set it to `"1.3.1"`; keep schema/ranges unchanged. Do not modify historical amendment files.

- [ ] **Step 6: Verify starter consistency and reserved-slot preservation**

```powershell
python -c "from pathlib import Path; root=Path('managing-project-source/templates'); files=[p for p in root.rglob('*.md') if '.git' not in p.parts]; current=[p for p in files if 'project-source-mockup' in str(p) or p.name in {'00-project-source-framework.md','core-document-skeletons.md'}]; bad=[]; [bad.append(str(p)) for p in current if 'project_source_framework_version:' in p.read_text(encoding='utf-8') and 'project_source_framework_version: \"1.3.1\"' not in p.read_text(encoding='utf-8')]; assert not bad, bad; readme=Path('managing-project-source/templates/project-source-mockup/README.md').read_text(encoding='utf-8'); assert '`18–19` | RESERVED' in readme; assert '[Project Upgrade]' in readme; print('starter propagation PASS')"
```

Expected: `starter propagation PASS` and exit `0`.

- [ ] **Step 7: Commit starter propagation**

```powershell
git add managing-project-source/templates
git commit -m "docs: propagate framework 1.3.1 project upgrade command"
```

---

### Task 5: Update Compact ChatGPT/Claude Launchers

**Files:**
- Modify: `managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md`
- Modify: `managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md`

**Interfaces:**
- Consumes: Normative `[Project Upgrade]` behavior from Task 3.
- Produces: Compact bootstrap launchers carrying enough command/upgrade semantics for correct routing while remaining subordinate to canonical sources.

- [ ] **Step 1: Change launcher titles to F1.3.1 / S1.0.0**

Use the existing title style and update only the release identity.

- [ ] **Step 2: Compact the shared Commands paragraph**

Retain `[Project Status]` and `[Project Path]`, then add `[Project Upgrade]` semantics in compact form:

```text
[Project Upgrade] fresh-compares local pin vs fresh canonical upstream; report UP_TO_DATE/UPGRADE_AVAILABLE/SOURCE_DIVERGENCE/VERIFICATION_REQUIRED; difference asks to prepare upgrade; yes ≠ mutation approval.
```

Keep command-help behavior registry-only.

- [ ] **Step 3: Keep Upgrade paragraph aligned**

Retain initialized-project pinning, direct current→target classification, preservation, and no destructive starter rebuild. Do not duplicate detailed migration rules already available from canonical sources.

- [ ] **Step 4: Make shared marker bodies byte-identical**

Text between `PROJECTFRAMEWORK-SHARED-CONTRACT:START` and `PROJECTFRAMEWORK-SHARED-CONTRACT:END` must be exactly identical in both files.

- [ ] **Step 5: Verify launcher sizes and marker equality**

```powershell
python -c "from pathlib import Path; ps=[Path('managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md'),Path('managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md')]; texts=[p.read_text(encoding='utf-8') for p in ps]; start='<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:START -->'; end='<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:END -->'; bodies=[t.split(start,1)[1].split(end,1)[0] for t in texts]; assert bodies[0]==bodies[1]; assert all(len(t)<=4500 for t in texts), [(str(p),len(t)) for p,t in zip(ps,texts)]; assert all('[Project Upgrade]' in t for t in texts); print([(p.name,len(t)) for p,t in zip(ps,texts)]); print('launcher PASS')"
```

Expected: both lengths `<= 4500`, then `launcher PASS`.

- [ ] **Step 6: Commit launcher update**

```powershell
git add managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md
git commit -m "docs: expose project upgrade command in launchers"
```

---

### Task 6: Run Affected Verification and Close Pressure Scenarios GREEN

**Files:**
- Verify: all files changed by Tasks 1–5
- Modify only when a verification failure identifies a real inconsistency in an affected current surface

**Interfaces:**
- Consumes: Complete candidate semantics from Tasks 1–5.
- Produces: Task-local/affected verification evidence sufficient to prepare the release candidate for `RELEASE_FULL`.

- [ ] **Step 1: Run `git diff --check` against the implementation range**

```powershell
git diff --check 7de0f2f..HEAD
```

Expected: no output, exit `0`.

- [ ] **Step 2: Verify Framework/Schema/release-format consistency**

Run a Python structural check across README, release descriptor, latest amendment, SKILL, root/current templates, mockup README, and launchers. Current surfaces must identify Framework `1.3.1` / Schema `1.0.0`; historical amendments must not be rewritten.

- [ ] **Step 3: Verify registered command coverage**

Assert `[Project Status]`, `[Project Path]`, and `[Project Upgrade]` exist across Core Governance, SKILL, root template, mockup README, and both launchers; command discovery must not list an invented fourth command.

- [ ] **Step 4: Verify comparison/approval invariants**

Assert current normative surfaces contain all report labels plus explicit semantics for fresh upstream evidence, local pin authority, ask-before-prepare, and preparation approval distinct from mutation approval.

- [ ] **Step 5: Verify Direct-to-Latest preservation remains intact**

Assert `FAST_PATH`, `ASSESSED_PATH`, `MAJOR_MIGRATION_REQUIRED`, no mandatory intermediate execution, preservation/history, and latest-starter non-destructive boundary still exist in normative sources.

- [ ] **Step 6: Verify pressure scenarios 136–150 now have matching normative support**

Read each Scenario 136–150 and map its PASS/GREEN expectation to at least one current normative surface. Any unmapped scenario is a failure and must be corrected before proceeding.

- [ ] **Step 7: Verify prohibited artifact absence**

Check the implementation range for newly added executable/runtime artifacts. The allowed change set is Markdown/YAML governance/tests only; no `.py`, `.js`, `.ts`, `.ps1`, `.sh`, workflow, scheduler, or runtime source file may be introduced as part of this Task.

```powershell
python -c "import subprocess; names=subprocess.check_output(['git','diff','--name-only','7de0f2f..HEAD'],text=True).splitlines(); bad=[p for p in names if not (p.endswith('.md') or p.endswith('.yaml'))]; assert not bad, bad; print('artifact-scope PASS')"
```

Expected: `artifact-scope PASS`.

- [ ] **Step 8: Commit any verification-driven corrections**

If no corrections are needed, do not create an empty commit. If corrections are needed, stage only affected Framework files and commit:

```powershell
git commit -m "fix: align project upgrade command governance"
```

---

### Task 7: RELEASE_FULL and Candidate Completion Checkpoint

**Files:**
- Evidence create: `docs/superpowers/evidence/2026-08-24-framework-1.3.1-project-upgrade-release-full.md`
- Verify: full current Framework distribution

**Interfaces:**
- Consumes: Candidate that has stopped changing after Task 6.
- Produces: One state-bound `RELEASE_FULL` result, candidate commit/tree/worktree evidence, and durable implementation completion commit before Task Registry reconciliation.

- [ ] **Step 1: Confirm the candidate has stopped changing**

Run `git status --short` and inspect all implementation changes. Do not start `RELEASE_FULL` while semantic edits are still expected.

- [ ] **Step 2: Run one full current-distribution structural verification**

The full check must cover at least:

- Framework `1.3.1` / Schema `1.0.0` / release format `3` identity;
- latest amendment pointer;
- all three registered commands across normative/current distribution surfaces;
- bracket/case-insensitive command contract;
- `[Project Upgrade]` report vocabulary and approval split;
- local-pin/current vs fresh-upstream/target authority separation;
- Direct-to-Latest path classes and preservation;
- pressure scenarios 136–150;
- launcher `<=4,500` and byte-identical marker bodies;
- reserved slots `18–19` unchanged;
- no executable updater/parser/CI/scheduler/watcher/runtime artifacts.

The command must exit `0`. Record exact check count and result; do not invent a pass count before running it.

- [ ] **Step 3: Capture candidate identity**

Record observed pre-completion candidate tree, working-tree state, verification command/result, and relevant assumptions in the evidence file.

- [ ] **Step 4: Commit the completed Framework 1.3.1 candidate**

Stage only release implementation/evidence files and commit:

```powershell
git commit -m "feat: release framework 1.3.1 project upgrade command"
```

Do not push.

- [ ] **Step 5: Re-observe completion commit and clean/understood worktree**

Record `git rev-parse HEAD`, `git rev-parse HEAD^{tree}`, and `git status --short`. The completed implementation state must be represented by observed Git commit(s); no required completed result may exist only uncommitted.

- [ ] **Step 6: Run `INTEGRATION_GATE` before any branch/worktree integration**

Fresh-resolve the Canonical Integration Target, classify Base Freshness, and confirm prior affected/`RELEASE_FULL` evidence remains valid for the exact candidate. If target movement, conflict resolution, rebase result, merge-time edits, or other material assumptions invalidate evidence, rerun the affected/full verification required by Framework 1.2.5/1.3 before integration. If no integration is performed in this execution, record `INTEGRATION_GATE: NOT_APPLICABLE` rather than fabricating a pass.

---

### Task 8: Reconcile `TASK-018` Project Task Source

**Files:**
- Modify: `docs/superpowers/PROJECT-TASKS.md`

**Interfaces:**
- Consumes: Observed completed Framework 1.3.1 implementation commit and `RELEASE_FULL` evidence from Task 7.
- Produces: Durable Workspace Task source whose `TASK-018` state matches verified Git truth without conflating commit with push.

- [ ] **Step 1: Update `TASK-018` implementation references**

Add the implementation plan path:

```text
docs/superpowers/plans/2026-08-24-project-upgrade-command.md
```

and the release evidence path:

```text
docs/superpowers/evidence/2026-08-24-framework-1.3.1-project-upgrade-release-full.md
```

- [ ] **Step 2: Mark `TASK-018` `DONE` only if the completion checkpoint is satisfied**

Required truth before changing status:

- design/spec approved;
- implementation plan executed;
- pressure/affected checks PASS;
- one final unchanged-candidate `RELEASE_FULL` PASS;
- required implementation state exists in observed completion commit(s);
- remaining working-tree state is clean or explicitly understood;
- no unresolved blocker prevents the Task's completion criteria.

If any item is false, keep `TODO`, `IN_PROGRESS`, or `BLOCKED` as applicable instead of fabricating `DONE`.

- [ ] **Step 3: Set the next step from remaining Project truth**

If `TASK-019` is still `TODO`, its exact next step remains the next backlog action. Do not make Task #18 completion imply Task #19 completion.

- [ ] **Step 4: Run Task-source consistency check**

Read `PROJECT-TASKS.md` and ensure Task #18 references the approved spec, implementation plan, completion evidence, and observed completion commit while preserving Task #19 independently.

- [ ] **Step 5: Commit Task-source reconciliation**

```powershell
git add docs/superpowers/PROJECT-TASKS.md
git commit -m "docs: complete project upgrade task tracking"
```

Do not push without separate publication approval.

---

## Final Implementation Acceptance Gate

Before claiming `TASK-018` implementation complete, verify all of the following from fresh evidence:

- [ ] Framework current release is exactly `1.3.1`; Schema exactly `1.0.0`; release format exactly `3`.
- [ ] `[Project Upgrade]` is registered consistently and command discovery lists it alongside `[Project Status]` and `[Project Path]` only.
- [ ] Literal brackets remain required and registered-name matching remains case-insensitive.
- [ ] Initialized Project current identity comes from active local pin; upstream is fresh target evidence, not current authority.
- [ ] Report vocabulary is exactly `UP_TO_DATE | UPGRADE_AVAILABLE | SOURCE_DIVERGENCE | VERIFICATION_REQUIRED` and remains presentation-only.
- [ ] Same-version material divergence cannot collapse to `UP_TO_DATE` automatically.
- [ ] `UPGRADE_AVAILABLE` asks before preparation; a positive answer does not authorize immediate mutation.
- [ ] Cumulative assessment/Preview + separate explicit mutation approval remain required before Project mutation.
- [ ] `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`, preservation/history, and no mandatory intermediate migration execution remain intact.
- [ ] Pressure scenarios 136–150 are present and supported by current normative surfaces.
- [ ] Launchers are `<=4,500` Unicode characters and shared marker bodies are byte-identical.
- [ ] No executable updater/parser/validator/CLI/CI/scheduler/watcher/runtime artifacts were introduced.
- [ ] One final unchanged-candidate `RELEASE_FULL` PASS is bound to observed candidate state.
- [ ] Completion commit(s) and working-tree state satisfy the Verified Task Completion Checkpoint.
- [ ] `TASK-018` Project Task source truth matches completion evidence; Task #19 remains independent.
- [ ] No push/publication claim is made unless fresh remote evidence confirms an explicitly approved push.
