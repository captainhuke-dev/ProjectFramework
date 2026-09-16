# Execution Checkpoint Template

Derived recovery accelerator for a deterministic execution runtime. Checkpoint is **not** canonical runtime truth and cannot repair missing Runtime Event Journal truth by inference.

```yaml
record_type: EXECUTION_CHECKPOINT
record_version: "1.0"
execution_id: "<execution id>"
checkpoint_seq: "<checkpoint sequence>"
event_sequence: "<last included authoritative journal sequence>"
previous_checkpoint_hash: "<hash or NOT_APPLICABLE>"
state_version: "<runtime state version>"
resume_cursor: "<deterministic resume location>"

compatibility:
  runtime_contract_version: "1.0"
  event_schema_version: "1.0"

control_identity:
  runtime_generation: "<generation>"

unresolved_action_refs:
  - "<action ref or NONE>"

remaining_budget:
  model_turns: "<n or NOT_APPLICABLE>"
  tool_calls: "<n or NOT_APPLICABLE>"
  tokens: "<n or NOT_APPLICABLE>"
  wall_time: "<duration or NOT_APPLICABLE>"
  retries: "<bounded summary>"
  child_executions: "<n or NOT_APPLICABLE>"
  recursion_depth_remaining: "<n or NOT_APPLICABLE>"

derivation:
  source: RUNTIME_EVENT_JOURNAL
  through_event_sequence: "<sequence>"
  status: "<VALID | STALE | INVALID | UNKNOWN>"
```

Rules:

```text
Runtime Event Journal > Checkpoint / Snapshot
Checkpoint ahead of Journal = INVALID
Missing/corrupt Checkpoint != permission to invent runtime state
Journal discontinuity -> RECOVERY_BLOCKED unless governed recovery proves continuity
```

Recovery loads a compatible checkpoint when useful, then replays the journal tail. Model/chat memory is not a substitute for journal truth.