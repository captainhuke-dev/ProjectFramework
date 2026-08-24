# Project Upgrade Command Design

Status: USER_APPROVED_DESIGN / IMPLEMENTATION_NOT_AUTHORIZED

Date: 2026-08-24

Task: `TASK-018`

## Goal

Add a registered `[Project Upgrade]` Project command that fresh-resolves the current Project Framework identity and the canonical upstream Framework identity, compares them, reports whether an upgrade is needed, and offers the user a governed path to prepare an upgrade when they differ.

The command is an inspection and upgrade-entry interface. It is not an automatic updater and does not itself authorize Project mutation.

## Scope Boundary

This design remains within ProjectFramework governance/documentation scope. It defines command semantics, comparison inputs, report vocabulary, approval boundaries, preservation behavior, affected Framework surfaces, and verification expectations.

It does **not** introduce a command parser service, CLI, bot, watcher, scheduler, migration engine, background updater, CI/CD workflow, branch switcher, workspace auto-selector, or any other executable enforcement runtime.

Existing initialized Projects remain governed by their locally pinned active `FRAMEWORK-001` until a separately approved migration is completed and promoted.

## Design Decision

Use a **Read-only Upgrade Comparator + Governed Upgrade Handoff** architecture.

The command performs fresh comparison first. If the current Project and canonical upstream differ, it asks whether the user wants to prepare an upgrade. A positive answer authorizes upgrade assessment/preparation only. It does not authorize immediate mutation.

The existing Direct-to-Latest workflow remains the mutation boundary:

```text
fresh compare
→ report result
→ user chooses whether to prepare an upgrade
→ current→target cumulative assessment
→ FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED
→ Preview delta + preservation + rollback
→ explicit mutation approval
→ apply required changes
→ affected/risk-scoped verification
→ RELEASE_FULL once on final unchanged target candidate
→ governed promotion/history preservation
```

This preserves the Framework 1.3 invariant that initialized Projects do not auto-upgrade merely because upstream advances.

## Registered Command Contract

Add the canonical registered command:

```text
[Project Upgrade] : compare the active Project Framework with the canonical upstream Framework and offer a governed upgrade when they differ
```

Existing registered-command rules remain unchanged:

- literal `[` and `]` delimiters are required for registered-command invocation;
- matching inside the brackets is case-insensitive;
- canonical display form is `[Project Upgrade]`;
- missing brackets do not invoke the registered command token;
- natural-language command discovery lists only commands registered by the active Framework/Project;
- adding the command creates no parser/runtime implementation authority.

## Current Framework Resolution

### Initialized Project

For an initialized Project, the command resolves current Framework identity from the active local Project Source.

Resolution order:

```text
resolve valid active local FRAMEWORK-001
→ read locally pinned Project Framework identity
→ treat that local pin as current Project authority
```

At minimum, observe when available:

- `project_source_framework_version`;
- `project_source_schema_version`;
- active Framework document identity/revision;
- local Project Source location/binding evidence relevant to resolving the active root.

The command must not substitute any of the following for the active local pin:

- canonical upstream version;
- chat memory;
- cached prior command output;
- recent/active workspace ranking;
- a similarly named repository;
- cached remote-tracking refs.

If no valid active local Framework can be resolved, report current identity as `VERIFICATION_REQUIRED` and do not proceed to an upgrade offer based on guessed state.

### Canonical ProjectFramework Distribution Repository

When the command is run against the canonical `ProjectFramework` distribution repository itself rather than a downstream initialized Project, current distribution identity may be read from the repository's `managing-project-source/FRAMEWORK-RELEASE.yaml` together with observed Git state.

This repository-self case must remain distinct from downstream local-pin authority semantics.

## Canonical Upstream Resolution

The comparison target is the canonical upstream Framework distribution resolved through the applicable Framework Source/bootstrap governance.

For the current canonical distribution, the declared repository identity is:

```text
captainhuke-dev/ProjectFramework
main
```

The target Framework identity is read from the upstream `managing-project-source/FRAMEWORK-RELEASE.yaml` or equivalent canonical release descriptor after fresh remote/source observation appropriate to the claim.

A cached local `origin/main` reference alone is not sufficient to claim that the observed target is the current canonical upstream state.

If the upstream source, release descriptor, or required identity cannot be resolved or freshly observed, report:

```text
Target Framework: VERIFICATION_REQUIRED
Upgrade Comparison: VERIFICATION_REQUIRED
```

and do not offer an upgrade as if a newer target had been verified.

## Comparison Inputs

The command compares more than a single version string.

Minimum comparison inputs when available:

```text
Current Framework Version
Current Schema Version
Target Framework Version
Target Schema Version
Current Framework/source identity
Target Framework/source identity
Freshness/evidence context
```

Where repository/source identity is observable, a same-version result does not automatically prove equivalence if the observed distribution/source identities conflict materially.

## Report Vocabulary

The command may use the following presentation-only comparison labels:

```text
UP_TO_DATE
UPGRADE_AVAILABLE
SOURCE_DIVERGENCE
VERIFICATION_REQUIRED
```

These labels are command-report vocabulary only. They do not create new Project lifecycle, Epistemic Status, Git freshness, authority, migration, or health state families.

### `UP_TO_DATE`

Use when the current Project Framework identity is adequately verified against the current canonical upstream target and no required target Framework difference is identified.

### `UPGRADE_AVAILABLE`

Use when a verified canonical target requires a newer/different Framework state than the current Project pin.

This label permits the command to ask whether the user wants to prepare an upgrade. It does not authorize mutation.

### `SOURCE_DIVERGENCE`

Use when nominal version identity appears equal or comparable but observed source/distribution identity contains a material conflict or unexplained divergence that prevents a safe `UP_TO_DATE` claim.

The command must surface the divergence and require resolution/assessment rather than silently treating equal version strings as proof of equivalence.

### `VERIFICATION_REQUIRED`

Use when current or target identity/freshness evidence is insufficient to make a supported comparison.

The response identifies what could not be verified and does not infer a convenient fallback.

## User-facing Behavior

### No Difference

Representative behavior:

```text
[Project Upgrade]

Current Framework: 1.3.0
Canonical Upstream: 1.3.0
Status: UP_TO_DATE

No Framework upgrade is required.
```

Exact prose may vary, but the semantic result and evidence boundary must remain clear.

### Upgrade Available

Representative behavior:

```text
[Project Upgrade]

Current Framework: 1.3.0
Canonical Upstream: 1.4.0
Status: UPGRADE_AVAILABLE

A different/newer canonical Framework is available.
Do you want to prepare an upgrade to Framework 1.4.0?
```

The offer is explicitly to **prepare an upgrade**, not to mutate immediately.

### User Says Yes

A positive answer means:

```text
prepare current→target cumulative upgrade assessment
```

It does not mean:

```text
rewrite active Project Source immediately
```

The next governed flow is:

1. materialize current reconstructable Project truth;
2. resolve the selected target Framework;
3. compare current state directly with target required semantics;
4. classify the cumulative delta as `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`;
5. prepare a Preview covering required changes, preservation, rollback/reversibility, affected scope, and verification;
6. obtain explicit mutation approval;
7. only then apply the approved migration.

## Approval Boundary

The design intentionally keeps two separate user decisions:

1. **Upgrade-intent decision** — user agrees to prepare/assess an upgrade after seeing that a difference exists.
2. **Mutation approval** — user approves the concrete cumulative migration Preview after affected scope, preservation, rollback, and verification expectations are known.

The first decision must never be silently promoted into the second.

This preserves existing authority/risk/migration governance and prevents `[Project Upgrade]` from becoming an implicit auto-upgrade mechanism.

## Direct-to-Latest Preservation Contract

If an upgrade is later approved, the command hands off to the existing Direct-to-Latest cumulative migration architecture.

The migration must preserve, as applicable:

- active local Framework pin authority until promotion;
- Stable IDs;
- Project-specific rules;
- current Project truth;
- Requirements and Decisions;
- Project Location and other governed bindings;
- authority/delegation state;
- migration/history/provenance records;
- approval and rollback/reversibility controls;
- validation and evidence;
- existing Task/Action truth;
- historical amendments and migration rationale.

Intermediate historical Framework migrations are not mechanically replayed unless a separately justified migration requires them. Upgrade cost should scale with the current-to-target semantic delta, not the number of skipped releases.

The latest starter remains a NEW-Project target representation and is not a default destructive replacement mechanism for initialized Projects.

`commit ≠ push` remains unchanged.

## Failure and Unknown Handling

The command fails closed for unsupported comparison/upgrade claims when any material prerequisite is unresolved, including:

- active local Framework cannot be resolved;
- applicable Framework Source/upstream identity is unresolved;
- remote/source freshness cannot be established for a claimed current upstream state;
- upstream release descriptor is unreadable or inconsistent;
- bootstrap/root location mismatch affects authority resolution;
- same-version source identity has an unresolved material conflict;
- current Project truth is not reconstructable enough for a safe upgrade assessment;
- target Framework semantics cannot be bounded safely.

Comparison failure uses `VERIFICATION_REQUIRED` or `SOURCE_DIVERGENCE` as appropriate. Upgrade assessment may later classify unsafe cumulative migration as `MAJOR_MIGRATION_REQUIRED` under existing Framework 1.3 rules.

The command never substitutes remembered, recent, mounted, cached, or similarly named locations/sources as authority.

## Interaction with Existing Commands

`[Project Upgrade]` composes with but does not replace existing commands.

### `[Project Status]`

`[Project Status]` continues to report current Project/Task/Git/verification/blocker state. It does not become an upgrade detector by implication.

`[Project Upgrade]` may reuse fresh identity/Git/source observations when they remain valid for the same command execution, but must not treat an old status response as current evidence.

### `[Project Path]`

`[Project Path]` continues to expose/verify configured bootstrap paths and route explicit persistent path-change requests through existing governance.

`[Project Upgrade]` uses applicable Framework Source/Workspace/Project Location information only for resolution. It creates no path mutation authority and must not rewrite a binding because an upstream comparison requires a different location.

## Distribution Surfaces Expected to Change During Implementation

Implementation is expected to assess and update the current normative/distribution surfaces needed to register and describe the command, including as applicable:

- `README.md`;
- `managing-project-source/FRAMEWORK-RELEASE.yaml` if a release identity/descriptor change is part of the resulting Framework release;
- a new latest Framework amendment if required by the release/change governance;
- `managing-project-source/references/core-governance-rules.md`;
- `managing-project-source/SKILL.md`;
- `managing-project-source/templates/00-project-source-framework.md`;
- relevant maintained starter/mockup documentation;
- compact ChatGPT/Claude launchers when command-registry coverage requires it;
- `managing-project-source/tests/pressure-scenarios.md`.

Historical amendments remain provenance and are not rewritten.

If launchers are changed, their shared marker bodies must remain byte-identical and each launcher must stay within the existing size constraint.

This design does not preselect the Framework release number for the eventual implementation. Release identity is a separate governed implementation/release decision and must remain internally consistent across the distribution when chosen.

## Verification Strategy

Implementation should use progressive/risk-scoped verification.

### Task-local / affected checks

At minimum, verify:

- registered command canonical display and case-insensitive bracket matching;
- command discovery includes `[Project Upgrade]` only after registration;
- current Project identity comes from active local Framework authority for initialized Projects;
- upstream/current-target claims require fresh applicable evidence;
- comparison labels are used only as report vocabulary;
- same-version source divergence does not collapse to `UP_TO_DATE` automatically;
- unavailable evidence produces `VERIFICATION_REQUIRED`;
- `UPGRADE_AVAILABLE` asks before entering upgrade preparation;
- upgrade-intent approval does not authorize immediate mutation;
- cumulative migration Preview + explicit mutation approval remain required;
- Direct-to-Latest preservation rules remain intact;
- no executable updater/parser/runtime artifacts are introduced unintentionally.

### Release verification

When the implementation candidate is complete and unchanged, run one applicable `RELEASE_FULL` for the final candidate, consistent with Framework 1.2.5/1.3 evidence-reuse semantics.

Before integration, run `INTEGRATION_GATE` with current Base Freshness and evidence-validity review.

## Pressure Scenarios

Implementation must add pressure coverage for at least the following behaviors.

### 1. Brackets Required

Unbracketed `Project Upgrade` must not be treated as the registered command token solely because the words match.

### 2. Case-insensitive Registered Matching

`[project upgrade]`, `[PROJECT UPGRADE]`, and `[Project Upgrade]` invoke the same registered command while canonical display remains `[Project Upgrade]`.

### 3. No Remembered Upstream Truth

An earlier chat statement that a newer Framework exists is not sufficient. The command fresh-observes applicable upstream state before claiming `UPGRADE_AVAILABLE`.

### 4. Cached Remote Ref Is Not Fresh Upstream Evidence

A cached `origin/main` alone must not support a verified latest/current upstream claim.

### 5. Local Pin Wins for Current Initialized Project

If active local `FRAMEWORK-001` says the Project is pinned to an older Framework while upstream is newer, current identity remains the local pin. Upstream does not silently replace it.

### 6. Same Version with Source Divergence

Equal Framework version strings with materially conflicting observed distribution/source identity must report `SOURCE_DIVERGENCE` or require verification, not `UP_TO_DATE` automatically.

### 7. Unavailable Upstream

If the canonical upstream cannot be freshly resolved, report `VERIFICATION_REQUIRED` and do not invent an upgrade recommendation.

### 8. Upgrade Available Requires User Choice

A verified newer/different target produces an upgrade offer; it does not start mutation automatically.

### 9. Yes Means Prepare, Not Mutate

If the user says yes to the upgrade offer, the system prepares cumulative assessment/Preview first and still requires explicit mutation approval afterward.

### 10. No Auto-upgrade

A detected difference must never rewrite the active Project merely because the command was invoked.

### 11. Direct-to-Latest

A Project several Framework releases behind is assessed directly against the selected target. Intermediate release execution is not mandatory.

### 12. Preservation

Upgrade preparation must preserve Stable IDs, Project-specific rules, bindings, current truth, and history rather than defaulting to rebuild-from-starter.

### 13. Major Migration Boundary

Breaking schema/root semantics, non-reconstructable current truth, or unresolved material conflicts must be able to classify as `MAJOR_MIGRATION_REQUIRED` rather than forcing a nominal fast upgrade.

### 14. Command Discovery

After registration, natural-language command discovery includes `[Project Upgrade]` and does not invent additional unsupported commands.

### 15. Path/Binding Authority Is Not Expanded

`[Project Upgrade]` may read applicable source/location information but cannot silently persist a new Framework Source, Workspace, Repository, or Project Location Binding.

## Acceptance Criteria

The design is implemented successfully only when all of the following are true:

1. `[Project Upgrade]` is registered consistently across applicable current Framework surfaces.
2. Literal brackets remain required and registered-name matching remains case-insensitive.
3. Initialized Project current identity resolves from the active local pin rather than upstream or memory.
4. Canonical upstream comparison uses fresh applicable evidence before claiming current/latest target state.
5. Comparison distinguishes `UP_TO_DATE`, `UPGRADE_AVAILABLE`, `SOURCE_DIVERGENCE`, and `VERIFICATION_REQUIRED` without creating new lifecycle/state families.
6. A detected difference asks whether the user wants to prepare an upgrade; it never auto-upgrades.
7. A positive upgrade-intent response leads to cumulative assessment and Preview, not immediate mutation.
8. Explicit mutation approval remains required after the concrete current→target Preview is known.
9. Direct-to-Latest path classes and preservation/history rules remain unchanged.
10. Same-version material source divergence cannot be silently reported as fully equivalent.
11. Failure/unknown cases fail closed without inferred fallback authority or paths.
12. Applicable pressure scenarios pass.
13. No unintended executable updater/parser/validator/CI/scheduler/watcher/runtime artifacts are introduced.
14. Final unchanged implementation candidate receives the required applicable `RELEASE_FULL` verification and integration freshness/evidence checks.

## Out of Scope

The following are explicitly outside this design:

- automatic periodic checking for Framework updates;
- notifications/reminders about new Framework versions;
- automatic mutation after detecting an update;
- automatic branch creation/merge/push;
- a standalone updater executable or service;
- semantic version ordering rules beyond what the canonical release identity and migration assessment safely support;
- changing Project Location Binding or Bootstrap Location as a side effect of comparison;
- redesigning the existing Direct-to-Latest migration architecture;
- implementing `TASK-019` language simplification as part of this Task.

## Implementation Authorization State

The user has approved this design direction and authorized creation of this design/spec artifact.

Implementation of `[Project Upgrade]` is **not authorized by this design approval alone**. The next workflow stage is written-spec review, followed by a separate implementation plan and implementation approval/workflow according to the active development process.
