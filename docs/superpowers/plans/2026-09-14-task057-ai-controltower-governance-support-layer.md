# TASK-057 AI-ControlTower Governance Support Layer Implementation Plan

> **Execution handoff:** `GPT = PLANNER / EXECUTION_HANDOFF_REQUIRED`. Planning completion does not assign execution. This approved plan MUST be handed to the applicable execution-control layer, which selects an eligible Executor from the current Task Contract, Execution Envelope, AUTH, `R4_CTX`, capability/tool/trust/executor policy, and Ready Gate. `Planner ≠ Executor ≠ Verifier`; GPT MUST NOT self-promote into TASK execution merely because planning is complete. Independent Verifier selection, when required, is separate from Executor selection.
>
> **For a selected agentic Executor:** after governed selection, use superpowers:subagent-driven-development or superpowers:executing-plans if supported by that execution environment. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement ProjectFramework `1.19.0` declarative PLAN/TASK/VERIFY governance support for AI-ControlTower/Multica consumers without implementing their runtime.

**Architecture:** Extend existing Core Governance and `Project-Execution/` with schema-first declarative contracts, state-bound verification, source-owner reconciliation, and maintained starters. Keep Project/Task/AUTH/Git authority where it already lives; `R4_CTX`, Ready Gate, claims, profiles, adapters, and execution state are derived/eligibility/coordination constructs only.

**Tech Stack:** Markdown, YAML, Git, Python 3 scratch verification only; no committed executable validator/runtime.

**Spec:** `docs/superpowers/specs/2026-09-14-task057-ai-controltower-governance-support-layer-design.md`

## Global Constraints

- Framework `1.19.0`; Project Source Schema `1.0.0`; release format `3`.
- Approach A — Schema-first Declarative Contracts.
- Canonical Risk remains `R0–R3`; `R4_CTX` is current-truth context, not Risk R4.
- Canonical Task lifecycle remains `TODO | IN_PROGRESS | DONE | BLOCKED | CANCELLED`; operational execution state is separate.
- No new Project Source semantic slot or Stable-ID family. Execution Envelope is nested Task constraint data, not Project Source `ENV-*`.
- `Contract ≠ Authority`; `Capability ≠ Authority`; `Eligibility ≠ Authority`; `Claim ≠ Authority`; `Verification PASS ≠ Task DONE`.
- Expected IPOCV and Actual IPOCV remain separate; I/P/O/C/V are mandatory, with explicit `NOT_APPLICABLE` + reason when genuinely inapplicable.
- Ready Gate returns exactly `PASS | FAIL | UNKNOWN` and fails closed on unknown/stale/conflicted mandatory truth.
- Multica owns coordination facts only and cannot set Task DONE or own Project/AUTH/Git/verification/release truth.
- Executor selection is filter-before-rank; TASK and VERIFY are separate evaluations; VERIFY support alone is not independent-review qualification.
- Material Git verification binds repository + exact commit SHA. Fresh `INTEGRATION_GATE` remains mandatory before shared-state mutation.
- Brownfield historical Tasks are not silently retrofitted.
- TASK-057 planner boundary: GPT is Planner; after plan completion state is `EXECUTION_HANDOFF_REQUIRED`; Executor selection belongs to the applicable execution-control layer using current Task Contract, Execution Envelope, AUTH, `R4_CTX`, capability/tool/trust/executor policy, and Ready Gate; independent Verifier selection remains separate when applicable.
- Do not implement AI-ControlTower runtime, Multica runtime, Control Plane, scheduler, queue, database/event store, leases/fencing, distributed lock, state engine, router, executable adapter, merge bot/queue, CI runner, API server, automatic Task DONE/reconciliation, Structured Core, Generated Governance, or Transaction Mode runtime.
- Pressure scenarios are RED-first. Allocate required classes contiguously as scenarios `529–556`.
- One final `RELEASE_FULL` on the unchanged final candidate; rerun only after candidate-invalidating change.
- Push/PR/merge/tag/Release/self-host promotion/consumer upgrade remain separately governed.

---

### Task 1: Add RED pressure scenarios 529–556

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`

**Interfaces:**
- Consumes: approved spec §15.
- Produces: one scenario for each required pressure class.

- [ ] Append scenarios 529–556 in this exact order: missing Contract/IPOCV field inference; explicit `NOT_APPLICABLE` reason; R4_CTX≠Risk R4; Envelope cannot expand AUTH; Ready Gate UNKNOWN≠PASS; execution state cannot mutate Task lifecycle; Multica claim≠AUTH/DONE; stale claim recovery reads durable/source-native effects; no inferred parallelism; filter-before-rank; no arbitrary fallback; VERIFY support≠independent verifier; Adapter≠source of truth; domain-owner conflict resolution; exact candidate SHA binding; candidate mutation invalidation; exact unchanged RELEASE_FULL reuse; fresh INTEGRATION_GATE; FAST_FORWARD_EXACT identity; merge-commit reconciliation; transforming integration proof boundary; exact-equivalence proof boundary; unknown merge verify-before-retry; local DONE≠publication; integration-required completion waits; post-merge reconciliation cannot expand authority; Brownfield no retrofit; no AI-ControlTower/Multica runtime.
- [ ] Run a scratch Python check that scenario headings are exactly `1..556` and unique. Expected: PASS.
- [ ] Run a scratch token probe against current Core Governance for `R4_CTX`, `PLAN_CONTRACT_VALID`, `EXPECTED_IPOCV_COMPLETE`, `READY_FOR_CLAIM`, `NO_ELIGIBLE_EXECUTOR`, and the 3 integration strategy names. Expected before normative implementation: FAIL (RED).
- [ ] Commit: `test(task057): add governance support pressure scenarios`.

### Task 2: Implement normative execution contracts

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260914-task057-ai-controltower-governance-support-layer.md`
- Modify: `Framework-Source/references/core-governance-rules.md`

**Interfaces:**
- Consumes: Task 1 RED contract.
- Produces: canonical PLAN/TASK/VERIFY, R4, contract/record, Ready Gate, execution-state, Multica/source-owner semantics.

- [ ] Add PLAN/TASK/VERIFY mode semantics and `R4_CTX / current_truth_context`; state explicitly that Risk remains `R0–R3`.
- [ ] Add Plan Contract and Task Contract shapes from the spec. Task Contract owns intent/acceptance/dependencies/completion/Expected IPOCV/integration applicability; Plan Contract must not duplicate authoritative success semantics.
- [ ] Add nested Execution Envelope with allowed scope/workspaces/mutation classes, prohibited effects, required AUTH refs, `R4_REQUIRED`, concurrency constraints, and `VERIFY_BEFORE_RETRY` unknown-result recovery.
- [ ] Add mandatory Expected IPOCV and separate Task Record/Actual IPOCV with comparison vocabulary `MATCH | ACCEPTED_VARIANCE | MISMATCH | UNKNOWN`.
- [ ] Add state-bound Verification Record with result `PASS | FAIL | UNKNOWN` and invalidation conditions.
- [ ] Add pure fail-closed Task Ready Gate requiring planning readiness, valid contracts/envelope, complete Expected IPOCV, satisfied dependencies, resolved R4/AUTH/executor/source owners, and no blocking conflict.
- [ ] Add operational state domain `PROPOSED → READY_FOR_CLAIM → CLAIMED → EXECUTING → RESULT_RECORDED → VERIFYING → VERIFIED → INTEGRATION_PENDING → INTEGRATED → CLOSED` plus exception states, explicitly separate from canonical Task lifecycle.
- [ ] Add Multica coordination-only boundary and domain-owner conflict examples from the spec.
- [ ] Re-run Task 1 token probe. Expected: PASS.
- [ ] Commit: `feat(task057): add declarative execution governance contracts`.

### Task 3: Implement executor, exact-SHA verification, and integration rules

**Files:**
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: TASK-057 amendment from Task 2.

**Interfaces:**
- Consumes: Task 2 vocabulary.
- Produces: deterministic selection, candidate verification, integration eligibility/reconciliation, Task DONE boundary.

- [ ] Encode exact filter-before-rank order from spec §9 and `NO_ELIGIBLE_EXECUTOR`; prohibit undeclared fallback; evaluate TASK and VERIFY separately.
- [ ] Define Material Git candidate identity fields: repository, commit SHA, tree SHA, worktree/branch ref, observed time; canonical verification identity is repository + exact commit SHA.
- [ ] Define `VERIFIED ≠ INTEGRATION_ELIGIBLE ≠ MERGED` and fresh `INTEGRATION_GATE` inputs: candidate, target/base freshness, AUTH, review, verification validity, PR/head identity when applicable, conflicts/mergeability.
- [ ] Define `FAST_FORWARD_EXACT`, `MERGE_COMMIT_PRESERVING_CANDIDATE`, `TRANSFORMING_INTEGRATION`, deterministic exact-equivalence proof reuse, and `RESULT_VERIFICATION_REQUIRED` after ambiguous shared effects.
- [ ] Define Integration Reconciliation and Task completion rules: local-only DONE may remain unpublished; integration-required DONE waits; ControlTower/Multica cannot set DONE directly; merged content may still be `RECONCILIATION_REQUIRED`.
- [ ] Run focused scratch checks for all strategy/result tokens and authority-separation statements. Expected: PASS.
- [ ] Commit: `feat(task057): add exact-sha verification and integration reconciliation`.

### Task 4: Add maintained Project-Execution starters

**Files:**
- Create: `Framework-Source/templates/project-execution/plan-contract.md`
- Create: `Framework-Source/templates/project-execution/task-contract.md`
- Create: `Framework-Source/templates/project-execution/task-record.md`
- Create: `Framework-Source/templates/project-execution/verification-record.md`
- Create: `Framework-Source/templates/project-execution/executor-profile.md`
- Create: `Framework-Source/templates/project-execution/project-adapter.md`
- Create: `Framework-Source/templates/project-execution/integration-reconciliation.md`
- Modify: `Framework-Source/templates/project-execution/README.md`
- Modify: `Framework-Source/templates/project-execution/capabilities.md`
- Modify: `Framework-Source/templates/project-execution/tools.md`
- Modify: `Framework-Source/templates/project-execution/trust.md`

**Interfaces:**
- Consumes: Tasks 2–3 normative definitions.
- Produces: optional/applicability-driven declarative artifacts.

- [ ] `plan-contract.md`: minimum PLAN shape from spec §4.1.
- [ ] `task-contract.md`: minimum TASK shape from §4.2, nested Execution Envelope, complete Expected IPOCV with explicit N/A reason form.
- [ ] `task-record.md`: Task/Plan/contract refs, execution ref, resolved current truth, Actual IPOCV, artifacts/evidence, candidate identity, execution result.
- [ ] `verification-record.md`: task/plan/record refs, verified candidate/current truth, acceptance/IPOCV/control results, evidence, `PASS|FAIL|UNKNOWN`, invalidation conditions.
- [ ] `executor-profile.md`: supported modes/work classes, capability/tool/trust refs, limits, workspace roles, coordination support, independent-verifier qualification separate from generic VERIFY support.
- [ ] `project-adapter.md`: owner/locator mapping only; explicitly not Project Source, Task Source, Git/GitHub, AUTH, or runtime authority.
- [ ] `integration-reconciliation.md`: candidate SHA, strategy, target, pre-target SHA, result SHA, candidate relation, proof reuse/reverification state, source-native evidence, result.
- [ ] Update `Project-Execution/README.md` inventory and applicability rules; align capabilities/tools/trust so none grants authority.
- [ ] Run scratch check: 7/7 new files exist and contain PLAN/TASK, expected/actual IPOCV, R4_REQUIRED, verification result vocabulary, and integration strategy vocabulary.
- [ ] Commit: `feat(task057): add declarative execution contract starters`.

### Task 5: Propagate agent/user guidance

**Files:**
- Modify: `Framework-Source/SKILL.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: Tasks 2–4.
- Produces: discoverable Framework guidance without new authority or mandatory AI-ControlTower adoption.

- [ ] Add applicable read/routing order: Task Source/Task Contract → Plan Contract when separate → applicable AUTH → R4 domain-owner truth → Project-Execution profiles → Ready Gate → TASK/VERIFY.
- [ ] Preserve explicit `R4_CTX≠Risk R4`, `Ready Gate PASS≠AUTH`, `Claim≠AUTH`, `VERIFY support≠independent verifier`, `Verification PASS≠Task DONE`.
- [ ] Point Framework template/skeleton guidance to optional Project-Execution starters without allocating a new Project Source slot.
- [ ] Update README with Framework 1.19 declarative support and explicit no-runtime boundary.
- [ ] Run scratch propagation check: PLAN/TASK/VERIFY appear in all four surfaces and `R4_CTX` appears in SKILL.
- [ ] Commit: `docs(task057): propagate governance support guidance`.

### Task 6: Prepare 1.19 release metadata and maintained stamps

**Files:**
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: all 22 `*.template.md` files under `Framework-Source/templates/project-source-mockup/` (00–17, 40, 60, 91, 92).

**Interfaces:**
- Consumes: completed Tasks 2–5.
- Produces: coherent 1.19.0 distribution metadata; does not self-promote live `Project-Source/`.

- [ ] Set `framework_version: "1.19.0"`, keep schema `1.0.0`, release format `3`, and point `latest_framework_amendment` to the new TASK-057 amendment.
- [ ] Add migration notes: additive adoption; no historical retrofit; non-ControlTower Projects remain valid; optional/applicability-driven Project-Execution contracts; no new slot/Stable-ID family.
- [ ] Update exactly 22 maintained starter Framework stamps to 1.19.0; do not alter historical specs/evidence or active self-host `Project-Source/` pin.
- [ ] Run scratch check: descriptor 4/4 fields correct and exactly 22 starter templates carry 1.19.0.
- [ ] Commit: `chore(task057): prepare Framework 1.19 release metadata`.

### Task 7: AFFECTED verification and independent review

**Files:**
- Modify only files required to fix review findings.

**Interfaces:**
- Consumes: Tasks 1–6 candidate.
- Produces: clean reviewed candidate eligible for freeze.

- [ ] Run `git diff --check` across TASK-057 changes.
- [ ] Run AFFECTED scratch verifier covering: scenarios 1–556 contiguous/unique; all 28 new classes; release descriptor; 7 starter files; contract/record minimum fields; IPOCV completeness; R4/Risk separation; Ready Gate semantics; unchanged canonical Task lifecycle; separate execution state; Multica boundary; filter-before-rank; TASK/VERIFY separation; exact-SHA binding; fresh integration gate; 3 strategies; ambiguous-result recovery; DONE/publication separation; Brownfield rule; 22/22 stamps; and no runtime/executable artifact. Record exact `TASK057_AFFECTED N/N PASS`.
- [ ] Invoke `superpowers:requesting-code-review` or available independent-review equivalent on the full TASK-057 diff. Require zero unresolved Critical/Important findings.
- [ ] Fix material findings only, rerun focused checks, and rerun AFFECTED if normative semantics changed.
- [ ] Commit review fixes only if needed: `fix(task057): address governance support review findings`.

### Task 8: Freeze candidate, run one RELEASE_FULL, persist evidence

**Files:**
- Create: `docs/superpowers/evidence/2026-09-14-task-057-ai-controltower-governance-support-layer-release-full.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md` only at proven lifecycle checkpoints.

**Interfaces:**
- Consumes: Task 7 reviewed candidate.
- Produces: exact candidate identity, one final release proof, durable completion evidence, truthful lifecycle state.

- [ ] Require clean working tree; record candidate commit SHA, repository tree SHA, and Framework-Source tree SHA.
- [ ] Run exactly one final RELEASE_FULL on that unchanged candidate. It must include AFFECTED checks plus existing Framework release invariants (Registered Commands, scenario continuity, maintained starters, descriptor/migration routing, historical provenance, launcher constraints where applicable, and no unexpected runtime additions). Record `TASK057_RELEASE_FULL N/N PASS_RUN_1`.
- [ ] If candidate content is wrong, invalidate it, fix+commit, re-establish candidate identity, rerun affected checks, then run RELEASE_FULL once on the new unchanged candidate. Do not reuse failed candidate proof.
- [ ] Create evidence recording: approved spec + approval date; plan path; scenario range; implementation commits; independent review; AFFECTED result; candidate/tree/Framework-Source tree; RELEASE_FULL result; no-runtime confirmation; truthful publication/self-host state.
- [ ] Update Task ledger only to what is actually proven. If shared-state/self-host integration is not authorized, preserve `LOCAL_VERIFIED_COMPLETE` vs publication/reconciliation instead of claiming merged/published state.
- [ ] Commit evidence/lifecycle checkpoint and freshly read back the exact completion commit.
- [ ] Stop before push/PR/merge/tag/Release/self-host promotion/consumer upgrade unless exact current authority separately covers that shared-state action and a fresh `INTEGRATION_GATE` passes.

## Plan Self-Review

- Spec coverage: §§2–16 map to Tasks 1–8; all 28 required pressure classes map one-to-one to scenarios 529–556.
- Placeholder scan: no TBD/TODO implementation placeholders.
- Vocabulary consistency: R4_CTX, Ready Gate, Task lifecycle, operational states, integration strategies, and ambiguous-result recovery match the approved spec.
- Scope: governance/docs/starters only; no runtime or new Project Source Stable-ID family.
- Publication boundary: implementation verification remains distinct from shared-state publication/self-host promotion.
- Execution handoff boundary: GPT remains Planner until a separate governed execution decision selects an eligible Executor; plan completion alone never starts TASK execution.
