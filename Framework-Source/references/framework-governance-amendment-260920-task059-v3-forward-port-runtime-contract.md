# Framework Governance Amendment — TASK-059 V3 Forward-Port Runtime Control Contract

Date: `2026-09-20`
Framework: `1.21.0`
Schema: `1.0.0`
Release format: `3`
Source Task: `TASK-059`
Design spec: `docs/superpowers/specs/2026-09-20-task059-v3-forward-port-runtime-contract-design.md` (ACTOR-001 explicit approval, 2026-09-20)
Predecessor amendment: `references/framework-governance-amendment-260916-task058-wave-a-v2-deterministic-execution-foundation.md` (Framework `1.20.0`; remains the authoritative Wave A V2 contract)
Historical source material: `docs/superpowers/specs/2026-09-16-task058-deterministic-execution-runtime-contract-design.md` (superseded Design V3; source material only, never reactivated)

## 1. Scope

Framework `1.21.0` forward-ports the still-useful, non-overlapping runtime-control semantics of the superseded TASK-058 Design V3 onto the verified Framework `1.20.0` Wave A V2 baseline. It adds a **Durable Runtime Control Contract**: a language-neutral, declarative set of record/contract semantics for long-running governed execution — durable runtime observation, checkpoint derivation, supervisor control generation, runtime liveness projection, Effect Gateway mediation with single-use Effect Permits, ambiguous-effect reconciliation, bounded continuation, RLM/recursive execution profiles, cancellation/compensation, and runtime version pinning.

The layer is additive. It changes no Project Source semantic slot, no Project Source Stable-ID family, no Registered Command set, no canonical Task lifecycle value, no Risk level (Risk remains exactly `R0–R3`), and no release-descriptor format. Project Source Schema remains `1.0.0`. Existing Framework `1.20.0` semantics — the Compositional State Binding Hub, `REVISION_SET`, `EXECUTION_INPUT_MANIFEST`, `EXECUTION_STATE_BINDING`, `EXECUTION_OWNERSHIP_GRANT` / `EXECUTION_OWNERSHIP_EVIDENCE`, `OPERATIONAL_TRANSITION`, `RESULT_ACCEPTANCE`, `VERIFICATION_VALIDITY_EVALUATION`, fencing assurance ordering, CAS transition semantics, Reassignment Gate, and all Framework `1.19.0` execution-workflow semantics — are preserved unchanged and remain authoritative. TASK-059 extends them compositionally; it creates no parallel equivalents.

This amendment implements no runtime. It defines declarative semantics only: record shapes, identity/binding rules, fail-closed eligibility and invalidation behavior, required ordering and guards, interoperability invariants, and no-inference / no-history-rewrite rules. The executable reference runtime is a separate AI-ControlTower implementation Task (Section 18).

## 2. Authority model and non-runtime boundary

The Framework `1.20.0` authority model carries forward unchanged:

```text
ProjectFramework        = governance contract semantics
Project Source          = canonical Project governance truth
Durable Task Source     = canonical Task lifecycle truth
AUTH-* / explicit User authority = mutation/operation authority
R4 Current Truth Context = execution-time resolution of mutable facts from their real owners
Project Adapter         = translation/locator boundary
Capability / Tool / Trust / Executor Profiles = execution eligibility policy
Multica                 = operational claim/coordination owner only
Executor                = bounded work performer / proposal producer
Task Record             = actual execution observation
Verification Record     = state-bound verification result
Git / GitHub / source-native systems = factual authority for state they own
```

The following remain distinct and none implies another. The Framework `1.20.0` chain is retained verbatim, and TASK-059 extends it:

```text
Contract ≠ Authority
Capability ≠ Authority
Eligibility ≠ Authority
Claim ≠ Authority
Execution success ≠ Verification PASS
Verification PASS ≠ Task DONE
Task DONE ≠ OUT achieved
Task DONE ≠ MERGED ≠ PUSHED ≠ RELEASED ≠ ARTIFACT_PUBLISHED ≠ DEPLOYED
Coordination Claim ≠ Execution Ownership Grant
Task Record observation ≠ Result Acceptance
Result Acceptance ELIGIBLE ≠ Verification PASS
Verification PASS ≠ Verification Validity CURRENT
Revision Set ≠ Input Manifest ≠ Execution State Binding
Resource Identity ≠ Locator ≠ Revision
```

TASK-059 additions:

```text
Runtime Event Journal ≠ Checkpoint ≠ Project Source ≠ canonical Task lifecycle truth
Supervisor decision ≠ AUTH
Supervisor liveness ≠ Execution Ownership Grant
Heartbeat ≠ completion evidence
Runtime control generation ≠ Project authority
Runtime lease / heartbeat = liveness projection (subordinate to ownership evidence)
Runtime fence = stale-runtime-effect rejection mechanism
Effect Permit ≠ AUTH-*
Model proposal ≠ Runtime decision
Model turn lifetime ≠ Worker lifetime ≠ Execution lifetime ≠ Task lifecycle
Checkpoint ≠ canonical runtime journal
Dispatch acknowledgement ≠ resulting-state proof
Cancellation ≠ rollback
Compensation ≠ history erasure
Retry ≠ safe unless effect semantics permit it
Exactly-once execution is not assumed
Task lifetime, model-turn lifetime, and worker lifetime remain separate
```

Framework `1.21.0` implements no AI-ControlTower runtime, Python Supervisor, runtime store/database, event store service, queue, scheduler, worker daemon, Multica runtime, lease/fencing service, distributed lock, automatic transition engine, model/executor router, executable Project Adapter, MCP router, Effect Gateway service, credential broker, sandbox/container runtime, network policy, RLM/recursive executor runtime, merge bot, merge queue, verification daemon, CI runner, API server, automatic Task DONE updater, automatic reconciliation worker, automatic acceptance engine, or automatic continuation engine.

## 3. Durable runtime observation: Runtime Event Journal

Within the execution-runtime domain, the **Runtime Event Journal** is the canonical observation source for execution-control events.

```text
Runtime Event Journal
= canonical observation only inside the execution-runtime domain
≠ Project Source
≠ canonical Task lifecycle truth
≠ Task Record
```

`record_type: RUNTIME_EVENT` is the journal entry:

```yaml
record_type: RUNTIME_EVENT
record_version: "1.0"
event_id: "<durable unique event identity>"
execution_id: "<durable runtime execution id>"
event_sequence: "<monotonic sequence within execution>"
event_class: "<declared runtime event class>"
attempt_ref: "<attempt identity when applicable>"
action_ref: "<action/effect identity when applicable>"
payload_ref: "<minimum durable representation; see Section 17>"
causation_ref: "<cause>"
correlation_ref: "<correlation>"
producer_namespace: "RUNTIME_OWNED"
observed_at: "<timestamp>"
```

Rules:

- The journal is append-oriented. Entries are never rewritten or deleted; correction is a new entry that references the superseded one.
- Journal ordering is by durable `event_sequence`, not by arrival time. Timestamp is audit evidence, not ordering authority (consistent with Wave A V2 transition semantics).
- **Strict writer isolation:** only the runtime-owned control path may append `RUNTIME_OWNED` events. Executors, models, and tool subprocesses cannot directly forge, rewrite, or delete runtime events. Model/tool output that embeds privileged event text is untrusted data (Section 17).
- Duplicate delivery of an already-recorded event is de-duplicated by durable event identity; duplicate observation produces no duplicate effect.
- The journal is runtime-local truth for the execution-runtime domain. It never outranks, replaces, or mutates Project Source, canonical Task lifecycle, AUTH, or source-native system truth.
- A journal continuity gap that cannot be proven resolved fails closed (Section 4).

## 4. Checkpoint / Snapshot

A **Checkpoint** is a derived recovery accelerator over the Runtime Event Journal.

```text
Checkpoint / Snapshot
= derived recovery accelerator
!= Runtime Event Journal
!= Project Source
!= canonical Task lifecycle truth
```

`record_type: EXECUTION_CHECKPOINT`:

```yaml
record_type: EXECUTION_CHECKPOINT
record_version: "1.0"
execution_id: "<execution>"
checkpoint_seq: "<checkpoint sequence>"
event_sequence: "<last included journal event sequence>"
previous_checkpoint_hash: "<previous checkpoint or NOT_APPLICABLE>"
state_version: "<runtime state version>"
resume_cursor: "<deterministic resume location>"
created_at: "<timestamp>"
```

Rules:

- A checkpoint MUST be traceable to the journal sequence it summarizes. A checkpoint that references an `event_sequence` beyond proven journal continuity is invalid and MUST be discarded.
- A checkpoint can be rebuilt or invalidated. It never outranks the journal or source-native truth.
- Recovery SHOULD load a compatible checkpoint and replay the journal tail. If required journal continuity cannot be proven, the runtime MUST fail closed as `RECOVERY_BLOCKED` or equivalent; it MUST NOT reconstruct execution truth from a checkpoint fragment, an LLM transcript, or model memory.
- No historical Task or execution receives an invented checkpoint; unresolvable mapping remains `UNKNOWN.`

## 5. Supervisor and control generation

A **Supervisor** is the declared runtime control path that owns runtime state transitions and scheduling decisions for long-running executions, recovering them across model-turn, worker, process, MCP, and host interruption.

Supervisor authority is bounded:

```text
Supervisor decision != AUTH
Supervisor liveness != Execution Ownership Grant
Heartbeat != completion evidence
Runtime control generation != Project authority
```

A `record_type: RUNTIME_CONTRACT` is the execution-runtime domain's top-level binding for one long-running execution:

```yaml
record_type: RUNTIME_CONTRACT
record_version: "1.0"
contract_ref: "<contract-local reference>"
execution_id: "<durable runtime execution id>"
task_ref: "TASK-xxx"
state_binding_ref: "<Wave A V2 Execution State Binding>"
runtime_contract_version: "<version>"
event_schema_version: "<version>"
control_generation: "<current runtime control generation>"
fence_epoch: "<monotonic epoch within generation>"
liveness:
  lease_mode: "RUNTIME_AUTHORITY_TIME | MONOTONIC_DURATION"
  lease_ref: "<lease identity when applicable>"
continuation_policy:
  continuation_budget: "<finite>"
  retry_budget: "<finite, per action class>"
  wake_conditions: ["<declared wake event / condition>"]
  fallback_check_at: "<time when applicable>"
disposition: "RUNNING | WAIT | BLOCKED | MANUAL_RESOLUTION_REQUIRED | BUDGET_EXHAUSTED | WAITING_FOR_REAUTHORIZATION | RECOVERY_BLOCKED | TERMINATED"
created_at: "<timestamp>"
```

Rules:

- An executor may propose actions or report observations but cannot self-promote runtime state, ownership, or AUTH.
- The end of an LLM turn MUST NOT be interpreted as completion. If an execution remains runnable and non-terminal, the Supervisor may schedule another reasoning step subject to authority, budgets, current truth, and wait/block policy — or persist an explicit wait/blocked disposition (Section 12).
- A **runtime control generation** is the unique successor identity of the runtime control path for an execution domain. A new control generation invalidates prior-generation runtime-local leases, fences, and Effect Permits.
- A control generation change does NOT rewrite the Framework `1.20.0` ownership epoch, the Execution State Binding, or canonical Task state. Ownership epochs remain governed by the Wave A V2 Execution Ownership Grant; the runtime generation is a runtime-local projection (Section 6).
- The `RUNTIME_CONTRACT` references the Wave A V2 Execution State Binding; it never replaces it. It is runtime-domain contract evidence, not Project authority.
- A runtime-store restore to an older snapshot MUST NOT reuse old control identity silently. A new control generation (or equivalent unique successor identity) is required before new effects, and unresolved effects from the former generation are reconciled first (Section 15).
- Recovery sequence on restart/restore: load or establish governed successor generation → validate journal continuity → load compatible checkpoint → replay journal tail → identify expired/lost attempts → reconcile unresolved dispatched effects → invalidate stale leases/fences/permits → re-resolve authority/R4/contract fingerprints → schedule only safely runnable work.

## 6. Runtime liveness projection

A runtime MAY maintain lease/heartbeat state for worker liveness, but this state is **subordinate** to Framework `1.20.0` ownership evidence:

```text
Execution Ownership Grant = governed ownership evidence
runtime lease/heartbeat = liveness projection
runtime fence = stale-runtime-effect rejection mechanism
AUTH = separate authority
```

Rules:

- No lease, heartbeat, or fence can create ownership or AUTH.
- The canonical runtime fence identity is the pair `(runtime_generation, fence_epoch)`. A simple numeric fence comparison across generations is insufficient because an old numeric epoch could reappear after restore. Stale-generation fence attempts are rejected.
- Lease time MUST be based on runtime-authoritative time or equivalent monotonic duration semantics. Executor-local wall clock cannot be lease authority; clock skew is telemetry, not permission.
- Lease expiry invalidates the worker's liveness projection. Effects attempted by a stale worker are rejected by the fence; the possibly-dispatched effect is reconciled before reassignment. Reassignment follows the Wave A V2 Reassignment Gate (`REASSIGNABLE | RESULT_VERIFICATION_REQUIRED | MANUAL_REVIEW_REQUIRED | BLOCKED | UNKNOWN`); loss of liveness never automatically authorizes repeating potentially non-idempotent work.
- The Multica claim remains coordination-only: `Multica claim != runtime lease != runtime fence != Effect Permit != AUTH.`

## 7. Effect Gateway

A **Material Effect** MUST transit the Effect Gateway when the applicable effect policy declares that effect class mediated.

For a mediated effect class, the governed path is:

```text
executor proposal
→ fresh authority / current-truth / precondition evaluation
→ Effect Permit
→ Effect Gateway dispatch
→ source-native reconciliation
```

The Gateway validates at least:

```text
current Operational Execution eligibility
current Attempt identity
current control generation + fence
Task / Plan / Envelope fingerprint validity (Wave A V2 State Binding references)
current applicable AUTH
required R4 current truth
Tool / Capability / Trust eligibility
target identity + target preconditions
effect semantics / idempotency / reconciliation class
remaining budget / retry policy
Effect Permit validity
```

Rules:

- The Gateway does not create authority. It enforces the intersection of already-valid authority and policy at the consequence boundary: `Gateway eligibility != AUTH`; `Effect Permit != AUTH`; `Tool availability != Gateway eligibility.`
- **Effect-surface closure:** for every mediated Material Effect class, every effect-capable surface available to the executor (MCP/tool calls, shell/process execution, network egress, credentials, mounts, sockets, database connections, external SDKs, child processes/recursive agents) MUST be either `MEDIATED_BY_EFFECT_GATEWAY` or `EXPLICITLY_PROHIBITED / CONFINED.` A direct uncontrolled mutation path for a mediated effect class is **non-conforming.** Policy text saying "use the Gateway" without enforceable surface closure is not conformance.
- For mediated Material Effects, raw mutation credentials SHOULD reside at or below the trusted Gateway boundary rather than inside model/RLM workspaces. Credential possession by an unconstrained executor that can bypass the Gateway is an architecture violation for that effect class.
- Framework `1.21.0` does not mandate a specific sandbox, network product, OS security primitive, or broker mechanism; it mandates the effect-surface-closure property.

## 8. Effect Policy

`record_type: EFFECT_POLICY` declares, per effect class, whether mediation is required and the effect's semantics:

```yaml
record_type: EFFECT_POLICY
record_version: "1.0"
policy_ref: "<contract-local reference>"
effect_class: "<declared effect class>"
mediation: "MEDIATED_BY_EFFECT_GATEWAY | EXPLICITLY_PROHIBITED | CONFINED"
idempotency_class: "IDEMPOTENT | CONDITIONALLY_IDEMPOTENT | NON_IDEMPOTENT | UNKNOWN"
reversibility_class: "REVERSIBLE_ATOMIC | COMPENSATABLE | IRREVERSIBLE | UNKNOWN"
reconciliation_class: "NATIVE_READBACK | IDEMPOTENCY_KEY | COMPARE_AND_SET | EXTERNAL_CONFIRMATION | HUMAN_VERIFICATION | NONE"
target_precondition_support: "SUPPORTED | NOT_SUPPORTED | UNKNOWN"
credential_placement: "AT_OR_BELOW_GATEWAY | DECLARED_ALTERNATIVE"
```

Rules:

- One Effect Permit corresponds to one **independently reconcilable Material Effect**, except where the source-native platform provides and the runtime verifies a real atomic transaction making a grouped effect independently reconcilable as one unit.
- Composite intent (for example: commit + push + create PR) is normally decomposed into separate effects with independent action identity, permit, result, reconciliation, and checkpoint boundaries.
- Where a target does not provide a usable precondition primitive, the policy MUST record that limitation explicitly and use the applicable reconciliation/fail-closed strategy rather than silently assuming target freshness.

## 9. Effect Permit

For every Gateway-mediated Material Effect, a conforming runtime mints a short-lived **Effect Permit** only after fresh validation at the effect boundary.

`record_type: EFFECT_PERMIT`:

```yaml
record_type: EFFECT_PERMIT
record_version: "1.0"
permit_id: "<unique id>"
execution_id: "<execution id>"
attempt_id: "<attempt id>"
action_id: "<action id>"
action_hash: "<canonical action fingerprint>"
target_ref: "<exact governed target>"
tool_ref: "<eligible effect tool>"
runtime_generation: "<control generation>"
fence_epoch: "<epoch within generation>"
ownership_epoch: "<Wave A V2 ownership epoch>"
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
short-lived
single-use
non-transferable
bound to execution / attempt / action identity
bound to exact target / tool / effect digest
bound to applicable ownership epoch and runtime control generation
never equivalent to AUTH-*
```

Rules:

- The transition `PERMIT_ACTIVE → PERMIT_CONSUMED` MUST be atomic/compare-and-set equivalent. Reuse, transfer, action mismatch, target mismatch, stale generation, stale fence, or expiry produces **rejection**, not fallback inference.
- `PERMIT_CONSUMED` proves only that dispatch eligibility was consumed; it does not prove that the external effect was applied.
- Fresh AUTH/R4/fence/target checks SHOULD occur as close as practical to dispatch. A long-lived queue approval MUST NOT be treated as proof that mutable prerequisites remain valid at effect time.

## 10. Target preconditions and TOCTOU control

A model may reason over state that changes before dispatch. Material Effects MUST declare source-native target preconditions whenever the target supports them, for example:

```text
Git exact ref/SHA
ETag / If-Match
resource_version / generation
row version
object hash
compare-and-set token
immutable candidate identity
```

Rules:

- A stale precondition yields `PRECONDITION_CONFLICT` or equivalent fail-closed result and requires refresh/replanning as applicable. The runtime MUST NOT silently dispatch against a materially different target.
- Where the target does not support a usable precondition, the Effect Policy records the limitation and the runtime uses the applicable reconciliation/fail-closed strategy (Section 11).

## 11. Effect semantics classes

The runtime classifies effect semantics along two independent axes:

**Idempotency class:** `IDEMPOTENT | CONDITIONALLY_IDEMPOTENT | NON_IDEMPOTENT | UNKNOWN.`

**Reversibility class:** `REVERSIBLE_ATOMIC | COMPENSATABLE | IRREVERSIBLE | UNKNOWN.`

Possible strategies: `NATIVE_IDEMPOTENCY_KEY | COMPARE_AND_SET | SOURCE_READBACK | EXTERNAL_CONFIRMATION | MANUAL_VERIFICATION | NONE.`

Framework `1.21.0` MUST NOT claim arbitrary exactly-once execution across external systems. The required guarantee is narrower and defensible:

```text
no blind duplicate Material Effect
+ deterministic ambiguity handling
+ source-native / result reconciliation where available
```

## 12. Ambiguous effects and reconciliation

The Wave A V2 `RESULT_VERIFICATION_REQUIRED` / verify-before-retry semantics remain binding and are extended for the runtime domain.

If a connection/process fails after dispatch may have occurred, absence of acknowledgement MUST NOT be normalized to failure. After a possibly-dispatched Material Effect with unknown result:

```text
UNKNOWN
→ reconcile at source-native truth owner
→ APPLIED | NOT_APPLIED | PARTIAL | STILL_UNKNOWN
```

Rules:

- Reconciliation classes: `NATIVE_READBACK | IDEMPOTENCY_KEY | COMPARE_AND_SET | EXTERNAL_CONFIRMATION | HUMAN_VERIFICATION | NONE.`
- For `NON_IDEMPOTENT | UNKNOWN` effects with `reconciliation: NONE`, an ambiguous result MUST become `STILL_UNKNOWN` with `MANUAL_RESOLUTION_REQUIRED` or another explicit blocking state. **Automatic retry is prohibited.**
- Unsafe blind retry is prohibited for every effect class. Idempotency keys, target preconditions, and source-native reconciliation are used where the target supports them.
- `ACKNOWLEDGED` is transport/protocol observation only and MUST NOT be treated as resulting-state proof when the source-native system requires readback/reconciliation.

## 13. Durable continuation, wait, and bounded autonomy

Runtime continuation is governed by durable execution state rather than model memory.

A conforming runtime declares:

```yaml
continuation_policy:
  continuation_budget: "<finite>"
  retry_budget: "<finite, per action class>"
  wake_conditions: ["<declared wake event / condition>"]
  fallback_check_at: "<time when applicable>"
```

Runtime dispositions include at least:

```text
WAIT
BLOCKED
MANUAL_RESOLUTION_REQUIRED
BUDGET_EXHAUSTED
WAITING_FOR_REAUTHORIZATION
```

Rules:

- No invisible infinite loop: fail-closed behavior MUST NOT become unbounded retry/spin. Transient/recoverable conditions use `WAIT` with bounded retry policy; external-truth conditions use `WAIT` with a wake condition; human-resolution conditions use `BLOCKED / MANUAL_RESOLUTION_REQUIRED`; unresolvable ambiguity uses `BLOCKED.`
- No automatic continuation after authority invalidation, state-binding invalidation, or contract invalidation. A materially changed pinned Task Contract / Plan Contract / Execution Envelope invalidates the active execution or requires governed replanning/revalidation; the runtime MUST NOT silently hot-swap success semantics into an active execution.
- Budget exhaustion persists a truthful state such as `BUDGET_EXHAUSTED`, `BLOCKED`, or `WAITING_FOR_REAUTHORIZATION` as applicable and MUST NOT imply Task DONE.
- Retry policy belongs to the deterministic runtime. A model `REQUEST_RETRY` does not itself authorize a retry.
- Task lifetime, model-turn lifetime, and worker lifetime remain separate.

## 14. RLM / recursive execution profile

Framework `1.21.0` defines a **provider-neutral RLM/recursive-executor profile contract** sufficient for a future reference runtime. It requires no specific RLM implementation, model provider, or product.

`record_type: RLM_EXECUTION_PROFILE`:

```yaml
record_type: RLM_EXECUTION_PROFILE
record_version: "1.0"
profile_ref: "<contract-local reference>"
max_recursion_depth: "<n>"
hierarchical_budget:
  parent_consumption_plus_child_allocations: "<= root budget>"
child_state_binding: "EXACT_PARENT_EXECUTION_INPUTS_AND_ALLOWED_SCOPE"
result_handoff: "EXPLICIT_AND_AUDITABLE"
gateway_bypass: "PROHIBITED"
parent_cancellation_propagation: "FAIL_CLOSED"
```

Rules:

- `max_recursion_depth` is normative. A child at the depth limit cannot spawn further children; violation fails closed with a truthful blocking state.
- Budgets are hierarchical **allocations**, not cloned allowances: `parent consumption + sum(child allocations) <= root budget.` A child execution **cannot mint new authority or budget** by recursion.
- Each child is state-bound to the exact parent execution inputs and allowed scope.
- Recursive result handoff is explicit and auditable.
- Recursive execution **cannot bypass Effect Gateway requirements** at any depth.
- Parent cancellation/authority revocation **propagates fail-closed** according to the declared contract: children stop new governed dispatches, reconcile in-flight effects, and record truthful resulting state.
- Budget exhaustion at any level persists a truthful state and MUST NOT imply Task DONE.

## 15. Cancellation and compensation

Cancellation prevents new governed effects but does not erase already-applied external state.

```text
Cancellation != rollback
Compensation != history erasure
```

Rules:

- If cancellation occurs while actions are in flight: (1) stop new dispatches covered by the cancelled authority/scope; (2) mark applicable attempt/execution cancellation state truthfully; (3) reconcile every possibly-dispatched Material Effect; (4) record resulting source-native truth even when the canonical Task is `CANCELLED`; (5) run compensation only when separately governed and permitted.
- A dispatched effect may still become `APPLIED` after cancellation. That fact is preserved rather than falsified to match lifecycle intent.
- **Compensation is a new governed effect**, not history erasure. For a compensatable effect, the compensation action has its own action identity, authority check, Effect Permit, budget, evidence, and reconciliation.
- If compensation fails, the runtime records truthful partial state such as `PARTIALLY_COMPENSATED` rather than claiming `ROLLED_BACK` unless the source-native system proves an actual atomic rollback. Partial compensation must remain truthful.

## 16. Runtime version pinning and recovery

Long-running executions bind to explicit runtime-contract and event-schema versions:

```yaml
runtime_execution_pin:
  runtime_contract_version: "<version>"
  event_schema_version: "<version>"
```

Rules:

- A runtime deployment upgrade classifies active executions as:

```text
BACKWARD_COMPATIBLE
REQUIRES_MIGRATION
INCOMPATIBLE
```

- `BACKWARD_COMPATIBLE` may continue under the pinned semantics. `REQUIRES_MIGRATION` requires quiesce/migration/verification/resume. `INCOMPATIBLE` blocks continuation until governed resolution.
- Incompatible runtime code MUST NOT silently reinterpret historical runtime events.
- Process restart does not terminate the Task or Execution; recovery follows the Section 5 sequence.

## 17. Security boundary

Framework `1.21.0` requires:

- **No raw secret values** in Project Source, runtime journal, checkpoint, or evidence. For sensitive arguments/results, the runtime uses the minimum durable representation sufficient for reconciliation: `REFERENCE_ONLY | REDACTED | HASH_ONLY | classified metadata.` Credential references may be persisted when governed; raw secret values MUST NOT be written merely for observability.
- **Executor/model output remains untrusted input.** Prompt injection or malicious tool output cannot create AUTH, ownership, permits, verification, or Task completion.
- **Runtime-owned authoritative events use a separate namespace** from model/tool proposals. An executor may produce bounded proposal/report types; it MUST NOT be able to create authoritative runtime events (for example: `AUTH_GRANTED`, `LEASE_ACQUIRED`, `FENCE_ADVANCED`, `PERMIT_ISSUED`, `VERIFIED`, `INTEGRATED`, `TASK_DONE`). Typed protocol parsing MUST fail closed on unknown privileged fields rather than treating model-generated state as trusted runtime metadata.
- **Effect-capable credentials are inaccessible to unconstrained executor paths** when the effect class requires Gateway mediation (Section 7).
- **Stale control generation / ownership epoch / permit attempts fail closed.**
- Even a compromised executor must still pass Effect Gateway authority/envelope/trust/fence/precondition checks, provided effect-surface closure is actually enforced.

Cryptographic producer identity, transport mTLS/key rotation, and a full authenticated event-envelope protocol may be added only if implementation evidence shows they are required for the selected deployment model; they are not silently assumed by this amendment.

## 18. AI-ControlTower Python Supervisor conformance handoff

TASK-059 defines the **conformance boundary** for a later AI-ControlTower executable implementation. It does not place runtime source in ProjectFramework.

Expected AI-ControlTower reference implementation direction (implementation choices remain AI-ControlTower's):

```text
Python 3.14
Supervisor service/library
durable runtime store
Runtime Event Journal
checkpoint/replay
Effect Gateway
Effect Permit validation
bounded continuation/budget engine
RLM/recursive executor adapter
source-native reconciliation adapters
```

The exact storage engine, queue, process model, and deployment topology remain AI-ControlTower implementation choices.

Expected consumers (cross-cutting contract input, not a replacement for the AI-ControlTower package sequence):

```text
Package C: long-running Workforce/Harness/operator runtime integration where applicable
Package D: Work / Approval / Capability execution plane and bounded Material Effects
Package E: recovery, replay prevention, quarantine, and durable recovery evidence
later Prime Agent / RLM implementation: autonomous long-horizon operator execution
```

Existing AI-ControlTower Package B state and verified history MUST NOT be rewritten by TASK-059.

**Prime Agent mapping boundary:** AI-ControlTower MAY map its candidate `Prime Agent = Autonomous / Long-Horizon Operator` role to the TASK-059 RLM/long-horizon Executor Profile if that candidate is separately promoted in AI-ControlTower.

```text
Prime Agent role != ProjectFramework dependency
Prime Agent role != authority
RLM execution != autonomous permission to mutate
```

TASK-059 MUST remain valid when Prime Agent is absent or replaced.

**Separate implementation Task:** the actual Python 3.14 runtime implementation (Supervisor reference runtime, RLM/recursive Executor adapter, Effect Gateway integration) is a **separate AI-ControlTower Task**, separately authorized, with its own Task Ready Gate and verification.

**Evidence required before canonical-source cutover can start:**

```text
1. TASK-059 release verified (AFFECTED + independent review + one RELEASE_FULL on unchanged candidate) and published as applicable
2. AI-ControlTower Python Supervisor reference runtime implemented under a separate AI-ControlTower Task
3. AI-ControlTower runtime verified against the TASK-059 conformance boundary (journal/checkpoint recovery, permit validation, generation/fence rejection, ambiguous-effect reconciliation, RLM budget/depth enforcement, security boundary)
4. AI-ControlTower runtime handoff accepted by ACTOR-001
5. standalone ProjectFramework self-host reconciled to the final Framework baseline
```

Only after those facts is a separate governed Cutover Task eligible to promote `AI-ControlTower/projectframework/` as the canonical development source and convert the standalone ProjectFramework repository to a read-only mirror/archive.

## 19. Compatibility and exclusions

Framework `1.21.0` is an additive successor to Framework `1.20.0`:

- Project Source Schema remains `1.0.0`; existing Framework `1.20.0` records remain valid.
- No historical record is retrofitted with invented journal, checkpoint, permit, or RLM state; unresolvable mapping remains `UNKNOWN.`
- Projects that do not use an execution runtime remain valid ProjectFramework Projects.
- AI-ControlTower adoption remains separately governed.
- Brownfield Projects adopt the final release only through governed `[Project Upgrade].`
- Wave A V2 exclusions remain in force: Release Transaction, deployment saga, and multi-system transactional release semantics (Wave C) are NOT included. Cryptographic producer authentication remains excluded unless implementation evidence requires it (Section 17).
- If implementation discovers a required breaking schema/authority change, the release classification and target version MUST be re-planned before mutation.

New TASK-059 record types use `record_version: "1.0"`: `RUNTIME_CONTRACT`, `RUNTIME_EVENT`, `EXECUTION_CHECKPOINT`, `EFFECT_POLICY`, `EFFECT_PERMIT`, `RLM_EXECUTION_PROFILE.` No existing record type's serialized meaning is redefined.

TASK-059 ships governance/documentation contracts and maintained starters only. It adds no task database, event store, queue, scheduler, worker daemon, lease/fencing service, distributed lock, fencing-token generator, runtime CAS store, automatic transition engine, model router, automatic acceptance engine, verification daemon, executable Project Adapter, API server, merge bot, or automatic Task-DONE updater. `Task DONE ≠ MERGED ≠ PUSHED ≠ RELEASED ≠ ARTIFACT_PUBLISHED ≠ DEPLOYED.` `R4_CTX ≠ Risk R4` (Risk remains exactly `R0–R3`).

## 20. Integrated pressure-scenario contract

This amendment is accepted only together with pressure scenarios `591–620` in `tests/pressure-scenarios.md`, which cover the TASK-059 design-level scenario classes: worker/process death, runtime restart, checkpoint corruption/consistency, event duplication/order, liveness expiry, Effect Gateway mediation, stale/replayed permits, ambiguous non-idempotent effects, authority/current-truth changes at dispatch, runtime-store rollback/control-generation reuse, cancellation/compensation, RLM recursion depth and hierarchical budgets, malicious tool output, Prime-Agent-optional mapping, version pinning, budget exhaustion, and non-terminal model-turn end — while preserving cumulative scenarios `1–620` contiguous/unique and the Wave A V2 scenarios `557–590` unchanged.

## 21. Completion and review gate

This amendment is `CONTRACT_READY` (not `IMPLEMENTED`, not `RELEASED`) when:

```text
spec Sections 1–12 explicitly approved
+ written spec self-review passes
+ Framework 1.20 baseline proven exact (1.20.0 / 1.0.0 / format 3)
+ V3 collision matrix: retained / already-satisfied / rejected complete
+ no Wave A V2 semantic duplication (Compositional State Binding Hub preserved authoritative)
+ no authority leakage (lease/heartbeat/fence/permit/generation never create ownership or AUTH)
+ no unsafe retry path (blind retry prohibited; ambiguity reconciles at source-native owner)
+ no permit replay/transfer path (single-use, bound, atomic consumption)
+ no stale-worker effect path (generation-paired fence; reassignment gate)
+ no secret persistence path (journal/checkpoint/evidence secret-free)
+ no model-forged runtime event path (separate namespace; fail-closed parsing)
+ no RLM budget/authority minting path (hierarchical allocation; depth bound)
+ Prime Agent remains optional mapping (contract valid with Prime Agent absent)
+ no AI-ControlTower runtime code in ProjectFramework
+ no canonical-source cutover performed
+ no new Project Source semantic slot, Stable-ID family, Registered Command, or Risk level
+ no historical record retrofit
+ no runtime implementation is introduced
```

`CONTRACT_READY ≠ IMPLEMENTED ≠ RELEASED.` Local implementation authority does not imply push, PR, merge, tag, GitHub Release, or canonical self-host promotion.
