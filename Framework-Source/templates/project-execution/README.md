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
├── runtime-contract.md     # TASK-058 runtime-control contract starter
├── execution-attempt.md    # TASK-058 Attempt identity/lifecycle starter
├── execution-checkpoint.md # TASK-058 derived checkpoint starter
├── action-journal.md       # TASK-058 Action/Effect observation starter
└── effect-policy.md        # TASK-058 Effect Gateway/consequence policy starter
```

`fallback-log.md` is applicability-driven append-only operational incident history for actual MCP fallback/recovery events. It is not selection policy, Root Governance, `AUTH-*`, credentials, secret storage, Project Source authority, or a Stable-ID registry. Projects with `fallback_mode: NONE` do not need to materialize it.

When ordered fallback is active, `tools.md` remains policy and `fallback-log.md` remains history. Do not infer fallback order from log recency, connected tools, or prior incidents.

Later Framework contracts may extend this directory with additional single-responsibility policy files. Every file remains subordinate to active `FRAMEWORK-001` and existing authority/risk/disclosure/secret rules.

Read Project authority first:

```text
PROJECT-BOOTSTRAP.md → active FRAMEWORK-001 → 01 → 03 → applicable Project-Execution policy
```

For TASK-057/TASK-058 execution consumers, applicable runtime routing is conceptually:

```text
Task/Plan/Execution Envelope
→ applicable AUTH
→ fresh R4 current truth
→ capability/tool/trust/executor profiles
→ runtime-contract/effect-policy when applicable
→ Task Ready Gate
→ claim/Attempt
→ bounded execution/effect mediation
→ Task Record / VERIFY / source-native reconciliation
```

Core invariants:

```text
Tool selection policy ≠ Tool availability ≠ Location ≠ Authority
Tool/MCP profile ≠ permission to mutate
Contract ≠ Authority
Runtime decision ≠ Authority
Effect Permit ≠ AUTH
Claim ≠ Lease ≠ Fence ≠ Authority
Runtime Event Journal > Checkpoint / Snapshot
```

TASK-034 adds `capabilities.md` for agent/model work eligibility. `Capability ≠ Authority`; capability eligibility never overrides tool, disclosure, Risk, or authority gates.

TASK-037 adds `trust.md` for security/trust crossing constraints. `Trust classification ≠ Authority`; UNKNOWN sensitive crossings fail closed.

TASK-057 (Framework `1.19.0`) adds declarative governance-support starters: `plan-contract.md`, `task-contract.md`, `task-record.md`, `verification-record.md`, `executor-profile.md`, `project-adapter.md`, and `integration-reconciliation.md`. They are optional/applicability-driven for AI-ControlTower/Multica consumers. `Contract ≠ Authority`; `Eligibility ≠ Authority`; `Claim ≠ Authority`; `Verification PASS ≠ Task DONE.` `R4_CTX` is execution-time current truth, not a Risk level (Risk remains `R0–R3`).

TASK-058 (Framework `1.20.0`) adds optional/applicability-driven **deterministic execution-runtime contract starters**: `runtime-contract.md`, `execution-attempt.md`, `execution-checkpoint.md`, `action-journal.md`, and `effect-policy.md`. They define future runtime conformance semantics—durable identities/state, Journal/Checkpoint authority, lease/heartbeat/fence/control generation, typed model proposals, hierarchical budgets, Effect-Surface Closure, JIT single-use Effect Permits, target preconditions, ambiguity/reconciliation, cancellation/compensation, and version-pinned recovery—without implementing a runtime service.

Non-ControlTower Projects remain valid and do not need to materialize runtime-contract artifacts merely because Framework 1.20 exists. Brownfield historical Tasks are not retrofitted by inference. No runtime, scheduler, database, worker daemon, Effect Gateway service, credential broker, model/MCP router, RLM runtime, or automatic Task DONE engine is introduced by these templates.
