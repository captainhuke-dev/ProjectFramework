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
├── integration-reconciliation.md  # TASK-057 Integration Reconciliation starter
├── runtime-contract.md     # TASK-058 deterministic runtime protocol starter
├── execution-attempt.md    # TASK-058 bounded worker-attempt starter
├── execution-checkpoint.md # TASK-058 derived recovery checkpoint starter
├── action-journal.md       # TASK-058 Action/Effect conceptual starter
└── effect-policy.md        # TASK-058 consequence-boundary policy starter
```

`fallback-log.md` is applicability-driven append-only operational incident history for actual MCP fallback/recovery events. It is not selection policy, Root Governance, `AUTH-*`, credentials, secret storage, Project Source authority, or a Stable-ID registry. Projects with `fallback_mode: NONE` do not need to materialize it.

When ordered fallback is active, `tools.md` remains policy and `fallback-log.md` remains history. Do not infer fallback order from log recency, connected tools, or prior incidents.

Every file remains subordinate to active `FRAMEWORK-001` and existing authority/risk/disclosure/secret rules.

Read Project authority first:

```text
PROJECT-BOOTSTRAP.md → active FRAMEWORK-001 → 01 → 03 → applicable Project-Execution policy
```

Core invariants:

```text
Tool selection policy ≠ Tool availability ≠ Location ≠ Authority
Tool/MCP profile ≠ permission to mutate
Project-Execution ≠ Project Source ≠ AUTH ≠ runtime authority
```

TASK-034 adds `capabilities.md` for agent/model work eligibility. `Capability ≠ Authority`; capability eligibility never overrides tool, disclosure, Risk, or authority gates.

TASK-037 adds `trust.md` for security/trust crossing constraints. `Trust classification ≠ Authority`; UNKNOWN sensitive crossings fail closed.

TASK-057 (Framework `1.19.0`) adds declarative PLAN/TASK/VERIFY governance-support starters. `Contract ≠ Authority`; `Eligibility ≠ Authority`; `Claim ≠ Authority`; `Verification PASS ≠ Task DONE`; `R4_CTX` is execution-time current truth, not Risk R4.

TASK-058 (Framework `1.20.0`) adds optional/applicability-driven **deterministic execution-runtime protocol starters** for runtimes that need durable long-running execution. They keep Task/Execution/Attempt/Action truth separate; require `Runtime Event Journal > Checkpoint / Snapshot`; distinguish `Multica claim != runtime lease != runtime fence != Effect Permit != AUTH`; and define Effect-Gateway mediation, JIT single-use permits, target preconditions, deterministic ambiguous-result handling, durable budgets, wait/wakeup, and recovery/version pinning.

These files do **not** bundle an AI-ControlTower runtime. Projects not using AI-ControlTower or deterministic long-running runtime control remain valid and need not materialize TASK-058 starters when not applicable.