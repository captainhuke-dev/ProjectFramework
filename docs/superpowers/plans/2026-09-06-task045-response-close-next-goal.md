# TASK-045 Response Close + Next Goal Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver ProjectFramework 1.15.0 with a mandatory visible response close of `Next Action → Next Goal → Reason`, preserving internal continuation/read routing and existing persistent-Goal authority rules.

**Architecture:** This is a documentation/governance protocol migration. Pressure scenarios define the desired contract first; normative Core/SKILL/release surfaces then make those scenarios GREEN; user-facing/starter/migration surfaces propagate the same contract; one final unchanged-candidate RELEASE_FULL and Project Source reconciliation close the Goal. No executable Framework runtime is introduced.

**Tech Stack:** Markdown, YAML, Git, ripgrep, Python scratch verification via `uv run python`; no application/runtime dependency.

**Spec:** `docs/superpowers/specs/2026-09-06-task045-response-close-next-goal-design.md`

## Global Constraints

- Target Framework exactly `1.15.0`; Schema remains `1.0.0`; release format remains `3`.
- Existing V2 `TASK-044 ProjectFramework 2.0 / AI-ControlTower Protocol Integration` is preserved and never modified by TASK-045.
- Current TASK-045 Goal lineage is `OUT-012 / AUTH-012 / ACT-024 / ENV-012`.
- Visible response-close fields are exactly `[Next Action] → [Next Goal] → [Reason]` after the two mandatory headings; nothing follows `[Reason]`.
- `[Chat]` and `[Required Read]` are removed only from the mandatory visible response close; internal Handoff/continuity/read-routing semantics remain available.
- `[Next Goal]` is presentation-only and never creates `OUT-*`, `AUTH-*`, `ACT-*`, or `ENV-*` until the Human explicitly invokes `[Goal]`.
- A non-`ไม่มี` `[Next Goal]` starts with literal `[Goal]` and is copy-ready; ambiguous, conflicting, redundant, no-next-action, or ungrounded high-risk cases use `ไม่มี`.
- Do not synthesize push/publication, destructive, Root/Binding, external-disclosure, R3, or secret-value opt-ins into `[Next Goal]`.
- Registered command set remains exactly seven commands; TASK-043 Command Contract Completeness Gate still precedes the revised Response Close Completeness Gate.
- TASK-042 unskippable-final-path semantics remain in force.
- Historical amendments/specs/evidence remain provenance and are not globally rewritten.
- `commit ≠ push`; AUTH-012 does not authorize push/publication/merge.
- No parser, middleware, UI hook, validator CLI, bot, scheduler, watcher, daemon, or other runtime implementation.

---

### Task 1: Establish TDD RED contract for response close v2

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`
- Create outside repository: `E:\GitHub\ProjectFramework\.worktrees\.task045-scratch\verify_task045.py`

**Interfaces:**
- Consumes: Framework 1.14 response-close contract currently present in Core/SKILL/README.
- Produces: scenarios `421–432` and a deterministic scratch verifier that fails before production semantics change and later drives GREEN/AFFECTED/RELEASE_FULL checks.

- [ ] **Step 1: Append scenarios 421–432 to the pressure-scenario source before editing production contract files**

Append exact scenario headings/expectations covering:

```text
421 — Response Close v2 exact visible field order
422 — Mandatory visible Chat field removed
423 — Mandatory visible Required Read field removed
424 — Next Goal may suggest a copy-ready new Goal
425 — Next Goal may suggest copy-ready Goal CHANGE
426 — Existing compatible active Goal suppresses redundant Next Goal
427 — No Next Action forces Next Goal ไม่มี
428 — Ambiguous or ungrounded high-risk outcome forces Next Goal ไม่มี
429 — PERSISTENCE_PENDING recovery cannot be bypassed by Next Goal
430 — Handoff retains internal Chat Continuity and Required Read routing
431 — Command Contract Completeness Gate still precedes Response Close gate
432 — Markdown-visible three-field close ends at Reason
```

Each scenario must assert the expected new contract, preserve authority boundaries, and state that no runtime enforcement is created.

- [ ] **Step 2: Create the scratch verifier with explicit current-surface assertions**

Use this structure in `verify_task045.py`:

```python
from pathlib import Path
import re
import sys

ROOT = Path(r"E:\GitHub\ProjectFramework\.worktrees\task-044-response-close-next-goal")
FS = ROOT / "Framework-Source"

def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")

def must(name: str, condition: bool) -> tuple[str, bool]:
    return name, bool(condition)

def run(mode: str) -> int:
    core = read("Framework-Source/references/core-governance-rules.md")
    skill = read("Framework-Source/SKILL.md")
    readme = read("README.md")
    scenarios = read("Framework-Source/tests/pressure-scenarios.md")
    release = read("Framework-Source/FRAMEWORK-RELEASE.yaml")
    migration = read("Framework-Source/MIGRATION-NOTES.md")
    checks = [
        must("scenarios-421-432", all(f"Scenario {n}" in scenarios or f"## {n}" in scenarios for n in range(421, 433))),
        must("core-next-goal", "[Next Goal]" in core),
        must("skill-next-goal", "[Next Goal]" in skill),
        must("readme-next-goal", "[Next Goal]" in readme),
        must("core-new-order", "[Next Action]" in core and "[Next Goal]" in core and "nothing follows `[Reason]`" in core),
        must("core-no-four-field-mandate", "exactly one visible semantic `[Next Action]:`, `[Chat]:`, `[Reason]:`, and `[Required Read]:`" not in core),
        must("skill-no-four-field-mandate", "[Next Action]:`, `[Chat]:`, `[Reason]:`, `[Required Read]:`" not in skill),
        must("release-1.15", 'framework_version: "1.15.0"' in release),
        must("migration-1.15", "1.14.0 → 1.15.0" in migration),
        must("command-gate-order", "Command Contract Completeness Gate" in core and "Response Close Completeness Gate" in core),
        must("goal-authority-boundary", "Suggested [Goal]" in core or "suggest" in core.lower()),
    ]
    passed = sum(ok for _, ok in checks)
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    print(f"TASK045_{mode.upper()} {passed}/{len(checks)} PASS")
    return 0 if passed == len(checks) else 1

if __name__ == "__main__":
    sys.exit(run(sys.argv[1] if len(sys.argv) > 1 else "structural"))
```

If exact scenario heading syntax differs from the `Scenario N`/`## N` probe, adjust only the heading detector to match the existing pressure-scenario format; do not weaken the semantic assertions.

- [ ] **Step 3: Run RED and verify failure is caused by missing TASK-045 production semantics**

Run:

```text
uv run python E:\GitHub\ProjectFramework\.worktrees\.task045-scratch\verify_task045.py red
```

Expected: non-zero exit. Scenario presence may PASS; new Core/SKILL/README/release/migration assertions MUST FAIL because production contract is still Framework 1.14.

- [ ] **Step 4: Verify scenario numbering remains contiguous/unique through 432**

Run a Python scratch check that extracts scenario numbers from `Framework-Source/tests/pressure-scenarios.md`, confirms no duplicate in 1–432, and confirms every integer 1..432 appears exactly once.

Expected: PASS.

- [ ] **Step 5: Commit RED contract**

```text
git add Framework-Source/tests/pressure-scenarios.md
git diff --cached --check
git commit -m "test(task045): define response close v2 pressure scenarios"
```

---

### Task 2: Implement normative Framework 1.15 response-close contract

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260906-task045-response-close-next-goal.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`

**Interfaces:**
- Consumes: TASK-045 spec and RED scenarios.
- Produces: authoritative Framework 1.15 visible close, Next Goal safety rules, revised Response Close Completeness Gate and latest-amendment routing.

- [ ] **Step 1: Write the new amendment as the latest cumulative TASK-045 authority**

The amendment must state:

```text
Framework 1.15.0 / Schema 1.0.0 / release format 3
visible close = two headings + Next Action + Next Goal + Reason
nothing after Reason
Chat/Required Read removed only from mandatory visible close
internal Handoff continuity/read-routing retained
Next Goal = suggestion only, never authority
Goal suggestion rules NG-1..NG-9
TASK-042 unskippable finalization preserved
TASK-043 command gate remains before response gate
no runtime/parser/validator implementation
initialized Projects remain pinned
```

- [ ] **Step 2: Update release descriptor**

Set exactly:

```yaml
framework_version: "1.15.0"
schema_version: "1.0.0"
release_format_version: 3
latest_framework_amendment: "references/framework-governance-amendment-260906-task045-response-close-next-goal.md"
```

Do not change canonical repository/branch or entrypoints.

- [ ] **Step 3: Replace Core Governance §16.3 mandatory visible close and gate**

Core must contain the exact target example:

```text
### ทำอะไรไป?

<concise statement of what was done or determined>

### และถัดไปคืออะไร?

**[Next Action]:** <one exact next action or ไม่มีขั้นตอนถัดไป>

**[Next Goal]:** <one copy-ready [Goal] ... / [Goal] CHANGE ... command or ไม่มี>

**[Reason]:** <concise reason>
```

Then define the revised pre-emit gate and NG rules. Keep `CONTINUE_CURRENT_CHAT | START_NEW_CHAT` only as internal Handoff/continuity vocabulary, not required visible fields.

- [ ] **Step 4: Align SKILL with Core**

Update:

- Response Close Completeness Gate summary;
- full close example;
- close-field explanation;
- anti-pattern references;
- any current operational instructions that still require the old four visible fields;
- Required References so the new amendment is first/current.

Do not rewrite historical amendment references.

- [ ] **Step 5: Run focused structural verifier**

Run:

```text
uv run python E:\GitHub\ProjectFramework\.worktrees\.task045-scratch\verify_task045.py structural
```

Expected after Task 2: Core/SKILL/release checks PASS; README/migration propagation checks may still FAIL and therefore overall structural verifier may remain non-zero until Task 3.

- [ ] **Step 6: Check text hygiene and commit normative implementation**

```text
git diff --check
git add Framework-Source/FRAMEWORK-RELEASE.yaml Framework-Source/references/core-governance-rules.md Framework-Source/SKILL.md Framework-Source/references/framework-governance-amendment-260906-task045-response-close-next-goal.md
git diff --cached --check
git commit -m "feat(framework): add response close next goal contract"
```

---

### Task 3: Propagate Framework 1.15 to README, migration and maintained starters

**Files:**
- Modify: `README.md`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: `Framework-Source/templates/project-source-mockup/README.md`
- Modify: applicable current files under `Framework-Source/templates/project-source-mockup/`
- Inspect, modify only if current contract requires: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md`, `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md`, `Framework-Source/templates/project-location-bootstrap.md`, `Framework-Source/templates/PROJECT-BOOTSTRAP.md`

**Interfaces:**
- Consumes: normative Task 2 contract.
- Produces: user-facing/install/migration/starter state aligned to Framework 1.15 without expanding thin launchers.

- [ ] **Step 1: Update README mandatory response close**

Use exactly the three-field example from Core. Remove lifecycle coupling that depends on mandatory visible `[Chat]`. Explain that continuation/read routing remains in Project state/Handoff and that `[Next Goal]` is a non-authoritative suggestion.

- [ ] **Step 2: Add top migration note `1.14.0 → 1.15.0`**

Include affected surfaces and an explicit checklist:

```text
response close changes four visible fields -> three
Next Goal safe suggestion rules
Chat/Required Read internal semantics preserved
no automatic Goal materialization
historical content preserved
Brownfield remains pinned until governed upgrade
one final RELEASE_FULL
```

- [ ] **Step 3: Update current root/starter guidance**

Ensure maintained current starter/template text that describes mandatory response close uses only `Next Action / Next Goal / Reason`.

Update Framework version stamps from `1.14.0` to `1.15.0` in maintained current Project Source starters where the existing release process expects every current starter to track Framework version. Do not modify historical archived examples/specs/evidence.

- [ ] **Step 4: Preserve thin launchers unless they actually duplicate the response close**

Inspect official ChatGPT/Claude thin launchers. If they contain no old four-field payload, leave their body unchanged except any release-current reference that must change. Confirm launcher size/parity constraints remain satisfied.

- [ ] **Step 5: Run structural GREEN**

```text
uv run python E:\GitHub\ProjectFramework\.worktrees\.task045-scratch\verify_task045.py structural
```

Expected: all checks PASS.

- [ ] **Step 6: Search current distribution for stale mandatory-four-field wording**

Run:

```text
rg -n "\[Next Action\].*\[Chat\].*\[Reason\].*\[Required Read\]|nothing after \[Required Read\]|nothing follows \`\[Required Read\]\`" Framework-Source README.md
```

Review every hit. Historical references inside migration notes/amendment provenance may remain only when explicitly labeled historical; current mandatory wording must not remain.

- [ ] **Step 7: Commit propagation**

```text
git diff --check
git add README.md Framework-Source
git diff --cached --check
git commit -m "docs(framework): propagate response close v2"
```

---

### Task 4: Run cumulative AFFECTED verification and freeze final candidate

**Files:**
- Modify as corrections only: affected TASK-045 Framework current surfaces.
- Update: `docs/superpowers/PROJECT-TASKS.md` with implementation/verification state before candidate freeze.
- Scratch-only: `E:\GitHub\ProjectFramework\.worktrees\.task045-scratch\verify_task045.py`

**Interfaces:**
- Consumes: Tasks 1–3 GREEN state.
- Produces: clean, state-bound final implementation candidate ready for exactly one RELEASE_FULL.

- [ ] **Step 1: Expand scratch verifier to AFFECTED checks**

Add assertions for:

```text
scenario range 1..432 contiguous/unique
Framework version/amendment identity
Core/SKILL exact visible close alignment
no current mandatory visible Chat/Required Read close fields
Next Goal NG safety rules in both normative sources
TASK-042 preserved
TASK-043 gate ordering preserved
seven registered commands unchanged
README/migration/current starters aligned
maintained starter Framework stamps aligned where applicable
thin launcher parity/size valid
no runtime/code artifact introduced by branch
V2 TASK-044 external worktree HEAD/file hashes unchanged from pre-TASK-045 observation
full branch git diff --check origin/main PASS
```

- [ ] **Step 2: Run AFFECTED**

```text
uv run python E:\GitHub\ProjectFramework\.worktrees\.task045-scratch\verify_task045.py affected
```

Expected: PASS all assertions.

- [ ] **Step 3: Fix only bounded findings and rerun AFFECTED until PASS**

Any correction changes the candidate and invalidates earlier candidate identity. Do not run RELEASE_FULL yet.

- [ ] **Step 4: Update Task source to candidate-ready state**

Record implementation commits, RED result, structural GREEN result and AFFECTED result. Keep publication `NOT_PUSHED / NOT_AUTHORIZED`.

- [ ] **Step 5: Commit final candidate and verify clean**

```text
git add -A
git diff --cached --check
git commit -m "chore(task045): freeze framework 1.15 candidate"
git status --short --branch
git rev-parse HEAD
git rev-parse HEAD^{tree}
git rev-parse HEAD:Framework-Source
```

Expected: clean worktree after commit. Record candidate commit/tree/Framework-Source tree for release evidence.

---

### Task 5: Run exactly one RELEASE_FULL and persist release evidence

**Files:**
- Create: `docs/superpowers/evidence/2026-09-06-task-045-response-close-next-goal-release-full.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md` only after release result is known.

**Interfaces:**
- Consumes: frozen unchanged Task 4 candidate.
- Produces: exactly one final RELEASE_FULL result bound to the candidate.

- [ ] **Step 1: Confirm candidate is unchanged before RELEASE_FULL**

```text
git status --short
git rev-parse HEAD
```

Expected: clean and exact frozen candidate SHA.

- [ ] **Step 2: Run RELEASE_FULL exactly once**

Use the scratch verifier in release mode plus full invariants used by previous releases:

```text
uv run python E:\GitHub\ProjectFramework\.worktrees\.task045-scratch\verify_task045.py release_full
git diff --check origin/main...HEAD
```

Release mode must include all AFFECTED checks plus candidate-cleanliness, release identity, current starter integrity, historical-surface preservation checks and no-runtime scope.

Expected: PASS on run 1. Do not rerun an unchanged passing candidate.

If it fails, the candidate is invalidated: correct the issue, rerun AFFECTED, create a new candidate commit, then run RELEASE_FULL once on the new candidate.

- [ ] **Step 3: Write release evidence**

Evidence must record:

```text
TASK-045
Framework 1.15.0 / Schema 1.0.0 / release format 3
candidate commit/tree/Framework-Source tree
RED result
structural GREEN result
AFFECTED result
RELEASE_FULL result and run count
scenario range 1–432
old visible fields removed / new Next Goal contract
TASK-042/TASK-043 preservation
seven-command registry unchanged
V2 TASK-044 preserved
no runtime expansion
publication NOT_AUTHORIZED / NOT_PUSHED
```

- [ ] **Step 4: Commit release evidence**

```text
git add docs/superpowers/evidence/2026-09-06-task-045-response-close-next-goal-release-full.md docs/superpowers/PROJECT-TASKS.md
git diff --cached --check
git commit -m "docs(evidence): record TASK-045 framework 1.15 release"
```

This evidence commit is not the frozen candidate; it points back to the verified candidate and does not require a second RELEASE_FULL.

---

### Task 6: Terminalize Goal and Project Source

**Files:**
- Supersede/archive active current revisions of slots `01,03,09,10,12,13,14,15,91`.
- Create next non-colliding active revisions for those slots.
- Modify: `docs/superpowers/PROJECT-TASKS.md`.

**Interfaces:**
- Consumes: verified release evidence from Task 5.
- Produces: `TASK-045 DONE`, `OUT-012 ACHIEVED`, `AUTH-012 TERMINATED`, `ACT-024 DONE`, `ENV-012 EXPIRED`, durable local completion with no push.

- [ ] **Step 1: Fresh-check Stable-ID and revision collision against canonical main and V2 branch before allocating terminal IDs**

Reserve the next unused IDs after `EVD-079 / CHG-079`; do not assume numbers without checking V2/current branches.

- [ ] **Step 2: Create terminal Project Source revisions**

Record:

```text
TASK-045 DONE / VERIFIED_COMPLETE
OUT-012 ACHIEVED
AUTH-012 TERMINATED
ACT-024 DONE / VERIFIED_COMPLETE
ENV-012 EXPIRED
Framework distribution local branch = 1.15.0 verified
release evidence pointer
candidate/evidence/completion commit identities
publication NOT_AUTHORIZED / NOT_PUSHED
no V2 TASK-044 mutation
no continuing TASK-045 authority
```

Handoff should state no implementation work remains for TASK-045 locally; if publication is desired later, it requires a new exact publication instruction/Goal.

- [ ] **Step 3: Validate Project Source routing/archive/manifest consistency**

```text
git diff --check
rg -n "OUT-012|AUTH-012|ACT-024|ENV-012|TASK-045" Project-Source docs/superpowers/PROJECT-TASKS.md
```

Confirm one current active revision per affected slot and current Stable IDs resolve without archive traversal.

- [ ] **Step 4: Commit terminal reconciliation**

```text
git add Project-Source docs/superpowers/PROJECT-TASKS.md
git diff --cached --check
git commit -m "docs(project-source): complete TASK-045 response close goal"
```

- [ ] **Step 5: Freshly observe completion**

```text
git status --short --branch
git log -3 --oneline
rg -n "TASK-045|OUT-012|AUTH-012|ACT-024|ENV-012" Project-Source -g "03-Current-State-*.md" -g "09-Handoff-*.md"
```

Expected: worktree clean; TASK-045 terminal states visible; no required local result remains uncommitted.

- [ ] **Step 6: Stop before publication**

Do not run `git push`, open a PR, merge, or mutate external Project Settings. Report local verified completion and the separate publication/adoption boundary.
