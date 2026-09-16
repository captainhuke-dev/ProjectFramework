# Task Record Template

Declarative record of **observed execution** for one Task. Task Record captures what actually happened; it does **not** rewrite the original Task Contract and does not become the fine-grained runtime journal.

```yaml
record_type: TASK_RECORD
record_version: "1.0"
task_ref: "TASK-xxx"
plan_ref: "<path or embedded reference to the Plan Contract, if separate>"
task_contract_ref: "<path or reference to the Task Contract>"
execution_ref: "<bounded execution reference>"
runtime_evidence_refs:
  execution_id: "<runtime execution id or NOT_APPLICABLE>"
  attempt_refs:
    - "<attempt ref only when needed to explain observed result>"
  checkpoint_ref: "<checkpoint ref or NOT_APPLICABLE>"
  journal_evidence_ref: "<bounded journal/evidence pointer or NOT_APPLICABLE>"
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
- Runtime references are bounded pointers needed to explain Actual IPOCV/result. **Runtime Event Journal = fine-grained execution-control observation; Task Record = bounded observed result used by VERIFY.** Task Record MUST NOT become an unbounded per-action event stream.
- `checkpoint_ref` never makes a Checkpoint authoritative over the Runtime Event Journal.
- `candidate_identity` binds the record to an exact observed candidate. For Material Git-backed work the canonical identity is **repository + exact observed commit SHA**; branch/ref is a routing reference, not immutable evidence.
- `execution_result` is an **execution observation**. It is not a Verification result and does not imply `Verification PASS` or `Task DONE`.
- This file is an observation record. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, runtime authority, or a Stable-ID family.
- No runtime, state engine, or automatic recorder is implied by this record.
