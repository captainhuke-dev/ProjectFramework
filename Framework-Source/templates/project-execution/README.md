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
├── task-contract.md        # TASK-057/058 declarative Task Contract starter (V1 + V2 shape)
├── task-record.md          # TASK-057/058 Task Record starter (V1 + V2 shape)
├── verification-record.md  # TASK-057/058 Verification Record starter (V1 + V2 shape)
├── executor-profile.md     # TASK-057 Executor Profile starter
├── project-adapter.md      # TASK-057/058 Project Adapter starter (Wave A locator mappings)
├── integration-reconciliation.md  # TASK-057/058 Integration Reconciliation starter (V2 Git rule)
├── revision-set.md                 # TASK-058 Revision Set starter
├── execution-input-manifest.md     # TASK-058 Execution Input Manifest starter
├── execution-state-binding.md      # TASK-058 Execution State Binding starter
├── execution-ownership.md          # TASK-058 Execution Ownership Grant/Evidence starter
├── operational-transition-record.md  # TASK-058 Operational Transition Record starter
├── result-acceptance.md              # TASK-058 Result Acceptance starter
├── verification-validity.md          # TASK-058 Verification Validity Evaluation starter
├── runtime-contract.md               # TASK-059 Durable Runtime Control Contract starter
├── runtime-event-journal.md          # TASK-059 Runtime Event Journal starter
├── execution-checkpoint.md           # TASK-059 Execution Checkpoint starter
├── effect-policy.md                  # TASK-059 Effect Policy / Effect Permit starter
└── rlm-executor-profile.md           # TASK-059 RLM / Recursive Executor Profile starter
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

TASK-058 (Framework `1.20.0`) adds the **Compositional State Binding Hub** starters: `revision-set.md`, `execution-input-manifest.md`, `execution-state-binding.md`, `execution-ownership.md`, `operational-transition-record.md`, `result-acceptance.md`, and `verification-validity.md`, plus explicit V2 shapes (`contract_version`/`record_version: "2.0"`) for `task-contract.md`, `task-record.md`, and `verification-record.md` with v1 compatibility preserved. Core invariants: `Resource Identity ≠ Locator ≠ Revision`; `Coordination Claim ≠ Execution Ownership Grant`; `Task Record observation ≠ Result Acceptance`; `Verification PASS ≠ Verification Validity CURRENT`; `COORDINATION_ONLY < ACCEPTANCE_FENCED < SIDE_EFFECT_FENCED.` Binding references are state-bound/reconstructable, historical records are never rewritten, `UNKNOWN` never normalizes to `PASS`, and no executor self-grants ownership or AUTH. No runtime, task database, event store, queue, scheduler, lease/fencing service, CAS store, automatic transition engine, or automatic acceptance/verification engine is introduced.

TASK-059 (Framework `1.21.0`) adds the **Durable Runtime Control Contract** starters: `runtime-contract.md`, `runtime-event-journal.md`, `execution-checkpoint.md`, `effect-policy.md`, and `rlm-executor-profile.md`. They are optional/applicability-driven for execution-runtime consumers (expected: the separately governed AI-ControlTower Python Supervisor reference runtime). Core invariants: `Runtime Event Journal ≠ Checkpoint ≠ Project Source ≠ canonical Task lifecycle truth`; `Supervisor decision ≠ AUTH`; `Supervisor liveness ≠ Execution Ownership Grant`; `Heartbeat ≠ completion evidence`; `Effect Permit ≠ AUTH-*`; `Model proposal ≠ Runtime decision`; `Cancellation ≠ rollback`; `Compensation ≠ history erasure`; `Prime Agent role ≠ ProjectFramework dependency.` The runtime lease/heartbeat/fence is a subordinate liveness/effect-control projection that never creates ownership or AUTH; permits are single-use, bound, and non-transferable; ambiguous effects reconcile at the source-native truth owner with no blind retry; RLM children cannot mint authority or budget and cannot bypass the Effect Gateway. No runtime, supervisor service, queue, database, scheduler, daemon, lease/fencing service, Effect Gateway service, RLM runtime, API server, or automatic continuation engine is introduced.
