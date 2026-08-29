# TASK-023 Self-Bootstrapping Project Contract Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Release Framework `1.7.0` with one stable vendor-neutral Project-root `PROJECT-BOOTSTRAP.md` discovery contract while preserving `FRAMEWORK-001` authority, Brownfield pinning, and existing binding/runtime separation.

**Architecture:** Add a maintained root-bootstrap template plus normative discovery semantics. Current Framework sources and starters route `PROJECT-BOOTSTRAP.md → 00 → 01 → 03`, with `09` for continuation; vendor launchers become optional thin adapters and Brownfield adoption remains `[Project Upgrade]`-only.

**Tech Stack:** Markdown, YAML, Git, PowerShell/Python structural verification.

**Spec:** `docs/superpowers/specs/2026-08-29-task023-self-bootstrapping-project-design.md`

## Global Constraints

- Target release: Framework `1.7.0` / Schema `1.0.0` / release format `3`.
- `PROJECT-BOOTSTRAP.md` is discovery/locator only; `FRAMEWORK-001` remains Project governance authority.
- Canonical route: `PROJECT-BOOTSTRAP.md → 00 → 01 → 03`; resolve `09 Handoff` for continuation.
- NEW `1.7.0+` Projects require the root bootstrap; initialized Projects adopt it only through governed `[Project Upgrade]`.
- `PROJECT-CONFIG.md` remains optional Bootstrap Location reference only.
- Bootstrap discovery remains distinct from bindings, current branch/worktree, Integration Target, Implementation Source, Runtime authority, and `AUTH-*`.
- No secrets or volatile branch/worktree/runtime state in the root bootstrap.
- Historical amendments remain unchanged.
- ChatGPT/Claude shared marker bodies remain byte-identical and each complete launcher remains `<=4,500` Unicode characters.
- No runtime, watcher, daemon, MCP routing, automatic upgrade, CI/CD, or deployment implementation.
- `commit ≠ push`.

---

### Task 1: Release identity and normative amendment

**Files:**
- Modify: `managing-project-source/FRAMEWORK-RELEASE.yaml`
- Create: `managing-project-source/references/framework-governance-amendment-260829-task023.md`
- Modify: `managing-project-source/MIGRATION-NOTES.md`

**Interfaces:**
- Consumes: approved TASK-023 design.
- Produces: Framework `1.7.0` release identity, latest-amendment pointer, root-bootstrap entrypoint metadata, and Brownfield upgrade checklist.

- [ ] **Step 1: Run a pre-change structural probe**

Run:
```powershell
python -c "from pathlib import Path; y=Path('managing-project-source/FRAMEWORK-RELEASE.yaml').read_text(); assert 'framework_version: \"1.6.0\"' in y; assert 'project_bootstrap:' not in y; print('RED baseline confirmed')"
```
Expected: PASS with `RED baseline confirmed`.

- [ ] **Step 2: Add Framework 1.7.0 metadata and amendment**

Descriptor changes:
- `framework_version: "1.7.0"`;
- `entrypoints.project_bootstrap: "templates/PROJECT-BOOTSTRAP.md"`;
- latest amendment → `references/framework-governance-amendment-260829-task023.md`;
- bootstrap policy records stable deployed filename, GREENFIELD requirement, Brownfield upgrade-only adoption, and optional vendor adapters.

Amendment must define the exact route, authority boundary, GREENFIELD/Brownfield behavior, `PROJECT-CONFIG.md` relationship, vendor adapters, failure handling, and non-goals from the spec.

Migration notes add `1.6.0 → 1.7.0` as current and preserve older sections.

- [ ] **Step 3: Verify release identity/amendment alignment**

Run a Python structural assertion that descriptor reports `1.7.0`, Schema `1.0.0`, release format `3`, `project_bootstrap` points to the maintained template, latest amendment is TASK-023, and migration notes contain `1.6.0 → 1.7.0`.

- [ ] **Step 4: Commit**

```text
git add managing-project-source/FRAMEWORK-RELEASE.yaml managing-project-source/references/framework-governance-amendment-260829-task023.md managing-project-source/MIGRATION-NOTES.md
git commit -m "docs: define Framework 1.7 self-bootstrap release"
```

### Task 2: Canonical bootstrap semantics and maintained template

**Files:**
- Create: `managing-project-source/templates/PROJECT-BOOTSTRAP.md`
- Modify: `managing-project-source/references/core-governance-rules.md`
- Modify: `managing-project-source/SKILL.md`
- Modify: `managing-project-source/templates/project-location-bootstrap.md`

**Interfaces:**
- Consumes: Task 1 release/amendment.
- Produces: normative discovery algorithm and reusable deployed root-bootstrap template.

- [ ] **Step 1: Add a failing/negative structural expectation before changes**

Confirm the root-bootstrap template does not yet exist and Core Governance lacks the `PROJECT-BOOTSTRAP.md → 00 → 01 → 03` contract.

- [ ] **Step 2: Create `templates/PROJECT-BOOTSTRAP.md`**

Required contents:
- non-authoritative locator declaration;
- stable deployed filename;
- default `Project-Source/` relative root;
- exact `00 → 01 → 03` route and `09` continuation rule;
- active `FRAMEWORK-001` precedence;
- fail-closed contradiction rules;
- no secrets/volatile Git/runtime authority;
- optional vendor adapters and optional `PROJECT-CONFIG.md` separation.

- [ ] **Step 3: Update Core Governance and SKILL**

Add Framework 1.7 bootstrap semantics and required-reference routing. Reclassify launchers as optional thin adapters once root access exists. Keep legacy/pre-1.7 discovery compatibility.

- [ ] **Step 4: Update Bootstrap Location template**

Retain Project Settings/Bootstrap Location semantics but explicitly distinguish them from the canonical root bootstrap. Reclassify `PROJECT-CONFIG.md` as optional location-reference only.

- [ ] **Step 5: Verify exact authority/routing tokens**

Assert current normative sources contain `PROJECT-BOOTSTRAP.md`, `FRAMEWORK-001`, `Project-Source/`, `00`, `01`, `03`, `09`, `[Project Upgrade]`, and explicit non-authority/fail-closed wording.

- [ ] **Step 6: Commit**

```text
git add managing-project-source/templates/PROJECT-BOOTSTRAP.md managing-project-source/references/core-governance-rules.md managing-project-source/SKILL.md managing-project-source/templates/project-location-bootstrap.md
git commit -m "docs: add canonical Project root bootstrap contract"
```

### Task 3: Starter and Project Source propagation

**Files:**
- Modify: `managing-project-source/templates/00-project-source-framework.md`
- Modify: `managing-project-source/templates/core-document-skeletons.md`
- Modify: `managing-project-source/templates/project-source-mockup/README.md`
- Modify: affected `00/01/03/09/14/16` mockup templates as needed
- Modify: all current mockup template release stamps that carry Framework version

**Interfaces:**
- Consumes: canonical semantics from Task 2.
- Produces: GREENFIELD starter guidance and Project Source routing aligned with 1.7.0.

- [ ] **Step 1: Add bootstrap-location/authority guidance to `00` and skeletons**

`00` must state that root bootstrap is a locator only and that active `FRAMEWORK-001` remains authority. `01` remains current routing, `03` current state, `09` continuation, and `14` may list the external root bootstrap without inventing a semantic slot/Stable ID.

- [ ] **Step 2: Update mockup README and affected starter templates**

Explain Project-root layout as:

```text
<Project-Root>/PROJECT-BOOTSTRAP.md
<Project-Root>/Project-Source/00-...
...
```

Keep `PROJECT-BOOTSTRAP.md` outside `Project-Source/`.

- [ ] **Step 3: Align current starter version stamps to Framework 1.7.0**

Change only current maintained starter/template release identity, not historical amendment/spec provenance.

- [ ] **Step 4: Verify starter alignment**

Assert all maintained mockup templates carrying a Framework version are `1.7.0`, the root bootstrap is outside semantic slots, and `18–19` remain RESERVED.

- [ ] **Step 5: Commit**

```text
git add managing-project-source/templates
git commit -m "docs: propagate Framework 1.7 bootstrap to starters"
```

### Task 4: README and vendor adapter compaction

**Files:**
- Modify: `README.md`
- Modify: `managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md`
- Modify: `managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md`

**Interfaces:**
- Consumes: Tasks 1–3 current semantics.
- Produces: human-facing release documentation and optional vendor discovery adapters.

- [ ] **Step 1: Update README release/use flow**

README must identify Framework `1.7.0`, explain root-native self-bootstrap, update NEW Project instructions to materialize/use `PROJECT-BOOTSTRAP.md`, and preserve Framework `1.6.0` as historical release documentation below the new section.

- [ ] **Step 2: Compact both launchers atomically**

Update release header to 1.7.0 and shared contract so, when root access exists, `PROJECT-BOOTSTRAP.md` is preferred. Preserve legacy discovery, command tokens, response-close fields, byte-identical shared marker bodies, and `<=4,500` characters.

- [ ] **Step 3: Verify launchers**

Run Python to extract shared marker bodies, assert equality, assert each complete launcher length `<=4500`, assert `PROJECT-BOOTSTRAP.md`, `[Project Status]`, `[Project Path]`, `[Project Upgrade]`, `[Session Envelope]`, `[Next Action]:`, `[Chat]:`, `[Reason]:`, and `[Required Read]:` are present.

- [ ] **Step 4: Commit**

```text
git add README.md managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md
git commit -m "docs: expose Framework 1.7 root bootstrap"
```

### Task 5: Pressure scenarios and affected verification

**Files:**
- Modify: `managing-project-source/tests/pressure-scenarios.md`

**Interfaces:**
- Consumes: complete current 1.7 semantics.
- Produces: regression coverage for discovery, authority, upgrade, and adapter failure modes.

- [ ] **Step 1: Add scenarios 172–180**

Cover exactly these cases:
1. root-access Agent without vendor settings finds `PROJECT-BOOTSTRAP.md`;
2. bootstrap attempts to override `FRAMEWORK-001`;
3. NEW 1.7 Project missing root bootstrap;
4. Brownfield Project silently auto-created bootstrap;
5. `PROJECT-CONFIG.md` contradicts root bootstrap;
6. Agent has no filesystem/repository access and must not claim discovery;
7. revision-suffixed bootstrap filename offered as replacement;
8. branch/worktree/runtime values embedded as bootstrap authority;
9. vendor adapter absent but root bootstrap present.

Each scenario includes Prompt / Temptation / Pass / Fail / GREEN expectation.

- [ ] **Step 2: Run affected structural verification**

Verify scenario numbers are unique and contiguous through 180; exact 1.7 bootstrap tokens exist on required current surfaces; launcher parity/size passes; historical TASK-022 amendment Git blob equals base `3af4bf1`; Markdown/YAML-only changed scope; and `git diff --check` passes.

- [ ] **Step 3: Commit**

```text
git add managing-project-source/tests/pressure-scenarios.md
git commit -m "docs: add self-bootstrap pressure scenarios"
```

### Task 6: Final candidate, RELEASE_FULL, evidence, and Task completion

**Files:**
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Create: `docs/superpowers/evidence/2026-08-29-task-023-self-bootstrap-release-full.md`

**Interfaces:**
- Consumes: unchanged completed 1.7 candidate.
- Produces: completion evidence and durable TASK-023 DONE state.

- [ ] **Step 1: Freeze candidate and confirm clean working tree**

Commit any final implementation corrections first. Record candidate commit and `managing-project-source` tree SHA. Do not edit candidate while RELEASE_FULL is being evaluated.

- [ ] **Step 2: Run one final RELEASE_FULL**

The full structural suite must cover release identity, latest amendment, root bootstrap template, routing/authority, GREENFIELD/Brownfield semantics, `PROJECT-CONFIG.md`, starter propagation/version stamps, launchers, scenario uniqueness, reserved slots, historical amendment preservation, documentation-only scope, and clean candidate state.

Expected result: every check PASS; record exact `N/N PASS` count.

- [ ] **Step 3: Write release evidence**

Evidence records release identity, candidate commit/tree, implemented scope, commit list, verification commands/findings, launcher sizes, scenario range, changed-file scope, non-goals, and publication state `NOT_PUSHED` unless separately published.

- [ ] **Step 4: Mark TASK-023 DONE**

Task Registry records Design Spec, Implementation Plan, executed state, implementation commits, evidence path, verification result, candidate commit/tree, completion criteria, clean tree, publication state, and exact next step.

- [ ] **Step 5: Commit completion metadata**

```text
git add docs/superpowers/PROJECT-TASKS.md docs/superpowers/evidence/2026-08-29-task-023-self-bootstrap-release-full.md
git commit -m "docs: record Framework 1.7 release evidence"
```

- [ ] **Step 6: Post-completion verification**

Confirm `git status --short --branch`, local completion commit, and remote publication state separately. Do not claim push unless `origin/main` is freshly observed at the completion commit.
