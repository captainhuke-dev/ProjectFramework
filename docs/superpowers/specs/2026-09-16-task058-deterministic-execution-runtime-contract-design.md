# TASK-058 — ProjectFramework 1.20 Deterministic Execution Runtime Contract Design

Date: `2026-09-16` (Asia/Bangkok)
Design state: `DESIGN_V3_USER_APPROVED / FROZEN / WRITTEN_SPEC_APPROVED`
Task: `TASK-058`
Depends on: `TASK-057`
Target release: Framework `1.20.0` / Project Source Schema `1.0.0` / release format `3`

## 1. Goal and design lineage

TASK-058 extends the Framework 1.19 AI-ControlTower Governance Support Layer with a deterministic **execution-runtime contract**. Framework 1.19 defines declarative PLAN/TASK/VERIFY contracts, R4 current truth, Task Ready Gate, operational execution state, source-owner reconciliation, exact-candidate verification, and executor/tool/trust eligibility while intentionally shipping no runtime. TASK-058 defines the additional protocol semantics required for a future AI-ControlTower runtime to enforce those contracts across long-running autonomous work without transferring Project authority to the runtime or to an LLM/RLM executor.

The design was developed through three adversarial RolePlay rounds and frozen as Design V3 after explicit user approval. The resulting architectural principle is:

```text
ProjectFramework defines the law.
AI-ControlTower owns deterministic execution-control state.
The Effect Gateway is the only authorized consequence boundary for mediated Material Effects.
LLM/RLM executors propose work but do not own authority, credentials, runtime state, or external side effects.
```

TASK-058 remains **governance/protocol design and Framework documentation only**. It does not implement the future AI-ControlTower runtime.

## 2. Design objectives

The runtime contract MUST make the following statements operationally meaningful rather than prompt-dependent:

```text
Task lifetime != model-turn lifetime
Task lifetime != chat lifetime
Task lifetime != MCP connection lifetime
Worker lifetime != execution lifetime
Execution lifetime != canonical Task lifecycle
Model proposal != runtime decision
Runtime decision != authority
Claim != lease != fence != authority
Verification PASS != Task DONE
```

The contract MUST allow a conforming runtime to:

1. survive model-turn, worker, process, MCP, and host interruption without falsely terminating the Task;
2. resume from durable current execution state instead of model memory;
3. prevent stale or reassigned workers from causing new governed effects;
4. prevent blind duplicate side effects after ambiguous external results;
5. validate authority/current truth/target state as close as possible to effect dispatch;
6. keep Task, Execution, Attempt, and Action/Effect truth domains separate;
7. bound autonomous work by durable budgets, retry policy, and wake/block semantics;
8. preserve source-native systems as factual authority for the state they own;
9. support GPT, Claude, Codex, Local LLM, RLM, Human, or future executors without binding the Framework protocol to one model/provider/language;
10. fail closed without turning fail-closed semantics into infinite retry loops.

## 3. Authority and ownership model

TASK-057 authority separation remains unchanged:

```text
ProjectFramework
= governance/protocol semantics

Project Source
= canonical Project governance truth

Durable Task Source
= canonical Task lifecycle truth

AUTH-* / explicit User authority
= mutation/operation authority

R4_CTX
= execution-time current-truth resolution from canonical/source-native owners

Multica
= claim/coordination owner only

Executor
= bounded performer / proposal producer

Task Record
= observed execution result

Verification Record
= state-bound verification result

Git / GitHub / source-native systems
= factual authority for state they own
```

TASK-058 adds these runtime-owned domains:

```text
AI-ControlTower Runtime Store
= execution-control facts only

Runtime Event Journal
= canonical runtime execution observation within the runtime domain

Checkpoint / Snapshot
= derived recovery accelerator, never stronger than the Runtime Event Journal

Effect Gateway
= governed Material-Effect mediation boundary

Effect Permit
= short-lived, single-use dispatch eligibility proof; never AUTH
```

The runtime MUST NOT become owner of Project intent, Requirements, Decisions, Risk, Project Source, canonical Task lifecycle, AUTH, Verification PASS, Git truth, deployment truth, release truth, or OUT achievement.

## 4. Four lifecycle domains

The Framework MUST keep four lifecycle domains separate.

### 4.1 Canonical Task lifecycle

Unchanged:

```text
TODO | IN_PROGRESS | DONE | BLOCKED | CANCELLED
```

Only the canonical Task owner may mutate this lifecycle under existing governance.

### 4.2 Operational Execution state

TASK-057 remains authoritative for the execution-workflow domain:

```text
PROPOSED
-> READY_FOR_CLAIM
-> CLAIMED
-> EXECUTING
-> RESULT_RECORDED
-> VERIFYING
-> VERIFIED
-> INTEGRATION_PENDING
-> INTEGRATED
-> CLOSED
```

with applicable exception states such as `VERIFICATION_FAILED | BLOCKED | CANCELLED | STALE`.

### 4.3 Execution Attempt state

TASK-058 adds the lifecycle of one worker attempt:

```text
CREATED
-> RUNNABLE
-> RUNNING
-> WAITING
-> RECONCILING
-> TERMINATED
```

Exceptional outcomes include:

```text
LOST | BLOCKED | CANCEL_REQUESTED
```

An Attempt ending or being lost MUST NOT by itself close the Operational Execution or canonical Task.

### 4.4 Action / Effect state

Each independently reconcilable Material Effect has its own lifecycle:

```text
PROPOSED
-> PREPARED
-> PERMITTED
-> DISPATCH_INTENT_RECORDED
-> DISPATCHED
-> ACKNOWLEDGED
-> RECONCILING
-> APPLIED | NOT_APPLIED | AMBIGUOUS | REJECTED
```

`ACKNOWLEDGED` is transport/protocol observation only and MUST NOT be treated as resulting-state proof when the source-native system requires readback/reconciliation.

## 5. Identity model

A runtime MUST use durable identities that survive process/model replacement.

Minimum conceptual hierarchy:

```text
Task
  `- Execution
       |- Attempt 1
       |- Attempt 2
       `- Attempt N
            `- Action / Effect records
```

Minimum fields are:

```yaml
execution_identity:
  task_ref: "TASK-xxx"
  execution_id: "<durable runtime execution id>"
  runtime_contract_version: "1.0"
  event_schema_version: "1.0"
  task_contract_ref: "<reference>"
  task_contract_fingerprint: "<immutable semantic fingerprint>"
  plan_contract_fingerprint: "<fingerprint when applicable>"
  execution_envelope_fingerprint: "<fingerprint>"

attempt_identity:
  execution_id: "<execution id>"
  attempt_id: "<attempt id>"
  executor_ref: "<selected executor>"
  claim_ref: "<coordination claim>"
  runtime_generation: "<control generation>"
  fence_epoch: "<monotonic epoch within generation>"
```

Task Contract, Plan Contract, and Execution Envelope semantic mutation MUST be detectable. A materially changed pinned contract invalidates the active execution or requires governed replanning/revalidation; the runtime MUST NOT silently hot-swap success semantics into an active execution.

## 6. Deterministic Supervisor

The deterministic Supervisor owns runtime state transitions and scheduling decisions. An executor may propose actions or report observations but cannot self-promote runtime state.

Conceptual control loop:

```text
load durable execution state
-> resolve/revalidate applicable prerequisites
-> select runnable Attempt
-> obtain model/executor proposal
-> validate proposal against contract/envelope/budget/policy
-> prepare bounded action
-> mediate Material Effect through Effect Gateway when applicable
-> persist result / reconcile source-native effect
-> checkpoint derived state
-> continue until governed terminal condition
```

The end of an LLM turn MUST NOT be interpreted as completion. If an execution remains runnable and non-terminal, the Supervisor may schedule another reasoning step subject to authority, budgets, current truth, and wait/block policy.

## 7. Effect-Surface Closure and executor confinement

The Effect Gateway is an enforcement boundary only when governed effect paths cannot bypass it.

For every Material Task, the conforming runtime MUST inventory effect-capable surfaces available to the executor, including where applicable:

```text
MCP/tool calls
shell/process execution
network egress
Git/SSH credentials
cloud credentials
filesystem mounts
Docker/container sockets
database connections
external service SDKs
child processes / recursive agents
```

Every governed Material Effect path MUST be either:

```text
MEDIATED_BY_EFFECT_GATEWAY
or
EXPLICITLY_PROHIBITED / CONFINED
```

An executor that retains an uncontrolled path capable of the same governed mutation MUST NOT be classified as autonomously eligible for that Material Effect class merely because policy says it should use the Gateway.

ProjectFramework does not mandate Docker, Kubernetes, a specific sandbox, a particular OS security primitive, or a specific network product. It mandates the **effect-surface-closure property**. A future implementation may realize that property through sandboxing, network policy, credential brokering, restricted shells, capability isolation, or another mechanism with equivalent enforcement semantics.

For mediated Material Effects, raw mutation credentials SHOULD reside at or below the trusted Effect Gateway boundary rather than inside model/RLM workspaces. Credential possession by an unconstrained executor that can bypass the Gateway is an architecture violation for that mediated effect class.

## 8. Effect Gateway

A Material Effect MUST transit the Effect Gateway when the applicable runtime profile declares that effect mediated.

The Gateway validates at least:

```text
current Operational Execution eligibility
current Attempt identity
current control generation + fence
Task/Plan/Envelope fingerprint validity
current applicable AUTH
required R4 current truth
Tool/Capability/Trust eligibility
Target identity + target preconditions
Effect semantics / idempotency / reconciliation class
remaining budget / retry policy
Effect Permit validity
```

The Gateway does not create authority. It enforces the intersection of already valid authority and policy at the consequence boundary.

```text
Gateway eligibility != AUTH
Effect Permit != AUTH
Tool availability != Gateway eligibility
```

## 9. Just-in-Time Effect Permit

For every Gateway-mediated Material Effect, a conforming runtime MUST mint a short-lived Effect Permit only after fresh validation at the effect boundary.

Minimum semantic shape:

```yaml
effect_permit:
  permit_id: "<unique id>"
  execution_id: "<execution id>"
  attempt_id: "<attempt id>"
  action_id: "<action id>"
  action_hash: "<canonical action fingerprint>"
  target_ref: "<exact governed target>"
  tool_ref: "<eligible effect tool>"
  runtime_generation: "<generation>"
  fence_epoch: "<epoch>"
  task_contract_fingerprint: "<fingerprint>"
  execution_envelope_fingerprint: "<fingerprint>"
  authority_ref: "<AUTH-* or explicit authority ref>"
  r4_context_ref: "<fresh current truth ref>"
  target_precondition_ref: "<precondition>"
  issued_at: "<runtime-authoritative time>"
  expires_at: "<short validity boundary>"
  max_uses: 1
```

Permit properties:

```text
single-use
non-transferable
attempt-bound
action-bound
action-hash-bound
target-bound
tool-bound
generation/fence-bound
contract/envelope-bound
short-lived
```

The transition `PERMIT_ACTIVE -> PERMIT_CONSUMED` MUST be atomic/compare-and-set equivalent. Reuse, transfer, action mismatch, target mismatch, stale generation, stale fence, or expiry produces rejection rather than fallback inference.

`PERMIT_CONSUMED` proves only that dispatch eligibility was consumed; it does not prove that the external effect was applied.

## 10. Target preconditions and TOCTOU control

A model may reason over state that changes before dispatch. Therefore Material Effects MUST declare source-native target preconditions whenever the target supports them. When a target does not provide a usable precondition primitive, the effect policy MUST record that limitation explicitly and use the applicable reconciliation/fail-closed strategy rather than silently assuming target freshness.

Examples include:

```text
Git exact ref/SHA
ETag / If-Match
resource_version / generation
row version
object hash
compare-and-set token
immutable candidate identity
```

A stale precondition yields `PRECONDITION_CONFLICT` or equivalent fail-closed result and requires refresh/replanning as applicable. It MUST NOT silently dispatch against a materially different target.

Fresh AUTH/R4/fence/target checks SHOULD occur as close as practical to dispatch. Long-lived queue approval MUST NOT be treated as proof that mutable prerequisites remain valid at effect time.

## 11. Bounded Action and Effect semantics

One Effect Permit MUST correspond to one **independently reconcilable Material Effect**, except when the source-native platform provides and the runtime verifies a real atomic transaction that makes the grouped effect independently reconcilable as one unit.

Composite human/model intent such as:

```text
commit code + push branch + create PR
```

is normally decomposed into separate effects with independent action identity, permit, result, reconciliation, and checkpoint boundaries unless the source-native platform provides a real atomic transaction that makes the grouped effect independently reconcilable as one unit.

The runtime MUST classify effect semantics at minimum along two independent axes.

### 11.1 Idempotency class

```text
IDEMPOTENT
CONDITIONALLY_IDEMPOTENT
NON_IDEMPOTENT
UNKNOWN
```

Possible strategies include:

```text
NATIVE_IDEMPOTENCY_KEY
COMPARE_AND_SET
SOURCE_READBACK
EXTERNAL_CONFIRMATION
MANUAL_VERIFICATION
NONE
```

### 11.2 Reversibility class

```text
REVERSIBLE_ATOMIC
COMPENSATABLE
IRREVERSIBLE
UNKNOWN
```

ProjectFramework MUST NOT claim arbitrary exactly-once execution across external systems. The required guarantee is narrower and defensible:

```text
no blind duplicate Material Effect
+ deterministic ambiguity handling
+ source-native/result reconciliation where available
```

## 12. Ambiguous results and reconciliation

TASK-057 `RESULT_VERIFICATION_REQUIRED` / verify-before-retry remains binding.

If a connection/process fails after dispatch may have occurred, absence of acknowledgement MUST NOT be normalized to failure.

Recovery decision:

```text
possibly dispatched?
  no  -> safe non-dispatch handling
  yes -> reconcile resulting state
             |
             |- proven APPLIED
             |- proven NOT_APPLIED
             `- cannot prove -> AMBIGUOUS
```

Reconciliation classes include:

```text
NATIVE_READBACK
IDEMPOTENCY_KEY
COMPARE_AND_SET
EXTERNAL_CONFIRMATION
HUMAN_VERIFICATION
NONE
```

For `NON_IDEMPOTENT | UNKNOWN` effects with `reconciliation: NONE`, an ambiguous result MUST become `AMBIGUOUS / MANUAL_RESOLUTION_REQUIRED` or another explicit blocking state. Automatic retry is prohibited.

## 13. Runtime Event Journal and Checkpoint authority

Within the runtime domain:

```text
Runtime Event Journal
> Checkpoint / Snapshot
```

The append-oriented Event Journal is the canonical runtime observation source. A Checkpoint/Snapshot is a derived recovery accelerator and MUST be traceable to the journal sequence it summarizes.

Minimum checkpoint linkage:

```yaml
checkpoint:
  execution_id: "<execution>"
  checkpoint_seq: "<checkpoint sequence>"
  event_sequence: "<last included event sequence>"
  previous_checkpoint_hash: "<previous checkpoint or NOT_APPLICABLE>"
  state_version: "<runtime state version>"
  resume_cursor: "<deterministic resume location>"
```

Recovery SHOULD load a compatible checkpoint and replay the journal tail. If required journal continuity cannot be proven, the runtime MUST fail closed as `RECOVERY_BLOCKED` or equivalent; it MUST NOT reconstruct execution truth from an LLM transcript or model memory.

The journal MUST use strict writer isolation: executors/models/tool subprocesses cannot directly forge, rewrite, or delete runtime events. Logical append-only semantics and atomic state-version transitions are required even when the physical storage implementation differs.

Hash chaining, signatures, immutable storage, or tamper-evident facilities may be used for higher assurance but are implementation choices, not mandatory Framework technologies.

## 14. Lease, heartbeat, fence, and control generation

These concepts remain distinct:

```text
Multica claim = coordination
lease = bounded worker liveness/assignment validity
heartbeat = liveness observation
fence = stale-attempt effect exclusion token
AUTH = permission
```

A heartbeat is not authority and not completion evidence.

A simple fence counter is insufficient across runtime-store restore/failover because an old numeric epoch could reappear. The canonical fence identity is therefore:

```text
(runtime_generation, fence_epoch)
```

A new authoritative control generation invalidates prior-generation leases, fences, and Effect Permits. Pending effects from the old generation require reconciliation before safe continuation.

Lease time MUST be based on runtime-authoritative time or equivalent monotonic duration semantics. Executor-local wall clock cannot be lease authority; clock skew is telemetry, not permission.

## 15. Atomic runtime transitions and concurrency

A highly available or multi-replica ControlTower may have multiple supervisors observing one execution. Runtime state transitions MUST therefore use `state_version` compare-and-set or an equivalent atomic primitive.

Conceptually:

```text
read state_version 17
attempt transition to 18 WHERE current == 17
0 rows / failed CAS -> STALE_CONTROL_DECISION -> reload
```

Framework semantics require one authoritative successful transition per execution version. They do not mandate PostgreSQL, Redis, Raft, a distributed lock product, or any specific database.

## 16. Typed Executor Protocol

Model/executor output and runtime-owned events MUST have separate namespaces and schemas.

An executor may produce bounded proposal/report types such as:

```text
ACTION_PROPOSAL
CANDIDATE_COMPLETE
WAIT_REQUEST
INPUT_REQUEST
YIELD
BLOCKED_REPORT
ERROR_REPORT
```

The executor MUST NOT be able to create authoritative runtime events such as:

```text
AUTH_GRANTED
LEASE_ACQUIRED
FENCE_ADVANCED
PERMIT_ISSUED
VERIFIED
INTEGRATED
TASK_DONE
```

A model saying `done` or emitting a candidate-complete proposal is only a request to evaluate completion. Verification and canonical Task completion remain governed by TASK-057/current Task contracts.

Typed protocol parsing MUST fail closed on unknown privileged fields rather than treating model-generated state as trusted runtime metadata.

## 17. Budget tree, retries, and recursion

Runtime budgets MUST be durable across model turns, worker replacement, and process restart.

Applicable dimensions may include:

```yaml
budget:
  max_model_turns: "<n>"
  max_tool_calls: "<n>"
  max_tokens: "<n>"
  max_wall_time: "<duration>"
  max_retries_per_action: "<n>"
  max_child_executions: "<n>"
  max_recursion_depth: "<n>"
```

For recursive/RLM execution, budgets are hierarchical allocations rather than cloned allowances:

```text
parent consumption + sum(child allocations) <= root budget
```

A child execution cannot manufacture new authority or budget by recursion. Budget exhaustion persists a truthful state such as `BUDGET_EXHAUSTED / BLOCKED / WAITING_FOR_REAUTHORIZATION` as applicable and MUST NOT imply Task DONE.

Retry policy belongs to the deterministic runtime. `REQUEST_RETRY` from a model does not itself authorize a retry.

## 18. Wait, wakeup, and fail-closed liveness

Long-running work SHOULD use explicit wait/wakeup semantics rather than burning model turns polling external conditions.

A wait declaration may include:

```yaml
wait_condition:
  reason: "<external condition>"
  wake_event: "<event when supported>"
  fallback_check_at: "<time when applicable>"
```

Fail-closed behavior MUST NOT become infinite retry/spin. The runtime distinguishes at least:

```text
transient/recoverable -> WAIT with bounded retry policy
external truth required -> WAIT / wake condition
human resolution required -> BLOCKED / MANUAL_RESOLUTION_REQUIRED
unresolvable ambiguity -> BLOCKED
```

## 19. Cancellation and in-flight effects

Cancellation prevents new governed dispatch under the cancelled scope but cannot erase facts already caused externally.

```text
Cancellation != rollback
Cancellation != undo of an already-dispatched effect
```

If cancellation occurs while an action is in flight:

1. stop new dispatches covered by the cancelled authority/scope;
2. mark applicable Attempt/Execution cancellation state truthfully;
3. reconcile every possibly-dispatched Material Effect;
4. record resulting source-native truth even when the canonical Task is `CANCELLED`;
5. run compensation only when separately governed and permitted.

A dispatched effect may still become `APPLIED` after cancellation. That fact is preserved rather than falsified to match lifecycle intent.

## 20. Compensation semantics

Compensation is a new governed effect, not history erasure.

```text
Compensation != atomic rollback
```

For a compensatable effect, the compensation action has its own Action identity, authority check, Effect Permit, budget, evidence, and reconciliation.

If compensation fails, the runtime records truthful partial state such as `PARTIALLY_COMPENSATED` rather than claiming `ROLLED_BACK` unless the source-native system proves an actual atomic rollback.

## 21. Runtime restart, store restore, and recovery

Process restart does not terminate the Task or Execution.

Recovery sequence:

```text
load runtime generation / establish governed successor generation when required
-> validate journal continuity
-> load compatible checkpoint
-> replay journal tail
-> identify expired/lost Attempts
-> reconcile unresolved DISPATCH_INTENT/DISPATCHED effects
-> invalidate stale leases/fences/permits
-> re-resolve authority/R4/contract fingerprints
-> schedule only safely runnable work
```

A runtime-store restore to an older snapshot MUST NOT reuse old control identity silently. A new Control Generation (or equivalent unique successor identity) is required before new effects, and unresolved effects from the former generation are reconciled first.

## 22. Runtime and event-schema version pinning

Long-running executions are version-pinned:

```yaml
runtime_contract_version: "1.0"
event_schema_version: "1.0"
```

Runtime deployment upgrades classify active-execution compatibility as:

```text
BACKWARD_COMPATIBLE
REQUIRES_MIGRATION
INCOMPATIBLE
```

`BACKWARD_COMPATIBLE` may continue under the pinned semantics. `REQUIRES_MIGRATION` requires quiesce/migration/verification/resume. `INCOMPATIBLE` blocks continuation until governed resolution. A new runtime MUST NOT silently reinterpret old journal events under incompatible semantics.

## 23. Security, trust, and durable observability

Durable journals/checkpoints MUST NOT become secret stores.

For sensitive arguments/results, the runtime uses the minimum durable representation sufficient for reconciliation, such as:

```text
REFERENCE_ONLY
REDACTED
HASH_ONLY
classified metadata
```

Credential references may be persisted when governed; raw secret values must not be written into Project Source, Task artifacts, runtime journal, checkpoints, or evidence merely for observability.

Tool output, retrieved content, or model text is untrusted data. Prompt injection or malicious tool output cannot create authority. Even a compromised executor must still pass Effect Gateway authority/envelope/trust/fence/precondition checks, provided effect-surface closure is actually enforced.

## 24. Multica boundary

TASK-057 remains authoritative: Multica owns coordination facts only.

TASK-058 explicitly separates:

```text
Multica claim
!= runtime lease
!= runtime fence
!= Effect Permit
!= AUTH
```

A Multica claim may be referenced by an Attempt but cannot make a stale worker safe, cannot prove source-native effect state, and cannot set Task DONE. A future implementation may integrate Multica with the runtime, but ownership boundaries remain separate.

## 25. Task Record and runtime journal separation

The TASK-057 Task Record remains a bounded observed execution result with Actual IPOCV and candidate/evidence references. It MUST NOT become an unbounded per-action event stream.

```text
Runtime Event Journal
= fine-grained execution-control observation

Task Record
= bounded durable result/Actual IPOCV observation used by VERIFY
```

Verification consumes the applicable Task Record, source-native evidence, exact candidate identity, and current truth. It does not need to trust arbitrary model narration or every raw runtime event.

## 26. Effect Gateway conformance boundary

A conforming implementation MUST be able to demonstrate, for each mediated Material Effect class:

1. the effect-capable surfaces available to the executor;
2. how uncontrolled mutation routes are prohibited or mediated;
3. where credentials live and how they are scoped;
4. how permits are minted/consumed atomically;
5. how stale generation/fence attempts are rejected;
6. which target preconditions are used;
7. which idempotency/reconciliation/reversibility classes apply;
8. how ambiguous results block or recover;
9. how cancellation/in-flight effects are reconciled;
10. how source-native resulting state is confirmed.

A policy document saying `use the Gateway` without enforceable effect-surface closure is not sufficient conformance for autonomous Material Effects.

## 27. Language- and host-neutral standard

TASK-058 standardizes protocol semantics, not an implementation language.

A future reference runtime may use Python, but a conforming implementation may use Python, Go, Rust, TypeScript, or another suitable environment if it satisfies the same contracts.

Likewise the Framework does not require:

```text
Prime Agent
PostgreSQL
SQLite
Redis
Kafka
Kubernetes
Docker
Raft
one queue product
one model provider
one MCP implementation
```

Prime Agent/RLM patterns remain useful reference evidence for persistent agent execution, recursive workspaces, and long-running autonomy, but no Prime Agent dependency is introduced by TASK-058.

## 28. Required Framework surfaces

Expected implementation surfaces after written-spec approval and implementation planning include at least:

```text
Framework-Source/references/core-governance-rules.md
Framework-Source/references/framework-governance-amendment-260916-task058-deterministic-execution-runtime-contract.md
Framework-Source/tests/pressure-scenarios.md
Framework-Source/templates/project-execution/README.md
Framework-Source/templates/project-execution/task-contract.md
Framework-Source/templates/project-execution/task-record.md
Framework-Source/templates/project-execution/executor-profile.md
Framework-Source/templates/project-execution/tools.md
Framework-Source/templates/project-execution/trust.md
```

Candidate new single-responsibility starters are:

```text
Framework-Source/templates/project-execution/runtime-contract.md
Framework-Source/templates/project-execution/execution-attempt.md
Framework-Source/templates/project-execution/execution-checkpoint.md
Framework-Source/templates/project-execution/action-journal.md
Framework-Source/templates/project-execution/effect-policy.md
```

The implementation plan may refine file decomposition while preserving the semantic boundaries in this spec. No new Project Source semantic slot or Stable-ID family is required by the design.

## 29. Pressure-scenario contract

TASK-057 allocated scenarios `529–556`. TASK-058 reserves the next contiguous design range `557–602` for RED-first implementation pressure coverage.

Required scenarios:

```text
557 worker death before mutation
558 worker death after possibly-applied mutation
559 stale/zombie worker after reassignment
560 lease expiry during slow action
561 runtime restart resumes from durable state
562 corrupted/missing checkpoint
563 duplicate event delivery
564 out-of-order event observation
565 model turn ends while execution is non-terminal
566 premature CANDIDATE_COMPLETE
567 budget exhaustion is not DONE
568 external WAIT/wakeup
569 Task cancellation during execution
570 AUTH revocation during execution
571 two workers contend for same resource
572 MCP fallback while previous result unresolved
573 non-Git external result reconciliation
574 RLM recursion depth violation
575 RLM hierarchical budget violation
576 Effect Gateway fence enforcement
577 AUTH revoked between validation and dispatch
578 R4 changes before dispatch
579 target precondition changes before dispatch
580 non-idempotent ambiguous effect
581 exactly-once assumption prohibited
582 checkpoint ahead of journal
583 journal discontinuity
584 Task Contract changes mid-execution
585 cancellation with in-flight action
586 irreversible effect after cancellation request
587 dual ControlTower CAS race
588 executor/runtime clock skew
589 model attempts forged runtime transition
590 model attempts forged authority/fence
591 sensitive journal argument leakage
592 stale Effect Permit
593 duplicate action proposal after resume
594 external human mutation during execution
595 runtime restart during reconciliation
596 runtime implementation upgrade during active execution
597 direct shell/network Gateway bypass
598 child process inherits mutation credential
599 consumed/stolen permit replay or transfer
600 runtime-store rollback / old-generation fence reuse
601 compound effect partial success / compensation failure
602 malicious tool-output prompt injection against effect controls
```

Scenario wording may be split into finer cases during TDD only if numbering remains contiguous and all listed semantic classes retain explicit coverage.

## 30. Release classification and migration

The candidate classification is:

```text
BACKWARD_COMPATIBLE_ADDITIVE_RUNTIME_CONTRACT
```

Target Framework version is `1.20.0`, Project Source Schema remains `1.0.0`, release format remains `3`.

Reasoning:

- new execution-runtime contracts and optional/applicability-driven Project-Execution starters are additive;
- canonical Task lifecycle remains unchanged;
- Risk remains `R0–R3`;
- no new Project Source semantic slot or Stable-ID family is introduced;
- non-ControlTower Projects remain valid;
- Brownfield historical Tasks are not silently retrofitted;
- a consuming Project adopts 1.20 only through existing governed Framework upgrade semantics.

If implementation discovers a true breaking contract or schema requirement, release classification MUST be re-evaluated rather than silently forcing it into 1.20.0.

## 31. Explicit implementation boundary

TASK-058 implementation, when separately authorized after written-spec approval and planning, is limited to Framework governance/documentation/contracts/templates/tests/release metadata.

TASK-058 MUST NOT implement:

```text
AI-ControlTower runtime service
Python supervisor
runtime database
scheduler / worker daemon
queue
lease/fencing service
Effect Gateway service
credential broker
sandbox/container runtime
network policy
MCP router
model router
RLM/recursive executor runtime
Multica runtime
automatic Task DONE updater
CI runner
merge bot / release bot
API server
self-improvement / continual-learning runtime
```

Those belong to separately governed future implementation scope, expected conceptually after TASK-058 acceptance.

## 32. Future task boundary

The expected next implementation line after verified TASK-058 is separate from this Task:

```text
TASK-059 candidate scope
= AI-ControlTower Python Supervisor Reference Runtime
```

A later RLM Executor Profile / recursive execution implementation and a governed continual-self-improvement harness remain separate future work. TASK-058 does not pre-register or authorize those Tasks merely by naming the likely decomposition.

## 33. Design V3 invariants

The frozen Design V3 requires all of the following:

```text
Model proposal != Runtime decision
Runtime decision != Authority
Claim != Lease != Fence != Authority
Heartbeat != completion evidence
Model turn lifetime != Task lifetime
Worker lifetime != Execution lifetime
Execution lifetime != Task lifecycle
Checkpoint != canonical runtime journal
Dispatch acknowledgement != resulting-state proof
Cancellation != rollback
Retry != safe unless effect semantics permit it
Exactly-once execution is not assumed
Task Contract material mutation invalidates pinned execution
Executor-local clock != lease authority
Child execution cannot create new budget
Material mediated effect without Effect Gateway = prohibited
Effect Permit != AUTH
Effect Permit is single-use/non-transferable/bound
Control generation change invalidates old lease/fence/permit
Compensation != rollback
Composite intent != atomic effect
Unreconcilable ambiguity != retryable failure
Fail closed != retry forever
Model cannot emit runtime-owned state
Executor cannot rewrite runtime journal
Effect-surface policy without confinement != enforcement
```

## 34. Completion criteria for TASK-058

TASK-058 may be considered complete only after:

1. this written spec receives explicit user approval;
2. an implementation plan is written and self-reviewed;
3. RED-first pressure scenarios cover the required `557–602` classes;
4. normative Framework surfaces implement the approved deterministic runtime contract without introducing runtime code;
5. maintained Project-Execution starters are coherent and authority-safe;
6. TASK-057 semantics remain preserved and non-conflicting;
7. independent review has no unresolved Critical/Important findings;
8. applicable AFFECTED verification passes;
9. one final `RELEASE_FULL` passes on the unchanged frozen candidate;
10. durable release/completion evidence is persisted;
11. Task lifecycle is reconciled truthfully;
12. publication/tag/GitHub Release/self-host promotion/AI-ControlTower runtime mutation remain separately governed.

## 35. Written-spec approval and execution gate

ACTOR-001 explicitly approved this Written Spec on `2026-09-16`. The TASK-058 implementation plan was then written/self-reviewed and execution was explicitly authorized on `2026-09-16`.

Current governed state during implementation:

```text
TASK-058 = IN_PROGRESS
WRITTEN_SPEC = APPROVED
IMPLEMENTATION_PLAN = WRITTEN / SELF_REVIEWED
EXECUTION = AUTHORIZED / IN_PROGRESS
AI_CONTROLTOWER_RUNTIME_IMPLEMENTATION = NOT AUTHORIZED_BY_TASK058
```

Execution still follows TASK-057 Planner/Execution Handoff semantics: current Task/Plan/Envelope, AUTH, `R4_CTX`, Ready Gate, tool/capability/trust/executor eligibility, workspace/target truth, and independent Verifier requirements remain binding. Planning/execution authorization does not authorize merge, tag/GitHub Release, consuming-Project upgrade, self-host promotion, or AI-ControlTower runtime mutation.
