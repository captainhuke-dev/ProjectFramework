# TASK-058 Deterministic Execution Runtime Contract Implementation Plan

> **Execution handoff:** `GPT = PLANNER / EXECUTION_HANDOFF_REQUIRED` after this plan is complete. Planning completion does not assign execution. The approved plan MUST be handed to the applicable execution-control layer, which resolves the current Task Contract, Execution Envelope, AUTH, `R4_CTX`, capability/tool/trust/executor policy, and Task Ready Gate before selecting an eligible Executor. `Planner ≠ Executor ≠ Verifier`; independent Verifier selection remains separate when applicable.
>
> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement ProjectFramework `1.20.0` deterministic execution-runtime governance contracts for long-running AI-ControlTower-compatible work without implementing an AI-ControlTower runtime.

**Architecture:** Extend Framework `1.19.0` declarative PLAN/TASK/VERIFY contracts with language-neutral runtime-control semantics: separate Task/Execution/Attempt/Action domains, canonical runtime journal + derived checkpoints, lease/heartbeat/fencing/control-generation semantics, atomic runtime transitions, an Effect Gateway contract with effect-surface closure and single-use Effect Permits, deterministic ambiguity/reconciliation rules, durable hierarchical budgets, typed executor proposals, cancellation/compensation, and version-pinned recovery. ProjectFramework defines protocol semantics only; source-native systems retain factual authority, canonical Task ownership remains unchanged, and future runtime services remain separate scope.

**Tech Stack:** Markdown, YAML, Git, scratch Python 3 for verification only; no committed executable runtime/validator/daemon/service.

**Spec:** `docs/superpowers/specs/2026-09-16-task058-deterministic-execution-runtime-contract-design.md` — `ACTOR-001 EXPLICIT WRITTEN-SPEC APPROVAL / 2026-09-16`.

## Global Constraints

- Target Framework `1.20.0`; Project Source Schema `1.0.0`; release format `3`.
- Candidate release classification: `BACKWARD_COMPATIBLE_ADDITIVE_RUNTIME_CONTRACT`; reclassify rather than forcing `1.20.0` if implementation reveals a breaking contract/schema requirement.
- TASK-057 remains authoritative for PLAN/TASK/VERIFY, `R4_CTX`, Task Ready Gate, Operational Execution state, Expected/Actual IPOCV, Verification Record, Multica coordination-only boundary, exact-candidate verification, `INTEGRATION_GATE`, and Task DONE ownership.
- Canonical Task lifecycle remains exactly `TODO | IN_PROGRESS | DONE | BLOCKED | CANCELLED`.
- Risk remains `R0–R3`; `R4_CTX` remains current-truth context, not Risk R4.
- Keep four truth/lifecycle domains distinct: canonical Task lifecycle; Operational Execution state; Execution Attempt state; Action/Effect state.
- `Runtime decision ≠ Authority`; `Claim ≠ Lease ≠ Fence ≠ Authority`; `Effect Permit ≠ AUTH`; `Heartbeat ≠ completion evidence`.
- Runtime Event Journal is canonical only inside the runtime execution-control domain; Checkpoint/Snapshot is derived recovery state and never outranks the Journal.
- Effect-surface closure is mandatory for autonomous mediated Material Effects: every governed effect-capable path is `MEDIATED_BY_EFFECT_GATEWAY` or explicitly prohibited/confined.
- Every Gateway-mediated Material Effect requires a fresh short-lived Effect Permit; Permit is single-use, non-transferable, attempt/action/action-hash/target/tool/generation/fence/contract/envelope-bound.
- One Permit maps to one independently reconcilable Material Effect unless a verified source-native atomic transaction makes the group one independently reconcilable unit.
- Material Effects declare source-native target preconditions whenever supported; unsupported preconditions are explicit and route to reconciliation/fail-closed handling rather than assumed freshness.
- Do not claim arbitrary exactly-once execution. Required guarantee is no blind duplicate Material Effect plus deterministic ambiguity handling and source-native/result reconciliation where available.
- `Cancellation ≠ rollback`; compensation is a separately governed Material Effect with its own identity/AUTH/Permit/evidence/reconciliation.
- Control identity is `(runtime_generation, fence_epoch)`; a new generation invalidates old leases/fences/permits and requires unresolved-effect reconciliation.
- Runtime state transitions require `state_version` compare-and-set or equivalent atomic semantics; no database/consensus product is mandated.
- Model/executor proposals and runtime-owned events use separate namespaces; models cannot emit authoritative `AUTH_GRANTED`, `LEASE_ACQUIRED`, `FENCE_ADVANCED`, `PERMIT_ISSUED`, `VERIFIED`, `INTEGRATED`, or `TASK_DONE` events.
- Budgets are durable and hierarchical; child/RLM recursion cannot manufacture budget or authority.
- Durable journal/checkpoint/evidence surfaces never persist raw secret values merely for observability.
- Runtime/event-schema semantics are version-pinned for active executions; incompatible runtime upgrades cannot silently reinterpret old journal events.
- No new Project Source semantic slot or Stable-ID family.
- Brownfield historical Tasks are not silently retrofitted with runtime artifacts.
- Pressure scenarios are RED-first and allocate exactly the contiguous range `557–602` unless a design-preserving split keeps all semantic classes explicit and the final numbering contiguous.
- One final `RELEASE_FULL` runs on the unchanged frozen candidate; candidate-invalidating changes require a new candidate and new final run.
- Push/PR/merge/tag/GitHub Release/self-host promotion/consumer upgrade/AI-ControlTower mutation remain separately governed.
- TASK-058 MUST NOT implement an AI-ControlTower runtime service, Python supervisor, runtime database, scheduler/queue/worker daemon, lease/fencing service, Effect Gateway service, credential broker, sandbox/container/network policy, MCP/model router, RLM runtime, Multica runtime, automatic Task DONE updater, CI/merge/release bot, API server, or self-improvement runtime.

---

### Task 1: Add RED pressure scenarios 557–602

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`

**Interfaces:**
- Consumes: approved spec §§2–33 and TASK-057 scenario baseline `1–556`.
- Produces: executable-by-review RED contract for all TASK-058 runtime/effect-control semantics before normative implementation.

- [ ] **Step 1: Append scenarios `557–602` with exact semantic coverage**

Add the following scenario classes in this order, keeping headings contiguous and unique:

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

Each scenario must state `Prompt`, `Temptation`, `Pass`, `Fail`, and `GREEN expectation`. Pass/Fail wording must enforce the frozen Design V3 invariants rather than merely mention the feature name.

- [ ] **Step 2: Verify scenario continuity before production changes**

Run scratch Python from repository root:

```bash
python - <<'PY'
import re
from pathlib import Path
p = Path('Framework-Source/tests/pressure-scenarios.md')
text = p.read_text(encoding='utf-8')
nums = [int(x) for x in re.findall(r'^## Scenario (\d+)\b', text, re.M)]
assert nums == list(range(1, 603)), (nums[-10:], len(nums))
assert len(nums) == len(set(nums)) == 602
print('TASK058_SCENARIO_CONTINUITY 602/602 PASS')
PY
```

Expected: `TASK058_SCENARIO_CONTINUITY 602/602 PASS`.

- [ ] **Step 3: Run a RED token probe against current production surfaces**

Probe `Framework-Source/references/core-governance-rules.md` and `Framework-Source/templates/project-execution/` for these required production tokens/semantics:

```text
runtime_generation
fence_epoch
Effect Permit
MEDIATED_BY_EFFECT_GATEWAY
PERMIT_CONSUMED
PRECONDITION_CONFLICT
MANUAL_RESOLUTION_REQUIRED
Runtime Event Journal
state_version
CANDIDATE_COMPLETE
max_recursion_depth
PARTIALLY_COMPENSATED
event_schema_version
```

Expected before implementation: at least one required TASK-058 production semantic is missing, so the RED probe reports failure while scenario continuity remains PASS.

- [ ] **Step 4: Commit RED scenarios only**

```bash
git add Framework-Source/tests/pressure-scenarios.md
git commit -m "test(task058): add deterministic runtime pressure scenarios"
```

---

### Task 2: Implement runtime ownership, lifecycle, identity, journal, lease, and atomic-transition semantics

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260916-task058-deterministic-execution-runtime-contract.md`
- Modify: `Framework-Source/references/core-governance-rules.md`

**Interfaces:**
- Consumes: Task 1 RED contract; TASK-057 PLAN/TASK/VERIFY and Operational Execution semantics.
- Produces: normative runtime-domain ownership, four-domain lifecycle separation, durable identity, Supervisor boundary, Journal/Checkpoint authority, lease/heartbeat/fence/control-generation rules, CAS semantics, recovery, version pinning.

- [ ] **Step 1: Add the TASK-058 authority/ownership extension**

Normative text must preserve TASK-057 owners and add exactly these runtime-domain roles:

```text
AI-ControlTower Runtime Store = execution-control facts only
Runtime Event Journal = canonical runtime execution observation within runtime domain
Checkpoint / Snapshot = derived recovery accelerator
Effect Gateway = governed Material-Effect mediation boundary
Effect Permit = dispatch eligibility proof, never AUTH
```

Explicitly prohibit the runtime from owning Project intent, Requirements, Decisions, Risk, Project Source, canonical Task lifecycle, AUTH, Verification PASS, Git truth, deployment truth, release truth, or OUT achievement.

- [ ] **Step 2: Add four-domain lifecycle separation**

Preserve canonical Task lifecycle and TASK-057 Operational Execution state. Add Execution Attempt state:

```text
CREATED -> RUNNABLE -> RUNNING -> WAITING -> RECONCILING -> TERMINATED
exceptions: LOST | BLOCKED | CANCEL_REQUESTED
```

Add Action/Effect state:

```text
PROPOSED -> PREPARED -> PERMITTED -> DISPATCH_INTENT_RECORDED -> DISPATCHED
-> ACKNOWLEDGED -> RECONCILING -> APPLIED | NOT_APPLIED | AMBIGUOUS | REJECTED
```

State explicitly:

```text
Attempt terminal != Operational Execution terminal
Operational Execution CLOSED != Task DONE
ACKNOWLEDGED != resulting-state proof
```

- [ ] **Step 3: Add durable execution and attempt identity**

Normative minimum fields:

```yaml
execution_identity:
  task_ref:
  execution_id:
  runtime_contract_version: "1.0"
  event_schema_version: "1.0"
  task_contract_ref:
  task_contract_fingerprint:
  plan_contract_fingerprint:
  execution_envelope_fingerprint:

attempt_identity:
  execution_id:
  attempt_id:
  executor_ref:
  claim_ref:
  runtime_generation:
  fence_epoch:
```

Material semantic change to pinned Task/Plan/Envelope fingerprints invalidates continuation or requires governed replanning/revalidation; silent hot-swap is prohibited.

- [ ] **Step 4: Add deterministic Supervisor boundary**

Encode this control order:

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

Explicitly state `model turn ended != execution completed`; non-terminal runnable execution may schedule another reasoning step subject to current gates.

- [ ] **Step 5: Add Runtime Event Journal > Checkpoint semantics**

Require append-oriented logical journal authority inside the runtime domain and checkpoint linkage:

```yaml
checkpoint:
  execution_id:
  checkpoint_seq:
  event_sequence:
  previous_checkpoint_hash:
  state_version:
  resume_cursor:
```

If journal continuity cannot be proven, result is `RECOVERY_BLOCKED` or equivalent fail-closed state. Model/chat memory is not a recovery source of truth. Executors/tools cannot forge/rewrite/delete authoritative runtime events.

- [ ] **Step 6: Add lease/heartbeat/fence/control-generation semantics**

Normative distinctions:

```text
claim = coordination
lease = bounded assignment/liveness validity
heartbeat = liveness observation
fence = stale-attempt effect exclusion
AUTH = permission
```

Canonical fence identity is `(runtime_generation, fence_epoch)`. New generation invalidates old leases/fences/permits. Runtime-authoritative/monotonic time governs lease validity; executor wall clock does not.

- [ ] **Step 7: Add atomic runtime transition and restart/version semantics**

Require `state_version` compare-and-set or equivalent atomic primitive and `STALE_CONTROL_DECISION -> reload` semantics. Add restart recovery order:

```text
establish/validate control generation
-> validate journal continuity
-> load compatible checkpoint
-> replay journal tail
-> mark expired/lost Attempts
-> reconcile unresolved possible effects
-> invalidate stale lease/fence/permit
-> fresh-resolve AUTH/R4/fingerprints
-> schedule safely runnable work
```

Add active-execution runtime/event-schema compatibility classes:

```text
BACKWARD_COMPATIBLE
REQUIRES_MIGRATION
INCOMPATIBLE
```

- [ ] **Step 8: Run focused normative checks and commit**

Run scratch assertions for all lifecycle tokens, identity fields, Journal>Checkpoint rule, `(runtime_generation, fence_epoch)`, `state_version`, restart ordering, and version compatibility vocabulary. Expected: PASS.

```bash
git add Framework-Source/references/core-governance-rules.md \
  Framework-Source/references/framework-governance-amendment-260916-task058-deterministic-execution-runtime-contract.md
git commit -m "feat(task058): add deterministic runtime control semantics"
```

---

### Task 3: Implement Effect Gateway, Permit, precondition, reconciliation, cancellation, and compensation semantics

**Files:**
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/references/framework-governance-amendment-260916-task058-deterministic-execution-runtime-contract.md`

**Interfaces:**
- Consumes: Task 2 runtime identities/state semantics.
- Produces: consequence-boundary enforcement contract and deterministic side-effect recovery rules.

- [ ] **Step 1: Add Effect-Surface Closure contract**

Require inventory of applicable effect-capable surfaces:

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

Every governed Material Effect route must be `MEDIATED_BY_EFFECT_GATEWAY` or `EXPLICITLY_PROHIBITED / CONFINED`. Policy-only instruction without enforceable closure is non-conformant for autonomous Material Effects.

- [ ] **Step 2: Add Effect Gateway validation boundary**

Gateway must fresh-check at least:

```text
Operational Execution eligibility
Attempt identity
runtime generation + fence
Task/Plan/Envelope fingerprints
applicable AUTH
required R4
Tool/Capability/Trust eligibility
target identity + target preconditions
effect idempotency/reconciliation/reversibility
remaining budget/retry policy
Effect Permit validity
```

Keep `Gateway eligibility != AUTH` and `Effect Permit != AUTH` explicit.

- [ ] **Step 3: Add mandatory single-use JIT Effect Permit**

Normative minimum fields:

```yaml
effect_permit:
  permit_id:
  execution_id:
  attempt_id:
  action_id:
  action_hash:
  target_ref:
  tool_ref:
  runtime_generation:
  fence_epoch:
  task_contract_fingerprint:
  execution_envelope_fingerprint:
  authority_ref:
  r4_context_ref:
  target_precondition_ref:
  issued_at:
  expires_at:
  max_uses: 1
```

Require atomic `PERMIT_ACTIVE -> PERMIT_CONSUMED`; reject reuse, transfer, stale generation/fence, mismatch, or expiry. State `PERMIT_CONSUMED != effect APPLIED`.

- [ ] **Step 4: Add target-precondition/TOCTOU rules**

When source-native target supports a precondition, declaration is mandatory. Recognize at least:

```text
exact Git ref/SHA
ETag / If-Match
resource_version / generation
row version
object hash
compare-and-set token
immutable candidate identity
```

Unsupported preconditions must be explicit and route to reconciliation/fail-closed policy. Stale target gives `PRECONDITION_CONFLICT`; long-lived queue validation is never sufficient proof of current AUTH/R4/fence/target.

- [ ] **Step 5: Add bounded-effect/idempotency/reversibility contract**

Require one Permit per independently reconcilable Material Effect except a verified real source-native atomic transaction. Define idempotency classes:

```text
IDEMPOTENT | CONDITIONALLY_IDEMPOTENT | NON_IDEMPOTENT | UNKNOWN
```

Define reconciliation strategies:

```text
NATIVE_IDEMPOTENCY_KEY | COMPARE_AND_SET | SOURCE_READBACK |
EXTERNAL_CONFIRMATION | MANUAL_VERIFICATION | NONE
```

Define reversibility:

```text
REVERSIBLE_ATOMIC | COMPENSATABLE | IRREVERSIBLE | UNKNOWN
```

Explicitly prohibit arbitrary exactly-once claims.

- [ ] **Step 6: Add ambiguous-result recovery**

Preserve TASK-057 `RESULT_VERIFICATION_REQUIRED`. For possibly dispatched actions, reconcile to `APPLIED`, `NOT_APPLIED`, or `AMBIGUOUS`. `NON_IDEMPOTENT|UNKNOWN + reconciliation NONE + ambiguous` becomes `MANUAL_RESOLUTION_REQUIRED`/blocking; automatic retry is forbidden.

- [ ] **Step 7: Add cancellation/in-flight/compensation semantics**

Cancellation blocks new dispatch but does not erase already-dispatched facts. Every in-flight possible effect is reconciled after cancellation. Compensation is a new governed effect with its own Action identity, AUTH, Permit, budget, evidence, and reconciliation. Failed compensation may produce `PARTIALLY_COMPENSATED`; claim `ROLLED_BACK` only when source-native atomic rollback is proven.

- [ ] **Step 8: Add secret-safe observability and prompt-injection boundary**

Durable journal/checkpoint/evidence representations support `REFERENCE_ONLY | REDACTED | HASH_ONLY | classified metadata`; raw secret values are prohibited merely for observability. Tool/model output remains untrusted and cannot create authority or bypass Gateway checks.

- [ ] **Step 9: Run focused effect-control checks and commit**

Verify tokens/invariants for closure, Permit binding, preconditions, idempotency/reconciliation/reversibility, `MANUAL_RESOLUTION_REQUIRED`, cancellation, compensation, secret-safe logging, and no-exactly-once rule.

```bash
git add Framework-Source/references/core-governance-rules.md \
  Framework-Source/references/framework-governance-amendment-260916-task058-deterministic-execution-runtime-contract.md
git commit -m "feat(task058): add governed effect boundary and recovery semantics"
```

---

### Task 4: Implement typed executor, budget, wait/wakeup, Multica, and Task Record boundaries

**Files:**
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/references/framework-governance-amendment-260916-task058-deterministic-execution-runtime-contract.md`

**Interfaces:**
- Consumes: Tasks 2–3 runtime/effect semantics.
- Produces: model/runtime schema isolation, autonomous liveness controls, recursive budget accounting, Multica separation, bounded Task Record relationship.

- [ ] **Step 1: Add typed executor proposal vocabulary**

Allow model/executor proposal/report types:

```text
ACTION_PROPOSAL
CANDIDATE_COMPLETE
WAIT_REQUEST
INPUT_REQUEST
YIELD
BLOCKED_REPORT
ERROR_REPORT
```

Explicitly prohibit models from authoritatively producing runtime/governance states including `AUTH_GRANTED`, `LEASE_ACQUIRED`, `FENCE_ADVANCED`, `PERMIT_ISSUED`, `VERIFIED`, `INTEGRATED`, `TASK_DONE`. Unknown privileged fields fail closed.

- [ ] **Step 2: Add durable hierarchical budget contract**

Define applicable dimensions:

```yaml
budget:
  max_model_turns:
  max_tool_calls:
  max_tokens:
  max_wall_time:
  max_retries_per_action:
  max_child_executions:
  max_recursion_depth:
```

Require `parent consumption + sum(child allocations) <= root budget`. Budget exhaustion persists truthful blocked/waiting state and never implies DONE. `REQUEST_RETRY` is advisory only.

- [ ] **Step 3: Add wait/wakeup and bounded fail-closed behavior**

Define wait shape:

```yaml
wait_condition:
  reason:
  wake_event:
  fallback_check_at:
```

Map transient conditions to bounded `WAIT`, external truth to WAIT/wake, human resolution to `BLOCKED / MANUAL_RESOLUTION_REQUIRED`, unresolvable ambiguity to `BLOCKED`. Explicitly state `fail closed != retry forever`.

- [ ] **Step 4: Preserve Multica boundary**

Add explicit separation:

```text
Multica claim != runtime lease != runtime fence != Effect Permit != AUTH
```

Multica may coordinate workers but cannot establish stale-worker safety, source-native effect truth, verification, or Task DONE.

- [ ] **Step 5: Preserve Task Record vs runtime journal boundary**

Normative split:

```text
Runtime Event Journal = fine-grained execution-control observation
Task Record = bounded observed result + Actual IPOCV used by VERIFY
```

Task Record must not become an unbounded event stream. Verification uses Task Record/source-native evidence/exact candidate/current truth rather than trusting model narration.

- [ ] **Step 6: Add Effect Gateway conformance evidence requirements**

For each mediated effect class require demonstrable answers for: executor effect surfaces; confinement/mediation; credential location; permit atomicity; stale generation/fence rejection; target preconditions; idempotency/reconciliation/reversibility; ambiguous result handling; cancellation/in-flight reconciliation; source-native resulting-state confirmation.

- [ ] **Step 7: Run focused behavioral checks and commit**

Expected: all typed-vocabulary, forbidden-runtime-event, budget-lineage, wait/block, Multica, Task Record/journal, and conformance-evidence checks PASS.

```bash
git add Framework-Source/references/core-governance-rules.md \
  Framework-Source/references/framework-governance-amendment-260916-task058-deterministic-execution-runtime-contract.md
git commit -m "feat(task058): add typed executor and bounded autonomy semantics"
```

---

### Task 5: Add new Project-Execution runtime-contract starters

**Files:**
- Create: `Framework-Source/templates/project-execution/runtime-contract.md`
- Create: `Framework-Source/templates/project-execution/execution-attempt.md`
- Create: `Framework-Source/templates/project-execution/execution-checkpoint.md`
- Create: `Framework-Source/templates/project-execution/action-journal.md`
- Create: `Framework-Source/templates/project-execution/effect-policy.md`

**Interfaces:**
- Consumes: Tasks 2–4 normative contracts.
- Produces: single-responsibility declarative starters for runtime implementers/consumers; no executable runtime.

- [ ] **Step 1: Create `runtime-contract.md`**

The starter must declare, without granting authority: runtime contract/event schema versions; runtime owner; Task/Execution/Attempt/Action separation; Supervisor ownership; runtime generation; state-version atomicity; journal authority; checkpoint derivation; budget root; wait/retry policy; runtime-upgrade compatibility; prohibited authority claims.

Required literal invariants include:

```text
Runtime decision ≠ Authority
Runtime Event Journal > Checkpoint / Snapshot
Model proposal ≠ Runtime decision
```

- [ ] **Step 2: Create `execution-attempt.md`**

Include execution/attempt IDs, executor/claim refs, generation/fence, lease/heartbeat metadata, Attempt state vocabulary, budget allocation/consumption, parent/root lineage, wait/block state, and terminal reason. State that Attempt termination/loss never directly closes Operational Execution or Task.

- [ ] **Step 3: Create `execution-checkpoint.md`**

Include `execution_id`, `checkpoint_seq`, `event_sequence`, `previous_checkpoint_hash`, `state_version`, `resume_cursor`, compatible runtime/event versions, unresolved action refs, remaining budget summary, and derivation rule. State checkpoint is derived and cannot repair missing journal truth by inference.

- [ ] **Step 4: Create `action-journal.md`**

Define Action identity and state vocabulary `PROPOSED → PREPARED → PERMITTED → DISPATCH_INTENT_RECORDED → DISPATCHED → ACKNOWLEDGED → RECONCILING → APPLIED|NOT_APPLIED|AMBIGUOUS|REJECTED`; include permit ref, target/precondition, effect semantics, source-native evidence/reconciliation, cancellation/compensation linkage, and secret-safe representation. State this starter is conceptual/declarative, not an instruction to store an unbounded log in Project Source.

- [ ] **Step 5: Create `effect-policy.md`**

Include effect-surface inventory; mediation/confinement classification; credential boundary; idempotency/reconciliation/reversibility vocabularies; target-precondition support/limitation; Permit requirements; cancellation/compensation; manual-resolution conditions; conformance evidence fields. Keep policy distinct from AUTH and Tool availability.

- [ ] **Step 6: Verify new starter coverage and commit**

Scratch check that exactly 5 new files exist and together contain all required lifecycle, generation/fence, journal/checkpoint, Permit, precondition, idempotency, reconciliation, reversibility, budget, cancellation, compensation, version-pinning, and authority-separation tokens.

```bash
git add Framework-Source/templates/project-execution/runtime-contract.md \
  Framework-Source/templates/project-execution/execution-attempt.md \
  Framework-Source/templates/project-execution/execution-checkpoint.md \
  Framework-Source/templates/project-execution/action-journal.md \
  Framework-Source/templates/project-execution/effect-policy.md
git commit -m "feat(task058): add deterministic runtime contract starters"
```

---

### Task 6: Align existing Project-Execution contracts and profiles

**Files:**
- Modify: `Framework-Source/templates/project-execution/README.md`
- Modify: `Framework-Source/templates/project-execution/task-contract.md`
- Modify: `Framework-Source/templates/project-execution/task-record.md`
- Modify: `Framework-Source/templates/project-execution/executor-profile.md`
- Modify: `Framework-Source/templates/project-execution/tools.md`
- Modify: `Framework-Source/templates/project-execution/trust.md`

**Interfaces:**
- Consumes: Tasks 2–5.
- Produces: coherent TASK-057/TASK-058 declarative profile set with no authority transfer or runtime implementation.

- [ ] **Step 1: Update Project-Execution README inventory and applicability**

Add the five TASK-058 starters to the maintained inventory. Explain that they are optional/applicability-driven protocol surfaces for runtimes that need deterministic long-running execution; non-ControlTower Projects remain valid. Preserve `Project-Execution ≠ Project Source ≠ AUTH ≠ runtime authority`.

- [ ] **Step 2: Extend `task-contract.md` only with runtime-facing declarations that belong to Task success/control semantics**

Add references/constraints for effect-policy/runtime applicability where needed, while keeping Task Contract owner of intent/acceptance/dependencies/completion/Expected IPOCV/integration. Do not move runtime journal or Attempt state into the Task Contract.

- [ ] **Step 3: Extend `task-record.md` with bounded runtime references only**

Allow references to execution/attempt/checkpoint/journal evidence necessary to explain observed Actual IPOCV/result, while explicitly prohibiting transformation of Task Record into per-action runtime log.

- [ ] **Step 4: Extend `executor-profile.md` for runtime/effect eligibility**

Add declarative support for mediated effect classes, effect-surface-closure capability, attempt/heartbeat support, checkpoint/resume support, recursive-execution capability/limits, and typed-proposal protocol support. Preserve `Capability/Eligibility ≠ Authority` and independent-verifier separation.

- [ ] **Step 5: Extend `tools.md` for Gateway/reconciliation compatibility**

Retain TASK-048 fallback/failback semantics. Add declarative fields/rules for mediated-vs-prohibited effect routes, target-precondition support, idempotency/reconciliation support, and the requirement that unresolved previous effects stay `RESULT_VERIFICATION_REQUIRED` before fallback/retry.

- [ ] **Step 6: Extend `trust.md` for executor/Gateway/credential boundaries**

Describe runtime store, executor workspace, Effect Gateway, source-native targets, and credentials as separate trust surfaces when applicable. Preserve secret/disclosure governance and state that privileged/trusted surfaces still do not grant AUTH.

- [ ] **Step 7: Run cross-starter consistency checks and commit**

Verify exact shared vocabularies and no contradictory ownership between the five new starters and six updated existing files.

```bash
git add Framework-Source/templates/project-execution/
git commit -m "docs(task058): align execution profiles with runtime contract"
```

---

### Task 7: Propagate Framework 1.20 guidance, migration, release metadata, and maintained stamps

**Files:**
- Modify: `Framework-Source/SKILL.md`
- Modify: `README.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: all 22 maintained files under `Framework-Source/templates/project-source-mockup/` (`00–17`, `40`, `60`, `91`, `92`)

**Interfaces:**
- Consumes: Tasks 2–6 completed semantics.
- Produces: discoverable Framework `1.20.0` distribution with additive migration guidance; active self-host Project Source remains outside this Task unless separately authorized.

- [ ] **Step 1: Update `SKILL.md` execution routing**

Add TASK-058 read/routing guidance after TASK-057 contracts: Task/Plan/Envelope + AUTH + R4 + Executor/Tool/Trust profiles + runtime/effect policy + Ready Gate before execution; source-native reconciliation after effects. Preserve Planner/Execution Handoff and no-self-promotion rules.

- [ ] **Step 2: Update root README and Framework templates**

Describe Framework 1.20 as additive deterministic execution-runtime **contract support**, not a bundled runtime. Include concise invariants `Task lifetime != model turn`, `Runtime decision != Authority`, `Material mediated effect -> Effect Gateway`, and language neutrality. Point consumers to `Project-Execution/` starters without creating a new Project Source slot.

- [ ] **Step 3: Update release descriptor**

Set:

```yaml
framework_version: "1.20.0"
schema_version: "1.0.0"
release_format: 3
latest_framework_amendment: "references/framework-governance-amendment-260916-task058-deterministic-execution-runtime-contract.md"
```

Preserve existing descriptor fields not changed by TASK-058.

- [ ] **Step 4: Update migration notes**

State: additive adoption; no historical Task retrofit; no runtime service included; no new semantic slot/Stable-ID family; non-ControlTower Projects remain valid; optional/applicability-driven runtime starters; Brownfield adoption through governed `[Project Upgrade]`; active executions in future runtimes must respect version pinning; release classification must be revisited if implementation found a breaking requirement.

- [ ] **Step 5: Update exactly 22 maintained starter Framework stamps to `1.20.0`**

Do not rewrite historical specs/plans/evidence/amendments. Do not self-promote active `Project-Source/` or root `PROJECT-BOOTSTRAP.md` as part of TASK-058 unless a separate governed self-host reconciliation is explicitly authorized after integration.

- [ ] **Step 6: Verify propagation and commit**

Run scratch checks for release descriptor 4/4 fields, latest amendment route, migration tokens, five new starter references, exactly 22 maintained stamps at 1.20.0, unchanged schema/release format, no runtime/executable artifact, and no active Project-Source self-host mutation in the TASK-058 implementation diff.

```bash
git add Framework-Source README.md
git commit -m "chore(task058): prepare Framework 1.20 runtime-contract distribution"
```

---

### Task 8: Run structural GREEN, cumulative AFFECTED verification, and independent review

**Files:**
- Modify only files required to resolve review findings inside approved TASK-058 scope.

**Interfaces:**
- Consumes: Tasks 1–7 candidate.
- Produces: reviewed Framework 1.20 candidate ready for freeze; no release proof yet.

- [ ] **Step 1: Run structural GREEN verifier**

Verify at minimum:

```text
scenarios 1–602 contiguous/unique
all 46 TASK-058 pressure classes present
four lifecycle domains remain separate
canonical Task lifecycle unchanged
TASK-057 Operational Execution vocabulary preserved
runtime identity + generation/fence + state_version present
Journal > Checkpoint rule present
Effect-Surface Closure present
Effect Permit binding/atomic-consumption rules present
target precondition + PRECONDITION_CONFLICT present
idempotency/reconciliation/reversibility vocabularies present
no exactly-once guarantee
ambiguous unreconcilable effect -> manual/block
cancellation/in-flight + compensation semantics present
typed executor vs runtime namespace separation present
hierarchical budget and recursion limits present
Multica boundary preserved
Task Record != runtime journal
runtime/event version pinning present
5/5 new starters present
6/6 existing execution profiles aligned
```

Record exact result as `TASK058_STRUCTURAL N/N PASS`.

- [ ] **Step 2: Run cumulative AFFECTED verifier**

Include structural checks plus release metadata, migration, 22 maintained stamps, Framework current-surface routing, TASK-057 regression invariants, TASK-048 MCP fallback/failback compatibility, secret/disclosure/trust constraints, `git diff --check`, documentation/YAML-only scope, and absence of runtime/service/code artifacts. Record exact `TASK058_AFFECTED N/N PASS`.

- [ ] **Step 3: Run independent fresh-context review**

Use `superpowers:requesting-code-review` or the available independent-review equivalent. Reviewer must compare the full candidate against the approved TASK-058 spec and specifically challenge:

```text
unintended authority transfer
Task/Execution/Attempt/Action state conflation
Gateway policy without enforceable closure semantics
Permit replay/transfer gaps
stale generation/fence gaps
exactly-once overclaim
blind retry on ambiguous effects
checkpoint outranking journal
cancellation/compensation false rollback
recursive budget escape
model-forged runtime state
secret leakage
TASK-057/TASK-048 semantic regressions
runtime implementation scope creep
```

Require zero unresolved Critical or Important findings before candidate freeze.

- [ ] **Step 4: Resolve findings proportionally**

Fix only material in-scope findings. Rerun focused checks for every fix and rerun structural/AFFECTED when normative semantics change. Do not add runtime implementation to satisfy review suggestions.

- [ ] **Step 5: Commit review fixes if any**

Stage only review-fix files within the approved Framework/doc scope. The worktree must be clean before review, so this command stages only newly introduced review-fix changes:

```bash
git add Framework-Source README.md
git commit -m "fix(task058): address deterministic runtime contract review findings"
```

If no files changed, record `REVIEW_PASS / NO_FIX_COMMIT_REQUIRED` in completion evidence later.

---

### Task 9: Freeze the final candidate, run one RELEASE_FULL, persist evidence, and reconcile Task lifecycle

**Files:**
- Create: `docs/superpowers/evidence/2026-09-16-task-058-deterministic-execution-runtime-contract-release-full.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md` only at proven lifecycle checkpoints.

**Interfaces:**
- Consumes: Task 8 clean reviewed candidate.
- Produces: exact Framework 1.20 candidate identity, final release proof, durable TASK-058 completion evidence, truthful terminal/local publication state.

- [ ] **Step 1: Freeze an unchanged candidate**

Require clean candidate workspace. Record:

```text
candidate commit SHA
repository tree SHA
Framework-Source tree SHA
Framework version 1.20.0
Schema 1.0.0
release format 3
```

No candidate content changes after freeze unless the candidate is invalidated and replaced.

- [ ] **Step 2: Run exactly one final RELEASE_FULL on the unchanged candidate**

The final suite must cover TASK-058 AFFECTED plus existing Framework release invariants: Registered Commands; scenario continuity; maintained starter stamps; Core/SKILL/latest-amendment routing; migration/release descriptor consistency; launcher constraints where applicable; historical provenance; TASK-057 declarative execution contracts; TASK-048 MCP fallback/failback compatibility; no unexpected runtime artifact. Record `TASK058_RELEASE_FULL N/N PASS_RUN_1`.

If a candidate-invalidating defect appears, do not reuse its proof: fix+commit, establish a new candidate identity, rerun affected checks, then run the one final RELEASE_FULL on the replacement candidate.

- [ ] **Step 3: Create release/completion evidence**

Evidence must record: Design V3 approval; explicit written-spec approval date `2026-09-16`; spec and plan paths; scenario range `557–602`; implementation/review commits; structural/AFFECTED results; independent review result; candidate/tree/Framework-Source tree; final RELEASE_FULL; five new starters; no-runtime confirmation; exact publication/self-host state; any invalidated candidate history.

- [ ] **Step 4: Reconcile `PROJECT-TASKS.md` truthfully**

Only set `TASK-058 DONE` after all completion criteria are evidenced. Preserve distinctions among local verified completion, push/merge, tag/Release, self-host promotion, consumer upgrade, and AI-ControlTower runtime implementation. Do not synthesize OUT/AUTH/ACT/ENV records after the fact unless separately governed.

- [ ] **Step 5: Persist evidence/lifecycle checkpoint and read it back**

```bash
git add docs/superpowers/evidence/2026-09-16-task-058-deterministic-execution-runtime-contract-release-full.md \
  docs/superpowers/PROJECT-TASKS.md
git commit -m "docs(task058): record Framework 1.20 release evidence and terminal task state"
```

Fresh-read the resulting commit/file state before claiming completion.

- [ ] **Step 6: Stop at the publication/runtime boundary**

Do not push/PR/merge/tag/GitHub Release/self-host promote/upgrade a consumer or mutate AI-ControlTower runtime unless exact current authority separately covers that action and its applicable fresh gates pass.

---

## Plan Self-Review

### Spec coverage

- Spec §§1–6: Tasks 2 and 7.
- Spec §§7–12: Task 3, with scenario coverage in Task 1.
- Spec §§13–15: Task 2.
- Spec §§16–18: Task 4.
- Spec §§19–23: Tasks 3–4.
- Spec §§24–26: Tasks 4 and 6.
- Spec §§27–28: Tasks 5–7.
- Spec §29: Task 1.
- Spec §§30–33: Global Constraints + Tasks 7–8.
- Spec §§34–35: Task 9 and this execution handoff.

All required pressure classes `557–602` have an explicit Task 1 allocation. All five candidate new starters are created in Task 5. All six existing Project-Execution surfaces named by the spec are aligned in Task 6. Release/migration/stamp propagation is Task 7. Independent review/AFFECTED/frozen-candidate/one-final-RELEASE_FULL/evidence are Tasks 8–9.

### Placeholder scan

Instruction steps contain no unresolved filler markers or replace-me path tokens. Empty values in YAML blocks intentionally specify required schema keys rather than unfinished plan content. Canonical `TODO` appears only as governed Task-lifecycle vocabulary, not as an unplanned implementation item.

### Interface/type consistency

The plan uses one consistent vocabulary across tasks:

```text
runtime_generation + fence_epoch
state_version
Runtime Event Journal > Checkpoint / Snapshot
Effect Permit
PERMIT_ACTIVE -> PERMIT_CONSUMED
PRECONDITION_CONFLICT
RESULT_VERIFICATION_REQUIRED
MANUAL_RESOLUTION_REQUIRED
IDEMPOTENT | CONDITIONALLY_IDEMPOTENT | NON_IDEMPOTENT | UNKNOWN
REVERSIBLE_ATOMIC | COMPENSATABLE | IRREVERSIBLE | UNKNOWN
ACTION_PROPOSAL | CANDIDATE_COMPLETE | WAIT_REQUEST | INPUT_REQUEST | YIELD | BLOCKED_REPORT | ERROR_REPORT
BACKWARD_COMPATIBLE | REQUIRES_MIGRATION | INCOMPATIBLE
```

Task 5 starter fields derive directly from Tasks 2–4; Task 6 references those starters without redefining owners; Tasks 8–9 verify the same vocabulary.

## Execution Handoff

Plan state after persistence/self-review:

```text
WRITTEN_SPEC = APPROVED
IMPLEMENTATION_PLAN = WRITTEN / SELF_REVIEWED
PLANNER = GPT
EXECUTION_STATE = EXECUTION_HANDOFF_REQUIRED
IMPLEMENTATION = NOT STARTED
AI_CONTROLTOWER_RUNTIME_IMPLEMENTATION = NOT AUTHORIZED_BY_TASK058
```

Before execution, the applicable execution-control layer must fresh-resolve the Task Contract, Plan Contract, Execution Envelope, AUTH, `R4_CTX`, Task Ready Gate, tool/capability/trust/executor eligibility, workspace/target truth, and independent Verifier requirement. Planning completion does not self-select GPT as Executor.
