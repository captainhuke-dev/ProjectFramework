# MCP Fallback Log

This file is applicability-driven append-only operational incident history. It is not Project Source authority, AUTH, credential storage, or a Stable-ID registry.

## Incident Record

```yaml
incident: "MCP-FB-<YYYYMMDD>-<SEQ>"
timestamp: "<ISO8601_WITH_TIMEZONE>"
event_type: "<FALLBACK_STARTED | FALLBACK_TRANSITION | PRIMARY_RECOVERED | FAILBACK_COMPLETED | INCIDENT_CLOSED | CORRECTION>"
primary_mcp: "<DECLARED_PRIMARY_MCP_ID>"
observed_primary_state: "<ACTIVE | UNAVAILABLE | VERIFICATION_REQUIRED>"
reason: "<CONNECTION_FAILED | AUTH_FAILED | CAPABILITY_UNAVAILABLE | TARGET_MISMATCH | POLICY_DISALLOWED | OTHER_OBSERVED_REASON>"
from_mcp: "<MCP_ID_OR_NONE>"
to_mcp: "<MCP_ID_OR_NONE>"
affected_action: "<BOUNDED_ACTION_DESCRIPTION>"
target_identity_scope: "<VERIFIED_TARGET_OR_SCOPE>"
checkpoint: "<CHECKPOINT_OR_NOT_APPLICABLE>"
result_verification: "<VERIFIED_APPLIED | VERIFIED_NOT_APPLIED | VERIFICATION_REQUIRED | NOT_APPLICABLE>"
recovery_state: "<PRIMARY | FALLBACK_ACTIVE | FAIL_CLOSED>"
failback_policy: "CHECKPOINT_FAILBACK"
failback_at: "<ISO8601_OR_NOT_APPLICABLE>"
incident_state: "<OPEN | CLOSED>"
```

Corrections append a `CORRECTION` event; prior event text is not silently rewritten. Never store passwords, tokens, secret-bearing URLs, or credential material.
