from pathlib import Path
import subprocess

BASELINE = "efba94321ece4cbd520c9937c78e142f8a6d3c71"
LEDGER = Path("docs/superpowers/PROJECT-TASKS.md")
SPEC = Path("docs/superpowers/specs/2026-09-14-task057-ai-controltower-governance-support-layer-design.md")
PLAN = Path("docs/superpowers/plans/2026-09-14-task057-ai-controltower-governance-support-layer.md")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def replace_once(path: Path, old: str, new: str) -> None:
    text = read(path)
    count = text.count(old)
    assert count == 1, f"{path}: expected exactly one match, got {count}: {old[:100]!r}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def assert_desired_state() -> None:
    ledger = read(LEDGER)
    spec = read(SPEC)
    plan = read(PLAN)

    assert "`WRITTEN_SPEC_APPROVED / IMPLEMENTATION_PLAN_COMPLETE / EXECUTION_HANDOFF_REQUIRED / IMPLEMENTATION_NOT_STARTED`" in ledger
    assert "`WRITTEN / SELF_REVIEWED / EXECUTION_HANDOFF_REQUIRED / EXECUTION_NOT_STARTED`" in ledger
    assert "**Planner / Execution Handoff:** `GPT = PLANNER / EXECUTION_HANDOFF_REQUIRED`" in ledger
    assert "Handoff the approved implementation plan to the applicable execution-control layer." in ledger
    assert "choose implementation execution mode for the approved plan" not in ledger

    assert "Implementation state: `PLANNING_COMPLETE / EXECUTION_HANDOFF_REQUIRED / IMPLEMENTATION_NOT_STARTED`" in spec
    assert "### 2.1 Planner / Execution Handoff Boundary" in spec
    assert "`Planner ≠ Executor ≠ Verifier`." in spec
    assert "GPT MUST NOT self-promote into TASK execution merely because planning is complete." in spec
    assert "Implementation planning is complete; execution handoff is required; Framework normative mutation has not started." in spec

    assert "> **Execution handoff:** `GPT = PLANNER / EXECUTION_HANDOFF_REQUIRED`." in plan
    assert "> **For a selected agentic Executor:**" in plan
    assert "TASK-057 planner boundary: GPT is Planner; after plan completion state is `EXECUTION_HANDOFF_REQUIRED`" in plan
    assert "Execution handoff boundary: GPT remains Planner until a separate governed execution decision selects an eligible Executor" in plan
    assert "> **For agentic workers:** REQUIRED SUB-SKILL:" not in plan


# RED: the approved handoff contract must not already be present.
try:
    assert_desired_state()
except AssertionError:
    print("RED_PASS: approved planner handoff contract is absent before patch")
else:
    raise SystemExit("RED_FAIL: approved planner handoff contract already present")

replace_once(
    LEDGER,
    "- **readiness:** `WRITTEN_SPEC_APPROVED / IMPLEMENTATION_PLAN_COMPLETE / IMPLEMENTATION_NOT_STARTED`",
    "- **readiness:** `WRITTEN_SPEC_APPROVED / IMPLEMENTATION_PLAN_COMPLETE / EXECUTION_HANDOFF_REQUIRED / IMPLEMENTATION_NOT_STARTED`",
)
replace_once(
    LEDGER,
    "- **Plan State:** `WRITTEN / SELF_REVIEWED / EXECUTION_NOT_STARTED`.",
    "- **Plan State:** `WRITTEN / SELF_REVIEWED / EXECUTION_HANDOFF_REQUIRED / EXECUTION_NOT_STARTED`.",
)
old_design_state = "- **Design State:** `WRITTEN_SPEC_APPROVED / USER_APPROVED`; ACTOR-001 explicitly approved the written spec on 2026-09-14; implementation planning is complete and Framework normative mutation remains NOT_STARTED."
new_design_state = old_design_state + "\n- **Planner / Execution Handoff:** `GPT = PLANNER / EXECUTION_HANDOFF_REQUIRED`. Planning completion does not assign execution. The applicable execution-control layer selects an eligible Executor from current Task Contract, Execution Envelope, AUTH, `R4_CTX`, capability/tool/trust/executor policy, and Ready Gate. If independent verification is required, Verifier selection is separate. GPT MUST NOT self-promote into TASK execution merely because planning is complete."
replace_once(LEDGER, old_design_state, new_design_state)
replace_once(
    LEDGER,
    "- **Exact Next Step:** choose implementation execution mode for the approved plan; Framework normative mutation remains NOT_STARTED until execution begins.",
    "- **Exact Next Step:** Handoff the approved implementation plan to the applicable execution-control layer. That layer selects an eligible Executor under the current Task Contract, Execution Envelope, AUTH, `R4_CTX`, capability/tool/trust/executor policy, and Ready Gate. GPT remains Planner unless a future governed execution decision separately selects it as an eligible Executor. Framework normative mutation remains NOT_STARTED until an Executor begins governed execution.",
)

replace_once(
    SPEC,
    "Implementation state: `PLANNING_COMPLETE / IMPLEMENTATION_NOT_STARTED`",
    "Implementation state: `PLANNING_COMPLETE / EXECUTION_HANDOFF_REQUIRED / IMPLEMENTATION_NOT_STARTED`",
)
planner_section = """### 2.1 Planner / Execution Handoff Boundary

For TASK-057, the designated GPT role is `PLANNER`. Planning completion does not assign execution.

`Planner ≠ Executor ≠ Verifier`.

After the implementation plan is complete, the planning state becomes `EXECUTION_HANDOFF_REQUIRED`. The approved plan is handed to the applicable execution-control layer, which resolves the current Task Contract, Execution Envelope, AUTH, `R4_CTX`, capability/tool/trust/executor policy, and Task Ready Gate before selecting an eligible Executor.

Planner capability to execute ≠ assignment as Executor. GPT MUST NOT self-promote into TASK execution merely because planning is complete. GPT may execute only if a future governed execution decision separately selects it as an eligible Executor under current authority and eligibility constraints.

When independent verification is required, Verifier selection is a separate evaluation from Executor selection.

"""
replace_once(
    SPEC,
    "## 3. PLAN / TASK / VERIFY and R4 Current Truth",
    planner_section + "## 3. PLAN / TASK / VERIFY and R4 Current Truth",
)
replace_once(
    SPEC,
    "This file is the durable written-spec artifact. ACTOR-001 explicitly approved this written specification on 2026-09-14. Implementation planning is complete; Framework normative mutation has not started.",
    "This file is the durable written-spec artifact. ACTOR-001 explicitly approved this written specification on 2026-09-14. Implementation planning is complete; execution handoff is required; Framework normative mutation has not started.",
)

old_plan_header = "> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking."
new_plan_header = "> **Execution handoff:** `GPT = PLANNER / EXECUTION_HANDOFF_REQUIRED`. Planning completion does not assign execution. This approved plan MUST be handed to the applicable execution-control layer, which selects an eligible Executor from the current Task Contract, Execution Envelope, AUTH, `R4_CTX`, capability/tool/trust/executor policy, and Ready Gate. `Planner ≠ Executor ≠ Verifier`; GPT MUST NOT self-promote into TASK execution merely because planning is complete. Independent Verifier selection, when required, is separate from Executor selection.\n>\n> **For a selected agentic Executor:** after governed selection, use superpowers:subagent-driven-development or superpowers:executing-plans if supported by that execution environment. Steps use checkbox (`- [ ]`) syntax for tracking."
replace_once(PLAN, old_plan_header, new_plan_header)
replace_once(
    PLAN,
    "- Brownfield historical Tasks are not silently retrofitted.",
    "- Brownfield historical Tasks are not silently retrofitted.\n- TASK-057 planner boundary: GPT is Planner; after plan completion state is `EXECUTION_HANDOFF_REQUIRED`; Executor selection belongs to the applicable execution-control layer using current Task Contract, Execution Envelope, AUTH, `R4_CTX`, capability/tool/trust/executor policy, and Ready Gate; independent Verifier selection remains separate when applicable.",
)
replace_once(
    PLAN,
    "- Publication boundary: implementation verification remains distinct from shared-state publication/self-host promotion.",
    "- Publication boundary: implementation verification remains distinct from shared-state publication/self-host promotion.\n- Execution handoff boundary: GPT remains Planner until a separate governed execution decision selects an eligible Executor; plan completion alone never starts TASK execution.",
)

# GREEN: the same desired-state assertions must now pass.
assert_desired_state()
print("GREEN_PASS: planner/executor/verifier handoff contract is present")

subprocess.run(["git", "diff", "--check"], check=True)
subprocess.run(["git", "diff", "--quiet", BASELINE, "--", "Framework-Source"], check=True)
expected = {str(LEDGER), str(SPEC), str(PLAN)}
actual = set(subprocess.check_output(["git", "diff", "--name-only"], text=True).splitlines())
assert actual == expected, f"working-tree diff escaped bounded scope: {sorted(actual)}"
print("BOUNDED_WORKTREE_DIFF_PASS", sorted(actual))
