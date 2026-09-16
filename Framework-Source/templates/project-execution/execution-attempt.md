# Execution Attempt Template

Declarative record shape for one worker Attempt within a durable Operational Execution. Attempt state is runtime execution-control truth only; it is not canonical Task lifecycle truth and grants no authority.

```yaml
record_type: EXECUTION_ATTEMPT
record_version: "1.0"
execution_id: "<durable execution id>"
attempt_id: "<durable attempt id>"
executor_ref: "<selected executor>"
claim_ref: "<Multica/coordination claim ref or NOT_APPLICABLE>"

control_identity:
  runtime_generation: "<generation>"
  fence_epoch: "<epoch>"

lease:
  lease_ref: "<runtime lease ref>"
  acquired_at: "<runtime-authoritative time>"
  expires_at: "<runtime-authoritative time>"
  heartbeat_observed_at: "<time or NOT_OBSERVED>"

state: "<CREATED | RUNNABLE | RUNNING | WAITING | RECONCILING | TERMINATED | LOST | BLOCKED | CANCEL_REQUESTED>"

budget_lineage:
  root_execution_id: "<root>"
  parent_execution_id: "<parent or NOT_APPLICABLE>"
  allocated:
    model_turns: "<n>"
    tool_calls: "<n>"
    tokens: "<n>"
    wall_time: "<duration>"
    retries_per_action: "<n>"
    child_executions: "<n>"
    recursion_depth: "<n>"
  consumed:
    model_turns: "<n>"
    tool_calls: "<n>"
    tokens: "<n>"
    wall_time: "<duration>"

wait_or_block:
  reason: "<reason or NOT_APPLICABLE>"
  wake_event: "<event or NOT_APPLICABLE>"
  fallback_check_at: "<time or NOT_APPLICABLE>"

terminal_reason: "<reason or NOT_APPLICABLE>"
```

Rules:

- `Multica claim ≠ runtime lease ≠ runtime fence ≠ Effect Permit ≠ AUTH`.
- Heartbeat is liveness observation only.
- Executor-local clock is not lease authority.
- Child/recursive execution cannot manufacture authority or budget; parent consumption + child allocations remain within the root budget.
- Attempt `TERMINATED` or `LOST` **never directly closes** Operational Execution or canonical Task.
- A stale `(runtime_generation, fence_epoch)` cannot obtain a new governed Material Effect.