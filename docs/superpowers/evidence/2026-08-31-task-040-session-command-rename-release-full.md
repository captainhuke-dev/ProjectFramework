# TASK-040 `[Session]` Command Rename — Release Verification Evidence

Captured: `2026-08-31` (Asia/Bangkok)
Task: `TASK-040`
Framework release: `1.8.0`
Project Source Schema: `1.0.0`
Release format: `3`
Publication state: `NOT_PUSHED`

## Scope

TASK-040 is a bounded documentation/governance command-name change requested explicitly by the user: the current registered command formerly displayed as `[Session Envelope]` is shortened to `[Session]`.

The change preserves the existing bounded session/task `ENV-*` model in `15 Action Registry`, `declare | show | close`, expiry/prohibited-zone semantics, Goal-derived narrowing, and all existing fail-closed gates. It adds no runtime parser, CLI, alias layer, automation, semantic slot, or Stable-ID family.

Historical amendments/specs/plans/evidence retain the older command spelling when that was true at capture time.

## Candidate Identity

```text
Candidate HEAD: 5b3d4e309976a88e1e57495b6fdaa049fabb6247
Candidate tree: 9fcdb6b3f0dc8c43f35865ee9155c0521c4e64fc
Framework-Source tree: 36804c105604fe8da492a9d71a1f0270e5e035ee
Base observed: origin/main at task start
Working tree at RELEASE_FULL: CLEAN
```

The final `RELEASE_FULL` ran on this unchanged implementation candidate.

## TDD / Verification Results

```text
RED baseline: SESSION_RENAME_RED 10/26 FAIL
GREEN after implementation: SESSION_RENAME_RED 26/26 PASS
AFFECTED: TASK040_AFFECTED 54/54 PASS
RELEASE_FULL: TASK040_RELEASE_FULL 160/160 PASS
Pressure scenarios: 1–248 contiguous and unique
TASK-040 scenarios: 246–248
Launcher shared-body parity: PASS
Launcher lengths: ChatGPT 4483 / Claude 4482 (ceiling 4500)
Git diff check: PASS
```

The RED baseline failed because current command surfaces still used `[Session Envelope]`, `[Session]` was absent, and release routing had no TASK-040 amendment. The same test passed after the bounded rename, demonstrating the test exercised the intended behavior change.

## Canonical Current Command

```text
[Session] : declare, show, or close the user-pre-approved scope of operations for the current session/task
```

Current command help/registry surfaces use `[Session]`. The older longer spelling is not a registered current alias.

## Preserved ENV Semantics

`[Session] declare` uses existing `ENV-*` records in `15 Action Registry` with:

```text
Allowed Operation Types
Target Surfaces
Expiry
Prohibited Zones
```

`show` displays current validity and `close` ends the Envelope early. Goal-derived `ENV-*` remains equal to or narrower than its parent `AUTH-*`.

No `SESSION-*` family is created.

## Preserved Authority Boundaries

The rename grants no new authority. Existing gates remain unchanged for:

```text
Project Location / Binding mutation
Root Governance mutation
schema / slot authority
secret handling
push / publication
destructive actions
external disclosure
higher-level platform / tool confirmation
```

Ambiguous or out-of-scope operations continue to fail closed to normal approval.

## Historical Integrity

Fresh verification confirmed these historical artifacts remained byte-unchanged relative to the task base:

```text
Framework-Source/references/framework-governance-amendment-260825-task021.md
Framework-Source/references/framework-governance-amendment-260829-task024.md
docs/superpowers/specs/2026-08-25-task021-mcp-continuity-design.md
docs/superpowers/evidence/2026-08-25-task-021-mcp-continuity-release-full.md
```

The TASK-021 amendment and evidence still contain the historical `[Session Envelope]` spelling, preserving provenance.

## Current Surfaces Updated

```text
README.md
Framework-Source/FRAMEWORK-RELEASE.yaml
Framework-Source/SKILL.md
Framework-Source/references/core-governance-rules.md
Framework-Source/references/framework-governance-amendment-260831-task040.md
Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md
Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md
Framework-Source/templates/00-project-source-framework.md
Framework-Source/templates/project-source-mockup/15-Action-Registry.template.md
Framework-Source/MIGRATION-NOTES.md
Framework-Source/tests/pressure-scenarios.md
docs/superpowers/PROJECT-TASKS.md
```

The maintained root starter command registry also regains the bounded session command using the new canonical `[Session]` name.

## Release / Compatibility Decision

Framework stays `1.8.0`; Schema stays `1.0.0`; release format stays `3`. TASK-040 is a command-name-only amendment within the current Framework 1.8.0 line. `FRAMEWORK-RELEASE.yaml` now routes the latest amendment to `framework-governance-amendment-260831-task040.md`.

## Result

TASK-040 implementation candidate satisfies the explicit user-requested rename with AFFECTED `54/54 PASS` and final unchanged-candidate RELEASE_FULL `160/160 PASS`. The command is now `[Session]`; `ENV-*` behavior and authority boundaries are unchanged; historical provenance remains intact.

`commit ≠ push`; publication remains `NOT_PUSHED`.
