# Framework Governance Amendment — TASK-037 Security & Trust Boundary Contract

**Framework:** 1.12.0
**Schema:** 1.0.0
**Release format:** 3
**Status:** CURRENT / APPROVED_SET1_FINAL
**Task:** TASK-037 — Security & Trust Boundary Contract

## 1. Purpose

Framework 1.12.0 defines a Project-level trust-boundary policy spanning repositories, workspaces, tools/MCPs, agents/models, external services, artifacts, code execution, releases, deployment targets, and privileged runtimes while preserving existing authority, secret, disclosure, and location homes.

```text
Trust classification ≠ Authority
Trusted surface ≠ permission to disclose secrets
Tool eligibility ≠ trust equivalence
Capability ≠ trust ≠ authority
Unknown trust for materially sensitive action → fail closed
```

## 2. Maintained representation and vocabulary

TASK-037 completes the optional shared profile:

```text
<Project-Root>/Project-Execution/
├── README.md
├── tools.md
├── capabilities.md
└── trust.md
```

Canonical trust classes:

```text
TRUSTED | LIMITED_TRUST | UNTRUSTED | PRIVILEGED | EXTERNAL | UNKNOWN
```

`PRIVILEGED` means elevated consequence/impact, not “more trusted”. `EXTERNAL` means outside Project-local control. `UNKNOWN` is explicit unresolved classification.

## 3. Crossing model

Material crossing evaluation composes:

```text
source surface + trust class
→ destination surface + trust class
→ crossing type
→ provenance/classification requirements
→ Tool/MCP Execution Profile
→ Agent/Model Capability Profile
→ TASK-026 disclosure/secret rules when applicable
→ AUTH/Risk/Decision/shared-state gates
→ execute only when all applicable boundaries permit
```

Crossing types include `DATA_READ`, `DATA_WRITE`, `CODE_EXECUTION`, `ARTIFACT_TRANSFER`, `EXTERNAL_DISCLOSURE`, and `PRIVILEGED_OPERATION`.

## 4. Data, secret, and disclosure boundary

Trust classification never grants secret access or external disclosure. `17 Secret Reference Registry` remains reference-only. External context continues through TASK-026 disclosure classes/provider eligibility/minimization/redaction/bounded authority. Material sensitive data crossing into `EXTERNAL`, `LIMITED_TRUST`, `UNTRUSTED`, or `UNKNOWN` requires applicable review/classification/authorization; unresolved sensitive classification fails closed.

## 5. Code, artifact, and supply-chain inputs

Code/scripts/dependencies/generated artifacts from `UNTRUSTED`, `LIMITED_TRUST`, `EXTERNAL`, or `UNKNOWN` do not become trusted merely because they are present in a workspace. Material execution/release use requires provenance/review proportional to impact. TASK-037 adds no scanner, sandbox enforcement, dependency service, attestation runtime, or supply-chain automation.

## 6. Tool/MCP and Agent/Model composition

TASK-027 determines tool eligibility; TASK-037 separately constrains trust of the tool/service and crossing. Allowed tools cannot bypass Project binding, `AUTH-*`, Risk, or disclosure. Unverified bound Project identity or `UNKNOWN` trust for materially sensitive execution fails closed while bounded read-only diagnosis may continue when safe.

TASK-034 capability eligibility is necessary but insufficient. External agents/models are `EXTERNAL` surfaces for Project-context processing and remain subject to TASK-026. A capable model does not gain privilege or authority from capability status.

## 7. Repository, release, artifact, and deployment composition

TASK-035 publication dimensions remain factual lifecycle truth. Trust review considers the concrete repository/registry/artifact/deployment/runtime surfaces without rewriting publication state.

- `PUSHED` does not prove remote trust for secrets;
- `PUBLISHED` does not prove artifact provenance sufficiency;
- `DEPLOYED` does not grant Runtime mutation authority;
- signatures/tags may increase assurance but do not replace trust/authority evaluation.

## 8. Privileged surfaces

`PRIVILEGED` covers high-impact contexts such as production control planes, administrative shells, protected deployment targets, high-impact credentials, or Project-defined equivalents. Material `PRIVILEGED_OPERATION` requires explicit authority plus applicable risk/review/evidence. Privileged classification never broadens access by itself.

## 9. Unknown/contradiction behavior

For materially sensitive actions, `UNKNOWN` trust means `VERIFICATION_REQUIRED` / fail closed. Materially contradictory trust sources surface through existing `DRIFT-*` / `CONFLICT-*` when governance-relevant. Recency/ranking/similarity never resolves trust. One-off user instructions do not silently rewrite standing trust classification.

## 10. Bootstrap and canonical homes

`PROJECT-BOOTSTRAP.md` resolves authority first. `Project-Execution/trust.md` is read only after active Project Source resolves and only when applicable. `FRAMEWORK-001` remains location/binding authority; `AUTH-*` remains execution permission; `RISK-*` remains risk; `SECRET-*` remains secret metadata; Project-Execution remains policy constraints only.

## 11. GREENFIELD/Brownfield

Trust policy is optional/applicability-driven. GREENFIELD invents no trusted/untrusted/privileged surfaces without evidence. Brownfield upgrades do not retroactively classify prior services/tools/providers trusted merely because they were used successfully.

## 12. Runtime boundary

TASK-037 adds no scanner, sandbox enforcement, policy engine, runtime isolation, supply-chain automation, external security service, secret store, or automatic privileged-operation executor.
