# Framework Governance Amendment — TASK-058 Deterministic Execution Runtime Contract

**Framework target:** `1.20.0`  
**Project Source Schema:** `1.0.0`  
**Release format:** `3`  
**Task:** `TASK-058`  
**Status:** normative successor amendment for the Framework 1.19 AI-ControlTower Governance Support Layer

This amendment adds deterministic execution-control protocol semantics for a future AI-ControlTower-compatible runtime. It is **documentation/governance only** and does not implement a runtime service, scheduler, queue, database, worker daemon, lease/fencing service, Effect Gateway service, credential broker, sandbox, network policy, model/MCP router, Multica runtime, merge/release bot, CI runner, API server, automatic Task-DONE updater, or self-improvement runtime.

TASK-057 remains authoritative for PLAN/TASK/VERIFY, `R4_CTX`, Task Ready Gate, Operational Execution state, Expected/Actual IPOCV, Task/Verification Records, Multica coordination-only ownership, exact-candidate verification, `INTEGRATION_GATE`, Integration Reconciliation, and canonical Task-DONE ownership. TASK-058 composes with those owners; it does not transfer Project authority to the runtime or executor.

---

## 1. Deterministic execution principle

```text
Task lifetime != model-turn lifetime
Task lifetime != chat lifetime
Task lifetime != MCP connection lifetime
Worker lifetime != Execution lifetime
Execution lifetime != canonical Task lifecycle
Model proposal != Runtime decision
Runtime decision != Authority
Claim != Lease != Fence != Authority
Heartbeat != completion evidence
Verification PASS != Task DONE
```

The end of a model turn, worker process, MCP connection, or runtime process is not itself a Task/Execution terminal condition.

## 2. Authority and truth ownership

Existing owners remain:

```text
ProjectFramework = governance/protocol semantics
Project Source = canonical Project governance truth
Durable Task Source = canonical Task lifecycle truth
AUTH-* / explicit User authority = mutation/operation authority
R4_CTX = execution-time current truth from canonical/source-native owners
Multica = claim/coordination facts only
Executor = bounded performer/proposal producer
Task Record = bounded observed result / Actual IPOCV
Verification Record = state-bound verification result
Git/GitHub/source-native systems = factual authority for the state they own
```

TASK-058 adds only runtime-domain owners:

```text
AI-ControlTower Runtime Store = execution-control facts only
Runtime Event Journal = canonical runtime execution observation inside runtime domain
Checkpoint / Snapshot = derived recovery accelerator; never stronger than Journal
Effect Gateway = governed consequence boundary for mediated Material Effects
Effect Permit = short-lived dispatch-eligibility proof; never AUTH
```

The runtime MUST NOT own Project intent, Requirements, Decisions, Risk, Project Source, canonical Task lifecycle, AUTH, Verification PASS, Git truth, deployment truth, release truth, or OUT achievement.

## 3. Four lifecycle domains

### Canonical Task lifecycle

Exactly:

```text
TODO | IN_PROGRESS | DONE | BLOCKED | CANCELLED
```

### Operational Execution state

TASK-057 remains authoritative:

```text
PROPOSED -> READY_FOR_CLAIM -> CLAIMED -> EXECUTING -> RESULT_RECORDED
-> VERIFYING -> VERIFIED -> INTEGRATION_PENDING -> INTEGRATED -> CLOSED
exceptions: VERIFICATION_FAILED | BLOCKED | CANCELLED | STALE
```

`Operational Execution CLOSED != Task DONE`.

### Execution Attempt state

```text
CREATED -> RUNNABLE -> RUNNING -> WAITING -> RECONCILING -> TERMINATED
exceptions: LOST | BLOCKED | CANCEL_REQUESTED
```

`Attempt terminal != Operational Execution terminal`.

### Action / Effect state

```text
PROPOSED -> PREPARED -> PERMITTED -> DISPATCH_INTENT_RECORDED -> DISPATCHED
-> ACKNOWLEDGED -> RECONCILING -> APPLIED | NOT_APPLIED | AMBIGUOUS | REJECTED
```

`ACKNOWLEDGED != resulting-state proof` where source-native reconciliation is required.

## 4. Durable identities and pinned semantics

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
  runtime_generation: "<authoritative control generation>"
  fence_epoch: "<monotonic epoch within generation>"
```

Task/Plan/Envelope material semantic mutation MUST be detectable. Active execution never silently hot-swaps success semantics from a newer mutable contract path.

## 5. Deterministic Supervisor

The deterministic Supervisor owns runtime state transitions/scheduling decisions. Executors only propose/report.

```text
load durable execution state
-> resolve/revalidate prerequisites
-> select runnable Attempt
-> obtain executor proposal
-> validate proposal against contract/envelope/budget/policy
-> prepare bounded action
-> mediate Material Effect when applicable
-> persist/reconcile result
-> derive checkpoint
-> continue until governed terminal condition
```

`model turn ended != execution completed`.

## 6. Runtime Event Journal > Checkpoint

```text
Runtime Event Journal > Checkpoint / Snapshot
```

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

If required journal continuity cannot be proven, recovery fails closed as `RECOVERY_BLOCKED` or equivalent. Model/chat/worker memory cannot reconstruct authoritative runtime truth. Executors/models/tools cannot forge, rewrite, or delete authoritative runtime events.

## 7. Claim, lease, heartbeat, fence, generation

```text
Multica claim = coordination
lease = bounded assignment/liveness validity
heartbeat = liveness observation
fence = stale-attempt effect exclusion
AUTH = permission
```

Canonical stale-control identity is:

```text
(runtime_generation, fence_epoch)
```

A new generation invalidates old leases, fences, and Effect Permits; unresolved former-generation effects are reconciled before new effects. Runtime-authoritative/monotonic time controls lease validity; executor-local wall clock does not.

## 8. Atomic transitions and concurrency

Authoritative runtime transitions require `state_version` CAS/equivalent semantics:

```text
read state_version 17
attempt transition to 18 WHERE current == 17
failed CAS -> STALE_CONTROL_DECISION -> reload
```

One authoritative successful transition exists per execution version. No database/consensus product is mandated.

## 9. Restart / store-restore recovery

```text
establish/validate control generation
-> validate journal continuity
-> load compatible checkpoint
-> replay journal tail
-> identify expired/lost Attempts
-> reconcile unresolved possible effects
-> invalidate stale lease/fence/permit
-> fresh-resolve AUTH/R4/fingerprints
-> schedule only safely runnable work
```

Runtime-store rollback cannot silently reuse old control identity.

## 10. Runtime/event-schema version pinning

```yaml
runtime_contract_version: "1.0"
event_schema_version: "1.0"
```

Compatibility is classified as:

```text
BACKWARD_COMPATIBLE
REQUIRES_MIGRATION
INCOMPATIBLE
```

Incompatible newer runtime semantics MUST NOT silently reinterpret active/old journal events.

## 11. Effect-Surface Closure

For every Material Task, applicable executor effect surfaces are inventoried, including:

```text
MCP/tool calls
shell/process execution
network egress
Git/SSH credentials
cloud credentials
filesystem mounts
Docker/container sockets
database connections
external SDKs
child processes / recursive agents
```

Each governed Material Effect route is:

```text
MEDIATED_BY_EFFECT_GATEWAY
or
EXPLICITLY_PROHIBITED / CONFINED
```

An uncontrolled equivalent mutation route makes the executor non-conformant for autonomous mediation of that effect class. Effect-surface closure is an enforcement property, not a prompt-policy statement.

## 12. Effect Gateway

Immediately before dispatch of a mediated Material Effect, Gateway validation includes:

```text
current Operational Execution eligibility
current Attempt identity
runtime_generation + fence_epoch
Task/Plan/Envelope fingerprint validity
current applicable AUTH
required R4_CTX
Tool/Capability/Trust eligibility
exact target + target preconditions
idempotency/reconciliation/reversibility class
remaining budget / retry policy
Effect Permit validity
```

```text
Gateway eligibility != AUTH
Effect Permit != AUTH
Tool availability != Gateway eligibility
```

## 13. JIT single-use Effect Permit

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

Permit properties: single-use, non-transferable, attempt/action/action-hash/target/tool/generation/fence/contract/envelope-bound, short-lived. `PERMIT_ACTIVE -> PERMIT_CONSUMED` is atomic/CAS-equivalent.

`PERMIT_CONSUMED != effect APPLIED`.

## 14. Target preconditions / TOCTOU

Use source-native preconditions whenever supported, including exact Git ref/SHA, ETag/If-Match, resource version/generation, row version, object hash, CAS token, immutable candidate identity.

Stale target yields `PRECONDITION_CONFLICT` or equivalent. Unsupported preconditions are explicit and use reconciliation/fail-closed policy instead of assumed freshness. Fresh AUTH/R4/fence/target checks occur as close as practical to dispatch.

## 15. Bounded effect, idempotency, reconciliation, reversibility

One Permit maps to one independently reconcilable Material Effect except a verified real source-native atomic transaction.

```text
Idempotency: IDEMPOTENT | CONDITIONALLY_IDEMPOTENT | NON_IDEMPOTENT | UNKNOWN
Reconciliation: NATIVE_IDEMPOTENCY_KEY | COMPARE_AND_SET | SOURCE_READBACK |
                EXTERNAL_CONFIRMATION | MANUAL_VERIFICATION | NONE
Reversibility: REVERSIBLE_ATOMIC | COMPENSATABLE | IRREVERSIBLE | UNKNOWN
```

ProjectFramework does not claim arbitrary external exactly-once execution. Required guarantee is no blind duplicate Material Effect + deterministic ambiguity handling + source-native/result reconciliation where available.

## 16. Ambiguous result handling

TASK-057 `RESULT_VERIFICATION_REQUIRED` remains binding.

```text
possibly dispatched?
  no  -> safe non-dispatch handling
  yes -> reconcile -> APPLIED | NOT_APPLIED | AMBIGUOUS
```

`NON_IDEMPOTENT|UNKNOWN + reconciliation NONE + ambiguous` becomes `MANUAL_RESOLUTION_REQUIRED`/blocking. Automatic retry is prohibited. Switching worker/tool/fallback does not erase existing action identity or unresolved result.

## 17. Cancellation and compensation

Cancellation blocks new dispatch but does not erase external facts.

```text
Cancellation != rollback
Cancellation != undo of already-dispatched effect
Compensation != atomic rollback
```

In-flight effects are reconciled. Compensation is a separate governed Material Effect with its own Action identity, AUTH, Permit, target checks, budget, evidence, and reconciliation. Failed compensation may yield `PARTIALLY_COMPENSATED` / `MANUAL_RESOLUTION_REQUIRED`; `ROLLED_BACK` requires source-native proof of actual rollback.

## 18. Typed executor protocol

Model/executor output and runtime-owned events use separate schemas/namespaces.

Allowed proposal/report vocabulary includes:

```text
ACTION_PROPOSAL
CANDIDATE_COMPLETE
WAIT_REQUEST
INPUT_REQUEST
YIELD
BLOCKED_REPORT
ERROR_REPORT
```

Executors/models MUST NOT authoritatively produce:

```text
AUTH_GRANTED
LEASE_ACQUIRED
FENCE_ADVANCED
PERMIT_ISSUED
VERIFIED
INTEGRATED
TASK_DONE
```

Unknown privileged fields fail closed. A model saying `done`, `CANDIDATE_COMPLETE`, or `REQUEST_RETRY` is advisory input to deterministic evaluation, not a state transition or permission.

## 19. Durable hierarchical budget

Applicable durable budget dimensions include:

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

A child execution cannot manufacture new budget or authority. Budget exhaustion persists truthful state such as `BUDGET_EXHAUSTED | BLOCKED | WAITING_FOR_REAUTHORIZATION` as applicable and never implies Task DONE.

## 20. Wait/wakeup and bounded fail-closed liveness

```yaml
wait_condition:
  reason: "<external condition>"
  wake_event: "<event when supported>"
  fallback_check_at: "<bounded time when applicable>"
```

Routing:

```text
transient/recoverable -> WAIT with bounded retry policy
external truth required -> WAIT / wake condition
human resolution required -> BLOCKED / MANUAL_RESOLUTION_REQUIRED
unresolvable ambiguity -> BLOCKED
```

`fail closed != retry forever`; a fail-closed runtime MUST NOT convert uncertainty into infinite model/tool polling.

## 21. Multica boundary

```text
Multica claim != runtime lease != runtime fence != Effect Permit != AUTH
```

Multica may coordinate workers but cannot establish stale-worker safety, source-native effect truth, Verification PASS, integration truth, or Task DONE.

## 22. Task Record vs Runtime Event Journal

```text
Runtime Event Journal = fine-grained execution-control observation
Task Record = bounded observed execution result + Actual IPOCV consumed by VERIFY
```

Task Record MUST NOT become an unbounded per-action event stream. Verification uses Task Record, source-native evidence, exact candidate identity, applicable current truth, and declared requirements rather than trusting model narration or every raw journal event.

## 23. Secret-safe observability and untrusted content

Durable journal/checkpoint/evidence representations may use:

```text
REFERENCE_ONLY | REDACTED | HASH_ONLY | classified metadata
```

Raw secret values are prohibited merely for observability. Tool output, retrieved content, and model text are untrusted data and cannot create AUTH, generation/fence/Permit state, Verification PASS, integration truth, or Task DONE.

## 24. Effect Gateway conformance evidence

For each mediated effect class, a conforming runtime can demonstrate:

1. executor effect surfaces;
2. confinement/mediation of equivalent mutation routes;
3. credential location/scope;
4. Permit atomicity and binding;
5. stale generation/fence rejection;
6. target preconditions or explicit limitation;
7. idempotency/reconciliation/reversibility classes;
8. ambiguous-result handling;
9. cancellation/in-flight reconciliation/compensation;
10. source-native resulting-state confirmation.

A policy sentence saying `use the Gateway` without enforceable closure is not sufficient conformance.

## 25. Language-/host-neutral implementation boundary

TASK-058 specifies protocol properties, not implementation language or infrastructure. No Python/Go/Rust/TypeScript, database, queue, sandbox, model provider, MCP implementation, container system, or consensus product is mandated.

This Framework release adds no AI-ControlTower runtime implementation.

## 26. Canonical TASK-058 invariants

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
Executor cannot rewrite Runtime Event Journal
Effect-surface policy without confinement != enforcement
```
