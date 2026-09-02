# TASK-028 + TASK-032 Integrity & Remediation Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver Framework 1.13.0 with a strict read-only `[Project Audit]` command (TASK-028) followed by a governed repair/remediation workflow (TASK-032), with TASK-028 completed before TASK-032 activation and one cumulative final release verification.

**Architecture:** `[Project Audit]` is a Strict Governed Interface that diagnoses current Project integrity without mutation. TASK-032 is a separate, authority-checked workflow that routes selected findings through existing canonical homes/Risk/AUTH/ACT/CR/MIG/DRIFT/CONFLICT semantics, requires rollback/result verification, and re-audits affected categories. Both Tasks share one Framework 1.13.0 release/amendment and final candidate, but retain separate focused completion checkpoints.

**Tech Stack:** Markdown, YAML, Git, Python scratch verification scripts; no runtime/validator/CLI implementation.

**Spec:** `docs/superpowers/specs/2026-09-02-task028-task032-integrity-remediation-design.md`

## Global Constraints

- Baseline: `origin/main` at suite creation `a5e73faf3d13ed8baad6a259c52e15efc981804f`.
- Target: Framework `1.13.0` / Schema `1.0.0` / release format `3`.
- Dependency order: `TASK-028 → TASK-032`; TASK-032 remains `WAITING` until TASK-028 focused completion is committed and observed.
- `[Project Audit]` exact top-level order: `Scope → Health → Categories → Findings → Unknowns → Evidence → Repair Routes → Continuity`.
- Audit health vocabulary: `GREEN | AMBER | RED | UNKNOWN`.
- Preserve exact invariant: `Audit finds ≠ Audit fixes`.
- No audit finding/remediation Stable-ID family (`AUDIT-*`, `FINDING-*`, `REPAIR-*`, `REM-*`) and no repair command.
- No executable validator/scanner/CLI/audit daemon/repair bot/auto-fix/cross-Project mutation/notification runtime.
- Preserve TASK-042 Response Close Completeness Gate and TASK-043 Strict Governed Interface/Command Contract Completeness Gate unchanged.
- Historical amendments/specs/evidence are immutable; current cumulative amendment may evolve only before final candidate freeze.
- Thin ChatGPT/Claude launcher bodies remain unchanged unless a verified current-surface requirement proves otherwise; always verify parity/size.
- Persistent Goal AUTH-007 covers bounded local work only; `commit ≠ push`; publication remains not authorized.
- One final `RELEASE_FULL` per unchanged final candidate.

---

### Task 1: Establish TDD RED Contract — Scenarios 357–380

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`
- Create scratch only: `.worktrees/.task028032-scratch/task028032_structural.py`
- Modify lifecycle: `docs/superpowers/PROJECT-TASKS.md`, active Project Source checkpoint surfaces after RED is observed

**Interfaces:**
- Consumes: design spec acceptance criteria and current scenarios `1–356`.
- Produces: scenarios `357–380` contiguous/unique plus a deterministic structural verifier that can show expected RED before production semantics and GREEN later.

- [ ] **Step 1: Append the exact suite pressure scenarios**

Add scenarios with these titles/contracts:

```text
357 Project Audit Brackets Required
358 Project Audit Matching Is Case-Insensitive
359 Project Audit Strict Top-Level Order
360 Audit Finds Does Not Fix
361 Audit Cross-Surface 00/01/03/09/14 Consistency
362 Audit Unresolved Stable ID Is Explicit
363 Audit Fresh Git/Binding Evidence Or UNKNOWN
364 Audit Conditional Surfaces Are Applicability-Driven
365 Audit Finding Is Not A Stable ID
366 Audit Reuses Existing Drift/Conflict/Migration Homes
367 Audit Bounded Aggregation Cannot Hide Material Findings
368 Audit Partial Source Failure Preserves Unknowns
369 Style Request Cannot Weaken Project Audit Interface
370 Project Audit Command Gate Precedes Response Close Gate
371 Audit Does Not Materialize Issue Records
372 Repair Requires Explicit Applicable Authority
373 Repair Mutates Only Canonical Owner/Home
374 Repair Preserves Independent R2/R3 Gates
375 Semantic Conflict Is Decision Work, Not Auto-Repair
376 Repair Declares Reversibility Or Limitation
377 Repair Requires Direct Resulting-State Verification
378 Repair Re-Audits Affected Categories
379 ACT DONE Does Not Prove Repair Outcome
380 No Repair Command / Remediation ID Family / Runtime Auto-Fix
```

Each scenario must include `Prompt`, `Temptation`, `Pass`, `Fail`, and `GREEN expectation` in the existing pressure-scenario style.

- [ ] **Step 2: Create scratch structural verifier**

`.worktrees/.task028032-scratch/task028032_structural.py` must check at minimum:

```text
scenario range 1–380 contiguous and unique
scenarios 357–380 present
Framework 1.13.0 identity
latest TASK-028/TASK-032 amendment
[Project Audit] registry in Core/SKILL/root template/README
exact strict dimension order in Core/SKILL/root template
read-only no-auto-fix contract
TASK-043 command gate composition preserved
TASK-032 canonical-home/Risk/AUTH/rollback/re-audit contract
no repair command / no new remediation family / no runtime artifacts
22 starter stamps at 1.13.0 when propagation is complete
TASK-028/TASK-032 lifecycle/dependency state
```

The verifier must clearly print one line per check plus `TASK028032_STRUCTURAL X/Y PASS|FAIL`.

- [ ] **Step 3: Run verifier on the pre-production baseline and record expected RED**

Run:

```powershell
python E:\GitHub\ProjectFramework\.worktrees\.task028032-scratch\task028032_structural.py
```

Expected: scenarios checks pass, but 1.13.0/audit/remediation/current-template checks fail because production semantics are not implemented yet. Record the exact count and failure list; do not guess it in advance.

- [ ] **Step 4: Verify diff hygiene and commit RED contract**

Run:

```powershell
git diff --check
git status --short
```

Commit only pressure scenarios plus Task/Project Source RED checkpoint updates:

```text
test: define integrity remediation regression contract
```

---

### Task 2: Implement TASK-028 `[Project Audit]` Normative Command Contract

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260902-task028-task032.md`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `README.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Create scratch only: `.worktrees/.task028032-scratch/task028_focused.py`

**Interfaces:**
- Consumes: TASK-043 Strict Governed Interface and global response-close gate.
- Produces: registered `[Project Audit]` command with exact structure, category/health semantics, finding/evidence/unknown rules, bounded output, read-only boundary, and repair-route advisory semantics.

- [ ] **Step 1: Create cumulative 1.13.0 amendment with TASK-028 normative sections**

The amendment must declare:

```text
previous Framework: 1.12.2
Framework: 1.13.0
Schema: 1.0.0
compatibility: backward-compatible additive audit/remediation suite
```

TASK-028 sections must encode:

```text
[Project Audit] literal/case-insensitive identity
read-only contract
exact top-level order
GREEN|AMBER|RED|UNKNOWN category health
canonical category ordering
finding-is-presentation rule
freshness/UNKNOWN behavior
bounded aggregation without silent material loss
Repair Routes advisory-only routing
TASK-042/TASK-043 composition
```

Do not add TASK-032 repair semantics yet beyond a clear suite boundary stating they remain non-normative until TASK-028 focused completion.

- [ ] **Step 2: Add `[Project Audit]` to Core/SKILL/root-template/README command registry**

Canonical help entry:

```text
[Project Audit] : fresh read-only integrity/drift audit with evidence, unknowns, and governed repair routes; never auto-fixes Project truth
```

Add the exact required dimension order and read-only semantics in Core, SKILL, and root Framework template. Root README day-to-day command list must include `[Project Audit]` without changing existing command meanings.

- [ ] **Step 3: Set current release identity and migration guidance to 1.13.0**

`FRAMEWORK-RELEASE.yaml`:

```yaml
framework_version: "1.13.0"
latest_framework_amendment: "references/framework-governance-amendment-260902-task028-task032.md"
```

`MIGRATION-NOTES.md` gets current transition:

```text
1.12.2 → 1.13.0 (current)
```

Migration guidance must preserve initialized-Project pinning and explain that `[Project Audit]` adoption is through governed Direct-to-Latest upgrade; no issue/repair objects are auto-created.

- [ ] **Step 4: Run structural verifier and focused TASK-028 verifier**

`task028_focused.py` must verify at least:

```text
[Project Audit] appears exactly once in each current command registry surface
exact dimension order matches spec
read-only/no-mutation text present
health vocabulary present
category order present
finding-not-Stable-ID and existing-home routing present
unknown/freshness and bounded-output rules present
TASK-042/TASK-043 strings preserved
no TASK-032 repair implementation yet beyond suite boundary
no runtime/CLI files added
```

Run:

```powershell
python ...\task028032_structural.py
python ...\task028_focused.py
git diff --check
```

Expected: TASK-028 focused checks GREEN; structural suite still RED only for TASK-032/final propagation checks.

- [ ] **Step 5: Commit TASK-028 implementation**

Commit message:

```text
docs: implement project audit command contract
```

---

### Task 3: Complete TASK-028 Focused Lifecycle and Activate TASK-032

**Files:**
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Revise active Project Source: `01`, `03`, `09`, `10`, `13`, `14`, `15` as required

**Interfaces:**
- Consumes: committed TASK-028 implementation plus focused verification evidence.
- Produces: `TASK-028 DONE`, `TASK-032 readiness READY`, `TASK-032 IN_PROGRESS`, durable evidence/continuation; OUT-007 remains ACTIVE.

- [ ] **Step 1: Record TASK-028 focused evidence**

Add next `EVD-*`/`CHG-*` entries containing exact focused verifier count, implementation commit, Framework 1.13.0 identity, scenario range, and no-runtime/no-auto-fix invariants.

- [ ] **Step 2: Transition Task states in dependency order**

Set:

```text
TASK-028 Status: DONE
TASK-028 readiness: READY (terminal historical metadata may remain)
TASK-032 Status: IN_PROGRESS
TASK-032 readiness: READY
TASK-032 depends_on: [TASK-028] satisfied
```

Do not mark OUT-007 achieved.

- [ ] **Step 3: Refresh Current State/Handoff**

Exact next action becomes TASK-032 remediation implementation. `09` resume block must name TASK-028 completion commit/focused PASS and TASK-032 active state.

- [ ] **Step 4: Verify and commit focused lifecycle checkpoint**

Run:

```powershell
git diff --check
python ...\task028_focused.py
```

Commit:

```text
docs: complete task 028 and activate task 032
```

---

### Task 4: Implement TASK-032 Governed Repair / Remediation Contract

**Files:**
- Modify: `Framework-Source/references/framework-governance-amendment-260902-task028-task032.md`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `README.md`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Create scratch only: `.worktrees/.task028032-scratch/task032_focused.py`

**Interfaces:**
- Consumes: TASK-028 finding/Repair Routes contract and existing Risk/AUTH/CR/ACT/MIG/DRIFT/CONFLICT semantics.
- Produces: non-command remediation workflow with proposal, canonical-owner routing, Risk/AUTH, semantic-conflict boundary, rollback, resulting-state verification, and affected re-audit.

- [ ] **Step 1: Extend cumulative amendment with TASK-032 normative sections**

Add exact remediation proposal fields:

```text
Source finding / evidence
Affected scope
Canonical owner/home
Desired resulting state
Risk class R0–R3
Applicable authority / approval
Prerequisites and freshness checks
Ordered repair actions
Reversibility / rollback
Verification of resulting state
Affected re-audit / resulting-state confirmation
Evidence and lifecycle updates
```

Encode:

```text
finding ≠ repair authority
semantic conflict → Decision/Change/Conflict path
R2/R3 gates remain independent
no new remediation family/command
ACT DONE ≠ repair outcome verified
new findings from re-audit do not self-authorize fixes
```

- [ ] **Step 2: Propagate remediation semantics to Core/SKILL/root template/README/migration notes**

Keep `[Project Audit]` command registry unchanged except its existing repair-route wording. TASK-032 must appear as a workflow, not another command.

- [ ] **Step 3: Run TASK-032 focused verifier**

`task032_focused.py` verifies:

```text
all proposal fields
canonical owner/home routing
R0–R3 and AUTH separation
semantic conflict no-auto-repair
rollback/reversibility
post-repair direct verification
re-audit/result confirmation
ACT DONE separation
no repair command / no remediation ID family
no runtime files
TASK-028 remains DONE and unchanged in command semantics
```

Run:

```powershell
python ...\task032_focused.py
python ...\task028032_structural.py
git diff --check
```

Expected: TASK-032 focused GREEN; remaining structural failures only final starter/release/lifecycle propagation if not yet done.

- [ ] **Step 4: Commit TASK-032 normative implementation**

Commit:

```text
docs: define governed project remediation workflow
```

---

### Task 5: Propagate Framework 1.13.0 and Run Cumulative AFFECTED Verification

**Files:**
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: all 22 maintained files under `Framework-Source/templates/project-source-mockup/*.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/README.md`
- Modify: `Framework-Source/templates/project-source-mockup/00-Project-Source-Framework.template.md` as needed for current command/workflow pointer text
- Verify unchanged: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md`, `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Create scratch only: `.worktrees/.task028032-scratch/task028032_affected.py`

**Interfaces:**
- Consumes: both focused implementations.
- Produces: all current maintained starter/version surfaces aligned to Framework 1.13.0 plus comprehensive AFFECTED evidence.

- [ ] **Step 1: Update current starter release stamps to 1.13.0**

All 22 maintained `.template.md` Project Source starter frontmatter stamps must resolve Framework `1.13.0` / Schema `1.0.0`. Core skeleton/current mockup README release identity must agree.

- [ ] **Step 2: Align mockup/root pointer text**

Current starter guidance must mention `[Project Audit]` where command registry/help is represented and preserve remediation as workflow-only. No active Goal/audit finding/repair record is synthesized in starter content.

- [ ] **Step 3: Build cumulative AFFECTED verifier**

`task028032_affected.py` must verify at least:

```text
structural suite GREEN
TASK-028 focused GREEN
TASK-032 focused GREEN
scenarios 1–380 contiguous/unique
release descriptor 1.13.0 / Schema 1.0.0 / format 3
latest amendment pointer
Core/SKILL/root template exact [Project Audit] registry/order
README current release and command list
migration current transition
22/22 starter stamps
skeleton/mockup current identity
TASK-042 amendment blob unchanged from origin/main
TASK-043 amendment blob unchanged from origin/main
existing six command contracts preserved plus one new [Project Audit] only
launchers unchanged/parity/size
no executable/runtime artifacts
ProjectFramework local Project Source pin remains 1.7.0
only expected roots changed
full git diff --check
TASK-028 DONE; TASK-032 implementation complete/pending cumulative acceptance
```

- [ ] **Step 4: Run cumulative verification**

```powershell
python ...\task028032_affected.py
```

Record the exact `TASK028032_AFFECTED X/X PASS` result; do not guess the count.

- [ ] **Step 5: Commit propagation/cumulative checkpoint**

Commit:

```text
docs: propagate framework 1.13 integrity remediation suite
```

Persist `EVD-* / CHG-*` AFFECTED checkpoint and update exact next action to final candidate freeze.

---

### Task 6: Freeze Final Candidate, Run One RELEASE_FULL, and Commit Evidence

**Files:**
- Modify checkpoint-only: Task/Project Source candidate-preparation state
- Create: `docs/superpowers/evidence/2026-09-02-task-028-task-032-integrity-remediation-release-full.md`
- Create scratch only: `.worktrees/.task028032-scratch/task028032_release_full.py`

**Interfaces:**
- Consumes: cumulative AFFECTED PASS.
- Produces: immutable final Framework 1.13.0 candidate identity, one RELEASE_FULL result, committed release evidence.

- [ ] **Step 1: Commit/freeze final implementation candidate**

Candidate-preparation commit must contain all Framework-Source implementation and current preterminal Project Source state, with a clean worktree afterwards. Capture:

```text
candidate HEAD
candidate tree
Framework-Source tree
```

No Framework-Source change is permitted after this freeze unless the candidate is explicitly invalidated.

- [ ] **Step 2: Create state-bound RELEASE_FULL verifier outside tracked repo**

`task028032_release_full.py` must pin the exact candidate/head/tree/Framework-Source tree and include/reuse cumulative AFFECTED plus final invariants:

```text
clean candidate
AFFECTED PASS
scenarios 1–380
release/amendment identity
exact command registry (7 commands total)
[Project Audit] strict order/read-only boundary
TASK-032 remediation workflow
TASK-042/TASK-043 historical/current semantics preserved
all maintained starters current
launchers parity/size
no forbidden runtime artifacts
historical amendments unchanged
Project Source local pin unchanged
Task states preterminal as expected
git diff --check
```

- [ ] **Step 3: Run RELEASE_FULL exactly once on unchanged candidate**

```powershell
python ...\task028032_release_full.py
```

If the candidate itself is defective, invalidate it, fix, rerun AFFECTED, freeze a new candidate, then run the final RELEASE_FULL on that new candidate. Do not repeatedly rerun an unchanged failed candidate without root-cause classification.

- [ ] **Step 4: Write release evidence with exact results**

Evidence file records:

```text
Framework 1.13.0 / Schema 1.0.0 / format 3
Goal/design/plan/RED/focused commits
TASK-028 focused result
TASK-032 focused result
AFFECTED exact result
candidate/head/tree/Framework-Source tree
RELEASE_FULL exact result
scenarios 1–380
22/22 starter stamps
TASK-042/TASK-043 preservation
no runtime/new ID family/repair command
Project Source pin 1.7.0
publication NOT_PUSHED
commit ≠ push
```

- [ ] **Step 5: Commit release evidence only**

Commit:

```text
docs: record integrity remediation suite release evidence
```

Verify Framework-Source tree still equals the frozen candidate Framework-Source tree.

---

### Task 7: Terminalize TASK-032, Suite Goal, and Project Source

**Files:**
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Revise active Project Source: `01`, `03`, `09`, `10`, `12`, `13`, `14`, `15`, `91`

**Interfaces:**
- Consumes: committed release evidence and frozen-candidate RELEASE_FULL PASS.
- Produces: durable verified local completion with no remaining suite action.

- [ ] **Step 1: Set terminal lifecycle truth**

Set:

```text
TASK-028 DONE
TASK-032 DONE
ACT-019 DONE
OUT-007 ACHIEVED
AUTH-007 TERMINATED
ENV-007 EXPIRED
Execution State READY
Publication NOT_PUSHED
Exact Next Action ไม่มีขั้นตอนถัดไป
Chat Continuity START_NEW_CHAT
```

- [ ] **Step 2: Add final EVD/CHG records**

Record release result, evidence commit, candidate identities, completion basis, publication boundary, and completion-commit observation requirement.

- [ ] **Step 3: Commit terminal reconciliation**

Commit:

```text
docs: complete integrity remediation suite lifecycle
```

- [ ] **Step 4: Fresh post-commit verification before any DONE claim**

Verify from committed HEAD:

```text
working tree clean
TASK-028 DONE
TASK-032 DONE
OUT-007 ACHIEVED
AUTH-007 TERMINATED
ACT-019 DONE
ENV-007 EXPIRED
completion commit observed
Framework-Source tree equals release-evidence candidate tree
branch remains unpushed / publication NOT_PUSHED
03 exact next action none
09 START_NEW_CHAT
```

Only after this fresh observation report suite completion.
