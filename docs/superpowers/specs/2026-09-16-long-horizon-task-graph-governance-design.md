# ProjectFramework Long-Horizon Planning and Task Graph Governance Design

Date: `2026-09-16` (Asia/Bangkok)
Design state: `USER_APPROVED_DIRECTION / WRITTEN_SPEC_PENDING_REVIEW`
Task registration: `NOT_YET_REGISTERED`
Implementation state: `NOT_AUTHORIZED`
Candidate target release: Framework `1.21.0` / Project Source Schema `1.0.0` / release format `3`
Source direction: approved scope interpretation based on the candidate document `ProjectFramework Scope Expansion Candidate — Long-Horizon Planning, Task Dependency Graphs, Just-in-Time Activation, and Continuous Execution Handoff`.

## 1. Goal

Extend ProjectFramework with the minimum generic declarative semantics needed to support long-horizon collections of bounded Tasks as dependency-driven execution plans while preserving the existing separation among planning, authority, runtime execution, verification, integration, and canonical Task completion.

The architectural principle is:

```text
Plan early.
Bind mutable execution truth late.
Execute continuously only through fresh gates.
Verify state-bound results.
Re-plan only where declared dependency/provenance semantics require it.
```

This design does **not** turn ProjectFramework into a scheduler, queue, runtime database, worker daemon, graph traversal engine, orchestration service, or automatic executor.

## 2. Baseline and sequencing constraints

This design is a successor layer, not a rewrite of Framework 1.19 or TASK-058.

Observed baseline at design time:

```text
Framework distribution baseline
= Framework 1.19.0 declarative PLAN/TASK/VERIFY governance support

ProjectFramework self-host baseline
= Framework 1.18.0 pin pending separately governed reconciliation

TASK-058
= registered TODO with Design V3 and reviewed implementation plan
= target Framework 1.20.0 deterministic execution-runtime contract
```

The required sequence is:

```text
Framework 1.19 self-host reconciliation
        ↓
TASK-058 implementation without scope expansion
        ↓
Framework 1.20 self-host reconciliation
        ↓
Register successor long-horizon/graph Task
        ↓
Implement this design through a separately approved implementation plan
```

The two self-host reconciliation steps are separate governed work. They are not silently included in this design's implementation scope.

## 3. Existing ownership that remains authoritative

Framework 1.19 remains authoritative for:

```text
PLAN / TASK / VERIFY
Plan Contract for one bounded Task
Task Contract for Task success semantics
Execution Envelope
Expected IPOCV / Actual IPOCV
Task Record
Verification Record
Task Ready Gate
R4_CTX current-truth resolution
Operational Execution state
Executor Profile / capability-tool-trust filtering
Project Adapter boundary
Multica coordination-only boundary
exact-candidate verification
INTEGRATION_GATE
Integration Reconciliation
Task DONE ownership separation
```

TASK-058 remains authoritative for the successor deterministic execution-runtime layer, including:

```text
Execution / Attempt / Action identity separation
immutable Task/Plan/Envelope semantic fingerprints
runtime_generation + fence_epoch
Runtime Event Journal > Checkpoint/Snapshot
state_version atomic transition semantics
Effect Gateway / Effect Permit
source-native target preconditions
ambiguous-result reconciliation
bounded budgets / wait-wakeup / cancellation semantics
runtime/event-schema version pinning
```

This design MUST compose with those owners and MUST NOT introduce parallel competing copies.

## 4. Scope interpretation matrix

| Proposal | Design decision | Canonical owner/action |
|---|---|---|
| Plan Set / Task Graph | `ADD_OPTIONAL_CONTRACT` | Optional `PLAN_SET` structural contract |
| Dependency satisfaction predicate | `EXTEND_EXISTING_CONTRACT` | Successor Task Contract version owns predicate |
| Derived planning readiness | `CLARIFICATION_ONLY` | Derived eligibility labels, never Task lifecycle |
| Activation binding | `COMPOSE_WITH_TASK058` | Extend execution identity/binding semantics; no duplicate record |
| Contract revision invalidation | `EXTEND_TASK058_FINGERPRINT_RULES` | Add Plan Set/dependency revision effects |
| Graph-level re-plan propagation | `ADD_DECLARATIVE_FACTS` | Task dependency consumption/invalidation declarations |
| Continuous execution handoff | `CLARIFICATION_ONLY` | Fresh dependency + Task Ready + activation gates |
| Verifier readiness | `EXTEND_READY_GATE_APPLICABILITY` | Task verification requirement controls applicability |
| Executor requirement vs runtime binding | `CLARIFICATION_PLUS_CONTRACT_FIELD` | Requirement in Task Contract; runtime instance binds later |
| Long-horizon current truth | `ALREADY_COVERED_PLUS_CLARIFICATION` | R4_CTX remains execution-time owner |
| Backlog membership vs runtime queue | `CLARIFICATION_ONLY / RUNTIME_OWNER` | Framework defines distinction; runtime owns queues |

## 5. Plan Set Contract

### 5.1 Purpose

Introduce an optional structural contract named `PLAN_SET`.

A Plan Set represents:

```text
long-horizon objective
+ bounded Task membership
+ dependency topology
+ exact planning revision
+ graph constraints
+ graph-level invalidation policy
```

It does not own Task intent, acceptance criteria, Expected IPOCV, completion requirements, authority, verification PASS, integration truth, or Task DONE.

A Project executing only one bounded Task does not require a Plan Set.

### 5.2 Version and identity

Initial contract version:

```yaml
contract_type: PLAN_SET
contract_version: "1.0"
```

`plan_set_ref` is a contract reference, not a new Project Source Stable-ID family.

Every material Plan Set change produces a distinct revision/fingerprint. Mutable-path identity alone is insufficient for activation.

### 5.3 Canonical conceptual shape

```yaml
contract_type: PLAN_SET
contract_version: "1.0"

plan_set_ref: "<durable reference>"
project_ref: "<Project identity>"
objective: "<long-horizon outcome>"

planning_horizon:
  from: "<first bounded milestone/package>"
  through: "<last bounded milestone/package>"

members:
  - task_ref: "TASK-A"
    task_contract_ref: "<exact planned Task Contract reference>"
    task_contract_fingerprint: "<immutable semantic fingerprint>"

edges:
  - from: "TASK-A"
    to: "TASK-B"
    downstream_dependency_key: "dep-a-verification"

graph_constraints:
  cycles: DISALLOWED
  undeclared_dependency_inference: DISALLOWED
  missing_member_reference: FAIL_CLOSED

current_truth_policy:
  mutable_truth_resolution: RESOLVE_AT_ACTIVATION

invalidation_policy:
  affected_descendants: REVALIDATE_BY_DECLARED_CONSUMPTION
  unrelated_branches: PRESERVE_IF_VALID
```

### 5.4 No competing dependency owner

Plan Set `edges` are a structural projection of dependency requirements owned by the downstream Task Contract.

For each graph edge:

```text
Plan Set edge
must resolve to
an exact downstream Task Contract dependency key
```

A Plan Set edge that conflicts with the Task Contract is invalid. The graph MUST NOT invent, weaken, or strengthen a Task dependency silently.

External dependencies outside Plan Set membership are allowed only when explicitly declared by the Task Contract and represented as an external graph boundary. Presence outside the Plan Set is not itself an error; undeclared inference is.

## 6. Successor Task Contract dependency semantics

### 6.1 Versioning decision

Existing Task Contract `1.0` remains valid for existing and historical work.

Predicate-aware graph participation uses successor:

```yaml
contract_type: TASK
contract_version: "1.1"
```

No existing `1.0` Task is silently converted to `1.1`, and historical dependency predicates are never reconstructed from outcome history.

### 6.2 Structured required dependencies

Task Contract `1.1` uses structured dependency requirements:

```yaml
dependencies:
  required:
    - key: "dep-b2r-verification"
      task_ref: "TASK-B2R"
      satisfaction:
        predicate: VERIFICATION_PASS
        freshness: CURRENT_REQUIRED
      consumes:
        - kind: UPSTREAM_RESULT
          ref: "<declared artifact/state selector>"
      invalidation:
        on_material_change: REVALIDATE
  blocks:
    - "TASK-B4"
  parallelizable_with:
    - "TASK-C1"
```

`key` is local to the Task Contract revision. It is not a new Stable-ID family.

### 6.3 Initial governed predicate set

The initial predicate set is:

```text
TASK_DONE
VERIFICATION_PASS
INTEGRATED
ARTIFACT_AVAILABLE
CANONICAL_STATE_PRESENT
CUSTOM_GOVERNED_PREDICATE
```

Semantics:

- `TASK_DONE` — canonical Task owner proves the upstream Task lifecycle is `DONE`.
- `VERIFICATION_PASS` — a current state-bound Verification Record proves PASS for the exact applicable candidate/contracts.
- `INTEGRATED` — source-native integration fact plus applicable Integration Reconciliation proves the required resulting state.
- `ARTIFACT_AVAILABLE` — declared source-native owner proves the exact required artifact exists with required identity/integrity.
- `CANONICAL_STATE_PRESENT` — the declared canonical/source-native owner proves an explicitly declared state predicate.
- `CUSTOM_GOVERNED_PREDICATE` — allowed only when the Task Contract names the predicate owner, evaluation rule, evidence type, and freshness rule. Free-text runtime inference is prohibited.

`RESULT_ACCEPTED` is **not** introduced by this version because Framework 1.19/TASK-058 do not currently define a canonical owner or lifecycle truth named Result Acceptance. Adding that predicate later requires an explicit owner/meaning decision rather than name reuse.

### 6.4 Dependency proof rules

A satisfied dependency must be reconstructable from governed evidence.

```text
declared dependency
+ exact predicate
+ exact upstream identity
+ current/non-stale evidence
+ declared evidence owner
= dependency proof
```

Rules:

```text
UNKNOWN != satisfied
STALE != satisfied
upstream record existence != predicate satisfaction
mutable branch/path label != immutable proof
historical PASS invalidated by candidate/contract change != current PASS
```

Dependency satisfaction is eligibility evidence only. It never creates AUTH.

## 7. Derived planning readiness

Long-horizon planning uses a derived, non-canonical readiness vocabulary:

```text
PLANNED
BLOCKED_BY_DEPENDENCY
ACTIVATION_CANDIDATE
STALE
REPLAN_REQUIRED
UNKNOWN
```

These labels are not a replacement for canonical Task lifecycle and are not Operational Execution states.

### 7.1 Meaning

- `PLANNED` — bounded Task/Plan contracts exist but dependency eligibility has not produced an activation candidate.
- `BLOCKED_BY_DEPENDENCY` — one or more required predicates are not currently satisfied.
- `ACTIVATION_CANDIDATE` — declared dependencies are currently satisfied and structural graph/contract references remain valid enough to attempt the normal Task Ready Gate.
- `STALE` — previously usable planning/dependency evidence is no longer current.
- `REPLAN_REQUIRED` — a declared invalidation condition proves the current bounded plan is insufficient or semantically invalid.
- `UNKNOWN` — required planning/dependency facts cannot be resolved deterministically.

Canonical invariant:

```text
ACTIVATION_CANDIDATE
!= Task Ready Gate PASS
!= AUTH
!= claim
!= execution
```

## 8. Activation binding and TASK-058 composition

### 8.1 No new competing Execution State Binding record

This design does not introduce a second canonical execution-binding record.

Long-horizon activation extends the TASK-058 execution identity/fingerprint composition with optional Plan Set identity and dependency proof references.

Conceptually:

```text
Plan Set exact fingerprint
+ Task Contract exact fingerprint
+ Plan Contract exact fingerprint
+ Execution Envelope exact fingerprint
+ dependency proofs
+ fresh R4_CTX
+ fresh applicable AUTH evaluation
+ Executor requirement
+ selected Executor runtime binding
+ applicable verifier readiness proof
+ Project / repository / workspace identity
+ TASK-058 runtime generation / fence / claim semantics
= governed activation evidence
```

A conforming runtime may materialize this in its runtime store/journal under TASK-058 rules. ProjectFramework does not mandate a new database table, event-store product, or standalone `ACTIVATION_BINDING` record type.

### 8.2 Execution identity extension

When Plan Set is applicable, runtime execution identity MUST be able to reconstruct:

```yaml
planning_binding:
  plan_set_ref: "<exact ref>"
  plan_set_fingerprint: "<exact fingerprint>"
  task_contract_fingerprint: "<exact fingerprint>"
  plan_contract_fingerprint: "<exact fingerprint>"
  execution_envelope_fingerprint: "<exact fingerprint>"
  dependency_proof_refs:
    - "<governed proof ref>"
```

No field above grants authority.

## 9. Plan early, bind runtime instances late

Long-horizon contracts describe requirements, not transient runtime process identities.

### 9.1 Executor requirement

Task Contract `1.1` may declare:

```yaml
executor_requirement:
  mode: TASK
  work_class: ENGINEERING
  profile_ref: "LOCAL_LLM_ENGINEER"
  required_capabilities:
    - CODING
  required_workspace_roles:
    - EDIT
    - BUILD
    - TEST
```

Activation-time runtime binding remains separate:

```text
Executor requirement != selected Executor
Executor Profile != runtime binding
eligibility != authority
```

### 9.2 Verifier requirement

Task Contract `1.1` may declare:

```yaml
verification_requirements:
  independent_review: REQUIRED
  activation_readiness: ELIGIBLE_INSTANCE_REQUIRED
  verifier_requirement:
    capability: REVIEW
    qualification: INDEPENDENT
```

`activation_readiness` is exactly one of:

```text
QUALIFIED_PATH_REQUIRED
ELIGIBLE_INSTANCE_REQUIRED
```

- `QUALIFIED_PATH_REQUIRED` requires a valid governed independent-verification path/policy to exist before activation; the exact verifier instance may bind later.
- `ELIGIBLE_INSTANCE_REQUIRED` additionally requires at least one currently eligible independent verifier instance before Task Ready can PASS.

The Task Ready Gate gains an applicability-driven condition equivalent to:

```text
REQUIRED_VERIFICATION_PATH_RESOLVED
```

and, when explicitly required:

```text
REQUIRED_VERIFIER_AVAILABILITY_RESOLVED
```

A missing required independent verifier cannot be replaced by self-verification or an unqualified reviewer.

## 10. Long-horizon current-truth policy

Framework 1.19 R4_CTX remains authoritative.

A Plan Set or Task Contract may record planning-time provenance, but planning-time mutable values do not become execution truth.

Canonical rule:

```text
Planning Baseline != Execution Current Truth
```

For mutable applicable facts:

```text
resolution policy = RESOLVE_AT_ACTIVATION
```

Fresh resolution includes, as applicable:

```text
Project Source
Git target / exact SHA
AUTH
workspace identity
Executor eligibility
Verifier eligibility
runtime generation/fence/claim state
source-native target preconditions
```

A planning baseline may be retained for provenance and invalidation comparison only.

## 11. Revision invalidation and no silent hot-swap

### 11.1 Bound execution remains bound

Once execution is activated, it remains bound to its exact Plan Set/Task/Plan/Envelope fingerprints.

Publishing a newer revision never causes an active execution to silently adopt it.

```text
execution bound to T1
T2 published
-> execution evidence remains T1-bound
-> verification evaluates T1-bound success semantics
-> T1 result does not automatically satisfy T2
```

### 11.2 Material revision classes

Revalidation is required when material change affects any of:

```text
Plan Set membership/topology
Plan Set graph revision
Task Contract acceptance/completion semantics
Task dependency predicate
Expected IPOCV
Plan invalidation conditions
Execution Envelope narrowing
required verification policy
consumed upstream artifact/state identity
```

TASK-058's existing fingerprint-change rule remains the execution-level enforcement basis.

### 11.3 Derived invalidation outcomes

Declarative evaluation may produce:

```text
NO_ACTION
REVALIDATE_READINESS
REVALIDATE_CONTRACT
STALE
REPLAN_REQUIRED
ACTIVE_EXECUTION_STALE
```

`ACTIVE_EXECUTION_STALE` does not itself grant cancellation authority. Cancellation/request semantics remain governed by TASK-058 and applicable authority.

### 11.4 Plan Set removal

If a newer Plan Set revision removes a Task while an older execution exists:

```text
older execution history remains valid for its bound revision
new graph does not erase the old execution
old result cannot unlock new-graph descendants unless explicitly revalidated
```

## 12. Affected-subtree re-plan semantics

ProjectFramework defines the facts; runtime performs traversal.

A Task Contract dependency may declare which upstream outputs/states it consumes. Material upstream change propagates only through declared consumption/dependency relations.

Rules:

```text
no declared consumption/dependency -> no inferred invalidation edge
material change to consumed input -> apply declared invalidation policy
unrelated branch -> preserve if its own proofs/contracts remain current
UNKNOWN propagation relevance -> fail closed for affected activation
```

The runtime may derive descendants requiring:

```text
readiness re-evaluation
contract revalidation
STALE marking
REPLAN_REQUIRED
active-execution stale handling
```

The Framework does not implement graph traversal or queue mutation.

## 13. Continuous execution handoff

Planner re-entry is not required between every successfully governed Task.

A downstream Task may proceed without Planner interaction only when this complete chain holds:

```text
upstream required predicate freshly satisfied
-> downstream Plan Set/Task/Plan references current
-> planning readiness = ACTIVATION_CANDIDATE
-> fresh Task Ready Gate PASS
-> required executor/verifier readiness resolves
-> new execution identity/binding established
-> new coordination/ownership state established
-> execution may begin
```

No authority, R4 observation, claim, fence, or verifier eligibility carries forward merely because the same workflow/worker handled the previous Task.

### 13.1 Planner re-entry reasons

Planner re-entry is required for semantic planning failures including:

```text
REPLAN_REQUIRED
PLAN_SCOPE_INSUFFICIENT
DEPENDENCY_SEMANTICS_CHANGED
CONTRACT_INVALIDATED
CURRENT_TRUTH_INVALIDATES_PLAN
ARCHITECTURE_GAP
ACCEPTANCE_CRITERIA_CHANGE
```

`NO_ELIGIBLE_EXECUTOR` or `NO_ELIGIBLE_VERIFIER` does not automatically mean re-plan when the cause is temporary runtime capacity. It becomes a planning issue only when the declared execution/verification strategy itself must change.

Implementation failure with a still-valid Plan may use governed retry/recovery without re-planning.

## 14. Backlog membership versus runtime queues

Canonical distinctions:

```text
Plan Set membership != runtime Ready Queue membership
Plan Set membership != execution authority
ACTIVATION_CANDIDATE != queue dispatch
queue priority != authority
```

ProjectFramework may define membership, predicates, evidence, readiness, and activation invariants.

AI-ControlTower or another runtime owns:

```text
Master Execution Backlog persistence
runtime graph storage/projection
dependency traversal
Ready Queue
Verify Queue
Replan Queue
scheduler
dispatch
retry timing
resource fairness/capacity
worker process management
runtime ordering
```

## 15. Runtime and ProjectFramework boundary

The following remain explicit non-Framework implementation scope:

```text
persistent task/graph database
graph traversal engine
queue implementation
event bus implementation
scheduler/worker daemon
automatic activation engine
automatic executor selection service
node health service
lease heartbeat service
fencing-token generator/enforcer
runtime CAS store
automatic verification daemon
automatic merge bot
automatic Task-DONE updater
deployment engine
```

Framework defines protocol correctness and interoperability properties only.

## 16. Brownfield and backward compatibility

Requirements:

1. Framework 1.19/1.20 historical Task/Plan contracts remain valid under the versions that created them.
2. Task Contract `1.0` is not silently reinterpreted as predicate-aware `1.1`.
3. Historical Tasks receive no invented Plan Set, graph revision, dependency predicate, dependency proof, activation binding, or propagation metadata.
4. Unknown historical mapping remains `UNKNOWN`.
5. Projects not using long-horizon planning remain valid.
6. Plan Contract `1.0` for one bounded Task remains valid.
7. Task Record and Verification Record remain unchanged unless implementation discovers a concrete serialization need that cannot be satisfied through existing execution references.
8. Plan Set introduces no Project Source semantic slot and no Stable-ID family.
9. Project Source Schema remains `1.0.0` unless implementation proves a breaking Project Source requirement; in that event release classification must be revisited rather than forcing `1.21.0`.
10. Existing canonical Task lifecycle remains exactly `TODO | IN_PROGRESS | DONE | BLOCKED | CANCELLED`.

## 17. Candidate maintained Framework surfaces

If this design is implemented, expected affected surfaces are:

```text
Framework-Source/references/core-governance-rules.md
new successor governance amendment
Framework-Source/templates/project-execution/task-contract.md
new Framework-Source/templates/project-execution/plan-set-contract.md
Framework-Source/templates/project-execution/plan-contract.md (clarification only if required)
Framework-Source/templates/project-execution/README.md
Framework-Source/SKILL.md
Framework-Source/MIGRATION-NOTES.md
README.md
Framework-Source/tests/pressure-scenarios.md
release metadata / maintained Framework stamps
```

TASK-058 runtime starters may require additive cross-reference updates, but they MUST NOT be duplicated or replaced.

## 18. Pressure-test contract

The implementation plan MUST begin RED-first with graph/long-horizon scenarios covering all candidate source scenarios.

If TASK-058 completes with its planned scenario range `557–602` unchanged, this successor allocates `603–642` to the forty long-horizon scenarios below. If TASK-058's canonical final range changes before successor implementation, use the immediately following contiguous range while preserving this scenario order and all forty semantic classes.

Required classes:

```text
1  whole B→F roadmap planned before first execution
2  parallel branch proceeds while another branch is blocked
3  cycle introduced
4  dependency points outside Plan Set
5  required dependency evidence UNKNOWN
6  upstream Verification PASS later invalidated
7  graph revision changes before downstream activation
8  graph revision changes during active execution
9  Task removed from newer Plan Set while older execution exists
10 Planner unavailable after graph materialization
11 planning-baseline Git SHA differs harmlessly at activation
12 planning-baseline change materially invalidates plan
13 Task Contract changes before activation
14 Task Contract changes after claim
15 AUTH valid at planning but revoked before activation
16 AUTH revoked during execution
17 executor requirement valid but no runtime binding
18 runtime binding exists but workspace identity mismatches
19 eligible Executor but required independent Verifier unavailable
20 Verifier available but not independently qualified
21 Task A verifies and Task B runs without Planner re-entry
22 Task B requires integration while A is only locally verified
23 Task B receives a new ownership/fence identity after Task A
24 stale Task-A worker attempts write during Task B
25 Task B discovers out-of-scope work and returns REPLAN_REQUIRED
26 implementation fails while Plan remains sufficient
27 unknown result after timeout does not blind-retry
28 affected subtree replans while unrelated work continues
29 candidate changes after Verification PASS
30 downstream VERIFICATION_PASS proof becomes STALE
31 downstream requires TASK_DONE while upstream only VERIFIED
32 downstream requires INTEGRATED while upstream unmerged
33 transforming integration requires re-verification/equivalence proof
34 Verifier attempts to rewrite Expected IPOCV
35 Fleet recommendation does not create authority
36 cross-project impact does not infer cross-project execution authority
37 two Projects contend for one Executor
38 runtime priority changes ordering but not authority
39 blocked Task in one Project does not block unrelated ready work
40 campaign/portfolio planning never replaces Project-local governance
```

Each scenario must define observable Pass/Fail criteria and fail closed on ambiguity.

## 19. Implementation-plan decomposition after written-spec approval

After this written spec is explicitly approved and the successor Task is registered, create one implementation plan with these reviewer-sized work units:

```text
1. RED graph/long-horizon pressure scenarios
2. Plan Set + Task Contract 1.1 dependency semantics
3. Activation binding + revision invalidation + verifier/executor readiness
4. Re-plan propagation + continuous handoff rules
5. Templates / migration / Brownfield compatibility
6. Structural GREEN / AFFECTED / independent review / release evidence
```

Do not split proposals A–K into eleven unrelated implementation plans; that would fragment ownership and encourage duplicate contracts.

## 20. Release and verification strategy

Candidate classification is:

```text
BACKWARD_COMPATIBLE_ADDITIVE_GRAPH_GOVERNANCE
```

Target Framework release is `1.21.0` if the implementation remains additive and Project Source Schema remains `1.0.0`.

Verification must include:

```text
RED scenario proof before normative implementation
structural contract checks
Task Contract 1.0 backward-compatibility checks
Task Contract 1.1 deterministic predicate checks
Plan Set graph validation checks
activation/revision-binding checks
Brownfield no-invention checks
AFFECTED verification
independent review
one final RELEASE_FULL on the unchanged frozen candidate
exact candidate/tree evidence
```

Any candidate-invalidating change after final verification establishes a new candidate and invalidates prior final proof.

Push, PR, merge, tag, GitHub Release, self-host promotion, consumer upgrade, and AI-ControlTower runtime implementation remain separate authority/gate domains.

## 21. Canonical invariants

If accepted, the successor Framework layer SHALL preserve these principles:

1. `Plan early; bind mutable execution truth late.`
2. `Task graph structure != authority.`
3. `Declared dependency != satisfied dependency.`
4. `Dependency satisfaction requires explicit governed predicate + current evidence.`
5. `Plan Set does not own Task success semantics.`
6. `Executor requirement != selected Executor runtime instance.`
7. `Verifier requirement != verifier runtime binding.`
8. `Activation is bound to exact applicable contract/graph revisions.`
9. `Active execution never silently hot-swaps to a newer mutable contract revision.`
10. `Planning Baseline != Execution Current Truth.`
11. `ACTIVATION_CANDIDATE != Task Ready Gate PASS.`
12. `Task Ready Gate PASS != AUTH.`
13. `Claim != Lease != Fence != AUTH.`
14. `Verification PASS != Task DONE.`
15. `Backlog membership != queue membership.`
16. `Queue ordering != authority.`
17. `Continuous handoff requires fresh gates for every Task.`
18. `Re-plan propagation follows declared dependency/consumption semantics; runtime does not guess.`
19. `UNKNOWN mandatory dependency/authority/current-truth/verification facts fail closed.`
20. `Historical/Brownfield facts are never invented.`
21. `ProjectFramework defines protocol; runtime implements scheduling/orchestration.`

## 22. Non-goals

This design does not authorize or specify implementation of:

```text
AI-ControlTower runtime service
Multica runtime
scheduler
queue service
background worker
persistent task database
graph database
event store
executor daemon
model/router service
node health monitor
distributed lock service
lease renewal daemon
fencing service
automatic Plan generation
automatic authorization
automatic merge
automatic Task DONE mutation
deployment automation
Memory rebuilding/Fleet runtime
```

It also does not revive the cancelled ProjectFramework 2.0 / Control Plane line.

## 23. Acceptance criteria for this design

This written design is ready for implementation planning only when the reviewer explicitly confirms that:

1. successor scope remains separate from TASK-058;
2. Plan Set is optional and structural only;
3. Task Contract owns explicit dependency predicates;
4. Task Contract `1.0` is preserved and predicate-aware semantics use successor `1.1`;
5. `RESULT_ACCEPTED` is intentionally not introduced without a canonical owner;
6. activation composes with TASK-058 execution identity/fingerprints rather than creating a duplicate binding record;
7. graph revision changes cannot silently hot-swap active execution;
8. re-plan propagation depends on declared consumption/dependency facts;
9. continuous execution requires a fresh Task Ready/authority/runtime binding per Task;
10. verifier readiness is applicability-driven and cannot be silently downgraded;
11. R4_CTX remains the mutable current-truth mechanism;
12. runtime queues/scheduler/traversal remain outside ProjectFramework;
13. no new Project Source slot or Stable-ID family is introduced;
14. Brownfield no-invention behavior is preserved;
15. implementation planning does not begin before explicit written-spec approval.

## 24. Review gate

Current state after this document is committed:

```text
architecture direction = USER_APPROVED
written spec = PENDING_EXPLICIT_USER_REVIEW
successor Task registration = NOT_YET_AUTHORIZED
implementation plan = NOT_YET_AUTHORIZED
implementation = NOT_AUTHORIZED
```

The next governed step is explicit user review/approval of this written spec. Only after that approval should the successor Task be registered and the detailed implementation plan be written.
