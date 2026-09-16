# TASK-058 — AI-ControlTower V4 Interoperability Wave A V2 Deterministic Execution Foundation Design

Date: `2026-09-16` (Asia/Bangkok)
Task: `TASK-058`
Design state: `SECTIONS_1_TO_6_USER_APPROVED / INTEGRATED_ROLEPLAY_PASS_WITH_CORRECTIONS / WRITTEN_SPEC_SELF_REVIEWED / WRITTEN_SPEC_USER_APPROVED`
Implementation state: `IMPLEMENTATION_PLAN_SELF_REVIEWED / EXECUTION_NOT_STARTED / SELF_HOST_RECONCILIATION_REQUIRED_BEFORE_IMPLEMENTATION`
Base distribution: ProjectFramework `1.19.0` / Project Source Schema `1.0.0` / release format `3`
Release classification: `ADDITIVE_EXECUTION_INTEROPERABILITY_CONTRACT_EVOLUTION`
Planned successor release: Framework `1.20.0` / Schema `1.0.0` / release format `3`, valid only if the fresh post-reconciliation baseline remains exactly Framework `1.19.0` with verified TASK-057 Framework-Source tree `23274ada739c56a10c8edcfc14e6a9a0e46e9a0b`; otherwise re-plan before normative mutation
Depends on: `TASK-057`
Runtime target: AI-ControlTower V4-compatible consumers; no AI-ControlTower runtime implementation is authorized by this design.

## 1. Source direction and purpose

ACTOR-001 directed on `2026-09-16`:

> `นำผล Roleplay นี้ไปสร้าง Wave A Design V2 โดยเริ่มจาก Execution State Binding + Operational Transition + Ownership/Fencing + Revision/Input/Result/Verification contracts และล็อก boundary ก่อนแตะ Wave B/C`

ACTOR-001 then explicitly approved Design V2 Sections 1 through 6 in sequence. After Section 6 approval, the integrated design roleplay was rerun across the complete composition. Two P0 cross-section consistency findings were corrected before this written specification was materialized:

1. `Execution State Binding` contains ownership generation evidence, therefore canonical execution ordering is `coordination claim → Execution Ownership Grant → finalize Execution State Binding → CAS transition to EXECUTING`, not State Binding before the ownership grant.
2. `VERIFYING → VERIFIED` requires not only a Verification Record `PASS` and verification validity `CURRENT`, but also a fresh applicable Result Acceptance evaluation that remains `ELIGIBLE`; result eligibility may change while verification is running.

After those corrections, the integrated design roleplay has no unresolved P0 semantic gap. This is a design-level assessment, not executable release verification.

Wave A V2 exists to answer one deterministic question:

> For this execution/result/verification, what exact materially relevant state was used, which ownership generation governed it, what effect/result was actually observed, was that result eligible for governed use, and is its verification proof still usable now?

The chosen architecture is **Compositional State Binding Hub**. It extends Framework 1.19 declarative execution governance without replacing the TASK-057 authority model and without creating a runtime/control plane inside ProjectFramework.

## 2. Non-negotiable authority and scope boundary

The TASK-057 authority model remains authoritative:

```text
ProjectFramework                         = governance / interoperability contract semantics
Project Source                           = canonical Project governance truth
Durable Task Source                      = canonical Task lifecycle truth
AUTH-* / explicit User authority         = mutation / operation authority
R4_CTX                                   = current mutable truth resolved from real owners
Project Adapter                          = owner / locator mapping only
Capability / Tool / Trust / Executor     = eligibility policy, not permission
Multica                                  = coordination / claim facts only by default
Declared execution-control owner         = operational execution / ownership state owner
Executor                                 = bounded work performer
Task Record                              = observed execution
Verification Record                      = historical state-bound verification result
Source-native systems                    = factual authority for state they own
```

Wave A V2 adds declarative semantics for:

```text
Revision Set
Execution Input Manifest
Execution State Binding
Operational Transition Record
Execution Ownership Grant / Evidence
Generic Result Identity / Result Set
Result Acceptance Evaluation
Verification Evidence Assessment
Verification Validity Evaluation
```

None of those records or evaluations becomes Project authority merely by existing.

Canonical invariants are:

```text
Contract ≠ Authority
State Binding ≠ Authority
Capability ≠ Authority
Eligibility ≠ Authority
Coordination Claim ≠ Execution Ownership
Execution Ownership ≠ AUTH
Ownership Epoch ≠ Authentication
Coordination Claim ≠ Fencing
Execution success ≠ Result Acceptance
Observation ≠ Acceptance
Accepted Result ≠ Verification PASS
Verification PASS ≠ Verification Validity CURRENT
Verification Validity CURRENT ≠ Task DONE
Task DONE ≠ OUT achieved
Task DONE ≠ MERGED ≠ PUSHED ≠ RELEASED ≠ ARTIFACT_PUBLISHED ≠ DEPLOYED
Timestamp ≠ ordering authority
Historical truth ≠ current eligibility
UNKNOWN ≠ PASS
Framework contract ≠ runtime implementation
```

This design creates no new Project Source semantic slot, Stable-ID family, Registered Command, Risk level, Task lifecycle, release-descriptor format, or authority system.

## 3. Wave boundary

### 3.1 In Wave A V2

Wave A owns declarative interoperability semantics for:

- stable resource identity versus locator versus exact revision;
- complete/partial/unknown Revision Sets;
- materially relevant execution input binding;
- immutable Execution State Binding;
- CAS/versioned operational transition semantics plus idempotency;
- execution ownership generation, scoped epoch, and fencing assurance;
- source-native Generic Result Identity / Result Set;
- factual Result Observation separated from Result Acceptance;
- Verification Evidence quality;
- historical Verification Result separated from current Verification Validity;
- fail-closed UNKNOWN/reconciliation behavior;
- additive compatibility with Framework 1.19 exact-SHA Tasks and Brownfield history.

### 3.2 Explicitly outside Wave A — Wave B

Wave A MUST NOT define or implement:

- Memory Generation / Derived Context Generation;
- atomic Memory Snapshot publication;
- tombstones / completeness watermark for derived memory;
- cryptographic producer identity;
- authenticated message/event envelope;
- signature, mTLS, key rotation, or anti-replay transport;
- Resume Eligibility Gate;
- controller-resumable execution mode;
- Continuation Budget or automatic GPT/MCP continuation controller.

Correct ownership epoch claims are not authenticated producer proof. Safe reconstruction of state after interruption is not permission to automatically resume execution.

### 3.3 Explicitly outside Wave A — Wave C

Wave A MUST NOT define or implement:

- build/artifact lifecycle or Artifact Set provenance workflow;
- Release Transaction / deployment saga;
- component deployment transaction semantics;
- health observation windows;
- migration reversibility;
- rollback / compensation engine;
- Project operational lifecycle for production orchestration.

`ARTIFACT` and `DEPLOYMENT_STATE` may appear only as generic source-native result-identity kinds. Result identity support does not create Wave C lifecycle semantics.

## 4. Canonical Wave A execution composition

The corrected canonical order is:

```text
PLAN / Task Contract / Execution Envelope
            ↓
Task Ready Gate PASS
            ↓
Executor eligibility selection
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

Before `VERIFYING → VERIFIED`, current applicable Result Acceptance MUST be freshly re-evaluated and remain `ELIGIBLE` in addition to Verification `PASS` and verification validity `CURRENT`.

No mega-record is introduced. Each record is single-responsibility and references the others.

## 5. Resource identity and Revision Set

### 5.1 Identity separation

```text
Resource Identity ≠ Locator ≠ Revision
```

A resource may move or be renamed without changing its logical identity. A locator is routing information. A revision is exact observed state.

No `RESOURCE-*` Project Stable-ID family is introduced. `resource_ref` may be a Project-owned identifier, Project Adapter mapping, or runtime-local identity whose scope is declared.

### 5.2 Revision Set semantic shape

```yaml
record_type: REVISION_SET
record_version: "<successor contract record version>"
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

- every declared required resource must resolve exactly for `COMPLETE`;
- optional missing resources do not block `COMPLETE` unless another contract makes them material;
- a single Git repository exact SHA is a valid one-member Revision Set;
- once referenced by an Execution State Binding, the Revision Set is immutable evidence;
- source change produces a new observation/set; historical evidence is never changed to `latest`;
- a digest is comparable only under a compatible `digest_profile_ref`.

## 6. Execution Input Manifest

Revision Set answers **which source state**. Execution Input Manifest answers **which materially relevant execution inputs**.

```yaml
record_type: EXECUTION_INPUT_MANIFEST
record_version: "<successor contract record version>"
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
completeness: "COMPLETE | INCOMPLETE | UNKNOWN"
manifest_digest: "<semantic digest>"
created_at: "<timestamp>"
```

Only input classes declared materially relevant by Task Contract, Plan Contract, Execution Envelope, Project-specific requirement, or applicable policy participate in binding identity. Irrelevant environment noise does not invalidate an execution.

Required unknown material input prevents a complete manifest. A requirement cannot be relaxed post hoc merely to make an execution complete.

Actual secret values MUST NOT enter the manifest. Only non-secret references/revisions/digests may be recorded where required. Mutable business/runtime facts remain R4 current truth unless deliberately and lawfully frozen as execution inputs.

## 7. Execution State Binding

Execution State Binding is an immutable description of the exact materially relevant execution state for one execution attempt. It is evidence, not authority.

```yaml
record_type: EXECUTION_STATE_BINDING
record_version: "<successor contract record version>"
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

Binding references that affect immutable identity MUST resolve to state-bound/reconstructable evidence. A mutable `current`, branch, locator, or `latest` pointer alone is insufficient historical binding evidence.

A complete binding does not make authority, ownership, R4, or downstream eligibility permanently valid. Material mutable truth is fresh-revalidated at the appropriate boundary.

## 8. Digest interoperability profile

Any semantic digest intended to compare identity across records or systems MUST declare or inherit a compatible `digest_profile_ref` describing at minimum:

- canonicalization/normalization profile;
- digest algorithm identity;
- profile version.

This applies to Revision Set, Input Manifest, State Binding, Result Set, and semantic Transition request fingerprints when digests are used.

```text
same bytes/digest text under incompatible profile
≠ proven semantic identity
```

ProjectFramework defines digest-profile semantics only. It does not implement cryptography, a canonicalization service, key management, or signing runtime.

## 9. Operational transition, CAS, and idempotency

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

Transition request:

```yaml
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
```

Transition outcome is exactly one of the applicable outcomes:

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

1. resolve whether the same idempotency operation was already durably accepted;
2. exact accepted duplicate returns `DUPLICATE_ACCEPTED`;
3. same idempotency key with a different semantic request fingerprint returns `IDEMPOTENCY_CONFLICT`;
4. otherwise evaluate expected aggregate version/state;
5. evaluate current authority/ownership/preconditions;
6. atomically apply the transition in the execution-state owner;
7. persist/return the observed outcome.

A timeout is not evidence of failure. `UNKNOWN` requires authoritative reconciliation before unsafe retry.

Operational Transition Record is evidence of what the state owner observed/applied; it does not itself become the state authority.

## 10. Result Observation and Result Acceptance

### 10.1 Result Observation

Task Record remains historical execution observation. It may state an observed outcome:

```text
SUCCEEDED | FAILED | PARTIAL | UNKNOWN
```

Observed success is not result eligibility. Observed failure may still be a valid governed result for verification/recovery.

### 10.2 Generic Result Identity

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

- Git: exact Revision Set, preserving repository + exact commit SHA semantics for single-repository work;
- ERP/business observation: source system, operation/query, `source_as_of`, business date, timezone, result digest;
- external mutation: target resource, source-native transaction ID, requested-effect digest, resulting-state evidence.

Timestamp alone is never a universal immutable result identity.

### 10.3 Result Set

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

### 10.4 Acceptance is a derived evaluation

Result Acceptance is a state-bound derived evaluation, not a new canonical truth owner. It consumes the applicable canonical/source-native truths.

```yaml
record_type: RESULT_ACCEPTANCE
record_version: "<successor contract record version>"
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

Historical acceptance evaluations are immutable. Current promotability uses the exact latest applicable state-bound evaluation for the current decision boundary; no global newest-timestamp rule is implied.

A stale ownership result remains historical evidence but cannot be promoted. Cancellation, authority invalidity, incomplete result identity, or unresolved material truth similarly block promotable verification.

## 11. Execution ownership, scoped epoch, and fencing assurance

### 11.1 Claim versus ownership

```text
Coordination Claim ≠ Execution Ownership Grant
```

Multica remains a coordination/claim owner unless an explicit future architecture gives another service a stronger declared execution-state role. The declared execution-control owner grants authoritative execution ownership.

### 11.2 Ownership Grant

```yaml
record_type: EXECUTION_OWNERSHIP_GRANT
record_version: "<successor contract record version>"
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

Epochs are comparable only within the same ownership domain and scope. Continuous lease renewal of one ownership generation does not increment epoch. Reassignment or reacquisition after ownership termination creates a new epoch, even if the same executor returns.

### 11.3 Ownership state and evidence

Observed ownership state is:

```text
ACTIVE | SUSPECT | EXPIRED | REVOKED | COMPLETED | UNKNOWN
```

`SUSPECT` and `UNKNOWN` are not proof of current ownership and fail closed where current ownership is materially required.

### 11.4 Fencing assurance

Ordered stale-owner protection levels are:

```text
COORDINATION_ONLY
       <
ACCEPTANCE_FENCED
       <
SIDE_EFFECT_FENCED
```

- `COORDINATION_ONLY`: assignment coordination only; stale side effects remain possible.
- `ACCEPTANCE_FENCED`: stale results cannot become governed accepted results, but stale external effects may still have happened.
- `SIDE_EFFECT_FENCED`: the target/source-native system rejects stale ownership generation before the governed effect is applied.

Assurance is evaluated per material operation path/target, not merely per executor. Runtime cannot silently downgrade a required assurance level.

Unknown possibly-applied non-idempotent stale effects require `RESULT_VERIFICATION_REQUIRED` before unsafe retry or reassignment.

Correct epoch claims do not prove producer authentication; cryptographic producer identity belongs to Wave B.

## 12. Verification Basis, Evidence, Result, and Validity

### 12.1 Verification Basis

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

Execution-time R4 and verification-time R4 may differ. The basis pins the exact acceptance evaluation used to begin VERIFY; before promoting `VERIFYING → VERIFIED`, acceptance is freshly re-evaluated and must still be `ELIGIBLE`.

### 12.2 Verification Evidence Assessment

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

### 12.3 Verification Result remains unchanged

Verification result remains exactly:

```text
PASS | FAIL | UNKNOWN
```

Do not overload this enum with freshness/validity states.

### 12.4 Verification Validity is separate

Historical Verification Records are immutable. Current proof usability is evaluated separately:

```yaml
record_type: VERIFICATION_VALIDITY_EVALUATION
record_version: "<successor contract record version>"
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

Historical `PASS` is not rewritten to `FAIL` merely because validity changes. Selective invalidation is allowed only when affected scope can be bounded safely; unknown material impact fails closed.

Task lifecycle eligibility and AUTH are still independent gates. A Task cancellation or later AUTH revocation does not automatically rewrite technical verification truth; it blocks new governed actions according to its own authority domain.

## 13. Operational state guards after Wave A V2

The Framework 1.19 operational execution-state domain remains:

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

Representative V2 guards are strengthened as follows:

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

Operational Execution State still MUST NOT directly mutate canonical Task lifecycle.

Result Acceptance and Verification Validity are dimensions/evaluations, not additional execution states.

## 14. Failure and recovery semantics

Wave A uses four conceptual failure classes without creating another lifecycle:

### A. Preconditions unresolved

Examples: required revision missing, required input unknown, AUTH unknown, ownership unknown, R4 materially stale, workspace mismatch, required fencing unavailable.

Behavior: do not begin the affected Material operation.

### B. Observation exists but is not eligible

Example: a stale executor really produced a result.

Behavior: retain factual observation; do not promote it.

### C. Ambiguous side effect

Example: non-idempotent external request may have been applied before transport failure.

Behavior: `RESULT_VERIFICATION_REQUIRED`; reconcile at the source-native truth owner before unsafe retry.

### D. Historical proof exists but cannot currently be used

Example: Verification `PASS` exists but candidate/input/dependency state materially changed.

Behavior: retain historical PASS; current validity becomes `STALE`, `INVALIDATED`, or `UNKNOWN` as supported by evidence.

`UNKNOWN` mandatory truth never becomes `PASS` by convenience and must be resolved at the relevant truth owner.

## 15. Crash and interruption semantics

- Transition submitted, response lost: reconcile using transition/idempotency identity and authoritative aggregate state; exact previously applied operation may return `DUPLICATE_ACCEPTED`; otherwise `UNKNOWN` until resolved.
- Side effect occurred, Task Record missing: absence of Task Record is not evidence of absence of effect. Inspect source-native truth. Confirmed effect may be represented by a reconstructed observation only from durable evidence; do not invent unknown IPOCV/result facts. Unknown effect requires verification before retry.
- Task Record exists, Acceptance missing: fresh-evaluate acceptance; do not re-execute merely because the evaluation record is absent.
- Verification PASS exists, controller restarted: reuse the exact proof only while its basis remains unchanged and current validity is established; downstream gates still fresh-resolve their mutable truth.

Wave A establishes safe reconstruction/reconciliation semantics only. It does not authorize or implement automatic continuation. Wave B owns Resume Eligibility and Continuation Budget.

## 16. Reassignment safety

Loss of liveness/ownership does not automatically authorize another worker to repeat potentially non-idempotent work.

A Reassignment Gate must consider:

- prior ownership state and epoch;
- whether prior result/effects are known;
- operation idempotency;
- available fencing assurance;
- source-native reconciliation status.

Conceptual outcomes are:

```text
REASSIGNABLE
RESULT_VERIFICATION_REQUIRED
MANUAL_REVIEW_REQUIRED
BLOCKED
UNKNOWN
```

These are evaluation outcomes, not a new Project Stable-ID family or Task lifecycle.

## 17. Backward compatibility and record-version rule

### 17.1 Framework 1.19 exact-SHA compatibility

Existing Framework 1.19 Task Records and Verification Records remain valid under the contract version that created them. A Git-backed `candidate_identity` may be viewed by a V2 consumer as a one-member `GIT_REVISION_SET` only when the existing evidence is sufficient. Historical files are not rewritten merely to normalize them into V2.

### 17.2 No Brownfield reconstruction

Historical Tasks MUST NOT receive invented Revision Sets, Input Manifests, State Bindings, ownership epochs, Result Acceptances, or Validity Evaluations. Unresolvable historical mapping remains `UNKNOWN`.

### 17.3 Record versioning

Wave A V2 MUST NOT silently redefine the required serialized meaning of an existing `record_version: "1.0"` record in place. If implementation changes required serialized shape or required fields, it MUST allocate a successor record version and document compatibility/mapping rules. Historical version `1.0` records remain valid according to their original contract.

The exact successor record-version numbers are implementation-plan allocation details and are intentionally not guessed in this design.

## 18. ProjectFramework versus AI-ControlTower runtime boundary

ProjectFramework defines:

- declarative record/contract semantics;
- truth-domain ownership and reference requirements;
- fail-closed eligibility and invalidation behavior;
- required ordering/guards;
- interoperability invariants;
- no-inference/no-history-rewrite rules.

AI-ControlTower or another declared runtime may implement:

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

## 19. Integrated roleplay / pressure-scenario contract

The written design MUST support at least these 34 design-level scenario classes before implementation is accepted:

### Identity / input

1. single Git repository exact-SHA compatibility;
2. required multi-repo member missing;
3. optional source missing;
4. unchanged Git SHA with changed material dependency/input;
5. resource locator changes while logical identity remains the same;
6. mutable AUTH/R4/current locator lacks reconstructable state-bound observation.

### Transition / race

7. two concurrent transitions CAS the same aggregate version;
8. accepted transition response is lost and exact operation is retried;
9. same idempotency key is reused for a different semantic operation;
10. transition transport timeout leaves outcome unknown;
11. Task cancellation races result recording.

### Ownership / fencing

12. continuous lease renewal preserves epoch;
13. lease/ownership terminates and same executor reacquires with a new epoch;
14. old executor reports after a newer ownership epoch is active;
15. Task requires `SIDE_EFFECT_FENCED` but path only provides `ACCEPTANCE_FENCED`;
16. stale worker may have produced an unknown non-idempotent side effect.

### Result / acceptance

17. successful result arrives after Task cancellation;
18. failed execution produces a complete valid governed failure result;
19. duplicate result report for the same exact identity;
20. one execution reports conflicting result identities;
21. non-Git ERP/source-as-of observation;
22. external mutation request was submitted but resulting state is unknown.

### Verification

23. same Git SHA but materially different Execution State Binding;
24. required flaky or untrusted evidence;
25. PASS followed only by freshness expiry;
26. PASS followed by known material candidate/input mutation;
27. one proof domain is selectively invalidated while others remain shown-equivalent;
28. material invalidation impact cannot be bounded.

### Compatibility / boundary

29. Framework 1.19 historical Task without V2 fields;
30. Project uses ProjectFramework without AI-ControlTower;
31. attempt to retrofit historical ownership/input state;
32. attempt to implement lease/CAS datastore inside ProjectFramework;
33. attempt to introduce Memory Snapshot/automatic continuation semantics into Wave A;
34. attempt to introduce Release Transaction/deployment-saga semantics into Wave A.

Integrated design roleplay also specifically checks the two corrected cross-section cases: ownership grant before State Binding finalization, and Result Acceptance revalidation immediately before VERIFIED promotion.

## 20. Wave A Design Exit Gate

Wave A V2 is `DESIGN_READY` only when:

```text
Sections 1–6 explicitly approved
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

`DESIGN_READY ≠ IMPLEMENTED ≠ RELEASED`.

## 21. Implementation prerequisite: canonical 1.19 self-host reconciliation

Fresh repository inspection on `2026-09-16` shows:

```text
Framework distribution: 1.19.0 / Schema 1.0.0
active ProjectFramework self-host FRAMEWORK-001: 1.18.0 / Schema 1.0.0
PROJECT-BOOTSTRAP.md: 1.18.0
active 01/03/09 Project Source: 1.18.0
TASK-057: DONE; no 1.19 self-host promotion occurred
```

This is a governance/release-state precondition, not a Wave A semantic defect.

TASK-058 normative Framework implementation MUST NOT begin while silently accumulating another release/self-host drift layer. Before implementation mutation starts, one of these must be freshly true under valid authority:

1. canonical ProjectFramework self-host reconciliation to Framework 1.19 is completed and verified; or
2. an exact separately governed implementation transaction explicitly includes the required 1.19 self-host reconciliation prerequisite with valid Root authority and verifies resulting state before successor release work proceeds.

The design/spec and local planning artifacts may exist before that reconciliation. No Root/Project Source promotion is authorized merely by this specification.

## 22. Expected implementation surfaces, not implementation authorization

A future approved implementation plan should minimize surface area and preserve single-responsibility files. Likely affected current surfaces include:

- current TASK-057 governance amendment successor/current normative amendment;
- `Framework-Source/references/core-governance-rules.md` projection;
- `Framework-Source/SKILL.md` operational guidance;
- `Framework-Source/templates/project-execution/` maintained contract starters;
- Task Record / Verification Record compatibility guidance;
- Project Adapter / Executor/Task Contract fields where required;
- `Framework-Source/MIGRATION-NOTES.md`;
- root README current release guidance as applicable;
- pressure scenarios and affected verification surfaces.

New maintained single-responsibility starters may be justified for `revision-set`, `execution-input-manifest`, `execution-state-binding`, ownership/transition/acceptance/validity records, but exact filenames and whether some structures should remain nested in existing records are implementation-plan decisions. This design does not authorize file proliferation by default.

## 23. Version and schema classification

Current design is intended as an additive Framework contract evolution because it does not change the Project Source semantic-slot model, Project Source Stable-ID families, canonical Task lifecycle, Risk `R0–R3`, Registered Commands, or release-descriptor format.

There is therefore no design-level requirement to change Project Source Schema family from `1.0.0`. The exact successor Framework version MUST be allocated only after fresh baseline/self-host reconciliation and implementation planning. A breaking incompatibility discovered during planning must trigger reclassification rather than being hidden behind the additive assumption.

## 24. Completion and review gate

Self-review result: `TASK058_SPEC_SELF_REVIEW PASS` — required semantic tokens PASS; pressure scenarios `1–34` contiguous/complete; TASK-058 registration/collision check PASS; placeholder scan has no unresolved placeholder marker; design-only diff hygiene PASS.

This written specification is ready for user review after:

- placeholder scan;
- internal consistency review;
- scope review;
- ambiguity review;
- design-only diff hygiene;
- local commit of the written spec and Task registration.

User approval of this written specification is required before invoking the implementation-planning workflow.

No implementation plan, normative Framework mutation, AI-ControlTower runtime change, Wave B design implementation, Wave C design implementation, push, tag, GitHub Release, Project Source Root promotion, or production/deployment action is authorized by this artifact.
