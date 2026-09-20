# TASK-059 Phase 0 — Baseline and Collision Reconciliation

Date: `2026-09-20` (Asia/Bangkok)
Task: `TASK-059`
Phase: `0 — baseline and collision reconciliation`
Result: `PASS`

## 1. Fresh baseline proof

Observed 2026-09-20 from the local checkout at `E:\GitHub\ProjectFramework`:

```text
branch:            task059-runtime-contract (fresh, from main)
HEAD:              04b718446d7579f0336d5cdac24a66037e0f20e0
origin/main:       04b718446d7579f0336d5cdac24a66037e0f20e0
repository tree:   4431b6a2a2b441f55762123f779d7dd060f0425b
working tree:      CLEAN (git status --porcelain empty)
Framework:         1.20.0 (FRAMEWORK-RELEASE.yaml framework_version)
Schema:            1.0.0 (FRAMEWORK-RELEASE.yaml schema_version)
release format:    3 (FRAMEWORK-RELEASE.yaml release_format_version)
Root pin:          1.20.0 / 1.0.0 (active 00 / FRAMEWORK-001 r008)
active Project Source: 16/16 documents ACTIVE at 1.20.0 / 1.0.0
pressure scenarios: 1–590 contiguous, unique, ends at 590 (590 scenarios)
TASK-058:          DONE / VERIFIED_COMPLETE / MERGED_TO_MAIN / PR_35 / TAGGED_v1.20.0 / RELEASED / SELF_HOST_RECONCILED (MIG-006)
```

Baseline is exactly Framework `1.20.0` / Schema `1.0.0` / release format `3`. No material change to the Framework baseline or schema; no re-plan required.

## 2. Historical V3 collision matrix

Historical V3 source: `docs/superpowers/specs/2026-09-16-task058-deterministic-execution-runtime-contract-design.md` (source material only; old V3 branches remain `SUPERSEDED / PAUSED / NOT_MERGED` and are not reactivated).

Classification per V3 concept against the verified Framework 1.20 Wave A V2 baseline:

### RETAINED — missing from Framework 1.20, still useful, forward-ported by TASK-059

| V3 concept (V3 §) | TASK-059 disposition |
|---|---|
| Runtime Event Journal as canonical runtime observation (V3 §13) | RETAINED — new normative contract + `runtime-event-journal.md` starter |
| Checkpoint as derived recovery accelerator (V3 §13) | RETAINED — new normative contract + `execution-checkpoint.md` starter |
| Supervisor / control generation recovery (V3 §6, §14, §21) | RETAINED — new normative contract + `runtime-contract.md` starter |
| Runtime liveness projection subordinate to ownership (V3 §14) | RETAINED — normative subsection; lease/heartbeat/fence subordinate to Framework 1.20 Ownership Grant and AUTH |
| Effect Gateway mediation (V3 §7, §8) | RETAINED — new normative contract + `effect-policy.md` starter |
| Just-in-Time Effect Permit (V3 §9) | RETAINED — normative contract inside Effect Policy; single-use/non-transferable/bound; never AUTH |
| Target preconditions / TOCTOU (V3 §10) | RETAINED — normative contract inside Effect Policy |
| Bounded action / idempotency + reversibility classes (V3 §11) | RETAINED — normative contract inside Effect Policy |
| Ambiguous-effect reconciliation (V3 §12) | RETAINED — normative contract; no arbitrary exactly-once; no blind retry |
| Durable continuation / wait / bounded autonomy (V3 §17, §18) | RETAINED — normative contract (continuation/retry budgets, wake conditions, explicit dispositions) |
| RLM / recursive executor profile (V3 §17) | RETAINED — new provider-neutral contract + `rlm-executor-profile.md` starter |
| Cancellation and in-flight effects (V3 §19) | RETAINED — normative contract |
| Compensation semantics (V3 §20) | RETAINED — normative contract; compensation ≠ rollback/history erasure |
| Runtime restart / store restore recovery (V3 §21) | RETAINED — normative contract |
| Runtime + event-schema version pinning (V3 §22) | RETAINED — normative contract |
| Security boundary: untrusted model/tool output, runtime-owned event namespace, secret exclusion (V3 §16, §23) | RETAINED — normative contract |
| Prime Agent optional mapping (V3 §27) | RETAINED — optional mapping only; not a ProjectFramework dependency or authority |
| Python Supervisor reference-runtime conformance handoff (V3 §26, §28, §31) | RETAINED — non-executable handoff section; AI-ControlTower implements separately |

### ALREADY SATISFIED — present in Framework 1.20 Wave A V2; not re-added

| V3 concept (V3 §) | Framework 1.20 owner |
|---|---|
| Four lifecycle domains: canonical Task lifecycle (V3 §4.1) | Framework 1.19 canonical Task lifecycle, unchanged |
| Operational Execution state (V3 §4.2) | Framework 1.19/1.20 operational execution-state domain + Wave A V2 guards |
| Execution Attempt state (V3 §4.3) | Mapped onto Wave A V2 execution attempt identity + Ownership Grant epoch; TASK-059 does not create a parallel lifecycle |
| Action / Effect state (V3 §4.4) | Superseded in shape by TASK-059 Effect Permit + reconciliation classes; no separate Action lifecycle record is introduced |
| Identity model: execution/attempt identity (V3 §5) | Composed onto Wave A V2 Execution State Binding + ownership epoch; TASK-059 adds `runtime_generation`/`fence_epoch` as runtime-local projections |
| Authority/ownership separation (V3 §3) | Framework 1.19/1.20 authority model + Wave A V2 ownership/fencing, unchanged |
| Atomic runtime transitions / CAS (V3 §15) | Wave A V2 `OPERATIONAL_TRANSITION` CAS + idempotency semantics |
| Reassignment safety (V3 §15, Wave A §15) | Wave A V2 Reassignment Gate outcomes |
| Multica coordination-only boundary (V3 §24) | Framework 1.19/1.20 Multica boundary, unchanged |
| Task Record vs runtime journal separation (V3 §25) | Wave A V2 Task Record semantics; TASK-059 keeps the journal runtime-local and never a Task Record replacement |
| Language/host-neutral standard (V3 §27) | Framework 1.20 no-runtime boundary, unchanged |
| Effect Gateway conformance boundary (V3 §26) | Retained as conformance inputs in the handoff section, not a new Framework record type |

### REJECTED — superseded, conflicting, or out of scope

| V3 concept (V3 §) | Reason |
|---|---|
| Old V3 scenario numbering `557–602` (V3 §29) | REJECTED — `557–590` are already allocated to Wave A V2; TASK-059 allocates strictly after `590` |
| V3 target release `1.20.0` (V3 §30) | REJECTED — `1.20.0` is the verified baseline; TASK-059 candidate is `1.21.0` |
| V3 amendment filename `...-task058-deterministic-execution-runtime-contract.md` (V3 §28) | REJECTED — TASK-059 is a successor amendment on the 1.20 baseline, not a rewrite of the TASK-058 Design of Record |
| V3 `execution-attempt.md` / `action-journal.md` starter names (V3 §28) | REJECTED in name — superseded by TASK-059 single-responsibility starters `runtime-contract.md`, `runtime-event-journal.md`, `execution-checkpoint.md`, `effect-policy.md`, `rlm-executor-profile.md` |
| Cryptographic producer identity / authenticated event envelopes (V3 §14 note) | REJECTED for now — optional only if implementation evidence shows the selected deployment model requires them; not silently assumed |
| Any executable runtime implementation (V3 §31 list) | REJECTED — belongs to a separate AI-ControlTower implementation Task |

## 3. Task Ready Gate

Fresh evaluation on 2026-09-20 against the pinned Framework 1.20 `Task Ready Gate` contract:

```text
TASK_PLANNING_READINESS == READY        PASS — spec USER_APPROVED (ACTOR-001, 2026-09-20); plan WRITTEN / SELF_REVIEWED / WRITTEN_SPEC_USER_APPROVED
PLAN_CONTRACT_VALID                  PASS — plan phases 0–8, execution boundary, and post-task sequence complete; no TBD/placeholder
TASK_CONTRACT_VALID                  PASS — TASK-059 ledger entry complete: depends_on [TASK-058], scope, boundaries, candidate target
EXPECTED_IPOCV_COMPLETE              PASS — I: approved spec/plan + 1.20 baseline; P: phases 0–8; O: 1.21.0 candidate + handoff package; C: no push/PR/merge/tag, no runtime code, no cutover; V: AFFECTED + independent review + one RELEASE_FULL
EXECUTION_ENVELOPE_VALID             PASS — local docs/governance mutations on branch task059-runtime-contract; risk ceiling R1 REVERSIBLE_LOCAL; publication separately governed
DEPENDENCIES_SATISFIED               PASS — TASK-058 DONE / MERGED_TO_MAIN / PR_35 / TAGGED_v1.20.0 / RELEASED / SELF_HOST_RECONCILED
R4_REQUIRED_TRUTH_RESOLVED           PASS — fresh-read origin/main, descriptor, root, all 16 active documents, TASK-058 evidence, task ledger, scenario ceiling 590
APPLICABLE_AUTHORITY_RESOLVED        PASS — ACTOR-001 explicit 2026-09-20: written-spec approval + Hermes designated Executor + "อ่าน plan แล้วดำเนินการ TASK-059" execution directive
REQUIRED_EXECUTOR_CAPABILITY_RESOLVED PASS — Hermes runtime binding exact: workspace E:\GitHub\ProjectFramework, branch task059-runtime-contract, git + file tools available; declared LOCAL_LLM_ENGINEER implementation
SOURCE_OF_TRUTH_OWNERS_RESOLVED      PASS — Framework-Source (distribution), Project-Source (governance truth), docs/superpowers (task ledger/evidence), Git (integration truth)
NO_BLOCKING_CONFLICT                 PASS — clean tree, local == origin/main, no open work on this branch
```

`Task Ready Gate = PASS`.

Note: `Task Ready Gate PASS ≠ authority grant ≠ claim ≠ execution success ≠ Task DONE.` The user's explicit 2026-09-20 execution directive is the applicable authority for local implementation-plane mutation; push/PR/merge/tag/Release remain separately governed and are excluded.

## 4. Result

`PHASE_0 PASS` — baseline exactly `1.20.0 / 1.0.0 / format 3`; collision matrix complete; Task Ready Gate `PASS`; implementation may proceed to Phase 1 (RED pressure contract).
