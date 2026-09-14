# TASK-057 — ProjectFramework 1.19 AI-ControlTower Governance Support Layer Design

Date: `2026-09-14` (Asia/Bangkok)
Design state: `DESIGN_SECTIONS_1_TO_6_USER_APPROVED / WRITTEN_SPEC_REVIEW_REQUIRED`
Implementation state: `NOT_STARTED`
Target release: Framework `1.19.0` / Project Source Schema `1.0.0` / release format `3`
Task: `TASK-057`

## 1. Goal and scope

Source Goal (ACTOR-001, 2026-09-14):

> `[Goal] ดำเนิน ProjectFramework 1.19 AI-ControlTower Governance Support Layer ต่อจาก Design Sections 1–2 ที่อนุมัติแล้ว จนถึง verified completion โดยยังไม่ implement AI-ControlTower runtime`

TASK-057 adds a declarative Governance Support Layer so AI-ControlTower, Multica, agents, tools, and future orchestrators can consume ProjectFramework work contracts deterministically without becoming Project authority.

The selected architecture is **Approach A — Schema-first Declarative Contracts**.

This release MUST preserve all existing ProjectFramework authority, Risk, Task lifecycle, evidence, publication, and source-of-truth semantics. It MUST NOT revive the cancelled ProjectFramework 2.0 / Control Plane line.

## 2. Authority model and non-runtime boundary

The authority model is:

```text
ProjectFramework
= governance contract semantics

Project Source
= canonical Project governance truth

Durable Task Source
= canonical Task lifecycle truth

AUTH-* / explicit User authority
= mutation/operation authority

R4 Current Truth Context
= execution-time resolution of mutable facts from their real owners

Project Adapter
= translation/locator boundary

Capability / Tool / Trust / Executor Profiles
= execution eligibility policy

Multica
= operational claim/coordination owner only

Executor
= bounded work performer

Task Record
= actual execution observation

Verification Record
= state-bound verification result

Git / GitHub / source-native systems
= factual authority for state they own
```

The following remain distinct:

```text
Contract ≠ Authority
Capability ≠ Authority
Eligibility ≠ Authority
Claim ≠ Authority
Execution success ≠ Verification PASS
Verification PASS ≠ Task DONE
Task DONE ≠ OUT achieved
Task DONE ≠ MERGED ≠ PUSHED ≠ RELEASED ≠ ARTIFACT_PUBLISHED ≠ DEPLOYED
```

Framework 1.19 does not implement AI-ControlTower runtime, ProjectFramework 2.0 cutover, a Control Plane, state/workflow engine, task database, event store, queue, scheduler, worker daemon, Multica runtime, lease/fencing service, distributed lock, automatic transition engine, model/executor router, executable Project Adapter, MCP router, merge bot, merge queue, verification daemon, CI runner, API server, automatic Task DONE updater, automatic reconciliation worker, Structured Core, Generated Governance, Transaction Mode implementation, or a new authority system.

## 3. PLAN / TASK / VERIFY and R4 Current Truth

Framework 1.19 standardizes three execution-facing modes:

```text
PLAN
TASK
VERIFY
```

### PLAN

PLAN establishes or validates the bounded execution contract. It resolves Plan Contract, Task Contract, Expected IPOCV, declared dependencies, Execution Envelope, required current truth, and verification requirements.

`PLAN complete ≠ Task Ready ≠ execution authority`.

### TASK

TASK performs work only inside the intersection of:

```text
Task Contract
∩ Plan Contract
∩ Execution Envelope
∩ applicable AUTH
∩ current R4 truth
```

Its durable result is represented by Task Record / Actual IPOCV plus source-native artifacts and evidence.

### VERIFY

VERIFY evaluates Task Contract + Expected IPOCV + Task Record + Actual IPOCV + exact candidate identity when applicable + required current truth + verification requirements.

VERIFY MUST NOT rewrite Expected IPOCV or acceptance criteria merely to make execution pass.

### R4 Current Truth Context

Framework 1.19 uses `R4_CTX` / `current_truth_context` for execution-time Current Truth. It MUST NOT be interpreted as a new Risk level. Canonical Project Risk remains exactly `R0–R3`.

Contracts declare which current truth is required; R4 resolves that truth from the applicable canonical/source-native owner at the relevant execution boundary.

```text
Contract declares required truth
        ↓
R4 resolves current truth
        ↓
Ready Gate / TASK / VERIFY consume it
```

R4 is derived context, not another authority and not a permanent copy of mutable state.

## 4. Plan Contract, Task Contract, Execution Envelope, and mandatory IPOCV

### 4.1 Plan Contract

Plan Contract owns execution strategy rather than Task success semantics.

Minimum semantic shape:

```yaml
contract_type: PLAN
contract_version: "1.0"
task_ref: TASK-xxx
intent:
scope:
  included:
  excluded:
required_current_truth:
  sources:
  freshness_requirements:
execution_sequence:
dependency_strategy:
verification_strategy:
rollback_or_recovery:
prohibited_operations:
invalidation_conditions:
```

A bounded/LOW Task MAY embed the Plan Contract in its durable Task artifact. A standalone Plan file is not universally required.

### 4.2 Task Contract

Task Contract owns what must be achieved.

```yaml
contract_type: TASK
contract_version: "1.0"
task_id: TASK-xxx
plan_ref:
intent:
task_type:
acceptance_criteria:
dependencies:
  depends_on:
  blocks:
  parallelizable_with:
execution_envelope:
expected_ipocv:
verification_requirements:
completion_requirements:
integration:
```

Task Contract owns intent, acceptance criteria, declared dependencies, completion requirements, Expected IPOCV, and integration applicability. Plan Contract may reference these semantics but MUST NOT create a competing authoritative copy.

### 4.3 Execution Envelope

Execution Envelope is a nested Task execution constraint. It is not Project Source `ENV-*`, is not a Stable-ID family, and grants no authority.

```yaml
execution_envelope:
  allowed_scope:
  allowed_workspaces:
  allowed_mutation_classes:
  prohibited_effects:
  required_authority_refs:
  current_truth_context: R4_REQUIRED
  concurrency:
    claim_scope:
    parallelism_constraints:
  recovery:
    unknown_result: VERIFY_BEFORE_RETRY
```

The envelope MAY narrow existing authority but can never broaden it.

### 4.4 Mandatory IPOCV

Every Task Contract carries complete Expected IPOCV:

```text
I = Input
P = Process
O = Output
C = Control
V = Verification
```

Every dimension is mandatory. A genuinely inapplicable dimension is represented explicitly as `NOT_APPLICABLE` with a reason; omission is not equivalent to not-applicable.

Mandatory no-inference rules include:

```text
missing field ≠ permission to infer
unknown authority ≠ authorized
unknown dependency ≠ satisfied
available tool ≠ eligible executor
```

### 4.5 Expected vs Actual IPOCV

Expected and Actual remain separate:

```text
Task Contract
└── Expected IPOCV

Task Record
└── Actual IPOCV
```

Comparison result is exactly:

```text
MATCH
ACCEPTED_VARIANCE
MISMATCH
UNKNOWN
```

`ACCEPTED_VARIANCE` requires a governed basis. `MISMATCH` cannot verify. Applicable `UNKNOWN` fails closed.

## 5. Task Record and Verification Record

Task Record captures observed execution rather than rewriting the original contract.

```yaml
record_type: TASK_RECORD
record_version: "1.0"
task_ref:
plan_ref:
task_contract_ref:
execution_ref:
resolved_current_truth:
  context_ref:
  observed_at:
actual_ipocv:
produced_artifacts:
evidence_refs:
candidate_identity:
execution_result:
```

Verification Record is state-bound:

```yaml
record_type: VERIFICATION_RECORD
record_version: "1.0"
task_ref:
plan_ref:
task_record_ref:
verified_candidate:
resolved_current_truth_ref:
acceptance_results:
ipocv_comparison:
control_results:
verification_evidence:
result: PASS | FAIL | UNKNOWN
invalidation_conditions:
```

Verification PASS is evidence for the exact observed state; it is not permanent universal truth.

## 6. Task Ready Gate

Task Ready Gate is a pure fail-closed eligibility evaluation and does not replace existing Task planning readiness vocabulary.

Gate result is exactly:

```text
PASS
FAIL
UNKNOWN
```

PASS requires all applicable conditions:

```text
TASK_PLANNING_READINESS == READY
PLAN_CONTRACT_VALID
TASK_CONTRACT_VALID
EXPECTED_IPOCV_COMPLETE
EXECUTION_ENVELOPE_VALID
DEPENDENCIES_SATISFIED
R4_REQUIRED_TRUTH_RESOLVED
APPLICABLE_AUTHORITY_RESOLVED
REQUIRED_EXECUTOR_CAPABILITY_RESOLVED
SOURCE_OF_TRUTH_OWNERS_RESOLVED
NO_BLOCKING_CONFLICT
```

`UNKNOWN`, materially stale, conflicted, or unresolved mandatory truth cannot be normalized to PASS.

```text
Task Ready Gate PASS
≠ authority grant
≠ claim
≠ execution success
≠ Task DONE
```

## 7. Operational execution state machine

Canonical Task lifecycle remains:

```text
TODO
IN_PROGRESS
DONE
BLOCKED
CANCELLED
```

Framework 1.19 adds a separate operational execution-state domain:

```text
PROPOSED
→ READY_FOR_CLAIM
→ CLAIMED
→ EXECUTING
→ RESULT_RECORDED
→ VERIFYING
→ VERIFIED
→ INTEGRATION_PENDING
→ INTEGRATED
→ CLOSED
```

Conditional/exception states include:

```text
VERIFICATION_FAILED
BLOCKED
CANCELLED
STALE
```

Representative guards:

```text
PROPOSED → READY_FOR_CLAIM
requires Task Ready Gate PASS

READY_FOR_CLAIM → CLAIMED
requires eligible executor + valid coordination claim

CLAIMED → EXECUTING
requires current claim + applicable AUTH + fresh R4

EXECUTING → RESULT_RECORDED
requires Task Record + Actual IPOCV + candidate identity when applicable

RESULT_RECORDED → VERIFYING
requires complete verification inputs

VERIFYING → VERIFIED
requires Verification Record PASS

VERIFIED → INTEGRATION_PENDING
requires integration applicability

INTEGRATION_PENDING → INTEGRATED
requires source-native integration readback + reconciliation PASS

VERIFIED/INTEGRATED → CLOSED
requires applicable completion reconciliation
```

Execution State MUST NOT directly mutate canonical Task lifecycle.

## 8. Multica authority and source-of-truth boundary

Multica owns operational coordination facts only: claim availability, claim holder, claim scope, worker assignment, claim release/expiry/stale observation, and parallel execution coordination.

Multica MUST NOT own or mutate Project intent, Plan Contract, Task Contract, acceptance criteria, AUTH, Risk, Project Source, Task lifecycle, Verification PASS, Git truth, merge/release/deployment truth, or OUT achievement.

A coordination claim is neither Project authority nor a guaranteed distributed lock/fencing mechanism.

There is no newest-timestamp-wins rule. Conflicts resolve by truth domain and canonical owner.

Examples:

```text
Multica CLAIMED + Task Source CANCELLED
→ Task lifecycle CANCELLED wins; claim is stale.

ControlTower INTEGRATION_PENDING + canonical Git proves merged
→ merge fact comes from Git; execution state requires reconciliation.

Task Record says tests ran successfully + Verification Record FAIL
→ execution observation remains true; verification result remains FAIL.
```

## 9. Capability, Executor Profile, Project Adapter, and execution selection

Framework 1.19 reuses existing Agent/Model Capability Profile, Tool/MCP Execution Profile, Trust Profile, and `AUTH-*` semantics.

It adds declarative Executor Profile semantics. An executor profile may state supported PLAN/TASK/VERIFY modes, work classes, capability/tool/trust profile references, execution limits, workspace roles, and coordination support. It is eligibility metadata, not permission.

Supporting VERIFY is not the same as qualifying as an independent verifier.

The Project Adapter maps generic contracts to Project-specific owners and locators. It does not become those owners.

```text
Project Adapter
≠ Project Source
≠ Task Source
≠ Git
≠ GitHub
≠ Runtime Authority
≠ AUTH
```

Selection is deterministic filter-before-rank:

```text
Task Ready Gate PASS
→ execution mode
→ work class
→ mandatory capabilities
→ provider scope
→ tool policy
→ trust policy
→ Execution Envelope
→ risk/side-effect compatibility
→ workspace compatibility
→ independent-review constraints
→ eligible executor set
→ preference ranking
→ selected executor
→ volatile-prerequisite recheck
→ coordination claim
```

An ineligible executor cannot become eligible because it is preferred, cheaper, stronger, recent, or available. No eligible candidate produces `NO_ELIGIBLE_EXECUTOR`; undeclared fallback is not invented.

TASK and VERIFY selection are separate evaluations.

## 10. Exact-SHA verification and candidate identity

For Material Git-backed work, verification binds to exact observed candidate identity:

```yaml
candidate_identity:
  repository:
  commit_sha:
  tree_sha:
  worktree_or_branch_ref:
  observed_at:
```

Canonical verification identity is repository + exact observed commit SHA. Mutable branch names, PR numbers, version labels, or "latest commit" are routing references, not immutable terminal evidence.

VERIFY operates on a frozen candidate. Material change after PASS invalidates affected proof.

```text
Verification PASS(candidate A)
≠ Verification PASS(candidate B)
```

Existing state-bound evidence reuse/selective invalidation semantics remain authoritative.

Task Verification and Framework `RELEASE_FULL` remain different proof domains. A Verification Record may reference exact valid release evidence; it does not clone or redefine that proof.

## 11. Integration eligibility and fresh INTEGRATION_GATE

`VERIFIED` is not sufficient to merge.

Integration eligibility requires:

```text
Verification PASS
exact verified candidate still current
integration applicable
target resolved
exact integration authority valid
Base Freshness valid
required review satisfied
no blocking conflict
fresh INTEGRATION_GATE PASS
```

```text
VERIFIED ≠ INTEGRATION_ELIGIBLE ≠ MERGED
```

Immediately before shared-state mutation, fresh-resolve candidate SHA, target ref/SHA, authority, verification validity, PR/head identity when applicable, Base Freshness, and mergeability/conflicts.

If the mutable target changes after the gate, the gate is stale and must be re-evaluated. That does not automatically require rerunning unchanged-candidate `RELEASE_FULL`.

## 12. Integration strategy and reconciliation

Framework 1.19 recognizes:

```text
FAST_FORWARD_EXACT
MERGE_COMMIT_PRESERVING_CANDIDATE
TRANSFORMING_INTEGRATION
```

For `FAST_FORWARD_EXACT`, canonical result equals the verified candidate.

A merge commit that preserves the candidate retains candidate proof about that candidate, but the canonical resulting state requires Integration Reconciliation.

Squash/rebase/manual conflict resolution/cherry-pick transformations do not automatically inherit candidate verification. Proof reuse requires deterministic exact-equivalence evidence; otherwise the canonical result must be reverified.

A derived Integration Reconciliation record captures verified candidate SHA, integration strategy, target, pre-integration target SHA, resulting SHA, candidate relation, verification reuse/reverification state, source-native evidence, and PASS/FAIL/UNKNOWN result.

Git / the declared canonical Git hosting target remains the source of truth for Git integration facts.

Unknown shared/non-idempotent outcomes use `RESULT_VERIFICATION_REQUIRED`; no blind retry is allowed after an ambiguous push/merge response.

## 13. Task DONE, CLOSED, and post-merge governance reconciliation

Task completion is determined by Task Contract `completion_requirements`.

A local-only bounded Task may become DONE after applicable verification + durable completion commit even when publication is outside its outcome.

An integration-required Task cannot become DONE until required integration/resulting-state criteria are satisfied.

AI-ControlTower/Multica may submit completion evidence but cannot set Task DONE directly.

Execution `CLOSED` is operational lifecycle closure and is not OUT achievement.

Code/content integration and governance reconciliation remain separate. A merged change may truthfully yield:

```text
MERGED
+ RECONCILIATION_REQUIRED
```

when required Root/Project Source reconciliation lacks authority. Workflow continuity never expands authority implicitly.

## 14. Brownfield, Greenfield, and distribution behavior

Framework 1.19 adoption does not retroactively require historical Tasks to acquire reconstructed Plan Contracts, IPOCV, Task Records, Executor Profiles, or Project Adapters.

Projects that do not use AI-ControlTower remain valid ProjectFramework Projects.

Recommended maintained additions are additive starter/contracts around existing `Project-Execution` and template surfaces, including executor/profile and Project Adapter semantics plus Plan/Task/Task Record/Verification Record contract starters. Exact filenames are implementation-plan detail; no new Project Source semantic slot or Stable-ID family is introduced by design.

Unknown Brownfield mappings remain UNKNOWN rather than guessed.

## 15. Required pressure-scenario classes

Implementation verification MUST cover at least:

1. missing mandatory Contract/IPOCV fields cannot be inferred;
2. `NOT_APPLICABLE` requires an explicit reason;
3. R4 context cannot be interpreted as Risk R4;
4. Execution Envelope cannot expand AUTH;
5. Ready Gate UNKNOWN cannot become PASS;
6. execution state cannot directly mutate canonical Task lifecycle;
7. Multica claim cannot grant authority or Task DONE;
8. stale claim recovery inspects durable/source-native effects before reassignment;
9. undeclared Task parallelism is not inferred;
10. Executor selection filters eligibility before preference ranking;
11. no eligible executor does not trigger arbitrary fallback;
12. an executor supporting VERIFY does not automatically satisfy independent review;
13. Project Adapter locates owners but does not become source of truth;
14. conflicting observations reconcile by domain owner rather than recency;
15. Git-backed Verification Record binds an exact candidate SHA;
16. candidate mutation invalidates affected proof;
17. exact unchanged upstream `RELEASE_FULL` evidence remains reusable where contract-valid;
18. fresh `INTEGRATION_GATE` remains mandatory;
19. FAST_FORWARD_EXACT preserves exact candidate identity;
20. merge commit requires canonical-result reconciliation;
21. transforming integration does not silently inherit candidate proof;
22. deterministic exact-equivalence proof may reuse only shown-equivalent proof domains;
23. unknown merge outcome is verified before retry;
24. local Task DONE remains distinct from publication;
25. integration-required completion waits for integration;
26. post-merge reconciliation cannot expand authority;
27. Brownfield Tasks are not silently retrofitted; and
28. AI-ControlTower/Multica runtime is not introduced by the release.

## 16. Completion criteria

TASK-057 implementation is complete only when all of the following are true:

- this written design is explicitly approved;
- an implementation plan is completed;
- pressure scenarios/TDD are established before normative implementation;
- normative Framework contract and maintained starters are implemented;
- Plan/Task/Verify, IPOCV, R4_CTX, Ready Gate/state machine, Multica boundary, Executor/Profile/Adapter, exact-SHA verification, integration reconciliation, Brownfield and non-runtime boundaries are mutually consistent;
- independent review passes where required;
- AFFECTED verification passes;
- one final `RELEASE_FULL` passes on the unchanged final Framework 1.19 candidate;
- state-bound evidence is persisted;
- the Material Git-backed completion commit is freshly observed; and
- canonical Task/Goal lifecycle is reconciled truthfully.

Publication, PR/merge, tag, GitHub Release, Project Source self-host promotion, and consuming-Project upgrades remain separately governed unless exact current authority explicitly includes them.

## 17. Design provenance and review gate

Design Sections 3–6 were consolidated from explicitly approved design text in the 2026-09-14 conversation. Sections 1–2 are conservative consolidation of the previously approved Approach A, AI-ControlTower-support scope, Plan/Task/Verify requirement, R4/source-of-truth boundary, and no-runtime boundary retained in Project conversation context.

This file is the durable written-spec review artifact. No implementation begins until ACTOR-001 explicitly accepts this written specification. After approval, the next process step is implementation planning (`writing-plans`) before mutation of Framework normative surfaces.
