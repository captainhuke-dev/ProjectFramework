# Task Contract Template

Declarative contract for what one bounded Task must achieve. Task Contract owns **intent, acceptance criteria, declared dependencies, completion requirements, Expected IPOCV, and integration applicability.**

Every dimension of Expected IPOCV is mandatory. A genuinely inapplicable dimension is explicit `NOT_APPLICABLE` **with a reason**; omission is not equivalent to not-applicable, and bare `NOT_APPLICABLE` without a reason keeps `EXPECTED_IPOCV_COMPLETE` false.

```yaml
contract_type: TASK
contract_version: "1.0"
task_id: "TASK-xxx"
plan_ref: "<path or embedded reference to the Plan Contract, if separate>"
intent: "<one-line bounded outcome>"
task_type: "<bounded work type>"
acceptance_criteria:
  - "<observable, checkable criterion>"
dependencies:
  depends_on:
    - "TASK-yyy"
  blocks:
    - "TASK-zzz"
  parallelizable_with:
    - "TASK-www"
execution_envelope:
  allowed_scope:
    - "<bounded in-scope surface>"
  allowed_workspaces:
    - "<Develop Workspace ref>"
  allowed_mutation_classes:
    - "<mutation class, e.g. LOCAL_FILE_EDIT>"
  prohibited_effects:
    - "<effect this Task must not cause>"
  required_authority_refs:
    - "<AUTH-* or explicit user authority reference>"
  current_truth_context: R4_REQUIRED
  runtime_contract_ref: "<./runtime-contract.md or NOT_APPLICABLE: <reason>>"
  effect_policy_ref: "<./effect-policy.md or NOT_APPLICABLE: <reason>>"
  runtime_controls:
    durable_resume_required: "<true | false>"
    mediated_material_effects: "<true | false>"
  concurrency:
    claim_scope: "<bounded claim scope>"
    parallelism_constraints: "<declared parallelism, or NONE>"
  recovery:
    unknown_result: VERIFY_BEFORE_RETRY
expected_ipocv:
  input: "<declared inputs, or NOT_APPLICABLE: <reason>>"
  process: "<declared process, or NOT_APPLICABLE: <reason>>"
  output: "<declared outputs, or NOT_APPLICABLE: <reason>>"
  control: "<declared controls, or NOT_APPLICABLE: <reason>>"
  verification: "<declared verification, or NOT_APPLICABLE: <reason>>"
verification_requirements:
  - "<required verification input or proof domain>"
completion_requirements:
  - "<what must be true for this Task to be DONE>"
integration:
  applicable: "<true | false>"
  strategy: "<FAST_FORWARD_EXACT | MERGE_COMMIT_PRESERVING_CANDIDATE | TRANSFORMING_INTEGRATION | NOT_APPLICABLE>"
  target: "<canonical integration target, if applicable>"
```

Rules:

- **Mandatory no-inference rules:** `missing field ≠ permission to infer`; `unknown authority ≠ authorized`; `unknown dependency ≠ satisfied`; `available tool ≠ eligible executor.`
- The Execution Envelope **may narrow** existing authority but can **never broaden** it. An entry naming a target, workspace, operation, runtime contract, or effect policy does not create authority for it.
- `current_truth_context: R4_REQUIRED` declares that execution-time current truth must be resolved from its owner; it is not a Risk level (`R4_CTX ≠ Risk R4`; Risk remains `R0–R3`).
- `runtime_contract_ref` / `effect_policy_ref` declare applicable execution-control requirements only. Runtime Event Journal, Attempt state, Action state, lease/fence, and Checkpoint truth remain runtime-domain data and MUST NOT be copied into this Task Contract as competing lifecycle truth.
- `durable_resume_required` and `mediated_material_effects` describe Task control requirements; they do not instantiate a runtime or grant Effect Permit/AUTH.
- `integration.applicable: false` means the Task may be DONE locally without integration; `true` means it cannot be DONE until required integration/resulting-state criteria are satisfied.
- This file is a work contract. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No runtime, scheduler, state engine, or automatic executor is implied by this contract.
