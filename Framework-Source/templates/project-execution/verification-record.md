# Verification Record Template

Declarative **state-bound** verification result for one Task. A Verification Record is bound to an exact observed candidate and the resolved current truth it was checked against.

```yaml
record_type: VERIFICATION_RECORD
record_version: "1.0"
task_ref: "TASK-xxx"
plan_ref: "<path or embedded reference to the Plan Contract, if separate>"
task_record_ref: "<reference to the Task Record>"
verified_candidate:
  repository: "<canonical repository>"
  commit_sha: "<exact observed commit SHA>"
  tree_sha: "<exact observed tree SHA>"
  worktree_or_branch_ref: "<observed ref, routing only>"
  observed_at: "<timestamp of candidate observation>"
resolved_current_truth_ref: "<reference to the resolved R4 current-truth context>"
acceptance_results:
  - criterion: "<Task Contract acceptance criterion>"
    result: "<observed result>"
ipocv_comparison:
  input: "MATCH | ACCEPTED_VARIANCE | MISMATCH | UNKNOWN"
  process: "MATCH | ACCEPTED_VARIANCE | MISMATCH | UNKNOWN"
  output: "MATCH | ACCEPTED_VARIANCE | MISMATCH | UNKNOWN"
  control: "MATCH | ACCEPTED_VARIANCE | MISMATCH | UNKNOWN"
  verification: "MATCH | ACCEPTED_VARIANCE | MISMATCH | UNKNOWN"
control_results:
  - "<control check and observed result>"
verification_evidence:
  - "<EVD-* or source-native evidence reference>"
result: "PASS | FAIL | UNKNOWN"
invalidation_conditions:
  - "<condition that invalidates this verification result>"
```

Rules:

- `result` is exactly `PASS | FAIL | UNKNOWN.` Verification `PASS` is evidence for the **exact observed state**, not permanent universal truth.
- **IPOCV comparison** is exactly `MATCH | ACCEPTED_VARIANCE | MISMATCH | UNKNOWN.` `ACCEPTED_VARIANCE` requires a governed basis; `MISMATCH` cannot verify; applicable `UNKNOWN` fails closed.
- The record binds to an exact candidate. `Verification PASS(candidate A) ≠ Verification PASS(candidate B).` Material change after `PASS` invalidates affected proof.
- VERIFY MUST NOT rewrite Expected IPOCV or acceptance criteria merely to make execution pass.
- Task Verification and Framework `RELEASE_FULL` remain different proof domains. This record may reference exact valid release evidence but does not clone or redefine that proof.
- This file is a state-bound verification result. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No runtime, verification daemon, or automatic verifier is implied by this record.

## Framework 1.20 V2 shape (TASK-058)

For Wave A V2 execution, the Verification Record starts from an exact Verification Basis and separates result from current validity:

```yaml
record_type: VERIFICATION_RECORD
record_version: "2.0"
task_ref: "TASK-xxx"
# ... all v1 fields remain required as above ...
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
evidence_assessment:
  - requirement: "<required verification input or proof domain>"
    assessment: "PASS | FAIL | FLAKY | UNTRUSTED | INCOMPLETE | UNKNOWN"
result: "PASS | FAIL | UNKNOWN"
validity_at_verification: "CURRENT | STALE | INVALIDATED | UNKNOWN"
```

Rules:

- Promotable verification starts only from a current applicable `ELIGIBLE` Result Acceptance and a complete Verification Basis.
- Any required `FAIL`, `FLAKY`, `UNTRUSTED`, `INCOMPLETE`, or `UNKNOWN` evidence assessment prohibits overall `result: PASS` absent a pre-governed optional/advisory or variance basis. The Verifier cannot relax requirements post hoc.
- `result` remains **exactly** `PASS | FAIL | UNKNOWN` and is never overloaded with freshness states. `validity_at_verification` is the separate current-usability dimension; a later validity change is recorded in a `VERIFICATION_VALIDITY_EVALUATION`, never by rewriting this record.
- Before `VERIFYING → VERIFIED`, the current applicable Result Acceptance MUST be freshly re-evaluated and remain `ELIGIBLE.`
- **Compatibility:** existing v1 Verification Records stay historical and exact-SHA bound under their original contract; they are never rewritten into V2.