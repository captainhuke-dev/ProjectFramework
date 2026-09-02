# Security & Trust Boundary Profile Template

```yaml
profile_name: "default"
profile_state: "ACTIVE | DISABLED"
surfaces:
  - surface_id: "repository"
    surface_type: "REPOSITORY | WORKSPACE | TOOL_MCP | AGENT_MODEL | EXTERNAL_SERVICE | ARTIFACT | RUNTIME | DEPLOYMENT_TARGET | OTHER"
    trust_class: "TRUSTED | LIMITED_TRUST | UNTRUSTED | PRIVILEGED | EXTERNAL | UNKNOWN"
    source_ref: "<BOUND_PROJECT_OR_SOURCE_NATIVE_POINTER>"
    allowed_crossings: ["DATA_READ", "DATA_WRITE", "CODE_EXECUTION", "ARTIFACT_TRANSFER", "EXTERNAL_DISCLOSURE", "PRIVILEGED_OPERATION"]
    review_trigger: "<EVENT_OR_NOT_APPLICABLE>"
```

Core rules:

```text
Trust classification ≠ Authority
Trusted surface ≠ permission to disclose secrets
Tool eligibility ≠ trust equivalence
Capability ≠ trust ≠ authority
UNKNOWN trust for materially sensitive action → VERIFICATION_REQUIRED / fail closed
```

- `PRIVILEGED` means elevated consequence, not greater authority or general trust.
- `EXTERNAL` means outside Project-local control and still requires purpose-specific disclosure/authority review.
- `surface_id` is profile-local metadata, not a Project Stable ID, credential, hostname authority, MCP workspace identity, or Project Location Binding.
- Material data/code/artifact/execution crossings require applicable provenance, tool eligibility, capability eligibility, TASK-026 disclosure/secret checks, and AUTH/Risk/Decision/shared-state gates.
- Actual secret values MUST NOT be stored here.
- Brownfield adoption never infers trust merely from successful prior use.
