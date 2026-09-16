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

The following distinctions are mandatory:

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
AI-ControlTower Runtime Store
= execution-control facts only

Runtime Event Journal
= canonical runtime execution observation inside the runtime domain

Checkpoint / Snapshot
= derived recovery accelerator; never stronger than Runtime Event Journal

Effect Gateway
= governed consequence boundary for mediated Material Effects

Effect Permit
= short-lived dispatch-eligibility proof; never AUTH
```

The runtime MUST NOT become owner of Project intent, Requirements, Decisions, Risk, Project Source, canonical Task lifecycle, `AUTH-*`, Verification PASS, Git truth, deployment truth, release truth, or OUT achievement.

No runtime observation, queue state, claim, lease, fence, Permit, preference, capability, or health fact grants Project authority.

## 3. Four lifecycle domains

The four lifecycle domains MUST remain distinct.

### 3.1 Canonical Task lifecycle

Unchanged and exactly:

```text
TODO | IN_PROGRESS | DONE | BLOCKED | CANCELLED
```

Only the canonical Task owner may mutate this lifecycle under existing governance.

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

Applicable exception states remain such as:

```text
VERIFICATION_FAILED | BLOCKED | CANCELLED | STALE
```

`Operational Execution CLOSED != Task DONE`.

### 3.3 Execution Attempt state

One bounded worker attempt uses:

```text
CREATED
-> RUNNABLE
-> RUNNING
-> WAITING
-> RECONCILING
-> TERMINATED
```

Applicable exceptional outcomes/states include:

```text
LOST | BLOCKED | CANCEL_REQUESTED
```

`Attempt terminal != Operational Execution terminal`. Worker loss/termination MUST NOT by itself close the Operational Execution or canonical Task.

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

`ACKNOWLEDGED` is transport/protocol observation only. `ACKNOWLEDGED != resulting-state proof` whenever source-native readback/reconciliation is required.

## 4. Durable identity model

A conforming runtime MUST use durable identities that survive model, worker, process, host, and connection replacement.

Conceptual hierarchy:

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

Task Contract, Plan Contract, and Execution Envelope semantic mutation MUST be detectable. A material change to a pinned contract invalidates continuation or requires governed replanning/revalidation as applicable. An active execution MUST NOT silently hot-swap to newer success semantics from a mutable path.

## 5. Deterministic Supervisor boundary

A deterministic Supervisor owns runtime state transitions and scheduling decisions inside the runtime domain. Executors may propose actions and report observations but cannot self-promote runtime state.

Required control order:

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

Recovery SHOULD load a compatible checkpoint and replay the journal tail. If required journal continuity cannot be proven, the execution becomes `RECOVERY_BLOCKED` or an equivalent fail-closed state. LLM transcript, chat memory, worker memory, or an unsupported checkpoint MUST NOT reconstruct authoritative runtime truth.

Executors, models, tool subprocesses, and retrieved content MUST NOT be able to forge, rewrite, or delete authoritative runtime events. Logical append-only semantics and atomic state-version transitions are required even when physical storage differs.

Hash chains, signatures, immutable storage, or tamper-evident products may strengthen assurance but are not mandated technologies.

## 7. Claim, lease, heartbeat, fence, and authority separation

These concepts are distinct:

```text
Multica claim = operational coordination
lease = bounded worker assignment/liveness validity
heartbeat = liveness observation
fence = stale-attempt effect exclusion token
AUTH = permission
```

Therefore:

```text
Claim != Lease != Fence != AUTH
Heartbeat != Authority
Heartbeat != completion evidence
```

A Multica claim may be referenced by an Attempt but cannot make a stale worker safe, cannot prove source-native effect state, cannot mint AUTH, and cannot set Task DONE.

The canonical stale-control identity is:

```text
(runtime_generation, fence_epoch)
```

A simple numeric `fence_epoch` alone is insufficient across runtime-store restore/failover because an old epoch could reappear. A new authoritative `runtime_generation` invalidates all prior-generation leases, fences, and Effect Permits. Any possibly-dispatched effect from an old generation MUST be reconciled before safe continuation.

Lease validity MUST use runtime-authoritative time or equivalent monotonic-duration semantics. Executor-local wall clock is telemetry only and MUST NOT be lease authority.

## 8. Atomic runtime transitions and concurrency

A highly available/multi-replica ControlTower may have multiple supervisors observing the same execution. Authoritative runtime transitions MUST therefore use `state_version` compare-and-set or an equivalent atomic primitive.

Conceptual rule:

```text
read state_version 17
attempt transition to 18 WHERE current == 17
0 rows / failed CAS -> STALE_CONTROL_DECISION -> reload
```

Exactly one authoritative transition may succeed for an execution version. A losing supervisor MUST reload current state rather than applying a competing transition.

ProjectFramework mandates the atomicity property, not PostgreSQL, Redis, Raft, distributed locks, or another specific product.

## 9. Restart, failover, and store-restore recovery

Process/runtime restart does not terminate Task or Execution.

Recovery order is:

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

If a runtime store is restored to an older snapshot, the runtime MUST NOT silently reuse prior control identity. A new control generation (or equivalent unique successor identity) is required before new effects, and unresolved former-generation effects are reconciled first.

Checkpoint corruption or loss does not outrank a valid journal. A valid prior checkpoint plus replay may be used. If journal continuity itself cannot be established, recovery fails closed rather than reconstructing from model/chat memory.

## 10. Runtime/event-schema version pinning

Long-running executions are interpretation-version pinned:

```yaml
runtime_contract_version: "1.0"
event_schema_version: "1.0"
```

A runtime implementation upgrade classifies active-execution compatibility exactly as applicable:

```text
BACKWARD_COMPATIBLE
REQUIRES_MIGRATION
INCOMPATIBLE
```

- `BACKWARD_COMPATIBLE` may continue under the execution's pinned semantics.
- `REQUIRES_MIGRATION` requires governed quiesce/migration/verification/resume.
- `INCOMPATIBLE` blocks continuation until governed resolution.

A newer runtime MUST NOT silently reinterpret historical journal events under incompatible semantics.

## 11. Durable observability and secrets

Runtime journals/checkpoints/evidence MUST NOT become secret stores. Persist the minimum representation sufficient for deterministic reconciliation, for example:

```text
REFERENCE_ONLY
REDACTED
HASH_ONLY
classified metadata
```

Credential references may be persisted when governed. Raw secret values MUST NOT be persisted in Project Source, Task artifacts, Runtime Event Journal, checkpoints, or evidence merely for observability.

Tool output, retrieved content, and model text are untrusted data; they cannot create authority, control generation, fences, verification, or Task completion state.

## 12. Source-native truth preservation

Runtime decision != authority and runtime observation != external truth ownership.

Git/GitHub/database/cloud/service/runtime targets remain factual owners for the state they own. External human/source-native changes observed during an execution MUST be reconciled as current truth; runtime recency or journal position does not permit overwriting a source-native fact by assertion.

A transport acknowledgement or runtime state transition never substitutes for source-native resulting-state proof where such proof is required.

## 13. Conformance and implementation neutrality

TASK-058 specifies protocol properties, not implementation language or infrastructure. A conforming implementation may use Python, Go, Rust, TypeScript, or another environment and may choose appropriate persistence/coordination technologies if all required semantics hold.

TASK-058 does not require Prime Agent, PostgreSQL, SQLite, Redis, Kafka, Kubernetes, Docker, Raft, one queue product, one model provider, or one MCP implementation.

This Framework release does not implement or require an AI-ControlTower runtime. Runtime implementation remains separately governed future scope.

## 14. Core invariants introduced by this amendment

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
Task/Plan/Envelope material mutation invalidates pinned execution as applicable
Executor-local clock != lease authority
Model/tool output cannot emit authoritative runtime-owned state
Executor cannot rewrite Runtime Event Journal
Runtime restart != execution restart from scratch
Control generation change invalidates old lease/fence/permit
Fail closed != retry forever
```

The Effect Gateway, Effect Permit, target precondition, effect idempotency/reconciliation/reversibility, cancellation/compensation, typed executor protocol, budget, and wait/wakeup rules are defined in the same TASK-058 contract and are added to this amendment in the subsequent bounded implementation steps of the approved TASK-058 plan.
