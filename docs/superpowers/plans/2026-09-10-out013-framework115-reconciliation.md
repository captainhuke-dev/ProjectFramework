# OUT-013 Framework 1.15 Reconciliation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reconcile the unpublished ProjectFramework 1.15 candidate so the current visible Final Response contract is exactly `Next Action → Next Goal → Reason`, cancel the 2.0 line without losing provenance, and complete verified local OUT-013 lifecycle closure.

**Architecture:** Reuse TASK-045 as the implementation lineage, but treat OUT-013 as a new correction/acceptance boundary because current README/SKILL/template drift changes the final Git candidate. A scratch-only verifier establishes RED before correction; only current/generic 1.15 drift is edited; historical four-field text stays untouched; a corrected candidate receives affected verification and exactly one new RELEASE_FULL before evidence and terminal Project Source reconciliation are committed.

**Tech Stack:** Markdown, YAML, Git, ripgrep, PowerShell, Python scratch verification via `uv run python`; no application/runtime/parser/validator/CLI artifact is added to the repository.

**Spec:** `docs/superpowers/specs/2026-09-10-task046-framework115-reconciliation-design.md`

## Global Constraints

- Active work object is `OUT-013 / AUTH-013 / ACT-025 / ENV-013`; TASK-046 is cancelled/superseded context, not the active implementation owner.
- Framework stays on `1.15.0`; Project Source Schema stays `1.0.0`; release format stays `3` unless a genuinely new schema requirement is discovered.
- Visible Final Response contract is exactly two mandatory headings followed by `[Next Action] → [Next Goal] → [Reason]`; `[Next Goal]` is mandatory and may be `ไม่มี`; nothing follows `[Reason]`.
- `[Chat]` and `[Required Read]` remain internal continuation/read-routing semantics and are not mandatory visible close fields.
- TASK-042 unskippable finalization and TASK-043 `Command Contract Completeness Gate → Response Close Completeness Gate → Emit` ordering remain binding.
- TASK-045 remains `DONE / VERIFIED_COMPLETE`; its original candidate/evidence are preserved as historical state-bound provenance and are not reused as verification of the changed OUT-013 candidate.
- TASK-044 remains `CANCELLED / IMPLEMENTATION_NOT_STARTED`; no ProjectFramework 2.0 cutover, AI-ControlTower mutation, or V2 runtime implementation is allowed.
- TASK-046 remains `CANCELLED / SUPERSEDED_BEFORE_IMPLEMENTATION`; its historical `BREAKING_RESPONSE_INTERFACE` classification does not classify OUT-013.
- V2 colliding Stable IDs are never imported/remapped/fabricated as current Project Source authority; preserve V2 via exact head/blob/artifact provenance only.
- Historical README/spec/plan/amendment/evidence text that accurately describes older four-field releases remains unchanged.
- Thin launchers remain `<=4,500` characters, retain shared body/parity where applicable, and must not reintroduce visible `[Chat]`/`[Required Read]` requirements.
- Registered command set remains exactly seven commands.
- Pressure scenarios remain contiguous/unique through `432`; scenarios `421–432` remain the current 1.15 response-close contract and are not renumbered.
- Maintained Project Source starter stamps remain `22/22` at Framework `1.15.0` / Schema `1.0.0`.
- Any byte change in an OUT-013 acceptance-scope current/release surface invalidates the old TASK-045 candidate as the OUT-013 final candidate.
- Exactly one new RELEASE_FULL is run on the corrected unchanged OUT-013 candidate.
- No repository runtime/parser/middleware/UI-hook/validator/CLI/bot/scheduler/watcher/daemon artifact is introduced.
- `commit ≠ push`; AUTH-013 does not authorize push/publication/PR/merge, destructive branch/worktree deletion, Root/Binding mutation, external disclosure, or actual secret values.

---

### Task 1: Establish OUT-013 RED verification contract

**Files:**
- Create outside the reconciliation worktree: `E:\GitHub\ProjectFramework\.worktrees\.out013-scratch\verify_out013.py`
- Inspect only: `README.md`
- Inspect only: `Framework-Source/SKILL.md`
- Inspect only: `Framework-Source/templates/00-project-source-framework.md`
- Inspect only: `Framework-Source/references/core-governance-rules.md`
- Inspect only: `Framework-Source/references/framework-governance-amendment-260906-task045-response-close-next-goal.md`
- Inspect only: `Framework-Source/MIGRATION-NOTES.md`
- Inspect only: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Inspect only: `Framework-Source/tests/pressure-scenarios.md`
- Inspect only: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md`
- Inspect only: `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md`
- Inspect only: `docs/superpowers/PROJECT-TASKS.md`

**Interfaces:**
- Consumes: approved OUT-013 spec and the current `f5f8ecf` reconciliation design checkpoint.
- Produces: one scratch verifier that fails on the known current/generic drift before production correction and becomes the focused/AFFECTED/RELEASE_FULL verification engine later. The verifier is never committed as Framework runtime or validator tooling.

- [ ] **Step 1: Fresh-check branch, ancestry, and clean state before creating RED evidence**

Run:

```powershell
git status --short --branch
git rev-parse HEAD
git merge-base --is-ancestor 1beaca26124e3be462bb812e93732f642ff25114 HEAD
git merge-base --is-ancestor caf2a19 HEAD
```

Expected:

```text
branch = task046-framework115-reconciliation
working tree = clean
TASK-045 terminal head ancestry exit = 0
TASK-046 registration reconciliation ancestry exit = 0
```

- [ ] **Step 2: Create the scratch verifier with exact current/historical/launcher/candidate checks**

Create `E:\GitHub\ProjectFramework\.worktrees\.out013-scratch\verify_out013.py` with exactly this content:

```python
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(r"E:\GitHub\ProjectFramework\.worktrees\task046-framework115-reconciliation")
FS = ROOT / "Framework-Source"


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def between(text: str, start: str, end: str) -> str:
    a = text.index(start)
    b = text.index(end, a)
    return text[a:b]


def task_block(text: str, number: int, next_number: int | None) -> str:
    start = text.index(f"## Task #{number}")
    if next_number is None:
        return text[start:]
    end = text.index(f"## Task #{next_number}", start)
    return text[start:end]


def git_ok(*args: str) -> bool:
    return subprocess.run(
        ["git", *args], cwd=ROOT, stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL, check=False
    ).returncode == 0


def check(name: str, ok: bool, results: list[tuple[str, bool]]) -> None:
    results.append((name, bool(ok)))


def main(mode: str) -> int:
    readme = read("README.md")
    skill = read("Framework-Source/SKILL.md")
    template = read("Framework-Source/templates/00-project-source-framework.md")
    core = read("Framework-Source/references/core-governance-rules.md")
    amendment = read("Framework-Source/references/framework-governance-amendment-260906-task045-response-close-next-goal.md")
    migration = read("Framework-Source/MIGRATION-NOTES.md")
    release = read("Framework-Source/FRAMEWORK-RELEASE.yaml")
    scenarios = read("Framework-Source/tests/pressure-scenarios.md")
    chatgpt = read("Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md")
    claude = read("Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md")
    tasks = read("docs/superpowers/PROJECT-TASKS.md")

    readme_top = "\n".join(readme.splitlines()[:60])
    skill_ops = between(skill, "Operational sequence:", "Mandatory Framework response close")
    t44 = task_block(tasks, 44, 45)
    t45 = task_block(tasks, 45, 46)
    t46 = task_block(tasks, 46, None)
    nums = [int(x) for x in re.findall(r"^## Scenario (\d+)\b", scenarios, re.M)]
    starter_files = list((FS / "templates" / "project-source-mockup").glob("*.md"))
    stamped = [p for p in starter_files if 'project_source_framework_version: "1.15.0"' in p.read_text(encoding="utf-8")]

    results: list[tuple[str, bool]] = []
    check("release-1.15", 'framework_version: "1.15.0"' in release, results)
    check("schema-1.0", 'schema_version: "1.0.0"' in release, results)
    check("core-three-field", "`[Next Action]:`, `[Next Goal]:`, and `[Reason]:`" in core and "nothing follows `[Reason]`" in core, results)
    check("amendment-next-goal-mandatory", "exactly one visible `[Next Goal]:` field" in amendment, results)
    check("migration-1.15", "## 1.14.0 → 1.15.0 (current)" in migration, results)
    check("readme-current-summary", "Every governed response ends with `[Next Action]:`, `[Next Goal]:`, `[Reason]:`." in readme_top, results)
    check("readme-current-no-four-field", "Every governed response ends with `[Next Action]:`, `[Chat]:`, `[Reason]:`, `[Required Read]:`." not in readme_top, results)
    check("skill-internal-chat", "Chat Continuity" in skill_ops and "`[Chat]` MUST" not in skill_ops, results)
    check("template-current-rendering", "**[Next Action]:**" in template and "e.g. `**[Chat]:** CONTINUE_CURRENT_CHAT`" not in template, results)
    check("historical-readme-1.3-preserved", "Mandatory response-close semantic labels remain `[Next Action]:`, `[Chat]:`, `[Reason]:`, and `[Required Read]:`" in readme, results)
    check("historical-readme-1.2.5-preserved", "two mandatory headings plus `[Next Action]`, `[Chat]`, `[Reason]`, and `[Required Read]`" in readme, results)
    check("historical-readme-1.2.4-preserved", "Mandatory response-close fields render as `[Next Action]:`, `[Chat]:`, `[Reason]:`, and `[Required Read]:`" in readme, results)
    check("scenarios-421-432", all(f"## Scenario {n} " in scenarios for n in range(421, 433)), results)
    check("scenario-contiguous-1-432", nums == list(range(1, 433)), results)
    check("launcher-ceiling", len(chatgpt) <= 4500 and len(claude) <= 4500, results)
    check("launcher-shared-body", chatgpt.splitlines()[1:] == claude.splitlines()[1:], results)
    check("launcher-no-visible-old-close", "[Chat]" not in chatgpt and "[Required Read]" not in chatgpt and "[Chat]" not in claude and "[Required Read]" not in claude, results)
    check("starter-stamps-22", len(stamped) == 22, results)
    check("task44-cancelled", "**Status:** `CANCELLED`" in t44 and "IMPLEMENTATION_NOT_STARTED" in t44, results)
    check("task45-done", "**Status:** `DONE`" in t45 and "Framework `1.15.0`" in t45, results)
    check("task46-cancelled", "**Status:** `CANCELLED`" in t46 and "SUPERSEDED_BEFORE_IMPLEMENTATION" in t46, results)
    check("breaking-class-history-only", "does not classify OUT-013" in read("docs/superpowers/specs/2026-09-10-task046-framework115-reconciliation-design.md"), results)
    check("task045-ancestry", git_ok("merge-base", "--is-ancestor", "1beaca26124e3be462bb812e93732f642ff25114", "HEAD"), results)
    check("task046-registration-ancestry", git_ok("merge-base", "--is-ancestor", "caf2a19", "HEAD"), results)
    check("v2-spec-blob", subprocess.check_output(["git", "rev-parse", "HEAD:docs/superpowers/specs/2026-09-04-projectframework-2-controltower-architecture-design.md"], cwd=ROOT, text=True).strip() == subprocess.check_output(["git", "rev-parse", "v2-premerge-readiness:docs/superpowers/specs/2026-09-04-projectframework-2-controltower-architecture-design.md"], cwd=ROOT, text=True).strip(), results)
    check("v2-plan-blob", subprocess.check_output(["git", "rev-parse", "HEAD:docs/superpowers/plans/2026-09-05-projectframework-2-ai-controltower-migration.md"], cwd=ROOT, text=True).strip() == subprocess.check_output(["git", "rev-parse", "v2-premerge-readiness:docs/superpowers/plans/2026-09-05-projectframework-2-ai-controltower-migration.md"], cwd=ROOT, text=True).strip(), results)
    check("v2-manifest-blob", subprocess.check_output(["git", "rev-parse", "HEAD:docs/superpowers/plans/2026-09-05-projectframework-2-ai-controltower-merge-manifest.md"], cwd=ROOT, text=True).strip() == subprocess.check_output(["git", "rev-parse", "v2-premerge-readiness:docs/superpowers/plans/2026-09-05-projectframework-2-ai-controltower-merge-manifest.md"], cwd=ROOT, text=True).strip(), results)

    if mode == "release_full":
        check("working-tree-clean", subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True) == "", results)
        check("branch-diff-hygiene", git_ok("diff", "--check", "origin/main..HEAD"), results)

    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    passed = sum(ok for _, ok in results)
    print(f"OUT013_{mode.upper()} {passed}/{len(results)}")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "affected"))
```

- [ ] **Step 3: Run the verifier against the uncorrected approved-design checkpoint and capture RED**

Run:

```powershell
uv run python E:\GitHub\ProjectFramework\.worktrees\.out013-scratch\verify_out013.py red
```

Expected: non-zero exit caused by the known current/generic drift checks:

```text
FAIL readme-current-summary
FAIL readme-current-no-four-field
FAIL skill-internal-chat
FAIL template-current-rendering
```

All baseline/provenance/current-1.15 contract checks should PASS. If a different semantic check fails, stop and classify it before editing production surfaces.

- [ ] **Step 4: Record RED as transient execution evidence, not a committed validator artifact**

Record the exact pass/fail count and failing check names for later `EVD-*`/release evidence. Do not add `verify_out013.py` to Git.

---

### Task 2: Correct the three known current/generic Framework 1.15 drift surfaces

**Files:**
- Modify: `README.md` — current Day-to-day summary only; preserve versioned historical 1.3.0 / 1.2.5 / 1.2.4 sections.
- Modify: `Framework-Source/SKILL.md` — `MCP Material Persistence and Chat Lifecycle` operational bullets only.
- Modify: `Framework-Source/templates/00-project-source-framework.md` — current generic Markdown response-close presentation sentence only.
- Inspect without semantic rewrite: `Framework-Source/references/core-governance-rules.md`
- Inspect without semantic rewrite: `Framework-Source/references/framework-governance-amendment-260906-task045-response-close-next-goal.md`
- Inspect without semantic rewrite: `Framework-Source/MIGRATION-NOTES.md`
- Inspect without semantic rewrite: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Inspect without semantic rewrite: `Framework-Source/tests/pressure-scenarios.md`

**Interfaces:**
- Consumes: Task 1 RED failures and approved three-field 1.15 contract.
- Produces: current/generic 1.15 surfaces that no longer contradict the canonical close while historical four-field release text remains intact.

- [ ] **Step 1: Replace the root README current Day-to-day close sentence**

Replace only the current summary sentence:

```text
Every governed response ends with `[Next Action]:`, `[Chat]:`, `[Reason]:`, `[Required Read]:`.
```

with:

```text
Every governed response ends with `[Next Action]:`, `[Next Goal]:`, `[Reason]:`. Chat lifecycle and Required Read routing remain internal continuation/Handoff state rather than mandatory visible close fields.
```

Do not alter the explicitly versioned historical text in the Framework 1.3.0, 1.2.5, or 1.2.4 sections.

- [ ] **Step 2: Rewrite SKILL operational bullets 8–13 as internal Chat Continuity rules**

Replace the six old bullets with exactly:

```text
8. Record internal Chat Continuity as exactly `CONTINUE_CURRENT_CHAT` or `START_NEW_CHAT` in `09 Handoff` when continuation state is material.
9. Use internal `START_NEW_CHAT` only after the persistence gate passes: durable current state, pending/blocker state, Exact Next Action, and Required Read location exist outside Chat.
10. If `[Next Action]` is exactly `ไม่มีขั้นตอนถัดไป`, internal Chat Continuity MUST be `START_NEW_CHAT`.
11. Internal `CONTINUE_CURRENT_CHAT` requires one concrete Next Action and MUST NOT pair with `ไม่มีขั้นตอนถัดไป`.
12. `PERSISTENCE_PENDING` requires internal Chat Continuity `CONTINUE_CURRENT_CHAT` plus one concrete persistence/recovery Next Action; it cannot pair with `START_NEW_CHAT` or `ไม่มีขั้นตอนถัดไป`.
13. Internal `START_NEW_CHAT` may carry a concrete Next Action when state is durably persisted and continuation is safe from Required Read locations.
```

Do not change the immediately following mandatory visible response-close example, which already correctly uses `Next Action → Next Goal → Reason`.

- [ ] **Step 3: Replace the current root-template Chat rendering example**

Replace:

```text
Markdown response-close presentation SHOULD keep canonical labels visibly renderable, e.g. `**[Chat]:** CONTINUE_CURRENT_CHAT`; wrapping is presentation-only and does not rename `[Chat]:` or lifecycle tokens.
```

with:

```text
Markdown response-close presentation SHOULD keep current canonical visible labels renderable, e.g. `**[Next Action]:** ...`, `**[Next Goal]:** ...`, and `**[Reason]:** ...`; wrapping is presentation-only and does not rename the semantic labels. Chat lifecycle remains internal Handoff state.
```

- [ ] **Step 4: Run the focused verifier after the three corrections**

Run:

```powershell
uv run python E:\GitHub\ProjectFramework\.worktrees\.out013-scratch\verify_out013.py affected
```

Expected: all checks PASS.

- [ ] **Step 5: Run a direct residual current/generic drift scan**

Run:

```powershell
rg -n "\[Chat\]|\[Required Read\]" README.md Framework-Source/SKILL.md Framework-Source/references/core-governance-rules.md Framework-Source/references/framework-governance-amendment-260906-task045-response-close-next-goal.md Framework-Source/MIGRATION-NOTES.md Framework-Source/templates Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md
```

Expected classification after correction:

```text
README top/current summary: no old four-field mandate
README 1.3.0 / 1.2.5 / 1.2.4 sections: historical, preserved
SKILL current gate text: only internal Chat/Required Read wording, no visible [Chat] MUST rule
Core/amendment/migration: explicit 1.15 removal/internal-preservation wording only
root template: 1.15 three-field visible contract + internal Chat wording only
launchers: no visible [Chat]/[Required Read] requirement
```

Any additional unversioned/current four-field mandate is a failure; classify and correct it before proceeding.

- [ ] **Step 6: Check diff scope/hygiene and commit the correction**

Run:

```powershell
git diff --check
git diff --name-only
```

Expected correction files only:

```text
README.md
Framework-Source/SKILL.md
Framework-Source/templates/00-project-source-framework.md
```

Then:

```powershell
git add README.md Framework-Source/SKILL.md Framework-Source/templates/00-project-source-framework.md
git diff --cached --check
git commit -m "docs(framework): reconcile 1.15 response close drift"
```

---

### Task 3: Run AFFECTED verification and freeze the corrected OUT-013 candidate

**Files:**
- Verify: `README.md`
- Verify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Verify: `Framework-Source/SKILL.md`
- Verify: `Framework-Source/references/core-governance-rules.md`
- Verify: `Framework-Source/references/framework-governance-amendment-260906-task045-response-close-next-goal.md`
- Verify: `Framework-Source/MIGRATION-NOTES.md`
- Verify: `Framework-Source/templates/00-project-source-framework.md`
- Verify: `Framework-Source/templates/core-document-skeletons.md`
- Verify: `Framework-Source/templates/project-source-mockup/*.md`
- Verify: `Framework-Source/tests/pressure-scenarios.md`
- Verify: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md`
- Verify: `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md`
- Verify: `docs/superpowers/PROJECT-TASKS.md`
- Verify provenance: imported TASK-044 V2 spec/plan/merge-manifest

**Interfaces:**
- Consumes: committed three-file correction from Task 2.
- Produces: AFFECTED PASS evidence and one frozen corrected candidate SHA/tree identity. No release evidence file is created until after the candidate is frozen.

- [ ] **Step 1: Re-run AFFECTED verifier from committed state**

Run:

```powershell
uv run python E:\GitHub\ProjectFramework\.worktrees\.out013-scratch\verify_out013.py affected
```

Expected: exit `0`, all focused/current/historical/provenance/launcher/starter/scenario checks PASS.

- [ ] **Step 2: Verify exactly seven Registered Commands remain unchanged**

Run this PowerShell check:

```powershell
$txt = Get-Content 'Framework-Source/templates/00-project-source-framework.md' -Raw -Encoding UTF8
$commands = @('[Project Status]','[Project Path]','[Project Upgrade]','[Session]','[Goal]','[Meeting]','[Project Audit]')
foreach($c in $commands){ if(-not $txt.Contains($c)){ throw "missing registered command $c" } }
if($txt.Contains('[Impact]') -or $txt.Contains('[Repair]')){ throw 'unexpected registered command-like addition' }
'OUT013_COMMAND_SET 7/7 PASS'
```

Expected: `OUT013_COMMAND_SET 7/7 PASS`.

- [ ] **Step 3: Verify starter stamps and scenario range independently**

Run:

```powershell
uv run python -c "from pathlib import Path; import re; r=Path(r'E:\GitHub\ProjectFramework\.worktrees\task046-framework115-reconciliation'); fs=r/'Framework-Source'; s=(fs/'tests/pressure-scenarios.md').read_text(encoding='utf-8'); nums=[int(x) for x in re.findall(r'^## Scenario (\d+)\b',s,re.M)]; files=list((fs/'templates/project-source-mockup').glob('*.md')); stamped=[p for p in files if 'project_source_framework_version: \"1.15.0\"' in p.read_text(encoding='utf-8')]; assert nums==list(range(1,433)); assert len(stamped)==22; print('OUT013_SCENARIOS_STARTERS PASS 432/432 22/22')"
```

Expected: `OUT013_SCENARIOS_STARTERS PASS 432/432 22/22`.

- [ ] **Step 4: Verify launcher ceiling and shared body independently**

Run:

```powershell
uv run python -c "from pathlib import Path; r=Path(r'E:\GitHub\ProjectFramework\.worktrees\task046-framework115-reconciliation\Framework-Source'); a=(r/'CHATGPT-PROJECT-INSTRUCTIONS.md').read_text(encoding='utf-8'); b=(r/'CLAUDE-PROJECT-INSTRUCTIONS.md').read_text(encoding='utf-8'); assert len(a)<=4500 and len(b)<=4500; assert a.splitlines()[1:]==b.splitlines()[1:]; assert '[Chat]' not in a+b and '[Required Read]' not in a+b; print(f'OUT013_LAUNCHERS PASS {len(a)}/{len(b)}')"
```

Expected: PASS with both lengths `<=4500`.

- [ ] **Step 5: Verify V2 artifact blobs still match the preserved V2 branch exactly**

Run:

```powershell
$paths = @(
  'docs/superpowers/specs/2026-09-04-projectframework-2-controltower-architecture-design.md',
  'docs/superpowers/plans/2026-09-05-projectframework-2-ai-controltower-migration.md',
  'docs/superpowers/plans/2026-09-05-projectframework-2-ai-controltower-merge-manifest.md'
)
foreach($p in $paths){
  $local = git rev-parse "HEAD:$p"
  $v2 = git rev-parse "v2-premerge-readiness:$p"
  if($local -ne $v2){ throw "V2 blob drift: $p" }
}
'OUT013_V2_PROVENANCE 3/3 PASS'
```

Expected: `OUT013_V2_PROVENANCE 3/3 PASS`.

- [ ] **Step 6: Verify full branch diff hygiene and clean working state**

Run:

```powershell
git diff --check origin/main..HEAD
git status --short --branch
```

Expected: diff check exit `0`; branch clean.

- [ ] **Step 7: Freeze and record corrected candidate identity**

Run:

```powershell
$env:OUT013_CANDIDATE = (git rev-parse HEAD).Trim()
$env:OUT013_TREE = (git rev-parse 'HEAD^{tree}').Trim()
$env:OUT013_FRAMEWORK_TREE = (git rev-parse 'HEAD:Framework-Source').Trim()
"CANDIDATE=$env:OUT013_CANDIDATE"
"TREE=$env:OUT013_TREE"
"FRAMEWORK_SOURCE_TREE=$env:OUT013_FRAMEWORK_TREE"
```

Persist these three exact identities in the later release evidence. Do not change any candidate-scope file before RELEASE_FULL.

---

### Task 4: Run exactly one new RELEASE_FULL and commit state-bound release evidence

**Files:**
- Create after the single RELEASE_FULL run: `docs/superpowers/evidence/2026-09-10-out013-framework115-reconciliation-release-full.md`
- Modify after RELEASE_FULL evidence exists: `docs/superpowers/PROJECT-TASKS.md` only to record OUT-013 candidate/verification state; do not change TASK-045 historical candidate evidence.

**Interfaces:**
- Consumes: frozen corrected candidate SHA/tree/Framework-Source tree from Task 3.
- Produces: exactly one new OUT-013 RELEASE_FULL result bound to the unchanged corrected candidate, plus a committed release-evidence artifact whose commit is referenced by terminal Project Source reconciliation.

- [ ] **Step 1: Confirm the candidate has not changed since freeze**

Run in the same execution environment that recorded the freeze variables:

```powershell
if((git rev-parse HEAD).Trim() -ne $env:OUT013_CANDIDATE){ throw 'OUT-013 candidate changed after freeze' }
if((git status --porcelain) -ne $null){
  $dirty = git status --porcelain
  if($dirty){ throw 'working tree changed after candidate freeze' }
}
'OUT013_CANDIDATE_UNCHANGED PASS'
```

Expected: `OUT013_CANDIDATE_UNCHANGED PASS`.

- [ ] **Step 2: Run the one and only new RELEASE_FULL for this candidate**

Run exactly once:

```powershell
uv run python E:\GitHub\ProjectFramework\.worktrees\.out013-scratch\verify_out013.py release_full
```

Expected: exit `0`; every release-full check PASS. Record the exact `OUT013_RELEASE_FULL X/X` count from stdout. Do not rerun on the unchanged candidate after a PASS. If it fails, the candidate is invalidated; correct the cause, create a new candidate, and only then run RELEASE_FULL for the new candidate.

- [ ] **Step 3: Create the release evidence file from observed results**

Create `docs/superpowers/evidence/2026-09-10-out013-framework115-reconciliation-release-full.md` with these concrete sections and replace angle-free labels with the exact observed values from Tasks 1–4:

```markdown
# OUT-013 Framework 1.15 Reconciliation Release Verification

## Scope
- Active work object: OUT-013 / AUTH-013 / ACT-025 / ENV-013.
- Framework: 1.15.0 / Schema 1.0.0 / release format 3.
- Publication: NOT_AUTHORIZED / NOT_PUSHED.

## Preserved lineage
- TASK-045 remains DONE / VERIFIED_COMPLETE; prior candidate bc7f91c49372ff33e9726da7461288479438b86a and RELEASE_FULL 33/33 PASS_RUN_1 are historical evidence only.
- TASK-044 remains CANCELLED / IMPLEMENTATION_NOT_STARTED; V2 spec/plan/merge-manifest blob equality 3/3 PASS.
- TASK-046 remains CANCELLED / SUPERSEDED_BEFORE_IMPLEMENTATION; historical BREAKING_RESPONSE_INTERFACE classification is non-applicable to OUT-013.

## RED
- Record the exact OUT013_RED pass/total and the four known failing current/generic checks observed before correction.

## Correction
- README current Day-to-day summary corrected.
- SKILL operational Chat lifecycle wording made internal-Handoff explicit.
- Root 00 template response-close rendering example corrected to Next Action / Next Goal / Reason.
- Historical README 1.3.0 / 1.2.5 / 1.2.4 four-field text preserved.

## AFFECTED
- Record exact OUT013_AFFECTED pass/total.
- Registered commands: 7/7 PASS.
- Scenarios: 1–432 contiguous/unique PASS.
- Maintained starter stamps: 22/22 at Framework 1.15.0 PASS.
- Thin launchers: <=4,500 / shared-body parity / no visible old-close mandate PASS.
- git diff --check origin/main..candidate PASS.

## Frozen candidate
- Candidate commit: use the exact Task 3 recorded candidate SHA.
- Candidate tree: use the exact Task 3 recorded tree SHA.
- Framework-Source tree: use the exact Task 3 recorded Framework-Source tree SHA.

## RELEASE_FULL
- Record exact OUT013_RELEASE_FULL pass/total.
- Run count: exactly one PASS run on this unchanged candidate.

## Boundary
No push, PR, merge, AI-ControlTower mutation, V2 cutover, runtime/parser/validator/CLI implementation, destructive branch/worktree deletion, Root/Binding mutation, external disclosure, or secret-value persistence occurred.
```

Do not leave unresolved placeholder tokens, angle-bracket placeholders, guessed counts, or guessed SHAs. Every value must come from the observed run.

- [ ] **Step 4: Update current Task ledger verification state without rewriting historical TASK-045 evidence**

In `docs/superpowers/PROJECT-TASKS.md`:

- keep TASK-044 `CANCELLED / IMPLEMENTATION_NOT_STARTED`;
- keep TASK-045 `DONE / VERIFIED_COMPLETE` and its original candidate/evidence unchanged;
- keep TASK-046 `CANCELLED / SUPERSEDED_BEFORE_IMPLEMENTATION`;
- append OUT-013 reconciliation state with exact corrected candidate, AFFECTED result, one new RELEASE_FULL result, and release-evidence path;
- state publication `NOT_AUTHORIZED / NOT_PUSHED`.

- [ ] **Step 5: Check evidence/task diff and commit**

Run:

```powershell
git diff --check
git add docs/superpowers/evidence/2026-09-10-out013-framework115-reconciliation-release-full.md docs/superpowers/PROJECT-TASKS.md
git diff --cached --check
git commit -m "docs(evidence): record OUT-013 Framework 1.15 verification"
git rev-parse HEAD
```

Record this exact release-evidence commit SHA for Task 5.

---

### Task 5: Terminalize OUT-013 Project Source and verify local completion

**Files:**
- Revise/promote/archive active: `Project-Source/01-Project-Source-Index-*.md`
- Revise/promote/archive active: `Project-Source/03-Current-State-*.md`
- Revise/promote/archive active: `Project-Source/09-Handoff-*.md`
- Revise/promote/archive active: `Project-Source/10-Change-Log-*.md`
- Revise/promote/archive active: `Project-Source/12-Authorization-Registry-*.md`
- Revise/promote/archive active: `Project-Source/13-Evidence-Registry-*.md`
- Revise/promote/archive active: `Project-Source/14-Project-Source-Manifest-*.md`
- Revise/promote/archive active: `Project-Source/15-Action-Registry-*.md`
- Revise/promote/archive active: `Project-Source/91-Project-Management-Control-*.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`

**Interfaces:**
- Consumes: release-evidence commit SHA and verified frozen candidate from Task 4.
- Produces: terminal `OUT-013 ACHIEVED / AUTH-013 TERMINATED / ACT-025 DONE / ENV-013 EXPIRED`, current routing to the terminal revisions, and a freshly observed local completion commit. Publication remains separate and unauthorized.

- [ ] **Step 1: Allocate next active revision filenames from the currently active set**

Starting from the committed design-approval + implementation-plan checkpoint active files:

```text
01 r086
03 r083
09 r083
10 r080
12 r028
13 r080
14 r086
15 r081
91 r045
```

Create exactly the next revision numbers (`01 r087`, `03 r084`, `09 r084`, `10 r081`, `12 r029`, `13 r081`, `14 r087`, `15 r082`, `91 r046`) with a fresh `260910-HHMM` suffix from the actual local timestamp. Each new file must `supersedes` the previous active filename; move the superseded active file to `Project-Source/archive/` only after the new revision content is validated.

- [ ] **Step 2: Terminalize lifecycle semantics in the owning registries**

Write these exact terminal states:

```text
OUT-013 ACHIEVED
AUTH-013 TERMINATED
ACT-025 DONE
ENV-013 EXPIRED
```

Required terminal facts:

```text
TASK-044 = CANCELLED / IMPLEMENTATION_NOT_STARTED
TASK-045 = DONE / VERIFIED_COMPLETE implementation lineage
TASK-046 = CANCELLED / SUPERSEDED_BEFORE_IMPLEMENTATION
Framework local distribution = 1.15.0 / Schema 1.0.0 / release format 3
corrected OUT-013 candidate/tree/Framework-Source tree = exact Task 3 values
OUT-013 AFFECTED = exact Task 3 result
OUT-013 RELEASE_FULL = exact Task 4 result / exactly one PASS run
release evidence = docs/superpowers/evidence/2026-09-10-out013-framework115-reconciliation-release-full.md + exact Task 4 evidence commit
publication = NOT_AUTHORIZED / NOT_PUSHED
no 2.0 cutover active
Exact Next Action = ไม่มีขั้นตอนถัดไป for local OUT-013 completion; publication/adoption requires separate authority
Chat Continuity = START_NEW_CHAT
Required Read Before Continue = PROJECT-BOOTSTRAP.md -> active 00 -> 01 -> 03 -> 09 -> OUT-013 release evidence if future publication/adoption is requested
```

Do not create a new OUT/AUTH/ACT/ENV family for terminalization.

- [ ] **Step 3: Add final `EVD-084` / `CHG-084` only if those IDs are still the next free active-lineage IDs at execution time**

Fresh-check current active `10` and `13` before allocating. If `CHG-084` and `EVD-084` remain unused, use them for final design-approval/plan/release/terminal evidence as appropriate; if another in-scope checkpoint has already consumed either ID, allocate the next observed free IDs. Never overwrite, remap, or reuse an existing Stable ID.

The final evidence record must reference the exact frozen candidate, one RELEASE_FULL result, release-evidence commit, terminal lifecycle states, and no-publication boundary.

- [ ] **Step 4: Update Index/Manifest/Handoff/Current State routing to the new active revisions**

Ensure `01` lists each new active filename once; `14` mirrors the active revision set without stale active Goal text; `03` and `09` report terminal OUT-013 state; all supersession chains point to the immediately prior active revision and never self-reference.

- [ ] **Step 5: Run terminal structural/readback verification before commit**

Run checks that prove:

```text
one active file per mandatory slot
all 9 revised active filenames routed by 01
all 9 prior active files present under archive/
no active file supersedes itself
OUT-013 / AUTH-013 / ACT-025 / ENV-013 terminal states agree across 03/09/12/15/91
TASK-044/045/046 statuses agree with docs/superpowers/PROJECT-TASKS.md
candidate/evidence identities agree with Task 4 release evidence
publication remains NOT_AUTHORIZED / NOT_PUSHED
```

Then run:

```powershell
git diff --check
git status --short
```

- [ ] **Step 6: Commit terminal reconciliation**

```powershell
git add Project-Source docs/superpowers/PROJECT-TASKS.md
git diff --cached --check
git commit -m "docs(project-source): terminalize OUT-013 reconciliation"
```

- [ ] **Step 7: Fresh-observe the completion commit and verify local terminal state**

Run:

```powershell
git status --short --branch
git rev-parse HEAD
git show --format=%H --name-only --no-renames HEAD
git merge-base --is-ancestor 1beaca26124e3be462bb812e93732f642ff25114 HEAD
git merge-base --is-ancestor caf2a19 HEAD
```

Then fresh-read active `01`, `03`, `09`, `12`, `13`, `14`, `15`, `91`, and Task ledger. Claim local Goal completion only if the completion commit is observed, working tree is clean, terminal lifecycle states agree, and the corrected candidate/release evidence identities are intact.

Do **not** rerun RELEASE_FULL after the already-passed unchanged candidate unless a candidate-scope dependency/content assumption was invalidated. Terminal Project Source/evidence bookkeeping after the frozen candidate uses proportional resulting-state confirmation.
