# Plan Contract Template

Declarative execution-strategy contract for one bounded Task. Plan Contract owns **execution strategy**, not Task success semantics. A bounded/LOW Task MAY embed this in its durable Task artifact; a standalone Plan file is not universally required.

`PLAN complete ≠ Task Ready ≠ execution authority.`

```yaml
contract_type: PLAN
contract_version: "1.0"
task_ref: "TASK-xxx"
intent: "<one-line bounded execution intent>"
scope:
  included:
    - "<bounded in-scope surface>"
  excluded:
    - "<explicitly out of scope>"
required_current_truth:
  sources:
    - "<canonical/source-native owner of a mutable fact>"
  freshness_requirements: "<freshness expectation, e.g. fresh read before mutation>"
execution_sequence: "<ordered or dependency-structured execution steps>"
dependency_strategy: "<how declared dependencies are resolved and checked>"
verification_strategy: "<which verification inputs and proof domain apply>"
rollback_or_recovery: "<recovery path when a step fails or a result is unknown>"
prohibited_operations:
  - "<operation this plan must not perform>"
invalidation_conditions:
  - "<condition that invalidates this plan and requires re-PLAN>"
```

Rules:

- Plan Contract may **reference** Task Contract intent/acceptance/IPOCV but MUST NOT create a competing authoritative copy of them.
- `required_current_truth` declares **which** current truth is required; it does not resolve it. R4 resolves declared truth from its owner at the execution boundary.
- `prohibited_operations` and `invalidation_conditions` are constraints, not grants. They never expand AUTH.
- This file is eligibility/strategy metadata. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No runtime, scheduler, state engine, or automatic executor is implied by this contract.
