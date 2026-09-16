# Effect Policy Template

Declarative policy for one governed Material Effect class. Effect Policy narrows/defines runtime mediation requirements; it is **not AUTH** and Tool availability does not make an effect eligible.

```yaml
policy_type: EFFECT_POLICY
policy_version: "1.0"
effect_class: "<governed Material Effect class>"

surface_inventory:
  - surface: "<MCP/tool | shell/process | network | Git/SSH | cloud credential | filesystem | container socket | database | SDK | child process>"
    disposition: "<MEDIATED_BY_EFFECT_GATEWAY | EXPLICITLY_PROHIBITED | CONFINED | NOT_APPLICABLE>"

credential_boundary:
  raw_mutation_credentials_in_executor_workspace: false
  trusted_holder: "<Gateway/broker/source-native boundary>"

permit:
  required: true
  max_uses: 1
  binding:
    - execution_id
    - attempt_id
    - action_id
    - action_hash
    - target_ref
    - tool_ref
    - runtime_generation
    - fence_epoch
    - task_contract_fingerprint
    - execution_envelope_fingerprint

precondition:
  support: "<SUPPORTED | EXPLICITLY_UNSUPPORTED>"
  source_native_type: "<exact SHA | ETag/If-Match | resource version | row version | object hash | CAS token | immutable candidate | NOT_APPLICABLE>"
  stale_result: PRECONDITION_CONFLICT

semantics:
  idempotency: "<IDEMPOTENT | CONDITIONALLY_IDEMPOTENT | NON_IDEMPOTENT | UNKNOWN>"
  reconciliation: "<NATIVE_IDEMPOTENCY_KEY | COMPARE_AND_SET | SOURCE_READBACK | EXTERNAL_CONFIRMATION | MANUAL_VERIFICATION | NONE>"
  reversibility: "<REVERSIBLE_ATOMIC | COMPENSATABLE | IRREVERSIBLE | UNKNOWN>"

cancellation:
  block_new_dispatch: true
  reconcile_in_flight: true

compensation:
  separately_governed_effect: true

manual_resolution_when:
  - "NON_IDEMPOTENT or UNKNOWN + reconciliation NONE + ambiguous result"

conformance_evidence:
  effect_surface_closure: "<evidence ref>"
  credential_scope: "<evidence ref>"
  permit_atomicity: "<evidence ref>"
  stale_fence_rejection: "<evidence ref>"
  target_precondition: "<evidence ref>"
  result_reconciliation: "<evidence ref>"
```

Required invariants:

```text
Gateway eligibility ≠ AUTH
Effect Permit ≠ AUTH
Tool availability ≠ Gateway eligibility
Effect-surface policy without confinement ≠ enforcement
Exactly-once external execution is not assumed
Cancellation ≠ rollback
Compensation ≠ rollback
```

A mediated class is not autonomously conformant while an executor retains an uncontrolled equivalent mutation route.