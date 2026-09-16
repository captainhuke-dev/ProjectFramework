# Task Record Template

Declarative record of **observed execution** for one Task. Task Record captures what actually happened; it does **not** rewrite the original Task Contract and does not become the fine-grained Runtime Event Journal.

```yaml
record_type: TASK_RECORD
record_version: "1.0"
task_ref: "TASK-xxx"
plan_ref: "<path or embedded reference to the Plan Contract, if separate>"
task_contract_ref: "<path or reference to the Task Contract>"
execution_ref: "<durable execution/commit/checkpoint reference>"
runtime_evidence:
  execution_id: "<runtime execution id or NOT_APPLICABLE>"
  attempt_refs:
    - "<Attempt ref relevant to the bounded result, or NONE>"
  checkpoint_ref: "<checkpoint ref relevant to recovery/result, or NOT_APPLICABLE>"
  journal_evidence_refs:
    - "<bounded journal/action evidence ref required to explain result, or NONE>"
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

- **Actual IPOCV** is separate from **Expected IPOCV**. VERIFY performs comparison.
- `candidate_identity` binds the record to an exact observed candidate. For Material Git-backed work, repository + exact observed commit SHA is canonical candidate identity; mutable branch/ref is routing only.
- `runtime_evidence` carries bounded references needed to explain the result/Actual IPOCV. It MUST NOT clone the Runtime Event Journal, Action/Effect stream, or every Attempt event.
- `Runtime Event Journal = fine-grained execution-control observation`; `Task Record = bounded observed result + Actual IPOCV used by VERIFY`.
- Verification consumes the Task Record plus source-native evidence, exact candidate identity, current truth, and declared requirements. It does not trust model narration or arbitrary raw runtime events as authority.
- `execution_result` is an execution observation; it does not imply Verification PASS or Task DONE.
- This record is not Root Governance, `AUTH-*`, Project Source, runtime authority, Task lifecycle truth, or a Stable-ID family.
- No runtime, state engine, or automatic recorder is implied by this record.