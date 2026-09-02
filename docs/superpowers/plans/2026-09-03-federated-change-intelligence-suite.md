# Federated Change Intelligence Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver Framework 1.14.0 with a bounded rebuildable Project Change Feed, evidence-based cross-Project relation reconciliation, advisory impact analysis, and vendor-neutral notification governance in dependency order without runtime automation or new Project Source authority families.

**Architecture:** TASK-036 and TASK-030 are parallel foundations. TASK-036 provides non-authoritative incremental change routing; TASK-030 establishes evidence-based relation reconciliation under existing `REL-*` semantics. TASK-029 consumes changed subjects plus authoritative/reconciled relation/dependency evidence, then TASK-031 defines notification eligibility/routing/ack/escalation semantics over authoritative source events. The suite is stacked on locally verified Framework 1.13.0 completion and uses one cumulative 1.14.0 release/candidate.

**Tech Stack:** Markdown, YAML, Git, Python scratch verification scripts; no watcher, crawler, webhook, graph-sync, notification delivery, scheduler, CLI, daemon, or other runtime implementation.

**Spec:** `docs/superpowers/specs/2026-09-03-federated-change-intelligence-suite-design.md`

## Global Constraints

- Stacked parent completion: `6c97832c162aecd01b848465f6d53cc433c12cf0` / Framework 1.13.0 / Framework-Source tree `61c27afad2bb794e54561e422b928fc777186585`.
- Current child Goal branch: `task036-030-029-031-federated-intelligence-suite`.
- Target: Framework `1.14.0` / Schema `1.0.0` / release format `3`.
- Dependency order: `TASK-036 + TASK-030 → TASK-029 → TASK-031`.
- TASK-036/TASK-030 may be implemented in either order but both focused completion checkpoints must exist before TASK-029 activation.
- TASK-031 waits for TASK-029 and TASK-030 completion.
- Preserve TASK-022 exact core relation vocabulary and reciprocal-compatible pairs; never infer a universal `DEPENDS_ON ↔ SUPPORTS` inverse.
- `Project-Change-Feed/` is optional, derived, bounded, rebuildable, and outside Project Source authority.
- Impact classification is exactly `DIRECT | POTENTIAL | UNKNOWN`; `NO_MATERIAL_IMPACT_FOUND` is report-only.
- Notification urgency is exactly `ROUTINE | ATTENTION | URGENT` and does not replace Risk/health/lifecycle semantics.
- No new Registered Command; current command registry remains exactly seven commands.
- No new Project Source semantic slot or Stable-ID family for feed/event/impact/notification/reconciliation.
- No automatic reciprocal assertion, cross-Project mutation, issue/risk creation, Knowledge promotion, publication, or external disclosure.
- No watcher/crawler/webhook/daemon/scheduler/event bus/queue/graph-sync/notification-delivery/runtime implementation.
- Thin ChatGPT/Claude launchers remain unchanged unless verification proves a bootstrap requirement; verify parity/size.
- OUT-008/AUTH-008 covers bounded local development only; `commit ≠ push`; publication/merge remain outside authority.
- One final `RELEASE_FULL` per unchanged final candidate.

---

### Task 1: Establish TDD RED — Scenarios 381–420

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`
- Create scratch: `.worktrees/.federated-scratch/federated_structural.py`
- Modify lifecycle: `docs/superpowers/PROJECT-TASKS.md` and active Project Source checkpoint surfaces after RED observation

**Interfaces:**
- Consumes: suite design acceptance criteria, current scenarios `1–380`, current Framework 1.13.0.
- Produces: scenarios `381–420` contiguous/unique and a deterministic structural verifier that is RED before production semantics and GREEN after suite implementation.

- [ ] **Step 1: Append exact scenario range**

Use the design titles/contracts for 381–420, grouped exactly:

```text
381–390 TASK-036 Project Change Feed
391–400 TASK-030 Relation Reconciliation
401–410 TASK-029 Cross-Project Impact Analysis
411–420 TASK-031 Notification Contract
```

Each scenario includes `Prompt`, `Temptation`, `Pass`, `Fail`, `GREEN expectation` in current style.

- [ ] **Step 2: Build structural verifier**

`federated_structural.py` checks at minimum:

```text
scenarios 1–420 contiguous/unique and 381–420 titles present
Framework 1.14.0 release/amendment identity
optional project-change-feed template root and two maintained files
feed derived/non-authority/checkpoint/retention/rebuild semantics
TASK-022 relation vocabulary and reciprocal pairs preserved
no DEPENDS_ON↔SUPPORTS universal inverse
reconciliation endpoint/evidence/counterpart authority rules
impact DIRECT|POTENTIAL|UNKNOWN + advisory/no-mutation boundary
notification ROUTINE|ATTENTION|URGENT + notification≠approval≠authority
no new command/Stable-ID/semantic slot/runtime artifacts
TASK dependency states/checkpoints
22 maintained Project Source starter stamps at 1.14.0 when propagation completes
TASK-042/TASK-043/TASK-028/TASK-032 historical/current preservation
launchers unchanged
ProjectFramework local Project Source pin 1.7.0
full branch git diff hygiene
```

- [ ] **Step 3: Run RED before production semantic edits**

Expected: scenario-range checks and baseline invariants pass; 1.14.0/feed/reconciliation/impact/notification/current-template checks fail because semantics are absent. Record exact PASS/FAIL count and failure names; do not predetermine count.

- [ ] **Step 4: Commit RED contract**

Run `git diff --check origin/main` and commit scenarios + durable RED checkpoint only:

```text
test: define federated change intelligence regression contract
```

---

### Task 2: Implement TASK-036 Project Change Feed Foundation

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260903-federated-change-intelligence.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `README.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Create: `Framework-Source/templates/project-change-feed/README.md`
- Create: `Framework-Source/templates/project-change-feed/feed.md.template`
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Create scratch: `.worktrees/.federated-scratch/task036_focused.py`

**Interfaces:**
- Consumes: 1.13.0 truth/freshness/history/Knowledge/OpenViking contracts.
- Produces: Framework 1.14.0 optional derived `Project-Change-Feed/` contract with projection identity/state, source checkpoint, bounded entries, `since` semantics, rebuildability, and retention.

- [ ] **Step 1: Create cumulative amendment with TASK-036 sections**

Encode exact release identity and feed invariants from spec. Include projection states:

```text
CURRENT | STALE | REBUILD_REQUIRED | UNAVAILABLE
```

and exact change kinds:

```text
STABLE_ID_CHANGE
DOCUMENT_CHANGE
RELATION_CHANGE
LIFECYCLE_CHANGE
EVIDENCE_CHANGE
RELEASE_PUBLICATION_CHANGE
OTHER_MATERIAL_CHANGE
```

No new Project Source Stable-ID family.

- [ ] **Step 2: Create maintained change-feed templates**

`README.md` explains authority, optional adoption, projection metadata/checkpoint/retention/rebuild. `feed.md.template` provides bounded entry schema and explicit non-authority warning. Do not materialize a consuming-Project feed instance in this repository merely because the Framework template exists.

- [ ] **Step 3: Propagate TASK-036 semantics to Core/SKILL/root template/README/migration**

Set current release identity to 1.14.0 and latest amendment. Migration notes start `1.13.0 → 1.14.0 (current)` and preserve Brownfield no-auto-feed behavior.

- [ ] **Step 4: Run TASK-036 focused verifier**

Verify feed root/templates, states/kinds/checkpoint/retention/rebuild/non-authority, no runtime, no command/new Stable-ID, Knowledge/OpenViking boundary, current release routing, full diff hygiene.

- [ ] **Step 5: Commit TASK-036 implementation**

```text
docs: define project change feed contract
```

---

### Task 3: Implement TASK-030 Relation Reconciliation Foundation

**Files:**
- Modify cumulative amendment
- Modify Core/SKILL/root template/README/migration notes
- Modify `Framework-Source/templates/project-source-mockup/92-Project-Graph.template.md` only for current reconciliation guidance; preserve existing relation definitions
- Modify Task source
- Create scratch `task030_focused.py`

**Interfaces:**
- Consumes: TASK-022 `REL-*`, project_uuid authority, exact reciprocal pairs, OpenViking `DERIVED_ONLY`.
- Produces: counterpart discovery/evidence/freshness/corroboration/conflict workflow without cross-Project writes.

- [ ] **Step 1: Extend amendment/Core with reconciliation workflow**

Encode exact reciprocal pairs and explicit non-rule:

```text
PARENT_OF↔CHILD_OF
PEER_OF↔PEER_OF
RELATED_TO↔RELATED_TO
DEPENDS_ON/SUPPORTS: directional; no universal inverse
```

- [ ] **Step 2: Encode CORROBORATED evidence requirements and unavailable/conflict behavior**

Require current local/counterpart REL pointers, matching UUIDs, compatible type/direction, current authoritative source refs, and sufficient freshness. Counterpart unavailable never auto-retires; contradiction uses `CONFLICTED` and existing `CONFLICT-*` when material.

- [ ] **Step 3: Align current Project Graph starter guidance**

Add reconciliation workflow/evidence guidance without creating reciprocal records or changing existing relation vocabulary/state families.

- [ ] **Step 4: Run focused verifier**

Check exact TASK-022 vocabulary/pairs preserved byte/semantic comparison where applicable; no universal directional inverse; no counterpart mutation; no central authority; endpoint/freshness/conflict rules.

- [ ] **Step 5: Commit TASK-030 implementation**

```text
docs: define cross-project relation reconciliation
```

---

### Task 4: Complete Both Foundations and Activate TASK-029

**Files:**
- Modify Task source
- Revise active Project Source `01/03/09/10/13/14/15`

**Interfaces:**
- Consumes: committed TASK-036 and TASK-030 implementations + focused PASS evidence.
- Produces: TASK-036 DONE; TASK-030 DONE; TASK-029 IN_PROGRESS/READY; TASK-031 remains WAITING; OUT-008 remains ACTIVE.

- [ ] Record separate focused EVD/CHG results for each foundation.
- [ ] Transition both foundation Tasks to DONE only after their focused PASS + implementation commits are observed.
- [ ] Set TASK-029 dependency `[TASK-036, TASK-030]` SATISFIED and activate it.
- [ ] Refresh Current State/Handoff exact next action to TASK-029.
- [ ] Validate routing + full branch diff and commit:

```text
docs: complete federated intelligence foundations
```

---

### Task 5: Implement TASK-029 Cross-Project Impact Analysis

**Files:**
- Modify amendment/Core/SKILL/root template/README/migration notes
- Update feed/Project Graph template guidance only where integration requires
- Modify Task source
- Create scratch `task029_focused.py`

**Interfaces:**
- Consumes: TASK-036 changed-subject routing, TASK-030 current relation evidence, existing DEP/REQ/DEC/EVD homes.
- Produces: `DIRECT | POTENTIAL | UNKNOWN` advisory impact contract with provenance/review-required behavior.

- [ ] Encode exact classification semantics.
- [ ] Require changed refs, affected Project UUID/scope, reasoning path, authoritative evidence, limitations, review disposition.
- [ ] Enforce feed/OpenViking routing-only boundary for material DIRECT claims.
- [ ] Preserve canonical payload homes and no target-Project mutation.
- [ ] Cover stale/conflicted/unavailable and merge/split behavior.
- [ ] Run focused verifier and commit:

```text
docs: define cross-project impact analysis
```

---

### Task 6: Complete TASK-029 and Activate TASK-031

**Files:**
- Task source
- Active Project Source checkpoint surfaces

**Interfaces:**
- Consumes: TASK-029 focused PASS + implementation commit.
- Produces: TASK-029 DONE; TASK-031 IN_PROGRESS/READY with TASK-029/TASK-030 dependencies satisfied.

- [ ] Persist TASK-029 focused evidence.
- [ ] Transition dependency state and Handoff.
- [ ] Keep OUT-008 ACTIVE.
- [ ] Verify and commit:

```text
docs: complete task 029 and activate task 031
```

---

### Task 7: Implement TASK-031 Event & Notification Governance

**Files:**
- Modify amendment/Core/SKILL/root template/README/migration notes
- Modify relevant starter guidance only; do not create delivery configuration
- Modify Task source
- Create scratch `task031_focused.py`

**Interfaces:**
- Consumes: TASK-028 Audit events, TASK-029 impacts, TASK-030 relation events, TASK-036 feed routing, existing RISK/DEP/ISS/DRIFT/CONFLICT/Goal/Action ownership.
- Produces: eligibility, urgency, recipient, acknowledgement, escalation, dedup, failure semantics without delivery runtime.

- [ ] Encode candidate event sources and eligibility.
- [ ] Encode exact urgency `ROUTINE | ATTENTION | URGENT` and separation from Risk/health/lifecycle.
- [ ] Encode governed recipient resolution; unresolved recipient = `VERIFICATION_REQUIRED`.
- [ ] Encode acknowledgement ≠ acceptance/authority; escalation ≠ authority/disclosure expansion.
- [ ] Encode source-based dedup and materially changed event behavior.
- [ ] Encode delivery failure/success separation and `PERSISTENCE_PENDING` only when required durable state is unpersisted.
- [ ] Run focused verifier and commit:

```text
docs: define project notification governance
```

---

### Task 8: Propagate Framework 1.14.0 and Run Cumulative AFFECTED

**Files:**
- Modify `Framework-Source/templates/core-document-skeletons.md`
- Modify 22 maintained `Framework-Source/templates/project-source-mockup/*.template.md` stamps to 1.14.0
- Modify mockup README and mockup 00 pointer
- Modify relevant Project Knowledge maintained template guidance if integration is represented there
- Verify unchanged launchers
- Task/Project Source AFFECTED checkpoint
- Create scratch `federated_affected.py`

**Interfaces:**
- Consumes all four focused contracts.
- Produces current maintained distribution alignment and cumulative acceptance evidence.

AFFECTED verifier must include:

```text
all four focused verifiers PASS
structural suite GREEN
scenarios 1–420 contiguous/unique
Framework 1.14.0 / Schema 1.0.0 / format 3
exact seven-command registry unchanged from 1.13.0
project-change-feed template count/content
TASK-022 vocabulary/reciprocal semantics preserved
TASK-028/032 audit/remediation semantics preserved
impact/notification exact vocabularies and boundaries
22/22 starter stamps 1.14.0
Knowledge/Graph current integration pointers aligned
historical amendments unchanged
launchers unchanged/parity/size
no runtime or new Stable-ID/semantic slot
ProjectFramework local Project Source pin 1.7.0
stacked parent ancestry/base recorded
full git diff --check against parent and origin/main
Task lifecycle states preterminal
```

Commit propagation/AFFECTED checkpoint only after exact PASS.

---

### Task 9: Freeze Corrected Final Candidate and Run One RELEASE_FULL

- [ ] Ensure worktree clean and full branch diff hygiene PASS.
- [ ] Capture candidate HEAD, tree, Framework-Source tree.
- [ ] Create state-bound scratch RELEASE_FULL verifier pinning all identities.
- [ ] Syntax-check verifier without executing release run.
- [ ] Run final RELEASE_FULL exactly once on unchanged candidate.
- [ ] If candidate defect exists, invalidate → fix → AFFECTED → new candidate → one final run on corrected candidate.

RELEASE_FULL includes all AFFECTED invariants plus candidate identity, clean worktree, stacked-parent ancestry, historical preservation, starter counts, local pin, no forbidden runtime, and preterminal Task/Goal state.

---

### Task 10: Commit Release Evidence Only

Create:

`docs/superpowers/evidence/2026-09-03-federated-change-intelligence-suite-release-full.md`

Record exact:

```text
Framework 1.14.0 / Schema 1.0.0 / format 3
Goal/design/plan/RED/focused/dependency checkpoint commits
AFFECTED result
candidate HEAD/tree/Framework-Source tree
RELEASE_FULL exact result and run count
scenarios 1–420
22/22 starter stamps
seven-command registry unchanged
TASK-022/TASK-028/TASK-032 preservation
no runtime/new ID/semantic slot
local Project Source pin 1.7.0
stacked parent identity
publication NOT_PUSHED
commit ≠ push
```

Stage/commit evidence file only and confirm Framework-Source tree unchanged.

---

### Task 11: Terminalize Suite Goal

**Files:**
- Task source
- Active Project Source `01/03/09/10/12/13/14/15/91`

Set:

```text
TASK-036 DONE
TASK-030 DONE
TASK-029 DONE
TASK-031 DONE
ACT-020 DONE
OUT-008 ACHIEVED
AUTH-008 TERMINATED
ENV-008 EXPIRED
Execution State READY
Publication NOT_PUSHED
Exact Next Action ไม่มีขั้นตอนถัดไป
Chat Continuity START_NEW_CHAT
```

Add final EVD/CHG with release result/evidence/candidate/completion-commit observation requirement. Commit:

```text
docs: complete federated change intelligence suite lifecycle
```

Fresh post-commit verification must observe exact completion commit, clean worktree, terminal Task/Goal states, Framework-Source tree equal candidate tree, full branch diff hygiene, local pin unchanged, and no remote publication before any DONE claim.
