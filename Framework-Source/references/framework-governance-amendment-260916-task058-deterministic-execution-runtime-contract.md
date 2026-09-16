# Framework Governance Amendment — TASK-058 Deterministic Execution Runtime Contract

**Framework target:** `1.20.0`  
**Project Source Schema:** `1.0.0`  
**Release format:** `3`  
**Task:** `TASK-058`  
**Status:** normative successor amendment for the Framework 1.19 AI-ControlTower Governance Support Layer

This amendment extends Framework 1.19 with deterministic execution-control protocol semantics for a future AI-ControlTower-compatible runtime. It remains **documentation/governance only**. It does not implement a runtime service, scheduler, queue, database, worker daemon, lease/fencing service, Effect Gateway service, credential broker, sandbox, model/MCP router, merge bot, CI runner, API server, automatic Task-DONE updater, or self-improvement runtime.

Normative precedence remains the current approved amendment → Core Governance → maintained operational/templates guidance. TASK-057 remains authoritative for PLAN/TASK/VERIFY, `R4_CTX`, Task Ready Gate, Operational Execution state, Task/Verification Records, Multica coordination-only ownership, exact-candidate verification, integration reconciliation, and canonical Task-DONE ownership. This amendment composes with those semantics and does not transfer Project authority to the runtime or executor.

---

## 1. Deterministic execution principle

ProjectFramework defines the governed protocol. AI-ControlTower or another conforming runtime may own deterministic execution-control state inside its runtime domain. Executors—including GPT, Claude, Codex, Local LLM, RLM, Human, or future executor types—produce bounded proposals/observations; they do not become owners of Project authority, runtime truth, credentials, verification truth, or external side effects merely by executing a Task.

Mandatory distinctions:

```text
Task lifetime != model-turn lifetime
Task lifetime != chat lifetime
Task lifetime != MCP connection lifetime
Worker lifetime != Execution lifetime
Execution lifetime != canonical Task lifecycle
Model proposal != runtime decision
Runtime decision != Authority
Claim != Lease != Fence != Authority
Heartbeat != completion evidence
Verification PASS != Task DONE
```

The end of a model turn, worker process, MCP connection, or runtime process is not by itself a Task/Execution terminal condition.

## 2. Authority and truth ownership

Framework 1.19 owners remain unchanged:

```text
ProjectFramework = governance/protocol semantics
Project Source = canonical Project governance truth
Durable Task Source = canonical Task lifecycle truth
AUTH-* / explicit User authority = mutation/operation authority
R4_CTX = execution-time current truth from canonical/source-native owners
Multica = claim/coordination facts only
Executor = bounded performer/proposal producer
Task Record = bounded observed execution result / Actual IPOCV
Verification Record = state-bound verification result
Git/GitHub/source-native systems = factual authority for the state they own
```

TASK-058 adds only these runtime-domain owners:

```text
AI-ControlTower Runtime Store = execution-control facts only
Runtime Event Journal = canonical runtime execution observation inside runtime domain
Checkpoint / Snapshot = derived recovery accelerator; never stronger than Runtime Event Journal
Effect Gateway = governed consequence boundary for mediated Material Effects
Effect Permit = short-lived dispatch-eligibility proof; never AUTH
```

The runtime MUST NOT become owner of Project intent, Requirements, Decisions, Risk, Project Source, canonical Task lifecycle, `AUTH-*`, Verification PASS, Git truth, deployment truth, release truth, or OUT achievement.

No runtime observation, queue state, claim, lease, fence, Permit, preference, capability, or health fact grants Project authority.

## 3. Four lifecycle domains

### 3.1 Canonical Task lifecycle

Unchanged and exactly:

```text
TODO | IN_PROGRESS | DONE | BLOCKED | CANCELLED
```

Only the canonical Task owner may mutate this lifecycle.

### 3.2 Operational Execution state

TASK-057 remains authoritative:

```text
PROPOSED -> READY_FOR_CLAIM -> CLAIMED -> EXECUTING -> RESULT_RECORDED
-> VERIFYING -> VERIFIED -> INTEGRATION_PENDING -> INTEGRATED -> CLOSED
```

Applicable exception states include `VERIFICATION_FAILED | BLOCKED | CANCELLED | STALE`.

`Operational Execution CLOSED != Task DONE`.

### 3.3 Execution Attempt state

```text
CREATED -> RUNNABLE -> RUNNING -> WAITING -> RECONCILING -> TERMINATED
exceptions: LOST | BLOCKED | CANCEL_REQUESTED
```

`Attempt terminal != Operational Execution terminal`. Worker loss/termination MUST NOT by itself close the Operational Execution or canonical Task.

### 3.4 Action / Effect state

Each independently reconcilable Material Effect uses:

```text
PROPOSED -> PREPARED -> PERMITTED -> DISPATCH_INTENT_RECORDED -> DISPATCHED
-> ACKNOWLEDGED -> RECONCILING -> APPLIED | NOT_APPLIED | AMBIGUOUS | REJECTED
```

`ACKNOWLEDGED` is transport/protocol observation only. `ACKNOWLEDGED != resulting-state proof` whenever source-native readback/reconciliation is required.

## 4. Durable identity model

A conforming runtime MUST use durable identities that survive model, worker, process, host, and connection replacement.

```text
Task
`- Execution
   |- Attempt 1
   |- Attempt 2
   `- Attempt N
      `- Action / Effect records
```

Minimum execution identity:

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
```

Minimum Attempt identity:

```yaml
attempt_identity:
  execution_id: "<execution id>"
  attempt_id: "<attempt id>"
  executor_ref: "<selected executor>"
  claim_ref: "<coordination claim>"
  runtime_generation: "<authoritative control generation>"
  fence_epoch: "<monotonic epoch within generation>"
```

Task Contract, Plan Contract, and Execution Envelope semantic mutation MUST be detectable. A material change to a pinned contract invalidates continuation or requires governed replanning/revalidation. An active execution MUST NOT silently hot-swap to newer success semantics from a mutable path.

## 5. Deterministic Supervisor boundary

The deterministic Supervisor owns runtime state transitions and scheduling decisions inside the runtime domain. Executors may propose actions/report observations but cannot self-promote runtime state.

```text
load durable execution state
-> resolve/revalidate applicable prerequisites
-> select runnable Attempt
-> obtain executor/model proposal
-> validate proposal against contract/envelope/budget/policy
-> prepare bounded action
-> mediate Material Effect through Effect Gateway when applicable
-> persist result / reconcile source-native effect
-> derive checkpoint
-> continue until governed terminal condition
```

A model returning `done`, a worker exiting, or a model turn ending is only an observation/proposal. If the execution remains runnable and non-terminal, another reasoning/action step may be scheduled subject to current authority, `R4_CTX`, budget, wait/block, eligibility, and control-generation rules.

## 6. Runtime Event Journal and Checkpoint authority

Inside the runtime domain:

```text
Runtime Event Journal > Checkpoint / Snapshot
```

The Runtime Event Journal is append-oriented logical canonical runtime observation. Checkpoint/Snapshot is derived recovery state and MUST identify the journal sequence it summarizes.

```yaml
checkpoint:
  execution_id: "<execution>"
  checkpoint_seq: "<checkpoint sequence>"
  event_sequence: "<last included event sequence>"
  previous_checkpoint_hash: "<previous checkpoint or NOT_APPLICABLE>"
  state_version: "<runtime state version>"
  resume_cursor: "<deterministic resume location>"
```

If required journal continuity cannot be proven, execution becomes `RECOVERY_BLOCKED` or equivalent. LLM transcript, chat memory, worker memory, or an unsupported checkpoint MUST NOT reconstruct authoritative runtime truth.

Executors, models, tool subprocesses, and retrieved content MUST NOT forge, rewrite, or delete authoritative runtime events. Logical append-only semantics and atomic state-version transitions are required even when physical storage differs.

## 7. Claim, lease, heartbeat, fence, and authority separation

```text
Multica claim = operational coordination
lease = bounded worker assignment/liveness validity
heartbeat = liveness observation
fence = stale-attempt effect exclusion token
AUTH = permission
```

Therefore `Claim != Lease != Fence != AUTH`; `Heartbeat != Authority`; `Heartbeat != completion evidence`.

Canonical stale-control identity is:

```text
(runtime_generation, fence_epoch)
```

A new authoritative `runtime_generation` invalidates prior-generation leases, fences, and Effect Permits. Any possibly-dispatched effect from an old generation MUST be reconciled before safe continuation.

Lease validity MUST use runtime-authoritative time or equivalent monotonic-duration semantics. Executor-local wall clock is telemetry only and MUST NOT be lease authority.

## 8. Atomic runtime transitions and concurrency

Authoritative runtime transitions MUST use `state_version` compare-and-set or equivalent atomic primitive.

```text
read state_version 17
attempt transition to 18 WHERE current == 17
0 rows / failed CAS -> STALE_CONTROL_DECISION -> reload
```

Exactly one authoritative transition may succeed for an execution version. ProjectFramework mandates the atomicity property, not a database/consensus product.

## 9. Restart, failover, and store-restore recovery

```text
establish/validate authoritative control generation
-> validate Runtime Event Journal continuity
-> load compatible checkpoint when available
-> replay journal tail
-> identify expired/lost Attempts
-> reconcile unresolved DISPATCH_INTENT_RECORDED / DISPATCHED effects
-> invalidate stale lease/fence/permit state
-> fresh-resolve AUTH / R4_CTX / pinned contract fingerprints
-> schedule only safely runnable work
```

Runtime-store rollback MUST NOT silently reuse prior control identity. A new generation/equivalent successor identity is required before new effects, and unresolved former-generation effects are reconciled first.

## 10. Runtime/event-schema version pinning

```yaml
runtime_contract_version: "1.0"
event_schema_version: "1.0"
```

Active-execution compatibility classes are:

```text
BACKWARD_COMPATIBLE
REQUIRES_MIGRATION
INCOMPATIBLE
```

A newer runtime MUST NOT silently reinterpret historical journal events under incompatible semantics.

## 11. Durable observability and secrets

Runtime journals/checkpoints/evidence MUST NOT become secret stores. Persist the minimum representation sufficient for deterministic reconciliation, e.g. `REFERENCE_ONLY | REDACTED | HASH_ONLY | classified metadata`.

Raw secret values MUST NOT be persisted in Project Source, Task artifacts, Runtime Event Journal, checkpoints, or evidence merely for observability.

Tool output, retrieved content, and model text are untrusted data; they cannot create authority, control generation, fences, verification, or Task completion state.

## 12. Source-native truth preservation

Runtime decision != authority and runtime observation != external truth ownership. Git/GitHub/database/cloud/service/runtime targets remain factual owners for the state they own. External human/source-native changes observed during an execution MUST be reconciled as current truth.

## 13. Effect-Surface Closure and executor confinement

The Effect Gateway is an enforcement boundary only when governed effect paths cannot bypass it.

For every Material Task, a conforming runtime MUST inventory effect-capable surfaces available to the executor, including where applicable:

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

Every governed Material Effect route MUST be exactly one of:

```text
MEDIATED_BY_EFFECT_GATEWAY
EXPLICITLY_PROHIBITED / CONFINED
```

An executor retaining an uncontrolled equivalent mutation route MUST NOT be classified as autonomously eligible for that mediated effect class merely because policy tells it to use the Gateway.

ProjectFramework mandates **effect-surface closure**, not Docker/Kubernetes/a specific sandbox/network/security technology. For mediated Material Effects, raw mutation credentials SHOULD reside at or below the trusted Gateway boundary rather than in unconstrained model/RLM workspaces.

## 14. Effect Gateway validation boundary

A Material Effect MUST transit the Gateway when the applicable runtime/effect policy declares that effect mediated.

Immediately before consequence dispatch, the Gateway validates at least:

```text
current Operational Execution eligibility
current Attempt identity
current runtime_generation + fence_epoch
Task/Plan/Execution-Envelope fingerprint validity
current applicable AUTH
required R4_CTX current truth
Tool / Capability / Trust eligibility
exact target identity + target preconditions
idempotency / reconciliation / reversibility semantics
remaining budget / retry policy
Effect Permit validity
```

The Gateway does not create authority. It enforces already-valid authority/policy at the consequence boundary.

```text
Gateway eligibility != AUTH
Effect Permit != AUTH
Tool availability != Gateway eligibility
```

## 15. Just-in-Time Effect Permit

Every Gateway-mediated Material Effect requires a fresh, short-lived Effect Permit minted only after the applicable consequence-boundary checks pass.

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

A Permit is:

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

`PERMIT_ACTIVE -> PERMIT_CONSUMED` MUST be atomic/CAS-equivalent. Reuse, transfer, action mismatch, target mismatch, tool mismatch, stale generation/fence, contract mismatch, or expiry is rejected rather than inferred away.

`PERMIT_CONSUMED != effect APPLIED`.

## 16. Target preconditions and TOCTOU control

Material Effects MUST declare source-native target preconditions whenever the target supports them, e.g.:

```text
Git exact ref/SHA
ETag / If-Match
resource_version / generation
row version
object hash
compare-and-set token
immutable candidate identity
```

A stale precondition yields `PRECONDITION_CONFLICT` or equivalent and blocks dispatch against the materially different target. Unsupported target preconditions MUST be explicit and route to the declared reconciliation/fail-closed strategy rather than assumed freshness.

Fresh AUTH/R4/fence/target checks SHOULD occur as close as practical to dispatch. Long-lived queue approval is not proof that mutable prerequisites remain valid.

## 17. Bounded Action / Effect semantics

One Effect Permit corresponds to one **independently reconcilable Material Effect**, except when a source-native platform provides and the runtime verifies a genuine atomic transaction making a group one independently reconcilable effect.

Composite intent such as `commit + push + create PR` is normally decomposed into separate actions/effects with independent identity, Permit, result, reconciliation, and checkpoint semantics.

Idempotency class is at least:

```text
IDEMPOTENT
CONDITIONALLY_IDEMPOTENT
NON_IDEMPOTENT
UNKNOWN
```

Reconciliation strategies may include:

```text
NATIVE_IDEMPOTENCY_KEY
COMPARE_AND_SET
SOURCE_READBACK
EXTERNAL_CONFIRMATION
MANUAL_VERIFICATION
NONE
```

Reversibility class is at least:

```text
REVERSIBLE_ATOMIC
COMPENSATABLE
IRREVERSIBLE
UNKNOWN
```

ProjectFramework MUST NOT claim arbitrary exactly-once execution across external systems. Required guarantee is:

```text
no blind duplicate Material Effect
+ deterministic ambiguity handling
+ source-native/result reconciliation where available
```

## 18. Ambiguous results and reconciliation

TASK-057 `RESULT_VERIFICATION_REQUIRED` / verify-before-retry remains binding.

```text
possibly dispatched?
  no  -> safe non-dispatch handling
  yes -> reconcile resulting state
          |- proven APPLIED
          |- proven NOT_APPLIED
          `- cannot prove -> AMBIGUOUS
```

Reconciliation classes include `NATIVE_READBACK | IDEMPOTENCY_KEY | COMPARE_AND_SET | EXTERNAL_CONFIRMATION | HUMAN_VERIFICATION | NONE`.

For `NON_IDEMPOTENT | UNKNOWN` effects with `reconciliation: NONE`, an ambiguous result MUST become `AMBIGUOUS / MANUAL_RESOLUTION_REQUIRED` or equivalent blocking state. Automatic retry is prohibited.

A new worker/tool route/fallback does not reset ambiguity. It must reconcile the existing Action identity/result before any new effect.

## 19. Cancellation and in-flight effects

Cancellation prevents **new** governed dispatch under the cancelled scope but cannot erase external facts already caused.

```text
Cancellation != rollback
Cancellation != undo of an already-dispatched effect
```

When cancellation occurs with an in-flight action:

1. stop new dispatches covered by cancelled authority/scope;
2. mark Attempt/Execution cancellation state truthfully;
3. reconcile every possibly-dispatched Material Effect;
4. preserve resulting source-native truth even when canonical Task is `CANCELLED`;
5. run compensation only when separately governed/permitted.

An effect may become `APPLIED` after cancellation. That fact is preserved.

## 20. Compensation semantics

Compensation is a new governed Material Effect, not history erasure and not implied rollback.

```text
Compensation != atomic rollback
```

A compensation action has its own Action identity, applicable AUTH, Gateway/Effect Permit, target preconditions, budget, evidence, and reconciliation.

If compensation fails, runtime records truthful partial state such as `PARTIALLY_COMPENSATED` / `MANUAL_RESOLUTION_REQUIRED` rather than claiming `ROLLED_BACK` unless source-native evidence proves actual atomic rollback.

## 21. Effect Gateway conformance evidence

For every mediated Material Effect class, a conforming implementation MUST be able to show:

1. effect-capable surfaces exposed to the executor;
2. how uncontrolled equivalent mutation routes are mediated/prohibited/confined;
3. where credentials live and how they are scoped;
4. how Permits are minted/consumed atomically;
5. how stale generation/fence attempts are rejected;
6. source-native target preconditions or explicit limitation;
7. idempotency/reconciliation/reversibility classification;
8. ambiguous-result handling;
9. cancellation/in-flight-effect handling;
10. resulting-state confirmation.

A policy sentence saying `use the Gateway` without enforceable effect-surface closure is not sufficient conformance for autonomous Material Effects.

## 22. Conformance and implementation neutrality

TASK-058 specifies protocol properties, not implementation language/infrastructure. It does not require Prime Agent, PostgreSQL, SQLite, Redis, Kafka, Kubernetes, Docker, Raft, one queue product, one model provider, or one MCP implementation.

This Framework release does not implement the AI-ControlTower runtime or Effect Gateway service.

## 23. Core invariants

```text
Model proposal != Runtime decision
Runtime decision != Authority
Claim != Lease != Fence != Authority
Heartbeat != completion evidence
Model turn lifetime != Task lifetime
Worker lifetime != Execution lifetime
Execution lifetime != Task lifecycle
Checkpoint != Runtime Event Journal
ACKNOWLEDGED != resulting-state proof
Cancellation != rollback
Retry != safe unless effect semantics permit it
Exactly-once execution is not assumed
Task/Plan/Envelope material mutation invalidates pinned execution as applicable
Executor-local clock != lease authority
Material mediated effect without Effect Gateway = prohibited
Effect Permit != AUTH
Effect Permit is single-use/non-transferable/bound
Control generation change invalidates old lease/fence/permit
Compensation != rollback
Composite intent != atomic effect
Unreconcilable ambiguity != retryable failure
Model/tool output cannot emit authoritative runtime-owned state
Executor cannot rewrite Runtime Event Journal
Effect-surface policy without confinement != enforcement
Fail closed != retry forever
```

Typed executor protocol, durable hierarchical budget, wait/wakeup, Multica/Task-Record boundaries, and the maintained Project-Execution starter surfaces are added by the following bounded TASK-058 implementation steps.
