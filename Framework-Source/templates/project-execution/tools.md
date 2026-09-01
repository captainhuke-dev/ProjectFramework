# Tool / MCP Execution Profile Template

```yaml
profile_name: "default"
profile_state: "ACTIVE | DISABLED"
primary_tool: "<TOOL_OR_MCP_ID>"
allowed_tools:
  - "<TOOL_OR_MCP_ID>"
disallowed_tools:
  - "<TOOL_OR_MCP_ID>"
fallback_mode: "NONE | ORDERED_ALLOW_LIST"
fallback_order:
  - "<TOOL_OR_MCP_ID>"
failure_policy: "FAIL_CLOSED | READ_ONLY_DIAGNOSTIC_ONLY"
review_trigger: "<EVENT_OR_NOT_APPLICABLE>"
```

Rules:

- `PRIMARY` means the declared `primary_tool` when ACTIVE and eligible.
- `primary_tool` SHOULD be present in `allowed_tools` when ACTIVE.
- `disallowed_tools` wins over allowed/fallback declarations.
- `fallback_mode: NONE` means no automatic substitute.
- `ORDERED_ALLOW_LIST` means only `fallback_order` entries are eligible, in declared order.
- `FAIL_CLOSED` blocks the affected execution when no eligible tool exists.
- `READ_ONLY_DIAGNOSTIC_ONLY` allows only bounded read-only diagnosis; it never authorizes mutation through an undeclared tool.
- Tool IDs are policy labels, not credentials, MCP workspace IDs, repository identity, Project Stable IDs, or authority.
- Actual secret values MUST NOT be stored here.
