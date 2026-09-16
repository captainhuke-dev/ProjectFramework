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
execution_limits:
  - "<bounded execution limit, e.g. max scope, mutation class ceiling>"
workspace_roles:
  - "<Develop Workspace role, e.g. EDIT / BUILD / TEST>"
coordination_support:
  claim_scope: "<bounded claim scope this executor can hold>"
  parallelism: "<declared parallelism support, or NONE>"
runtime_support:
  typed_proposal_protocol: "<SUPPORTED | UNSUPPORTED>"
  attempt_lease_heartbeat: "<SUPPORTED | UNSUPPORTED>"
  checkpoint_resume: "<SUPPORTED | UNSUPPORTED>"
  mediated_effect_classes:
    - "<effect class or NONE>"
  effect_surface_closure: "<SUPPORTED_WITH_EVIDENCE | NOT_SUPPORTED | NOT_APPLICABLE>"
  recursive_execution:
    support: "<SUPPORTED | UNSUPPORTED>"
    max_child_executions: "<n or NOT_APPLICABLE>"
    max_recursion_depth: "<n or NOT_APPLICABLE>"
independent_verifier:
  qualified: "<true | false>"
  basis: "<declared basis for independent-review qualification, or NOT_APPLICABLE: <reason>>"
```

Rules:

- `Eligibility ≠ Authority.` This profile never grants AUTH, mutation, approval, deployment, disclosure, or binding authority.
- Runtime support metadata cannot self-create a lease, fence, Effect Permit, runtime event, or Effect-Gateway eligibility.
- `effect_surface_closure: SUPPORTED_WITH_EVIDENCE` requires demonstrable confinement/mediation for applicable equivalent mutation surfaces; prompt-policy intent alone is insufficient.
- Recursive execution support remains subject to durable hierarchical budget and cannot manufacture authority/budget.
- **Supporting VERIFY is not the same as qualifying as an independent verifier.** Qualification is evaluated separately.
- Selection remains deterministic **filter-before-rank**: Ready Gate PASS → mode → work class → mandatory capabilities → provider scope → tool policy → trust policy → Execution Envelope → risk/side-effect → workspace → independent-review/runtime constraints → eligible set → preference ranking → selection → volatile recheck → claim.
- An ineligible executor cannot become eligible because it is preferred, cheaper, stronger, recent, or available. No eligible candidate produces `NO_ELIGIBLE_EXECUTOR`; no undeclared fallback is invented.
- TASK and VERIFY selection are separate evaluations.
- This file is eligibility metadata, not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, runtime state, or a Stable-ID family.
- No runtime, router, scheduler, or automatic selector is implied.