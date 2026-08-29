# TASK-038 Framework-Source Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rename the reusable Framework distribution from `managing-project-source/` to the single canonical `Framework-Source/` root for Framework `1.8.0`, preserve historical provenance, and reconcile ProjectFramework's own current Project Source without auto-upgrading its local Framework pin.

**Architecture:** Use one Git directory move, then rewrite only current mutable routing/documentation/governance surfaces. Historical specs/plans/evidence/amendment payloads retain their old path text; there is no compatibility alias. ProjectFramework's active Project Source is reconciled through governed revisions and `MIG/EVD/CHG/ACT` records so current truth points at `Framework-Source/` while captured historical facts remain reconstructable.

**Tech Stack:** Markdown/YAML governance sources, Git rename/history, Python structural verification scripts used only as test runners.

**Spec:** `docs/superpowers/specs/2026-08-29-task038-framework-source-rename-design.md`

## Global Constraints

- Canonical target directory is exactly `Framework-Source/`; Project-specific authority remains exactly `Project-Source/`.
- No live `managing-project-source/` compatibility alias, duplicate tree, symlink, or shim remains after migration.
- Framework release becomes `1.8.0`; Project Source Schema remains `1.0.0`; release format remains `3`.
- Historical old-path strings are preserved when they describe actual historical repository state.
- Do not globally replace `managing-project-source/` across the repository.
- The three historical Framework amendments observed to contain old-path strings retain identical content blobs after the move: `framework-governance-amendment-260820-0735.md`, `framework-governance-amendment-260820-0821.md`, and `framework-governance-amendment-260825-task020.md`.
- `PROJECT-BOOTSTRAP.md` remains a Project-root locator into `Project-Source/`; it never points to `Framework-Source/` as Project authority.
- ProjectFramework's existing active `FRAMEWORK-001` pin remains `1.7.0` unless a separate governed `[Project Upgrade]` explicitly changes it.
- Current Project Source path statements must resolve `Framework-Source/` after migration; old captured EVD/CHG payload remains historical.
- Root Governance changes in active `00` use revision/validate/promote/supersede/archive flow.
- Existing external/Brownfield Projects are not auto-rewritten.
- TASK-038 owns pressure scenarios `181–188`; TASK-039 starts at `189`.
- Official launchers remain byte-identical in their shared marker bodies and each remains within the current `<=4,500` Unicode-character ceiling.
- `18–19` remain RESERVED; no new Stable-ID family or semantic slot is introduced.
- `commit ≠ push`; this plan does not infer remote publication authority.

---

### Task 1: Establish RED migration scenarios and provenance baselines

**Files:**
- Modify: `managing-project-source/tests/pressure-scenarios.md`
- Read/hash: `managing-project-source/references/framework-governance-amendment-260820-0735.md`
- Read/hash: `managing-project-source/references/framework-governance-amendment-260820-0821.md`
- Read/hash: `managing-project-source/references/framework-governance-amendment-260825-task020.md`
- Read/hash: `docs/superpowers/specs/2026-08-29-task023-self-bootstrapping-project-design.md`
- Read/hash: `docs/superpowers/evidence/2026-08-29-task-023-self-bootstrapping-project-release-full.md`

**Interfaces:**
- Consumes: approved TASK-038 design and current Framework `1.7.0` tree.
- Produces: RED-first migration contract plus historical blob/hash baselines used by final verification.

- [ ] **Step 1: Fresh-check base state**

Run:

```bash
git status --short --branch
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

Classify Base Freshness. Do not start the migration on an unexplained dirty tree or unresolved semantic base conflict.

- [ ] **Step 2: Capture historical blob/hash baselines before any move**

Run:

```bash
git hash-object managing-project-source/references/framework-governance-amendment-260820-0735.md
git hash-object managing-project-source/references/framework-governance-amendment-260820-0821.md
git hash-object managing-project-source/references/framework-governance-amendment-260825-task020.md
git hash-object docs/superpowers/specs/2026-08-29-task023-self-bootstrapping-project-design.md
git hash-object docs/superpowers/evidence/2026-08-29-task-023-self-bootstrapping-project-release-full.md
```

Persist the five observed SHAs in the TASK-038 release evidence scratch/notes used later; do not modify the hashed files.

- [ ] **Step 3: Append scenarios 181–188**

Use the repository's existing `Prompt / Pass / Fail / GREEN expectation` structure and these exact identities:

```text
181 Framework-Source Is The Only Canonical Distribution Root
182 Legacy Distribution Root Is Not A Live Alias
183 Historical Old-Path References Preserve Provenance
184 Current Bootstrap And README Routing Use Framework-Source
185 Brownfield Projects Are Not Auto-Rewritten By Upstream Rename
186 ProjectFramework Current Project Source Reconciles Distribution Path
187 PROJECT-BOOTSTRAP Still Routes To Project-Source, Not Framework-Source
188 Framework-Source And Project-Source Authority Roles Must Not Collapse
```

Each scenario must fail against the pre-migration repository for the intended reason; scenario 183 must reject cosmetic historical rewriting, not demand zero old-path strings.

- [ ] **Step 4: Verify scenario identity and RED baseline**

Run a Python check equivalent to:

```python
from pathlib import Path
import re
p = Path('managing-project-source/tests/pressure-scenarios.md')
t = p.read_text(encoding='utf-8')
nums = [int(x) for x in re.findall(r'^## Scenario (\d+) —', t, re.M)]
assert nums[-8:] == list(range(181, 189))
assert len(nums) == len(set(nums))
assert not Path('Framework-Source').exists()
assert Path('managing-project-source').is_dir()
```

- [ ] **Step 5: Commit RED contract**

```bash
git add managing-project-source/tests/pressure-scenarios.md
git commit -m "test: define Framework-Source migration scenarios"
```

---

### Task 2: Move the distribution tree and establish Framework 1.8.0 identity

**Files:**
- Move: `managing-project-source/` → `Framework-Source/`
- Create: `Framework-Source/references/framework-governance-amendment-260829-task038.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: RED scenarios and historical hash baselines.
- Produces: one physical canonical distribution root and current Framework `1.8.0` source identity.

- [ ] **Step 1: Perform one Git directory move**

```bash
git mv managing-project-source Framework-Source
```

Immediately verify:

```text
Framework-Source/ exists
managing-project-source/ does not exist
Framework-Source/FRAMEWORK-RELEASE.yaml exists
Framework-Source/templates/PROJECT-BOOTSTRAP.md exists
```

Do not create any alias at the old path.

- [ ] **Step 2: Create the TASK-038 Framework amendment**

Create `Framework-Source/references/framework-governance-amendment-260829-task038.md` with this header:

```yaml
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.7.0"
project_source_framework_version: "1.8.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_EXPLICIT_CONTINUOUS_APPROVAL_2026-08-29"
compatibility: "BACKWARD_COMPATIBLE_PROJECT_PIN_WITH_UPSTREAM_DISTRIBUTION_ROOT_MIGRATION"
```

The amendment body must define exactly one canonical `Framework-Source/`, preserve `Project-Source/` authority separation, reject alias/duplicate roots, preserve historical old-path provenance, require Brownfield explicit upgrade/migration, and keep `PROJECT-BOOTSTRAP.md` routing into Project Source.

- [ ] **Step 3: Update release descriptor**

Set:

```yaml
framework_version: "1.8.0"
schema_version: "1.0.0"
release_format_version: 3
latest_framework_amendment: "references/framework-governance-amendment-260829-task038.md"
```

Keep descriptor entrypoints relative to `Framework-Source/` and preserve existing 1.7 bootstrap policy semantics unless refined by TASK-038.

- [ ] **Step 4: Rewrite current Core Governance distribution paths only**

In `Framework-Source/references/core-governance-rules.md`, replace current canonical references such as:

```text
managing-project-source/FRAMEWORK-RELEASE.yaml
managing-project-source/templates/PROJECT-BOOTSTRAP.md
managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md
managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md
```

with their `Framework-Source/...` equivalents. Do not edit historical amendment files that still mention the old path.

- [ ] **Step 5: Update `SKILL.md` current distribution identity**

Set current distribution to Framework `1.8.0` / Schema `1.0.0`, make `Framework-Source/` the reusable Framework source root, and preserve the existing authority rule that initialized local Project Source remains authoritative after bootstrap.

- [ ] **Step 6: Add migration notes**

Add a current `1.7.0 → 1.8.0` section stating:

```text
canonical upstream distribution root changes from managing-project-source/ to Framework-Source/
no live alias remains at the old root
initialized Projects are not auto-rewritten
direct external deep links/scripts using the old upstream path require explicit update
historical path strings remain historical and are not globally rewritten
PROJECT-BOOTSTRAP.md continues to locate Project-Source/
```

- [ ] **Step 7: Update root README current routing**

All current user instructions, package-root lines, tree diagrams, bootstrap read order, launcher-copy paths, and reusable-package descriptions must use `Framework-Source/`. Explicit historical/migration explanations may retain `managing-project-source/` only when clearly marked old/source path.

- [ ] **Step 8: Verify historical distribution amendment blobs are unchanged**

Run `git hash-object` on the three moved files under `Framework-Source/references/` and compare each result with the baseline SHA captured in Task 1. All three must match exactly.

- [ ] **Step 9: Commit physical migration and release identity**

```bash
git add -A
git commit -m "refactor: rename Framework distribution root"
```

---

### Task 3: Propagate Framework 1.8.0 current starter and launcher surfaces

**Files:**
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: current maintained `Framework-Source/templates/project-source-mockup/*.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/README.md`
- Modify: `Framework-Source/templates/project-location-bootstrap.md` when current root wording applies
- Modify: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md`
- Modify: `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md`

**Interfaces:**
- Consumes: Framework `1.8.0` release identity and renamed tree.
- Produces: maintained current starters/adapters aligned to `Framework-Source/` without changing historical amendments.

- [ ] **Step 1: Update current starter version stamps**

Every maintained current starter containing `project_source_framework_version:` must be `"1.8.0"`; `project_source_schema_version:` remains `"1.0.0"`.

Narrative text that intentionally says a feature was introduced in an earlier version (for example `STANDARD IN FRAMEWORK 1.2.0+`) remains historical and is not mechanically changed.

- [ ] **Step 2: Update current Framework-source path wording**

Where current starter/docs explicitly identify the reusable distribution root, use `Framework-Source/`. Do not change the consuming Project Source location `<Project-Root>/Project-Source/`.

- [ ] **Step 3: Preserve root bootstrap semantics**

`Framework-Source/templates/PROJECT-BOOTSTRAP.md` remains a template for deployed `<Project-Root>/PROJECT-BOOTSTRAP.md` and must continue to route to the consuming Project's `Project-Source/00 → 01 → 03`, with `09` continuation.

- [ ] **Step 4: Update launcher release titles/current-source wording**

Set ChatGPT/Claude launcher Framework identity to `1.8.0 / 1.0.0`. If the launcher body mentions a concrete distribution root, use `Framework-Source/`; keep project-specific path placeholders and current command/response-close tokens unchanged.

- [ ] **Step 5: Verify launcher parity and size**

Run a Python check that extracts the shared marker body from both launchers, asserts exact byte identity, and asserts both full launcher strings are `<= 4500` Unicode characters.

- [ ] **Step 6: Verify starter shape**

Assert:

```text
18–19 RESERVED
mandatory/conditional slot map unchanged
92 remains conditional Project Graph
no new Stable-ID family
all maintained current stamps = Framework 1.8.0 / Schema 1.0.0
```

- [ ] **Step 7: Commit starter/launcher propagation**

```bash
git add Framework-Source/templates Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md
git commit -m "docs: propagate Framework-Source 1.8 starters"
```

---

### Task 4: Reconcile ProjectFramework's own current Project Source

**Files:**
- Modify: `PROJECT-BOOTSTRAP.md`
- Create/promote new active revisions for affected Project Source documents using one Bangkok timestamp `STAMP` computed at Task 4 start.
- Archive superseded affected revisions under `Project-Source/archive/`.
- At minimum revise semantic slots: `00`, `01`, `02`, `03`, `09`, `10`, `13`, `14`, `15`, `16`.
- Preserve unchanged active slots: `04`, `05`, `11`, `12`, `17` unless fresh review proves another current-path dependency.

**Interfaces:**
- Consumes: completed physical distribution rename and current Project Source `1.7.0` pin.
- Produces: current ProjectFramework governance that accurately routes to `Framework-Source/` without auto-upgrading its local Framework pin.

- [ ] **Step 1: Compute one Project Source revision timestamp**

At Task 4 start, compute Bangkok `YYMMDD-HHMM` once and call it `STAMP`. Every new Project Source filename created by this migration uses that exact `STAMP`; metadata `updated_at` uses the corresponding offset-aware ISO 8601 time.

- [ ] **Step 2: Create candidate `00` revision**

Create `Project-Source/drafts/00-Project-Source-Framework-r002-${STAMP}.md` from active r001 with:

```text
revision: 2
project_source_framework_version: "1.7.0"  # local pin intentionally unchanged
Framework Distribution Root: Framework-Source/
TASK-038 no longer described as a future proposed rename
```

Do not weaken any Root Governance invariant or change Project Location Binding.

- [ ] **Step 3: Create candidate revisions for current routing/state/provenance**

Create r002 candidates for `01`, `02`, `03`, `09`, `14`, and `16` so current statements resolve:

```text
Framework distribution current root: Framework-Source/
Current Framework release descriptor: Framework-Source/FRAMEWORK-RELEASE.yaml
Framework upstream current release: 1.8.0
ProjectFramework local Project Source pin: 1.7.0
TASK-039 plan remains next after TASK-038 completion
```

`16` must materialize `MIG-001` for `managing-project-source/ → Framework-Source/`, including preservation rules, rollback, approval basis, and verification/evidence pointers.

- [ ] **Step 4: Create candidate Change/Evidence/Action revisions**

Create r002 candidates for:

```text
10 Change Log — append CHG-003 for TASK-038 distribution-root migration
13 Evidence Registry — preserve EVD-001/EVD-002 payload verbatim and append EVD-003 for migration verification
15 Action Registry — preserve ACT-001 and add ACT-002 for TASK-038 with current status
```

Old evidence statements that name `managing-project-source/` remain unchanged because they describe capture-time state.

- [ ] **Step 5: Validate candidate Project Source before promotion**

Check:

```text
same immutable project_uuid across candidates
00 remains document_id FRAMEWORK-001 and framework_root true
00 Framework pin remains 1.7.0
current path statements use Framework-Source/
MIG-001 exists in 16
old EVD payload preserved
01/14 active registry/manifest will resolve all active files
no duplicate active semantic revision after promotion
PROJECT-BOOTSTRAP will point at the new active 00/01/03/09 filenames
```

- [ ] **Step 6: Promote and archive**

For every revised slot, move the old r001 active file into `Project-Source/archive/`, move the validated r002 candidate from `Project-Source/drafts/` into the Project Source root, and update `PROJECT-BOOTSTRAP.md` to the new exact active filenames.

The final active root must contain one active revision per semantic slot. Archived r001 files remain reconstructable history.

- [ ] **Step 7: Refresh `01` and `14` after final filenames are known**

Ensure `01 Active Document Registry` and `14 Current Reconstructable Snapshot` list the exact promoted filenames, including unchanged r001 slots and revised r002 slots. Neither current registry may point into archive for active truth.

- [ ] **Step 8: Set ACT-002 completion metadata only after verification**

Keep ACT-002 `IN_PROGRESS` until Task 5 affected verification passes and required migration commits exist. Do not mark migration `DONE` simply because `git mv` succeeded.

- [ ] **Step 9: Commit Project Source reconciliation checkpoint**

```bash
git add PROJECT-BOOTSTRAP.md Project-Source
git commit -m "docs: reconcile Project Source after Framework rename"
```

---

### Task 5: Make scenarios 181–188 GREEN and verify historical/current path classification

**Files:**
- Verify/modify exact TASK-038 current surfaces only.
- Modify `Framework-Source/tests/pressure-scenarios.md` only if a test-format defect exists; never weaken approved semantics to make a failing implementation pass.

**Interfaces:**
- Consumes: renamed distribution, Framework 1.8 starters, reconciled Project Source.
- Produces: AFFECTED PASS candidate and migration evidence inputs.

- [ ] **Step 1: Verify top-level path exclusivity**

Assert:

```python
from pathlib import Path
assert Path('Framework-Source').is_dir()
assert not Path('managing-project-source').exists()
assert Path('Project-Source').is_dir()
assert Path('PROJECT-BOOTSTRAP.md').is_file()
```

- [ ] **Step 2: Verify scenarios 1–188 identity**

Assert scenario numbers are unique/contiguous and the last eight are `181..188`.

- [ ] **Step 3: Verify current old-path allowlist**

Enumerate tracked text occurrences of `managing-project-source/`. Every match must classify as one of:

```text
historical completed spec/plan/evidence
historical Framework amendment
archived Project Source revision or historical EVD/CHG payload
TASK-038/TASK-039 migration design/plan/task text explaining old → new
MIGRATION-NOTES source-side migration text
```

Fail if a current README route, current Core Governance route, current launcher instruction, active Project Source current-state statement, or current verifier treats the old root as canonical.

- [ ] **Step 4: Recheck historical blob/hash sentinels**

Compare the five `git hash-object` results from Task 1 against post-migration paths/content. The three moved historical amendments must keep identical blob SHAs; the selected completed spec/evidence outside the tree must also remain identical.

- [ ] **Step 5: Verify bootstrap/authority separation**

Assert root `PROJECT-BOOTSTRAP.md` points to active `Project-Source/00 → 01 → 03` and never declares `Framework-Source/` as Project authority. Assert active `00` still pins ProjectFramework's own Framework version to `1.7.0`.

- [ ] **Step 6: Verify release/starter/launcher invariants**

Assert:

```text
Framework-Source/FRAMEWORK-RELEASE.yaml = 1.8.0 / 1.0.0 / format 3
latest amendment = task038
maintained starters = 1.8.0 / 1.0.0
18–19 RESERVED
launcher shared bodies byte-identical
launchers <=4500 chars
```

- [ ] **Step 7: Run `git diff --check` and affected verification**

Record exact affected-check count/result. Fix root causes in owning current surfaces only.

- [ ] **Step 8: Commit verification fixes if required**

If tracked verification fixes were necessary:

```bash
git add -u
git commit -m "fix: align Framework-Source migration contract"
```

Skip this commit when no fix is needed.

---

### Task 6: Final RELEASE_FULL, Project Source completion, and TASK-038 evidence

**Files:**
- Create: `docs/superpowers/evidence/2026-08-29-task-038-framework-source-rename-release-full.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Modify/promote final current revisions as required: Project Source `03`, `09`, `10`, `13`, `15`, `16`, plus `01/14` if final active filenames change.

**Interfaces:**
- Consumes: unchanged TASK-038 candidate with AFFECTED PASS.
- Produces: TASK-038 `DONE`, durable migration evidence, clean handoff to TASK-039.

- [ ] **Step 1: Freeze candidate identity**

Observe:

```bash
git status --short --branch
git rev-parse HEAD
git rev-parse HEAD^{tree}
```

Working tree must be clean before final candidate verification.

- [ ] **Step 2: Run one `RELEASE_FULL` on the unchanged candidate**

The verifier must cover scenarios `1–188`, release identity, amendment chain, root rename, historical allowlist/blob preservation, README/Core/SKILL, starters, launchers, Project Source reconciliation, Task lifecycle, and `git diff --check`.

- [ ] **Step 3: Write TASK-038 release evidence**

Record at minimum:

```text
candidate commit + tree SHA
AFFECTED result
RELEASE_FULL result
scenario range 1–188
old/new distribution roots
historical blob sentinel SHAs before/after
remaining-old-path classification result
Project Source active Framework pin remains 1.7.0
MIG-001 / EVD / CHG / ACT pointers
launcher sizes + shared-body parity
working-tree state
publication state = NOT_PUSHED unless fresh remote evidence proves otherwise
```

- [ ] **Step 4: Finalize Project Source ACT/MIG/current state**

After verification and completion commit evidence are available:

```text
ACT-002 → DONE
MIG-001 → completed/validated state defined by current registry semantics
03 → READY; next action = execute approved TASK-039 implementation plan
09 → PERSISTED continuation; next action = execute TASK-039 plan
13 → append final verification evidence pointer if not already present
10 → append completion CHG if material
```

Use normal Project Source revision/promotion if these updates change already-promoted active documents; do not overwrite archived history.

- [ ] **Step 5: Reconcile TASK-038 Task Registry**

Set TASK-038 `DONE` only after required verification and completion commit criteria are met. Record Design Spec, Implementation Plan, implementation commits, release evidence, candidate identity, verification result, working-tree state, and publication state separately.

- [ ] **Step 6: Commit completion evidence**

```bash
git add docs/superpowers/evidence/2026-08-29-task-038-framework-source-rename-release-full.md docs/superpowers/PROJECT-TASKS.md PROJECT-BOOTSTRAP.md Project-Source
git commit -m "docs: record Framework-Source migration evidence"
```

- [ ] **Step 7: Postflight and TASK-039 handoff**

Fresh-observe local HEAD, working tree, and `origin/main`. Do not claim push from commit existence. Once TASK-038 is `DONE` and `Framework-Source/` is canonical, TASK-039's approved plan at `docs/superpowers/plans/2026-08-29-task039-persistent-goal-command.md` is unblocked and becomes the exact next Framework implementation action.
