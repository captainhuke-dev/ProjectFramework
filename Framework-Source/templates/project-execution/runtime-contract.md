# Runtime Contract Template

Declarative **durable runtime-control** contract for one long-running governed execution: supervisor control generation, liveness projection, bounded continuation, and version pinning. This is the execution-runtime domain's top-level binding; it never replaces Framework 1.20 Execution State Binding, Ownership Grant, or AUTH.

```yaml
record_type: RUNTIME_CONTRACT
record_version: "1.0"
contract_ref: "<contract-local reference>"
execution_id: "<durable runtime execution id>"
task_ref: "TASK-xxx"
state_binding_ref: "<Wave A V2 Execution State Binding>"
runtime_contract_version: "<version>"
event_schema_version: "<version>"
control_generation: "<current runtime control generation>"
fence_epoch: "<monotonic epoch within generation>"
liveness:
  lease_mode: "RUNTIME_AUTHORITY_TIME | MONOTONIC_DURATION"
  lease_ref: "<lease identity when applicable>"
continuation_policy:
  continuation_budget: "<finite>"
  retry_budget: "<finite, per action class>"
  wake_conditions: ["<declared wake event / condition>"]
  fallback_check_at: "<time when applicable>"
disposition: "RUNNING | WAIT | BLOCKED | MANUAL_RESOLUTION_REQUIRED | BUDGET_EXHAUSTED | WAITING_FOR_REAUTHORIZATION | RECOVERY_BLOCKED | TERMINATED"
created_at: "<timestamp>"
```

Rules:

- `Supervisor decision != AUTH`; `Supervisor liveness != Execution Ownership Grant`; `Heartbeat != completion evidence`; `Runtime control generation != Project authority.`
- The runtime lease/heartbeat is a **subordinate liveness projection** to the Wave A V2 Execution Ownership Grant. No lease, heartbeat, or fence creates ownership or AUTH.
- The canonical fence identity is the pair `(runtime_generation, fence_epoch)`. Cross-generation numeric fence comparison is insufficient; stale-generation fence, lease, or permit attempts **fail closed.**
- A new control generation invalidates prior-generation runtime-local leases, fences, and Effect Permits. It never rewrites the Wave A V2 ownership epoch, Execution State Binding, or canonical Task state.
- A runtime-store restore to an older snapshot MUST NOT silently reuse old control identity: a governed successor generation is required before new effects, and former-generation unresolved effects are reconciled first.
- Continuation is governed by durable execution state, not model memory: finite continuation/retry budgets, declared wake conditions, and explicit dispositions. No invisible infinite loop; no automatic continuation after authority, state-binding, or contract invalidation.
- The end of an LLM turn is not completion. Task lifetime, model-turn lifetime, and worker lifetime remain separate.
- The contract pins `runtime_contract_version` and `event_schema_version.` Upgrades classify active executions as `BACKWARD_COMPATIBLE | REQUIRES_MIGRATION | INCOMPATIBLE`; incompatible runtime code never silently reinterprets historical runtime events.
- This file is runtime-domain contract evidence. It is not Root Governance, `AUTH-*`, Project Source, canonical Task lifecycle truth, or a Stable-ID family.
- No supervisor service, scheduler, daemon, lease/fencing service, CAS store, or automatic continuation engine is implied by this record.
