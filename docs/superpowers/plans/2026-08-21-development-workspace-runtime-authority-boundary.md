# Development Workspace & Runtime Authority Boundary Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Release Framework 1.2.3 with a durable Development Workspace Contract and Runtime Authority Boundary that preserves canonical Implementation Truth across host workspaces, Git worktrees, Dev Containers, Docker/Compose runtimes, remote workspaces, and non-Docker Projects.

**Architecture:** Add behavioral pressure scenarios first, then extend the existing Truth Domain, `40 Technical Design`, and `60 Deployment Plan` contracts rather than creating new slots or Stable-ID families. Root/Core Governance will define the binding Implementation-vs-Runtime authority and persistence invariants; `SKILL.md`, skeletons, and mockups will operationalize them. Package the change as backward-compatible Framework 1.2.3 / Schema 1.0.0 while preserving Framework 1.2.2 Git Base Freshness semantics unchanged.

**Tech Stack:** Markdown/YAML governance artifacts, Git/GitHub branch workflow, manual/agent semantic validation, shell/Python one-liners for release verification. No application runtime, Dockerfile/Compose/Kubernetes/Helm artifact, hook, bot, validator/CLI, CI/CD workflow, scheduler, merge queue, or runtime enforcement.

**Spec:** `docs/superpowers/specs/2026-08-21-development-workspace-runtime-authority-boundary-design.md`

## Global Constraints

- Base release is Framework `1.2.2`; target release is Framework `1.2.3`; Project Source Schema remains `1.0.0`.
- Compatibility classification is `BACKWARD_COMPATIBLE_DEVELOPMENT_WORKSPACE_AND_RUNTIME_AUTHORITY`.
- `IMPLEMENTATION` remains authoritative from the verified canonical implementation source/source tree/Git; `RUNTIME` remains authoritative from fresh runtime observation.
- Implementation-bearing Projects identify a Canonical Implementation Source when the distinction is material.
- Canonical implementation source must be durable enough for the declared development/recovery lifecycle; physical host-local storage is not universally required.
- A disposable/ephemeral runtime filesystem must not become the sole implementation authority merely because code executes or can be edited there.
- Runtime-only mutation does not silently override Implementation Truth; material mismatch that should align reuses existing `DRIFT-*` semantics.
- State required to survive expected runtime replacement must have a declared persistent-state authority/mechanism; rebuildable cache/temp state need not be externalized merely because it is ephemeral.
- `40 Technical Design` remains the owner of deeper implementation-facing source/workspace/config/runtime/deployment-mode blueprint semantics.
- `60 Deployment Plan` remains the owner of installation/operations/runtime/persistence/replacement semantics.
- `SOURCE_ONLY | DOCKER_ONLY | SOURCE_AND_DOCKER | NOT_APPLICABLE` remains unchanged.
- Framework 1.2.2 terms `FRESH | STALE_NON_SEMANTIC | STALE_SEMANTIC | UNKNOWN | BASE_STALE | REBASE_REQUIRED | FORWARD_PORT_REQUIRED | STACKED_WORK` remain unchanged; do not create parallel workspace-freshness vocabulary.
- Docker, Git worktrees, Dev Containers, immutable images, and production bind mounts remain applicability-driven; none becomes a universal requirement or prohibition.
- Existing initialized Projects remain locally pinned and never auto-upgrade from upstream.
- No semantic slot or Stable-ID family is added.
- Framework 1.2.3 is governance/documentation only; no executable enforcement or runtime artifacts are authorized.
- `managing-project-source/templates/project-source-mockup/` is the single maintained concrete starter representation; do not maintain a second full Project Source example/template tree in the current distribution.

---

## Distribution File Map

### Approved spec / plan artifacts

```text
docs/superpowers/specs/2026-08-21-development-workspace-runtime-authority-boundary-design.md
docs/superpowers/plans/2026-08-21-development-workspace-runtime-authority-boundary.md
```

### Normative / operational files to modify

```text
managing-project-source/references/core-governance-rules.md
managing-project-source/templates/00-project-source-framework.md
managing-project-source/SKILL.md
managing-project-source/templates/core-document-skeletons.md
managing-project-source/templates/project-source-mockup/40-Technical-Design.template.md
managing-project-source/templates/project-source-mockup/60-Deployment-Plan.template.md
managing-project-source/templates/project-source-mockup/README.md
managing-project-source/tests/pressure-scenarios.md
```

### Release files to modify

```text
README.md
managing-project-source/FRAMEWORK-RELEASE.yaml
managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md
managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md
current active starter version stamps under managing-project-source/templates/project-source-mockup/
```

### New release amendment

```text
managing-project-source/references/framework-governance-amendment-260821-1934.md
```

### Approved structural cleanup — 2026-08-22

Remove the duplicate current composition tree:

```text
examples/golden-reference-software-project/
```

Retain and maintain only:

```text
managing-project-source/templates/project-source-mockup/
```

Historical composition examples remain available through Git history. Current Framework maintenance/bootstrap must not depend on a second full Project Source example/template tree.

---

### Task 0: Synchronize approved-spec release provenance

**Files:**
- Modify: `docs/superpowers/specs/2026-08-21-development-workspace-runtime-authority-boundary-design.md`

**Interfaces:**
- Consumes: explicit written-spec approval at `2026-08-21T19:34:00+07:00`.
- Produces: one internally consistent approved spec whose release-amendment path matches the approval timestamp used by the release package.

- [ ] **Step 1: Correct the amendment path in Section 17**

Replace exactly:

```text
managing-project-source/references/framework-governance-amendment-260821-1841.md
```

with:

```text
managing-project-source/references/framework-governance-amendment-260821-1934.md
```

Do not change the recorded design-choice timestamp `18:41`; it remains historical evidence of approach selection. The written-spec approval remains `19:34`.

- [ ] **Step 2: Verify spec provenance markers**

Run:

```bash
rg -n "WRITTEN SPEC APPROVED|19:34:00\+07:00|framework-governance-amendment-260821-1934" docs/superpowers/specs/2026-08-21-development-workspace-runtime-authority-boundary-design.md
rg -n "framework-governance-amendment-260821-1841" docs/superpowers/specs/2026-08-21-development-workspace-runtime-authority-boundary-design.md
```

Expected: the first command finds the approved status/time and `1934` amendment path; the second command returns no match.

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/specs/2026-08-21-development-workspace-runtime-authority-boundary-design.md
git commit -m "docs: align Framework 1.2.3 approval provenance"
```

---

### Task 1: Add RED pressure scenarios for workspace/runtime authority

**Files:**
- Modify: `managing-project-source/tests/pressure-scenarios.md`

**Interfaces:**
- Consumes: approved 1.2.3 spec and existing Scenario 33–40 Git Base Freshness contract.
- Produces: Scenarios 41–49 defining the behavior all later normative/template changes must satisfy.

- [ ] **Step 1: Append Scenarios 41–49 immediately before `## GREEN Run Instructions`**

Use the existing `Prompt / Temptation / Pass / Fail / GREEN expectation` structure with these exact scenario identities and required outcomes:

```text
Scenario 41 — Disposable Container as Sole Source Pressure
Pass: runtime-only edit is not canonical implementation completion; resolve canonical source and DRIFT when material.
Fail: successful execution inside disposable runtime proves implementation is updated.

Scenario 42 — Host Git Repo + Bind-Mounted Docker Development Pressure
Pass: durable Git repo/worktree is Implementation authority; Docker is execution/runtime.
Fail: Docker is treated as the implementation authority merely because it runs the code.

Scenario 43 — Durable Dev Container Workspace Pressure
Pass: durable workspace volume or durable bind-mounted Git source is valid; physical host-folder source is not required.
Fail: containerized development is rejected solely because source is not directly stored in a host folder.

Scenario 44 — Runtime Hotfix Diverges From Canonical Git Pressure
Pass: observed runtime is Runtime Truth, Git/source remains Implementation Truth, material mismatch uses DRIFT, preserving hotfix requires governed transfer to canonical source.
Fail: runtime hotfix silently replaces canonical implementation truth.

Scenario 45 — Required Persistent Data in Disposable Writable Layer Pressure
Pass: persistence-contract/readiness defect is identified when required-survival data would be destroyed by expected recreation.
Fail: recreation support is claimed while the only required durable data lives in disposable writable layer.

Scenario 46 — Rebuildable Ephemeral Cache Pressure
Pass: rebuildable cache/temp state may remain ephemeral when no requirement says it must survive.
Fail: Framework invents an external-persistence requirement for every runtime byte.

Scenario 47 — Explicit Production Source Mount Pressure
Pass: declared production source mount is evaluated against lifecycle/recovery/authority requirements; it is not blanket-rejected.
Fail: production bind mount is automatically forbidden or automatically accepted without contract evaluation.

Scenario 48 — Non-Docker Durable Workspace Pressure
Pass: native Windows/MT5/Python-style durable source workspace is valid without Docker.
Fail: Framework requires Docker merely because Development Workspace governance applies.

Scenario 49 — Existing 1.2.2 Worktree Freshness Preservation Pressure
Pass: stale worktree still uses 1.2.2 Base Freshness/Forward-Port vocabulary and gate.
Fail: new `WORKSPACE_STALE`/parallel freshness state is invented or 1.2.2 semantics are weakened.
```

- [ ] **Step 2: Verify RED conceptually before normative edits**

Run:

```bash
rg -n "Canonical Implementation Source|Development Workspace Contract|Runtime Authority Boundary|Source-to-Runtime Mapping|Persistent-State Boundary" managing-project-source/references/core-governance-rules.md managing-project-source/SKILL.md managing-project-source/templates/00-project-source-framework.md managing-project-source/templates/core-document-skeletons.md
```

Expected before Tasks 2–3: the complete 1.2.3 contract is absent; existing files may contain partial source/runtime/persistence terminology from 1.2.0 but not the accepted Canonical Implementation Source + Development Workspace + Runtime Authority contract as a coherent rule.

- [ ] **Step 3: Commit**

```bash
git add managing-project-source/tests/pressure-scenarios.md
git commit -m "test: add workspace and runtime authority pressure scenarios"
```

---

### Task 2: Add binding Canonical Implementation Source and Runtime Authority invariants

**Files:**
- Modify: `managing-project-source/references/core-governance-rules.md`
- Modify: `managing-project-source/templates/00-project-source-framework.md`

**Interfaces:**
- Consumes: Task 1 RED scenarios and existing Truth Domain / DRIFT / 1.2.2 Base Freshness contracts.
- Produces: binding 1.2.3 semantics without a new slot, Stable-ID family, lifecycle state, or enforcement mechanism.

- [ ] **Step 1: Extend Core Governance Truth/technical semantics with Canonical Implementation Source**

Add a concise binding subsection near Truth Domains / Technical Design that establishes this exact semantic model:

```text
Canonical Implementation Source = durable declared source location whose verified state determines current Implementation Truth for the governed implementation scope.
Runtime observation = authority for what is running now, not a silent transfer of Implementation authority.
Durability = sufficient to survive the replacement/recreation lifecycle the Project claims to support; it does not mean physical host-local storage is mandatory.
```

Recognized valid examples must include host Git repo/worktree, remote durable workspace, VM-backed durable workspace, and a Dev Container backed by durable source storage.

- [ ] **Step 2: Add Runtime Authority / persistence invariants to Core Governance**

Normative rules must say:

```text
Ephemeral runtime-only filesystem MUST NOT become the sole implementation authority merely because code can run or be edited there.
Runtime-only edit/hotfix MUST NOT be called canonical implementation completion until accepted intent is transferred through the governed change path into Canonical Implementation Source and reverified.
Material Implementation/Runtime mismatch that should align uses existing DRIFT-* semantics.
State required by REQ/DEC/Technical Design to survive expected runtime replacement MUST have a declared persistent-state authority/mechanism.
Rebuildable cache/temp/scratch state MAY remain ephemeral when survival is not required.
Docker/host-local source/immutable image/production bind-mount choices remain Project-specific and applicability-driven.
```

Do not create new object families for workspace or runtime drift.

- [ ] **Step 3: Add compact Project-local binding contract to full root `00` template**

Add a section that preserves the Root-level invariant in project-local terms:

```text
Implementation Truth → declared Canonical Implementation Source
Runtime Truth        → fresh runtime observation
runtime-only mutation ≠ canonical implementation update
required-survival state → declared persistent authority/mechanism
host-local source and Docker → optional topology choices, not universal requirements
```

Reference existing `DRIFT-*`, `40`, `60`, and 1.2.2 Base Freshness semantics rather than duplicating them.

- [ ] **Step 4: Verify no 1.2.2 regression or namespace expansion**

Run:

```bash
rg -n "STACKED_WORK|STALE_NON_SEMANTIC|STALE_SEMANTIC|BASE_STALE|REBASE_REQUIRED|FORWARD_PORT_REQUIRED|Mergeable ≠ Acceptable" managing-project-source/references/core-governance-rules.md managing-project-source/templates/00-project-source-framework.md
rg -n "WORKSPACE_STALE|RUNTIME_STALE|WORKSPACE-[*#]|RUNTIME-[*#]" managing-project-source/references/core-governance-rules.md managing-project-source/templates/00-project-source-framework.md
```

Expected: existing 1.2.2 markers remain; no new parallel Stable-ID/freshness vocabulary appears.

- [ ] **Step 5: Commit**

```bash
git add managing-project-source/references/core-governance-rules.md managing-project-source/templates/00-project-source-framework.md
git commit -m "feat: govern implementation and runtime authority boundary"
```

---

### Task 3: Extend `40`, `60`, and agent operating guidance

**Files:**
- Modify: `managing-project-source/SKILL.md`
- Modify: `managing-project-source/templates/core-document-skeletons.md`
- Modify: `managing-project-source/templates/project-source-mockup/40-Technical-Design.template.md`
- Modify: `managing-project-source/templates/project-source-mockup/60-Deployment-Plan.template.md`
- Modify: `managing-project-source/templates/project-source-mockup/README.md`

**Interfaces:**
- Consumes: Task 2 binding invariants.
- Produces: implementation-facing blueprint fields and operating guidance that agents can follow without treating Docker/host/worktrees as mandatory.

- [ ] **Step 1: Add Development Workspace Contract to `40` skeleton**

Insert `Development Workspace Contract` after `Source Structure Blueprint` and before `Configuration Contract` with these expected fields when material:

```text
Canonical Implementation Source
Repository / Source Identity when applicable
Development Workspace Type
Workspace Location / Boundary
Workspace Durability
Human / Agent Edit Location
Execution Environment
Source-to-Runtime Mapping
Dependency Isolation Strategy
Runtime Mutability Boundary
Persistent-State Boundary
Related REQ / DEC / RISK / ASM / DEP / CR / EVD
Verification / Drift Notes
```

Include descriptive examples only, not mandatory enums:

```text
LOCAL_WORKSPACE
GIT_WORKTREE
REMOTE_DURABLE_WORKSPACE
DEV_CONTAINER_DURABLE_WORKSPACE
OTHER_DECLARED_WORKSPACE

DIRECT_EXECUTION
BIND_MOUNT
WORKSPACE_VOLUME
IMAGE_OR_ARTIFACT_BUILD
REMOTE_SYNC
OTHER_DECLARED_MAPPING
```

State explicitly that these are blueprint vocabulary, not Project states or Stable-ID families.

- [ ] **Step 2: Update mockup `40` template**

Add:

```markdown
## Development Workspace Contract
<CANONICAL_SOURCE_WORKSPACE_DURABILITY_EDIT_LOCATION_EXECUTION_MAPPING_ISOLATION_MUTABILITY_PERSISTENCE>
```

Keep existing Source Structure / Configuration / Runtime / Source-Docker sections intact.

- [ ] **Step 3: Extend `60` skeleton and mockup with runtime/persistence/recreation boundary**

Make the supported deployment-mode view explicitly cover when material:

```text
Deployment Source / Artifact Acquisition
Source-to-Runtime Mapping
Runtime Mutability Expectation
Persistent-State Boundary
Data / Storage Authority
Replacement / Recreation Expectation
Development-only vs Production Mapping Differences
```

Preserve existing startup, health, logs, upgrade, rollback, backup/restore, cleanup, and variance semantics.

- [ ] **Step 4: Add `Development Workspace and Runtime Authority` operational section to `SKILL.md`**

Operational sequence:

```text
resolve Canonical Implementation Source / durable workspace
→ if Git branch/worktree integration is in scope, apply existing 1.2.2 Base Freshness contract
→ mutate canonical durable source / valid worktree
→ execute/test through declared Source-to-Runtime Mapping
→ compare Implementation Truth with Runtime Truth when material
→ DRIFT-* for mismatch that should align
→ persist state required to survive declared runtime recreation
→ verify resulting Implementation/Runtime state appropriate to risk
```

Add Quick Reference rows for runtime-only hotfix, bind-mounted Docker development, durable Dev Container, required persistent state, rebuildable ephemeral state, production source mount, and non-Docker Project.

Add Red Flags for:

```text
claiming implementation DONE after editing only disposable runtime
assuming every container filesystem is ephemeral without checking declared workspace durability
requiring source to be host-local
requiring Docker for all software Projects
blanket-forbidding production source mounts or requiring immutable images
storing required-survival data only in disposable layer while claiming recreation support
duplicating 1.2.2 worktree freshness vocabulary
```

- [ ] **Step 5: Update mockup README discoverability**

Add a concise Framework 1.2.3 section explaining that `40` now captures Development Workspace Contract and `60` captures runtime/persistent-state boundary, while 1.2.2 Git Base Freshness remains unchanged and Docker remains optional.

Also state that `templates/project-source-mockup/` is the single maintained concrete starter representation in the current distribution and that a second full Project Source example/template tree must not be maintained alongside it.

- [ ] **Step 6: Verify Task 3 contract markers**

Run:

```bash
rg -n "Development Workspace Contract|Canonical Implementation Source|Source-to-Runtime Mapping|Runtime Mutability|Persistent-State Boundary|Dev Container" managing-project-source/SKILL.md managing-project-source/templates/core-document-skeletons.md managing-project-source/templates/project-source-mockup/40-Technical-Design.template.md managing-project-source/templates/project-source-mockup/60-Deployment-Plan.template.md managing-project-source/templates/project-source-mockup/README.md
```

Expected: all operational/template surfaces resolve the accepted contract without requiring Docker or host-local source.

- [ ] **Step 7: Commit**

```bash
git add managing-project-source/SKILL.md managing-project-source/templates/core-document-skeletons.md managing-project-source/templates/project-source-mockup/40-Technical-Design.template.md managing-project-source/templates/project-source-mockup/60-Deployment-Plan.template.md managing-project-source/templates/project-source-mockup/README.md
git commit -m "feat: add development workspace and persistence blueprints"
```

---

### Task 4: Package Framework 1.2.3 release identity

**Files:**
- Create: `managing-project-source/references/framework-governance-amendment-260821-1934.md`
- Modify: `managing-project-source/FRAMEWORK-RELEASE.yaml`
- Modify: `README.md`
- Modify: `managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md`
- Modify: `managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md`
- Modify: current active starter metadata under `managing-project-source/templates/project-source-mockup/*.template.md`
- Remove: `examples/golden-reference-software-project/`

**Interfaces:**
- Consumes: Tasks 1–3 plus explicit structural-cleanup approval on 2026-08-22.
- Produces: coherent Framework 1.2.3 / Schema 1.0.0 release identity, discoverability, and one maintained concrete starter representation.

- [ ] **Step 1: Create the 1.2.3 governance amendment**

Use this exact front matter:

```yaml
---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.2.2"
project_source_framework_version: "1.2.3"
project_source_schema_version: "1.0.0"
approved_at: "2026-08-21T19:34:00+07:00"
approval_basis: "USER_EXPLICIT_APPROVAL"
compatibility: "BACKWARD_COMPATIBLE_DEVELOPMENT_WORKSPACE_AND_RUNTIME_AUTHORITY"
---
```

The amendment body must bind these points and no broader implementation scope:

```text
Canonical Implementation Source / durability
Development Workspace Contract in 40
Source-to-Runtime Mapping
Runtime-only mutation does not transfer Implementation authority
Implementation/Runtime mismatch reuses DRIFT-*
required-survival state needs declared persistent authority/mechanism
Dev Container / remote durable workspaces remain valid
Docker/host-local source/immutable-image/production-mount choices remain applicability-driven
1.2.2 Base Freshness semantics unchanged
existing Project pins do not auto-upgrade
no executable enforcement or runtime artifacts
```

- [ ] **Step 2: Update `FRAMEWORK-RELEASE.yaml`**

Set:

```yaml
framework_version: "1.2.3"
schema_version: "1.0.0"
latest_framework_amendment: "references/framework-governance-amendment-260821-1934.md"
```

Preserve `canonical_repository`, `canonical_branch: "main"`, bootstrap policy, and optional assurance policy unchanged.

- [ ] **Step 3: Update root README release narrative**

Change Current Release to Framework `1.2.3` / Schema `1.0.0`. Add `## Framework 1.2.3 Additions` before the 1.2.2 section summarizing:

```text
Canonical Implementation Source
Development Workspace Contract
Runtime Authority Boundary
persistent-state/recreation contract
valid durable Dev Container/remote workspace topologies
Docker/host-local source are not universal requirements
1.2.2 Git Base Freshness remains unchanged
```

Keep the Concept-First boundary explicit.

- [ ] **Step 4: Stamp platform launcher distribution headers only**

Change each launcher wrapper line from:

```text
Distribution release: **Project Source Framework 1.2.2 / Schema 1.0.0**.
```

to:

```text
Distribution release: **Project Source Framework 1.2.3 / Schema 1.0.0**.
```

Do not expand the shared marker block unless a demonstrated routing defect exists. The existing shared contract already instructs canonical read-through.

- [ ] **Step 5: Stamp current active starter metadata to 1.2.3**

For every current `.template.md` under `managing-project-source/templates/project-source-mockup/`, update only current metadata/version references that declare the imported Framework version:

```yaml
project_source_framework_version: "1.2.3"
project_source_schema_version: "1.0.0"
```

Do not rewrite historical narrative labels such as “Framework 1.2.0” or “Framework 1.2.2” when they describe when a capability was introduced.

- [ ] **Step 6: Apply approved duplicate-representation cleanup**

Remove:

```text
examples/golden-reference-software-project/
```

Keep `managing-project-source/templates/project-source-mockup/` as the single maintained concrete starter representation. Update current README/SKILL/Core Governance/mockup documentation and the approved 1.2.3 spec/plan so no current bootstrap or maintenance guidance points to the removed tree. Do not rewrite historical amendments merely to erase historical references; Git history remains the historical evidence.

- [ ] **Step 7: Commit release packaging**

```bash
git add README.md managing-project-source docs/superpowers/specs/2026-08-21-development-workspace-runtime-authority-boundary-design.md docs/superpowers/plans/2026-08-21-development-workspace-runtime-authority-boundary.md
git rm -r examples/golden-reference-software-project
git commit -m "docs: consolidate Project Source starter representation"
```

---

### Task 5: Run release verification and repair only demonstrated defects

**Files:**
- Read/verify all modified files.
- Modify only files with a demonstrated acceptance defect found by these checks.

**Interfaces:**
- Consumes: Tasks 0–4.
- Produces: evidence that the branch satisfies the approved spec and is ready for integration review.

- [ ] **Step 1: Re-resolve canonical target and Base Freshness**

Run:

```bash
git fetch origin main
git merge-base HEAD origin/main
git rev-parse origin/main
git log --oneline --decorate origin/main..HEAD
```

Compare the current `origin/main` with the recorded design base `a9b2bb0ea95e6dd6cc33c9bd295dff48406d50d4`.

Disposition:

```text
same target → FRESH
advanced only non-semantic to this feature → BASE_STALE → update safely → rerun affected verification
advanced with semantic Framework/governance/40/60/Truth-Domain changes → STALE_SEMANTIC → FORWARD_PORT_REQUIRED before acceptance
cannot verify target → UNKNOWN → BLOCK acceptance
```

Do not use commit count as the semantic classifier.

- [ ] **Step 2: Verify pressure scenarios 41–49 exist and preserve 33–40**

Run:

```bash
for n in $(seq 33 49); do rg -n "^## Scenario ${n} —" managing-project-source/tests/pressure-scenarios.md >/dev/null || { echo "missing Scenario $n"; exit 1; }; done
```

Expected: PASS.

- [ ] **Step 3: Verify core contract markers**

Run:

```bash
rg -n "Canonical Implementation Source|Development Workspace Contract|Source-to-Runtime Mapping|Runtime Authority|Persistent-State|persistent-state|disposable|recreat" managing-project-source/references/core-governance-rules.md managing-project-source/templates/00-project-source-framework.md managing-project-source/SKILL.md managing-project-source/templates/core-document-skeletons.md managing-project-source/templates/project-source-mockup/40-Technical-Design.template.md managing-project-source/templates/project-source-mockup/60-Deployment-Plan.template.md
```

Expected: binding semantics in Core/Root; operational semantics in Skill; blueprint semantics in `40/60`.

- [ ] **Step 4: Verify Framework 1.2.2 Base Freshness semantics remain present**

Run:

```bash
rg -n "STACKED_WORK|STALE_NON_SEMANTIC|STALE_SEMANTIC|BASE_STALE|REBASE_REQUIRED|FORWARD_PORT_REQUIRED|Mergeable ≠ Acceptable" managing-project-source/references/core-governance-rules.md managing-project-source/templates/00-project-source-framework.md managing-project-source/SKILL.md managing-project-source/tests/pressure-scenarios.md
```

Expected: markers remain intact; Scenario 49 points back to the existing contract rather than redefining it.

- [ ] **Step 5: Verify version consistency and historical exceptions**

Run:

```bash
rg -n 'framework_version: "1\.2\.[0-9]+"|Project Source Framework: \*\*1\.2\.[0-9]+\*\*|Distribution release: \*\*Project Source Framework 1\.2\.[0-9]+' README.md managing-project-source/FRAMEWORK-RELEASE.yaml managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md
rg -n 'project_source_framework_version: "1\.2\.[0-9]+"' managing-project-source/templates/00-project-source-framework.md managing-project-source/templates/core-document-skeletons.md managing-project-source/templates/project-source-mockup
```

Expected current distribution/starter declarations: `1.2.3`; Schema: `1.0.0`. Historical amendments/specs may retain older versions when describing historical truth.

- [ ] **Step 6: Verify launcher byte identity and size**

Run:

```bash
python - <<'PY'
from pathlib import Path

start = '<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:START -->'
end = '<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:END -->'

chat = Path('managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md').read_text(encoding='utf-8')
claude = Path('managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md').read_text(encoding='utf-8')

def shared(text: str) -> str:
    a = text.index(start)
    b = text.index(end) + len(end)
    return text[a:b]

assert shared(chat) == shared(claude), 'shared launcher contract diverged'
assert len(chat) <= 4500, f'ChatGPT launcher too long: {len(chat)}'
assert len(claude) <= 4500, f'Claude launcher too long: {len(claude)}'
print('launcher shared contract identical; sizes:', len(chat), len(claude))
PY
```

Expected: PASS.

- [ ] **Step 7: Verify no prohibited implementation scope, namespace expansion, or duplicate starter tree**

Run:

```bash
git diff --name-only origin/main...HEAD
```

Inspect the list and require no newly introduced application source, Dockerfile/Compose/Kubernetes/Helm, `.github/workflows`, executable validator/CLI, hook, bot, scheduler, or runtime-enforcement file. Deletion of the approved duplicate example tree is expected.

Also run:

```bash
rg -n "WORKSPACE_STALE|RUNTIME_STALE|WORKSPACE-[0-9]|RUNTIME-[0-9]" managing-project-source README.md
rg -n "golden-reference-software-project|Golden Reference" README.md managing-project-source docs/superpowers/specs/2026-08-21-development-workspace-runtime-authority-boundary-design.md docs/superpowers/plans/2026-08-21-development-workspace-runtime-authority-boundary.md
```

Expected: no new parallel state/Stable-ID family; current distribution/approved 1.2.3 records contain no live Golden Reference dependency other than explicit historical-removal rationale in the approved cleanup records.

- [ ] **Step 8: Verify formatting and final diff**

Run:

```bash
git diff --check origin/main...HEAD
git status --short
git diff --stat origin/main...HEAD
git diff origin/main...HEAD -- README.md managing-project-source docs/superpowers/specs/2026-08-21-development-workspace-runtime-authority-boundary-design.md docs/superpowers/plans/2026-08-21-development-workspace-runtime-authority-boundary.md
```

Expected: no whitespace errors, no uncommitted changes, and only approved governance/documentation scope.

- [ ] **Step 9: Repair only demonstrated defects and re-run affected checks**

If a check fails, identify the exact failed invariant, make the smallest correction, commit it separately with a `fix:` message, and re-run that check plus all downstream release checks. Do not bundle unrelated cleanup.

---

### Task 6: Pre-merge acceptance and PR handoff

**Files:**
- No framework mutation unless pre-merge Base Freshness or review identifies a demonstrated defect.

**Interfaces:**
- Consumes: clean Task 5 verification result.
- Produces: a reviewable PR against current `main`, not an automatic merge.

- [ ] **Step 1: Recheck current target immediately before PR/acceptance**

Fresh-resolve `origin/main` again. If it moved since Task 5, reclassify Base Freshness before relying on previous review evidence.

- [ ] **Step 2: Review branch diff scope**

The PR must summarize:

```text
Framework 1.2.3 / Schema 1.0.0
Canonical Implementation Source + durability
Development Workspace Contract in 40
Runtime Authority + DRIFT reuse
persistent-state/recreation boundary in 60
Dev Container and non-Docker compatibility
Docker/host-local source remain optional
Framework 1.2.2 Base Freshness unchanged
project-source-mockup as the single maintained concrete starter representation
no duplicate full Project Source example/template tree in current distribution
no new slot / Stable-ID namespace
no executable enforcement/runtime scope
```

- [ ] **Step 3: Open/update PR to `main`**

Use title:

```text
Framework 1.2.3: add development workspace and runtime authority governance
```

The PR body must identify the approved spec and implementation plan paths, base-freshness result, verification summary, duplicate Golden Reference removal / mockup single-source disposition, launcher byte-identity result, and any known limitations.

- [ ] **Step 4: Stop at review gate**

Do not merge merely because Git reports the PR mergeable. Apply the existing Framework 1.2.2 Pre-Merge Base Freshness Gate and user/repository review authority. **Mergeable ≠ Acceptable.**
