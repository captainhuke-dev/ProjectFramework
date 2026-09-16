# Runtime Contract Template

Declarative runtime-control contract for a future deterministic execution runtime. This file grants no authority and implements no runtime.

```yaml
runtime_contract:
  contract_version: "1.0"
  event_schema_version: "1.0"
  runtime_owner: "<AI_CONTROLTOWER_RUNTIME_OWNER>"
  task_ref: "TASK-xxx"
  execution_id: "<durable execution id>"
  task_contract_ref: "<task contract>"
  task_contract_fingerprint: "<semantic fingerprint>"
  plan_contract_fingerprint: "<fingerprint or NOT_APPLICABLE>"
  execution_envelope_fingerprint: "<fingerprint>"
  runtime_generation: "<control generation>"
  state_version: "<integer/CAS token>"
  journal:
    owner: RUNTIME_EVENT_JOURNAL
    append_only_logical_semantics: true
  checkpoint:
    authority: DERIVED_ONLY
  budget_root_ref: "<budget root>"
  wait_retry_policy_ref: "<policy>"
  runtime_upgrade_compatibility: "BACKWARD_COMPATIBLE | REQUIRES_MIGRATION | INCOMPATIBLE"
```

Required invariants:

```text
Runtime decision ≠ Authority
Model proposal ≠ Runtime decision
Runtime Event Journal > Checkpoint / Snapshot
Task lifecycle ≠ Operational Execution ≠ Attempt ≠ Action/Effect
Claim ≠ Lease ≠ Fence ≠ Authority
```

The runtime owns execution-control facts only. It MUST NOT own Project Source, Task lifecycle, AUTH, Verification PASS, Git/source-native truth, deployment/release truth, or OUT achievement.
