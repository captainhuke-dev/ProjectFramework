# RLM / Recursive Executor Profile Template

Declarative **provider-neutral recursive-execution** profile. Framework 1.21 requires no specific RLM implementation, model provider, or product; this profile is eligibility and budget metadata, not permission.

```yaml
record_type: RLM_EXECUTION_PROFILE
record_version: "1.0"
profile_ref: "<contract-local reference>"
parent_execution_id: "<parent execution id>"
child_execution_id: "<child execution id>"
recursion_depth: "<current depth>"
max_recursion_depth: "<n>"
hierarchical_budget:
  root_budget_ref: "<root budget identity>"
  parent_consumption: "<observed>"
  child_allocation: "<allocated to this child>"
  invariant: "parent consumption + sum(child allocations) <= root budget"
child_state_binding:
  parent_input_manifest_ref: "<exact parent execution inputs>"
  allowed_scope_ref: "<declared allowed scope>"
result_handoff: "EXPLICIT_AND_AUDITABLE"
gateway_bypass: "PROHIBITED"
parent_cancellation_propagation: "FAIL_CLOSED"
```

Rules:

- `max_recursion_depth` is **normative.** A child at the depth limit cannot spawn further children; violation fails closed with a truthful blocking state.
- Budgets are hierarchical **allocations, not cloned allowances:** `parent consumption + sum(child allocations) <= root budget.` A child execution **cannot mint new authority or budget** by recursion.
- Each child is **state-bound** to the exact parent execution inputs and allowed scope; a child that would exceed the bound scope fails closed.
- Recursive result handoff is **explicit and auditable;** implicit or narrated handoff is not conformance.
- Recursive execution **cannot bypass Effect Gateway requirements** at any depth; mediated Material Effects from a child transit the Gateway with their own permits.
- Parent cancellation/authority revocation **propagates fail-closed:** children stop new governed dispatches, reconcile in-flight effects, and record truthful resulting state.
- Budget exhaustion at any level persists a truthful state (`BUDGET_EXHAUSTED | BLOCKED | WAITING_FOR_REAUTHORIZATION`) and MUST NOT imply Task DONE.
- The optional AI-ControlTower `Prime Agent = Autonomous / Long-Horizon Operator` candidate MAY map to this profile when separately promoted in AI-ControlTower: `Prime Agent role != ProjectFramework dependency`; `Prime Agent role != authority`; `RLM execution != autonomous permission to mutate.` This profile remains valid when Prime Agent is absent or replaced.
- This file is profile metadata. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No RLM runtime, recursive executor service, agent spawner, or provider integration is implied by this record.
