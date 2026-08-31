# TASK-038 Framework-Source Distribution-Root Migration — Release Evidence

Date: `2026-08-29` (Asia/Bangkok)
Task: `TASK-038`
Framework distribution candidate: `1.8.0`
Project Source Schema: `1.0.0`
Release format: `3`
Publication state at evidence capture: `NOT_PUSHED`

## Candidate identity

```text
Candidate HEAD: d068914e5fdc12eb9055ff5bae28cf57962495b4
Candidate tree: f6c6bba9113308d60354112245f4d7574a350191
Framework-Source distribution tree: 5e254140867195c37a2eef9ce6aadb03890af858
Branch: main
Working tree before RELEASE_FULL: CLEAN
Fresh origin/main observed: eb231ee2d1d83b42455ab2f3cab250d4d442fda0
Base freshness: remote main is an ancestor of the candidate; candidate was local-ahead only at verification time
```

The candidate above is the unchanged Framework/TASK-038 implementation state verified by the final full check. This evidence file and later Project Source/Task reconciliation are post-verification metadata; they do not change the verified `Framework-Source/` distribution tree.

## Implementation checkpoints

```text
80ac496  test: define Framework-Source migration scenarios
fb24141  refactor: rename Framework distribution root
5757660  docs: propagate Framework-Source 1.8 starters
d068914  docs: reconcile Project Source after Framework rename
```

TASK-038 design/plan checkpoints were committed earlier and remain referenced from the Task source.

## AFFECTED verification

Result:

```text
AFFECTED 74/74 PASS
Scenarios: 1–188 contiguous/unique; TASK-038 scenarios 181–188 present
```

Coverage included:

- exactly one live `Framework-Source/` reusable distribution root;
- no live `managing-project-source/` root/alias;
- current Framework release `1.8.0 / 1.0.0 / format 3` and TASK-038 latest amendment;
- README/Core Governance/SKILL/current launcher routing on `Framework-Source/`;
- 24/24 maintained starter version stamps at Framework `1.8.0` / Schema `1.0.0`;
- launcher shared marker bodies byte-identical, lengths `4285 / 4284`, and `[Goal]` not prematurely implemented;
- `PROJECT-BOOTSTRAP.md` continues to route active `Project-Source/00 → 01 → 03`, with `09` continuation;
- active ProjectFramework `FRAMEWORK-001` remains locally pinned to Framework `1.7.0` / Schema `1.0.0`;
- active Project Source current-path reconciliation plus `MIG-001`, `ACT-002`, `CHG-003`, `EVD-003`;
- selected historical blobs preserved;
- remaining old-path references role-classified instead of globally rewritten;
- `git diff --check` PASS and clean working tree.

The first AFFECTED checker run reported `72/74` because two assertions in the ignored scratch verifier were defective: one case-sensitive Scenario 181 title token and one omitted allowlist entry for the mockup README's explicit historical-name explanation. No tracked source changed. After correcting only the ignored verifier, the same committed candidate passed `74/74`.

## Historical provenance preservation

Selected Git-blob-compatible SHA-1 sentinels remained unchanged after the directory migration:

```text
Framework-Source/references/framework-governance-amendment-260820-0735.md
7f2156f28a031680322e3a4e16cff45bf803cb94

Framework-Source/references/framework-governance-amendment-260820-0821.md
5ad06a827829fe5c96ae9a8c8c17e1071b1f4f1d

Framework-Source/references/framework-governance-amendment-260825-task020.md
e6a074b77fb0165de1c281eabfbab7c6c938d6e3

docs/superpowers/specs/2026-08-29-task023-self-bootstrapping-project-design.md
9fcf09e3bcc6f2c9c46ae9f2ec98682f87f48f5e

docs/superpowers/evidence/2026-08-29-task-023-self-bootstrapping-project-release-full.md
fef1b9d976e9ab227f90fce6258a83743e9532a8
```

Historical path strings remain valid historical/capture-time truth. Verification found `55` tracked files containing `managing-project-source/`; every match was classified into an allowed historical/migration role. No current canonical README/Core/SKILL/launcher or active Project Source routing surface still treats the old root as current.

## RELEASE_FULL

Final result on the unchanged candidate:

```text
RELEASE_FULL PASS 198/198
Candidate HEAD: d068914e5fdc12eb9055ff5bae28cf57962495b4
Candidate tree: f6c6bba9113308d60354112245f4d7574a350191
Framework-Source distribution tree: 5e254140867195c37a2eef9ce6aadb03890af858
Changed files from TASK-038 implementation base: 79
Launcher lengths: 4285 / 4284
Scenarios: 188 (last = 188)
Maintained starter stamps: 24
Role-classified tracked old-path files: 55
Fresh origin/main at verification: eb231ee2d1d83b42455ab2f3cab250d4d442fda0
```

The first full-verifier execution reported `197/198`: the source amendment correctly states that a newer distribution does not override the active local `Project-Source/00 / FRAMEWORK-001` pin, but the scratch checker searched only for the literal phrase `local pin`. The checker was corrected to assert the actual approved phrase; no tracked candidate content changed. The final full verification above then passed `198/198` on the same exact HEAD/tree.

## Migration result

```text
Canonical reusable Framework distribution root: Framework-Source/
Historical pre-1.8 root name: managing-project-source/
Live old-root alias: NONE
Framework upstream current release: 1.8.0 / Schema 1.0.0
ProjectFramework active local Project Source Framework pin: 1.7.0 / Schema 1.0.0
ProjectFramework Project UUID: 00575e76-17ce-4dd3-ad24-377494a4a45b (unchanged)
Project Location Binding: unchanged
PROJECT-BOOTSTRAP authority route: Project-Source/00 → 01 → 03; 09 continuation (unchanged role)
```

This is a repository/distribution-path migration, not an automatic `[Project Upgrade]` of ProjectFramework's own initialized Project Source.

## Completion readiness

All TASK-038 implementation and verification criteria required before final lifecycle reconciliation are satisfied. Final Project Source/Task metadata may now mark `ACT-002` and `MIG-001` complete, set current state/handoff to the TASK-039 continuation, and mark `TASK-038` `DONE` while preserving publication separately as `NOT_PUSHED` until a fresh authorized push occurs.
