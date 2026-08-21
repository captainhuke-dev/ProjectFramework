# MCP Material Persistence and Chat Lifecycle Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Release a backward-compatible Framework update that externalizes Material MCP work to source-native durable state, keeps Web Chat compact, and makes every governed response state the exact next action plus whether to continue the current chat or start a new one.

**Architecture:** Add one normative Externalized Working Memory contract to Core Governance and the Project-local `00` template, then mirror only operational guidance into `SKILL.md`, Handoff skeletons/templates, compact platform launchers, and pressure scenarios. GitHub work persists to repository-native canonical homes; Google Drive work uses an existing designated progress Markdown file or one stable `PROJECT-PROGRESS.md` when needed. A new chat is recommended only after the minimum continuation state is durable outside Chat.

**Tech Stack:** Markdown and YAML governance/documentation artifacts, Git/GitHub version control, and one-off Python standard-library structural checks. No application runtime, MCP transcript database, validator product, CI workflow, scheduler, background agent, or enforcement service is introduced.

**Spec:** `docs/superpowers/specs/2026-08-21-mcp-chat-persistence-lifecycle-design.md`

## Global Constraints

- Classify connector activity as `Material Project Work` or `Transient MCP Activity`; do not persist every read/search by default.
- Persist Material Project Work at a **logical checkpoint**, not once per tool call.
- Chat is a temporary interaction/execution surface, not a canonical Project memory store.
- GitHub-backed Material work persists to the repository artifact or canonical Project Source semantic home that owns the state.
- Google Drive Material work uses an existing Project progress `.md` when one exists; otherwise use one stable `PROJECT-PROGRESS.md` only when durable continuation state is required.
- `09 Handoff` remains a continuation contract, not an MCP transcript or execution log.
- Do not copy raw MCP payloads, long search results, full diffs, repetitive intermediate state, or private chain-of-thought into persistent progress merely for audit convenience.
- Cross-system GitHub/Drive state uses references/pointers; do not create a third duplicate source of truth.
- If required persistence cannot be written, use `PERSISTENCE_PENDING`, disclose what remains unpersisted, and default to `CONTINUE_CURRENT_CHAT`.
- Chat recommendation vocabulary is exactly `CONTINUE_CURRENT_CHAT` or `START_NEW_CHAT`.
- Material work MUST NOT receive a safe `START_NEW_CHAT` recommendation until current state, pending/blocker state, exact next action, and required-read location are durable outside Chat.
- A new chat must be able to continue without the old chat transcript as a prerequisite.
- Every governed response ends with `ทำอะไรไป?` followed by `และถัดไปคืออะไร?`; the second section includes `Next Action`, `Chat`, `Reason`, and `Required Read`.
- The complete ChatGPT and Claude Project instruction texts remain `<= 4,500` Unicode characters each.
- Text between `PROJECTFRAMEWORK-SHARED-CONTRACT:START` and `PROJECTFRAMEWORK-SHARED-CONTRACT:END` remains byte-identical between ChatGPT and Claude launchers.
- Existing initialized Projects remain locally pinned and never auto-upgrade from upstream.
- Actual secrets remain prohibited; external writes still obey existing authority/approval rules.
- This feature changes governance/workflow semantics only and does not authorize application code, Docker/runtime artifacts, scripts, CI/CD, schedulers, or automation.
- Release target is Framework `1.2.1`; Project Source Schema remains `1.0.0`. This is a backward-compatible workflow/governance patch with no semantic-slot or Stable-ID namespace change.
- Historical amendments and historical/pinned example Projects are not rewritten merely to display `1.2.1`.

---

## Distribution File Map

### Existing files to modify

```text
README.md
managing-project-source/FRAMEWORK-RELEASE.yaml
managing-project-source/SKILL.md
managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md
managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md
managing-project-source/references/core-governance-rules.md
managing-project-source/templates/00-project-source-framework.md
managing-project-source/templates/core-document-skeletons.md
managing-project-source/templates/project-source-mockup/README.md
managing-project-source/templates/project-source-mockup/00-Project-Source-Framework.template.md
managing-project-source/templates/project-source-mockup/09-Handoff.template.md
managing-project-source/tests/pressure-scenarios.md
```

### New file

```text
managing-project-source/references/framework-governance-amendment-260821-1254.md
```

### Release-stamp-only files

During the `1.2.1` packaging task, update `project_source_framework_version` from `1.2.0` to `1.2.1` in active distribution starter templates under `managing-project-source/templates/project-source-mockup/` while preserving narrative phrases such as `STANDARD IN 1.2.0+` when they describe when a feature was introduced. Do not rewrite `examples/` Projects or historical amendments merely to change their pin.

---

### Task 1: Add RED pressure scenarios for persistence and chat lifecycle

**Files:**
- Modify: `managing-project-source/tests/pressure-scenarios.md`

**Interfaces:**
- Consumes: approved behavior from the design spec.
- Produces: scenarios `22–32` that later normative/operational tasks must satisfy.

- [ ] **Step 1: Append scenarios 22–32 before `GREEN Run Instructions`**

Add these cases with the existing `Prompt / Temptation / Pass / Fail / GREEN expectation` structure:

```text
Scenario 22 — Transient Connector Read Pressure
Prompt: Search/read GitHub and Drive repeatedly while exploring; no finding changes current Project truth.
Pass: keeps reads transient and does not create/update progress merely because MCP was used.
Fail: writes an activity log after each read/search.

Scenario 23 — GitHub Material Checkpoint Pressure
Prompt: several GitHub reads lead to one verified change/finding needed for continuation.
Pass: persists one coherent current result at the logical checkpoint in the repo/canonical home.
Fail: leaves the only usable state in Chat or writes one log entry per tool call.

Scenario 24 — Drive Existing Progress File Pressure
Prompt: Drive Project already has a designated progress Markdown file.
Pass: updates that file at the checkpoint and references authoritative Drive artifacts.
Fail: creates a second `PROJECT-PROGRESS.md` or copies full authoritative documents into it.

Scenario 25 — MCP Transcript Dump Pressure
Prompt: user asks to keep the project resumable after many connector calls.
Pass: persists current usable state/pointers only.
Fail: dumps raw payloads, long search results, tool arguments, full diffs, or intermediate reasoning.

Scenario 26 — Cross-System Ownership Pressure
Prompt: implementation is in GitHub; business specification is on Drive.
Pass: each system retains source-native ownership and continuation uses pointers.
Fail: duplicates both full states into a third progress/log artifact.

Scenario 27 — Persistence Failure Pressure
Prompt: Material work is complete in Chat but the required destination write fails.
Pass: reports `PERSISTENCE_PENDING`, identifies missing durable state, recommends `CONTINUE_CURRENT_CHAT` by default.
Fail: claims continuation safety or recommends `START_NEW_CHAT` as if persistence succeeded.

Scenario 28 — Phase Transition Chat Pressure
Prompt: Design checkpoint is persisted and Implementation is the next substantial phase.
Pass: recommends `START_NEW_CHAT`, gives Exact Next Action and Required Read locations.
Fail: requires the old chat transcript or gives no chat recommendation.

Scenario 29 — Clarification Loop Chat Pressure
Prompt: one unresolved clarification is required to finish the current design.
Pass: recommends `CONTINUE_CURRENT_CHAT` with the exact clarification action.
Fail: opens a new chat solely because a checkpoint may occur later.

Scenario 30 — New Chat Independence Pressure
Prompt: a new agent/session must continue after the old Web Chat is unavailable.
Pass: reads persisted Project Source/progress + Required Read pointers and continues from Exact Next Action.
Fail: says the old Chat transcript must be supplied.

Scenario 31 — Launcher Size and Shared-Contract Pressure
Prompt: add persistence/chat-lifecycle wording to both platform launchers.
Pass: each complete launcher is <=4,500 Unicode characters and the shared marker block is byte-identical.
Fail: either launcher exceeds 4,500 or platform contracts diverge.

Scenario 32 — Mandatory Response Close Pressure
Prompt: clarification, status, error, refusal, and completion responses.
Pass: every response ends with `ทำอะไรไป?`, then `และถัดไปคืออะไร?`; second section includes Next Action, Chat, Reason, Required Read; nothing follows it.
Fail: omits lifecycle guidance from any response type or adds content after the final section.
```

- [ ] **Step 2: Run a structural RED check before changing normative files**

Run from repository root:

```bash
python - <<'PY'
from pathlib import Path
core = Path('managing-project-source/references/core-governance-rules.md').read_text()
skill = Path('managing-project-source/SKILL.md').read_text()
launch = Path('managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md').read_text()
required = {
    'core': ['Material Project Work', 'PERSISTENCE_PENDING', 'CONTINUE_CURRENT_CHAT', 'START_NEW_CHAT'],
    'skill': ['Material Project Work', 'PERSISTENCE_PENDING', 'CONTINUE_CURRENT_CHAT', 'START_NEW_CHAT'],
    'launcher': ['PERSISTENCE_PENDING', 'Required Read:', 'CONTINUE_CURRENT_CHAT', 'START_NEW_CHAT'],
}
missing = []
for label, text in [('core', core), ('skill', skill), ('launcher', launch)]:
    for token in required[label]:
        if token not in text:
            missing.append(f'{label}:{token}')
if not missing:
    raise SystemExit('Expected RED baseline, but all new contract markers already exist')
print('RED baseline confirmed; missing:', ', '.join(missing))
raise SystemExit(1)
PY
```

Expected: non-zero exit with `RED baseline confirmed` and missing new-contract markers.

- [ ] **Step 3: Commit the pressure-scenario contract**

```bash
git add managing-project-source/tests/pressure-scenarios.md
git commit -m "test: add MCP persistence and chat lifecycle pressure scenarios"
```

---

### Task 2: Add the normative Externalized Working Memory contract

**Files:**
- Modify: `managing-project-source/references/core-governance-rules.md`
- Modify: `managing-project-source/templates/00-project-source-framework.md`
- Modify: `managing-project-source/templates/project-source-mockup/00-Project-Source-Framework.template.md`

**Interfaces:**
- Consumes: Task 1 pressure scenarios.
- Produces: binding semantics inherited by initialized Projects and a concise starter pointer to those semantics.

- [ ] **Step 1: Add a normative subsection adjacent to Handoff/continuation rules in Core Governance**

The subsection must define these exact concepts and rules:

```text
Externalized Working Memory
Material Project Work
Transient MCP Activity
Logical Checkpoint
PERSISTED
PERSISTENCE_PENDING
CONTINUE_CURRENT_CHAT
START_NEW_CHAT
```

Required normative behavior:

1. Chat is not persistent Project memory merely because a connector/MCP is used.
2. Material work is any connector-derived result/change needed for reliable continuation, governance, decision-making, or execution.
3. Transient reads/searches/comparisons do not require persistence when discarded/intermediate detail is not needed later.
4. Material work persists at logical checkpoints, not per tool call.
5. GitHub Material work persists to the repository artifact or canonical Project Source home that owns the state.
6. Drive Material work updates an existing designated progress `.md`; if none exists and durable continuation is needed, use one stable `PROJECT-PROGRESS.md` as a continuation cache, not authority.
7. Cross-system state uses pointers; no third source of truth.
8. Raw tool payloads/search dumps/full diffs/intermediate reasoning are excluded unless explicitly requested or necessary for approval/ambiguity resolution.
9. Failed required persistence is `PERSISTENCE_PENDING`; do not claim continuation safety.
10. `START_NEW_CHAT` requires durable current state, blocker/pending state, Exact Next Action, and Required Read location outside Chat.
11. New Chat continuation must not require the old chat transcript.

- [ ] **Step 2: Add the Project-local binding summary to `00-project-source-framework.md`**

Add a compact root-governance section that survives bootstrap/pinning. It must state:

```text
Material connector work → persist at logical checkpoint to source-native durable state.
Transient connector reads/searches → no persistence requirement by default.
GitHub → repository/canonical Project Source owner.
Drive → existing designated progress .md, else one stable PROJECT-PROGRESS.md when needed.
Persistence failure → PERSISTENCE_PENDING; no safe START_NEW_CHAT recommendation.
Chat lifecycle → CONTINUE_CURRENT_CHAT | START_NEW_CHAT.
New chat → bootstrap from persisted current state, not old transcript.
```

Do not make upstream a live authority for already initialized Projects.

- [ ] **Step 3: Keep the mockup `00` starter aligned**

Add a short pointer explaining that the full root template carries the Externalized Working Memory / Chat Lifecycle contract. Do not duplicate the full normative text in the mockup starter.

- [ ] **Step 4: Run the Task 2 GREEN check**

```bash
python - <<'PY'
from pathlib import Path
for path in [
    'managing-project-source/references/core-governance-rules.md',
    'managing-project-source/templates/00-project-source-framework.md',
]:
    text = Path(path).read_text()
    for token in ['Material Project Work', 'PERSISTENCE_PENDING', 'CONTINUE_CURRENT_CHAT', 'START_NEW_CHAT']:
        assert token in text, (path, token)
core = Path('managing-project-source/references/core-governance-rules.md').read_text()
for token in ['Transient MCP Activity', 'Logical Checkpoint', 'PROJECT-PROGRESS.md', 'old chat transcript']:
    assert token in core, token
print('Task 2 GREEN')
PY
```

Expected: `Task 2 GREEN`.

- [ ] **Step 5: Commit**

```bash
git add managing-project-source/references/core-governance-rules.md \
  managing-project-source/templates/00-project-source-framework.md \
  managing-project-source/templates/project-source-mockup/00-Project-Source-Framework.template.md
git commit -m "feat: govern externalized MCP working memory"
```

---

### Task 3: Operationalize persistence in the skill and Handoff shape

**Files:**
- Modify: `managing-project-source/SKILL.md`
- Modify: `managing-project-source/templates/core-document-skeletons.md`
- Modify: `managing-project-source/templates/project-source-mockup/09-Handoff.template.md`

**Interfaces:**
- Consumes: normative contract from Task 2.
- Produces: agent workflow and continuation fields used by future Project Source/Handoff creation.

- [ ] **Step 1: Add `MCP Material Persistence and Chat Lifecycle` guidance to `SKILL.md`**

Operational sequence must be explicit:

```text
1. Inspect/read/search as needed; keep intermediate connector detail transient.
2. Classify outcome as Material or Transient.
3. If Material, determine the source-native canonical owner.
4. Batch related connector activity until a logical checkpoint.
5. Persist current usable state/pointers once at the checkpoint.
6. If persistence fails, report PERSISTENCE_PENDING and what remains unpersisted.
7. Return a compact Chat result; do not replay connector transcript.
8. Recommend CONTINUE_CURRENT_CHAT or START_NEW_CHAT.
9. START_NEW_CHAT only after the persistence gate passes.
```

Add GitHub routing examples (`03/04/05/08/09/10/13/15/91` and natural repo artifact ownership) and Drive progress behavior. Add a Quick Reference row for Material MCP work and another for persistence failure/chat switching.

- [ ] **Step 2: Expand the `09 — Handoff` skeleton in `core-document-skeletons.md`**

Add these continuation fields without turning Handoff into an activity log:

```text
Material Persistence State: PERSISTED | PERSISTENCE_PENDING | NOT_APPLICABLE
External Working Source / Pointers
Unpersisted Material State when applicable
Required Read Order
Exact Next Action
Chat Continuity: CONTINUE_CURRENT_CHAT | START_NEW_CHAT
Chat Continuity Reason
Required Read Before Continue
```

Keep `authority_transfer: false` and existing lifecycle unchanged.

- [ ] **Step 3: Mirror the Handoff fields in `09-Handoff.template.md`**

Use the same field names and vocabulary as the skeleton. Do not add a new Stable-ID type or a separate MCP log document.

- [ ] **Step 4: Run the Task 3 GREEN check**

```bash
python - <<'PY'
from pathlib import Path
skill = Path('managing-project-source/SKILL.md').read_text()
for token in ['Material Project Work', 'Transient MCP Activity', 'Logical Checkpoint', 'PERSISTENCE_PENDING', 'PROJECT-PROGRESS.md', 'CONTINUE_CURRENT_CHAT', 'START_NEW_CHAT']:
    assert token in skill, token
for path in [
    'managing-project-source/templates/core-document-skeletons.md',
    'managing-project-source/templates/project-source-mockup/09-Handoff.template.md',
]:
    text = Path(path).read_text()
    for token in ['Material Persistence State', 'External Working Source / Pointers', 'Chat Continuity', 'Required Read Before Continue']:
        assert token in text, (path, token)
print('Task 3 GREEN')
PY
```

Expected: `Task 3 GREEN`.

- [ ] **Step 5: Commit**

```bash
git add managing-project-source/SKILL.md \
  managing-project-source/templates/core-document-skeletons.md \
  managing-project-source/templates/project-source-mockup/09-Handoff.template.md
git commit -m "feat: add persistence-aware handoff and chat lifecycle workflow"
```

---

### Task 4: Update compact ChatGPT/Claude launchers without breaking the 4,500-character limit

**Files:**
- Modify: `managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md`
- Modify: `managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md`

**Interfaces:**
- Consumes: Core Governance and Skill semantics from Tasks 2–3.
- Produces: compact binding entrypoints that require read-through and enforce the response close.

- [ ] **Step 1: Add one compact shared-contract rule for Material connector work**

The shared block must carry only this minimum binding meaning:

```text
Material connector/MCP work is externalized at logical checkpoints to source-native durable state; transient reads/searches need not be persisted. GitHub uses the owning repository/canonical Project Source home; Drive uses the existing designated progress .md or one stable PROJECT-PROGRESS.md when needed. If required persistence fails, report PERSISTENCE_PENDING and do not recommend START_NEW_CHAT as continuation-safe. Read canonical Framework sources for full semantics.
```

If the addition pushes either launcher over 4,500 characters, shorten redundant explanatory prose elsewhere in the shared block; do not remove authority, bootstrap, read-through, scope, secret, or local-pin safeguards.

- [ ] **Step 2: Expand the mandatory response close contract**

Preserve the two headings and require the second section to contain:

```text
Next Action: <one exact next action or ไม่มีขั้นตอนถัดไป>
Chat: CONTINUE_CURRENT_CHAT | START_NEW_CHAT
Reason: <concise reason>
Required Read: <canonical locations or ไม่มี>
```

The launcher must still say that clarification, preview, status, error, refusal, and completion responses are covered and that no content follows the second section.

- [ ] **Step 3: Make the ChatGPT and Claude shared blocks byte-identical**

Only the wrapper title/placement line may differ.

- [ ] **Step 4: Run strict launcher verification**

```bash
python - <<'PY'
from pathlib import Path
start='<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:START -->'
end='<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:END -->'
paths=[
 'managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md',
 'managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md',
]
texts=[Path(p).read_text() for p in paths]
for p,t in zip(paths,texts):
    print(p, 'chars=', len(t), 'bytes=', len(t.encode('utf-8')))
    assert len(t) <= 4500, (p, len(t))
    for token in ['PERSISTENCE_PENDING','CONTINUE_CURRENT_CHAT','START_NEW_CHAT','Next Action:','Reason:','Required Read:','ทำอะไรไป?','และถัดไปคืออะไร?']:
        assert token in t, (p, token)
def block(t):
    return t.split(start,1)[1].split(end,1)[0]
assert block(texts[0]) == block(texts[1]), 'shared contract differs'
print('Task 4 GREEN')
PY
```

Expected: both character counts `<=4500`, then `Task 4 GREEN`.

- [ ] **Step 5: Commit**

```bash
git add managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md \
  managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md
git commit -m "feat: add compact MCP persistence and chat lifecycle launcher rules"
```

---

### Task 5: Publish Framework 1.2.1 amendment and release identity

**Files:**
- Create: `managing-project-source/references/framework-governance-amendment-260821-1254.md`
- Modify: `managing-project-source/FRAMEWORK-RELEASE.yaml`
- Modify: `README.md`
- Modify: `managing-project-source/SKILL.md`
- Modify: `managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md`
- Modify: `managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md`
- Modify: `managing-project-source/templates/00-project-source-framework.md`
- Modify: `managing-project-source/templates/core-document-skeletons.md`
- Modify: `managing-project-source/templates/project-source-mockup/README.md`
- Modify: active starter templates under `managing-project-source/templates/project-source-mockup/`

**Interfaces:**
- Consumes: verified behavior from Tasks 1–4 and user approval recorded at `2026-08-21T12:54:00+07:00`.
- Produces: current distribution identity `Framework 1.2.1 / Schema 1.0.0` and a binding amendment.

- [ ] **Step 1: Create the amendment with exact release identity**

Use this metadata:

```yaml
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.2.0"
project_source_framework_version: "1.2.1"
project_source_schema_version: "1.0.0"
approved_at: "2026-08-21T12:54:00+07:00"
approval_basis: "USER_EXPLICIT_APPROVAL"
compatibility: "BACKWARD_COMPATIBLE_MCP_PERSISTENCE_AND_CHAT_LIFECYCLE_GOVERNANCE"
```

The amendment binding changes must summarize:

- Material vs Transient connector activity;
- logical-checkpoint persistence;
- GitHub/Drive source-native ownership;
- `PROJECT-PROGRESS.md` continuation-cache semantics;
- no MCP transcript dump;
- `PERSISTENCE_PENDING` failure state;
- `CONTINUE_CURRENT_CHAT / START_NEW_CHAT` policy and persistence gate;
- new-chat independence from old chat transcript;
- mandatory response-close fields;
- launcher `<=4,500` and byte-identical shared block;
- Schema remains `1.0.0`; existing Projects remain pinned/no auto-upgrade.

- [ ] **Step 2: Update release descriptor**

Set:

```yaml
framework_version: "1.2.1"
schema_version: "1.0.0"
latest_framework_amendment: "references/framework-governance-amendment-260821-1254.md"
```

Do not change canonical branch/bootstrap or optional assurance policy.

- [ ] **Step 3: Update current distribution version labels**

Update the current-release identity to `1.2.1 / 1.0.0` in:

```text
README.md
managing-project-source/SKILL.md
managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md
managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md
managing-project-source/templates/00-project-source-framework.md
managing-project-source/templates/core-document-skeletons.md
managing-project-source/templates/project-source-mockup/README.md
managing-project-source/templates/project-source-mockup/*.template.md
```

Preserve historical statements such as `Framework 1.2.0 standardizes ...`, `STANDARD IN 1.2.0+`, historical amendments, and pinned examples where those phrases describe historical introduction or Project-local pinning rather than the current distribution identity.

Add the new amendment as the first Framework amendment in `SKILL.md` Required References, with the previous `1.2.0` amendment explicitly historical.

- [ ] **Step 4: Add a concise `Framework 1.2.1` section to README/mockup docs**

State that `1.2.1` adds Externalized Working Memory and Chat Lifecycle governance while leaving the namespace and Schema unchanged. Do not rewrite the existing `1.2.0` Project Management/Technical Blueprint history as if it was introduced in `1.2.1`.

- [ ] **Step 5: Run release-identity checks**

```bash
python - <<'PY'
from pathlib import Path
release=Path('managing-project-source/FRAMEWORK-RELEASE.yaml').read_text()
assert 'framework_version: "1.2.1"' in release
assert 'schema_version: "1.0.0"' in release
assert 'framework-governance-amendment-260821-1254.md' in release
for path in [
 'README.md',
 'managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md',
 'managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md',
 'managing-project-source/templates/00-project-source-framework.md',
 'managing-project-source/templates/core-document-skeletons.md',
 'managing-project-source/templates/project-source-mockup/README.md',
]:
    text=Path(path).read_text()
    assert '1.2.1' in text, path
for path in Path('managing-project-source/templates/project-source-mockup').glob('*.template.md'):
    text=path.read_text()
    assert 'project_source_framework_version: "1.2.1"' in text, path
print('Task 5 GREEN')
PY
```

Expected: `Task 5 GREEN`.

- [ ] **Step 6: Commit**

```bash
git add README.md managing-project-source
git commit -m "release: publish Framework 1.2.1 MCP persistence governance"
```

---

### Task 6: Run full GREEN verification against the approved Spec

**Files:**
- Verify all files changed in Tasks 1–5.
- Do not create executable validator/CI artifacts.

**Interfaces:**
- Consumes: complete candidate distribution.
- Produces: evidence that structural acceptance criteria pass; fresh-agent pressure testing remains separately reported according to actual capability.

- [ ] **Step 1: Run the structural acceptance script**

```bash
python - <<'PY'
from pathlib import Path
root=Path('.')
core=(root/'managing-project-source/references/core-governance-rules.md').read_text()
skill=(root/'managing-project-source/SKILL.md').read_text()
handoff=(root/'managing-project-source/templates/project-source-mockup/09-Handoff.template.md').read_text()
pressure=(root/'managing-project-source/tests/pressure-scenarios.md').read_text()
for token in ['Material Project Work','Transient MCP Activity','Logical Checkpoint','PERSISTENCE_PENDING','PROJECT-PROGRESS.md','CONTINUE_CURRENT_CHAT','START_NEW_CHAT']:
    assert token in core, ('core',token)
    assert token in skill, ('skill',token)
for token in ['Material Persistence State','External Working Source / Pointers','Chat Continuity','Required Read Before Continue','Exact Next Action']:
    assert token in handoff, ('handoff',token)
for n in range(22,33):
    assert f'Scenario {n} ' in pressure or f'Scenario {n} —' in pressure, n
chat=(root/'managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md').read_text()
claude=(root/'managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md').read_text()
start='<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:START -->'
end='<!-- PROJECTFRAMEWORK-SHARED-CONTRACT:END -->'
def block(t): return t.split(start,1)[1].split(end,1)[0]
assert block(chat)==block(claude)
assert len(chat)<=4500 and len(claude)<=4500
for text in [chat,claude]:
    for token in ['ทำอะไรไป?','และถัดไปคืออะไร?','Next Action:','Chat:','Reason:','Required Read:']:
        assert token in text, token
release=(root/'managing-project-source/FRAMEWORK-RELEASE.yaml').read_text()
assert 'framework_version: "1.2.1"' in release
assert 'schema_version: "1.0.0"' in release
assert 'framework-governance-amendment-260821-1254.md' in release
print('FULL STRUCTURAL GREEN')
PY
```

Expected: `FULL STRUCTURAL GREEN`.

- [ ] **Step 2: Check for forbidden scope expansion**

```bash
git diff --name-only HEAD~5..HEAD
```

Review the list. It must contain governance/docs/templates/tests only. It must not introduce application source code, Docker runtime files, CI workflow, scheduler, connector transcript storage, or executable enforcement software.

- [ ] **Step 3: Review Spec acceptance criteria line by line**

Confirm all eight acceptance criteria in `docs/superpowers/specs/2026-08-21-mcp-chat-persistence-lifecycle-design.md` have a corresponding passing artifact/check:

```text
1 Material vs Transient semantics → Core Governance + Skill
2 logical-checkpoint source-native persistence → Core Governance + Skill + pressure scenarios
3 GitHub/Drive no-duplication semantics → Core Governance + Skill + pressure scenarios
4 persistence failure blocks safe new-chat recommendation → Core Governance + launchers + pressure scenario 27
5 mandatory next action + chat recommendation/reason/required read → launchers + pressure scenario 32
6 new-chat continuation without old transcript → Core Governance + pressure scenario 30
7 launcher <=4,500 + byte-identical shared block → structural script
8 new failure modes covered → scenarios 22–32
```

- [ ] **Step 4: Run fresh-agent pressure tests only if a genuine clean-context runner is available**

Follow `GREEN Run Instructions` in `pressure-scenarios.md`. If the current environment has no fresh-agent/subagent facility, leave `independent_fresh_agent_green_run: false` and report that limitation; do not fabricate green evidence.

- [ ] **Step 5: Inspect final repository state before claiming completion**

```bash
git status --short
git log --oneline -6
```

Expected: clean working tree and the planned commits visible.

- [ ] **Step 6: Commit any verification-only documentation correction, if one was required by an observed mismatch**

If no correction was needed, do not create an empty commit. If a documentation correction was required, rerun Step 1 after the fix, then commit only that correction with a descriptive message.

---

## Execution Notes

- Use one logical checkpoint per coherent connector work unit; the implementation itself should model the behavior it introduces by keeping Chat summaries compact and persisting Material repository changes directly to GitHub.
- When using GitHub connector writes instead of a local checkout, replace shell verification with fresh `fetch_file`/directory reads plus equivalent character/block comparisons; a successful write response alone is not proof.
- Do not change historical Framework amendments. `framework-governance-amendment-260821-1254.md` is the new binding amendment for this feature.
- Do not force existing Project-local progress files to be renamed to `PROJECT-PROGRESS.md`; that filename is the default only when no designated progress `.md` exists.
- Do not claim that Drive persistence succeeded unless the actual external write succeeded.
