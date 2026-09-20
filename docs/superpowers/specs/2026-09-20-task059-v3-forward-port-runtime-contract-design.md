# TASK-059 — V3 Forward-Port Runtime Contract & AI-ControlTower Handoff Design

Date: `2026-09-20` (Asia/Bangkok)
Task: `TASK-059`
Design state: `USER_APPROVED_DIRECTION / WRITTEN_SPEC_SELF_REVIEWED / EXPLICIT_WRITTEN_SPEC_APPROVAL_PENDING`
Depends on: `TASK-058`
Baseline: ProjectFramework `1.20.0` / Project Source Schema `1.0.0` / release format `3`
Candidate target: ProjectFramework `1.21.0` / Project Source Schema `1.0.0` / release format `3`

## 1. Goal

Forward-port the still-useful parts of the superseded TASK-058 Design V3 onto the verified Framework 1.20 Wave A V2 baseline, without reviving the old V3 branch or overwriting TASK-058 history.

TASK-059 is intended to be the final standalone ProjectFramework feature line before a separately governed canonical-source cutover into AI-ControlTower.

The design principle is:

```text
Framework 1.20 Wave A V2 remains authoritative.
TASK-059 adds only missing runtime-control semantics.
ProjectFramework defines protocol law; it does not host the executable AI-ControlTower runtime.
AI-ControlTower will own the Python Supervisor / RLM runtime implementation under a separate execution task.
Canonical-source cutover happens only after TASK-059 is verified and the AI-ControlTower runtime handoff is accepted.
```

## 2. Lineage and supersession rule

Historical Design V3 remains preserved at:

`docs/superpowers/specs/2026-09-16-task058-deterministic-execution-runtime-contract-design.md`

It is source material only. TASK-059 MUST NOT:

- reactivate `task058-framework120` or `task058/framework-1.20-deterministic-runtime`;
- reuse the old V3 scenario numbering `557–602`;
- rewrite TASK-058 Design of Record;
- reinterpret Framework 1.20 Wave A V2 records in place;
- downgrade or replace `Compositional State Binding Hub`.

Every retained V3 concept must be reconciled explicitly against Framework 1.20 before becoming normative.

## 3. Framework 1.20 contracts that remain authoritative

TASK-059 inherits without replacement:

- Revision Set and Stable Resource Identity;
- Execution Input Manifest;
- immutable Execution State Binding;
- Execution Ownership Grant / Evidence and scoped ownership epoch;
- fencing assurance ordering `COORDINATION_ONLY < ACCEPTANCE_FENCED < SIDE_EFFECT_FENCED`;
- versioned/CAS Operational Transition semantics and idempotency;
- Result Observation separate from Result Acceptance;
- Generic Result Identity / Result Set;
- Verification Result separate from Verification Validity;
- fresh `ELIGIBLE` Result Acceptance before promotable verification;
- Brownfield no-retrofit rules;
- `PLAN | TASK | VERIFY`, `R4_CTX`, Task Ready Gate, Executor Profile, Project Adapter and `INTEGRATION_GATE`.

TASK-059 MUST extend these contracts compositionally rather than create parallel equivalents.

## 4. New runtime-control semantics owned by TASK-059

### 4.1 Durable runtime observation

Define a language-neutral Runtime Event Journal for execution-control observations.

```text
Runtime Event Journal
= canonical observation only inside the execution-runtime domain

Checkpoint / Snapshot
= derived recovery accelerator
!= Runtime Event Journal
!= Project Source
!= canonical Task lifecycle truth
```

A checkpoint can be rebuilt or invalidated. It never outranks the journal or source-native truth.

### 4.2 Supervisor and control generation

Define a Supervisor contract that can recover long-running executions across model-turn, worker, process, MCP and host interruption.

Supervisor authority is bounded:

```text
Supervisor decision != AUTH
Supervisor liveness != Execution Ownership Grant
Heartbeat != completion evidence
Runtime control generation != Project authority
```

A new control generation invalidates prior runtime-local leases, permits and stale worker liveness state. It does not rewrite the Framework 1.20 ownership epoch or canonical Task state.

### 4.3 Runtime liveness projection

A runtime MAY maintain lease/heartbeat state for worker liveness, but this state is subordinate to Framework 1.20 ownership evidence.

```text
Execution Ownership Grant = governed ownership evidence
runtime lease/heartbeat = liveness projection
runtime fence = stale-runtime-effect rejection mechanism
AUTH = separate authority
```

No lease, heartbeat or fence can create ownership or AUTH.

### 4.4 Effect Gateway and Effect Permit

Add a governed Material-Effect mediation contract.

For effect classes declared as mediated:

```text
executor proposal
-> fresh authority/current-truth/precondition evaluation
-> Effect Permit
-> Effect Gateway dispatch
-> source-native reconciliation
```

Effect Permit properties:

- short-lived;
- single-use;
- non-transferable;
- bound to execution/attempt/action identity;
- bound to exact target/tool/effect digest;
- bound to applicable ownership epoch and runtime control generation;
- never equivalent to `AUTH-*`.

Direct uncontrolled mutation paths for a mediated effect class are non-conforming.

### 4.5 Ambiguous effects and reconciliation

TASK-059 prohibits arbitrary exactly-once claims.

After a possibly-dispatched Material Effect with unknown result:

```text
UNKNOWN
-> reconcile at source-native truth owner
-> APPLIED | NOT_APPLIED | PARTIAL | STILL_UNKNOWN
```

Unsafe blind retry is prohibited. Idempotency keys, target preconditions and source-native reconciliation are used where the target supports them.

### 4.6 Durable continuation, wait and bounded autonomy

Runtime continuation is governed by durable execution state rather than model memory.

Define:

- finite continuation budget;
- retry budget;
- wake conditions;
- explicit `WAIT`, `BLOCKED`, `MANUAL_RESOLUTION_REQUIRED` or equivalent runtime dispositions;
- no invisible infinite loop;
- no automatic continuation after authority, state-binding or contract invalidation.

Task lifetime, model-turn lifetime and worker lifetime remain separate.

### 4.7 RLM / recursive execution profile

TASK-059 defines a provider-neutral RLM/recursive-executor profile contract sufficient for a future Python reference runtime.

Required semantics include:

- `max_recursion_depth`;
- hierarchical child budgets;
- child execution cannot mint new authority or budget;
- each child is state-bound to exact parent execution inputs and allowed scope;
- recursive result handoff is explicit and auditable;
- recursive execution cannot bypass Effect Gateway requirements;
- parent cancellation/authority revocation propagates fail-closed according to the declared contract.

ProjectFramework does not require a specific RLM implementation or model provider.

### 4.8 Prime Agent mapping boundary

AI-ControlTower MAY map its candidate `Prime Agent = Autonomous / Long-Horizon Operator` role to the TASK-059 RLM/long-horizon Executor Profile if that candidate is separately promoted in AI-ControlTower.

```text
Prime Agent role != ProjectFramework dependency
Prime Agent role != authority
RLM execution != autonomous permission to mutate
```

TASK-059 must remain valid when Prime Agent is absent or replaced.

### 4.9 Cancellation and compensation

Cancellation prevents new governed effects but does not erase already-applied external state.

```text
Cancellation != rollback
Compensation != history erasure
```

Compensation is a new governed effect with its own authority, permit, evidence and reconciliation. Partial compensation must remain truthful.

### 4.10 Runtime version pinning and recovery

Long-running executions bind to explicit runtime-contract and event-schema versions.

A runtime upgrade classifies active executions as:

```text
BACKWARD_COMPATIBLE
REQUIRES_MIGRATION
INCOMPATIBLE
```

Incompatible runtime code may not silently reinterpret historical runtime events.

## 5. Python Supervisor reference-runtime handoff

TASK-059 defines the conformance boundary for a later AI-ControlTower executable implementation. It does not place runtime source in ProjectFramework.

Expected AI-ControlTower reference implementation direction:

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

The exact storage engine, queue, process model and deployment topology remain AI-ControlTower implementation choices.

## 6. Relationship to AI-ControlTower packages

TASK-059 is a cross-cutting contract input, not a replacement for the AI-ControlTower package sequence.

Expected consumers:

- Package C: long-running Workforce/Harness/operator runtime integration where applicable;
- Package D: Work / Approval / Capability execution plane and bounded Material Effects;
- Package E: recovery, replay prevention, quarantine and durable recovery evidence;
- later Prime Agent/RLM implementation: autonomous long-horizon operator execution.

Existing Package B state and verified history must not be rewritten by TASK-059.

## 7. Security boundary

TASK-059 requires:

- no raw secret values in Project Source, runtime journal, checkpoint or evidence;
- executor/model output remains untrusted input;
- runtime-owned authoritative events use a separate namespace from model proposals;
- effect-capable credentials are inaccessible to unconstrained executor paths when the effect class requires Gateway mediation;
- stale control generation / ownership epoch / permit attempts fail closed;
- malicious tool output cannot create AUTH, ownership, permit, verification or Task completion.

Cryptographic producer identity, transport mTLS/key rotation and a full authenticated event-envelope protocol may be added only if implementation evidence shows they are required for the selected deployment model; they are not silently assumed by this design.

## 8. Compatibility

TASK-059 is intended as an additive successor to Framework 1.20.

- Project Source Schema remains `1.0.0` unless implementation proves a breaking requirement.
- Existing Framework 1.20 records remain valid.
- No historical record is retrofitted with invented journal, checkpoint, permit or RLM state.
- Projects that do not use an execution runtime remain valid ProjectFramework Projects.
- AI-ControlTower adoption remains separately governed.
- Brownfield Projects adopt the final release only through governed `[Project Upgrade]`.

If implementation discovers a required breaking schema/authority change, the release classification and target version must be re-planned before mutation.

## 9. Candidate Framework surfaces

Expected ProjectFramework surfaces include:

- a new TASK-059 governance amendment;
- Core Governance projection;
- SKILL operational guidance;
- Project-Execution README;
- runtime-contract starter;
- runtime-event-journal starter;
- execution-checkpoint starter;
- effect-policy / Effect Permit starter;
- RLM Executor Profile starter or explicit extension of the current Executor Profile;
- pressure scenarios allocated strictly after current scenario 590;
- Framework release/migration metadata;
- maintained starter version propagation only where required.

The implementation plan must collision-check exact paths and versions before mutation.

## 10. Verification contract

Required verification includes:

1. fresh Framework 1.20 exact baseline;
2. RED-first pressure scenarios using only numbers greater than 590;
3. explicit proof that Wave A V2 semantics are preserved rather than duplicated;
4. no new Project Source authority, Stable-ID family, Risk level or canonical Task lifecycle;
5. no executable AI-ControlTower runtime code committed to ProjectFramework;
6. provider-neutral RLM contract;
7. Prime Agent remains optional mapping only;
8. stale-worker / ambiguous-effect / permit-replay / runtime-restart / budget-exhaustion pressure coverage;
9. cumulative AFFECTED verification;
10. independent fresh-context review;
11. exactly one final RELEASE_FULL on the unchanged candidate;
12. state-bound evidence and terminal reconciliation.

## 11. Standalone ProjectFramework closure boundary

TASK-059 does not perform canonical-source cutover.

After TASK-059 is verified, published as applicable, self-host reconciled, and the AI-ControlTower runtime handoff is accepted:

```text
standalone ProjectFramework feature development = FROZEN
next ProjectFramework mutation = cutover/reconciliation only
```

A separate governed Cutover Task will:

- upgrade AI-ControlTower to the final Framework baseline;
- create/promote `AI-ControlTower/projectframework/` as canonical development source;
- verify one-source-of-truth ownership;
- convert the standalone ProjectFramework repository to a read-only distribution mirror / historical archive.

## 12. Explicit exclusions

TASK-059 does not authorize:

- Python Supervisor source implementation in ProjectFramework;
- AI-ControlTower source/runtime mutation;
- Prime Agent installation/deployment;
- RLM provider deployment;
- production deployment;
- canonical-source cutover;
- repository archival;
- destructive branch/worktree deletion;
- push/PR/merge/tag/GitHub Release without separately applicable authority.

## 13. Self-review result

`TASK059_SPEC_PLAN_SELF_REVIEW 12/12 PASS` — Framework 1.20 baseline confirmed; TASK-059 registration unique; current pressure-scenario ceiling confirmed at 590; proposed runtime starter paths do not collide with current Project-Execution files; no TBD/FIXME/placeholders; Wave A V2 authority preserved; historical V3 remains source-only; Prime Agent remains optional mapping; AI-ControlTower runtime code remains excluded from ProjectFramework; Package C/D/E handoff aligns with current R027 direction; candidate 1.21 remains conditional; diff hygiene passes.

## 14. Exact next design step

Obtain explicit written-spec approval for this self-reviewed TASK-059 spec before implementation-plane mutation.
