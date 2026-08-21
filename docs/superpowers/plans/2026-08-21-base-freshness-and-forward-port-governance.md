# Base Freshness and Forward-Port Governance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Release Framework 1.2.2 with governance that keeps new Git worktrees/branches on a fresh canonical base, distinguishes non-semantic from semantic upstream drift, and requires Forward-Port rather than blind merge when stale work no longer matches current Framework semantics.

**Architecture:** Add pressure scenarios first, then one normative Base Freshness / Forward-Port contract to Core Governance and the root `00` template. Mirror operational behavior into `SKILL.md` and the mockup `00` starter. Package as a backward-compatible 1.2.2 governance patch with a new amendment and aligned release/version surfaces. No executable Git enforcement or CI is introduced.

**Tech Stack:** Markdown/YAML governance artifacts, Git/GitHub branch workflow, manual/agent semantic validation. No application runtime, hook, bot, validator, CI workflow, scheduler, or branch-protection automation.

**Spec:** `docs/superpowers/specs/2026-08-21-base-freshness-and-forward-port-governance-design.md`

## Global Constraints

- Independent new Git work starts from a freshly verified canonical integration target, not the currently checked-out feature branch.
- For ProjectFramework, the canonical integration target is repository `main`; freshness is evaluated against current remote/canonical `main`, not assumed local `main`.
- Feature-on-feature ancestry is permitted only as explicit `STACKED_WORK` with parent dependency and integration order discoverable.
- Base freshness vocabulary is `FRESH | STALE_NON_SEMANTIC | STALE_SEMANTIC | UNKNOWN`.
- `BASE_STALE`, `REBASE_REQUIRED`, and `FORWARD_PORT_REQUIRED` are workflow conditions/dispositions, not new Stable-ID families or Project lifecycle states.
- Commit count is never the semantic staleness threshold.
- Non-semantic upstream drift may be resolved by rebase for private/rewritable work or merge/update for shared/public branches; do not mandate history rewriting.
- Semantic upstream drift requires re-evaluation and normally `FORWARD_PORT_REQUIRED` into a clean branch/worktree from current canonical target.
- A conflict-free Git merge/rebase does not prove semantic compatibility.
- Pre-merge acceptance rechecks the current target head; target movement after review can make the prior review stale.
- Existing initialized Projects remain locally pinned and never auto-upgrade from upstream.
- Framework 1.2.2 remains Schema 1.0.0 with no semantic-slot or Stable-ID namespace change.
- This release is governance/documentation only; no Git hooks, bots, Actions, validators, schedulers, or enforcement automation.

---

## Distribution File Map

### Existing files to modify

```text
README.md
managing-project-source/FRAMEWORK-RELEASE.yaml
managing-project-source/SKILL.md
managing-project-source/references/core-governance-rules.md
managing-project-source/templates/00-project-source-framework.md
managing-project-source/templates/project-source-mockup/00-Project-Source-Framework.template.md
managing-project-source/templates/project-source-mockup/README.md
managing-project-source/tests/pressure-scenarios.md
```

### New file

```text
managing-project-source/references/framework-governance-amendment-260821-1505.md
```

### Release-stamp set

Before calling 1.2.2 release-ready, update `project_source_framework_version` / current distribution version stamps from `1.2.1` to `1.2.2` across active starter templates under `managing-project-source/templates/project-source-mockup/`. Do not rewrite historical amendments/examples merely to display the new version.

---

### Task 1: Add RED pressure scenarios for stale Git bases

**Files:**
- Modify: `managing-project-source/tests/pressure-scenarios.md`

**Interfaces:**
- Consumes: approved design spec.
- Produces: scenarios 33–40 defining the behavior all later normative changes must satisfy.

- [ ] **Step 1: Append scenarios 33–40 before `GREEN Run Instructions`**

Add tests for:

```text
33 Independent Worktree From Feature Branch Pressure
34 Stale Local Main vs Current origin/main Pressure
35 Non-Semantic Upstream Drift Pressure
36 Framework Semantic Drift Pressure
37 Conflict-Free But Semantically Stale Merge Pressure
38 Explicit Stacked Work Pressure
39 Clean Forward-Port Pressure
40 Target Moves After Review Pressure
```

Each uses the existing `Prompt / Temptation / Pass / Fail / GREEN expectation` structure.

- [ ] **Step 2: Verify RED conceptually**

Before normative edits, confirm current `SKILL.md` / Core Governance do not yet define all of:

```text
STACKED_WORK
STALE_NON_SEMANTIC
STALE_SEMANTIC
BASE_STALE
REBASE_REQUIRED
FORWARD_PORT_REQUIRED
```

Expected: at least these contract markers are missing from current normative files.

- [ ] **Step 3: Commit**

```bash
git add managing-project-source/tests/pressure-scenarios.md
git commit -m "test: add base freshness and forward-port pressure scenarios"
```

---

### Task 2: Add normative Base Freshness / Forward-Port contract

**Files:**
- Modify: `managing-project-source/references/core-governance-rules.md`
- Modify: `managing-project-source/templates/00-project-source-framework.md`
- Modify: `managing-project-source/templates/project-source-mockup/00-Project-Source-Framework.template.md`

**Interfaces:**
- Consumes: Task 1 pressure scenarios.
- Produces: binding semantics for Git-backed work packages and pinned Project-local root governance.

- [ ] **Step 1: Add Core Governance subsection near migration/versioning/preflight**

Define:

```text
Canonical Integration Target
Base Snapshot
Independent Work
STACKED_WORK
FRESH
STALE_NON_SEMANTIC
STALE_SEMANTIC
UNKNOWN
BASE_STALE
REBASE_REQUIRED
FORWARD_PORT_REQUIRED
```

Normative rules must require latest-target-first for independent work, checkpoint freshness checks, semantic/non-semantic drift classification, safe shared/public history handling, semantic Forward-Port, clean integration, and pre-merge target-head recheck.

- [ ] **Step 2: Add compact Project-local binding section to full `00` template**

Include the conceptual flow:

```text
Independent Git work → fresh canonical integration target
Feature-on-feature dependency → explicit STACKED_WORK
Non-semantic stale base → update/rebase appropriately
Semantic stale base → FORWARD_PORT_REQUIRED
Before merge → Base Freshness Gate against current target head
Git conflict-free ≠ semantic acceptance
```

- [ ] **Step 3: Add mockup `00` pointer**

Point to the full root template; do not duplicate the entire contract.

- [ ] **Step 4: Verify Task 2 contract markers**

All three normative/starter files should resolve the new contract without creating a new Stable-ID namespace or automation requirement.

- [ ] **Step 5: Commit**

```bash
git add managing-project-source/references/core-governance-rules.md managing-project-source/templates/00-project-source-framework.md managing-project-source/templates/project-source-mockup/00-Project-Source-Framework.template.md
git commit -m "feat: govern Git base freshness and forward-port integration"
```

---

### Task 3: Mirror operational workflow into the managing skill

**Files:**
- Modify: `managing-project-source/SKILL.md`

**Interfaces:**
- Consumes: Task 2 normative contract.
- Produces: agent-facing operating sequence, quick-reference decisions, and red flags.

- [ ] **Step 1: Add `Git Base Freshness and Worktree/Branch Integration` section**

Operational sequence:

```text
resolve canonical integration target
→ fresh-read/fetch target
→ classify Independent vs STACKED_WORK
→ create work from verified current base
→ checkpoint freshness
→ classify non-semantic vs semantic drift
→ update/rebase OR Forward-Port
→ pre-merge target-head recheck
```

- [ ] **Step 2: Update Workflow**

Add a conditional step when Git worktrees/branches are used. Do not force Git workflow on non-Git Projects.

- [ ] **Step 3: Update Quick Reference**

Add rows for independent worktree, stacked work, non-semantic stale base, semantic stale base, and pre-merge base freshness.

- [ ] **Step 4: Update Red Flags**

Include creating independent work from the currently checked-out feature branch by default, assuming local `main` is current, blind merge of semantic stale work, treating conflict-free merge as acceptance, and rewriting shared branch history merely to satisfy rebase preference.

- [ ] **Step 5: Commit**

```bash
git add managing-project-source/SKILL.md
git commit -m "feat: add base freshness workflow to managing skill"
```

---

### Task 4: Package Framework 1.2.2 release identity

**Files:**
- Create: `managing-project-source/references/framework-governance-amendment-260821-1505.md`
- Modify: `managing-project-source/FRAMEWORK-RELEASE.yaml`
- Modify: `README.md`
- Modify: `managing-project-source/templates/project-source-mockup/README.md`
- Modify: current version stamps in active mockup starter templates.

**Interfaces:**
- Consumes: Tasks 1–3.
- Produces: release identity and discoverability for Framework 1.2.2 / Schema 1.0.0.

- [ ] **Step 1: Write the 1.2.2 amendment**

Header:

```yaml
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.2.1"
project_source_framework_version: "1.2.2"
project_source_schema_version: "1.0.0"
approved_at: "2026-08-21T15:05:00+07:00"
approval_basis: "USER_EXPLICIT_APPROVAL"
compatibility: "BACKWARD_COMPATIBLE_GIT_BASE_FRESHNESS_AND_FORWARD_PORT_GOVERNANCE"
```

- [ ] **Step 2: Update release descriptor**

Set `framework_version: "1.2.2"` and latest amendment to the new file. Preserve canonical bootstrap `main` and optional assurance semantics.

- [ ] **Step 3: Update README**

Current Release becomes 1.2.2; add a concise `Framework 1.2.2 Additions` section before 1.2.1 describing latest-main-first independent work, explicit stacked work, semantic drift, Forward-Port, and pre-merge freshness gate.

- [ ] **Step 4: Align current mockup starter version stamps**

Change active starter metadata/provenance references from 1.2.1 to 1.2.2 while retaining historical narrative labels such as `Framework 1.2.0 Extended Semantics` where they describe introduction history.

- [ ] **Step 5: Commit**

```bash
git add README.md managing-project-source/FRAMEWORK-RELEASE.yaml managing-project-source/references/framework-governance-amendment-260821-1505.md managing-project-source/templates/project-source-mockup
git commit -m "release: prepare Framework 1.2.2 base freshness governance"
```

---

### Task 5: Release verification

**Files:**
- Read/verify all modified files; no production-file changes unless verification finds a defect.

**Interfaces:**
- Consumes: Tasks 1–4.
- Produces: evidence that the branch is ready for PR review.

- [ ] **Step 1: Verify branch base and divergence**

Confirm branch descends from `main@0dbfce789486f6c28853d3abfff0966f1ab8256d` and contains only intended feature commits.

- [ ] **Step 2: Verify contract markers**

Require new pressure scenarios plus the following in Core Governance and `SKILL.md`:

```text
STACKED_WORK
STALE_NON_SEMANTIC
STALE_SEMANTIC
BASE_STALE
REBASE_REQUIRED
FORWARD_PORT_REQUIRED
```

- [ ] **Step 3: Verify version consistency**

Current distribution surfaces must agree on Framework 1.2.2 / Schema 1.0.0. Historical amendments/examples remain historically pinned.

- [ ] **Step 4: Verify no accidental automation scope**

No GitHub Actions, hooks, bots, validator/CLI, branch-protection enforcement, scheduler, or runtime files are added.

- [ ] **Step 5: Verify platform launchers unchanged**

Because the new contract is reached through canonical read-through, ChatGPT/Claude launchers should remain byte-for-byte unchanged in this feature unless a demonstrated gap requires otherwise. Existing <=4,500-character and shared-contract invariants remain preserved.

- [ ] **Step 6: Review final diff and open PR**

PR summary should emphasize:

```text
Latest-main-first for independent work
Explicit STACKED_WORK exception
Base Freshness Gate
Semantic drift → Forward-Port
Mergeable ≠ Acceptable
No automation/runtime scope
Schema unchanged at 1.0.0
```
