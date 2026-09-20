# TASK-059 V3 Forward-Port Runtime Contract Implementation Plan

Date: `2026-09-20` (Asia/Bangkok)
State: `WRITTEN / SELF_REVIEWED / WRITTEN_SPEC_USER_APPROVED / EXECUTION_HANDOFF_REQUIRED`
Spec: `docs/superpowers/specs/2026-09-20-task059-v3-forward-port-runtime-contract-design.md`

## Goal

Produce the final standalone ProjectFramework runtime-control contract release by forward-porting only the non-overlapping, still-useful V3 semantics onto Framework 1.20, then create a precise handoff contract for AI-ControlTower's later Python Supervisor/RLM implementation.

## Execution boundary

- `GPT = PLANNER`.
- `LOCAL_LLM_ENGINEER = designated TASK Executor profile`; `Hermes = selected Executor implementation` by ACTOR-001 on 2026-09-20.
- Hermes may execute only after fresh Task Ready Gate plus exact runtime/workspace/tool binding, applicable AUTH/R4_CTX and executor/trust eligibility all PASS.
- If Hermes is unavailable, stale-bound or cannot prove the exact target binding, return `NO_ELIGIBLE_EXECUTOR / FAIL_CLOSED`; do not substitute GPT, Codex, generic shell automation or another undeclared Executor.
- Independent Verifier remains separate.
- No AI-ControlTower runtime mutation occurs in this plan.
- No canonical-source cutover occurs in this plan.
- Push/PR/merge/tag/Release remain separately governed.

## Phase 0 — baseline and collision reconciliation

- [ ] Fresh-read canonical `origin/main`, Framework release descriptor, TASK-058 evidence, active self-host and task ledger.
- [ ] Prove baseline is exactly Framework `1.20.0` / Schema `1.0.0` / format `3`.
- [ ] Compare historical V3 against current TASK-058 amendment/Core/SKILL/starters.
- [ ] Build a retained / already-satisfied / rejected V3 concept matrix.
- [ ] Verify current pressure scenarios end at `590`.
- [ ] Re-plan if Framework baseline or schema has materially changed.

## Phase 1 — RED pressure contract

- [ ] Allocate a new contiguous scenario range starting at `591`.
- [ ] Cover worker/process death, runtime restart, checkpoint corruption, event duplication/order, liveness expiry, Effect Gateway mediation, stale/replayed permits, ambiguous non-idempotent effects, authority/current-truth changes at dispatch, runtime-store rollback/control-generation reuse, cancellation/compensation, RLM recursion depth and hierarchical budgets, malicious tool output and Prime-Agent-optional mapping.
- [ ] Run continuity/uniqueness checks.
- [ ] Prove expected RED because TASK-059 production contracts are absent.

## Phase 2 — normative runtime-control contract

- [ ] Add TASK-059 amendment.
- [ ] Project exact normative subset into Core Governance.
- [ ] Add SKILL guidance for durable runtime state, Effect Gateway, ambiguity reconciliation, continuation limits and RLM execution.
- [ ] Preserve Framework 1.20 State Binding / Ownership / Operational Transition / Result Acceptance / Verification Validity as authoritative.
- [ ] Explicitly state runtime lease/heartbeat/fence are subordinate liveness/effect-control projections and never replace Ownership Grant or AUTH.

## Phase 3 — Project-Execution contract starters

- [ ] Add or extend single-responsibility starter for Runtime Contract.
- [ ] Add Runtime Event Journal contract.
- [ ] Add Execution Checkpoint contract.
- [ ] Add Effect Policy / Effect Permit contract.
- [ ] Add provider-neutral RLM/recursive Executor Profile contract.
- [ ] Update Project-Execution README composition.
- [ ] Do not create executable supervisor, queue, database or Gateway code.

## Phase 4 — release propagation

- [ ] Re-evaluate semantic version from the fresh 1.20 baseline; expected candidate is Framework `1.21.0`, Schema `1.0.0`, release format `3`.
- [ ] Update release descriptor, migration notes, README and maintained starter stamps as applicable.
- [ ] Preserve all historical TASK-058 artifacts unchanged.
- [ ] Verify launchers/Registered Commands remain unchanged unless a proven contract dependency requires otherwise.

## Phase 5 — AI-ControlTower runtime handoff package

- [ ] Produce a non-executable handoff section/artifact that defines Python Supervisor conformance inputs/outputs.
- [ ] Map expected consumers to AI-ControlTower Package C/D/E without changing their canonical history.
- [ ] Define optional Prime Agent mapping to the RLM Executor Profile.
- [ ] State that actual Python 3.14 runtime implementation is a separate AI-ControlTower Task.
- [ ] Define the evidence needed before canonical-source cutover can start.

## Phase 6 — AFFECTED + independent review

- [ ] Run cumulative AFFECTED verification.
- [ ] Independent fresh-context review must check authority leakage, duplicate Wave A semantics, unsafe retry, permit replay, stale worker effects, secret persistence, model-forged runtime events, RLM budget creation, Prime Agent hard dependency and AI-ControlTower runtime leakage.
- [ ] Resolve all Critical/Important findings and rerun AFFECTED.

## Phase 7 — frozen candidate and RELEASE_FULL

- [ ] Freeze exact candidate commit/tree/Framework-Source tree.
- [ ] Rerun AFFECTED on exact frozen candidate.
- [ ] Run exactly one final RELEASE_FULL on the unchanged candidate.
- [ ] Write state-bound release evidence.
- [ ] Commit terminal TASK-059 lifecycle state only after all completion facts are observed.

## Phase 8 — publication and self-host boundary

- [ ] Stop before push/PR/merge/tag/Release unless separately authorized.
- [ ] After canonical merge, perform governed self-host reconciliation to the final Framework baseline if applicable.
- [ ] Mark standalone feature-development freeze only after canonical readback.

## Post-TASK-059 sequence

1. AI-ControlTower separate implementation Task: Python Supervisor reference runtime + RLM/recursive Executor adapter + Effect Gateway integration as applicable.
2. Verify AI-ControlTower runtime against TASK-059 conformance.
3. Separate Canonical Source Cutover Task.
4. Promote `AI-ControlTower/projectframework/` as the sole canonical development source.
5. Convert standalone ProjectFramework repository to read-only mirror/archive.
