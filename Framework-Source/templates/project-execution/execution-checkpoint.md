# Execution Checkpoint Template

Derived recovery snapshot for one execution. A checkpoint accelerates recovery but never outranks the Runtime Event Journal.

```yaml
execution_checkpoint:
  execution_id: "<execution id>"
  checkpoint_seq: "<checkpoint sequence>"
  event_sequence: "<last authoritative journal event included>"
  previous_checkpoint_hash: "<hash or NOT_APPLICABLE>"
  state_version: "<runtime CAS/state version>"
  resume_cursor: "<deterministic resume location>"
  runtime_contract_version: "1.0"
  event_schema_version: "1.0"
  unresolved_action_refs:
    - "<action ref or NOT_APPLICABLE>"
  remaining_budget_summary: "<durable summary>"
  derived_at: "<runtime-authoritative time>"
```

Rules:

```text
Runtime Event Journal > Checkpoint / Snapshot
```

- A checkpoint is `DERIVED_ONLY` runtime recovery state.
- Missing/corrupt checkpoint may be rebuilt from continuous authoritative journal state when possible.
- Missing journal truth MUST NOT be repaired by inference from model/chat memory or a newer-looking checkpoint.
- Incompatible `runtime_contract_version` / `event_schema_version` requires governed compatibility handling before resume.
