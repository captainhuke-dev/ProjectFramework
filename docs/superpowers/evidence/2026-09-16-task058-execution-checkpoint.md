# TASK-058 Execution Checkpoint — Deterministic Runtime Contract

Date: `2026-09-16` (Asia/Bangkok)
Task: `TASK-058`
Execution state: `IN_PROGRESS / TOOLING_BLOCKED_BEFORE_CANDIDATE_FREEZE`
Canonical Task lifecycle mutation: `NOT_PERFORMED_ON_MAIN`
Implementation branch: `task058-framework120`
Checkpoint branch head before this evidence commit: `259e5c8c326c52ace5b912804b417bddd08d3c56`
Checkpoint tree before this evidence commit: `c3120c5f6c52180c1f506d9ea0880082c02a9f35`

## 1. Execution authorization and boundary

ACTOR-001 explicitly approved execution after Written Spec approval and Implementation Plan completion. Execution follows:

- `docs/superpowers/specs/2026-09-16-task058-deterministic-execution-runtime-contract-design.md`
- `docs/superpowers/plans/2026-09-16-task058-deterministic-execution-runtime-contract.md`

TASK-058 remains Framework governance/documentation/contracts/templates/tests only. No AI-ControlTower runtime service, Python supervisor, runtime database, scheduler/queue/worker daemon, lease/fencing service, Effect Gateway service, credential broker, sandbox/network policy, model/MCP router, RLM runtime, Multica runtime, automatic Task DONE updater, CI/merge/release bot, API server, or self-improvement runtime is authorized or introduced.

## 2. Isolation and baseline

Implementation branch `task058-framework120` was created from current canonical `main` after restoring an accidental empty probe file mutation. The probe created an empty root file `noop` and was immediately reverted on `main`; no Framework semantic/content drift remained. Implementation then proceeded only on the isolated branch.

Fresh branch baseline proved:

```text
Framework version = 1.19.0
Schema = 1.0.0
latest amendment = TASK-057
canonical pressure suite ends at Scenario 556
Scenario 557 absent
TASK-057 dependency = DONE
```

Baseline canonical pressure-scenario blob:

```text
3e6d990b40ae8a135724b3ed09a8ebaf3008993e
```

## 3. TDD RED evidence

The current connector exposes full-file replacement but no safe patch/append mutation for very large files. To preserve RED-before-production ordering without guessing/reconstructing the full 7k+ line canonical pressure file, a temporary staging RED contract was persisted:

`Framework-Source/tests/task058-pressure-scenarios-staging.md`

Commit:

`ca90855d93067c483891fccc6c9b62fa1b6798c6`

It contains Scenario classes `557–602`, each with Prompt / Temptation / Pass / Fail / GREEN expectation. It is explicitly non-final and MUST be consolidated into canonical `Framework-Source/tests/pressure-scenarios.md`, then removed, before candidate freeze.

RED production probe against Framework 1.19 Core Governance confirmed required TASK-058 semantics were absent before production implementation, including zero matches for:

```text
runtime_generation
Effect Permit
Runtime Event Journal
```

Therefore the RED contract failed for the intended reason: TASK-058 production semantics did not yet exist.

## 4. GREEN work completed on branch

### Normative amendment

Created:

`Framework-Source/references/framework-governance-amendment-260916-task058-deterministic-execution-runtime-contract.md`

Commit:

`5e2814b1d8c3357b5fb5528d6c121d2aa21df223`

Implemented declarative semantics for:

- authority/runtime ownership separation;
- four lifecycle domains;
- durable Execution/Attempt identity and contract fingerprints;
- deterministic Supervisor boundary;
- Runtime Event Journal > Checkpoint/Snapshot;
- lease/heartbeat/fence/control-generation semantics;
- `state_version` CAS semantics;
- Effect-Surface Closure;
- Effect Gateway;
- mandatory single-use JIT Effect Permit;
- target preconditions/TOCTOU;
- idempotency/reconciliation/reversibility classes;
- no arbitrary exactly-once guarantee;
- ambiguous-result reconciliation/no blind retry;
- typed Executor proposal vs runtime-event separation;
- durable hierarchical budgets/recursion limits;
- WAIT/wakeup/fail-closed liveness;
- cancellation/in-flight reconciliation;
- compensation as a separately governed effect;
- restart/store-restore recovery;
- runtime/event-schema version pinning;
- secret-safe durable observability;
- Multica/runtime separation;
- Task Record vs runtime journal separation;
- Effect Gateway conformance evidence;
- language/host neutrality and explicit no-runtime boundary.

### New Project-Execution starters — 5/5

Created:

1. `runtime-contract.md` — `f16be7088b7ce09a79dac3ebc2eedc9b19642a44`
2. `execution-attempt.md` — `5ed25bebdab4bcd82f1d4d7d1edc1be6d43d893e`
3. `execution-checkpoint.md` — `4cb8b81dd385bf65b974b359b522575b5366759d`
4. `action-journal.md` — `0f7f7ca832fa43e18a3582fa83698ac8d9d8f459`
5. `effect-policy.md` — `101dbff154fff47ca435018fa11ce4645a3b489d`

### Existing Project-Execution surfaces aligned — 6/6

Updated:

1. `task-contract.md` — `f55af086ca145e002c60bce08a45a7f941dcac4a`
2. `task-record.md` — `7723151239c8a5f0aeddcdf983a99023c7e1f39d`
3. `executor-profile.md` — `121ba56f82cd80c8c8c38c122d8ed66b844a6326`
4. `tools.md` — `fb845f70dee82139f70187c67062d8afc1068c7b`
5. `trust.md` — `5b4ede7c314d44d60a1b25e6de81625a56356666`
6. `Project-Execution/README.md` — `cdf96e98f1901820ed0b4250aecdb625fd74d7c8`

Key preservation result: TASK-048 Primary/fallback/`CHECKPOINT_FAILBACK` semantics remain in place; an unresolved prior effect remains `RESULT_VERIFICATION_REQUIRED`, and a fallback tool cannot blind-replay it.

### Release descriptor

Branch-only descriptor prepared as Framework `1.20.0` / Schema `1.0.0` with latest TASK-058 amendment:

`Framework-Source/FRAMEWORK-RELEASE.yaml`

Commit:

`259e5c8c326c52ace5b912804b417bddd08d3c56`

This descriptor does NOT imply candidate freeze or release acceptance because propagation remains incomplete.

## 5. Branch diff at checkpoint

Before this checkpoint evidence commit, branch was `14` commits ahead of `main` and changed `14` files. All production changes were Markdown/YAML documentation/contracts/templates/release metadata; no executable runtime/service/code artifact was introduced.

## 6. Tooling blocker

Current execution environment has no local repository checkout/worktree with network access. Attempted local clone failed because the container cannot resolve `github.com`.

The available GitHub connector can:

- read files/ranges;
- create files;
- replace whole UTF-8 files;
- create branches/commits/trees.

It does **not** expose safe line-level patch/append mutation. Several remaining canonical surfaces are large enough that whole-file replacement from truncated connector output risks historical/content drift and is therefore not acceptable under ProjectFramework preservation rules.

This blocks safe completion of these required in-place surfaces in the current harness:

1. consolidate scenarios `557–602` into `Framework-Source/tests/pressure-scenarios.md` and remove staging file;
2. project TASK-058 current semantics into `Framework-Source/references/core-governance-rules.md`;
3. update `Framework-Source/MIGRATION-NOTES.md` for `1.19.0 → 1.20.0`;
4. update root `README.md` current release / Framework 1.20 guidance;
5. update `Framework-Source/SKILL.md` routing/guidance;
6. update `Framework-Source/templates/00-project-source-framework.md`;
7. update `Framework-Source/templates/core-document-skeletons.md`;
8. update exactly 22 maintained Project Source mockup Framework stamps to `1.20.0`;
9. run canonical Structural GREEN and cumulative AFFECTED after the above;
10. independent fresh-context review;
11. candidate freeze;
12. exactly one final unchanged-candidate `RELEASE_FULL`;
13. release/completion evidence and truthful Task lifecycle reconciliation.

## 7. Current verification truth

```text
TDD RED = OBSERVED / INTENDED FAILURE
NORMATIVE AMENDMENT = IMPLEMENTED ON ISOLATED BRANCH
NEW STARTERS = 5/5 CREATED
EXISTING PROJECT-EXECUTION ALIGNMENT = 6/6 UPDATED
FRAMEWORK 1.20 DESCRIPTOR = PREPARED ON BRANCH
CANONICAL PRESSURE SUITE = NOT YET CONSOLIDATED
CORE GOVERNANCE PROJECTION = NOT YET UPDATED
PROPAGATION = INCOMPLETE
STRUCTURAL GREEN = NOT CLAIMED
AFFECTED = NOT RUN / NOT CLAIMED
INDEPENDENT REVIEW = NOT RUN
CANDIDATE = NOT FROZEN
RELEASE_FULL = NOT RUN
TASK-058 DONE = NOT CLAIMED
AI-CONTROLTOWER RUNTIME IMPLEMENTATION = NOT PERFORMED
```

## 8. Exact resume rule

Resume only in an execution environment that provides either:

1. a local Git checkout/worktree capable of safe line-level edits and verification; or
2. an equivalent source mutation interface that can apply bounded patches without reconstructing large canonical files from truncated reads.

At resume:

```text
fresh-read branch task058-framework120
-> verify checkpoint/head ancestry
-> consolidate canonical pressure scenarios 557–602 first
-> verify RED/GREEN scenario continuity 1–602
-> update Core/current propagation surfaces
-> remove staging pressure file
-> run structural GREEN + AFFECTED
-> independent review
-> freeze exact candidate
-> one RELEASE_FULL
-> evidence + lifecycle reconciliation
```

Do not merge/publish/release/self-host-promote or mutate AI-ControlTower merely to bypass this blocker.

## 9. Resume — bounded patch capability restored

Execution resumed after the prior checkpoint using an ephemeral branch-only GitHub Actions helper whose sole purpose was to apply exact bounded text patches to large Markdown surfaces inside a real repository checkout. The helper is not a Framework runtime/CI feature, is removed before candidate review, and grants no Project authority. This resume operation consolidated scenarios `557–602` into the canonical pressure suite, projected TASK-058 into Core/current guidance/migration/templates, and advanced durable Task truth to `IN_PROGRESS`. Candidate freeze still requires Structural GREEN, AFFECTED, independent review, and final release verification.
