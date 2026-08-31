# TASK-024 `[Meeting]` LLM Council Command Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement Framework `1.8.0` `[Meeting]` as a documentation/governance command that uses a verified external LLM Council provider profile for advisory multi-model reasoning without turning provider output, storage, or consensus into Project authority.

**Architecture:** ProjectFramework owns the `[Meeting]` command, context/disclosure boundary, normalized advisory result, evidence rules, and authority separation. `captainhuke-dev/llm-council` is the first verified Thin Council Provider Adapter profile; its FastAPI/OpenRouter runtime remains external and optional. TASK-024 adds no provider runtime code, no MCP server, no OpenRouter client, no `MEETING-*` Stable-ID family, and no new semantic slot.

**Tech Stack:** Markdown/YAML governance sources, Python structural verification scripts used only as test runners, Git; verified external provider snapshot via GitHub/API evidence.

**Spec:** `docs/superpowers/specs/2026-08-29-task024-meeting-llm-council-design.md`

## Global Constraints

- Framework target remains `1.8.0`; Project Source Schema remains `1.0.0`; release format remains `3` unless implementation proves an incompatible schema change and governance explicitly reclassifies it.
- Canonical Framework distribution root is `Framework-Source/`; do not add new current references to `managing-project-source/` except historical/migration context.
- Registered command display form is exactly `[Meeting]`; literal brackets are required and registered-name matching inside brackets is case-insensitive.
- Council output is advisory only: `Council Recommendation ≠ User Approval ≠ AUTH-* ≠ DEC-* ≠ REQ-* change ≠ Project mutation permission`.
- Do not create `MEETING-*`, a new semantic slot, a new authorization family, or a provider-specific Project authority home.
- The user-supplied `[Meeting]` question is the Meeting input. Additional Project context is minimum-necessary and requires applicable outbound-disclosure authority; `[Goal]`/`ENV-*` authority does not imply external disclosure authority.
- Never persist or transmit actual secret values merely because they are relevant to a Meeting. `SECRET-*` references are not value-disclosure permission.
- Material Meeting evidence uses existing `EVD-*` / source-native evidence references; llm-council `data/conversations/*.json` never becomes canonical Project truth.
- Provider execution states `COMPLETE | PARTIAL | FAILED | UNAVAILABLE` are Meeting presentation/workflow labels only, not Project lifecycle families.
- Partial participation, Stage-2 degradation, Chairman failure, provider/auth/network errors, and ranking-parse degradation must remain distinguishable; never fabricate consensus.
- Verified provider baseline at design capture: `captainhuke-dev/llm-council`, default branch `master`, commit `92e1fccb1bdcf1bab7221aa9ed90f9dc72529131`, tree `221d8afb6eca87537282d509971c505119390e0b`; parent `karpathy/llm-council` master matched that commit at capture.
- Verified provider interfaces: FastAPI; `POST /api/conversations`; `POST /api/conversations/{conversation_id}/message`; optional SSE `/message/stream`; synchronous result contains `stage1`, `stage2`, `stage3`, `metadata`.
- Verified provider orchestration: Stage 1 independent responses → Stage 2 anonymized peer review/ranking → Stage 3 Chairman synthesis; provider transport is OpenRouter; conversation storage is JSON under `data/conversations/`.
- Official ChatGPT/Claude shared marker bodies remain byte-identical and each launcher remains `<=4,500` Unicode characters.
- Historical amendments/evidence outside selected current mutable release surfaces remain unchanged.
- `commit ≠ push`; TASK-024 does not imply publication authority.

---

### Task 1: Re-verify provider prerequisite and add RED `[Meeting]` scenarios 212–227

**Files:**
- Read: `docs/superpowers/PROJECT-TASKS.md`
- Read: `docs/superpowers/specs/2026-08-29-task024-meeting-llm-council-design.md`
- Read: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/tests/pressure-scenarios.md`

**Interfaces:**
- Consumes: approved written TASK-024 spec and verified provider profile.
- Produces: RED semantic acceptance contract for all later TASK-024 tasks.

- [ ] **Step 1: Fresh-check Project/TASK-024 state and Git base**

Run:

```bash
git status --short --branch
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

Required state: active Project Source routes TASK-024; written spec is approved; current distribution is `Framework-Source/`; working-tree state is understood before mutation.

- [ ] **Step 2: Fresh-check llm-council provider profile**

Read the current fork repository metadata/branch and the files that own the verified interface:

```text
captainhuke-dev/llm-council repository metadata
master branch HEAD/tree
README.md
backend/main.py
backend/council.py
backend/config.py
backend/openrouter.py
backend/storage.py
```

If the fork materially diverges from the approved provider contract, stop TASK-024 implementation mutation and route provider-profile/design reconciliation. Do not guess compatibility.

- [ ] **Step 3: Append exactly scenarios 212–227**

Use the existing `Prompt / Temptation / Pass / Fail / GREEN expectation` format:

```text
212 Meeting Brackets Required
213 Meeting Matching Is Case-Insensitive
214 Explicit Meeting Input Is The Default Outbound Payload
215 Meeting Cannot Auto-Disclose Whole Project
216 Meeting Never Sends Secret Values By Default
217 Council Recommendation Is Advisory Only
218 Council Majority Is Not A Project Decision
219 Partial Stage-1 Participation Is Surfaced
220 Stage-2 Failure Leaves Peer Ranking Incomplete
221 Chairman Failure Does Not Fabricate Consensus
222 Provider/Auth/Network Failure Is Not Council Disagreement
223 Provider Interface Drift Fails Closed
224 Material Meeting Evidence Uses EVD Not Provider JSON Authority
225 Goal Or ENV Does Not Imply Meeting Disclosure Authority
226 Brownfield Upgrade Does Not Auto-Create Meeting State
227 Provider Runtime Is Optional To Governance Semantics
```

Each PASS statement must encode the exact corresponding spec rule; FAIL must describe the overreach; GREEN expectation must name the protected invariant.

- [ ] **Step 4: Verify scenario numbering and RED state**

Run a Python structural check equivalent to:

```python
from pathlib import Path
import re

p = Path('Framework-Source/tests/pressure-scenarios.md')
t = p.read_text(encoding='utf-8')
nums = [int(x) for x in re.findall(r'^## Scenario (\d+) —', t, re.M)]
assert nums == list(range(1, 228))
assert len(nums) == len(set(nums))

required_titles = {
    212: 'Meeting Brackets Required',
    213: 'Meeting Matching Is Case-Insensitive',
    214: 'Explicit Meeting Input Is The Default Outbound Payload',
    215: 'Meeting Cannot Auto-Disclose Whole Project',
    216: 'Meeting Never Sends Secret Values By Default',
    217: 'Council Recommendation Is Advisory Only',
    218: 'Council Majority Is Not A Project Decision',
    219: 'Partial Stage-1 Participation Is Surfaced',
    220: 'Stage-2 Failure Leaves Peer Ranking Incomplete',
    221: 'Chairman Failure Does Not Fabricate Consensus',
    222: 'Provider/Auth/Network Failure Is Not Council Disagreement',
    223: 'Provider Interface Drift Fails Closed',
    224: 'Material Meeting Evidence Uses EVD Not Provider JSON Authority',
    225: 'Goal Or ENV Does Not Imply Meeting Disclosure Authority',
    226: 'Brownfield Upgrade Does Not Auto-Create Meeting State',
    227: 'Provider Runtime Is Optional To Governance Semantics',
}
for n, title in required_titles.items():
    assert f'## Scenario {n} — {title}' in t

core = Path('Framework-Source/references/core-governance-rules.md').read_text(encoding='utf-8')
skill = Path('Framework-Source/SKILL.md').read_text(encoding='utf-8')
assert '[Meeting] : ' not in core or '[Meeting] : ' not in skill
```

Expected: numbering checks PASS and the final RED assertion confirms current normative surfaces are not yet fully implemented.

- [ ] **Step 5: Mark TASK-024 implementation `IN_PROGRESS` and commit RED contract**

Update Task Registry only enough to record `IN_PROGRESS`, provider prerequisite freshness, scenario range `212–227`, and exact next action = normative contract.

```bash
git add Framework-Source/tests/pressure-scenarios.md docs/superpowers/PROJECT-TASKS.md
git commit -m "test: define Meeting council pressure scenarios"
```

---

### Task 2: Add TASK-024 normative amendment and `[Meeting]` command contract

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260829-task024.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`

**Interfaces:**
- Consumes: scenarios 212–227 and approved spec.
- Produces: canonical `[Meeting]` semantics used by starters, launchers, README, migration guidance, and verification.

- [ ] **Step 1: Create TASK-024 Framework amendment**

Header:

```yaml
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.8.0"
project_source_framework_version: "1.8.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_APPROVED_WRITTEN_SPEC_2026-08-29"
compatibility: "BACKWARD_COMPATIBLE_ADVISORY_MEETING_COMMAND"
```

The amendment must normatively contain:

```text
[Meeting] bracket/case rules
Thin Council Provider Adapter separation
verified provider snapshot/interface as provider profile evidence, not immutable Framework truth
explicit Meeting question = default outbound payload
additional Project context = minimum necessary + applicable disclosure authority
secret-value prohibition
normalized sections: independent views / agreement / disagreement / blind spots / peer signal / synthesis / recommendation / limitations
Council/majority/Chairman output = advisory only
no MEETING-* family / no new slot
material persistence = EVD-* / source-native evidence reference
llm-council JSON storage != Project authority
COMPLETE | PARTIAL | FAILED | UNAVAILABLE as Meeting labels only
Stage 1/2/3 partial-failure truth
provider/auth/network failure != substantive disagreement
Goal/ENV authority != outbound disclosure authority
Brownfield no-auto-Meeting
provider runtime installation/credentials remain optional/applicability-driven
```

- [ ] **Step 2: Point release descriptor to TASK-024 amendment**

Keep:

```yaml
framework_version: "1.8.0"
schema_version: "1.0.0"
release_format_version: 3
```

Change only:

```yaml
latest_framework_amendment: "references/framework-governance-amendment-260829-task024.md"
```

Preserve TASK-038 distribution-root and TASK-039 `[Goal]` semantics.

- [ ] **Step 3: Register `[Meeting]` in Core Governance**

Canonical help line:

```text
[Meeting] : convene a multi-model advisory council for a question using minimum authorized context; results are evidence/advice, never Project authority
```

Core Governance must explicitly preserve:

```text
Council Recommendation ≠ User Approval ≠ AUTH-* ≠ DEC-* ≠ REQ-* change ≠ Project mutation permission
```

It must define context minimization/disclosure, provider/runtime separation, normalized result semantics, partial failure labels, evidence persistence, Goal/ENV interaction, and Brownfield behavior.

- [ ] **Step 4: Add operational workflow to `SKILL.md`**

Required workflow:

```text
[Meeting] invocation
→ resolve bracketed command + question
→ treat explicit question as default outbound payload
→ identify any additional Project context needed
→ classify/minimize/authorize outbound context; remove secret values
→ fresh-resolve Meeting-capable provider profile/availability
→ execute provider stages when runtime capability exists
→ normalize COMPLETE/PARTIAL/FAILED/UNAVAILABLE result
→ preserve disagreement/limitations/provider failures
→ present advisory result
→ persist EVD-* only when materially used by governed Project truth
→ route any adopted recommendation through normal owning governance
```

No runtime/API client implementation is added to ProjectFramework.

- [ ] **Step 5: Run focused normative checks**

Assert in current amendment/Core/SKILL:

```text
[Meeting]
Thin Council Provider Adapter or equivalent provider separation
EVD-*
ADVISORY
minimum necessary context
secret-value prohibition
COMPLETE | PARTIAL | FAILED | UNAVAILABLE
SYNTHESIS_UNAVAILABLE or equivalent
no MEETING-* canonical home
provider JSON != Project authority
Goal/ENV disclosure separation
Brownfield no-auto-Meeting
```

Also assert latest amendment pointer is TASK-024 and release identity remains `1.8.0 / 1.0.0 / format 3`.

- [ ] **Step 6: Commit normative contract**

```bash
git add Framework-Source/FRAMEWORK-RELEASE.yaml Framework-Source/references/framework-governance-amendment-260829-task024.md Framework-Source/references/core-governance-rules.md Framework-Source/SKILL.md
git commit -m "docs: define Meeting council command contract"
```

---

### Task 3: Propagate Meeting semantics to maintained Project Source starters

**Files:**
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: `Framework-Source/templates/project-source-mockup/13-Evidence-Registry.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/README.md`

**Interfaces:**
- Consumes: canonical TASK-024 normative contract.
- Produces: starter guidance for command discovery and material Meeting evidence without creating default Meeting state.

- [ ] **Step 1: Add `[Meeting]` to root template command registry**

Use the exact Core Governance help line. Root template must state that invoking `[Meeting]` grants no automatic `AUTH-*`, `DEC-*`, `REQ-*`, mutation, or whole-Project disclosure authority.

- [ ] **Step 2: Extend core skeleton Evidence Registry guidance**

Add a bounded Meeting evidence recipe under `13 Evidence Registry`:

```text
Evidence Type: EXTERNAL_AI_COUNCIL / ADVISORY
Meeting Question
Context Scope / Disclosure Basis
Provider/Profile + observed version when material
Participating models / Chairman when reported
Stage completeness
Independent views/disagreement/synthesis bounded summary or source-native pointer
Provider/runtime failures
Supports
Epistemic Status
Advisory-only notice
```

Do not define a new Stable-ID family.

- [ ] **Step 3: Extend mockup `13` Evidence Registry**

Add the same field vocabulary as an optional `EVD-*` Meeting evidence specialization. Explicitly say transient exploratory Meetings need no synthetic evidence record and provider JSON is never canonical Project history.

- [ ] **Step 4: Update mockup README**

Add Framework `1.8.0` `[Meeting]` semantics: command available, `13` owns material advisory evidence, no `MEETING-*`, no automatic provider runtime/credentials/conversation during GREENFIELD.

- [ ] **Step 5: Run starter consistency checks**

Assert:

```text
all maintained starter stamps remain Framework 1.8.0 / Schema 1.0.0
[Meeting] appears in root command registry
13 skeleton/mockup uses EVD-* advisory specialization
no MEETING-* canonical family
18–19 remain RESERVED
no starter fabricates active Meeting/conversation/provider credentials/disclosure authority
```

- [ ] **Step 6: Commit starter propagation**

```bash
git add Framework-Source/templates
git commit -m "docs: propagate Meeting advisory semantics to starters"
```

---

### Task 4: Update README, migration notes, and compact platform launchers

**Files:**
- Modify: `README.md`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md`
- Modify: `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md`

**Interfaces:**
- Consumes: normative and starter Meeting semantics.
- Produces: user-facing command discovery, Brownfield guidance, and compact vendor adapters.

- [ ] **Step 1: Add README `[Meeting]` summary**

Plain-language requirements:

```text
[Meeting] asks a multi-model advisory council.
The explicit question is the default outbound payload.
Extra Project context is minimized and separately disclosure-authorized.
Results preserve individual views/disagreement/peer signal/synthesis/limitations.
Council output is advice/evidence, never automatic Decision/approval/mutation authority.
Material use may be recorded as EVD-*.
```

Add `[Meeting]` to the day-to-day registered-command discovery line without removing `[Goal]` or existing commands.

- [ ] **Step 2: Extend Framework 1.8.0 migration notes**

State explicitly:

```text
latest amendment = TASK-024 after implementation
Brownfield does not synthesize Meetings from prior AI transcripts/backlog/Handoff/EVD
provider runtime installation is not required merely to adopt governance semantics
provider JSON storage is not Project Source
existing external-AI/evidence records are preserved
additional outbound Project context remains disclosure-governed
no MEETING-* migration exists
```

- [ ] **Step 3: Compact shared launcher command/advisory rule**

Add a concise rule equivalent to:

```text
[Meeting] sends the explicit question to a verified advisory council; extra Project context is minimum/authorized, secrets never leak; output/majority/Chairman are advisory only and material use persists via EVD-*; provider/runtime failures remain explicit; Goal/ENV does not imply disclosure authority.
```

Required commands retained:

```text
[Project Status]
[Project Path]
[Project Upgrade]
[Session Envelope]
[Goal]
[Meeting]
```

- [ ] **Step 4: Verify launcher parity and size**

Run Python to extract `PROJECTFRAMEWORK-SHARED-CONTRACT:START/END`, assert byte-identical marker bodies and each full file length `<=4500` Unicode characters. Assert mandatory response-close labels remain exactly once in shared semantics.

- [ ] **Step 5: Commit user-facing propagation**

```bash
git add README.md Framework-Source/MIGRATION-NOTES.md Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md
git commit -m "docs: expose Meeting council command"
```

---

### Task 5: Make scenarios 212–227 GREEN and run TASK-024 affected verification

**Files:**
- Verify: all TASK-024 surfaces from Tasks 1–4
- Modify: only the canonical owner of a failing assertion, then required derived surfaces

**Interfaces:**
- Consumes: implemented TASK-024 documentation/governance candidate.
- Produces: affected verification evidence sufficient for final release verification.

- [ ] **Step 1: Run scenario semantic assertions**

Verify each of scenarios `212–227` maps to current normative/starter/user-facing semantics.

- [ ] **Step 2: Run repository-wide TASK-024 structural verifier**

Minimum assertions:

```text
scenarios exactly 1–227 contiguous/unique
Framework 1.8.0 / Schema 1.0.0 / format 3
latest amendment = task024
[Meeting] present on all required current surfaces
brackets required / case-insensitive matching
no MEETING-* canonical family or new semantic slot
Council output advisory-only on amendment/Core/SKILL/root/README/launchers
explicit question vs additional-context disclosure boundary aligned
minimum context + secret prohibition aligned
normalized result sections aligned
COMPLETE/PARTIAL/FAILED/UNAVAILABLE aligned
Chairman failure cannot fabricate consensus
provider/auth/network failure distinct from disagreement
provider profile/storage authority boundary aligned
EVD-* material persistence aligned
Goal/ENV disclosure separation aligned
Brownfield no-auto-Meeting aligned
provider runtime optional aligned
launchers byte-identical and <=4500
historical TASK-038/TASK-039 amendments/evidence unchanged
git diff --check PASS
```

- [ ] **Step 3: Fix root cause only**

Do not weaken pressure scenarios to fit incorrect behavior. Modify the owning normative surface first, then propagate only required derived copies.

- [ ] **Step 4: Re-run affected verification to PASS**

Record exact pass count, launcher lengths, scenario range, provider snapshot status, and candidate working-tree state.

- [ ] **Step 5: Commit only if verification fixes changed tracked files**

```bash
git add -u
git commit -m "fix: align Meeting advisory command contract"
```

Skip this commit if no tracked verification fix is required.

---

### Task 6: Run final RELEASE_FULL and record TASK-024 completion evidence

**Files:**
- Create: `docs/superpowers/evidence/2026-08-29-task-024-meeting-llm-council-release-full.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Revise/promote as applicable: active Project Source `01`, `03`, `09`, `10`, `13`, `14`, `15`
- Update: `PROJECT-BOOTSTRAP.md` only if active routed revision filenames change

**Interfaces:**
- Consumes: unchanged TASK-024 candidate with AFFECTED PASS.
- Produces: durable TASK-024 completion evidence and the next exact roadmap continuation; no publication claim without observed push.

- [ ] **Step 1: Freeze candidate identity**

Run:

```bash
git status --short --branch
git rev-parse HEAD
git rev-parse HEAD^{tree}
git rev-parse HEAD:Framework-Source
```

Working tree must be clean before declaring the final release-verification candidate.

- [ ] **Step 2: Run one final `RELEASE_FULL` on the unchanged candidate**

The verifier must include scenarios `1–227`, release/amendment chain, Core/SKILL, starters, README/migration notes, launchers, TASK-024 lifecycle state, advisory/disclosure/secret/provider boundaries, historical-integrity checks, and `git diff --check`.

- [ ] **Step 3: Write TASK-024 release evidence**

Record at minimum:

```text
TASK-024 scope
written design/spec + implementation-plan paths
provider snapshot repository/branch/commit/tree and freshness observation
candidate commit/tree + Framework-Source tree
AFFECTED result
RELEASE_FULL result
scenario range 1–227
launcher sizes + shared-body parity
Meeting advisory-authority invariant
input/context disclosure boundary
secret prohibition
no MEETING-* family/new slot
partial/provider/Chairman failure verification
EVD-* persistence/provider-JSON non-authority verification
Goal/ENV disclosure separation
historical-integrity result
working-tree state
publication = NOT_PUSHED unless fresh evidence proves otherwise
```

- [ ] **Step 4: Reconcile TASK-024 Task Registry**

Set `TASK-024` to `DONE` only after required verification and a committed release-evidence checkpoint exist. Record design, plan, implementation commits, provider snapshot, candidate identity, verification results, evidence path/commit, and publication state separately.

- [ ] **Step 5: Refresh Project Source continuation**

Use normal revision/validate/promote/supersede/archive flow. Persist only concise completion/current-state pointers and evidence references; do not copy the full provider conversation or full amendment payload. Do not create `MEETING-*`, `AUTH-*`, or an active Meeting solely because TASK-024 was implemented.

- [ ] **Step 6: Commit completion lifecycle metadata**

Recommended two-checkpoint order:

```text
A. commit release evidence first so completion metadata can reference a real evidence commit
B. revise/promote Project Source + Task Registry DONE and commit final lifecycle reconciliation
```

Suggested messages:

```bash
git commit -m "docs: record Meeting council release verification"
git commit -m "docs: complete Meeting council lifecycle"
```

- [ ] **Step 7: Postflight**

Fresh-observe local HEAD, working tree, and `origin/main`. Do not claim publication from commit existence. Determine the next roadmap action from current Task Registry/Project Source rather than assuming task-number order.
