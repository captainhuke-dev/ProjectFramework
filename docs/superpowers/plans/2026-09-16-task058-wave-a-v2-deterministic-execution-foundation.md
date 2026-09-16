# TASK-058 Wave A V2 Deterministic Execution Foundation Implementation Plan

> **Execution role boundary:** `GPT = PLANNER / EXECUTION_HANDOFF_REQUIRED`; `LOCAL_LLM_ENGINEER = designated TASK Executor`; `INDEPENDENT_ENGINEERING_VERIFIER = VERIFY`. GPT MUST NOT perform TASK-058 implementation-plane source/test/migration mutation or substitute itself for the designated Executor. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver a verified ProjectFramework successor to Framework `1.19.0` that implements TASK-058 Wave A V2 deterministic execution interoperability contracts while preserving ProjectFramework authority boundaries, exact historical evidence, Brownfield compatibility, and the no-runtime boundary.

**Architecture:** Use the approved **Compositional State Binding Hub**. Resolve the canonical Framework `1.19.0` self-host drift first; only after canonical self-host readback proves ProjectFramework itself is on `1.19.0` may TASK-058 normative implementation start. The normative release then adds Revision Set, Execution Input Manifest, Execution State Binding, ownership/epoch/fencing semantics, CAS/idempotent Operational Transition, Result Acceptance, Generic Result Identity, and Verification Validity as declarative contracts layered on TASK-057 without introducing a runtime/control plane.

**Tech Stack:** Markdown/YAML governance artifacts, Git/GitHub workflow, `uv run python` scratch structural verification, existing ProjectFramework pressure-scenario conventions; no application runtime, database, scheduler, lease service, CAS store, daemon, API server, or executable validator is added to the release.

**Spec:** `docs/superpowers/specs/2026-09-16-task058-wave-a-v2-deterministic-execution-foundation-design.md`

## Execution Role Boundary

- `GPT = PLANNER`. GPT owns PLAN-mode analysis, contract/plan creation and revision, evidence consumption, and REPLAN/REWORK decisions. Planning completion yields `EXECUTION_HANDOFF_REQUIRED`; it does not authorize GPT to perform implementation-plane mutation.
- `LOCAL_LLM_ENGINEER = designated TASK Executor`. Phase 0 mutation and TASK-058 implementation Tasks may execute only after the applicable Task Ready Gate passes and an eligible, runtime-bound Local LLM Executor is selected for the exact repository/workspace/task envelope.
- `INDEPENDENT_ENGINEERING_VERIFIER = VERIFY`. Independent verification is selected separately from TASK execution; the designated Local LLM Executor MUST NOT self-satisfy an independent-verifier requirement and the Verifier MUST NOT repair implementation while acting in VERIFY.
- Commands in this plan are instructions for the selected `LOCAL_LLM_ENGINEER` execution context. They are not authorization for GPT to run implementation steps directly.
- If no eligible/runtime-bound designated Local LLM Executor exists, return `NO_ELIGIBLE_EXECUTOR` and `FAIL_CLOSED`. Do not substitute GPT, Codex, generic shell automation, another undeclared agent, or an availability-based fallback.
- Integrator/canonical completion remains a separate role/boundary and requires its own current authority and downstream gates. `Verification PASS ≠ integration authority ≠ Task DONE`.

## Global Constraints

- TASK-058 status remains `TODO` until implementation actually begins; planning is not implementation.
- Execution role assignment is fixed for this plan: `GPT = PLANNER`, `LOCAL_LLM_ENGINEER = designated TASK Executor`, `INDEPENDENT_ENGINEERING_VERIFIER = VERIFY`.
- GPT MUST NOT run Phase 0 or TASK-058 implementation-plane mutation and MUST NOT invoke Inline/Subagent execution as a substitute execution path.
- `NO_ELIGIBLE_EXECUTOR → FAIL_CLOSED`: if the designated Local LLM Executor is unavailable, ineligible, or not runtime-bound to the exact target, stop and return to PLAN/REPLAN; never fall back to GPT, Codex, generic shell automation, or another undeclared executor.
- Current observed local planning baseline at plan creation: local `HEAD=e2e20d99433bc38a2063e81c5d388832b29fa2df`, local `origin/main=38f9993824b03c5afd58fee0279f717b120d7918`, `HEAD:Framework-Source=23274ada739c56a10c8edcfc14e6a9a0e46e9a0b`.
- Framework distribution is `1.19.0` / Project Source Schema `1.0.0` / release format `3` before TASK-058 execution.
- Active canonical ProjectFramework self-host is currently Framework `1.18.0`; **TASK-058 normative implementation MUST NOT begin until canonical `origin/main` self-host reconciliation to Framework `1.19.0` is completed and freshly verified.**
- Phase 0 self-host reconciliation is a separately governed Root/Project Source transaction. If valid Root/shared-state authority is not present at the required step, stop with `RECONCILIATION_REQUIRED`; do not silently absorb that authority into TASK-058.
- After Phase 0, execution MUST fresh-read `Framework-Source/FRAMEWORK-RELEASE.yaml`. This plan is valid for normative implementation only when the fresh baseline is exactly Framework `1.19.0` / Schema `1.0.0` / release format `3` and Framework-Source tree remains the verified TASK-057 tree `23274ada739c56a10c8edcfc14e6a9a0e46e9a0b`. If that baseline has advanced or changed materially, stop and revise/rebase this plan before normative mutation.
- Given the exact `1.19.0` baseline above, TASK-058 targets Framework `1.20.0` / Project Source Schema `1.0.0` / release format `3` as a backward-compatible additive Framework interface evolution. A discovered schema/namespace/authority break invalidates this classification and requires a new design/plan approval before implementation continues.
- Existing `record_version: "1.0"` Task Record and Verification Record artifacts remain valid historical contracts. V2 required shapes MUST use explicit successor contract/record versions and MUST NOT silently reinterpret v1 required fields.
- Use Task Contract `contract_version: "2.0"`, Task Record `record_version: "2.0"`, and Verification Record `record_version: "2.0"` for the V2 required shapes. Existing Plan Contract `1.0`, Executor Profile, capability/tool/trust profiles, Task lifecycle, Risk `R0–R3`, and Registered Command set remain unchanged unless a specific task below says otherwise.
- New Wave A record contracts use `record_version: "1.0"` because they are new record types: `REVISION_SET`, `EXECUTION_INPUT_MANIFEST`, `EXECUTION_STATE_BINDING`, `EXECUTION_OWNERSHIP_*`, `OPERATIONAL_TRANSITION`, `RESULT_ACCEPTANCE`, and `VERIFICATION_VALIDITY_EVALUATION`.
- Canonical execution ordering is `eligible executor → coordination claim → Execution Ownership Grant → finalize immutable Execution State Binding → CAS CLAIMED→EXECUTING`. Never finalize a binding that claims an ownership epoch before the corresponding ownership grant exists.
- `VERIFYING → VERIFIED` requires Verification `PASS`, `validity_at_verification=CURRENT`, **and a fresh applicable Result Acceptance that is still `ELIGIBLE`**.
- Immutable bindings/references must be reconstructable/state-bound; a mutable `current`/`latest` locator alone cannot serve as historical binding evidence.
- `Observation ≠ Acceptance`; `Verification Result ≠ Verification Validity`; `Coordination Claim ≠ Execution Ownership`; `Ownership ≠ AUTH`; `Ownership Epoch ≠ producer authentication`.
- Fencing assurance ordering is exactly `COORDINATION_ONLY < ACCEPTANCE_FENCED < SIDE_EFFECT_FENCED` for stale-owner protection. It is evaluated per material operation path/target, not globally per executor.
- Wave A excludes Memory Generation/Snapshot, authenticated event envelope/crypto producer identity, anti-replay transport, Resume Eligibility/Continuation Controller/Budget, Artifact build lifecycle, Release Transaction, deployment saga, health-window semantics, migration reversibility, rollback/compensation engine, and Project operational lifecycle.
- No new Project Source semantic slot, Stable-ID family, Registered Command, runtime database, queue, scheduler, lease/heartbeat daemon, distributed lock, fencing-token generator, CAS datastore, automatic transition/acceptance/verification engine, executable Project Adapter, merge bot, release/deployment orchestrator, or automatic Task DONE updater is permitted.
- Brownfield/historical Tasks are never retrofitted with invented Revision Sets, Input Manifests, State Bindings, ownership epochs, Result Acceptance, or Verification Validity records; unresolved mappings remain `UNKNOWN`.
- Projects that do not use AI-ControlTower remain valid ProjectFramework Projects.
- Pressure scenarios for TASK-058 allocate exactly `557–590`, preserving existing scenarios `1–556` and producing cumulative `1–590` contiguous/unique.
- TDD order is mandatory: pressure scenarios RED first, then normative contracts, then starter/propagation work, then cumulative AFFECTED, independent review, one final unchanged-candidate `RELEASE_FULL`, evidence, and terminal Task reconciliation.
- Publication remains separate: local implementation authority does not imply push/PR/merge/tag/GitHub Release or canonical post-1.20 self-host promotion.

---

## File Structure and Responsibility Map

### Phase 0 — canonical Framework 1.19 self-host reconciliation prerequisite

Current active inputs (fresh-read again at execution time):

- `PROJECT-BOOTSTRAP.md` — root discovery pointer, currently stamped Framework 1.18.
- `Project-Source/00-Project-Source-Framework-r005-260913-2151.md` — active `FRAMEWORK-001` root, currently 1.18.
- `Project-Source/01-Project-Source-Index-r109-260913-2302.md`
- `Project-Source/02-Project-Overview-r005-260913-2151.md`
- `Project-Source/03-Current-State-r105-260913-2302.md`
- `Project-Source/04-Decision-Log-r004-260913-2151.md`
- `Project-Source/05-Requirements-r004-260913-2151.md`
- `Project-Source/09-Handoff-r105-260913-2302.md`
- `Project-Source/10-Change-Log-r103-260913-2302.md`
- `Project-Source/11-Actor-Registry-r004-260913-2151.md`
- `Project-Source/12-Authorization-Registry-r046-260913-2302.md`
- `Project-Source/13-Evidence-Registry-r102-260913-2302.md`
- `Project-Source/14-Project-Source-Manifest-r109-260913-2302.md`
- `Project-Source/15-Action-Registry-r101-260913-2302.md`
- `Project-Source/16-Migration-Registry-r009-260913-2302.md`
- `Project-Source/17-Secret-Reference-Registry-r004-260913-2151.md`
- `Project-Source/91-Project-Management-Control-r065-260913-2302.md`
- predecessors move to `Project-Source/archive/` only through the normal successor/promote/archive transaction.

Phase 0 creates one coherent successor set. Capture one execution-time filename stamp with `uv run python -c "from datetime import datetime; print(datetime.now().astimezone().strftime('%y%m%d-%H%M'))"` and use that same stamp for every successor filename. Increment only the active revision number (`r005→r006`, `r109→r110`, etc.); preserve every Stable document ID and Project UUID. Add `MIG-005` for Framework `1.18.0→1.19.0` canonical self-host reconciliation.

### TASK-058 normative distribution files

Create:

- `Framework-Source/references/framework-governance-amendment-260916-task058-wave-a-v2-deterministic-execution-foundation.md` — full normative Wave A V2 amendment.
- `Framework-Source/templates/project-execution/revision-set.md` — Stable Resource Identity + Revision Set + completeness/digest semantics.
- `Framework-Source/templates/project-execution/execution-input-manifest.md` — materially declared execution inputs, secret-reference boundary, completeness/digest semantics.
- `Framework-Source/templates/project-execution/execution-state-binding.md` — immutable state binding referencing Revision Set/Input Manifest/R4/AUTH/workspace/ownership state-bound evidence.
- `Framework-Source/templates/project-execution/execution-ownership.md` — ownership grant/evidence, scoped epochs, lifecycle, fencing assurance, reassignment semantics.
- `Framework-Source/templates/project-execution/operational-transition-record.md` — operational aggregate version, CAS, idempotency, transition result semantics.
- `Framework-Source/templates/project-execution/result-acceptance.md` — immutable acceptance evaluations and dispositions.
- `Framework-Source/templates/project-execution/verification-validity.md` — `CURRENT | STALE | INVALIDATED | UNKNOWN` proof-validity evaluations.

Modify:

- `Framework-Source/templates/project-execution/task-contract.md` — V2 source requirements, required execution-input classes, ownership/fencing requirements; `contract_version: "2.0"` for the V2 required shape with explicit v1 compatibility rule.
- `Framework-Source/templates/project-execution/task-record.md` — `record_version: "2.0"`, `state_binding_ref`, Generic Result Identity/Result Set, ownership-at-report; preserve v1 exact-SHA history compatibility.
- `Framework-Source/templates/project-execution/verification-record.md` — `record_version: "2.0"`, exact Verification Basis, accepted result binding, evidence assessment, `validity_at_verification`; result remains exactly `PASS | FAIL | UNKNOWN`.
- `Framework-Source/templates/project-execution/project-adapter.md` — mappings for runtime-local Resource Identity, ownership/state owner locators, operational aggregate owner, and source-native result owners without turning the adapter into authority.
- `Framework-Source/templates/project-execution/integration-reconciliation.md` — compatibility note: V2 Git integration derives exact candidate SHA from verified `GIT_REVISION_SET`; non-Git Result Identity never makes Git integration applicable by itself.
- `Framework-Source/templates/project-execution/README.md` — list the seven new starter files and Wave A V2 invariants.
- `Framework-Source/references/core-governance-rules.md` — binding Core projection of the TASK-058 amendment.
- `Framework-Source/SKILL.md` — operational usage/selection/transition/acceptance/verification guidance.
- `Framework-Source/FRAMEWORK-RELEASE.yaml` — Framework 1.20.0 identity and latest TASK-058 amendment after all normative semantics are stable.
- `Framework-Source/MIGRATION-NOTES.md` — `1.19.0 → 1.20.0` affected surfaces/upgrade checklist; additive/no-retrofit/no-runtime boundaries.
- `README.md` — current release summary and Wave A V2 user-facing architecture summary.
- `Framework-Source/templates/00-project-source-framework.md` and `Framework-Source/templates/core-document-skeletons.md` — current Framework 1.20 distribution projection where version/current contract text is carried.
- 22 maintained mockup starters under `Framework-Source/templates/project-source-mockup/`: `00–17`, `40`, `60`, `91`, `92` — stamp Framework `1.20.0` / Schema `1.0.0` only; do not invent optional Project-Execution applicability.
- `Framework-Source/tests/pressure-scenarios.md` — scenarios `557–590`.
- `docs/superpowers/PROJECT-TASKS.md` — TASK-058 execution/verification/candidate/evidence lifecycle only as work actually progresses.
- `docs/superpowers/evidence/2026-09-16-task-058-wave-a-v2-deterministic-execution-foundation-release-full.md` — final state-bound release evidence after one final unchanged-candidate `RELEASE_FULL`.

Scratch-only, ignored verification:

- `.worktrees/.task058-scratch/verify_task058.py` — structural RED/GREEN/AFFECTED/RELEASE_FULL checks. Never add this file to the release candidate.

---

### Task 1: Persist written-spec approval and freeze the execution preflight

**Files:**
- Modify: `docs/superpowers/specs/2026-09-16-task058-wave-a-v2-deterministic-execution-foundation-design.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Create: `docs/superpowers/plans/2026-09-16-task058-wave-a-v2-deterministic-execution-foundation.md` (this plan; already created during planning)

**Interfaces:**
- Consumes: approved written spec commit `e2e20d99433bc38a2063e81c5d388832b29fa2df`.
- Produces: durable `WRITTEN_SPEC_USER_APPROVED / IMPLEMENTATION_PLAN_SELF_REVIEWED / EXECUTION_NOT_STARTED` state and the exact Phase 0 hard gate.

- [ ] **Step 1: Fresh-read the design, Task ledger, release descriptor, active FRAMEWORK-001, bootstrap, and Git refs**

Run:

```bash
git status --short
git rev-parse HEAD origin/main HEAD:Framework-Source
git show HEAD:Framework-Source/FRAMEWORK-RELEASE.yaml
git show HEAD:Project-Source/00-Project-Source-Framework-r005-260913-2151.md
git show HEAD:PROJECT-BOOTSTRAP.md
```

Expected before any implementation execution: clean tree; TASK-058 written spec exists and is user-approved; Framework distribution `1.19.0`; self-host still `1.18.0`; TASK-058 remains `TODO`.

- [ ] **Step 2: Record written-spec approval without starting implementation**

Change the spec header to `WRITTEN_SPEC_USER_APPROVED / IMPLEMENTATION_PLAN_SELF_REVIEWED / EXECUTION_NOT_STARTED`. In `PROJECT-TASKS.md`, set TASK-058 Design State to `WRITTEN_SPEC_USER_APPROVED`, Plan State to `WRITTEN / SELF_REVIEWED / EXECUTION_NOT_STARTED`, and leave `Status: TODO`.

- [ ] **Step 3: Verify planning-only state**

Run a scratch assertion that proves:

```text
TASK-058 count == 1
TASK-058 Status == TODO
written spec == USER_APPROVED
plan == SELF_REVIEWED / EXECUTION_NOT_STARTED
Framework-Source current version == 1.19.0
active FRAMEWORK-001 current version == 1.18.0
normative TASK-058 amendment does not yet exist
```

Expected: all PASS.

- [ ] **Step 4: Commit planning state only**

```bash
git add docs/superpowers/PROJECT-TASKS.md docs/superpowers/specs/2026-09-16-task058-wave-a-v2-deterministic-execution-foundation-design.md docs/superpowers/plans/2026-09-16-task058-wave-a-v2-deterministic-execution-foundation.md
git diff --cached --check
git commit -m "docs(task058): approve spec and add implementation plan"
```

Expected: one local documentation/planning commit; no Framework-Source or Project-Source mutation in this commit.

---

### Task 2: Phase 0A — prepare the Framework 1.19 canonical self-host reconciliation candidate

**Files:**
- Modify via successors/archive transaction: all 16 active `Project-Source/` files listed in the Phase 0 map.
- Modify: `PROJECT-BOOTSTRAP.md`.
- No `Framework-Source/` content changes.

**Interfaces:**
- Consumes: canonical Framework `1.19.0` release descriptor, TASK-057 exact Framework-Source tree `23274ada739c56a10c8edcfc14e6a9a0e46e9a0b`, TASK-057 release evidence, current 1.18 self-host set.
- Produces: local coherent Framework 1.19 self-host candidate with `MIG-005`, preserved UUID/Stable IDs/bindings/history, but no canonical completion claim before shared-state integration/readback.

- [ ] **Step 1: Re-resolve exact canonical release identity and authority before Root mutation**

Run:

```bash
git fetch origin
git rev-parse origin/main origin/main:Framework-Source
git show origin/main:Framework-Source/FRAMEWORK-RELEASE.yaml
git show origin/main:docs/superpowers/evidence/2026-09-15-task-057-ai-controltower-governance-support-layer-release-full.md
```

Required observed contract:

```text
framework_version = 1.19.0
schema_version = 1.0.0
release_format_version = 3
Framework-Source tree = 23274ada739c56a10c8edcfc14e6a9a0e46e9a0b
TASK-057 release evidence = valid for that exact unchanged tree
```

If any value differs, stop and revise the plan. Do not reconcile to a guessed/newer release.

Before mutation, resolve the applicable Root/shared-state authority. If authority is absent or narrower than the full successor/archive/Bootstrap transaction, stop with `RECONCILIATION_REQUIRED`.

- [ ] **Step 2: Create a scratch RED check for the current drift**

Create `.worktrees/.task058-scratch/verify_task058.py` with a `selfhost` mode that fails while any of these are true:

```python
assert distribution_version == "1.19.0"
assert active_root_version == "1.19.0"
assert bootstrap_version == "1.19.0"
assert all(active_doc_versions == "1.19.0")
assert root_framework_source_tree == "23274ada739c56a10c8edcfc14e6a9a0e46e9a0b"
assert migration_registry_contains_completed_mig005
```

Run:

```bash
uv run python .worktrees/.task058-scratch/verify_task058.py selfhost
```

Expected before mutation: FAIL specifically because active Root/Bootstrap/Project Source are still 1.18 and MIG-005 is absent; release distribution checks must already PASS.

- [ ] **Step 3: Materialize one coherent successor set**

Capture one filename stamp:

```bash
uv run python -c "from datetime import datetime; print(datetime.now().astimezone().strftime('%y%m%d-%H%M'))"
```

For every active Project Source document, create exactly one successor with revision incremented by one, `document_status: ACTIVE`, `supersedes` pointing to the exact old active filename, preserved `document_id`, `project_uuid`, inheritance/binding values, and:

```yaml
project_source_framework_version: "1.19.0"
project_source_schema_version: "1.0.0"
```

Archive each predecessor only after its successor is validated. Update all active routing (`01`, `14`, Bootstrap pointer) to the new exact filenames. Do not materialize optional `06–08/40/60/92` merely for completeness.

The new `00 / FRAMEWORK-001` provenance must bind Framework 1.19 to the exact verified distribution tree `23274ada739c56a10c8edcfc14e6a9a0e46e9a0b` and current canonical release commit observed in Step 1; preserve Project Location Binding exactly.

`16 Migration Registry` adds `MIG-005` with:

```text
Adoption Mode: CANONICAL_SELF_HOST_POST_RELEASE_RECONCILIATION
Source / Target: Framework 1.18.0 → 1.19.0
Schema: 1.0.0 unchanged
Release format: 3 unchanged
Release Evidence Reuse: exact TASK-057 RELEASE_FULL tree proof reused; Project-specific affected verification remains mandatory
Preserved: Project UUID, FRAMEWORK-001, Location Binding, Stable IDs, Project-specific truth, predecessor history, secret boundary
Automation Boundary: no daemon/bot/hook/CI/scheduler/updater/runtime
Status before canonical integration: VERIFIED_LOCAL / CANONICAL_INTEGRATION_PENDING
```

- [ ] **Step 4: Update `PROJECT-BOOTSTRAP.md` only as locator/routing**

Update its Framework stamp to `1.19.0` and `First Read` to the new exact active 00 filename. Preserve the invariant that Bootstrap is discovery only and never Project authority.

- [ ] **Step 5: Run self-host structural GREEN + diff hygiene**

```bash
uv run python .worktrees/.task058-scratch/verify_task058.py selfhost
git diff --check
git status --short
```

Expected: self-host structural checks PASS locally; no Framework-Source changes; predecessors preserved under archive; active routing resolves without archive traversal.

- [ ] **Step 6: Commit the local self-host candidate**

```bash
git add PROJECT-BOOTSTRAP.md Project-Source
git diff --cached --check
git commit -m "docs(self-host): reconcile ProjectFramework to Framework 1.19"
```

Record the exact candidate commit/tree in the task/evidence surfaces used for this separately governed reconciliation. Do **not** claim canonical convergence yet.

---

### Task 3: Phase 0B — verify and canonically integrate the Framework 1.19 self-host prerequisite

**Files:**
- Modify only applicable self-host lifecycle/evidence successors in `Project-Source/` after real integration/readback.
- No TASK-058 normative `Framework-Source` mutation yet.

**Interfaces:**
- Consumes: local verified self-host candidate from Task 2.
- Produces: fresh canonical `origin/main` readback proving ProjectFramework self-host is exactly Framework 1.19; this is the hard gate that unlocks Task 4+.

- [ ] **Step 1: Run Project-specific affected verification for the self-host candidate**

Verification must prove at least:

```text
active 00/01/02/03/04/05/09/10/11/12/13/14/15/16/17/91 all 1.19.0 / Schema 1.0.0
all Stable document IDs preserved
Project UUID preserved
Project Location Binding preserved byte-semantically
Bootstrap routes to active 00
all active routing resolves without archive traversal
MIG-005 is present and local status is not falsely canonical
Framework-Source tree remains 23274ada739c56a10c8edcfc14e6a9a0e46e9a0b
TASK-057 release proof is reused rather than rerun as if Framework-Source changed
```

Expected: AFFECTED PASS. Do not run a redundant TASK-057 release full against an unchanged Framework-Source tree solely for self-host metadata changes.

- [ ] **Step 2: Stop if shared-state integration authority is absent**

If push/PR/merge authority is not explicitly valid for the exact self-host candidate and canonical target, record `RECONCILIATION_REQUIRED / TASK058_BLOCKED_BEFORE_NORMATIVE_IMPLEMENTATION` and stop. **Do not start Task 4.**

- [ ] **Step 3: With exact shared-state authority, run fresh `INTEGRATION_GATE` and integrate**

Fresh-resolve candidate commit, `origin/main`, Base Freshness, exact authority, candidate evidence, mergeability/conflicts, and canonical repository identity. Integrate using the currently governed Git strategy. Never force push or rewrite history.

- [ ] **Step 4: Fresh-read canonical `origin/main` after integration**

Run:

```bash
git fetch origin
git rev-parse origin/main origin/main:Framework-Source
git show origin/main:PROJECT-BOOTSTRAP.md
git show origin/main:<active-00-successor-path>
git show origin/main:<active-01-successor-path>
git show origin/main:<active-14-successor-path>
```

Expected:

```text
origin/main Framework-Source tree = 23274ada739c56a10c8edcfc14e6a9a0e46e9a0b
active Root = Framework 1.19.0 / Schema 1.0.0
Bootstrap = Framework 1.19.0 and routes to that Root
all active Project Source = Framework 1.19.0 / Schema 1.0.0
MIG-005 = COMPLETED / PERSISTED / NOT_PENDING
```

Only after this readback may TASK-058 normative implementation begin.

- [ ] **Step 5: Rebase/fresh-start the TASK-058 implementation workspace from the canonical reconciled baseline**

At execution time invoke `superpowers:using-git-worktrees` and create an isolated TASK-058 implementation worktree/branch from fresh canonical `origin/main`. Do not perform normative TASK-058 work on a stale pre-reconciliation base.

---

### Task 4: Allocate the exact Framework 1.20 release baseline and add TASK-058 RED pressure scenarios

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`
- Create/modify scratch: `.worktrees/.task058-scratch/verify_task058.py` (ignored)
- Modify lifecycle only after execution begins: `docs/superpowers/PROJECT-TASKS.md`

**Interfaces:**
- Consumes: canonical self-host 1.19 readback from Task 3.
- Produces: TASK-058 `IN_PROGRESS`, exact target Framework 1.20.0 classification, scenarios `557–590`, and a RED structural verifier whose failures correspond only to missing Wave A V2 production contracts.

- [ ] **Step 1: Prove the baseline is still exactly eligible for this plan**

Run in the isolated worktree:

```bash
git rev-parse HEAD HEAD:Framework-Source
git show HEAD:Framework-Source/FRAMEWORK-RELEASE.yaml
uv run python .worktrees/.task058-scratch/verify_task058.py selfhost
```

Required: Framework `1.19.0`, Schema `1.0.0`, release format `3`, Framework-Source tree `23274ada739c56a10c8edcfc14e6a9a0e46e9a0b`, canonical self-host 1.19 PASS. If not exact, stop and revise plan.

- [ ] **Step 2: Mark TASK-058 implementation started**

Set Task status to `IN_PROGRESS`, readiness `SELF_HOST_1_19_RECONCILED / TDD_RED_IN_PROGRESS`, Target Release `1.20.0 / Schema 1.0.0 / format 3`. Do not create Project Source Goal/AUTH records unless separately authorized by current Goal governance.

- [ ] **Step 3: Append pressure scenarios 557–590 before normative changes**

Map the approved 34 design scenario classes exactly:

```text
557 single Git repo exact-SHA compatibility
558 multi-repo required member missing
559 optional source missing
560 same SHA + changed material dependency
561 locator changed / logical resource identity unchanged
562 mutable AUTH/R4 locator without state-bound observation
563 two CAS writers race on same aggregate version
564 accepted transition response lost + exact retry
565 same idempotency key reused for different semantic effect
566 transition timeout / outcome UNKNOWN
567 cancellation vs result-recording race
568 continuous lease renewal keeps epoch
569 expiry + same executor reacquisition creates new epoch
570 old executor result after new epoch
571 SIDE_EFFECT_FENCED required but only ACCEPTANCE_FENCED available
572 stale worker unknown non-idempotent side effect
573 successful result but Task cancelled
574 failed execution with complete governed result
575 duplicate result report
576 conflicting result identities from same execution
577 non-Git ERP operational observation
578 external transaction request sent but resulting state unknown
579 same Git SHA but different Execution State Binding
580 required verification evidence is FLAKY
581 Verification PASS then freshness expires → STALE
582 Verification PASS then material candidate/input mutation → INVALIDATED
583 selective proof-domain invalidation
584 invalidation impact cannot be bounded → UNKNOWN/fail closed
585 historical Framework 1.19 Task without V2 fields
586 ProjectFramework consumer without AI-ControlTower remains valid
587 attempt to retrofit historical ownership/input state
588 attempt to implement lease/CAS datastore inside Framework
589 attempt to introduce Memory Snapshot/automatic continuation into Wave A
590 attempt to introduce Release Transaction/deployment saga into Wave A
```

Each scenario must state Prompt / Temptation / Pass / Fail / GREEN expectation and must explicitly cover the two integrated corrections where relevant: ownership grant before binding finalization and fresh acceptance revalidation before VERIFIED promotion.

- [ ] **Step 4: Extend scratch verifier and prove RED**

The verifier must assert presence/semantics of the future TASK-058 amendment/Core/SKILL/starters and scenario numbering `1–590`. Before normative implementation, run:

```bash
uv run python .worktrees/.task058-scratch/verify_task058.py structural
```

Expected: scenarios `1–590` contiguous/unique PASS, but Wave A V2 production-contract assertions FAIL because the normative files/fields do not exist yet. Record the exact RED count in TASK-058 progress; do not require an arbitrary preselected fail count.

- [ ] **Step 5: Commit RED only**

```bash
git add Framework-Source/tests/pressure-scenarios.md docs/superpowers/PROJECT-TASKS.md
git diff --cached --check
git commit -m "test(task058): add Wave A V2 pressure scenarios"
```

Scratch verifier remains ignored/uncommitted.

---

### Task 5: Implement the normative Wave A V2 amendment and Core/SKILL projection

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260916-task058-wave-a-v2-deterministic-execution-foundation.md`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`

**Interfaces:**
- Consumes: Sections 1–6 written spec + scenarios 557–590.
- Produces: one authoritative declarative semantic contract for all Wave A V2 invariants; no runtime implementation.

- [ ] **Step 1: Author the TASK-058 amendment from the approved spec**

The amendment must explicitly define:

```text
Compositional State Binding Hub
Resource Identity ≠ Locator ≠ Revision
Revision Set completeness and immutable semantic identity
Execution Input Manifest materiality / secrets boundary
state-bound/reconstructable references
coordination claim ≠ ownership grant
scoped ownership epoch + renewal/reacquisition rules
COORDINATION_ONLY < ACCEPTANCE_FENCED < SIDE_EFFECT_FENCED
claim → ownership grant → finalize State Binding → CAS EXECUTING
Operational Aggregate version / CAS / idempotency / UNKNOWN
Task Record observation ≠ Result Acceptance
Generic Result Identity / Result Set
Verification Basis + evidence assessment
Verification result exactly PASS | FAIL | UNKNOWN
Verification Validity exactly CURRENT | STALE | INVALIDATED | UNKNOWN
fresh ELIGIBLE acceptance required before VERIFYING and again before VERIFIED promotion
Brownfield v1 compatibility/no retrofit
Wave B/C exclusions
no-runtime boundary
```

Do not add a new Project authority, Stable-ID family, semantic slot, Registered Command, Risk level, Task lifecycle value, or timestamp ordering rule.

- [ ] **Step 2: Project the exact normative subset into Core Governance**

Add a Framework 1.20 TASK-058 section after the TASK-057 projection. Core must preserve the same canonical tokens and must not introduce weaker shorthand. Explicitly retain `Task DONE ≠ MERGED ≠ PUSHED ≠ RELEASED ≠ ARTIFACT_PUBLISHED ≠ DEPLOYED` and `R4_CTX ≠ Risk R4`.

- [ ] **Step 3: Add operational guidance to SKILL**

SKILL must tell executors to:

```text
resolve state-bound inputs
select executor via existing filter-before-rank
claim coordination scope
obtain authoritative ownership grant/epoch
finalize binding
CAS into execution
record observation independently of acceptance
fresh-evaluate acceptance before promotable verification
fresh-re-evaluate acceptance before VERIFIED promotion
separate verification result from current validity
reconcile UNKNOWN at truth owner before unsafe retry
```

Never instruct GPT/Multica to self-grant ownership/AUTH or implement automatic continuation.

- [ ] **Step 4: Run focused normative checks**

```bash
uv run python .worktrees/.task058-scratch/verify_task058.py normative
git diff --check
```

Expected: all amendment/Core/SKILL semantic assertions PASS; starter assertions remain pending.

- [ ] **Step 5: Commit normative contract**

```bash
git add Framework-Source/references/framework-governance-amendment-260916-task058-wave-a-v2-deterministic-execution-foundation.md Framework-Source/references/core-governance-rules.md Framework-Source/SKILL.md
git diff --cached --check
git commit -m "feat(task058): add Wave A V2 execution governance contract"
```

---

### Task 6: Add single-responsibility Wave A V2 starters and explicit v1/v2 compatibility

**Files:**
- Create seven new files listed in the File Structure map.
- Modify: `Framework-Source/templates/project-execution/task-contract.md`
- Modify: `Framework-Source/templates/project-execution/task-record.md`
- Modify: `Framework-Source/templates/project-execution/verification-record.md`
- Modify: `Framework-Source/templates/project-execution/project-adapter.md`
- Modify: `Framework-Source/templates/project-execution/integration-reconciliation.md`
- Modify: `Framework-Source/templates/project-execution/README.md`

**Interfaces:**
- Consumes: TASK-058 normative amendment.
- Produces: maintainable starter contract surface for AI-ControlTower V4 consumers without runtime code.

- [ ] **Step 1: Create `revision-set.md` and `execution-input-manifest.md`**

`revision-set.md` must include:

```yaml
record_type: REVISION_SET
record_version: "1.0"
revision_set_ref:
resources:
  - resource_ref:
    role:
    required: true
    identity_kind: "GIT | FILE_SET | SCHEMA | EXTERNAL_CONTRACT | SOURCE_NATIVE"
    locator_ref:
    exact_revision:
    observed_at:
completeness:
  state: "COMPLETE | INCOMPLETE | UNKNOWN"
revision_set_digest:
created_at:
```

Rules: required unresolved resource blocks COMPLETE; single-repo exact SHA is a one-member set; identity/locator/revision are distinct; semantic digest excludes irrelevant timestamps/formatting.

`execution-input-manifest.md` must include materially declared input classes, source Revision Set ref, toolchain/dependencies/config/feature/schema/external-contract/material-input/environment constraint refs, completeness, digest, and explicit prohibition on secret values.

- [ ] **Step 2: Create `execution-ownership.md` and `execution-state-binding.md`**

Ownership starter must define `EXECUTION_OWNERSHIP_GRANT` and `EXECUTION_OWNERSHIP_EVIDENCE`, scoped epochs, `ACTIVE | SUSPECT | EXPIRED | REVOKED | COMPLETED | UNKNOWN`, renewal without epoch bump, reacquisition/reassignment with a new epoch, assurance levels, and source-native evidence.

State Binding starter must bind exact Revision Set/Input Manifest digests plus dispatch-time state-bound R4/AUTH/workspace evidence and the already-issued ownership grant/epoch. It is immutable historical evidence, not perpetual authority. A new world state causes revalidation/new binding, never rewrite.

- [ ] **Step 3: Create `operational-transition-record.md` and `result-acceptance.md`**

Operational Transition must include `transition_id`, `idempotency_key`, aggregate ref, expected version/state, requested state, observed before, result (`ACCEPTED | DUPLICATE_ACCEPTED | VERSION_CONFLICT | STATE_CONFLICT | AUTHORITY_REJECTED | OWNERSHIP_REJECTED | PRECONDITION_REJECTED | INVALID_TRANSITION | IDEMPOTENCY_CONFLICT | UNKNOWN`), resulting state/version, and source-native evidence. Exact duplicate recognition precedes generic CAS conflict handling; timestamps never own order.

Result Acceptance must include immutable evaluation identity/ref, exact Task Record + State Binding refs, evaluated current Task/AUTH/ownership/R4/aggregate state, and disposition exactly:

```text
ELIGIBLE
STALE_OWNERSHIP
TASK_NOT_ACTIVE
AUTHORITY_INVALID
STATE_BINDING_INVALIDATED
DUPLICATE
STATE_CONFLICT
RESULT_IDENTITY_INCOMPLETE
PRECONDITION_FAILED
UNKNOWN
```

Historical evaluations remain immutable; promotion uses the latest applicable fresh evaluation.

- [ ] **Step 4: Create `verification-validity.md`**

Define `VERIFICATION_VALIDITY_EVALUATION` with state exactly `CURRENT | STALE | INVALIDATED | UNKNOWN`. Preserve historical Verification PASS; validity is current proof usability, not a rewrite of the old result.

- [ ] **Step 5: Upgrade Task Contract/Task Record/Verification Record shapes explicitly**

`task-contract.md`: define V2 `contract_version: "2.0"` and required source/material-input/ownership/fencing declarations. Include a compatibility section stating existing Task Contract 1.0 remains valid under its original contract and is not retrofitted.

`task-record.md`: define V2 `record_version: "2.0"`, `state_binding_ref`, result observation, Generic Result Identity/Result Set, ownership-at-report, Actual IPOCV. Existing v1 `candidate_identity` stays valid historical exact-SHA evidence and maps only through an explicit compatibility view when evidence is sufficient; it is not silently rewritten.

`verification-record.md`: define V2 `record_version: "2.0"`, exact Verification Basis, accepted result, state binding, verification-time R4, structured evidence assessment, `result: PASS | FAIL | UNKNOWN`, `validity_at_verification`. Existing v1 stays historical and exact-SHA bound.

- [ ] **Step 6: Update adapter/integration/README composition**

Project Adapter gains locator mappings for declared operational aggregate owner, ownership owner, runtime-local logical resource refs, and source-native result owners; still `Adapter ≠ owner`.

Integration Reconciliation adds only the compatibility rule for V2 Git result: exact Git candidate comes from verified `GIT_REVISION_SET`. Do not generalize Git integration into Wave C deployment semantics.

Project-Execution README lists all starters and core invariants.

- [ ] **Step 7: Run starter structural GREEN**

```bash
uv run python .worktrees/.task058-scratch/verify_task058.py starters
uv run python .worktrees/.task058-scratch/verify_task058.py structural
git diff --check
```

Expected: all new starter and v1/v2 compatibility checks PASS; any remaining failures are propagation/release metadata only.

- [ ] **Step 8: Commit starter contracts**

```bash
git add Framework-Source/templates/project-execution
git diff --cached --check
git commit -m "feat(task058): add Wave A V2 declarative execution starters"
```

---

### Task 7: Propagate Framework 1.20 release identity and migration guidance

**Files:**
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `README.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: 22 maintained mockup starter files (`00–17`, `40`, `60`, `91`, `92`).
- Modify: `docs/superpowers/PROJECT-TASKS.md` progress metadata.

**Interfaces:**
- Consumes: stable TASK-058 normative/starter contract.
- Produces: one coherent Framework `1.20.0` distribution candidate; Schema remains `1.0.0`; release format remains `3`.

- [ ] **Step 1: Update release descriptor exactly**

Set:

```yaml
framework_version: "1.20.0"
schema_version: "1.0.0"
release_format_version: 3
latest_framework_amendment: "references/framework-governance-amendment-260916-task058-wave-a-v2-deterministic-execution-foundation.md"
```

Preserve all unrelated bootstrap/upgrade/assurance policy fields.

- [ ] **Step 2: Add `1.19.0 → 1.20.0` migration notes**

Document affected surfaces, v1/v2 compatibility, no Brownfield retrofit, V2 opt-in/applicability, Wave B/C exclusion, scenario range `557–590`, and no-runtime boundary. State that non-ControlTower Projects remain valid.

- [ ] **Step 3: Update root README current-release summary**

Explain Wave A V2 in user-facing terms without turning runtime concepts into Project authority. Preserve existing 1.19 history rather than rewriting it.

- [ ] **Step 4: Update maintained generic templates/stamps**

Update the current Framework version/schema stamp in `templates/00-project-source-framework.md`, `core-document-skeletons.md`, and all 22 current mockup starters. Do not add Wave A V2 execution records inside Project Source starters merely for completeness; Project-Execution remains optional/applicability-driven outside `00–99`.

- [ ] **Step 5: Verify launchers/current command surface remain unchanged unless required**

TASK-058 introduces no Registered Command and no new bootstrap requirement. Compare `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md` and `CLAUDE-PROJECT-INSTRUCTIONS.md` against the pre-TASK-058 baseline. If they contain no stale release-bound text, leave them byte-unchanged and record that fact in AFFECTED verification.

- [ ] **Step 6: Run propagation checks**

```bash
uv run python .worktrees/.task058-scratch/verify_task058.py propagation
uv run python .worktrees/.task058-scratch/verify_task058.py structural
git diff --check
```

Expected: structural `GREEN`; scenarios `1–590` contiguous/unique; 22/22 maintained starter stamps at `1.20.0 / 1.0.0`; no runtime files introduced.

- [ ] **Step 7: Commit release propagation**

```bash
git add Framework-Source/FRAMEWORK-RELEASE.yaml Framework-Source/MIGRATION-NOTES.md README.md Framework-Source/templates/00-project-source-framework.md Framework-Source/templates/core-document-skeletons.md Framework-Source/templates/project-source-mockup docs/superpowers/PROJECT-TASKS.md
git diff --cached --check
git commit -m "chore(task058): prepare Framework 1.20 release surfaces"
```

---

### Task 8: Run cumulative AFFECTED verification and independent review

**Files:**
- Scratch-only verifier: `.worktrees/.task058-scratch/verify_task058.py`
- Modify only if findings require correction: the exact affected normative/starter/propagation files.
- Update: `docs/superpowers/PROJECT-TASKS.md` with observed review/verification facts only.

**Interfaces:**
- Consumes: complete Framework 1.20 implementation candidate before release freeze.
- Produces: AFFECTED PASS + independent review with no unresolved Critical/Important findings.

- [ ] **Step 1: Run cumulative AFFECTED verification**

The verifier must check at minimum:

```text
scenario range 1–590 contiguous/unique
TASK-058 amendment/Core/SKILL token and semantic alignment
Task Contract 2.0 / Task Record 2.0 / Verification Record 2.0 compatibility rules
all seven new starter files and required enums
claim → ownership grant → finalize binding ordering
fresh acceptance revalidation before VERIFIED
state-bound reference rule
CAS + idempotency + UNKNOWN semantics
fencing levels/order/per-target applicability
Observation ≠ Acceptance
Verification Result ≠ Validity
non-Git Result Identity support
no post-hoc ACCEPTED_VARIANCE/requirement relaxation
Brownfield no retrofit
no Wave B/C leakage
Project-Execution optionality
22/22 starter stamps 1.20/1.0
Framework release descriptor + latest amendment consistency
no Registered Command/Risk/Task lifecycle/Stable-ID/semantic-slot expansion
no runtime/executable files
historical TASK-057 design/amendment/evidence left intact
git diff --check
```

Run:

```bash
uv run python .worktrees/.task058-scratch/verify_task058.py affected
```

Expected: all checks PASS. Record exact pass count from the run; do not pre-invent a count.

- [ ] **Step 2: Request independent fresh-context review**

Reviewer brief must include the written spec, TASK-057 amendment, TASK-058 amendment, all Project-Execution starters, migration notes, scenarios 557–590, and diff against the post-self-host canonical 1.19 baseline.

Required review questions:

```text
Any authority leak?
Any silent runtime implementation?
Any v1 history reinterpretation?
Any ownership/binding ordering contradiction?
Any stale-owner result promotion path?
Any timestamp ordering path?
Any UNKNOWN→PASS path?
Any verification PASS/validity collapse?
Any Wave B/C leakage?
Any Git-only universal assumption remaining?
```

- [ ] **Step 3: Apply reviewer findings only when technically valid**

For every finding, verify against the written spec before editing. Fix Critical/Important findings; Minor findings may be fixed when they improve unambiguous conformance without scope creep. Re-run affected verification after every semantic fix.

- [ ] **Step 4: Commit review fixes and observed review state**

Use focused commit(s), e.g.:

```bash
git add <exact-fixed-files> docs/superpowers/PROJECT-TASKS.md
git diff --cached --check
git commit -m "fix(task058): address independent Wave A V2 review"
```

Do not create an empty review-fix commit if no files change.

---

### Task 9: Freeze the Framework 1.20 candidate and run exactly one final RELEASE_FULL

**Files:**
- Create: `docs/superpowers/evidence/2026-09-16-task-058-wave-a-v2-deterministic-execution-foundation-release-full.md`
- Modify after evidence exists: `docs/superpowers/PROJECT-TASKS.md`

**Interfaces:**
- Consumes: unchanged candidate with AFFECTED PASS and accepted independent review.
- Produces: exact candidate/tree/Framework-Source tree identity + one `RELEASE_FULL` PASS + durable state-bound evidence.

- [ ] **Step 1: Freeze the candidate commit**

Commit any final implementation-state metadata required before candidate freeze, then capture:

```bash
git rev-parse HEAD HEAD^{tree} HEAD:Framework-Source
git status --short
```

Required: clean tree. Record exact commit SHA, repository tree SHA, and Framework-Source tree SHA as candidate identity.

- [ ] **Step 2: Re-run AFFECTED on the frozen candidate**

```bash
uv run python .worktrees/.task058-scratch/verify_task058.py affected
```

Expected: PASS on exactly the frozen candidate.

- [ ] **Step 3: Run one final `RELEASE_FULL` on that unchanged candidate**

```bash
uv run python .worktrees/.task058-scratch/verify_task058.py release-full
```

Release-full must include AFFECTED plus Framework-wide integrity checks used by current ProjectFramework releases: release descriptor/amendment alignment, current starter stamps, pressure scenario continuity, launcher/current command preservation, historical integrity, diff hygiene, no runtime expansion, and exact candidate/tree identity.

Expected: `PASS_RUN_1`. If any candidate content changes afterward, invalidate this evidence and create a new candidate; never claim the old PASS for the new tree.

- [ ] **Step 4: Write release evidence**

Evidence must record:

```text
TASK-058
Framework 1.20.0 / Schema 1.0.0 / format 3
candidate commit/tree/Framework-Source tree
self-host 1.19 prerequisite readback identity
scenario range 1–590
AFFECTED exact count/result
independent review result
RELEASE_FULL exact count/result / PASS_RUN_1
v1 compatibility statement
Wave B/C exclusion
no-runtime file-type/scope confirmation
publication state = NOT_PUSHED unless separately authorized
```

- [ ] **Step 5: Commit evidence**

```bash
git add docs/superpowers/evidence/2026-09-16-task-058-wave-a-v2-deterministic-execution-foundation-release-full.md
git diff --cached --check
git commit -m "docs(task058): record Framework 1.20 release evidence"
```

Evidence commit occurs after the verified candidate and must clearly distinguish evidence-commit HEAD from the frozen release candidate identity.

---

### Task 10: Reconcile TASK-058 local lifecycle and stop at the publication boundary

**Files:**
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Modify Project Source lifecycle/evidence only if an independently valid active Goal/AUTH requires and authorizes those exact updates; never synthesize OUT/AUTH/ACT/ENV after the fact.

**Interfaces:**
- Consumes: frozen candidate PASS, release evidence commit, fresh local readback.
- Produces: truthful local TASK-058 terminal state and exact next boundary; no unauthorized publication.

- [ ] **Step 1: Fresh-read candidate/evidence/working tree**

```bash
git log -3 --oneline
git status --short
git show <frozen-candidate-sha>:Framework-Source/FRAMEWORK-RELEASE.yaml
git show <evidence-commit-sha>:docs/superpowers/evidence/2026-09-16-task-058-wave-a-v2-deterministic-execution-foundation-release-full.md
```

Verify the evidence names the exact frozen candidate and release tree.

- [ ] **Step 2: Mark TASK-058 `DONE` only if all completion requirements are actually satisfied**

Required local completion facts:

```text
written spec user-approved
plan executed
Phase 0 canonical self-host 1.19 prerequisite verified
scenarios 557–590 implemented and GREEN
normative/starter/propagation contracts complete
AFFECTED PASS
independent review accepted
one final unchanged-candidate RELEASE_FULL PASS_RUN_1
evidence committed
completion commit observed
no unresolved Critical/Important finding
working tree clean or explicitly explained
```

Record publication dimensions truthfully (`NOT_PUSHED`, `NOT_RELEASED`, etc.) unless separately observed otherwise.

- [ ] **Step 3: Commit terminal Task ledger state**

```bash
git add docs/superpowers/PROJECT-TASKS.md
git diff --cached --check
git commit -m "docs(task058): record verified local completion"
```

- [ ] **Step 4: Stop before publication unless separately authorized**

Do not push, open/update PR, merge, tag, publish a GitHub Release, or perform canonical Framework 1.20 self-host promotion under this plan merely because local TASK-058 is DONE. If Framework 1.20 is later integrated to canonical `main`, current canonical self-host rules require a fresh post-merge 1.20 self-host reconciliation under separate valid Root/shared-state authority.

---

## Plan Self-Review Checklist

Before offering execution, verify all of the following against the written spec:

1. Every Section 1–6 requirement maps to a task above.
2. Phase 0 is a hard prerequisite, not a hidden setup step; canonical 1.19 self-host readback is required before normative TASK-058 mutation.
3. Plan invalidates itself if the post-Phase-0 baseline is not exactly Framework 1.19.0 / Schema 1.0.0 / Framework-Source tree `23274ada739c56a10c8edcfc14e6a9a0e46e9a0b`.
4. Framework target is exactly 1.20.0 only under that baseline; Project Source Schema remains 1.0.0.
5. Scenario allocation is exactly 557–590 (34 classes), cumulative 1–590.
6. `claim → ownership grant → finalize State Binding → CAS EXECUTING` is represented consistently.
7. `VERIFYING → VERIFIED` rechecks Result Acceptance = ELIGIBLE after verification.
8. V1 Task/Verification records remain historical; V2 required shapes use explicit 2.0 versions rather than reinterpretation.
9. New record types each have single responsibility; no mega-record.
10. `Observation ≠ Acceptance`, `Verification Result ≠ Verification Validity`, `Ownership ≠ AUTH`, `Epoch ≠ authentication` remain explicit.
11. Non-Git results are supported without weakening exact-SHA Git compatibility.
12. UNKNOWN is never normalized to PASS and ambiguous side effects use `RESULT_VERIFICATION_REQUIRED` before unsafe retry.
13. Required fencing cannot silently downgrade; assurance is evaluated per operation path/target.
14. Wave B/C concepts are explicitly excluded.
15. No runtime/executable infrastructure is added.
16. Brownfield history is not retrofitted.
17. ProjectFramework remains usable without AI-ControlTower.
18. Existing Task lifecycle, Risk R0–R3, Stable-ID namespace, Registered Commands, release format, and Project Source Schema family remain unchanged.
19. AFFECTED verification and independent review occur before candidate freeze.
20. Exactly one final RELEASE_FULL runs on the unchanged candidate; evidence is state-bound.
21. Publication and post-1.20 self-host promotion remain separately governed.
22. Plan contains no unresolved placeholder markers, no vague generic test/error-handling steps, and no undefined implementation interface.
23. GPT is PLAN-only for implementation work and never performs TASK-058 implementation-plane source/test/migration mutation.
24. `LOCAL_LLM_ENGINEER` is the designated TASK Executor for Phase 0 and TASK-058 implementation after Ready Gate + runtime-binding checks.
25. Independent verification remains a separate `INDEPENDENT_ENGINEERING_VERIFIER / VERIFY` role and is not satisfied by the Task Executor.
26. `NO_ELIGIBLE_EXECUTOR → FAIL_CLOSED`; the plan contains no GPT/Codex/generic-shell/undeclared-executor fallback path.
