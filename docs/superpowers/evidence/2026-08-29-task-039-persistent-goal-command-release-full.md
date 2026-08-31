# TASK-039 Persistent `[Goal]` Command — Release Evidence

Date: `2026-08-29` (Asia/Bangkok)
Task: `TASK-039`
Framework distribution candidate: `1.8.0`
Project Source Schema: `1.0.0`
Release format: `3`
Publication state at evidence capture: `NOT_PUSHED`

## Candidate identity

```text
Candidate HEAD: 0f2ecfde7112a7d7d101e316fc0c3069c8ece5db
Candidate tree: a3adaeef91d3a729f9d14d570400ed73b47ee3a2
Framework-Source distribution tree: 2101c2d22b9d23d0bae3517a6462c4895edecf15
Branch: main
Working tree before RELEASE_FULL: CLEAN
Fresh origin/main observed: eb231ee2d1d83b42455ab2f3cab250d4d442fda0
Tracking at freeze: local main ahead 16 / behind 0
```

The candidate above is the unchanged Framework/TASK-039 implementation state verified by the final full check. This evidence file and later Project Source/Task lifecycle reconciliation are post-verification metadata and do not change the verified Framework distribution candidate.

## Implementation checkpoints

```text
47aadac  test: define persistent Goal command pressure scenarios
25b335d  docs: define persistent Goal command contract
4b3ce45  docs: propagate persistent Goal semantics to starters
0f2ecfd  docs: expose persistent Goal command
```

Design: `docs/superpowers/specs/2026-08-29-task039-persistent-goal-command-design.md`

Implementation plan: `docs/superpowers/plans/2026-08-29-task039-persistent-goal-command.md`

## Implemented contract

Framework `1.8.0` now registers:

```text
[Goal] : create/show/change/cancel a persistent outcome and its bounded continuous-execution authorization
```

Canonical composition is:

```text
OUT-* in 91   = persistent Goal outcome / success evidence
AUTH-* in 12  = persistent user-granted Goal authority
ACT-* in 15   = executable work decomposition
ENV-* in 15   = session/task envelope equal to or narrower than parent AUTH-*
03            = current Goal/status summary
09            = continuation references only; authority_transfer: false
```

No `GOAL-*` Stable-ID family or new semantic slot was introduced.

Goal lifecycle:

```text
ACTIVE | BLOCKED | ACHIEVED | CANCELLED | SUPERSEDED
```

Verified authority boundaries:

- bounded local read/design/plan/edit/test/fix/verify/local-commit/checkpoint work is covered by default unless the user narrows the Goal;
- push/publication is opt-in and target-bound;
- destructive action is opt-in by exact operation + target/conditions;
- Root Governance / Project Location Binding mutation is opt-in by exact mutation + target and still uses the normal revision/validation/promotion/history lifecycle;
- actual secret values remain forbidden;
- external AI/provider disclosure is not implied by Goal execution authority;
- `ENV-*` never expands parent `AUTH-*`;
- partial blockers do not stop independent safe work; global blockers move the Goal to `BLOCKED`;
- cancellation/revocation stops future Goal-authorized execution while preserving history;
- conflicts do not resolve by recency;
- Goal authority does not silently rewrite `REQ-*` / `DEC-*` to simplify completion;
- `ACT DONE ≠ OUT ACHIEVED` and Goal success requires criterion evidence;
- system/developer/product/MCP/tool/authentication controls remain higher-level gates.

## Pressure scenarios

```text
Scenario range: 1–211 contiguous and unique
TASK-039 range: 189–211
```

Scenarios 189–211 cover bracketed identity, case-insensitive command matching, cross-chat resume, stale/revoked authorization, local no-repeat-approval execution, push boundaries, destructive boundaries, Root/Binding boundaries, secret/disclosure boundaries, ENV narrowing, partial/global blockers, cancellation, conflicts, governed REQ/DEC boundaries, outcome evidence, and higher-level tool confirmation.

## AFFECTED verification

Final result:

```text
AFFECTED 43/43 PASS
```

The first affected-verifier run reported `42/43` because the scratch verifier required literal `authority_transfer: false` inside platform launchers. The approved launcher plan requires equivalent compact semantics, and both launchers correctly state `Handoff never transfers authority`; literal `authority_transfer: false` remains present in normative and Handoff/starter surfaces. The checker was corrected only; no tracked candidate source changed.

Affected verification also confirmed:

- Framework `1.8.0` / Schema `1.0.0` / release format `3`;
- latest amendment = TASK-039;
- `[Goal]` on all required current surfaces;
- no canonical `GOAL-*` family;
- OUT/AUTH/ACT/ENV/Handoff composition aligned;
- all Goal lifecycle states aligned;
- default-local and all opt-in authority boundaries aligned;
- Brownfield no-auto-Goal semantics;
- 24/24 maintained starter version stamps remain `1.8.0 / 1.0.0`;
- `18–19` remain RESERVED;
- launchers remain byte-identical in the shared marker body;
- launcher lengths `4469 / 4468`, both within `<=4500`;
- ProjectFramework's active local Project Source pin remains Framework `1.7.0` / Schema `1.0.0`;
- historical TASK-038/TASK-023 amendments/evidence and TASK-039 design/plan remain unchanged from the pre-implementation base;
- `git diff --check` PASS;
- working tree clean.

## RELEASE_FULL

Final result on the unchanged candidate:

```text
RELEASE_FULL PASS 220/220
Candidate HEAD: 0f2ecfde7112a7d7d101e316fc0c3069c8ece5db
Candidate tree: a3adaeef91d3a729f9d14d570400ed73b47ee3a2
Framework-Source tree: 2101c2d22b9d23d0bae3517a6462c4895edecf15
Scenarios: 211 (last = 211)
Maintained starter stamps: 24
Launcher lengths: 4469 / 4468
```

No tracked source changed between the final AFFECTED PASS and this RELEASE_FULL candidate verification.

## Brownfield / migration result

Framework `1.8.0` migration guidance explicitly does not synthesize a persistent Goal from free-text goals, backlog items, old Handoff prose, existing `OUT-*`, or prior “continue” messages. Existing `OUT-* / AUTH-* / ACT-* / ENV-*` are preserved. A persistent Goal begins only through explicit `[Goal]` invocation/adoption under the active contract.

## ProjectFramework self-governance boundary

ProjectFramework's active local Project Source remains pinned to Framework `1.7.0` / Schema `1.0.0`. Implementing TASK-039 in the reusable upstream Framework distribution does not silently upgrade the initialized Project's local pin and does not fabricate an active Goal/OUT/AUTH for this repository from the user's ordinary continuous-work wording.

## Completion readiness

All TASK-039 implementation and verification criteria required before final lifecycle reconciliation are satisfied. Final Project Source/Task metadata may now mark TASK-039 `DONE`, record this evidence, and select the next governed roadmap action. Remote publication remains separate and is `NOT_PUSHED` until an authorized push is actually observed.
