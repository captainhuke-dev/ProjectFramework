# TASK-023 Self-Bootstrapping Project Contract (Framework 1.7.0) — RELEASE_FULL Evidence

Captured: `2026-08-29` (Asia/Bangkok)

Task: `TASK-023`
Execution branch: `main` (inline fallback after linked-worktree mutation routing was blocked by the host Active Workspace guard)
Pre-TASK-023 base: `3af4bf17bbca22c29e0f1d0a6ccd0c78903d2931`

## Release identity

- Framework: **1.7.0** (previous 1.6.0)
- Schema: **1.0.0** (unchanged)
- Release format: **3** (unchanged)
- Latest amendment: `references/framework-governance-amendment-260829-task023.md`
- Candidate commit: `e2caa5e68f037104cf7ca41756690daf03ede576`
- Candidate `managing-project-source` tree SHA: `100338b4186e5ccbe0502b92a85e38555e40db3c`

## Implemented scope

1. **Stable root discovery entrypoint** — Framework 1.7.0 standardizes `<Project-Root>/PROJECT-BOOTSTRAP.md` as a vendor-neutral discovery/locator artifact outside the `00–99` semantic namespace.
2. **Authority boundary preserved** — the root bootstrap never replaces or overrides active `00 / FRAMEWORK-001`; it owns no Stable ID and stores no requirements, decisions, risks, bindings, current status, handoff state, or secret values.
3. **Canonical read route** — once Project-root access exists, discovery routes `PROJECT-BOOTSTRAP.md → 00 / FRAMEWORK-001 → 01 / Project Source Index → 03 / Current State → task-specific routing`, with `09 / Handoff` when continuation applies.
4. **GREENFIELD contract** — NEW Projects created under Framework 1.7.0+ include the stable root bootstrap as part of the approved creation result.
5. **Brownfield contract** — initialized Projects remain pinned and receive the root bootstrap only through governed `[Project Upgrade]` / approved migration or repair; absence on a pre-1.7 Project is not itself invalidity.
6. **Vendor-adapter reclassification** — ChatGPT/Claude Project Settings, `AGENTS.md`, `CLAUDE.md`, and similar surfaces are optional thin discovery adapters once Project-root access exists; they are never Project authority.
7. **Bootstrap-location separation** — `PROJECT-CONFIG.md` remains an optional/legacy Bootstrap Location reference; it is not promoted to the canonical root discovery entrypoint and material contradictions fail closed.
8. **Volatile-state separation** — concrete current branch/worktree, runtime endpoint, workspace handle, or mutable status is not persisted as bootstrap authority; volatile state remains fresh-observed from canonical sources when material.
9. **Starter propagation** — root template, core skeletons, mockup routing/manifest/handoff/migration guidance, and all 22 concrete starter templates are aligned to Framework 1.7.0 / Schema 1.0.0.
10. **Pressure coverage** — scenarios `172–180` cover root-native discovery, active-root authority, GREENFIELD/Brownfield behavior, `PROJECT-CONFIG.md` contradiction, no-filesystem-access boundary, stable filename, volatile state, and vendor independence.

## Commits

Preparation / design:

- `cd2a506` — approve TASK-023 self-bootstrap design
- `24ccda8` — add TASK-023 implementation plan

Implementation candidate:

- `ee4b088` — define Framework 1.7 self-bootstrap release
- `094e9a4` — add canonical Project root bootstrap contract
- `e67ac2f` — propagate Framework 1.7 bootstrap to starters
- `c1496b0` — expose Framework 1.7 root bootstrap
- `e2caa5e` — add Framework 1.7 self-bootstrap pressure scenarios

## Verification history

### Affected verification

Before candidate freeze, affected structural verification passed:

**`AFFECTED PASS 65/65`**

`git diff --check` initially reported one formatting-only finding: an extra blank line at EOF in `managing-project-source/tests/pressure-scenarios.md`. The newline was corrected without changing scenario semantics, then affected verification was rerun and `git diff --check` passed.

### RELEASE_FULL verification-method correction

The first full checker execution was interrupted by the Windows console default `cp874` while printing a Unicode arrow. The checker was rerun with UTF-8-safe output handling.

The next full run reported `135/146` because eleven assertions compared exact wording rather than the approved semantic contract (for example expecting one-line `00 → 01 → 03` text where the amendment intentionally expresses the route as a multiline chain, and expecting `09 Handoff` where the maintained form is `09 / Handoff`). The candidate sources were inspected directly; all eleven semantics were present. Only the **verification predicates** in the ignored scratch checker were aligned to the approved design wording. No candidate file changed.

### Final unchanged-candidate RELEASE_FULL

Final result on candidate `e2caa5e68f037104cf7ca41756690daf03ede576`, distribution tree `100338b4186e5ccbe0502b92a85e38555e40db3c`:

**`RELEASE_FULL PASS 146/146`**

Observed supporting results:

- ChatGPT launcher: **4,285** Unicode characters
- Claude launcher: **4,284** Unicode characters
- shared launcher marker bodies: byte-identical
- pressure scenarios: **1–180**, exactly once each
- maintained mockup files: **23** total (`22` concrete templates + README), all concrete templates aligned to Framework 1.7.0
- changed files from pre-TASK-023 base: **39**
- Framework change scope: Markdown/YAML only; no runtime/discovery daemon/tool-routing implementation
- `git diff --check`: clean
- candidate working tree before RELEASE_FULL: clean
- historical TASK-022 amendment Git blob unchanged: `c124182cc945c728af949938658ee8fb3e0a6c1e`

The 146 checks cover release identity, descriptor/amendment alignment, root-bootstrap content boundary, canonical discovery route, active-root authority, GREENFIELD/Brownfield behavior, vendor-adapter semantics, Bootstrap Location separation, no-secret/no-volatile-state rules, migration guidance, README/SKILL/Core Governance alignment, launcher parity/size/tokens, starter version/routing alignment, scenario uniqueness/coverage, reserved slots, Project Graph preservation, historical amendment immutability, documentation-only scope, and clean candidate state.

## Non-goals preserved

No filesystem watcher/daemon, automatic discovery service, MCP runtime/tool routing, model routing, vendor plugin runtime, automatic Brownfield upgrade, secret store, automatic path/binding repair, CI/CD, deployment automation, or TASK-024+ implementation was added.

## Publication state

`commit ≠ push` remains binding. At evidence creation, the candidate was committed locally and had not yet been published. Under the user's explicit continuous completion approval, verified Framework 1.7.0 implementation and completion through commit `94661bb71f223a7e4e86045c7737ccb0d792f91f` were subsequently pushed to `origin/main` on `2026-08-29`. A separate publication-state reconciliation commit records the observed remote state without modifying the verified `managing-project-source` candidate tree.
