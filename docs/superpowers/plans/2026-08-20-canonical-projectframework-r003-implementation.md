# Canonical ProjectFramework r003 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Import the complete r002 framework package into the public canonical repository and release the approved r003 governance clarification as Project Source Framework `1.1.1` while keeping Schema `1.0.0`.

**Architecture:** Preserve `managing-project-source/` as the distributable package root. Implement documentation/governance only: materialized current canonical records, archive-independent Stable-ID resolution, CURRENT export integrity, and a regression pressure scenario. Publish through the isolated branch, review the PR diff/status, then merge to `main`.

**Tech Stack:** Markdown governance artifacts, Git/GitHub branch + pull-request workflow, shell/Python text validation; no executable validator/CLI/runtime dependencies.

**Spec:** `docs/superpowers/specs/2026-08-20-canonical-projectframework-r003-design.md`

## Global Constraints

- Repository: `captainhuke-dev/ProjectFramework`.
- Work only on `framework-r003-materialized-current-state` until verified.
- Preserve ZIP package root `managing-project-source/`; do not flatten it.
- Framework becomes exactly `1.1.1`; Schema remains exactly `1.0.0`.
- Preserve historical approved artifacts unchanged; add a new 1.1.1 amendment instead of rewriting the old amendment.
- Do not implement executable resolver, CLI, validator, migration engine, or automation.
- Every current Stable ID must resolve from the Current Reconstructable Snapshot without archived revisions.
- New projects bootstrap from public `main`; existing projects remain version-pinned until an approved `MIG-*` migration.

---

### Task 1: Import r002 baseline and establish repository bootstrap contract

**Files:**
- Modify: `README.md`
- Create: all seven files from the ZIP under `managing-project-source/` at their original relative paths.

**Interfaces:**
- Consumes: `ProjectSourceFramework-r002-260814-1213.zip`.
- Produces: complete package baseline and canonical new-project bootstrap documentation.

- [ ] **Step 1: Verify source inventory**

Run:
```bash
find managing-project-source -type f -print | sort
```
Expected r002 inventory:
```text
managing-project-source/SKILL.md
managing-project-source/references/approved-design-spec-historical-260813-2140.md
managing-project-source/references/core-governance-rules.md
managing-project-source/references/framework-governance-amendment-260814-0808.md
managing-project-source/templates/00-project-source-framework.md
managing-project-source/templates/core-document-skeletons.md
managing-project-source/tests/pressure-scenarios.md
```

- [ ] **Step 2: Stage those seven files under exactly the same paths**; do not rename or flatten them.

- [ ] **Step 3: Replace root README** so it explicitly states:
```text
captainhuke-dev/ProjectFramework main is the canonical public upstream bootstrap source for new Project Source creation.
Read README.md, then managing-project-source/SKILL.md and its required references/templates.
Current Framework = 1.1.1; Schema = 1.0.0.
Existing projects do not auto-upgrade; they remain pinned until an approved MIG-* migration.
The distributable package root is managing-project-source/.
```

- [ ] **Step 4: Re-run the inventory** and confirm no framework package file was flattened to repository root.

---

### Task 2: Implement Framework 1.1.1 materialized-current-state governance

**Files:**
- Modify: `managing-project-source/SKILL.md`
- Modify: `managing-project-source/references/core-governance-rules.md`

**Interfaces:**
- Consumes: existing canonical-home, archive, Manifest, CURRENT export, and readiness rules.
- Produces: normative archive-independent Current Truth behavior.

- [ ] **Step 1: Add `references/framework-governance-amendment-260820-0646.md` to SKILL required reading**, while retaining the previous amendment as historical context.

- [ ] **Step 2: Add the operational invariant**:
```text
Active canonical registries are materialized current projections, not delta chains.
Every active/current Stable ID must resolve from the Current Reconstructable Snapshot.
Archive may explain history but must not be required to determine current truth.
"retain previous status", "unchanged from rNNN", and "see archived revision" cannot substitute for current authoritative semantic payload.
A long payload may live in an active/current canonical Detail Document only when the current record links to it and the detail is included in the current snapshot/export when needed.
```

- [ ] **Step 3: Add `Archive-dependent Current Truth` to SKILL Red Flags** and require current Stable-ID resolution before readiness/export completeness claims.

- [ ] **Step 4: Add Core Governance section `Materialized Current State and Stable-ID Resolution`** general to current-state-bearing canonical homes, explicitly clarifying `DEC-*` in `04` and `REQ-*` in `05`.

- [ ] **Step 5: Strengthen Manifest/CURRENT rules** so current records plus any required active Detail Documents are included and archive-only semantic dependencies are forbidden.

- [ ] **Step 6: Add this validation requirement exactly in substance**:
```text
Every Stable ID referenced from the Active/Current snapshot MUST resolve to a current authoritative record within the Current Reconstructable Snapshot without requiring an archived revision.
```
State that failure is an integrity/readiness defect and affected scope is not operationally ready when current truth cannot be determined.

- [ ] **Step 7: Verify concepts**:
```bash
grep -RInE "materialized current|delta chain|archiv.*current truth|Stable ID|Current Reconstructable Snapshot|retain previous status|CURRENT" managing-project-source/SKILL.md managing-project-source/references/core-governance-rules.md
```
Expected: both files cover materialization, archive independence, Stable-ID resolution, and CURRENT/Manifest effects.

---

### Task 3: Update active templates to Framework 1.1.1

**Files:**
- Modify: `managing-project-source/templates/00-project-source-framework.md`
- Modify: `managing-project-source/templates/core-document-skeletons.md`

**Interfaces:**
- Consumes: Task 2 normative rules.
- Produces: new Project Sources encoding the invariant by default.

- [ ] **Step 1: Change active pins** to:
```yaml
project_source_framework_version: "1.1.1"
project_source_schema_version: "1.0.0"
```

- [ ] **Step 2: Add the root invariant to the Framework template**: current canonical registries are materialized projections, current Stable IDs resolve inside Current Reconstructable Snapshot, archive is historical only, and delta-only placeholders are invalid authoritative payload.

- [ ] **Step 3: Add Manifest/export validation consequences** including required active Detail Documents.

- [ ] **Step 4: Clarify `04 — Decision Log`**: every current `DEC-*` record materializes Decision/Status semantics or links to an active/current canonical Detail Document; `retain previous status` cannot be the authoritative current record.

- [ ] **Step 5: Clarify `05 — Requirements`** equivalently for Requirement/Status/Acceptance semantics.

- [ ] **Step 6: Clarify `14 — Project Source Manifest`** to include active Detail Documents required to interpret referenced current Stable IDs.

- [ ] **Step 7: Verify version/invariant**:
```bash
grep -RIn 'project_source_framework_version: "1.1.1"' managing-project-source/templates
grep -RIn 'project_source_schema_version: "1.0.0"' managing-project-source/templates
grep -RInE 'retain previous status|materialized current|archiv.*current|Detail Document|Stable ID' managing-project-source/templates
```

---

### Task 4: Add immutable Framework 1.1.1 amendment

**Files:**
- Create: `managing-project-source/references/framework-governance-amendment-260820-0646.md`
- Preserve unchanged: `managing-project-source/references/framework-governance-amendment-260814-0808.md`

**Interfaces:**
- Consumes: approved r003 design and Tasks 2–3 wording.
- Produces: auditable compatibility record for `1.1.1`.

- [ ] **Step 1: Record metadata**: `FRAMEWORK-001`, previous `1.1.0`, new `1.1.1`, Schema `1.0.0` unchanged, explicit user approval on 2026-08-20, backward-compatible clarification/fix.

- [ ] **Step 2: Record five binding changes**:
```text
1. Active canonical registries are materialized current projections, not delta chains.
2. Current Stable IDs resolve without archived revisions.
3. Archive is Historical Truth, not a Current Truth runtime dependency.
4. CURRENT/Current Reconstructable Snapshot includes active records/details needed to interpret referenced current Stable IDs.
5. Referential validation fails when current semantics require archive traversal.
```
Explicitly name `DEC-*` and `REQ-*` as the observed case without narrowing the invariant to only those types.

- [ ] **Step 3: State non-goals**: no executable Stable-ID resolver, CLI, validator, migration engine, or automation.

- [ ] **Step 4: Compare the prior amendment with the ZIP source** and require identical content.

---

### Task 5: Add Scenario 9 regression pressure coverage

**Files:**
- Modify: `managing-project-source/tests/pressure-scenarios.md`

**Interfaces:**
- Consumes: r003 invariant.
- Produces: explicit regression coverage while preserving test-harness honesty.

- [ ] **Step 1: Keep `independent_fresh_agent_green_run: false`**; do not claim an unavailable independent run.

- [ ] **Step 2: Add `Scenario 9 — Archive-Dependent Current Truth Pressure`** with pressure equivalent to:
```text
Decision r003 and Requirements r003 say DEC-005 / REQ-008 / REQ-017 retain previous status. Detailed records are preserved in archived r002, so leave r003 concise and open archive when needed.
```
Pass: materialize current semantics in active canonical records or link to active/current canonical Detail Documents included in the current snapshot.
Fail: require archived r002 to determine current Decision/Requirement semantics.

- [ ] **Step 3: Verify**:
```bash
grep -n "Scenario 9" managing-project-source/tests/pressure-scenarios.md
grep -nE "retain previous status|archive|materializ|Detail Document|current truth" managing-project-source/tests/pressure-scenarios.md
```

---

### Task 6: Release verification, PR, and merge

**Files:** verify all package files, `README.md`, design spec, and this plan.

**Interfaces:**
- Consumes: Tasks 1–5.
- Produces: merged canonical Framework `1.1.1` on `main`.

- [ ] **Step 1: Inventory**: original seven r002 paths plus exactly one new 1.1.1 amendment; no executable tooling files.

- [ ] **Step 2: Version scan**:
```bash
grep -RIn 'project_source_framework_version: "1.1.0"' managing-project-source --exclude='approved-design-spec-historical-260813-2140.md' --exclude='framework-governance-amendment-260814-0808.md'
grep -RIn 'project_source_framework_version: "1.1.1"' managing-project-source
grep -RIn 'project_source_schema_version: "1.0.0"' managing-project-source
```
Expected: no unintended active `1.1.0`; active guidance/templates show `1.1.1`; Schema stays `1.0.0`.

- [ ] **Step 3: Invariant consistency scan** across SKILL, Core Governance, new amendment, both templates, and pressure scenarios for materialization, Stable ID, Current Reconstructable Snapshot, archive independence, and Detail Document language.

- [ ] **Step 4: Scope scan**:
```bash
find managing-project-source -type f \( -name '*.py' -o -name '*.js' -o -name '*.ts' -o -name '*.sh' -o -name '*.go' -o -name '*.rs' \) -print
```
Expected: no output.

- [ ] **Step 5: Verify historical 260814 amendment unchanged** against ZIP source.

- [ ] **Step 6: Compare branch against `main`**; preserve `LICENSE`; confirm only intended import, README, design/plan records, and r003 governance changes.

- [ ] **Step 7: Open PR** titled `Release Project Source Framework 1.1.1 as canonical bootstrap source` summarizing import, canonical bootstrap contract, `1.1.0 -> 1.1.1`, Schema unchanged, materialized current records, CURRENT/Manifest integrity, Scenario 9, and no executable tooling.

- [ ] **Step 8: Inspect changed files and available status checks**. If CI is absent, report `no automated CI checks configured/observed`; do not interpret absence as a pass.

- [ ] **Step 9: Merge verified PR to `main`** using squash unless repository constraints require another supported method; never force-update `main`.

- [ ] **Step 10: Post-merge fetch** of `README.md`, `SKILL.md`, templates, amendment, and Scenario 9 from `main`; confirm Framework `1.1.1`, Schema `1.0.0`, and canonical new-project bootstrap language.

- [ ] **Step 11: Report** PR/commit identifiers, merged state, versions, bootstrap read order, and that existing projects remain pinned until governed migration.
