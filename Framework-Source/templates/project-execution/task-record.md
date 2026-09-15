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
