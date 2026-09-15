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
independent_verifier:
  qualified: "<true | false>"
  basis: "<declared basis for independent-review qualification, or NOT_APPLICABLE: <reason>>"
```

Rules:

- `Eligibility ≠ Authority.` This profile never grants AUTH, mutation, approval, deployment, disclosure, or binding authority.
- **Supporting VERIFY is not the same as qualifying as an independent verifier.** `independent_verifier.qualified` is declared separately; generic VERIFY support does not satisfy an independent-review requirement.
- Selection is deterministic **filter-before-rank**: Ready Gate PASS → mode → work class → mandatory capabilities → provider scope → tool policy → trust policy → Execution Envelope → risk/side-effect → workspace → independent-review constraints → eligible set → preference ranking → selection → volatile recheck → claim.
- An ineligible executor cannot become eligible because it is preferred, cheaper, stronger, recent, or available. No eligible candidate produces `NO_ELIGIBLE_EXECUTOR`; no undeclared fallback is invented.
- TASK and VERIFY selection are separate evaluations.
- This file is eligibility metadata. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No runtime, model/executor router, or automatic selector is implied by this profile.
