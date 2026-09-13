# ProjectFramework Transaction Mode Optimization Roadmap

Date: `2026-09-13` (Asia/Bangkok)
Document type: `PLANNING_PROPOSAL / UPSTREAM_ROADMAP`
Task allocation: `NOT_ALLOCATED`
Stable-ID allocation: `NOT_ALLOCATED`
Implementation state: `NOT_STARTED`
Recommended sequencing: `IMPLEMENT_AFTER_CURRENT_TASK051/TASK052_LINEAGE_IS_STABLE`

## 1. Purpose

Define an upstream optimization program that keeps ProjectFramework governance strength while materially reducing elapsed governance ceremony, repeated namespace/revision collision scans, redundant checkpoints, repeated release verification, and multi-round approval latency.

The target operating model is a **ProjectFramework Transaction Mode**:

```text
one canonical read
→ one bounded assessment
→ one namespace/revision reservation
→ one exact Preview
→ one explicit approval
→ one isolated mutation transaction
→ one final Manifest build
→ one final candidate verification
→ one completion commit
→ one fresh integration gate
→ one publication/readback sequence when authorized
```

The intended result is not weaker governance. The intended result is the same or stronger auditability with fewer intermediate artifacts and fewer repeated proof operations.

## 2. Existing Upstream Foundation

This roadmap MUST build on, not replace, the following existing upstream work:

- `TASK-051 Risk-Tiered Feature Delivery Fast Path`
  - Derived Delivery Tier `LOW | MEDIUM | HIGH` over canonical `R0–R3`.
  - Tiered preflight/review/verification.
  - Stable evidence reuse while assumptions remain bound.
  - One-session LOW objective.
  - Direct Git/GitHub eligibility without synthesizing authority.
  - Task acceptance remains distinct from `RELEASE_FULL` and `INTEGRATION_GATE`.

- `TASK-052 Project Upgrade One-Session Fast Path`
  - One comparison/assessment.
  - One exact Preview.
  - One explicit mutation approval.
  - One bounded mutation batch.
  - Exact reusable upstream release-proof reuse.
  - One completion commit and terminal readback.
  - No per-document checkpoint requirement absent a real continuation boundary.

Transaction Mode is the umbrella operational model that generalizes those principles to Project Source mutation, migration, publication preparation, and other bounded governance workflows.

## 3. Problem Statement

ProjectFramework has strong authority, history, evidence, and verification semantics, but current execution can still become disproportionately slow when several of these behaviors combine:

1. Stable IDs and primary revisions are allocated by repeated global scans rather than a bounded reservation transaction.
2. Parallel governance work can consume the same next IDs/revisions while another workflow is preparing its candidate.
3. Goal persistence, preview wrappers, publication wrappers, forward-port reconciliation, Root mutation, and publication can become separate bookkeeping transactions even when they are one logical outcome.
4. Index, Current State, Handoff, registries, PMCTRL, and Manifest may be rotated at multiple intermediate points instead of once at the final meaningful state transition.
5. Manifest generation may occur repeatedly before the final candidate is frozen.
6. `RELEASE_FULL` can be rerun when exact valid release proof or an unchanged final candidate already exists.
7. Tool/transport syntax failures can cause workflow churn even when Project evidence remains valid.
8. Mutable-target freshness is sometimes checked repeatedly during preparation instead of at the boundaries where freshness materially matters.
9. Concurrent writers can cause repeated re-freeze cycles because no single-writer or namespace reservation rule exists for a bounded governance transaction.
10. The Framework does not currently expose a measurable governance-friction budget, so ceremony can grow without an explicit cost signal.

## 4. Design Goals

Transaction Mode MUST:

- preserve canonical `R0–R3`, authority, Root/Binding, disclosure, secret, destructive, Production, and publication gates;
- preserve Stable-ID uniqueness and non-recycling;
- preserve reconstructable Project Source history;
- preserve exact rollback/revert routes;
- preserve `Task DONE ≠ push ≠ merge ≠ release`;
- preserve `RELEASE_FULL` at release/equivalent acceptance boundaries;
- preserve a fresh `INTEGRATION_GATE` before mutable-target shared actions;
- reduce repeated Owner prompts when one exact approval already covers the bounded transaction;
- prevent namespace/revision collision races through reservation rather than repeated discovery;
- prefer one isolated worktree and one final candidate per logical transaction;
- make deterministic generated metadata non-material for reapproval purposes;
- build Manifest once per final candidate unless a material candidate change invalidates it;
- make interruption/recovery reuse unchanged evidence instead of restarting from zero;
- distinguish tool execution failure from governance-state invalidation;
- define measurable governance-friction budgets and acceptance criteria; and
- remain documentation/governance-first without requiring a daemon, service, scheduler, watcher, or persistent runtime.

## 5. Non-Goals

Transaction Mode does NOT:

- auto-authorize Root mutation;
- auto-authorize push/PR/merge/release/deployment;
- weaken HIGH-risk review or verification requirements;
- create a second Risk model;
- create a new Stable-ID family merely for transactions;
- allow namespace reservations to permanently consume unused Stable IDs;
- eliminate Project Source archives/history;
- make Manifest optional;
- eliminate `RELEASE_FULL` where no valid reusable proof exists;
- eliminate `INTEGRATION_GATE`;
- serialize unrelated repositories/Projects globally; or
- introduce runtime transaction infrastructure as a prerequisite for governance correctness.

## 6. Transaction Model

A governance transaction is a bounded working contract, not a new canonical lifecycle family.

Recommended working vocabulary:

```text
ASSESS
RESERVE
PREVIEW
APPROVE
MUTATE
VERIFY
COMMIT
INTEGRATE
READBACK
CLOSE
```

These are execution phases only and MUST NOT become a competing Stable-ID/lifecycle family unless separately justified.

### 6.1 Transaction identity

A transaction SHOULD be identified by existing Project/Task/Goal/AUTH context plus exact Git/worktree state. A separate permanent `TX-*` Stable-ID family is NOT recommended.

### 6.2 Transaction fingerprint

The Preview SHOULD bind a deterministic transaction fingerprint derived from material assumptions, including:

- Project UUID;
- canonical base commit/tree;
- exact target release/content identity;
- bounded affected semantic slots/files;
- requested authority scope;
- namespace/revision reservation set;
- rollback route;
- verification plan;
- publication scope when applicable.

Deterministic timestamps/filenames derived after approval are not material fingerprint changes unless they change semantics or collide with an occupied reservation.

## 7. Namespace and Revision Reservation

### 7.1 Reservation objective

Replace repeated "find the next free ID" scans with one reservation pass at transaction start.

A transaction MAY reserve:

```text
Stable IDs required by the approved bounded outcome
+ primary successor revisions
+ archive destination names
+ one optional contingency range when justified
```

### 7.2 Reservation is not canonical consumption

Reservation MUST distinguish:

```text
RESERVED_WORKING
CONSUMED_CANONICAL
RELEASED_UNUSED
```

Only materialized/committed canonical records consume Stable IDs permanently.

A failed or cancelled transaction releases unused reservations without creating ghost history.

### 7.3 Collision boundary

Before mutation:

- scan committed reachable Project history;
- scan active governed worktrees for currently reserved/materialized conflicting IDs;
- atomically freeze the reservation set for the transaction.

After reservation, concurrent writers MUST NOT allocate from the same reserved set.

### 7.4 Reservation storage

Preferred order:

1. Git/worktree-local ignored transaction ledger or equivalent ephemeral local state;
2. existing governed Task/Plan evidence when persistence is required across sessions;
3. canonical Project Source only when reservation itself is materially relevant to durable Project truth.

Do not rotate Project Source registries merely to record an ephemeral reservation.

## 8. Single-Writer Governance Transaction

For one Project Source namespace, a HIGH governance mutation transaction SHOULD be single-writer from approved mutation start through final local candidate commit.

Other work MAY:

- read current Project Source;
- perform unrelated application/runtime work in independent worktrees;
- prepare non-conflicting drafts;
- reserve a disjoint namespace block if the Framework can prove independence.

Other work MUST NOT consume the active transaction's reserved Stable IDs/revisions or mutate overlapping canonical Project Source slots.

This is a transaction-scoped writer lock, not a global Project freeze.

## 9. Artifact Scaling

Transaction Mode SHOULD scale artifacts to risk and interruption need.

### 9.1 Normal compatible transaction

Expected minimum durable artifacts:

```text
one exact Preview
one applicable authority record when required
one final successor set
one final Manifest
one verification/evidence record
one completion commit
one terminal readback
```

### 9.2 Intermediate wrappers

A separate preview wrapper, publication-preparation wrapper, forward-port wrapper, or bookkeeping checkpoint SHOULD NOT be created when all of the following are true:

- the semantic candidate is unchanged;
- the same exact transaction authority covers the next local phase;
- interruption recovery can reconstruct state from Git + Preview + evidence;
- no new shared/external action has occurred;
- no material assumption has changed.

Create an intermediate durable checkpoint only at a real continuation boundary.

## 10. Goal Persistence Optimization

A `[Goal]` SHOULD NOT force immediate rotation of Index/State/Handoff/Manifest solely to persist a simple bounded outcome when the Goal can be represented durably without changing current Project semantics.

Recommended policy:

- use existing Goal/Task durable state surface when available;
- materialize Project Source Goal records only when the Goal becomes material Project truth requiring reconstructability from Project Source;
- avoid multiple Project Source rotations for Goal declaration, Goal forward-port, and Goal execution when one final transaction can preserve the same truth.

`ACT DONE ≠ OUT ACHIEVED` remains unchanged.

## 11. Manifest Optimization

### 11.1 Final-candidate Manifest

Normal transaction budget:

```text
Manifest generation: 1 per unchanged final candidate
```

Intermediate Project Source files MAY be verified through Git index/tree identity before final Manifest materialization.

### 11.2 Regeneration trigger

Regenerate Manifest only when the candidate content set changes after the previous Manifest build.

Metadata-only execution events outside the candidate tree do not invalidate it.

## 12. Verification Budget

Transaction Mode composes TASK-051 and TASK-052 verification rules.

Recommended normal budgets:

| Boundary | Normal budget |
|---|---:|
| structural/affected checks during mutation | as needed, focused |
| `CHECKPOINT_INTEGRITY` | 0–1 at a real continuation boundary |
| final Manifest verification | 1 per unchanged candidate |
| `RELEASE_FULL` | 0 with exact reusable proof where contract permits, otherwise 1 |
| `INTEGRATION_GATE` | 1 immediately before mutable-target action |
| terminal remote readback | 1 after integration |

Repeated `RELEASE_FULL` without material candidate invalidation SHOULD be treated as a process defect.

## 13. Approval Bundling

An exact Preview MAY request one approval covering multiple state-bound phases, for example:

```text
local Root mutation
+ final verification
+ conditional non-force branch publication
+ PR creation
+ normal merge
+ exact remote-main readback
```

The approval MUST remain conditional on verification/freshness gates.

Bundling authority does not skip any gate. It removes unnecessary Owner round-trips when the same exact scope was already approved.

## 14. Tool Failure and Recovery

Tool syntax failure, transport retry, or equivalent execution-surface failure does not invalidate Project evidence automatically.

On interruption:

1. determine whether any side effect may have occurred;
2. if result is unknown for a non-idempotent/shared action, classify `RESULT_VERIFICATION_REQUIRED`;
3. otherwise re-read only the affected execution state;
4. preserve still-valid canonical base, reservation, Preview, authority, and release evidence;
5. resume unfinished transaction work.

Do not create new governance revisions solely because a shell/file primitive failed before mutation.

## 15. Governance Friction Budget

ProjectFramework SHOULD make governance cost visible.

For each material transaction record or evidence report, capture when practical:

```text
owner_approval_count
preview_count
namespace_scan_count
reservation_reallocation_count
primary_rotation_count
manifest_generation_count
checkpoint_commit_count
release_full_count
integration_gate_count
publication_round_trip_count
elapsed_human_wait_points
```

### 15.1 Initial optimization targets

For a normal compatible one-session Project upgrade:

```text
owner_approval_count <= 1 mutation approval
preview_count = 1
namespace reservation = 1
reservation reallocation = 0 under normal uncontended execution
manifest generation = 1
RELEASE_FULL <= 1 and preferably 0 when exact upstream proof is reusable
completion commit = 1
integration gate = 1
publication flow = 1 non-force branch/PR/merge/readback sequence
```

These are optimization objectives, not authority overrides.

## 16. Required Upstream Changes

A future implementation task SHOULD review and, where needed, update:

- `Framework-Source/references/core-governance-rules.md`
- `Framework-Source/SKILL.md`
- `Framework-Source/templates/upgrade-preview.md`
- `Framework-Source/templates/00-project-source-framework.md`
- `Framework-Source/templates/core-document-skeletons.md`
- `Framework-Source/tests/pressure-scenarios.md`
- `Framework-Source/MIGRATION-NOTES.md`
- current README/user guidance

The implementation SHOULD explicitly reconcile this roadmap with TASK-051 and TASK-052 rather than create a competing fast-path contract.

## 17. Required Pressure Scenarios

At minimum test:

1. two concurrent transactions attempt the same next Stable ID;
2. reservation prevents collision without consuming unused canonical IDs;
3. abandoned reservation releases cleanly;
4. one transaction owns overlapping Project Source primary slots;
5. disjoint work continues concurrently;
6. one Preview approval covers conditional publication after PASS;
7. deterministic revision/timestamp generation does not require reapproval;
8. material semantic scope change does require re-Preview/reapproval;
9. unchanged candidate does not rerun Manifest/RELEASE_FULL;
10. tool failure before mutation preserves valid transaction evidence;
11. unknown non-idempotent result requires verification before retry;
12. interrupted transaction resumes without redoing completed proof;
13. Goal declaration does not force unnecessary primary rotations;
14. normal compatible upgrade meets the friction budget;
15. HIGH/root/security/destructive work still retains mandatory gates.

## 18. Phased Implementation

### Phase A — Measure

- instrument current TASK-051/TASK-052 workflows with friction-budget counters in evidence;
- establish baseline elapsed ceremony on representative LOW/MEDIUM/HIGH changes and Project upgrades;
- identify the most frequent redundant state transitions.

### Phase B — Reservation + Single Writer

- define transaction reservation semantics;
- add concurrency pressure scenarios;
- implement reservation/release rules;
- add transaction-scoped single-writer rule for overlapping Project Source mutation.

### Phase C — Artifact and Manifest Scaling

- remove required intermediate wrappers/checkpoints where no real continuation boundary exists;
- move Manifest generation to final-candidate boundary;
- define lightweight Git-index/tree integrity checks during mutation.

### Phase D — Approval + Verification Budget

- standardize bundled conditional approval;
- enforce one final verification budget;
- treat repeated unchanged-candidate `RELEASE_FULL` as process defect evidence.

### Phase E — Adoption

- update upgrade/feature templates;
- add migration guidance for existing Projects;
- measure before/after friction metrics;
- retain rollback to the prior workflow for projects that cannot satisfy transaction-mode assumptions.

## 19. Acceptance Criteria

Transaction Mode is successful only when all are true:

- canonical authority/safety semantics remain unchanged or stricter;
- Stable-ID collision races are prevented without ghost consumption;
- a normal compatible upgrade can complete with one Preview and one mutation approval;
- no per-document checkpoint is required absent a real continuation boundary;
- final Manifest is generated once per unchanged candidate;
- `RELEASE_FULL` is not redundantly rerun;
- shared integration remains protected by fresh `INTEGRATION_GATE`;
- interruption recovery does not restart the workflow unnecessarily;
- friction metrics show a material reduction in approvals/checkpoints/scans/verification runs;
- pressure scenarios prove concurrent and failure behavior; and
- existing Brownfield Projects remain no-auto-adopt.

## 20. Relationship to Option 3

Transaction Mode SHOULD be implemented and measured before Structured Core + Generated Governance.

Option 2 optimizes the current Markdown/Project Source architecture with limited migration risk. Its friction metrics will reveal which manually synchronized surfaces remain expensive enough to justify Option 3.

The recommended sequence is:

```text
TASK-051 / TASK-052 foundation
→ Transaction Mode optimization
→ measure real residual friction
→ decide whether/where Structured Core + Generated Governance is justified
```
