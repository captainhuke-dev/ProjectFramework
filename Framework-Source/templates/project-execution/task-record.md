# Task Record Template

Declarative record of **observed execution** for one Task. Task Record captures what actually happened; it does **not** rewrite the original Task Contract.

```yaml
record_type: TASK_RECORD
record_version: "1.0"
task_ref: "TASK-xxx"
plan_ref: "<path or embedded reference to the Plan Contract, if separate>"
task_contract_ref: "<path or reference to the Task Contract>"
execution_ref: "<bounded execution/commit/checkpoint reference>"
resolved_current_truth:
  context_ref: "<reference to the resolved R4 current-truth context>"
  observed_at: "<timestamp of the current-truth observation>"
actual_ipocv:
  input: "<observed inputs>"
  process: "<observed process>"
  output: "<observed outputs>"
  control: "<observed controls>"
  verification: "<observed verification>"
produced_artifacts:
  - "<source-native artifact reference>"
evidence_refs:
  - "<EVD-* or source-native evidence reference>"
candidate_identity:
  repository: "<canonical repository>"
  commit_sha: "<exact observed commit SHA>"
  tree_sha: "<exact observed tree SHA>"
  worktree_or_branch_ref: "<observed ref, routing only>"
  observed_at: "<timestamp of candidate observation>"
execution_result: "<observed execution outcome, e.g. COMPLETED | FAILED | UNKNOWN>"
```

Rules:

- **Actual IPOCV** is separate from **Expected IPOCV** (which lives in the Task Contract). Comparison is performed by VERIFY, not here.
- `candidate_identity` binds the record to an exact observed candidate. For Material Git-backed work the canonical identity is **repository + exact observed commit SHA**; branch/ref is a routing reference, not immutable evidence.
- `execution_result` is an **execution observation**. It is not a Verification result and does not imply `Verification PASS` or `Task DONE`.
- This file is an observation record. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No runtime, state engine, or automatic recorder is implied by this record.

## Framework 1.20 V2 shape (TASK-058)

For Wave A V2 execution, the Task Record adds state binding, generic result identity, and ownership-at-report:

```yaml
record_type: TASK_RECORD
record_version: "2.0"
task_ref: "TASK-xxx"
# ... all v1 fields remain required as above ...
state_binding_ref: "<Execution State Binding>"
result_observation: "SUCCEEDED | FAILED | PARTIAL | UNKNOWN"
result_identity:
  kind: "GIT_REVISION_SET | OPERATIONAL_OBSERVATION | EXTERNAL_TRANSACTION | ARTIFACT | DEPLOYMENT_STATE | OTHER_SOURCE_NATIVE"
  source_native_ref: "<owner/source ref>"
  exact_identity: "<kind-specific exact identity>"
  digest_profile_ref: "<when digest participates in identity>"
  identity_digest: "<when applicable>"
  completeness: "COMPLETE | INCOMPLETE | UNKNOWN"
  observed_at: "<timestamp>"
result_set_ref: "<Result Set when one execution produces multiple material outputs>"
ownership_at_report:
  ownership_ref: "<grant>"
  ownership_epoch: "<generation at report time>"
  state: "ACTIVE | SUSPECT | EXPIRED | REVOKED | COMPLETED | UNKNOWN"
```

Rules:

- `result_observation` is an **execution observation.** Observed success is not result eligibility; observed failure may still be a valid governed result for verification/recovery.
- Generic Result Identity is source-native and **not Git-only.** Timestamp alone is never a universal immutable result identity.
- `ownership_at_report` records the observed ownership state at report time; it does not re-grant or extend ownership.
- **Compatibility:** existing v1 `candidate_identity` stays valid historical exact-SHA evidence. A v1 Git-backed `candidate_identity` may be viewed by a V2 consumer as a one-member `GIT_REVISION_SET` **only when the existing evidence is sufficient** (repository + exact commit SHA present). The mapping is an explicit compatibility view; v1 records are never silently rewritten.