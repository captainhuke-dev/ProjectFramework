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
failback_policy: "CHECKPOINT_FAILBACK"
review_trigger: "<EVENT_OR_NOT_APPLICABLE>"
```

Rules:

- `PRIMARY` means the declared `primary_tool` when ACTIVE and eligible.
- `primary_tool` SHOULD be present in `allowed_tools` when ACTIVE.
- `disallowed_tools` wins over allowed/fallback declarations.
- `fallback_mode: NONE` means no automatic substitute.
- `ORDERED_ALLOW_LIST` means only `fallback_order` entries are eligible, in declared order.
- An undeclared tool is never eligible merely because it is available, connected, recent, similar, or highly ranked.
- Execution eligibility requires applicable tool/capability availability, active policy eligibility, and verified bound Project/workspace/repository target identity.
- `FAIL_CLOSED` blocks the affected execution when no eligible tool exists.
- `READ_ONLY_DIAGNOSTIC_ONLY` allows only bounded read-only diagnosis; it never authorizes mutation through an undeclared tool.
- `CHECKPOINT_FAILBACK` never switches MCPs in the middle of the current bounded action/checkpoint. Finish/persist/verify that checkpoint, reverify Primary, append recovery/failback history, then use Primary for the next action.
- Unknown potentially-applied side effects enter `RESULT_VERIFICATION_REQUIRED`; verify resulting state before retrying or transitioning to another declared fallback.
- Material fallback mutation requires the applicable append-only `fallback-log.md` incident event to be persisted first; inability to persist it is `FAIL_CLOSED`.
- Tool IDs are policy labels, not credentials, MCP workspace IDs, repository identity, Project Stable IDs, or authority.
- TASK-057: tool policy is one filter in deterministic filter-before-rank executor selection; an undeclared tool is never eligible, and `NO_ELIGIBLE_EXECUTOR` fails closed without invented fallback.
- Actual secret values MUST NOT be stored here.
