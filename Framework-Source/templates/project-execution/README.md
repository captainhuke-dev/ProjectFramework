# Project Execution Profile

`Project-Execution/` is an optional/applicability-driven governed Project policy surface outside `Project-Source/00–99`.

It is not Root Governance, Project Location Binding, `AUTH-*`, current branch/worktree, Canonical Integration Target, Canonical Implementation Source, Runtime authority, credentials, or secret storage.

Current maintained files:

```text
Project-Execution/
├── README.md
├── tools.md
├── fallback-log.md   # only when ordered fallback is applicable
├── capabilities.md
└── trust.md
```

`fallback-log.md` is applicability-driven append-only operational incident history for actual MCP fallback/recovery events. It is not selection policy, Root Governance, `AUTH-*`, credentials, secret storage, Project Source authority, or a Stable-ID registry. Projects with `fallback_mode: NONE` do not need to materialize it.

When ordered fallback is active, `tools.md` remains policy and `fallback-log.md` remains history. Do not infer fallback order from log recency, connected tools, or prior incidents.

Later Framework contracts may extend this directory with additional single-responsibility policy files. Every file remains subordinate to active `FRAMEWORK-001` and existing authority/risk/disclosure/secret rules.

Read Project authority first:

```text
PROJECT-BOOTSTRAP.md → active FRAMEWORK-001 → 01 → 03 → applicable Project-Execution policy
```

Core invariants:

```text
Tool selection policy ≠ Tool availability ≠ Location ≠ Authority
Tool/MCP profile ≠ permission to mutate
```

TASK-034 adds `capabilities.md` for agent/model work eligibility. `Capability ≠ Authority`; capability eligibility never overrides tool, disclosure, Risk, or authority gates.

TASK-037 adds `trust.md` for security/trust crossing constraints. `Trust classification ≠ Authority`; UNKNOWN sensitive crossings fail closed.
