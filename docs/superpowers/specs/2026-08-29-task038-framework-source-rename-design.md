# TASK-038 Framework Source Naming & Distribution-Root Migration — Design

Date: `2026-08-29` (Asia/Bangkok)
Task: `TASK-038`
Design state: `USER_APPROVED_DESIGN / SPEC_APPROVED`
Approval basis: the user explicitly chose the paired names `Framework-Source/` and `Project-Source/`, approved separating ProjectFramework's own `Project-Source/`, and later authorized continuous development without repeated approval prompts on `2026-08-29`. This approval covers the bounded TASK-038 design/plan/local implementation workflow; push/publication remains separate unless explicitly authorized or covered by a later valid Goal.
Target release: Framework `1.8.0` / Schema `1.0.0` / release format `3`

## 1. Problem

The reusable Framework distribution currently lives at:

```text
managing-project-source/
```

ProjectFramework now also has its own authoritative Project governance source at:

```text
Project-Source/
```

The old distribution name is easy for Humans and Agents to confuse with the Project-specific authority tree. The repository needs an explicit paired naming boundary:

```text
Framework-Source/ = reusable Framework distribution / upstream source
Project-Source/   = authoritative governance/current truth for this Project
```

The migration must make this distinction unambiguous without globally rewriting historical provenance, inventing a second canonical distribution root, auto-upgrading external Projects, or allowing the repository rename to transfer Project authority.

## 2. Observed inventory before design

Fresh tracked-file inspection on `2026-08-29` found `96` tracked files associated with the old distribution path by file location or textual reference:

```text
CURRENT_DISTRIBUTION_TREE 55
CURRENT_PROJECT_SOURCE     7
CURRENT_ROOT_DOC           1
CURRENT_TASK_REGISTRY      1
HISTORICAL_SPEC           14
HISTORICAL_PLAN           16
HISTORICAL_EVIDENCE        2
```

Within the current distribution tree, only four files actually contain the literal string `managing-project-source/`:

```text
references/core-governance-rules.md                              current normative
references/framework-governance-amendment-260820-0735.md         historical
references/framework-governance-amendment-260820-0821.md         historical
references/framework-governance-amendment-260825-task020.md      historical
```

This inventory proves that TASK-038 is primarily a repository-root rename plus targeted current-reference reconciliation, not a justification for a repository-wide string replacement.

## 3. Alternatives considered

### A. Global search/replace

Rename the directory and replace every textual occurrence of `managing-project-source/` across the repository.

Rejected because it would rewrite historical specs, plans, evidence, and amendments that correctly describe the repository state at the time they were created. It would fabricate provenance and make old evidence harder to reconstruct.

### B. Permanent compatibility alias or duplicated tree

Keep `managing-project-source/` as a symlink, redirect directory, shim tree, or duplicate copy of `Framework-Source/`.

Rejected because it preserves two visible distribution roots, reintroduces the ambiguity TASK-038 is intended to remove, risks drift between copies, and has cross-platform/symlink behavior problems. A permanent alias would also weaken deterministic discovery by allowing two path names to appear current.

### C. Single canonical rename with scoped current-reference migration — chosen

Use one Git-tracked move:

```text
managing-project-source/ → Framework-Source/
```

Then update only current mutable surfaces that must describe the new repository state. Historical prose and evidence remain byte/provenance preserving. Brownfield/external consumers are not silently rewritten; migration guidance tells them how the upstream layout changed when they explicitly adopt Framework `1.8.0`.

This is the chosen architecture.

## 4. Canonical naming contract

After TASK-038 implementation, the repository has exactly one canonical reusable Framework distribution root:

```text
Framework-Source/
```

and ProjectFramework's own Project governance remains:

```text
Project-Source/
```

Canonical meanings:

```text
Framework-Source/ = reusable Framework distribution, templates, amendments, launchers, tests
Project-Source/   = this Project's active FRAMEWORK-001, current state, authority, evidence, handoff
```

Correct access to `Framework-Source/` grants no consuming-Project authority. Correct access to `Project-Source/` does not make that tree the reusable Framework distribution.

## 5. Physical repository migration

Implementation uses Git rename semantics for the whole distribution directory:

```text
git mv managing-project-source Framework-Source
```

The move preserves file contents unless a file is separately identified as a current mutable surface requiring semantic edits.

Required post-move top-level shape:

```text
ProjectFramework/
├── PROJECT-BOOTSTRAP.md
├── Project-Source/
├── Framework-Source/
├── docs/
├── README.md
└── LICENSE
```

`managing-project-source/` MUST NOT remain as a second canonical directory, duplicate tree, symlink, or compatibility alias.

## 6. Current versus historical classification

TASK-038 uses content role, not text matching alone, to decide whether a reference changes.

### 6.1 Current mutable surfaces — rewrite to `Framework-Source/`

At minimum:

```text
README.md
Framework-Source/references/core-governance-rules.md
Framework-Source current release/amendment/migration guidance created or changed by TASK-038
Framework-Source current templates/launchers/tests when they describe the distribution root explicitly
docs/superpowers/PROJECT-TASKS.md current lifecycle/result fields for TASK-038
ProjectFramework active Project Source current-routing/current-state/current-provenance surfaces
```

A current source may still mention `managing-project-source/` when describing the historical/source side of the migration. Such wording must be clearly historical/migration context, not a second current location.

### 6.2 Historical/provenance surfaces — preserve old textual path

Do not rewrite old path strings merely to make them look current in:

```text
docs/superpowers/specs/ for completed historical work
docs/superpowers/plans/ for completed historical work
docs/superpowers/evidence/ historical release evidence
historical Framework amendments whose payload described the old distribution root
archived/superseded Project Source revisions
historical EVD/CHG payload that records the old location at capture time
```

Historical Framework amendments moved physically under `Framework-Source/references/` retain their blob contents. Their internal `managing-project-source/...` strings remain accurate historical statements.

TASK-039 design/plan may also mention `managing-project-source/` as the prerequisite source path being replaced; those references are intentional dependency history and are not current distribution routing.

## 7. Framework release identity

TASK-038 establishes the Framework `1.8.0` distribution line while keeping:

```text
Framework: 1.8.0
Schema:    1.0.0
Format:    3
```

Create a TASK-038 amendment under the renamed distribution, for example:

```text
Framework-Source/references/framework-governance-amendment-260829-task038.md
```

The release descriptor remains physically inside the distribution:

```text
Framework-Source/FRAMEWORK-RELEASE.yaml
```

Its internal relative entrypoint paths remain relative to the distribution root unless TASK-038 design explicitly requires another semantic change. The descriptor's canonical repository remains `captainhuke-dev/ProjectFramework`; the root rename does not create branch authority.

## 8. Root README and bootstrap guidance

Root `README.md` must describe:

```text
Distributable package root: Framework-Source/
Release descriptor: Framework-Source/FRAMEWORK-RELEASE.yaml
Framework bootstrap reads from Framework-Source/...
Project-specific governance lives in Project-Source/
```

The README repository tree example and ChatGPT/Claude launcher-copy instructions use `Framework-Source/`.

`PROJECT-BOOTSTRAP.md` remains the Project-root entrypoint into this Project's `Project-Source/`. It MUST NOT be repointed to `Framework-Source/`.

The Framework distribution's maintained `templates/PROJECT-BOOTSTRAP.md` moves with the distribution to:

```text
Framework-Source/templates/PROJECT-BOOTSTRAP.md
```

but its deployed role stays unchanged: it locates a consuming Project's `Project-Source/`, never the Framework distribution.

## 9. ProjectFramework's own active Project Source reconciliation

Because ProjectFramework itself is now an initialized governed Project, current Project Source references to the reusable distribution must not remain stale after the rename.

Observed current Project Source files containing the old path before migration are:

```text
00 Project Source Framework
01 Project Source Index
02 Project Overview
03 Current State
13 Evidence Registry
14 Project Source Manifest
16 Migration Registry
```

Reconciliation rules:

1. **Do not rewrite historical evidence.** Existing EVD/CHG statements that correctly record `managing-project-source/` at their capture time remain unchanged in historical revisions/current registry history.
2. **Materialize current truth.** Current routing/overview/state/provenance fields that answer "where is the Framework distribution now?" resolve to `Framework-Source/` after migration.
3. **Use normal Project Source revision flow.** Affected active documents receive new monotonic revisions where required; old revisions are preserved/archived rather than destructively overwritten.
4. **Root Governance mutation discipline.** Because active `00 / FRAMEWORK-001` contains a ProjectFramework-specific distribution-root statement, changing that current root document uses the normal user-approved revision → validate → promote → supersede/archive flow. The Project's Framework pin does not auto-upgrade merely because the upstream distribution becomes `1.8.0`.
5. **Bootstrap route follows active 00.** If `00` receives a new active filename/revision, root `PROJECT-BOOTSTRAP.md`, `01`, `14`, and continuation pointers are reconciled to the new active root.
6. **Record migration.** `16 Migration Registry` materializes a `MIG-*` record for the ProjectFramework repository path migration when material; `10`/`13` may record change/evidence pointers without rewriting old captured evidence.

This keeps two facts separate:

```text
Framework distribution current release may become 1.8.0
≠
ProjectFramework's own initialized Project Source automatically upgrades its FRAMEWORK-001 pin
```

A later explicit `[Project Upgrade]` may upgrade ProjectFramework's own Project Source pin; TASK-038 does not do so by implication.

## 10. External and Brownfield compatibility

Existing initialized consuming Projects remain locally pinned and are not rewritten. Their local `Project-Source/`, launcher copies, vendor settings, or local Framework package remain unchanged until their own governed upgrade/migration.

Framework `1.8.0` migration notes must state that the canonical upstream distribution path changed:

```text
managing-project-source/ → Framework-Source/
```

For a consuming Project that explicitly upgrades to `1.8.0`, migration assessment updates only current references that depend on the canonical upstream distribution path. It preserves Project-specific rules, bindings, Stable IDs, current truth, history, and deployed `PROJECT-BOOTSTRAP.md` semantics.

Direct external scripts, bookmarks, deep links, or automations that hard-code `managing-project-source/...` against upstream `main` may require manual/governed update. TASK-038 does not pretend those references remain valid and does not silently rewrite external systems.

## 11. No compatibility alias

The Framework deliberately does not retain a live compatibility alias at `managing-project-source/`.

Reasons:

- one canonical distribution root is simpler and deterministic;
- a duplicate/alias would continue the naming ambiguity;
- symlink behavior varies by platform/tool;
- a shim cannot preserve arbitrary old deep paths without effectively duplicating the tree;
- initialized Projects already preserve backward compatibility through local pinning rather than upstream-path aliasing.

Migration notes and governed upgrade are the compatibility mechanism.

## 12. Current-source reference rewrite policy

After the move, a search for `managing-project-source/` is not expected to return zero results. Instead, every remaining result must belong to an allowed historical/migration-context class.

Allowed examples:

```text
historical specs/plans/evidence
historical Framework amendments
archived Project Source revisions
TASK-038/TASK-039 migration design/plan explaining the old path
MIGRATION-NOTES describing source → target
current Task records describing TASK-038 problem/history
```

Forbidden remaining examples:

```text
current README routing to old path
current Core Governance bootstrap paths using old root
current launcher instructions telling users to copy from old root
current active Project Source saying old root is current
current release descriptor discovery instructions resolving old root
current verification scripts expecting old root as canonical
```

Verification therefore uses an explicit allowlist/classification rather than a naive zero-match assertion.

## 13. TASK-039 sequencing

TASK-038 is the first Framework `1.8.0` distribution-path implementation. TASK-039 implementation is blocked until TASK-038 is `DONE` and `Framework-Source/` is canonical.

Pressure scenario numbering is reserved as:

```text
TASK-038: scenarios 181–188
TASK-039: scenarios 189–211
```

This prevents duplicate scenario identities and gives TASK-039 a stable post-migration path basis.

## 14. TASK-038 pressure scenarios

Add exactly eight scenarios:

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

Scenario semantics must verify both the rename and the authority/provenance boundary; tests must not force historical text to be rewritten.

## 15. Verification strategy

Affected verification must prove at minimum:

1. top-level `Framework-Source/` exists and `managing-project-source/` does not exist as a live directory/alias;
2. all expected distribution files moved under `Framework-Source/`;
3. Framework release identity is `1.8.0 / 1.0.0 / 3`;
4. current release descriptor and current Framework surfaces resolve from `Framework-Source/`;
5. root README uses the new canonical path and clearly separates `Framework-Source/` from `Project-Source/`;
6. `PROJECT-BOOTSTRAP.md` still routes to active `Project-Source/00 → 01 → 03`, not to Framework distribution;
7. current Core Governance old-root routing references are rewritten;
8. historical amendments that contained old-path strings retain identical content blobs after the directory move;
9. completed historical specs/plans/evidence outside the distribution are unchanged;
10. remaining `managing-project-source/` strings pass the explicit historical/migration-context allowlist;
11. current active ProjectFramework Project Source has no stale claim that the old distribution root is current;
12. old Project Source revisions/evidence remain reconstructable;
13. a governed `MIG-*`/evidence/change trail exists for the current Project when required by the final migration implementation;
14. external/Brownfield behavior states no auto-rewrite and no alias fallback;
15. scenarios `1–188` are unique/contiguous and scenarios 181–188 pass;
16. launcher marker bodies remain byte-identical and each launcher stays within `<=4,500` Unicode characters;
17. current maintained starter Framework stamps are `1.8.0` while Schema remains `1.0.0`;
18. `18–19` remain RESERVED and existing slot/Stable-ID families are unchanged;
19. `git diff --check` passes;
20. one final `RELEASE_FULL` runs on the unchanged TASK-038 Framework `1.8.0` candidate before TASK-038 is marked `DONE`.

Historical blob preservation should be checked with observed Git blob SHAs for the three identified historical amendments that contain the old path, plus selected completed design/evidence files used as migration sentinels.

## 16. Rollback and reversibility

Before remote publication, TASK-038 is reversible through Git history. If affected verification fails materially:

```text
stop publication
retain evidence of the failing candidate
repair forward when semantics are clear
or revert the TASK-038 migration commits through normal Git governance
```

Do not create a temporary compatibility alias as rollback. A rollback returns the repository to the old canonical root through Git state, not to a dual-root state.

If publication has already occurred, any retraction/reversal follows current shared-state/release authority and does not silently rewrite external consumers.

## 17. Non-goals

TASK-038 does not:

- rename `Project-Source/`;
- make `Framework-Source/` Project authority;
- auto-upgrade ProjectFramework's own active `FRAMEWORK-001` pin;
- auto-upgrade external consuming Projects;
- rewrite completed historical specs/plans/evidence for cosmetic consistency;
- keep a duplicate/symlink/shim distribution root;
- add runtime path redirectors, CI/CD, filesystem watchers, or migration daemons;
- implement TASK-039 `[Goal]` or other Framework `1.8.0` feature Tasks.

## 18. Acceptance criteria

TASK-038 is acceptable when the repository has one canonical reusable distribution root named `Framework-Source/`; `Project-Source/` remains clearly distinct and authoritative only for ProjectFramework itself; current Framework/current Project references point to the new distribution path; historical references remain truthful and reconstructable; external/Brownfield consumers are never silently rewritten; no live old-root alias exists; `PROJECT-BOOTSTRAP.md` continues to route into Project Source; scenarios 181–188 and release verification pass; and the migration can be understood without guessing which source tree owns Framework distribution versus Project authority.
