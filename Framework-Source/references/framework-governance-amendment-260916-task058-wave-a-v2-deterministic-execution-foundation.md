# Framework Governance Amendment — TASK-058 Wave A V2 Deterministic Execution Foundation

Date: `2026-09-16`
Framework: `1.20.0`
Schema: `1.0.0`
Release format: `3`
Source Task: `TASK-058`
Design spec: `docs/superpowers/specs/2026-09-16-task058-wave-a-v2-deterministic-execution-foundation-design.md` (ACTOR-001 explicit approval, 2026-09-16)
Predecessor amendment: `references/framework-governance-amendment-260914-task057-ai-controltower-governance-support-layer.md` (Framework `1.19.0`; remains the historical contract for Framework `1.19.0` records)

## 1. Scope

Framework `1.20.0` adds the **Compositional State Binding Hub**: a set of declarative record/contract semantics that bind one execution attempt to the exact materially relevant state it ran against, so that results, verification, and later integration decisions remain state-bound and reconstructable. The hub is compositional: each concern is a single-responsibility record that references the others. No mega-record is introduced.

The layer is additive. It changes no Project Source semantic slot, no Project Source Stable-ID family, no Registered Command set, no canonical Task lifecycle value, no Risk level (Risk remains exactly `R0–R3`), and no release-descriptor format. Project Source Schema remains `1.0.0`. Existing Framework `1.19.0` semantics — `PLAN | TASK | VERIFY` modes, Plan/Task Contract, Execution Envelope, Expected/Actual IPOCV, Task Ready Gate, operational execution-state domain, Multica coordination-only boundary, Executor Profile / Project Adapter, filter-before-rank selection, exact-SHA candidate verification, fresh `INTEGRATION_GATE`, integration reconciliation — are preserved unchanged except where this amendment explicitly strengthens an operational state guard.

This amendment implements no runtime. It defines declarative semantics only: record shapes, identity/digest rules, fail-closed eligibility and invalidation behavior, required ordering and guards, interoperability invariants, and no-inference / no-history-rewrite rules.

## 2. Authority model and non-runtime boundary

The Framework `1.19.0` authority model carries forward unchanged:

```text
ProjectFramework        = governance contract semantics
Project Source          = canonical Project governance truth
Durable Task Source     = canonical Task lifecycle truth
AUTH-* / explicit User authority = mutation/operation authority
R4 Current Truth Context = execution-time resolution of mutable facts from their real owners
Project Adapter         = translation/locator boundary
Capability / Tool / Trust / Executor Profiles = execution eligibility policy
Multica                 = operational claim/coordination owner only
Executor                = bounded work performer
Task Record             = actual execution observation
Verification Record     = state-bound verification result
Git / GitHub / source-native systems = factual authority for state they own
```

The following remain distinct and none implies another. The Framework `1.19.0` chain is retained verbatim, and Wave A V2 extends it:

```text
Contract ≠ Authority
Capability ≠ Authority
Eligibility ≠ Authority
Claim ≠ Authority
Execution success ≠ Verification PASS
Verification PASS ≠ Task DONE
Task DONE ≠ OUT achieved
Task DONE ≠ MERGED ≠ PUSHED ≠ RELEASED ≠ ARTIFACT_PUBLISHED ≠ DEPLOYED
```

Wave A V2 additions:

```text
Coordination Claim ≠ Execution Ownership Grant
Task Record observation ≠ Result Acceptance
Result Acceptance ELIGIBLE ≠ Verification PASS
Verification PASS ≠ Verification Validity CURRENT
Revision Set ≠ Input Manifest ≠ Execution State Binding
Resource Identity ≠ Locator ≠ Revision
```

Framework `1.20.0` implements no AI-ControlTower runtime, ProjectFramework 2.0 cutover, Control Plane, state/workflow engine, task database, event store, queue, scheduler, worker daemon, Multica runtime, lease/fencing service, distributed lock, automatic transition engine, model/executor router, executable Project Adapter, MCP router, merge bot, merge queue, verification daemon, CI runner, API server, automatic Task DONE updater, automatic reconciliation worker, automatic acceptance engine, Structured Core, Generated Governance, or Transaction Mode implementation.

## 3. Canonical Wave A execution composition

The canonical order for a governed execution attempt is:

```text
PLAN / Task Contract / Execution Envelope
            ↓
Task Ready Gate PASS
            ↓
Executor eligibility selection (filter-before-rank)
            ↓
Applicable Coordination Claim
            ↓
Execution Ownership Grant
+ scoped ownership epoch
+ required fencing assurance
            ↓
Resolve Revision Set
+ Execution Input Manifest
+ dispatch-time R4 observation
+ dispatch-time AUTH evaluation
+ Workspace identity
+ state-bound Ownership evidence
            ↓
Finalize immutable Execution State Binding
            ↓
CAS operational transition CLAIMED → EXECUTING
            ↓
Bounded Execution / Material Effects
            ↓
Task Record / Result Observation
            ↓
Generic Result Identity or Result Set
            ↓
Fresh Result Acceptance Evaluation
            │
            ├─ non-ELIGIBLE / UNKNOWN → retain observation; do not promote
            │
            └─ ELIGIBLE
                  ↓
             Verification Basis
                  ↓
             Verification Evidence
                  ↓
             PASS | FAIL | UNKNOWN
                  ↓
             Verification Validity Evaluation
                  ↓
             CURRENT | STALE | INVALIDATED | UNKNOWN
```

Rules:

- The Execution Ownership Grant MUST precede Execution State Binding finalization. A binding that references an ownership state which does not yet exist is `INCOMPLETE`.
- The `CLAIMED → EXECUTING` transition is an operational CAS transition (Section 8). Binding finalization is not itself a transition; it is evidence production.
- Before `VERIFYING → VERIFIED`, the current applicable Result Acceptance MUST be freshly re-evaluated and remain `ELIGIBLE`, in addition to Verification `PASS` and verification validity `CURRENT`.
- Each record is single-responsibility and references the others. No mega-record is introduced.

## 4. Resource identity and Revision Set

### 4.1 Identity separation

```text
Resource Identity ≠ Locator ≠ Revision
```

A resource may move or be renamed without changing its logical identity. A locator is routing information. A revision is exact observed state.

No `RESOURCE-*` Project Stable-ID family is introduced. `resource_ref` may be a Project-owned identifier, a Project Adapter mapping, or a runtime-local identity whose scope is declared.

### 4.2 Revision Set

`record_type: REVISION_SET` answers **which source state** the execution ran against.

```yaml
record_type: REVISION_SET
record_version: "1.0"
revision_set_ref: "<contract-local reference>"
digest_profile_ref: "<canonicalization + digest profile>"
resources:
  - resource_ref: "<logical resource identity>"
    role: "<declared role>"
    required: true
    identity_kind: "GIT | FILE_SET | SCHEMA | EXTERNAL_CONTRACT | SOURCE_NATIVE"
    locator_ref: "<routing locator>"
    revision:
      exact_identity: "<source-native exact revision>"
    observed_at: "<timestamp>"
completeness:
  required_resources: 1
  resolved_required_resources: 1
  state: "COMPLETE | INCOMPLETE | UNKNOWN"
revision_set_digest: "<semantic digest under digest_profile_ref>"
created_at: "<timestamp>"
```

Rules:

- Every declared required resource must resolve exactly for `COMPLETE`.
- Optional missing resources do not block `COMPLETE` unless another contract makes them material.
- A single Git repository exact SHA is a valid one-member Revision Set.
- Once referenced by an Execution State Binding, the Revision Set is immutable evidence.
- Source change produces a new observation/set. Historical evidence is never changed to `latest`.
- A digest is comparable only under a compatible `digest_profile_ref` (Section 7).

## 5. Execution Input Manifest

The Revision Set answers which source state; the `record_type: EXECUTION_INPUT_MANIFEST` answers **which materially relevant execution inputs** participated.

```yaml
record_type: EXECUTION_INPUT_MANIFEST
record_version: "1.0"
input_manifest_ref: "<contract-local reference>"
source_revision_set_ref: "<Revision Set>"
digest_profile_ref: "<canonicalization + digest profile>"
toolchain:
  - tool_ref: "<tool>"
    version_or_digest: "<exact observed identity>"
dependencies:
  - dependency_manifest_ref: "<lock/manifest source>"
    digest: "<digest>"
configuration:
  - config_ref: "<material config>"
    revision_or_digest: "<exact observed identity>"
feature_state:
  - flag_set_ref: "<material flag set>"
    revision_or_digest: "<exact observed identity>"
schemas:
  - system_ref: "<system>"
    revision: "<revision>"
external_contracts:
  - contract_ref: "<contract>"
    version_or_digest: "<identity>"
material_inputs:
  - input_ref: "<material input>"
    revision_or_digest: "<identity>"
environment_constraints:
  - constraint_ref: "<declared environment constraint, if material>"
    revision_or_digest: "<exact observed identity>"
completeness: "COMPLETE | INCOMPLETE | UNKNOWN"
manifest_digest: "<semantic digest>"
created_at: "<timestamp>"
```

Rules:

- Only input classes declared materially relevant by the Task Contract, Plan Contract, Execution Envelope, Project-specific requirement, or applicable policy participate in binding identity. Irrelevant environment noise does not invalidate an execution.
- A required unknown material input prevents a complete manifest. A requirement cannot be relaxed post hoc merely to make an execution complete.
- Actual secret values MUST NOT enter the manifest. Only non-secret references/revisions/digests may be recorded where required.
- Mutable business/runtime facts remain R4 current truth unless deliberately and lawfully frozen as execution inputs.

## 6. Execution State Binding

`record_type: EXECUTION_STATE_BINDING` is an immutable description of the exact materially relevant execution state for one execution attempt. It is evidence, not authority.

```yaml
record_type: EXECUTION_STATE_BINDING
record_version: "1.0"
state_binding_ref: "<contract-local reference>"
project_ref: "<Project>"
task_ref: "TASK-xxx"
execution_ref: "<runtime/contract-local execution attempt>"
digest_profile_ref: "<canonicalization + digest profile>"
source_state:
  revision_set_ref: "<Revision Set>"
  revision_set_digest: "<digest>"
execution_inputs:
  input_manifest_ref: "<Input Manifest>"
  input_manifest_digest: "<digest>"
current_truth:
  r4_context_ref: "<state-bound R4 observation>"
  observed_revision_or_digest: "<when source supports it>"
  observed_at: "<timestamp>"
authority:
  authority_refs: ["<AUTH/user authority refs>"]
  evaluation_ref: "<state-bound dispatch evaluation>"
  observed_revision_or_digest: "<when source supports it>"
  evaluated_at: "<timestamp>"
ownership:
  ownership_ref: "<grant>"
  ownership_domain_ref: "<domain>"
  ownership_scope_ref: "<scope>"
  owner_ref: "<executor>"
  ownership_epoch: "<scoped generation>"
  assurance_at_dispatch: "COORDINATION_ONLY | ACCEPTANCE_FENCED | SIDE_EFFECT_FENCED"
  ownership_evidence_ref: "<state-bound evidence>"
workspace:
  workspace_ref: "<governed workspace>"
  workspace_identity_ref: "<state-bound identity>"
  observed_at: "<timestamp>"
completeness: "COMPLETE | INCOMPLETE | UNKNOWN"
binding_digest: "<semantic digest>"
binding_created_at: "<timestamp>"
```

Rules:

- Binding references that affect immutable identity MUST resolve to state-bound/reconstructable evidence. A mutable `current`, branch, locator, or `latest` pointer alone is insufficient historical binding evidence.
- A complete binding does not make authority, ownership, R4, or downstream eligibility permanently valid. Material mutable truth is fresh-revalidated at the appropriate boundary.

## 7. Digest interoperability profile

Any semantic digest intended to compare identity across records or systems MUST declare or inherit a compatible `digest_profile_ref` describing at minimum:

- canonicalization/normalization profile;
- digest algorithm identity;
- profile version.

This applies to Revision Set, Input Manifest, State Binding, Result Set, and semantic Transition request fingerprints when digests are used.

```text
same bytes/digest text under incompatible profile
≠ proven semantic identity
```

ProjectFramework defines digest-profile semantics only. It does not implement cryptography, a canonicalization service, key management, or a signing runtime.

## 8. Operational transition, CAS, and idempotency

Operational state ordering belongs to the declared execution-state owner and its authoritative aggregate version. Timestamp order is audit evidence, not transition authority.

Conceptual aggregate:

```yaml
aggregate_ref: "<execution aggregate>"
task_ref: "TASK-xxx"
execution_ref: "<attempt>"
current_state: "<operational execution state>"
current_version: "<monotonic version within aggregate>"
last_transition_ref: "<record>"
```

`record_type: OPERATIONAL_TRANSITION` is the evidence of a transition request/outcome:

```yaml
record_type: OPERATIONAL_TRANSITION
record_version: "1.0"
transition_id: "<unique operation ref>"
idempotency_key: "<retry identity>"
request_digest_profile_ref: "<semantic digest profile>"
request_semantic_digest: "<digest of intended semantic operation>"
aggregate_ref: "<aggregate>"
expected_version: "<version>"
expected_state: "<state>"
requested_state: "<state>"
causation_ref: "<cause>"
correlation_ref: "<correlation>"
authority_refs: ["<authority>"]
ownership_evidence_ref: "<ownership>"
state_binding_ref: "<binding when applicable>"
result: "<exactly one applicable outcome>"
observed_at: "<timestamp>"
```

The outcome is exactly one of the applicable outcomes:

```text
ACCEPTED
DUPLICATE_ACCEPTED
VERSION_CONFLICT
STATE_CONFLICT
IDEMPOTENCY_CONFLICT
AUTHORITY_REJECTED
OWNERSHIP_REJECTED
PRECONDITION_REJECTED
INVALID_TRANSITION
UNKNOWN
```

Evaluation order is semantically:

1. Resolve whether the same idempotency operation was already durably accepted.
2. An exact accepted duplicate returns `DUPLICATE_ACCEPTED`.
3. The same idempotency key with a different semantic request fingerprint returns `IDEMPOTENCY_CONFLICT`.
4. Otherwise evaluate expected aggregate version/state.
5. Evaluate current authority/ownership/preconditions.
6. Atomically apply the transition in the execution-state owner.
7. Persist/return the observed outcome.

Rules:

- A timeout is not evidence of failure. `UNKNOWN` requires authoritative reconciliation before unsafe retry.
- The Operational Transition Record is evidence of what the state owner observed/applied; it does not itself become the state authority.

## 9. Result observation and Result Acceptance

### 9.1 Result Observation

The Task Record remains the historical execution observation. It may state an observed outcome:

```text
SUCCEEDED | FAILED | PARTIAL | UNKNOWN
```

Observed success is not result eligibility. Observed failure may still be a valid governed result for verification/recovery.

### 9.2 Generic Result Identity

Universal result identity is generalized beyond Git:

```yaml
result_identity:
  kind: "GIT_REVISION_SET | OPERATIONAL_OBSERVATION | EXTERNAL_TRANSACTION | ARTIFACT | DEPLOYMENT_STATE | OTHER_SOURCE_NATIVE"
  source_native_ref: "<owner/source ref>"
  exact_identity: "<kind-specific exact identity>"
  digest_profile_ref: "<when digest participates in identity>"
  identity_digest: "<when applicable>"
  completeness: "COMPLETE | INCOMPLETE | UNKNOWN"
  observed_at: "<timestamp>"
```

Examples:

- Git: exact Revision Set, preserving repository + exact commit SHA semantics for single-repository work.
- ERP/business observation: source system, operation/query, `source_as_of`, business date, timezone, result digest.
- External mutation: target resource, source-native transaction ID, requested-effect digest, resulting-state evidence.

Timestamp alone is never a universal immutable result identity.

### 9.3 Result Set

When one execution produces multiple material outputs, membership is explicit:

```yaml
result_set:
  membership_basis_ref: "<Task Contract / Expected IPOCV basis>"
  members: ["<result identities>"]
  coverage: "COMPLETE | PARTIAL | UNKNOWN"
  digest_profile_ref: "<profile>"
  result_set_digest: "<semantic digest>"
```

Result identity completeness is separate from execution success.

### 9.4 Acceptance is a derived evaluation

`record_type: RESULT_ACCEPTANCE` is a state-bound derived evaluation, not a new canonical truth owner. It consumes the applicable canonical/source-native truths.

```yaml
record_type: RESULT_ACCEPTANCE
record_version: "1.0"
acceptance_ref: "<immutable evaluation instance>"
task_ref: "TASK-xxx"
execution_ref: "<attempt>"
task_record_ref: "<observation>"
state_binding_ref: "<binding>"
evaluated_against:
  task_lifecycle_ref: "<Task Source observation>"
  authority_evaluation_ref: "<fresh AUTH evaluation>"
  ownership_evidence_ref: "<fresh ownership evidence>"
  r4_context_ref: "<fresh applicable current truth>"
  operational_aggregate_ref: "<aggregate>"
  aggregate_version: "<version>"
disposition: "ELIGIBLE | STALE_OWNERSHIP | TASK_NOT_ACTIVE | AUTHORITY_INVALID | STATE_BINDING_INVALIDATED | DUPLICATE | STATE_CONFLICT | RESULT_IDENTITY_INCOMPLETE | PRECONDITION_FAILED | UNKNOWN"
evidence_refs: ["<evidence>"]
evaluated_at: "<timestamp>"
```

Rules:

- Historical acceptance evaluations are immutable. Current promotability uses the exact latest applicable state-bound evaluation for the current decision boundary; no global newest-timestamp rule is implied.
- A stale ownership result remains historical evidence but cannot be promoted. Cancellation, authority invalidity, incomplete result identity, or unresolved material truth similarly block promotable verification.

## 10. Execution ownership, scoped epoch, and fencing assurance

### 10.1 Claim versus ownership

```text
Coordination Claim ≠ Execution Ownership Grant
```

Multica remains a coordination/claim owner unless an explicit future architecture gives another service a stronger declared execution-state role. The declared execution-control owner grants authoritative execution ownership. No executor self-grants ownership or AUTH.

### 10.2 Ownership Grant

```yaml
record_type: EXECUTION_OWNERSHIP_GRANT
record_version: "1.0"
ownership_ref: "<contract-local ref>"
ownership_domain_ref: "<declared execution-control domain>"
ownership_scope_ref: "<bounded scope, normally execution attempt>"
task_ref: "TASK-xxx"
execution_ref: "<attempt>"
owner_ref: "<executor>"
ownership_epoch: "<generation within domain/scope>"
coordination_claim_ref: "<claim when applicable>"
granted_at: "<timestamp>"
validity_basis:
  mode: "LEASE_BASED | EXPLICIT_REVOCATION | SOURCE_NATIVE"
  evidence_ref: "<source-native basis>"
fencing_requirement:
  minimum_assurance: "COORDINATION_ONLY | ACCEPTANCE_FENCED | SIDE_EFFECT_FENCED"
grant_evidence_ref: "<evidence>"
```

Epoch rules:

- Epochs are comparable only within the same ownership domain and scope.
- Continuous lease renewal of one ownership generation does not increment the epoch.
- Reassignment or reacquisition after ownership termination creates a new epoch, even if the same executor returns.

### 10.3 Ownership state and evidence

Observed ownership state is:

```text
ACTIVE | SUSPECT | EXPIRED | REVOKED | COMPLETED | UNKNOWN
```

`SUSPECT` and `UNKNOWN` are not proof of current ownership and fail closed where current ownership is materially required.

### 10.4 Fencing assurance

Ordered stale-owner protection levels, in single-line canonical form:

```text
COORDINATION_ONLY < ACCEPTANCE_FENCED < SIDE_EFFECT_FENCED
```

Expanded:

```text
COORDINATION_ONLY
       <
ACCEPTANCE_FENCED
       <
SIDE_EFFECT_FENCED
```

- `COORDINATION_ONLY`: assignment coordination only; stale side effects remain possible.
- `ACCEPTANCE_FENCED`: stale results cannot become governed accepted results, but stale external effects may still have happened.
- `SIDE_EFFECT_FENCED`: the target/source-native system rejects the stale ownership generation before the governed effect is applied.

Rules:

- Assurance is evaluated per material operation path/target, not merely per executor. A runtime cannot silently downgrade a required assurance level.
- Unknown possibly-applied non-idempotent stale effects require `RESULT_VERIFICATION_REQUIRED` before unsafe retry or reassignment.
- Correct epoch claims do not prove producer authentication; cryptographic producer identity belongs to Wave B.

## 11. Verification basis, evidence, result, and validity

### 11.1 Verification Basis

Promotable verification starts only from a current applicable `ELIGIBLE` Result Acceptance.

```yaml
verification_basis:
  task_contract_ref: "<contract>"
  task_record_ref: "<observation>"
  result_acceptance_ref: "<exact immutable acceptance evaluation used to begin verification>"
  state_binding_ref: "<exact execution binding>"
  accepted_result_ref: "<exact result/result set>"
  verification_requirements_ref: "<requirements>"
  verification_current_truth:
    r4_context_ref: "<verification-time current truth>"
    observed_at: "<timestamp>"
```

Execution-time R4 and verification-time R4 may differ. The basis pins the exact acceptance evaluation used to begin VERIFY. Before promoting `VERIFYING → VERIFIED`, acceptance is freshly re-evaluated and must still be `ELIGIBLE`.

### 11.2 Verification Evidence Assessment

Required evidence may be assessed as:

```text
PASS | FAIL | FLAKY | UNTRUSTED | INCOMPLETE | UNKNOWN
```

Any required `FAIL`, `FLAKY`, `UNTRUSTED`, `INCOMPLETE`, or `UNKNOWN` evidence prohibits overall Verification `PASS` unless an applicable requirement was already governed as optional/advisory or an explicit pre-governed variance basis applies. The Verifier cannot relax requirements post hoc.

Expected-vs-Actual IPOCV remains exactly:

```text
MATCH | ACCEPTED_VARIANCE | MISMATCH | UNKNOWN
```

`ACCEPTED_VARIANCE` requires a governed basis.

### 11.3 Verification Result remains unchanged

The Verification Record result remains exactly:

```text
PASS | FAIL | UNKNOWN
```

Do not overload this enum with freshness/validity states.

### 11.4 Verification Validity is separate

Historical Verification Records are immutable. Current proof usability is evaluated separately:

```yaml
record_type: VERIFICATION_VALIDITY_EVALUATION
record_version: "1.0"
validity_ref: "<immutable evaluation instance>"
verification_record_ref: "<historical verification>"
evaluated_against:
  state_binding_ref: "<applicable state>"
  result_acceptance_ref: "<current applicable acceptance>"
  current_truth_ref: "<current truth>"
  dependency_state_refs: ["<dependencies>"]
  target_state_refs: ["<targets when applicable>"]
state: "CURRENT | STALE | INVALIDATED | UNKNOWN"
reason_refs: ["<reason/evidence>"]
invalidated_by: "<cause or NOT_APPLICABLE>"
evaluated_at: "<timestamp>"
```

- `CURRENT`: proof remains usable for its exact applicable scope.
- `STALE`: freshness is insufficient; incompatibility is not yet proven.
- `INVALIDATED`: a known material incompatibility/invalidation condition exists.
- `UNKNOWN`: current applicability cannot be established.

Rules:

- A historical `PASS` is not rewritten to `FAIL` merely because validity changes.
- Selective invalidation is allowed only when the affected scope can be bounded safely; unknown material impact fails closed.
- Task lifecycle eligibility and AUTH are still independent gates. Task cancellation or later AUTH revocation does not automatically rewrite technical verification truth; it blocks new governed actions according to its own authority domain.

## 12. Operational state guards after Wave A V2

The Framework `1.19.0` operational execution-state domain remains:

```text
PROPOSED
→ READY_FOR_CLAIM
→ CLAIMED
→ EXECUTING
→ RESULT_RECORDED
→ VERIFYING
→ VERIFIED
→ INTEGRATION_PENDING
→ INTEGRATED
→ CLOSED
```

Exception states remain compatible with `VERIFICATION_FAILED | BLOCKED | CANCELLED | STALE`.

Wave A V2 strengthens the representative guards as follows:

```text
PROPOSED → READY_FOR_CLAIM
requires Task Ready Gate PASS

READY_FOR_CLAIM → CLAIMED
requires eligible executor + applicable coordination claim

CLAIMED → EXECUTING
requires current Execution Ownership Grant
       + complete Execution State Binding finalized after the grant
       + required fencing assurance available
       + current applicable AUTH
       + applicable current R4
       + compatible workspace identity
       + accepted CAS transition

EXECUTING → RESULT_RECORDED
requires Task Record + Actual IPOCV + sufficient result observation/identity

RESULT_RECORDED → VERIFYING
requires current applicable Result Acceptance = ELIGIBLE
       + complete Verification Basis

VERIFYING → VERIFIED
requires Verification Record result = PASS
       + validity_at_verification = CURRENT
       + fresh applicable Result Acceptance = ELIGIBLE

VERIFIED → INTEGRATION_PENDING
requires integration applicability plus existing downstream eligibility

INTEGRATION_PENDING → INTEGRATED
requires source-native integration readback + reconciliation PASS

VERIFIED/INTEGRATED → CLOSED
requires applicable completion reconciliation
```

Rules:

- Operational Execution State still MUST NOT directly mutate canonical Task lifecycle.
- Result Acceptance and Verification Validity are dimensions/evaluations, not additional execution states.

## 13. Failure and recovery semantics

Wave A uses four conceptual failure classes without creating another lifecycle:

**A. Preconditions unresolved** — required revision missing, required input unknown, AUTH unknown, ownership unknown, R4 materially stale, workspace mismatch, required fencing unavailable. Behavior: do not begin the affected Material operation.

**B. Observation exists but is not eligible** — a stale executor really produced a result. Behavior: retain the factual observation; do not promote it.

**C. Ambiguous side effect** — a non-idempotent external request may have been applied before a transport failure. Behavior: `RESULT_VERIFICATION_REQUIRED`; reconcile at the source-native truth owner before unsafe retry.

**D. Historical proof exists but cannot currently be used** — Verification `PASS` exists but candidate/input/dependency state materially changed. Behavior: retain the historical `PASS`; current validity becomes `STALE`, `INVALIDATED`, or `UNKNOWN` as supported by evidence.

`UNKNOWN` mandatory truth never becomes `PASS` by convenience and must be resolved at the relevant truth owner.

## 14. Crash and interruption semantics

- Transition submitted, response lost: reconcile using transition/idempotency identity and authoritative aggregate state. An exact previously applied operation may return `DUPLICATE_ACCEPTED`; otherwise the outcome is `UNKNOWN` until resolved.
- Side effect occurred, Task Record missing: absence of a Task Record is not evidence of absence of effect. Inspect source-native truth. A confirmed effect may be represented by a reconstructed observation only from durable evidence; do not invent unknown IPOCV/result facts. Unknown effect requires verification before retry.
- Task Record exists, Acceptance missing: fresh-evaluate acceptance; do not re-execute merely because the evaluation record is absent.
- Verification `PASS` exists, controller restarted: reuse the exact proof only while its basis remains unchanged and current validity is established; downstream gates still fresh-resolve their mutable truth.

Wave A establishes safe reconstruction/reconciliation semantics only. It does not authorize or implement automatic continuation. Wave B owns Resume Eligibility and Continuation Budget.

## 15. Reassignment safety

Loss of liveness/ownership does not automatically authorize another worker to repeat potentially non-idempotent work. A Reassignment Gate must consider:

- prior ownership state and epoch;
- whether prior result/effects are known;
- operation idempotency;
- available fencing assurance;
- source-native reconciliation status.

Conceptual outcomes:

```text
REASSIGNABLE
RESULT_VERIFICATION_REQUIRED
MANUAL_REVIEW_REQUIRED
BLOCKED
UNKNOWN
```

These are evaluation outcomes, not a new Project Stable-ID family or Task lifecycle.

## 16. Backward compatibility and record-version rule

### 16.1 Framework 1.19 exact-SHA compatibility

Existing Framework `1.19.0` Task Records and Verification Records remain valid under the contract version that created them. A Git-backed `candidate_identity` may be viewed by a V2 consumer as a one-member `GIT_REVISION_SET` only when the existing evidence is sufficient. Historical files are not rewritten merely to normalize them into V2.

### 16.2 No Brownfield reconstruction

Historical Tasks MUST NOT receive invented Revision Sets, Input Manifests, State Bindings, ownership epochs, Result Acceptances, or Validity Evaluations. Unresolvable historical mapping remains `UNKNOWN`.

### 16.3 Record versioning

Wave A V2 MUST NOT silently redefine the required serialized meaning of an existing `record_version: "1.0"` record in place. This amendment allocates the successor versions:

- Task Contract: `contract_version: "2.0"` for the V2 required shape.
- Task Record: `record_version: "2.0"` for the V2 required shape.
- Verification Record: `record_version: "2.0"` for the V2 required shape.
- New Wave A record types use `record_version: "1.0"` because they are new record types: `REVISION_SET`, `EXECUTION_INPUT_MANIFEST`, `EXECUTION_STATE_BINDING`, `EXECUTION_OWNERSHIP_GRANT`, `EXECUTION_OWNERSHIP_EVIDENCE`, `OPERATIONAL_TRANSITION`, `RESULT_ACCEPTANCE`, `VERIFICATION_VALIDITY_EVALUATION`.

Historical version `1.0` Task Contract / Task Record / Verification Record artifacts remain valid according to their original contract. Existing Plan Contract `1.0`, Executor Profile, capability/tool/trust profiles, Task lifecycle, Risk `R0–R3`, and the Registered Command set remain unchanged.

## 17. Wave B / Wave C exclusions

Wave A V2 explicitly does NOT include, and no Wave A surface may leak:

- Resume Eligibility, Continuation Budget, or automatic continuation semantics (Wave B).
- Memory Snapshot or checkpoint/restore execution semantics (Wave B).
- Cryptographic producer authentication, signing, or key management (Wave B).
- Release Transaction, deployment saga, or multi-system transactional release semantics (Wave C).
- Any runtime implementation (Section 18).

## 18. ProjectFramework versus runtime boundary

ProjectFramework defines:

- declarative record/contract semantics;
- truth-domain ownership and reference requirements;
- fail-closed eligibility and invalidation behavior;
- required ordering/guards;
- interoperability invariants;
- no-inference/no-history-rewrite rules.

A declared runtime (AI-ControlTower or another explicitly governed owner) may implement:

- operational aggregate storage/versioning;
- atomic compare-and-set;
- idempotency storage/duplicate detection;
- ownership grant/revoke and epoch generation;
- leases/heartbeats if selected;
- fencing token issuance/enforcement;
- target/source-native fencing integration;
- execution routing;
- transition/result/evaluation persistence;
- runtime reconciliation.

ProjectFramework MUST NOT add a task database, event store, queue, scheduler, worker daemon, lease service, heartbeat daemon, distributed lock, fencing-token generator, runtime CAS store, automatic transition engine, model router, automatic acceptance engine, verification daemon, executable Project Adapter, API server, merge bot, or automatic Task-DONE updater merely to satisfy this design.

## 19. Integrated pressure-scenario contract

This amendment is accepted only together with pressure scenarios `557–590` in `tests/pressure-scenarios.md`, which cover the 34 design-level scenario classes: identity/input, transition/race, ownership/fencing, result/acceptance, verification, and compatibility/boundary — including the two corrected cross-section cases: ownership grant before State Binding finalization, and Result Acceptance revalidation immediately before `VERIFIED` promotion.

## 20. Completion and review gate

This amendment is `CONTRACT_READY` (not `IMPLEMENTED`, not `RELEASED`) when:

```text
spec Sections 1–6 explicitly approved
+ written spec self-review passes
+ integrated roleplay has no unresolved P0 semantic gap
+ canonical ordering uses Ownership Grant before State Binding finalization
+ VERIFIED promotion fresh-checks Result Acceptance ELIGIBLE
+ state-bound references are reconstructable rather than mutable-latest only
+ no authority leak
+ no timestamp-based ordering authority
+ no silent UNKNOWN → PASS normalization
+ no stale-owner promotion
+ no historical truth rewrite
+ no Git-only universal assumption
+ no Brownfield retrofit
+ no Wave B/C semantic leakage
+ Framework 1.19 compatibility rule is explicit
+ no runtime implementation is introduced
```

`CONTRACT_READY ≠ IMPLEMENTED ≠ RELEASED.` Local implementation authority does not imply push, PR, merge, tag, GitHub Release, or canonical post-1.20 self-host promotion.
