# TASK-025 Project Knowledge Layer — Release Evidence

## Evidence identity

- **Task:** `TASK-025` — Project Knowledge Layer / Compounding Knowledge Contract
- **Release:** Framework `1.10.0` / Schema `1.0.0` / release format `3`
- **Branch:** `task025-project-knowledge`
- **Publication:** `NOT_PUSHED`
- **Implementation scope:** documentation/governance/templates/tests only; no wiki engine, vector database, UI, watcher, crawler, auto-ingest daemon, embedding pipeline, MCP wiki service, runtime automation, CI/CD, or executable validator/CLI added
- **Design spec:** `docs/superpowers/specs/2026-09-01-task025-project-knowledge-layer-design.md`
- **Implementation plan:** `docs/superpowers/plans/2026-09-01-task025-project-knowledge-layer.md`

## Approved architecture

TASK-025 implements an optional **Derived Markdown Project Knowledge Layer** with the invariant:

```text
Project Knowledge ≠ Project Authority
Derived synthesis ≠ Evidence ≠ Governed Project truth
Retrieval rank/confidence/recency ≠ Authority
Knowledge promotion ≠ automatic mutation
```

The maintained distribution representation is `Framework-Source/templates/project-knowledge/` with four files:

```text
README.md
index.md
log.md
page-template.md
```

A consuming Project may materialize root `Project-Knowledge/` only when applicable and approved. Knowledge pages are advisory/derived; Knowledge→Governance promotion routes through existing canonical Project Source homes and authority gates. External-AI use remains subject to TASK-026 disclosure governance. Project Knowledge cross-links are not `REL-*`; OpenViking remains `DERIVED_ONLY` / rebuildable and must preserve `PROJECT_SOURCE_AUTHORITY` versus `PROJECT_KNOWLEDGE_ADVISORY` content classes.

## Design and planning evidence

- Written design checkpoint: `ec9911451f6a1271b473e7f1a02e8e3c1cd3d1f7`
- Spec self-review: `TASK025_SPEC_SELF_REVIEW 42/42 PASS`
- User written-spec approval: explicit `[Goal] ทำจนจบ task` on `2026-09-01`
- Goal checkpoint: `0147d7a`
- Implementation plan commit: `187c802`
- Plan self-review: `TASK025_PLAN_REVIEW 43/43 PASS`
- Plan checkpoint: `f59e250`

## TDD evidence

Task 1 created pressure scenarios `269–288` before production Framework changes.

```text
Scenario range after Task 1: 1–288 contiguous/unique
Initial TASK025_RED: 33/68 FAIL (expected)
Failure basis: Framework 1.10.0 identity/amendment/Core/SKILL/Project Knowledge templates were not implemented yet
Scenario contract commit: 64823a9
RED checkpoint commit: 755e21d
```

After implementation:

```text
TASK025_RED 68/68 PASS
Scenarios 1–288 contiguous/unique
```

This establishes observed RED→GREEN progression for the governed behavior change.

## Implementation checkpoints

- Normative Framework 1.10.0 implementation: `1c7be78`
  - focused verification: `TASK025_TASK2 62/62 PASS`
- Project Knowledge maintained templates + current-surface propagation: `ed5aa4d`
  - focused verification: `TASK025_TASK3 77/77 PASS`
- Maintained Project Knowledge template files: `4`
- Maintained Project Source starter stamps: `22` at Framework `1.10.0` / Schema `1.0.0`
- Vendor launchers: unchanged from branch base
- ProjectFramework local Project Source pin: preserved at Framework `1.7.0` / Schema `1.0.0`

## AFFECTED verification

Comprehensive affected verification result:

```text
TASK025_AFFECTED 175/175 PASS
SCENARIOS 288
KNOWLEDGE_TEMPLATES 4
STARTER_STAMPS 22
FAILS []
```

Coverage included release identity/latest amendment, Project Knowledge authority separation, page schema/states, `index.md`/`log.md`, ingest/query-file/lint semantics, source provenance, Knowledge→Governance promotion, Meeting/EVD/TASK-026/03/09/92/OpenViking boundaries, GREENFIELD optionality, Brownfield no-auto-adoption, no secret-value permission, unchanged thin launchers, historical preservation, no runtime/executable expansion, local Project Source pin preservation, and Git diff hygiene.

## Invalidated candidate provenance

The first implementation candidate was:

```text
HEAD: 2688c995448131b2154b3fa505acaef6352389d3
Tree: f96c601efdc55e7b603a4c44901ed74f49ac2038
Framework-Source tree: d39c4550a4272e3ae2c5f957ec444f93bd514485
RELEASE_FULL: 119/120 FAIL
AFFECTED: 175/175 PASS
```

The sole release failure was `git diff --check` caused by extra EOF blank lines in three branch-created archived Project Source revisions. No Framework/Knowledge semantic check failed. This candidate was explicitly invalidated before evidence reuse.

The hygiene correction commit is `99c2f5a90e0c8f02dd68001d0e22b5362cd45a03`; the Framework-Source tree remained unchanged across that correction.

## Final corrected candidate

```text
Candidate HEAD: 99c2f5a90e0c8f02dd68001d0e22b5362cd45a03
Candidate tree: 26d1f5354ab0a59616b9fbca28d25c74ac6746ca
Framework-Source tree: d39c4550a4272e3ae2c5f957ec444f93bd514485
Working tree at candidate freeze: CLEAN
Candidate diff check: PASS
```

## Final RELEASE_FULL

A state-bound final RELEASE_FULL was run on the corrected unchanged candidate and completed successfully on `2026-09-01T15:19:58+07:00`:

```text
TASK025_RELEASE_FULL 120/120 PASS
CANDIDATE_HEAD 99c2f5a90e0c8f02dd68001d0e22b5362cd45a03
CANDIDATE_TREE 26d1f5354ab0a59616b9fbca28d25c74ac6746ca
FRAMEWORK_SOURCE_TREE d39c4550a4272e3ae2c5f957ec444f93bd514485
AFFECTED TASK025_AFFECTED 175/175 PASS
SCENARIOS 288
KNOWLEDGE_TEMPLATES 4
STARTER_STAMPS 22
CHANGED_FROM_MAIN 89
FAILS []
```

No Framework/current-contract mutation occurred after this successful candidate-bound release verification before this evidence file was written.

## Completion basis

The release evidence supports terminal evaluation of `ACT-013` and `OUT-003` after this evidence is committed and Project Source terminal reconciliation is validated/promoted/committed. `ACT DONE ≠ OUT ACHIEVED`; terminal state is not asserted by this evidence file alone.

`commit ≠ push`. TASK-025 publication remains `NOT_PUSHED`, and no publication authority is inferred from the persistent Goal.
