# TASK-043 Registered Command Strict-Interface Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement Framework `1.12.2` so every recognized Registered Command is a Strict Governed Interface whose command body passes a Command Contract Completeness Gate before TASK-042's existing Response Close Completeness Gate, while repairing verified Core/SKILL `[Project Status]` `Continuity` drift.

**Architecture:** Keep ProjectFramework documentation/governance-only. Encode six regression scenarios first, prove the Framework `1.12.1` baseline fails the new command-contract verifier, then minimally update Core/SKILL/current root template plus one additive TASK-043 amendment/release/migration routing. Freeze one candidate after AFFECTED verification, run exactly one final `RELEASE_FULL` on that unchanged candidate, commit evidence, then terminally reconcile TASK-043 Goal/Project Source.

**Tech Stack:** Markdown/YAML governance sources; Python/PowerShell structural verification in ignored `.worktrees/.task043-scratch`; Git.

**Spec:** `docs/superpowers/specs/2026-09-02-task043-registered-command-strict-interface-design.md`

## Global Constraints

- Target is Framework `1.12.2` / Schema `1.0.0` / release format `3`.
- No new Registered Command, semantic slot, Stable-ID family, lifecycle state, authority family, parser/runtime/middleware/interceptor/validator/CLI/tool implementation.
- Preserve TASK-042 Response Close Completeness Gate unchanged as the final global pre-emit gate.
- Command Contract Completeness Gate runs only for recognized Registered Commands and precedes TASK-042's global close gate.
- Strict interface governs required structure/order/tokens/freshness/fail-closed representation; non-governed explanatory prose remains flexible.
- Baseline verified drift: Core `[Project Status]` includes `Continuity`; SKILL current main command text and quick reference omit it.
- Historical amendments/specs/plans/evidence are immutable historical provenance; edit current surfaces only.
- ProjectFramework local Project Source pin remains `1.7.0` / Schema `1.0.0`.
- Push/publication is outside `AUTH-005`; `commit ≠ push`.

---

### Task 1: Encode TASK-043 TDD RED Contract

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`
- Create outside repository tracking: `.worktrees/.task043-scratch/task043_verify.py`
- Modify checkpoint metadata: `docs/superpowers/PROJECT-TASKS.md`, active Project Source lifecycle files

**Interfaces:**
- Consumes: Framework `1.12.1` baseline; scenarios currently end at `350`.
- Produces: scenarios `351–356`; structural verifier whose failures name missing Strict-Interface/gate/alignment requirements.

- [ ] **Step 1: Append scenarios 351–356 before any production Framework semantic change**

Add exactly the six scenarios specified by the design: correct-information/wrong-protocol, narrative replacement, missing fresh observation preserves dimension, style cannot weaken structure, command gate precedes close gate, Core/SKILL alignment.

- [ ] **Step 2: Write the structural verifier**

The verifier must check at least:

```python
checks = {
    "scenario_range": scenarios_351_356_exist_and_numbering_is_contiguous,
    "strict_interface_core": core_has_registered_command_strict_interface_rule,
    "command_gate_core": core_has_command_contract_completeness_gate,
    "command_gate_skill": skill_has_command_contract_completeness_gate,
    "gate_order": command_gate_precedes_response_close_gate,
    "status_core_continuity": core_status_sequence_ends_in_continuity,
    "status_skill_continuity": skill_status_sequence_ends_in_continuity,
    "skill_quick_ref_continuity": skill_quick_reference_includes_continuity,
    "no_new_command": command_registry_is_unchanged,
    "task042_preserved": response_close_gate_text_still_exists,
}
```

- [ ] **Step 3: Run verifier and prove RED**

Run:

```text
python E:\GitHub\ProjectFramework\.worktrees\.task043-scratch\task043_verify.py
```

Expected: non-zero exit with scenarios present but failures for missing Strict-Interface/gate and SKILL `Continuity`; no script/runtime error.

- [ ] **Step 4: Run `git diff --check`**

Expected: exit `0`.

- [ ] **Step 5: Commit RED contract**

```text
git add Framework-Source/tests/pressure-scenarios.md docs/superpowers/PROJECT-TASKS.md Project-Source

git commit -m "test: define task 043 command compliance scenarios"
```

Record RED counts/commit in Project Source evidence/checkpoint.

---

### Task 2: Implement Normative Strict-Interface and Command Gate

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260902-task043.md`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/MIGRATION-NOTES.md`

**Interfaces:**
- Consumes: scenarios/verifier from Task 1; TASK-042 amendment semantics.
- Produces: normative Strict-Interface contract; Command Contract Completeness Gate; operational SKILL pipeline; 1.12.2 release routing.

- [ ] **Step 1: Add TASK-043 amendment**

The amendment must define:

```text
Registered Command = Strict Governed Interface
semantic equivalence alone != command compliance
missing evidence != permission to omit required structure
Command Contract Completeness Gate -> Response Close Completeness Gate -> Emit
```

It must explicitly preserve TASK-042 and the no-runtime boundary.

- [ ] **Step 2: Update Core Governance**

Immediately inside/adjacent to `16.4 Registered Project Command Contract`, add the normative strict-interface rule and command-body gate. Preserve command registry identities.

- [ ] **Step 3: Update SKILL operational flow and repair drift**

Add semantically exact pipeline:

```text
Recognize
→ Resolve Contract
→ Fresh Observe
→ Materialize Governed Structure
→ Populate
→ Command Contract Completeness Gate
→ Response Close Completeness Gate
→ Emit
```

Change both current `[Project Status]` summaries to include `Continuity` after `Blockers`.

- [ ] **Step 4: Update release descriptor and migration notes**

Set `framework_version: "1.12.2"`; point `latest_framework_amendment` to TASK-043; add a bounded `1.12.1 → 1.12.2` migration section explaining command-body semantics, Core/SKILL alignment, Brownfield pin preservation, and no runtime requirement.

- [ ] **Step 5: Run Task 1 verifier**

Expected: core/skill/gate/status checks now pass; template/release propagation checks may remain for Task 3 only if the verifier separates them.

- [ ] **Step 6: Commit normative implementation**

```text
git add Framework-Source/references Framework-Source/SKILL.md Framework-Source/FRAMEWORK-RELEASE.yaml Framework-Source/MIGRATION-NOTES.md

git commit -m "docs: harden registered command interface semantics"
```

---

### Task 3: Propagate Current Root Template and Release Identity

**Files:**
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify if it duplicates current command contract: `Framework-Source/templates/project-source-mockup/00-Project-Source-Framework.template.md`
- Modify current Framework version stamps in maintained starter/template files required by repository release consistency
- Modify `README.md` only for current public release identity and a concise strict-interface clarification if needed; do not duplicate the full algorithm

**Interfaces:**
- Consumes: normative Core/SKILL contract from Task 2.
- Produces: GREENFIELD/current starter consistency at Framework 1.12.2.

- [ ] **Step 1: Align the canonical 00 template**

Add the strict-interface/command-gate rule near Registered Project Commands and update `[Project Status]` sequence to include `Continuity`.

- [ ] **Step 2: Align maintained duplicate root/mockup surfaces only where current contract is duplicated**

Do not edit historical provenance files.

- [ ] **Step 3: Update current release stamps from 1.12.1 to 1.12.2 where the repository's maintained starter contract requires a unified current Framework version**

Preserve Schema `1.0.0` and release format `3`.

- [ ] **Step 4: Run verifier and focused propagation checks**

Expected: scenarios `1–356` contiguous/unique; Core/SKILL/template sequences aligned; no command registry growth; current release identity consistent.

- [ ] **Step 5: Commit propagation**

```text
git add Framework-Source/templates README.md Framework-Source

git commit -m "docs: propagate task 043 command contract"
```

---

### Task 4: AFFECTED Verification and Candidate Freeze

**Files:**
- No new production semantics unless a failed check proves a bounded defect.
- Update: `docs/superpowers/PROJECT-TASKS.md`, active Project Source checkpoint/evidence.

**Interfaces:**
- Consumes: Tasks 1–3 implementation.
- Produces: AFFECTED PASS and one frozen candidate commit for final release verification.

- [ ] **Step 1: Run Task 1 structural verifier**

Expected: all TASK-043 structural checks PASS.

- [ ] **Step 2: Run affected assertions**

Verify:

```text
scenarios 1–356 contiguous/unique
six TASK-043 scenarios present
Core Strict-Interface + command gate present
SKILL operational flow present
Core/SKILL status sequence includes Continuity
TASK-042 Response Close semantics preserved
command registry unchanged
release descriptor = 1.12.2 / schema 1.0.0 / format 3
latest amendment points TASK-043
migration notes include 1.12.1→1.12.2
current maintained starter stamps consistent
ProjectFramework local Project Source pin still 1.7.0
no runtime/CLI/parser/interceptor/middleware artifacts added
git diff --check PASS
```

- [ ] **Step 3: Fix only bounded verified failures and rerun affected checks**

Do not broaden scope.

- [ ] **Step 4: Update checkpoint metadata and commit the final candidate**

```text
git add Framework-Source README.md docs/superpowers/PROJECT-TASKS.md Project-Source

git commit -m "docs: prepare task 043 release candidate"
```

Capture candidate commit/tree and `Framework-Source` tree. No production edit is allowed after this candidate if its final release evidence is to be reused.

---

### Task 5: Final RELEASE_FULL, Evidence, and Terminal Reconciliation

**Files:**
- Create: `docs/superpowers/evidence/2026-09-02-task-043-registered-command-strict-interface-release-full.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Revise active Project Source: `01`, `03`, `09`, `10`, `12`, `13`, `14`, `15`, `91`; archive superseded revisions

**Interfaces:**
- Consumes: unchanged frozen candidate from Task 4.
- Produces: one final state-bound `RELEASE_FULL`, committed evidence, `TASK-043 DONE`, `OUT-005 ACHIEVED`, `AUTH-005 TERMINATED`, `ACT-016 DONE`, `ENV-005 EXPIRED`.

- [ ] **Step 1: Run exactly one final RELEASE_FULL on the unchanged candidate**

The release verifier must include the TASK-043 AFFECTED contract plus repository-wide invariants relevant to Framework release acceptance: current release descriptor routing, scenario numbering, maintained current templates/stamps, launcher parity/size if unchanged, historical immutability sentinels where available, Project Source local pin, no runtime expansion, and `git diff --check`.

Expected: PASS with candidate/tree identities recorded.

- [ ] **Step 2: Write release evidence without changing the verified Framework candidate tree**

The evidence records target, candidate commit/tree, Framework-Source tree, RED→GREEN result, AFFECTED result, RELEASE_FULL result, scenario range, command-gate ordering, Continuity alignment, no-runtime/no-new-command boundaries, and publication `NOT_PUSHED`.

- [ ] **Step 3: Commit release evidence**

```text
git add docs/superpowers/evidence/2026-09-02-task-043-registered-command-strict-interface-release-full.md

git commit -m "docs: record task 043 release evidence"
```

The Framework candidate tree must remain identical to the verified candidate tree.

- [ ] **Step 4: Terminally reconcile Task/Goal/Project Source**

Set:

```text
TASK-043: DONE
ACT-016: DONE
OUT-005: ACHIEVED
AUTH-005: TERMINATED
ENV-005: EXPIRED
publication: NOT_PUSHED
exact next action: ไม่มีขั้นตอนถัดไป
```

Persist release evidence pointer and candidate identities; update `03/09` Resume Block and active routing/Manifest.

- [ ] **Step 5: Commit terminal reconciliation**

```text
git add docs/superpowers/PROJECT-TASKS.md Project-Source

git commit -m "docs: complete task 043 lifecycle"
```

- [ ] **Step 6: Post-commit completion verification**

Freshly verify:

```text
working tree clean
TASK-043 DONE
OUT-005 ACHIEVED / AUTH-005 TERMINATED / ACT-016 DONE / ENV-005 EXPIRED
completion commit observed
Framework-Source tree still equals RELEASE_FULL-verified tree
branch publication remains NOT_PUSHED / ahead of origin/main as applicable
```

Only after this evidence may TASK-043 be reported DONE.
