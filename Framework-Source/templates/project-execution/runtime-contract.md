# Runtime Contract Template

Declarative protocol starter for a runtime that enforces ProjectFramework Task execution. This file is **not** AUTH, Project Source, a scheduler, a runtime database, or executable runtime code.

```yaml
contract_type: RUNTIME_CONTRACT
contract_version: "1.0"
runtime_contract_version: "1.0"
event_schema_version: "1.0"
runtime_owner: "<execution-control runtime owner>"

lifecycle_domains:
  canonical_task: "TODO | IN_PROGRESS | DONE | BLOCKED | CANCELLED"
  operational_execution: "TASK-057 governed"
  execution_attempt: "CREATED | RUNNABLE | RUNNING | WAITING | RECONCILING | TERMINATED | LOST | BLOCKED | CANCEL_REQUESTED"
  action_effect: "PROPOSED | PREPARED | PERMITTED | DISPATCH_INTENT_RECORDED | DISPATCHED | ACKNOWLEDGED | RECONCILING | APPLIED | NOT_APPLIED | AMBIGUOUS | REJECTED"

supervisor:
  owns_runtime_transitions: true
  executor_proposals_are_advisory: true

control:
  runtime_generation: "<authoritative generation>"
  state_version_policy: COMPARE_AND_SET_EQUIVALENT
  fence_identity: "(runtime_generation, fence_epoch)"

journal:
  canonical_runtime_observation: RUNTIME_EVENT_JOURNAL
  checkpoint_authority: DERIVED_ONLY
  writer_isolation: REQUIRED

budget_root:
  max_model_turns: "<n or NOT_APPLICABLE>"
  max_tool_calls: "<n or NOT_APPLICABLE>"
  max_tokens: "<n or NOT_APPLICABLE>"
  max_wall_time: "<duration or NOT_APPLICABLE>"
  max_retries_per_action: "<n>"
  max_child_executions: "<n>"
  max_recursion_depth: "<n>"

wait_retry_policy:
  fail_closed_retry_forever: false
  external_truth: WAIT_WITH_WAKE_CONDITION
  manual_resolution: BLOCKED

upgrade_compatibility:
  class: "<BACKWARD_COMPATIBLE | REQUIRES_MIGRATION | INCOMPATIBLE>"

prohibited_authority_claims:
  - "Runtime decision does not create AUTH"
  - "Claim/Lease/Fence/Permit do not create AUTH"
  - "Runtime cannot set Verification PASS or Task DONE"
```

Required invariants:

```text
Runtime decision ≠ Authority
Model proposal ≠ Runtime decision
Runtime Event Journal > Checkpoint / Snapshot
Worker lifetime ≠ Execution lifetime
Execution lifetime ≠ Task lifecycle
```

A runtime implementation chooses its own language/storage/process model while preserving these semantics. This starter grants no permission to mutate any target.