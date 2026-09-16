# Executor Profile Template

Declarative **eligibility metadata** for an executor. An Executor Profile states what an executor can support; it is **eligibility metadata, not permission.**

```yaml
profile_name: "<EXECUTOR_ID>"
profile_state: "ACTIVE | DISABLED"
supported_modes:
  - "PLAN | TASK | VERIFY"
work_classes:
  - "<bounded work class this executor supports>"
capability_profile_ref: "./capabilities.md"
tool_profile_ref: "./tools.md"
trust_profile_ref: "./trust.md"
runtime_support:
  typed_proposal_protocol: "SUPPORTED | UNSUPPORTED"
  durable_attempt_resume: "SUPPORTED | UNSUPPORTED"
  heartbeat_reporting: "SUPPORTED | UNSUPPORTED"
  checkpoint_resume: "SUPPORTED | UNSUPPORTED"
  mediated_effect_classes:
    - "<effect class or NONE>"
  effect_surface_closure:
    state: "PROVEN | NOT_PROVEN | NOT_APPLICABLE"
    policy_ref: "./effect-policy.md"
    inventory_state: "COMPLETE | INCOMPLETE | UNKNOWN | NOT_APPLICABLE"
    all_governed_routes_accounted_for: "<true | false | NOT_APPLICABLE>"
    evidence_refs:
      - "<independently reviewable closure evidence ref, or NOT_APPLICABLE: <reason>>"
  recursive_execution: "SUPPORTED | UNSUPPORTED"
  max_child_executions: "<n or NOT_APPLICABLE>"
  max_recursion_depth: "<n or NOT_APPLICABLE>"
execution_limits:
  - "<bounded execution limit, e.g. max scope, mutation class ceiling>"
workspace_roles:
  - "<Develop Workspace role, e.g. EDIT / BUILD / TEST>"
coordination_support:
  claim_scope: "<bounded claim scope this executor can hold>"
  parallelism: "<declared parallelism support, or NONE>"
independent_verifier:
  qualified: "<true | false>"
  basis: "<declared basis for independent-review qualification, or NOT_APPLICABLE: <reason>>"
```

Rules:

- `Eligibility ≠ Authority.` This profile never grants AUTH, mutation, approval, deployment, disclosure, or binding authority.
- **Supporting VERIFY is not the same as qualifying as an independent verifier.** `independent_verifier.qualified` is declared separately; generic VERIFY support does not satisfy an independent-review requirement.
- For an autonomous mediated Material Effect class, `effect_surface_closure.state: PROVEN` is valid only when the referenced Effect Policy has `inventory_state: COMPLETE`, `all_governed_routes_accounted_for: true`, every governed route is mediated/prohibited/confined, and `evidence_refs` resolve to independently reviewable enforcement evidence. Any incomplete/unknown inventory, missing route, missing evidence, or policy-only self-attestation forces `NOT_PROVEN` and makes the executor ineligible for that autonomous effect class.
- `effect_surface_closure.state: NOT_APPLICABLE` requires an explicit reason/basis in the referenced policy and cannot be used to bypass a Material Effect that actually has an executable route.
- `typed_proposal_protocol: SUPPORTED` means the executor can emit allowed proposal/report messages; it does not let the executor emit runtime-owned `AUTH_GRANTED`, `LEASE_ACQUIRED`, `FENCE_ADVANCED`, `PERMIT_ISSUED`, `VERIFIED`, `INTEGRATED`, or `TASK_DONE` events.
- Recursive-execution limits are capability/eligibility ceilings. Child execution cannot create authority or budget.
- Selection is deterministic **filter-before-rank**: Ready Gate PASS → mode → work class → mandatory capabilities → provider scope → tool policy → trust policy → Execution Envelope → runtime/effect requirements → risk/side-effect → workspace → independent-review constraints → eligible set → preference ranking → selection → volatile recheck → claim.
- An ineligible executor cannot become eligible because it is preferred, cheaper, stronger, recent, or available. No eligible candidate produces `NO_ELIGIBLE_EXECUTOR`; no undeclared fallback is invented.
- TASK and VERIFY selection are separate evaluations.
- This file is eligibility metadata. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, runtime state, or a Stable-ID family.
- No runtime, model/executor router, or automatic selector is implied by this profile.
