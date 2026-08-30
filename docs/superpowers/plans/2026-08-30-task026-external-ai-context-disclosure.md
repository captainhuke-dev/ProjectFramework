# TASK-026 External AI Context & Disclosure Governance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement Framework `1.8.0` External AI Context & Disclosure Governance as a documentation/governance contract that classifies outbound Project context, separates disclosure eligibility from authority, minimizes/redacts context, and fails closed without adding a runtime disclosure system.

**Architecture:** Use the approved Compositional Disclosure Boundary. Reuse existing `AUTH-*` for standing disclosure authority, exact User Explicit Instruction for bounded one-off disclosure, `SECRET-*` for metadata/reference only, and `EVD-*` for material evidence. Canonical disclosure classes are `EXTERNAL_OK | EXTERNAL_REVIEW | DO_NOT_DISCLOSE | UNCLASSIFIED`; provider/tool eligibility is independently resolved as `ELIGIBLE | LIMITED | INELIGIBLE | VERIFICATION_REQUIRED`. No `DISC-*` Stable-ID family, semantic slot, mandatory per-object schema field, runtime redactor/router/proxy, secret manager, or DLP system is introduced.

**Tech Stack:** Markdown/YAML governance sources, Python standard-library structural checks used only as verification runners, Git.

**Spec:** `docs/superpowers/specs/2026-08-30-task026-external-ai-context-disclosure-design.md`

## Global Constraints

- Framework target remains `1.8.0`; Project Source Schema remains `1.0.0`; release format remains `3` unless implementation proves an incompatible schema requirement and governance explicitly reclassifies it.
- Canonical Framework distribution root is `Framework-Source/`; ProjectFramework's active local Project Source pin remains `1.7.0 / 1.0.0` unless separately upgraded.
- Canonical disclosure classes are exactly `EXTERNAL_OK | EXTERNAL_REVIEW | DO_NOT_DISCLOSE | UNCLASSIFIED`.
- Provider/tool eligibility labels are exactly `ELIGIBLE | LIMITED | INELIGIBLE | VERIFICATION_REQUIRED` and remain workflow labels, not lifecycle/authority families.
- `Classification ≠ Authorization`; `Provider Eligibility ≠ Authority`; `Disclosure Permission ≠ Decision/Mutation/Binding/Runtime/Publication/Risk authority`; `Secret Reference ≠ Secret Value Disclosure Permission`; `Unknown ≠ Safe`.
- Actual secret values are never persisted or transmitted merely because a runtime can access them; `SECRET-*` remains metadata/reference only.
- Standing disclosure permission reuses `AUTH-*`; exact User Explicit Instruction may authorize one bounded disclosure action without creating standing `AUTH-*`.
- Additional Project context sent by `[Meeting]` routes through this boundary; the explicit Meeting question remains the default action-specific input.
- Project Knowledge, OpenViking/cross-Project indexing, `[Goal]`, `ENV-*`, Tool/MCP access, model capability, repository/workspace access, and provider availability never bypass disclosure governance.
- Minimum-necessary context precedes transmission; mixed-sensitivity context is partitioned; uncertain redaction fails closed for the affected portion.
- Material disclosure evidence uses `EVD-*` or source-native pointers and must not duplicate full sensitive payload merely for audit.
- GREENFIELD creates no standing disclosure `AUTH-*`, provider credential, provider grant, automatic redaction runtime, or blanket `EXTERNAL_OK` classification.
- Brownfield never mass-classifies historical content as safe or synthesizes disclosure authority from prior AI use, credentials, chats, Meetings, Goals, or “continue” wording.
- Official ChatGPT/Claude shared marker bodies remain byte-identical and each launcher remains `<=4,500` Unicode characters if modified.
- Historical completed amendments/evidence outside selected current mutable release surfaces remain unchanged.
- `commit ≠ push`; TASK-026 does not authorize remote publication.

---

### Task 1: Add RED External-AI disclosure pressure scenarios 228–245

**Files:**
- Read: `docs/superpowers/PROJECT-TASKS.md`
- Read: `docs/superpowers/specs/2026-08-30-task026-external-ai-context-disclosure-design.md`
- Modify: `Framework-Source/tests/pressure-scenarios.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`

**Interfaces:**
- Consumes: approved written TASK-026 spec.
- Produces: executable semantic acceptance contract for Tasks 2–5.

- [ ] **Step 1: Fresh-check Project/Git state**

Run:

```bash
git status --short --branch
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

Required: current Project Source routes TASK-026; written spec is approved; working-tree state is understood; no publication is inferred from local commits.

- [ ] **Step 2: Append exactly scenarios 228–245**

Use the existing `Prompt / Temptation / Pass / Fail / GREEN expectation` format and these exact titles:

```text
228 Unclassified Project Context Fails Closed
229 Secret Value Never Becomes AI Context
230 Secret Reference Is Not Disclosure Permission
231 Generic Goal Does Not Grant AI Disclosure
232 Exact One-Off Disclosure Is Action Scoped
233 Standing Disclosure AUTH Is Provider Purpose And Scope Bound
234 Provider Mismatch Invalidates Disclosure Basis
235 Provider Policy Unknown Fails Closed
236 Mixed Sensitivity Context Is Partitioned
237 Uncertain Redaction Fails Closed
238 Whole Repository Convenience Dump Is Rejected
239 Meeting Extra Context Uses Disclosure Boundary
240 Project Knowledge External Processing Uses Disclosure Boundary
241 OpenViking Cannot Export Another Project By Relation Alone
242 Disclosure Evidence Must Not Duplicate Sensitive Payload
243 Brownfield Does Not Auto-Classify Historical Content Safe
244 Classification Does Not Grant Authorization
245 Provider Eligibility Does Not Grant Project Authority
```

Each PASS statement must encode the exact matching spec invariant. Do not introduce `DISC-*`.

- [ ] **Step 3: Verify RED contract**

Run a structural check asserting:

```python
nums == list(range(1, 246))
last 18 titles == exact 228–245 title map
all scenario numbers unique
current Core/SKILL do not yet fully implement canonical TASK-026 class/provider vocabulary
```

Expected: numbering/title checks PASS; current normative implementation remains intentionally RED.

- [ ] **Step 4: Mark TASK-026 implementation `IN_PROGRESS`**

Task Registry records:

```text
Status: IN_PROGRESS
Plan State: IMPLEMENTATION_PLAN_EXECUTING / INLINE_CONTINUOUS_EXECUTION_APPROVED
Implementation Scenario Contract: 228–245; framework-wide 1–245 contiguous/unique
Exact Next Step: Task 2 normative contract
```

- [ ] **Step 5: Verify and commit RED checkpoint**

Run `git diff --check`, stage only pressure scenarios + Task Registry, then:

```bash
git commit -m "test: define external AI disclosure pressure scenarios"
```

---

### Task 2: Add TASK-026 normative disclosure contract

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260830-task026.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`

**Interfaces:**
- Consumes: RED scenarios 228–245 and approved spec.
- Produces: canonical classification/authorization/provider/minimization/redaction/evidence semantics for all derived surfaces.

- [ ] **Step 1: Create TASK-026 Framework amendment**

Header:

```yaml
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.8.0"
project_source_framework_version: "1.8.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_APPROVED_WRITTEN_SPEC_2026-08-30"
compatibility: "BACKWARD_COMPATIBLE_EXTERNAL_AI_DISCLOSURE_GOVERNANCE"
```

Normative body must include:

```text
EXTERNAL_OK | EXTERNAL_REVIEW | DO_NOT_DISCLOSE | UNCLASSIFIED
ELIGIBLE | LIMITED | INELIGIBLE | VERIFICATION_REQUIRED
Classification ≠ Authorization
Provider Eligibility ≠ Authority
standing disclosure permission = AUTH-*; exact one-off instruction remains action scoped
actual secret values effectively DO_NOT_DISCLOSE; SECRET-* reference != value permission
minimum-necessary context order
partition mixed-sensitivity context
redaction/transformation adequacy rule; uncertainty fails closed
provider identity/policy mismatch/freshness behavior
EVD-* material disclosure evidence without duplicate sensitive payload
Meeting explicit question vs extra Project context routing
Project Knowledge/OpenViking/Goal/ENV/Tool/Model boundaries
GREENFIELD no blanket grants/classification/provider/runtime
Brownfield no retrospective safe classification or synthetic AUTH
no DISC-* family/slot/schema field/runtime enforcement
```

- [ ] **Step 2: Point release descriptor to TASK-026 amendment**

Keep:

```yaml
framework_version: "1.8.0"
schema_version: "1.0.0"
release_format_version: 3
```

Change only `latest_framework_amendment` to `references/framework-governance-amendment-260830-task026.md`.

- [ ] **Step 3: Add Core Governance section**

Core Governance must define the compositional boundary, exact vocabularies, default/use-time classification rules, standing/action-specific authority, provider eligibility, outbound decision flow, minimization/redaction/mixed-context behavior, evidence, consumer integration, fail-closed behavior, and no-runtime/non-family scope.

Preserve this invariant verbatim:

```text
Disclosure Permission ≠ Decision Authority ≠ Mutation Authority ≠ Binding Authority ≠ Runtime Authority
```

- [ ] **Step 4: Add operational `SKILL.md` workflow**

Required operational sequence:

```text
external-AI consumer requests context
→ identify purpose + provider/tool
→ identify candidate sources
→ classify each portion
→ remove secret/DO_NOT_DISCLOSE material
→ minimize/redact
→ resolve provider eligibility
→ resolve AUTH-* or exact one-off basis
→ partition mixed sensitivity
→ send authorized eligible subset only
→ surface blocked/omitted portions when material
→ persist EVD-* only when governance-relevant
```

No runtime interception/redactor/router code is added.

- [ ] **Step 5: Run focused normative checks**

Assert release identity and latest amendment plus all canonical classes, provider states, authority separations, secret boundary, mixed-context partition, redaction uncertainty, EVD behavior, consumer boundaries, Brownfield/GREENFIELD rules, and no `DISC-*` canonical family.

- [ ] **Step 6: Commit normative contract**

```bash
git add Framework-Source/FRAMEWORK-RELEASE.yaml Framework-Source/references/framework-governance-amendment-260830-task026.md Framework-Source/references/core-governance-rules.md Framework-Source/SKILL.md
git commit -m "docs: define external AI disclosure contract"
```

---

### Task 3: Propagate disclosure semantics to maintained Project Source starters

**Files:**
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: `Framework-Source/templates/project-source-mockup/12-Authorization-Registry.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/13-Evidence-Registry.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/17-Secret-Reference-Registry.template.md`
- Modify: `Framework-Source/templates/project-source-mockup/README.md`

**Interfaces:**
- Consumes: TASK-026 normative contract.
- Produces: starter guidance that can represent disclosure authority/evidence/secret boundaries without fabricating grants or classifications.

- [ ] **Step 1: Add root-template disclosure boundary summary**

Include exact class vocabulary and preserve:

```text
Classification ≠ Authorization
Disclosure Permission ≠ Project Mutation Permission
```

State that initial Project creation does not create standing disclosure authority, provider grants, credentials, or blanket safe classifications.

- [ ] **Step 2: Extend `12 Authorization Registry` guidance**

Add disclosure-specific `AUTH-*` fields:

```text
Consumer / Grantee
Provider / Tool / Provider Class
Allowed Content/Source Scope
Allowed Disclosure Classes
Purpose
Minimum-context / Redaction Conditions
Forbidden Content / Effects
Start
Expiry / Termination / Revocation
Risk Ceiling when applicable
Evidence / Approval Reference
Status
```

Clarify exact one-off disclosure does not require synthetic standing `AUTH-*` and standing authority is provider/purpose/content scoped.

- [ ] **Step 3: Extend `13 Evidence Registry` guidance**

Add optional material disclosure evidence specialization:

```text
Evidence Type: EXTERNAL_AI_DISCLOSURE / ADVISORY_CONTEXT
Consumer / Workflow
Purpose
Provider / Tool
Provider Eligibility State / Evidence
Source Pointers / Bounded Context Scope
Disclosure Classes
Authorization Basis
Minimization / Redaction Performed
Blocked/Omitted Portions when material
Result/Artifact Pointer
Epistemic Status
```

Explicitly prohibit storing full sensitive payload merely for evidence.

- [ ] **Step 4: Extend `17 Secret Reference Registry` guidance**

State actual secret values are never disclosure payload/evidence; `SECRET-*` metadata does not authorize value disclosure; secret-bearing source text must be excluded/redacted before external AI use.

- [ ] **Step 5: Update mockup README**

Document Framework 1.8.0 TASK-026 semantics and GREENFIELD no-auto-grant/classification/runtime behavior. Do not create a new physical registry/family.

- [ ] **Step 6: Run starter consistency checks**

Assert all maintained starter stamps remain `1.8.0 / 1.0.0`, `18–19` remain RESERVED, no `DISC-*` family/slot, no starter creates provider credentials/standing disclosure AUTH/blanket EXTERNAL_OK, and 12/13/17 field semantics align.

- [ ] **Step 7: Commit starter propagation**

```bash
git add Framework-Source/templates
git commit -m "docs: propagate external AI disclosure semantics to starters"
```

---

### Task 4: Update README, migration notes, and compact platform launchers

**Files:**
- Modify: `README.md`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md` only if size/parity can be maintained
- Modify: `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md` only if size/parity can be maintained

**Interfaces:**
- Consumes: normative + starter TASK-026 semantics.
- Produces: user-facing disclosure behavior and Brownfield upgrade guidance.

- [ ] **Step 1: Add README disclosure summary**

Plain-language requirements:

```text
External AI uses the smallest necessary context.
Unknown Project context is not automatically safe.
EXTERNAL_REVIEW needs bounded disclosure authority.
DO_NOT_DISCLOSE is excluded.
Provider eligibility is separate from authority.
Secret references never authorize secret values.
Disclosure permission never grants Project mutation/Decision authority.
```

- [ ] **Step 2: Extend 1.7.0→1.8.0 migration notes**

State:

```text
latest amendment becomes TASK-026
no historical mass classification
no synthetic disclosure AUTH from prior AI usage/credentials/chats/Meeting/Goal
existing AUTH/EVD/SECRET records are preserved
provider integrations must be reassessed prospectively when next used
no DISC-* migration
runtime redactor/router/credential setup not required for governance adoption
```

- [ ] **Step 3: Compact launchers only if feasible**

Shared semantic rule equivalent to:

```text
External AI context: minimum necessary; classify EXTERNAL_OK|EXTERNAL_REVIEW|DO_NOT_DISCLOSE|UNCLASSIFIED; unknown/restricted fails closed; provider eligibility + disclosure AUTH are separate; secrets never leak; Meeting extra context/Goal/ENV/tool access never bypass this boundary.
```

Preserve all registered commands, response-close tokens, marker parity, and `<=4,500` characters. If the rule cannot fit without dropping canonical behavior, leave launchers unchanged and document why in verification/evidence; launcher modification is conditional per approved spec.

- [ ] **Step 4: Verify user-facing surfaces**

Check README/migration semantics; if launchers changed, assert shared marker bodies byte-identical and full lengths `<=4500` plus all required commands/close labels.

- [ ] **Step 5: Commit user-facing propagation**

```bash
git add README.md Framework-Source/MIGRATION-NOTES.md Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md
git commit -m "docs: expose external AI disclosure governance"
```

Stage launcher files only when actually changed.

---

### Task 5: Make scenarios 228–245 GREEN and run TASK-026 AFFECTED verification

**Files:**
- Verify: all TASK-026 surfaces from Tasks 1–4
- Modify: only the canonical owner of a failing semantic assertion, then required derived surfaces

**Interfaces:**
- Consumes: implemented TASK-026 governance candidate.
- Produces: affected verification evidence sufficient for final release verification.

- [ ] **Step 1: Verify scenarios 228–245 semantically**

Map every scenario to current normative/derived surfaces; do not weaken scenario text to fit incorrect behavior.

- [ ] **Step 2: Run repository-wide TASK-026 structural verifier**

Minimum assertions:

```text
scenarios exactly 1–245 contiguous/unique
Framework 1.8.0 / Schema 1.0.0 / format 3
latest amendment = TASK-026
canonical classes exact
provider eligibility labels exact
Classification != Authorization
Provider Eligibility != Authority
UNCLASSIFIED automatic protected outbound fails closed
actual secret values prohibited; SECRET-* reference != permission
standing disclosure uses AUTH-*; exact one-off stays action scoped
provider/content/purpose scope alignment
minimum necessary before external send
mixed-sensitivity partition behavior
redaction uncertainty fails closed
Meeting extra context routes through boundary
Goal/ENV/tool/model/repo/provider availability do not imply disclosure
Project Knowledge/OpenViking source-Project boundary
EVD material evidence without sensitive payload duplication
GREENFIELD/Brownfield behavior
no DISC-* canonical family/slot
no runtime disclosure implementation
starter stamps + reserved slots aligned
README/migration aligned
launcher parity/size if modified
historical TASK-024/TASK-039 amendments/evidence unchanged
git diff --check PASS
working tree clean after checkpoint commits
```

- [ ] **Step 3: Fix root cause only**

If a failure is a verifier wording defect, fix verifier semantics only. If source behavior is wrong, fix the owning normative surface first and propagate only required derived copies.

- [ ] **Step 4: Re-run AFFECTED to PASS**

Record exact pass count, scenario range, launcher lengths/change status, and exact candidate identity.

- [ ] **Step 5: Commit only if verification fixes changed tracked files**

```bash
git add -u
git commit -m "fix: align external AI disclosure contract"
```

Skip if no tracked fix is needed.

---

### Task 6: Run final RELEASE_FULL and reconcile TASK-026 lifecycle

**Files:**
- Create: `docs/superpowers/evidence/2026-08-30-task-026-external-ai-context-disclosure-release-full.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Revise/promote as applicable: active Project Source `01`, `03`, `09`, `10`, `13`, `14`, `15`
- Update: `PROJECT-BOOTSTRAP.md` only when active routed revision filenames change

**Interfaces:**
- Consumes: clean unchanged TASK-026 candidate with AFFECTED PASS.
- Produces: durable release evidence, TASK-026 `DONE`, and exact next roadmap continuation without publication claim.

- [ ] **Step 1: Freeze candidate identity**

Run:

```bash
git status --short --branch
git rev-parse HEAD
git rev-parse HEAD^{tree}
git rev-parse HEAD:Framework-Source
git ls-remote origin refs/heads/main
```

Working tree must be clean and remote freshness recorded.

- [ ] **Step 2: Run one final `RELEASE_FULL`**

Cover scenarios `1–245`, release/amendment chain, Core/SKILL, 12/13/17 starter semantics, README/migration, launchers as applicable, no-family/no-runtime rules, consumer boundaries, historical integrity, Task lifecycle, and `git diff --check`.

- [ ] **Step 3: Write and commit release evidence**

Record:

```text
TASK-026 scope
AFFECTED result
RELEASE_FULL result
candidate HEAD/tree/Framework-Source tree
scenarios 1–245
launcher lengths/change status
canonical classes/provider eligibility labels
no DISC-* family/slot
no runtime disclosure implementation
ProjectFramework local pin 1.7.0 / Schema 1.0.0
publication NOT_PUSHED
```

Commit:

```bash
git add docs/superpowers/evidence/2026-08-30-task-026-external-ai-context-disclosure-release-full.md
git commit -m "docs: record external AI disclosure release verification"
```

- [ ] **Step 4: Reconcile Task Registry to `DONE`**

Only after evidence commit exists, record implementation commits, evidence path, exact verification counts, candidate identities, completion criteria, `Publication State: NOT_PUSHED`, and next roadmap action.

- [ ] **Step 5: Reconcile active Project Source through revision lifecycle**

Use current active revisions, not stale plan examples. Create the next monotonic revision only for materially changed slots, validate candidates, promote, archive superseded revisions, synchronize Index/Manifest/bootstrap pointers, and record completion `CHG-* / EVD-* / ACT-*` as applicable. Preserve local Framework pin `1.7.0 / 1.0.0`; do not fabricate a standing disclosure authorization for ProjectFramework.

- [ ] **Step 6: Commit final lifecycle checkpoint**

```bash
git add PROJECT-BOOTSTRAP.md Project-Source docs/superpowers/PROJECT-TASKS.md
git diff --cached --check
git commit -m "docs: complete external AI disclosure lifecycle"
```

- [ ] **Step 7: Fresh postflight**

Verify fresh HEAD, clean working tree, `origin/main`, ahead/behind, current bootstrap routing, TASK-026 `DONE`, and `NOT_PUSHED`. Do not push without separate explicit publication authorization.
