# Execution Attempt Template

Declarative record/contract shape for one worker attempt inside one Operational Execution. Attempt state is runtime-control truth only and never canonical Task lifecycle truth.

```yaml
execution_attempt:
  execution_id: "<execution id>"
  attempt_id: "<attempt id>"
  executor_ref: "<selected executor>"
  claim_ref: "<Multica/coordination claim ref>"
  runtime_generation: "<control generation>"
  fence_epoch: "<monotonic epoch within generation>"
  attempt_state: "CREATED | RUNNABLE | RUNNING | WAITING | RECONCILING | TERMINATED | LOST | BLOCKED | CANCEL_REQUESTED"
  lease:
    granted_at_runtime: "<runtime-authoritative timestamp>"
    duration: "<bounded duration>"
    heartbeat_at: "<runtime-observed heartbeat>"
  budget_lineage:
    root_budget_id: "<root budget>"
    parent_budget_id: "<parent or NOT_APPLICABLE>"
    allocated: "<bounded allocation>"
    consumed: "<durable consumption>"
  parent_execution_id: "<parent or NOT_APPLICABLE>"
  root_execution_id: "<root>"
  recursion_depth: "<n>"
  wait_condition_ref: "<ref or NOT_APPLICABLE>"
  terminal_reason: "<reason or NOT_APPLICABLE>"
```

Rules:

- Attempt loss/termination does not close Operational Execution or canonical Task.
- Heartbeat is liveness observation, not AUTH or completion proof.
- Lease validity uses runtime-authoritative/monotonic time, not executor wall clock.
- Fence identity is `(runtime_generation, fence_epoch)`.
- A child Attempt/Execution cannot create new authority or budget by recursion.
