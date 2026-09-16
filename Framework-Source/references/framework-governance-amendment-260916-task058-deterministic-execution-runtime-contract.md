# Framework Governance Amendment — TASK-058 Deterministic Execution Runtime Contract

Date: `2026-09-16`
Target: Framework `1.20.0` / Project Source Schema `1.0.0` / release format `3`
Classification: `BACKWARD_COMPATIBLE_ADDITIVE_RUNTIME_CONTRACT`
Depends on: `TASK-057`

## 1. Scope

Framework 1.20 extends the TASK-057 declarative PLAN/TASK/VERIFY governance layer with language-neutral deterministic execution-runtime **contract semantics** for long-running autonomous work. This amendment defines protocol boundaries that a future AI-ControlTower runtime may enforce. It does not implement that runtime.

The governing principle is:

```text
ProjectFramework defines governance/protocol law.
AI-ControlTower may own deterministic execution-control facts only.
The Effect Gateway is the consequence boundary for mediated Material Effects.
LLM/RLM/Human Executors propose or perform bounded work but do not become Project authority.
```

TASK-057 remains authoritative for PLAN/TASK/VERIFY, Expected/Actual IPOCV, `R4_CTX`, Task Ready Gate, Operational Execution state, Multica coordination-only ownership, exact-candidate verification, `INTEGRATION_GATE`, and canonical Task DONE ownership.

## 2. Authority and runtime ownership

Existing owners remain unchanged:

```text
Project Source = canonical Project governance truth
Durable Task Source = canonical Task lifecycle truth
AUTH-* / explicit User authority = operation/mutation authority
R4_CTX = current truth resolved from the real owner
Multica = operational claim/coordination facts only
Task Record = bounded observed execution result
Verification Record = state-bound verification result
Git/GitHub/source-native systems = factual authority for state they own
```

Framework 1.20 defines these runtime-domain owners:

```text
AI-ControlTower Runtime Store = execution-control facts only
Runtime Event Journal = canonical runtime observation inside the runtime domain
Checkpoint / Snapshot = derived recovery accelerator
Effect Gateway = governed Material-Effect mediation boundary
Effect Permit = short-lived dispatch-eligibility proof; never AUTH
```

The runtime MUST NOT own or mutate Project intent, Requirements, Decisions, Risk, Project Source, canonical Task lifecycle, AUTH, Verification PASS, Git truth, deployment truth, release truth, or OUT achievement merely because it coordinates execution.

```text
Runtime decision != Authority
Effect Permit != AUTH
Claim != Lease != Fence != Authority
Heartbeat != completion evidence
```

## 3. Four separate lifecycle domains

### 3.1 Canonical Task lifecycle

Unchanged:

```text
TODO | IN_PROGRESS | DONE | BLOCKED | CANCELLED
```

Only the canonical Task owner may mutate it under existing governance.

### 3.2 Operational Execution state

TASK-057 remains authoritative:

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

with applicable `VERIFICATION_FAILED | BLOCKED | CANCELLED | STALE` exceptions.

### 3.3 Execution Attempt state

One worker/executor attempt uses:

```text
CREATED
-> RUNNABLE
-> RUNNING
-> WAITING
-> RECONCILING
-> TERMINATED
```

Applicable exceptions/reporting states include:

```text
LOST | BLOCKED | CANCEL_REQUESTED
```

Attempt loss/termination MUST NOT by itself close Operational Execution or canonical Task.

### 3.4 Action / Effect state

Each independently reconcilable Material Effect uses:

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

`ACKNOWLEDGED != resulting-state proof` when the source-native domain requires readback/reconciliation.

## 4. Durable identity and contract pinning

Minimum conceptual identity:

```yaml
execution_identity:
  task_ref: "TASK-xxx"
  execution_id: "<durable execution id>"
  runtime_contract_version: "1.0"
  event_schema_version: "1.0"
  task_contract_ref: "<reference>"
  task_contract_fingerprint: "<semantic fingerprint>"
  plan_contract_fingerprint: "<fingerprint or NOT_APPLICABLE>"
  execution_envelope_fingerprint: "<fingerprint>"

attempt_identity:
  execution_id: "<execution id>"
  attempt_id: "<attempt id>"
  executor_ref: "<selected executor>"
  claim_ref: "<coordination claim>"
  runtime_generation: "<control generation>"
  fence_epoch: "<monotonic epoch within generation>"
```

Material Task Contract, Plan Contract, or Execution Envelope semantic changes MUST invalidate continuation or require governed replanning/revalidation. Active execution MUST NOT silently hot-swap success semantics.

## 5. Deterministic Supervisor

The deterministic Supervisor owns runtime state transitions and scheduling decisions. Executor proposals are inputs, not authoritative runtime transitions.

Conceptual order:

```text
load durable execution state
-> fresh-resolve applicable prerequisites
-> select runnable Attempt
-> obtain Executor proposal
-> validate against Contract/Envelope/budget/policy
-> prepare bounded Action
-> mediate Material Effect through Effect Gateway when applicable
-> persist/reconcile result
-> derive Checkpoint
-> continue until governed terminal condition
```

```text
Model turn ended != Execution completed
Worker lifetime != Execution lifetime
Execution lifetime != canonical Task lifecycle
Task lifetime != chat/MCP/model-turn lifetime
```

A runnable non-terminal execution may schedule another reasoning step subject to current authority, R4, claim/lease/fence, budgets, trust/tool/capability policy, and wait/block conditions.

## 6. Runtime Event Journal and Checkpoint authority

Inside the runtime domain:

```text
Runtime Event Journal > Checkpoint / Snapshot
```

The journal is logically append-oriented authoritative runtime observation. Checkpoint/Snapshot is derived and MUST identify the journal sequence summarized.

Minimum checkpoint linkage:

```yaml
checkpoint:
  execution_id: "<execution id>"
  checkpoint_seq: "<checkpoint sequence>"
  event_sequence: "<last journal event included>"
  previous_checkpoint_hash: "<hash or NOT_APPLICABLE>"
  state_version: "<runtime state version>"
  resume_cursor: "<deterministic resume location>"
```

A compatible checkpoint MAY accelerate recovery, but missing/corrupt checkpoint never authorizes inference. If required journal continuity cannot be proven, execution enters `RECOVERY_BLOCKED` or equivalent fail-closed state. Model/chat memory is not runtime truth.

Executors, model processes, tool subprocesses, and untrusted children MUST NOT directly forge, rewrite, or delete authoritative runtime events. Logical append-only semantics plus atomic state-version transitions are required; physical database technology is not prescribed.

## 7. Lease, heartbeat, fence, and control generation

These remain distinct:

```text
Multica claim = coordination
lease = bounded worker assignment/liveness validity
heartbeat = liveness observation
fence = stale-attempt effect-exclusion token
AUTH = permission
```

Canonical fence identity is:

```text
(runtime_generation, fence_epoch)
```

A new authoritative `runtime_generation` invalidates prior-generation leases, fences, and Effect Permits. Unresolved possible effects from the former generation MUST be reconciled before safe new dispatch.

Lease validity uses runtime-authoritative time or equivalent monotonic-duration semantics. Executor-local wall clock is telemetry, not authority.

## 8. Atomic runtime transitions

Runtime state transition uses `state_version` compare-and-set or an equivalent atomic primitive.

```text
read state_version = N
attempt transition WHERE current state_version = N
success -> N+1
failed CAS -> STALE_CONTROL_DECISION -> reload
```

One execution version has one authoritative successful transition. The Framework does not mandate PostgreSQL, Redis, Raft, a distributed lock product, or another specific storage/consensus technology.

## 9. Effect-Surface Closure

The Effect Gateway is an enforcement boundary only when uncontrolled equivalent effect paths do not remain available to the Executor.

For each applicable Material effect class, inventory effect-capable surfaces such as:

```text
MCP/tool calls
shell/process execution
network egress
Git/SSH credentials
cloud credentials
filesystem mounts
container/Docker sockets
database connections
external SDKs
child processes / recursive agents
```

Each governed effect-capable route MUST be one of:

```text
MEDIATED_BY_EFFECT_GATEWAY
EXPLICITLY_PROHIBITED
CONFINED
```

An Executor retaining an uncontrolled path capable of the same governed mutation MUST NOT be classified autonomously eligible for that effect class merely because policy says `use the Gateway`.

ProjectFramework mandates the effect-surface-closure property, not a specific sandbox/container/network technology.

For mediated Material Effects, mutation credentials SHOULD remain at or below the trusted Effect Gateway boundary rather than in unconstrained model/RLM/child workspaces. Uncontrolled Executor possession of a credential that bypasses the Gateway is non-conformant for that mediated effect class.

## 10. Effect Gateway

A Material Effect declared mediated MUST transit the Effect Gateway. Before consequence dispatch, the Gateway validates at least:

```text
current Operational Execution eligibility
current Attempt identity
runtime_generation + fence_epoch
Task/Plan/Envelope fingerprints
current applicable AUTH
required fresh R4 truth
Tool/Capability/Trust eligibility
target identity + target precondition
effect idempotency/reconciliation/reversibility
remaining budget/retry policy
Effect Permit validity
```

```text
Gateway eligibility != AUTH
Tool availability != Gateway eligibility
```

## 11. Just-in-Time Effect Permit

Every Gateway-mediated Material Effect MUST receive a short-lived JIT Effect Permit only after fresh effect-boundary validation.

Minimum shape:

```yaml
effect_permit:
  permit_id: "<unique id>"
  execution_id: "<execution id>"
  attempt_id: "<attempt id>"
  action_id: "<action id>"
  action_hash: "<canonical action fingerprint>"
  target_ref: "<exact target>"
  tool_ref: "<eligible effect tool>"
  runtime_generation: "<generation>"
  fence_epoch: "<epoch>"
  task_contract_fingerprint: "<fingerprint>"
  execution_envelope_fingerprint: "<fingerprint>"
  authority_ref: "<AUTH-* or explicit authority ref>"
  r4_context_ref: "<fresh truth ref>"
  target_precondition_ref: "<precondition or explicit unsupported classification>"
  issued_at: "<runtime-authoritative time>"
  expires_at: "<short validity boundary>"
  max_uses: 1
```

Permit requirements:

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

`PERMIT_ACTIVE -> PERMIT_CONSUMED` MUST be atomic/CAS-equivalent. Reuse, transfer, action mismatch, target mismatch, stale generation/fence, or expiry is rejected.

```text
PERMIT_CONSUMED != effect APPLIED
```

## 12. Target preconditions and TOCTOU

Material Effects MUST declare source-native target preconditions whenever supported, including as applicable:

```text
exact Git ref/SHA
ETag / If-Match
resource_version / generation
row version
object hash
compare-and-set token
immutable candidate identity
```

Unsupported precondition capability is explicit and routes to declared reconciliation/fail-closed handling. It never silently implies target freshness.

A mismatch yields `PRECONDITION_CONFLICT` or equivalent fail-closed result and requires refresh/replanning/revalidation as applicable.

Fresh AUTH, R4, generation/fence, target identity, and precondition checks occur as close as practical to dispatch. Queue-time validation does not prove effect-time validity.

## 13. Bounded Effect semantics

One Effect Permit MUST correspond to one independently reconcilable Material Effect, except when a verified source-native atomic transaction makes the grouped operation independently reconcilable as one unit.

Composite intent such as `commit + push + create PR` is therefore normally decomposed into independent effects.

### 13.1 Idempotency class

```text
IDEMPOTENT
CONDITIONALLY_IDEMPOTENT
NON_IDEMPOTENT
UNKNOWN
```

### 13.2 Reconciliation strategies/classes

```text
NATIVE_IDEMPOTENCY_KEY
COMPARE_AND_SET
SOURCE_READBACK
NATIVE_READBACK
EXTERNAL_CONFIRMATION
MANUAL_VERIFICATION
NONE
```

### 13.3 Reversibility class

```text
REVERSIBLE_ATOMIC
COMPENSATABLE
IRREVERSIBLE
UNKNOWN
```

Framework 1.20 MUST NOT claim arbitrary exactly-once execution across external systems. Its defensible contract is:

```text
no blind duplicate Material Effect
+ deterministic ambiguity handling
+ source-native/result reconciliation where available
```

## 14. Ambiguous results and retry

TASK-057 `RESULT_VERIFICATION_REQUIRED` / verify-before-retry remains binding.

After possible dispatch:

```text
source-native/result reconciliation
-> APPLIED
-> NOT_APPLIED
-> AMBIGUOUS
```

Missing acknowledgement is not proof of failure. For `NON_IDEMPOTENT | UNKNOWN` effects with no valid reconciliation path, `AMBIGUOUS` becomes `MANUAL_RESOLUTION_REQUIRED`/blocking. Automatic blind retry is prohibited.

Fallback tools/MCPs MUST NOT repeat an unresolved prior effect merely because the Primary is unavailable.

## 15. Typed Executor Protocol

Executor/model messages and runtime-owned events use separate schemas/namespaces.

Allowed proposal/report examples:

```text
ACTION_PROPOSAL
CANDIDATE_COMPLETE
WAIT_REQUEST
INPUT_REQUEST
YIELD
BLOCKED_REPORT
ERROR_REPORT
```

The Executor MUST NOT authoritatively emit:

```text
AUTH_GRANTED
LEASE_ACQUIRED
FENCE_ADVANCED
PERMIT_ISSUED
VERIFIED
INTEGRATED
TASK_DONE
```

Unknown privileged fields fail closed. `CANDIDATE_COMPLETE` is only a request for governed verification/completion evaluation.

## 16. Durable hierarchical budgets and recursion

Applicable budgets may include:

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

For recursive/RLM work:

```text
parent consumption + sum(child allocations) <= root budget
```

A child cannot manufacture authority or budget. Budget counters survive model turns, worker replacement, and runtime restart. Budget exhaustion is truthful blocked/waiting/reauthorization state as applicable and never Task DONE.

Model `REQUEST_RETRY` is advisory; retry policy is runtime-owned.

## 17. WAIT, wakeup, and fail-closed liveness

Long waits use durable wait/wakeup semantics rather than indefinite model polling.

```yaml
wait_condition:
  reason: "<external condition>"
  wake_event: "<event or NOT_APPLICABLE>"
  fallback_check_at: "<bounded check time or NOT_APPLICABLE>"
```

At minimum:

```text
transient/recoverable -> WAIT with bounded retry
external truth required -> WAIT / wake condition
human resolution required -> BLOCKED / MANUAL_RESOLUTION_REQUIRED
unresolvable ambiguity -> BLOCKED
```

```text
Fail closed != retry forever
```

## 18. Cancellation and in-flight effects

Cancellation prevents new dispatch under the cancelled scope; it does not erase already-dispatched facts.

```text
Cancellation != rollback
Cancellation != undo of dispatched effect
```

On cancellation with in-flight/potentially-dispatched effects:

1. prevent new affected dispatch;
2. preserve truthful Attempt/Execution cancellation state;
3. reconcile every possibly-dispatched Material Effect;
4. record source-native resulting truth even if canonical Task is `CANCELLED`;
5. run compensation only when separately governed and permitted.

An effect may become `APPLIED` after cancellation and remains factual.

## 19. Compensation

Compensation is a new governed effect, not history erasure.

It has its own Action identity, AUTH check, Effect Permit, budget, evidence, and reconciliation. Failure may produce `PARTIALLY_COMPENSATED` or another truthful partial state.

`ROLLED_BACK` is claimed only when the source-native system proves an actual atomic rollback.

## 20. Runtime restart, restore, and recovery

Process restart does not terminate the Task or Execution.

Recovery sequence:

```text
establish/validate control generation
-> validate journal continuity
-> load compatible derived checkpoint
-> replay journal tail
-> identify expired/lost Attempts
-> reconcile unresolved DISPATCH_INTENT_RECORDED/DISPATCHED effects
-> invalidate stale leases/fences/permits
-> fresh-resolve AUTH/R4/contract fingerprints
-> schedule only safely runnable work
```

Restoring an older runtime-store snapshot MUST NOT silently reuse former control identity. A new unique successor `runtime_generation` (or equivalent) is required before new effects; unresolved former-generation effects are reconciled first.

## 21. Runtime/event schema version pinning

Active Execution records include:

```text
runtime_contract_version
event_schema_version
```

Runtime upgrade compatibility is exactly:

```text
BACKWARD_COMPATIBLE
REQUIRES_MIGRATION
INCOMPATIBLE
```

`BACKWARD_COMPATIBLE` may continue under pinned semantics. `REQUIRES_MIGRATION` requires quiesce/migrate/verify/resume. `INCOMPATIBLE` blocks until governed resolution. New runtimes do not silently reinterpret old journal events.

## 22. Security and durable observability

Runtime journal/checkpoint/evidence MUST NOT become raw secret stores merely for observability.

Use minimum durable representation such as:

```text
REFERENCE_ONLY
REDACTED
HASH_ONLY
classified metadata
```

Tool output, retrieved content, and model text are untrusted data. Prompt injection cannot create AUTH or runtime-owned state. Even a compromised Executor still must pass effect-boundary controls, provided effect-surface closure is actually enforced.

## 23. Multica boundary

TASK-057 remains authoritative:

```text
Multica claim != runtime lease != runtime fence != Effect Permit != AUTH
```

Multica may coordinate worker claims/assignment/expiry but cannot establish stale-worker effect safety, source-native effect truth, Verification PASS, Task DONE, Git truth, release truth, or OUT achievement.

## 24. Task Record versus runtime journal

```text
Runtime Event Journal = fine-grained execution-control observations
Task Record = bounded observed result + Actual IPOCV used by VERIFY
```

Task Record MUST NOT become an unbounded action event stream. Verification consumes Task Record, exact candidate identity where applicable, current truth, required source-native evidence, and governed verification inputs; model narration is not authoritative proof.

## 25. Effect Gateway conformance evidence

For every mediated Material Effect class, a conforming implementation MUST demonstrate:

1. Executor effect-capable surfaces;
2. how uncontrolled routes are prohibited/confined/mediated;
3. credential location and scope;
4. atomic Permit mint/consume behavior;
5. stale generation/fence rejection;
6. target preconditions or explicit unsupported classification;
7. idempotency/reconciliation/reversibility classes;
8. ambiguous-result handling;
9. cancellation/in-flight reconciliation;
10. source-native resulting-state confirmation.

A policy statement saying `use the Gateway` without effect-surface closure is not sufficient conformance for autonomous Material Effects.

## 26. Language and host neutrality

This is a protocol/governance standard, not a language/runtime dependency. A future runtime may use Python, Go, Rust, TypeScript, or another implementation if it satisfies the contract.

Framework 1.20 does not require Prime Agent, PostgreSQL, SQLite, Redis, Kafka, Kubernetes, Docker, Raft, a queue product, a model provider, or an MCP product.

RLM/Prime Agent patterns remain useful reference evidence only; RLM remains an optional future Executor strategy rather than ProjectFramework authority.

## 27. Brownfield and adoption

- no historical Task is silently retrofitted;
- non-ControlTower Projects remain valid;
- new runtime-contract starters are optional/applicability-driven;
- no new Project Source semantic slot or Stable-ID family is introduced;
- consuming Projects adopt Framework 1.20 only through existing governed upgrade semantics;
- canonical Task lifecycle and Risk `R0–R3` remain unchanged.

## 28. Explicit no-runtime boundary

TASK-058 Framework implementation MUST NOT introduce:

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
MCP/model router
RLM runtime
Multica runtime
automatic Task DONE updater
CI runner
merge/release bot
API server
self-improvement / continual-learning runtime
```

The Framework ships governance/documentation/contracts/templates/tests/release metadata only.

## 29. Required invariants

```text
Model proposal != Runtime decision
Runtime decision != Authority
Claim != Lease != Fence != Authority
Heartbeat != completion evidence
Model turn lifetime != Task lifetime
Worker lifetime != Execution lifetime
Execution lifetime != Task lifecycle
Checkpoint != canonical Runtime Event Journal
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
