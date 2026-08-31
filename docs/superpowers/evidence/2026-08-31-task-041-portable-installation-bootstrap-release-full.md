# TASK-041 Portable Installation Bootstrap & Project Settings Handoff — Release Evidence

- **Task:** `TASK-041`
- **Target Release:** Project Source Framework `1.9.0` / Schema `1.0.0` / release format `3`
- **Design Spec:** `docs/superpowers/specs/2026-08-31-task041-portable-installation-bootstrap-design.md`
- **Implementation Plan:** `docs/superpowers/plans/2026-08-31-task041-portable-installation-bootstrap.md`
- **Verification Date:** `2026-08-31`
- **Publication:** `NOT_PUSHED`

## State-Bound Candidate

```text
Candidate HEAD: f5cee5fb2f3cb4da7967f56dcb294ce2a1703530
Candidate Tree: 71756d53cbbcff54883915f24ef353e40b37bda6
Framework-Source Tree: 06ce4013473ec014e70d8d3233f6132aa90339fd
Working Tree At RELEASE_FULL: CLEAN
```

The final `RELEASE_FULL` was run once on this unchanged candidate. Any later Framework contract mutation invalidates this state-bound release evidence and would require a new candidate/run.

## TDD / Progressive Verification History

```text
Task 1 RED baseline:
  TASK041_RED 40/97 FAIL
  Expected reason: Framework 1.9.0 behavior absent before implementation

After Task 2 normative contract:
  TASK041_TASK2_NORMATIVE 51/51 PASS
  TASK041_RED 50/97 FAIL

After Task 3 thin adapters:
  TASK041_TASK3 42/42 PASS
  TASK041_RED 73/97 FAIL

After Task 4 README/starter propagation:
  TASK041_TASK4 53/53 PASS
  Maintained starter stamps: 24 / all Framework 1.9.0 / Schema 1.0.0
  TASK041_RED 93/97 FAIL
  Remaining failures: migration-only

After Task 5 migration:
  TASK041_RED 97/97 PASS
  TASK041_AFFECTED 273/273 PASS
```

## Final RELEASE_FULL

```text
TASK041_RELEASE_FULL PASS 248/248
CANDIDATE_HEAD f5cee5fb2f3cb4da7967f56dcb294ce2a1703530
CANDIDATE_TREE 71756d53cbbcff54883915f24ef353e40b37bda6
FRAMEWORK_SOURCE_TREE 06ce4013473ec014e70d8d3233f6132aa90339fd
AFFECTED TASK041_AFFECTED 273/273 PASS
SCENARIOS 268 268
TEMPLATE_STAMPS 24
LAUNCHER_LENGTHS 513 512
CHANGED_FROM_MAIN 96
FAILS []
```

## Verified Contract Results

1. Framework release identity is exactly `1.9.0 / 1.0.0 / 3`; latest amendment is TASK-041.
2. Canonical Project Settings adapter is the two-binding `ProjectFramework Upstream` + verified absolute `Project Bootstrap` contract with the approved three-line Bootstrap Rule.
3. Fixed upstream remains `https://github.com/captainhuke-dev/ProjectFramework` and never becomes consuming Project repository/authority.
4. Maintained ChatGPT/Claude launchers are thin adapters; legacy five mandatory Project Settings fields/full shared governance payload are absent from current launchers.
5. Thin launcher semantic body parity passes; lengths are `513 / 512`, below the existing `<=4,500` ceiling.
6. `framework_source`, `remote_location`, `file_storage_locations`, `mcp_location`, `local_workspace`, `current_branch_worktree`, dedicated Drive semantics, and `[Project Path]` remain available internally.
7. Root `PROJECT-BOOTSTRAP.md` documents Project Settings primary entry and consuming README fallback while remaining locator-only.
8. Upstream repository `README.md` contains exactly one valid managed `PROJECTFRAMEWORK-BOOTSTRAP` block using portable `./PROJECT-BOOTSTRAP.md`.
9. Upstream README documents GREENFIELD install intent, one Preview/approval cycle, core installation completion, required user handoff, authority separation, and Brownfield upgrade behavior.
10. Upstream README contains the exact mandatory response-close headings/fields plus lifecycle coupling and nothing-after-Required-Read rule.
11. Root Framework template, core skeletons, and mockup README propagate portable bootstrap/managed README/Project Settings handoff semantics without creating a new lifecycle family.
12. All `24` current maintained template/frontmatter Framework stamps are `1.9.0`; Schema stamps remain `1.0.0`.
13. Mandatory/conditional/reserved slot integrity remains valid; `18–19` remain unmaterialized/reserved in current mockup.
14. Pressure scenarios `1–268` are contiguous and unique; TASK-041 scenarios are exactly `249–268`.
15. `MIGRATION-NOTES.md` contains current `1.8.0 → 1.9.0` Brownfield guidance, including managed README preservation, absolute-vs-relative path semantics, no vendor-settings claim without observation, retained internal location semantics, active `FRAMEWORK-001` authority, and Direct-to-Latest behavior.
16. GREENFIELD installation does not synthesize Goal/OUT/AUTH/ENV/Meeting/provider/disclosure/secret-value/runtime/daemon state merely because ProjectFramework is installed.
17. No runtime/code/CLI/bot/hook/CI/watcher/scheduler/daemon artifact was introduced; changed tracked scope is Markdown/YAML only.
18. Selected historical amendments/evidence remain byte-unchanged relative to canonical `origin/main` baseline.
19. No live pre-1.8 `managing-project-source/` distribution root exists.
20. ProjectFramework's own active Project Source remains locally pinned at Framework `1.7.0 / Schema 1.0.0`; implementing upstream Framework `1.9.0` did not auto-upgrade the Project-local pin.
21. Persistent TASK-041 Goal authority remained bounded; push/publication was not included and no publication occurred.
22. `git diff --check` and exact-candidate working-tree cleanliness passed at RELEASE_FULL.

## Implementation Commits Before Candidate

```text
Task 1 scenarios / RED contract:
  a14eeb2c476f6de812bd8b3bcd69a551814b3448

Task 2 normative 1.9.0 contract:
  61bfb3724347a4cba988d987604ade92f66cc45d

Task 3 thin adapters:
  062c20a8bedc002650dd059e65b1fa792db6dd8c

Task 4 README / starter propagation:
  5d2349ab2e89091e7bbf31c5ae2d9a76e7fc1e6e

Task 5 final implementation candidate:
  f5cee5fb2f3cb4da7967f56dcb294ce2a1703530
```

Project Source continuity checkpoint commits between implementation tasks are separate governance persistence commits and do not alter the state-bound Framework-Source tree recorded above.

## Authority / Security Boundary

This evidence records local implementation and verification only. It grants no push/publication, destructive operation, Root/Project Location Binding mutation, external disclosure, provider authority, or permission to store/reveal actual secret values. `commit ≠ push` remains binding.
