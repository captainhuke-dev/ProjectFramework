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
├── trust.md
├── plan-contract.md        # TASK-057 declarative Plan Contract starter
├── task-contract.md        # TASK-057 declarative Task Contract starter
├── task-record.md          # TASK-057 Task Record starter
├── verification-record.md  # TASK-057 Verification Record starter
├── executor-profile.md     # TASK-057 Executor Profile starter
├── project-adapter.md      # TASK-057 Project Adapter starter
└── integration-reconciliation.md  # TASK-057 Integration Reconciliation starter
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

TASK-057 (Framework `1.19.0`) adds declarative governance-support starters: `plan-contract.md`, `task-contract.md`, `task-record.md`, `verification-record.md`, `executor-profile.md`, `project-adapter.md`, and `integration-reconciliation.md`. They are optional/applicability-driven for AI-ControlTower/Multica consumers. `Contract ≠ Authority`; `Eligibility ≠ Authority`; `Claim ≠ Authority`; `Verification PASS ≠ Task DONE.` `R4_CTX` is execution-time current truth, not a Risk level (Risk remains `R0–R3`). No runtime, scheduler, state engine, router, or automatic executor is introduced.
