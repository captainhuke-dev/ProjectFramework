# TASK-037 Security & Trust Boundary Contract — Design

**Task:** TASK-037 — Security & Trust Boundary Contract
**Design state:** USER_APPROVED_SET1_DIRECTION / WRITTEN_SPEC_APPROVED_BY_GOAL
**Set 1 position:** 5 of 5
**Depends on:** TASK-035; consumes TASK-027 and TASK-034
**Target Framework:** 1.12.0
**Project Source Schema:** 1.0.0
**Release format:** 3

## 1. Purpose

TASK-026 governs outbound AI context disclosure, but Project security also spans repositories, workspaces, MCP/tools, agents/models, external services, artifacts, code execution, releases, deployment targets, and privileged runtimes.

TASK-037 extends the shared optional profile directory:

```text
<Project-Root>/Project-Execution/
├── README.md
├── tools.md
├── capabilities.md
└── trust.md
```

Core invariants:

```text
Trust classification ≠ Authority
Trusted surface ≠ permission to disclose secrets
Tool eligibility ≠ trust equivalence
Capability ≠ trust ≠ authority
Unknown trust for materially sensitive action → fail closed
```

## 2. Trust vocabulary

The canonical surface trust classes are:

```text
TRUSTED
LIMITED_TRUST
UNTRUSTED
PRIVILEGED
EXTERNAL
UNKNOWN
```

`PRIVILEGED` is not “more trusted” than `TRUSTED`; it means compromise/misuse has elevated impact and therefore requires stronger handling. `EXTERNAL` means outside the Project-local control boundary and still requires purpose-specific disclosure/authority review. `UNKNOWN` is explicit unresolved classification.

## 3. `trust.md` contract

A maintained profile may declare boundaries such as:

```yaml
profile_name: "default"
profile_state: "ACTIVE | DISABLED"
surfaces:
  - surface_id: "repository"
    surface_type: "REPOSITORY | WORKSPACE | TOOL_MCP | AGENT_MODEL | EXTERNAL_SERVICE | ARTIFACT | RUNTIME | DEPLOYMENT_TARGET | OTHER"
    trust_class: "TRUSTED | LIMITED_TRUST | UNTRUSTED | PRIVILEGED | EXTERNAL | UNKNOWN"
    source_ref: "<BOUND_PROJECT_OR_SOURCE_NATIVE_POINTER>"
    allowed_crossings: ["DATA_READ", "DATA_WRITE", "CODE_EXECUTION", "ARTIFACT_TRANSFER"]
    review_trigger: "<EVENT_OR_NOT_APPLICABLE>"
```

`surface_id` is a profile-local label, not a Project Stable-ID family, credential, hostname authority, MCP workspace ID, or replacement for Project Location Binding.

## 4. Crossing model

Material crossings are evaluated as:

```text
source surface + trust class
→ destination surface + trust class
→ crossing type (data/code/artifact/execution)
→ provenance/classification requirements
→ applicable Tool/MCP profile
→ applicable Agent/Model capability profile
→ TASK-026 disclosure/secret rules when external context is involved
→ AUTH/Risk/Decision/shared-state gates
→ execute only when all applicable boundaries permit
```

Crossing types include `DATA_READ`, `DATA_WRITE`, `CODE_EXECUTION`, `ARTIFACT_TRANSFER`, `EXTERNAL_DISCLOSURE`, and `PRIVILEGED_OPERATION` when applicable.

## 5. Data and secret handling

Trust classification never permits storing/revealing actual secret values merely because a surface is trusted. Existing `17 Secret Reference Registry` remains reference-only. External disclosure continues through TASK-026 classes/provider eligibility/minimization/redaction and bounded authority.

Material data crossing from a higher-control/trusted source into `EXTERNAL`, `LIMITED_TRUST`, `UNTRUSTED`, or `UNKNOWN` destinations requires the applicable review/classification/authorization. Unknown sensitive-data classification fails closed.

## 6. Code execution and supply-chain inputs

Code, scripts, dependencies, generated artifacts, and external packages from `UNTRUSTED`, `LIMITED_TRUST`, `EXTERNAL`, or `UNKNOWN` sources do not become trusted because they exist in the workspace. Material execution/release use requires provenance and review proportional to impact.

TASK-037 defines governance only. It does not add malware scanning, sandbox enforcement, dependency scanners, package attestation services, policy engines, or supply-chain automation.

## 7. Tool/MCP integration

TASK-027 decides whether a tool is eligible for execution. TASK-037 separately evaluates trust of the tool/service and the target crossing. An allowed tool may still be inappropriate for privileged/untrusted-boundary work; a trusted tool cannot bypass `AUTH-*`, binding, or disclosure gates.

If an MCP/tool cannot prove it is acting on the bound Project or its trust classification is `UNKNOWN` for a materially sensitive action, fail closed for that action while permitting bounded read-only diagnostics where safe.

## 8. Agent/Model integration

TASK-034 capability eligibility is necessary but not sufficient. External agents/models are also `EXTERNAL` surfaces for Project-context processing and must satisfy TASK-026 disclosure rules. A local capable model may still be ineligible for privileged operations if the required tool/runtime/trust conditions are not met.

## 9. Repository, artifact, release, and deployment integration

TASK-035 publication dimensions remain factual lifecycle state. Trust review considers the concrete repository/artifact/registry/deployment/runtime surfaces involved in crossings, but does not change publication truth automatically.

Examples:

- a `PUSHED` repository state does not prove the remote is trusted for secrets;
- a `PUBLISHED` artifact does not prove provenance/review sufficiency;
- a `DEPLOYED` workload does not grant Runtime mutation authority;
- a signed tag may increase assurance but does not replace trust/authority evaluation.

## 10. Privileged surfaces

`PRIVILEGED` surfaces include environments/actions where misuse has elevated consequence: production control planes, high-impact credentials, protected deployment targets, administrative shells, or equivalent Project-defined contexts.

Material privileged operations require explicit authority plus the Project's applicable risk/review/evidence. A privileged classification never broadens access by itself.

## 11. Unknown and contradiction behavior

For materially sensitive actions:

- `UNKNOWN` trust → `VERIFICATION_REQUIRED` / fail closed;
- materially contradictory trust sources → surface conflict using existing `DRIFT-*` / `CONFLICT-*` when governance-relevant;
- recency/ranking/similarity never resolves trust;
- one-off user instructions may authorize a bounded action but do not silently rewrite persistent trust classification.

## 12. Bootstrap and canonical homes

`PROJECT-BOOTSTRAP.md` resolves authority first. `Project-Execution/trust.md` is read only after active Project Source is resolved and when the task needs trust-boundary policy. `00 / FRAMEWORK-001` remains binding/location authority; `AUTH-*` remains execution permission; `RISK-*` remains risk; `SECRET-*` remains secret metadata; `Project-Execution/` defines policy constraints without replacing those homes.

## 13. GREENFIELD/Brownfield

The trust profile is optional/applicability-driven. GREENFIELD does not invent trusted/untrusted/privileged surfaces without evidence. Brownfield adoption preserves existing controls/history and does not retroactively classify prior services/tools/providers trusted merely because they were used successfully.

## 14. Affected surfaces and verification

Implementation adds maintained `Framework-Source/templates/project-execution/trust.md` and updates current release/amendment/Core/SKILL/README/migration/templates/task/tests. It creates no scanner, sandbox, policy engine, runtime isolation, supply-chain automation, external security service, or secret store.

Pressure/AFFECTED verification must prove trust/authority/capability/tool separation; UNKNOWN fail-closed behavior; privileged semantics; TASK-026 secret/disclosure preservation; repository/workspace/MCP/model/artifact/runtime/deployment crossings; publication-dimension integration; Brownfield no invented trust; no runtime enforcement.
