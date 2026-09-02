# TASK-042 Response Finalization Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Harden ProjectFramework so every Project-governed response bootstraps local governance before the first Project response and cannot bypass the mandatory response-close on normal or exceptional finalization paths.

**Architecture:** Keep the Framework documentation/governance-only. First, encode the regression as new pressure scenarios and a structural verifier that fails against Framework 1.9.0. Then minimally change the thin bootstrap wording, Core/SKILL/amendment/release identity, and maintained bootstrap/README/migration surfaces to make first-response bootstrap and unskippable pre-emit finalization explicit. Freeze one verified 1.9.1 candidate, run AFFECTED and one final RELEASE_FULL, commit state-bound evidence, then reconcile Project Source/Goal locally.

**Tech Stack:** Markdown, YAML, Git, Python scratch verification scripts only; no product/runtime code.

**Spec:** `docs/superpowers/specs/2026-09-01-task042-response-finalization-hardening-design.md`

## Global Constraints

- Target Framework `1.9.1` / Schema `1.0.0` / release format `3`.
- Documentation/governance implementation only; no runtime interceptor, transport hook, parser, CLI, validator service, MCP daemon change, scheduler, watcher, or UI automation.
- Preserve the exact canonical response-close headings/fields/order/lifecycle tokens.
- Do not duplicate the full response-close block into thin vendor launchers.
- First-response bootstrap grants no mutation/Root/Binding/push/disclosure/secret authority.
- Read-only/status/diagnostic/failure-report responses are not exempt from first-response bootstrap.
- No early-return/tool failure/timeout/connector error/refusal/partial-result/exception-recovery path may bypass Response Close Completeness Gate.
- Existing initialized Projects remain pinned; ProjectFramework local Project Source pin remains Framework `1.7.0` / Schema `1.0.0`.
- Historical amendments/specs/plans/evidence remain historical unless a current-surface pointer must change.
- Push/publication is not authorized by `AUTH-003`.
- Use TDD: scenarios/verifier first, observe RED, then production documentation changes.
- One final `RELEASE_FULL` only on the unchanged candidate; bind evidence to candidate HEAD/tree/Framework-Source tree.

---

### Task 1: Encode the Exceptional-Path Regression Contract (RED)

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`
- Create scratch only: `.worktrees/.task042-scratch/task042_red_verify.py`

**Interfaces:**
- Consumes: current Framework 1.9.0 thin launcher/Core/bootstrap semantics.
- Produces: scenarios `269–280` plus structural expectations used by Tasks 2–4.

- [ ] **Step 1: Append scenarios 269–280 before production changes**

Add these scenario themes with Prompt / Temptation / Pass / Fail / GREEN expectation:

```text
269 first Project-governed read-only response bootstraps before answer
270 [Project Status] is not exempt from first-response bootstrap
271 MCP/tool diagnostic response is not exempt
272 tool exception still emits mandatory response close
273 connector unavailable/disconnected still emits close
274 timeout still emits close
275 partial-result response still emits close
276 refusal/blocked-action response still emits close
277 PERSISTENCE_PENDING uses CONTINUE_CURRENT_CHAT + concrete recovery + close
278 bootstrap unresolved/repair response never fabricates path/authority and still closes when governed contract is available
279 early-return/exception-recovery path cannot bypass pre-emit gate
280 thin launchers remain thin; no full response-close duplication
```

- [ ] **Step 2: Write `task042_red_verify.py`**

The verifier must assert at least:

```python
assert framework_version == "1.9.1"
assert latest_amendment.endswith("task042.md")
assert scenarios == list(range(1, 281))
assert "before the first Project-governed response" in chatgpt_launcher
assert "before the first Project-governed response" in claude_launcher
assert "Read-only, status, diagnostic" in launchers_or_normative_surface
assert "No early-return" in core
assert "tool/MCP failure" in core_or_amendment
assert "timeout" in core_or_amendment
assert "partial" in core_or_amendment
assert "refusal" in core_or_amendment
assert "exception-recovery" in core_or_amendment
assert "PERSISTENCE_PENDING" in core
assert full_response_close_block_not_duplicated_in_thin_launchers
```

- [ ] **Step 3: Run RED verifier**

Run:

```text
python E:\GitHub\ProjectFramework\.worktrees\.task042-scratch\task042_red_verify.py
```

Expected: `FAIL` because current 1.9.0 launchers still say `before Material Project work`, release identity is 1.9.0, and exceptional-path hardening text is absent.

- [ ] **Step 4: Verify scenario numbering and diff hygiene**

Run a scratch check that scenarios are contiguous/unique `1–280` and `git diff --check` passes.

- [ ] **Step 5: Commit RED contract**

```text
git add Framework-Source/tests/pressure-scenarios.md
git commit -m "test: define response finalization hardening scenarios"
```

---

### Task 2: Implement Normative First-Response and Unskippable Finalization Rules

**Files:**
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Create: `Framework-Source/references/framework-governance-amendment-260901-task042.md`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`
- Modify: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md`
- Modify: `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md`

**Interfaces:**
- Consumes: Task 1 RED expectations and TASK-042 spec.
- Produces: canonical Framework 1.9.1 semantics and thin launcher wording for Task 3 propagation.

- [ ] **Step 1: Bump release descriptor**

Set exactly:

```yaml
framework_version: "1.9.1"
schema_version: "1.0.0"
latest_framework_amendment: "references/framework-governance-amendment-260901-task042.md"
```

Do not change release format or bootstrap entrypoints.

- [ ] **Step 2: Add TASK-042 amendment**

Normative amendment must state:

```text
First Project Response Bootstrap Invariant
- resolve Project Bootstrap before first Project-governed response in each chat/session when available
- read-only/status/diagnostic/failure-report responses are not exempt
- Material work still applies independent mutation gates

Unskippable Response Finalization Invariant
- every Project-governed final response runs Response Close Completeness Gate immediately before emit
- no early-return, tool/MCP failure, connector unavailable, timeout, partial result, refusal/blocked action, persistence failure, exception recovery, or bootstrap repair path may bypass it
- response-close format/lifecycle vocabulary unchanged
```

- [ ] **Step 3: Strengthen Core Governance**

Update bootstrap/finalization sections so the first-response trigger and no-bypass control-flow invariant are explicit. Keep existing close block byte/semantic meaning unchanged.

- [ ] **Step 4: Update SKILL workflow**

Add first-response bootstrap before Project-governed response generation and explicit final pre-emit gate coverage for exceptional paths.

- [ ] **Step 5: Update ChatGPT/Claude thin launchers identically in semantics**

Target body:

```text
ProjectFramework Bootstrap Rule:
Read Project Bootstrap before the first Project-governed response in each chat.
Read-only, status, diagnostic, and failure-report responses are not exempt.
Before Material Project work, also apply all existing binding, authority, risk, and mutation gates.
If Project Bootstrap cannot be resolved, use the Project README managed bootstrap block as fallback.
ProjectFramework Upstream is for Framework discovery/upgrade only; it never replaces local Project Source authority.
```

Do not paste the full response-close block into launchers.

- [ ] **Step 6: Run Task-2 focused verifier**

Expected: release/amendment/Core/SKILL/launchers pass; Task 3 propagation checks may still fail.

- [ ] **Step 7: Commit normative implementation**

```text
git add Framework-Source/FRAMEWORK-RELEASE.yaml Framework-Source/references/framework-governance-amendment-260901-task042.md Framework-Source/references/core-governance-rules.md Framework-Source/SKILL.md Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md
git commit -m "docs: harden response bootstrap and finalization"
```

---

### Task 3: Propagate Current Bootstrap/README/Starter/Migration Semantics

**Files:**
- Modify: `README.md`
- Modify: `Framework-Source/templates/PROJECT-BOOTSTRAP.md`
- Modify: `Framework-Source/templates/project-location-bootstrap.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: `Framework-Source/templates/project-source-mockup/README.md`
- Modify maintained mockup template Framework-version stamps from 1.9.0 → 1.9.1
- Modify: `Framework-Source/MIGRATION-NOTES.md`

**Interfaces:**
- Consumes: Task 2 canonical wording.
- Produces: aligned current distribution/starter/Brownfield guidance for verification.

- [ ] **Step 1: Update upstream README and managed bootstrap explanation**

Replace Material-only bootstrap wording with first-response semantics where the text is current. Preserve exact mandatory response-close block already present.

- [ ] **Step 2: Update root bootstrap and location-bootstrap templates**

State that Project Settings/README should resolve the root bootstrap before the first Project-governed response, while Material work keeps additional mutation gates.

- [ ] **Step 3: Update Framework/root/skeleton/mockup current guidance**

Propagate first-response/non-exemption semantics without making status/diagnostic responses Material mutations.

- [ ] **Step 4: Bump maintained starter version stamps**

All maintained current starter templates that declare Framework version must say `1.9.1`; Schema remains `1.0.0`.

- [ ] **Step 5: Add `1.9.0 → 1.9.1` migration notes**

Include current affected surfaces, no-auto-upgrade rule, no response-format change, no runtime component, and direct-to-latest compatibility.

- [ ] **Step 6: Run Task-3 verifier**

Verify current current-surface wording, starter stamps, no historical rewrite, and no runtime artifacts.

- [ ] **Step 7: Commit propagation**

```text
git add README.md Framework-Source/templates Framework-Source/MIGRATION-NOTES.md
git commit -m "docs: propagate first response bootstrap hardening"
```

---

### Task 4: Green Contract, Comprehensive AFFECTED Verification, and Candidate Freeze

**Files:**
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Scratch verification only under `.worktrees/.task042-scratch/`

**Interfaces:**
- Consumes: Tasks 1–3 complete Framework surfaces.
- Produces: exact candidate commit/tree identities and AFFECTED evidence inputs.

- [ ] **Step 1: Run original RED verifier as GREEN**

Expected: all TASK-042 structural checks pass.

- [ ] **Step 2: Run comprehensive AFFECTED verifier**

Cover at least:

```text
release 1.9.1/schema/format/latest amendment
scenario 1–280 contiguous + TASK-042 scenario semantics
thin launcher semantic equivalence and size
no full close duplication in launchers
exact close block unchanged in Core/README
first-response bootstrap across current surfaces
non-exemption wording
unskippable exceptional paths
PERSISTENCE_PENDING lifecycle coupling
Project Bootstrap/README authority separation
Brownfield no-auto-upgrade
24 maintained starter stamps at 1.9.1/1.0.0
no executable/runtime/CI/CLI/validator artifacts
historical TASK-041 evidence/amendment preserved
ProjectFramework local Project Source pin 1.7.0/1.0.0
git diff --check
```

- [ ] **Step 3: Update TASK-042 execution metadata**

Record Task 1 RED result, implementation commits, GREEN result, AFFECTED result, and candidate-next state; keep `Publication State: NOT_PUSHED`.

- [ ] **Step 4: Re-run AFFECTED after metadata update**

Must remain PASS.

- [ ] **Step 5: Commit final implementation candidate**

```text
git add docs/superpowers/PROJECT-TASKS.md Framework-Source README.md
git commit -m "docs: complete response finalization hardening implementation"
```

- [ ] **Step 6: Freeze candidate identities**

Capture:

```text
Candidate HEAD
Candidate tree
Framework-Source tree
working tree clean
```

No Framework/current-contract mutation after freeze until final RELEASE_FULL finishes.

---

### Task 5: Final RELEASE_FULL, Evidence, and Terminal Goal Reconciliation

**Files:**
- Create: `docs/superpowers/evidence/2026-09-01-task-042-response-finalization-hardening-release-full.md`
- Modify governed Project Source 01/03/09/10/12/13/14/15/91 via revision/promotion/archive
- Modify: `PROJECT-BOOTSTRAP.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`

**Interfaces:**
- Consumes: frozen Task-4 candidate.
- Produces: state-bound release evidence and local terminal Task/Goal truth.

- [ ] **Step 1: Run exactly one final RELEASE_FULL on frozen candidate**

Bind verifier to exact candidate HEAD/tree/Framework-Source tree and include AFFECTED reuse. Expected PASS with no candidate mutation.

- [ ] **Step 2: Write and commit release evidence**

Evidence records RED→GREEN, AFFECTED, RELEASE_FULL, scenarios 1–280, launcher lengths, maintained starter stamp count, exact candidate/tree identities, and `Publication: NOT_PUSHED`.

- [ ] **Step 3: Prepare terminal Project Source revisions**

Set:

```text
TASK-042 DONE
ACT-012 DONE
OUT-003 ACHIEVED
AUTH-003 TERMINATED
ENV-003 EXPIRED
Execution State READY
Publication NOT_PUSHED
Exact Next Action ไม่มีขั้นตอนถัดไป
Chat START_NEW_CHAT
```

Do not alter local Project Source Framework pin `1.7.0`.

- [ ] **Step 4: Validate terminal drafts and promote**

Verify Index/Manifest/bootstrap routing, Stable-ID resolution, Goal terminal semantics, candidate/evidence pointers, no Framework-Source drift after candidate, and `git diff --check`.

- [ ] **Step 5: Commit terminal lifecycle reconciliation**

```text
git add PROJECT-BOOTSTRAP.md Project-Source docs/superpowers/PROJECT-TASKS.md
git commit -m "docs: complete task 042 lifecycle"
```

- [ ] **Step 6: Fresh final verification before completion claim**

Verify observed completion commit, parent evidence/candidate chain, Framework-Source tree remains evidence-bound, working tree clean, TASK-042/OUT/AUTH/ACT/ENV terminal states, and remote publication not performed.

- [ ] **Step 7: Finish branch without publication**

Because `[Goal]` excludes push/publication, keep the verified branch/worktree intact and report `NOT_PUSHED`; do not create PR or merge without later explicit publication intent.
