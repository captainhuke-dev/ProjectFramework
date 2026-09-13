# TASK-051 Risk-Tiered Feature Delivery Fast Path Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver ProjectFramework `1.17.0` with a deterministic risk-tiered Feature Delivery Fast Path that lets genuinely low-risk feature work reach durable Task completion quickly while preserving canonical `R0–R3`, authority/location gates, Task DONE evidence, release acceptance, integration freshness, and high-risk review/approval boundaries.

**Architecture:** Add `LOW | MEDIUM | HIGH` as a Derived Delivery Tier over existing `R0–R3`, blast radius, sensitive-surface flags, and uncertainty. Reuse existing `TASK_LOCAL_FAST`, `CHECKPOINT_INTEGRITY`, `RELEASE_FULL`, `INTEGRATION_GATE`, Goal/AUTH continuity, completion-commit, evidence-reuse, tool/capability/trust, and publication-state contracts; add only the missing deterministic classification, per-tier preflight/review/verification, one-session, recovery, parallelism, and direct Git/GitHub rules. No new Risk family, Stable-ID family, Registered Command, runtime service, scheduler, validator, CI/CD, or merge bot is introduced.

**Tech Stack:** Markdown, YAML, Git, Node.js scratch verification (`node.exe`); no Framework runtime/parser/daemon/router dependency.

**Spec:** `docs/superpowers/specs/2026-09-13-task051-risk-tiered-feature-delivery-fast-path-design.md`

**Plan State:** `SELF_REVIEWED / EXECUTION_AUTHORIZED_BY_OUT-019`

## Global Constraints

- Target Framework exactly `1.17.0`; Schema remains `1.0.0`; release format remains `3`.
- `LOW | MEDIUM | HIGH` is Derived Delivery Tier workflow vocabulary only; canonical Risk remains exactly `R0 READ_ONLY | R1 REVERSIBLE_LOCAL | R2 SHARED_STATE | R3 EXTERNAL_OR_IRREVERSIBLE`.
- Delivery tier may escalate but never lower Risk, AUTH, binding, trust, disclosure, secret, destructive, production, publication, or platform/tool gates.
- LOW required completion actions are R0/R1 only; R2 is never LOW; any R3 action is HIGH.
- Root/`FRAMEWORK-001`, Project Location Binding, bootstrap authority/routing, security/trust/disclosure/secret policy, schema/Stable-ID compatibility, production/deployment safety, cross-Project write authority, and delivery/review/verification-gate semantics are HIGH when their controlling semantics change.
- LOW independent review is `NOT_REQUIRED` by default; MEDIUM is `OPTIONAL` unless a defined trigger makes it `REQUIRED`; HIGH is `REQUIRED` absent an explicit governed waiver.
- Reviewer unavailability never becomes an implicit waiver.
- Task-level verification is tiered; `RELEASE_FULL` remains the release/equivalent semantic acceptance gate; `INTEGRATION_GATE` remains separate and re-resolves mutable target/Base Freshness/evidence validity before integration/publication.
- Material Git-backed Task `DONE` still requires affected/risk-appropriate verification plus observed durable completion commit; `WIP commit ≠ Task DONE`; `commit ≠ push`.
- One-session LOW delivery is an objective, not an SLA.
- Stable state-bound authority/location/governance evidence may be reused only while bound material assumptions remain unchanged; volatile Git state and applicable R2/R3 authority remain fresh-check obligations.
- Parallel mutation requires evidenced independence and final combined-candidate verification; HIGH mutation is serialized by default.
- Unknown potentially-applied external/non-idempotent result uses `RESULT_VERIFICATION_REQUIRED` before retry.
- Direct Git/GitHub repository-native operations are allowed only when identity, tool policy, authority, and platform gates permit; they never create push/merge/publication authority.
- MCP is not retained merely to represent nonexistent ProjectFramework application runtime/process/UI state.
- Optional `Project-Execution/` profiles are stricter overlays, not prerequisites for base Fast Path semantics.
- Registered command set remains exactly seven; TASK-042/TASK-043/TASK-045 response/finalization semantics remain intact.
- Historical amendments/specs/plans/evidence remain provenance and are not globally rewritten.
- Existing initialized Projects do not auto-adopt 1.17; adoption remains governed Direct-to-Latest `[Project Upgrade]`.
- ProjectFramework active `Project-Source/` and root `PROJECT-BOOTSTRAP.md` remain self-host pinned to Framework `1.16.0` during this local implementation. Canonical 1.17 self-host promotion is a later separately authorized post-merge operation.
- AUTH-019 authorizes local verified completion only. No push, PR, merge, tag, GitHub Release, Root/Binding mutation, external-AI disclosure, destructive worktree cleanup, runtime/daemon/router/watcher/CI/CD/validator/CLI, or secret-value persistence.

---

## File Structure Map

**Normative release and Fast Path contract**
- Create: `Framework-Source/references/framework-governance-amendment-260913-task051-feature-delivery-fast-path.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`

**Current user-facing / migration / starter propagation**
- Modify: `README.md`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: `Framework-Source/templates/project-source-mockup/README.md`
- Modify: all 22 maintained `Framework-Source/templates/project-source-mockup/*.template.md` files carrying `project_source_framework_version: "1.16.0"` to `1.17.0`
- Inspect only and preserve unless a concrete affected current-reference exists: `Framework-Source/templates/PROJECT-BOOTSTRAP.md`
- Inspect only; preserve thin bootstrap body unchanged: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md`, `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md`

**TDD / verification**
- Modify first: `Framework-Source/tests/pressure-scenarios.md`
- Scratch only outside candidate tree: `E:\GitHub\ProjectFramework\.git\task051_verify.js`

**Task / evidence / lifecycle**
- Modify at checkpoints: `docs/superpowers/PROJECT-TASKS.md`
- Create after final verification: `docs/superpowers/evidence/2026-09-13-task-051-risk-tiered-feature-delivery-fast-path-release-full.md`
- Promote current Project Source successors only for TASK-051 lifecycle/evidence; keep active `FRAMEWORK-001`/Bootstrap pin `1.16.0`

---

### Task 1: Establish TDD RED for the complete Fast Path contract

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`
- Create scratch only: `E:\GitHub\ProjectFramework\.git\task051_verify.js`

**Interfaces:**
- Consumes: approved TASK-051 spec; current Framework `1.16.0`; exact current scenario range `1–472`; existing `R0–R3`, progressive verification, Goal/AUTH, completion commit, Base Freshness, review/capability, and tool-policy contracts.
- Produces: scenarios `473–504` and one deterministic scratch verifier with modes `red`, `structural`, `affected`, and `release-full`.

- [ ] **Step 1: Append scenarios 473–504 before editing production contract files**

Use these exact scenario identities and acceptance intent:

```text
473 — Bounded reversible local change derives LOW
474 — Multi-surface R1 blast radius escalates to MEDIUM
475 — Sensitive authority semantics escalate R1 to HIGH
476 — R2 action is never LOW
477 — R3 action is always HIGH
478 — Uncertainty escalates rather than downgrades delivery tier
479 — LOW/MEDIUM/HIGH does not replace canonical R0–R3
480 — Stable preflight evidence is reusable while assumptions stay bound
481 — Volatile Git state is fresh-observed despite stable governance reuse
482 — R2/R3 authority is fresh-read immediately before applicable mutation
483 — LOW uses focused affected verification without Task-boundary RELEASE_FULL
484 — MEDIUM uses broader dependency/affected verification
485 — HIGH uses comprehensive affected/risk verification
486 — Release Candidate still requires RELEASE_FULL regardless of contributing Task tiers
487 — INTEGRATION_GATE remains separate from RELEASE_FULL
488 — LOW independent review is not required by default
489 — MEDIUM review trigger promotes independent review to REQUIRED
490 — HIGH reviewer unavailable is not an implicit waiver
491 — Explicit governed HIGH review waiver is bounded to exact scope/action
492 — One-session LOW avoids redundant governance rereads/checkpoints/prompts
493 — Bounded LOW existing-flow change does not require standalone spec/plan by Framework
494 — HIGH preserves Preview / explicit approval gates
495 — Non-Git execution failure does not invalidate unchanged Git evidence
496 — Unknown non-idempotent result requires RESULT_VERIFICATION_REQUIRED before retry
497 — Independent read/test verification may run in parallel
498 — Proven-disjoint LOW mutation may parallelize but combined candidate is reverified
499 — Overlapping or uncertain parallel mutation serializes
500 — HIGH mutation is serialized by default
501 — Direct Git/GitHub repository-native operation may be eligible under policy/authority
502 — MCP is not required solely for nonexistent runtime/process/UI state
503 — Direct Git/GitHub eligibility does not grant push/merge/publication authority
504 — Task DONE remains tier verification + observed completion commit and is distinct from publication
```

- [ ] **Step 2: Create the scratch verifier with four explicit modes**

Create `E:\GitHub\ProjectFramework\.git\task051_verify.js` with this interface:

```javascript
// Invocation:
//   node E:\GitHub\ProjectFramework\.git\task051_verify.js red E:\GitHub\ProjectFramework\.worktrees\task051-feature-delivery-fast-path
//   node E:\GitHub\ProjectFramework\.git\task051_verify.js structural E:\GitHub\ProjectFramework\.worktrees\task051-feature-delivery-fast-path
//   node E:\GitHub\ProjectFramework\.git\task051_verify.js affected E:\GitHub\ProjectFramework\.worktrees\task051-feature-delivery-fast-path
//   node E:\GitHub\ProjectFramework\.git\task051_verify.js release-full E:\GitHub\ProjectFramework\.worktrees\task051-feature-delivery-fast-path $candidateHead
//
// Required output prefix:
//   TASK051_RED
//   TASK051_STRUCTURAL
//   TASK051_AFFECTED
//   TASK051_RELEASE_FULL
//
// Exit non-zero on any failed required assertion except `red`, where the
// expected missing production contract must itself be proven.
```

The verifier must parse files as UTF-8 with Node `fs.readFileSync(..., 'utf8')`, never rely on Windows ANSI decoding, and assert at least these groups:

```text
BASELINE
- scenario numbering before append was 1–472 contiguous/unique
- after append scenarios are 1–504 contiguous/unique
- Schema remains 1.0.0
- release format remains 3
- registered commands remain exactly seven
- active Project Source/PROJECT-BOOTSTRAP remain self-host 1.16 during candidate work
- thin ChatGPT/Claude launcher bodies remain unchanged/byte-compatible with baseline
- no forbidden runtime/CI/router/validator artifact is added

NEW CONTRACT
- release 1.17.0 + latest TASK-051 amendment route
- Derived Delivery Tier exact vocabulary LOW | MEDIUM | HIGH
- canonical R0–R3 preserved
- escalate-only / uncertainty escalation
- HIGH sensitive-surface triggers
- common invariant preflight
- state-bound stable-evidence reuse + volatile fresh checks
- R2/R3 fresh authority preserved
- LOW / MEDIUM / HIGH review floors
- MEDIUM trigger list
- HIGH reviewer-unavailable ≠ waiver
- LOW / MEDIUM / HIGH verification floors
- Task acceptance ≠ RELEASE_FULL ≠ INTEGRATION_GATE
- one-session objective and artifact/persistence scaling
- checkpoint interruption/recovery + selective evidence invalidation
- RESULT_VERIFICATION_REQUIRED before retry
- safe parallelism + combined-candidate verification
- HIGH mutation serialization default
- direct Git/GitHub eligibility constraints
- MCP not required for nonexistent runtime state
- direct Git/GitHub ≠ authority
- completion commit + Task DONE distinction
- Brownfield no-auto-adopt
- no new Risk/Stable-ID/Registered-Command family
```

- [ ] **Step 3: Run RED mode before production changes**

Run:

```powershell
node E:\GitHub\ProjectFramework\.git\task051_verify.js red E:\GitHub\ProjectFramework\.worktrees\task051-feature-delivery-fast-path
```

Expected: `TASK051_RED ... PASS_EXPECTED_MISSING_CONTRACT` and exit `0`, proving scenarios `473–504` exist while the new 1.17 production markers are still absent. RED mode must fail if the production contract is already fully present or if baseline invariants are broken.

- [ ] **Step 4: Verify diff hygiene and commit RED scenarios**

Run:

```powershell
git diff --check
git diff -- Framework-Source/tests/pressure-scenarios.md
```

Expected: no diff-hygiene errors; only scenarios `473–504` are added to the pressure file.

Commit only the scenario file:

```powershell
git add -- Framework-Source/tests/pressure-scenarios.md
git commit -m "test(task051): add feature delivery fast-path pressure scenarios"
```

---

### Task 2: Implement the normative Framework 1.17 Fast Path contract

**Files:**
- Create: `Framework-Source/references/framework-governance-amendment-260913-task051-feature-delivery-fast-path.md`
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`

**Interfaces:**
- Consumes: scenarios `473–504`, TASK-051 written spec, current 1.16 progressive verification/Risk/Goal/tool/capability rules.
- Produces: canonical 1.17 release identity and the normative Fast Path contract used by all propagation surfaces.

- [ ] **Step 1: Bump release identity without changing Schema/format**

Edit `Framework-Source/FRAMEWORK-RELEASE.yaml` exactly:

```yaml
release_format_version: 3
framework_version: "1.17.0"
schema_version: "1.0.0"
```

Set:

```yaml
latest_framework_amendment: "references/framework-governance-amendment-260913-task051-feature-delivery-fast-path.md"
```

Do not change Direct-to-Latest `path_classes` or `final_release_full_per_unchanged_candidate: 1`.

- [ ] **Step 2: Create the TASK-051 amendment**

The new amendment must contain explicit normative sections for:

```text
1. Scope / release classification
2. Derived Delivery Tier definition
3. LOW / MEDIUM / HIGH classification table
4. Sensitive-surface HIGH escalation
5. Highest-tier outcome / anti-splitting rule
6. Common invariant preflight
7. State-bound preflight evidence reuse + invalidation
8. Per-tier authority/location preflight floor
9. Review policy and MEDIUM triggers
10. Review evidence validity / reviewer unavailable / governed waiver
11. Per-tier Task verification floor
12. Task acceptance vs RELEASE_FULL vs INTEGRATION_GATE
13. One-session delivery and design/plan/persistence scaling
14. Interruption/recovery and RESULT_VERIFICATION_REQUIRED
15. Parallelism and combined-candidate evidence
16. Direct Git/GitHub vs MCP boundary
17. Tool/capability/trust/disclosure overlays
18. Task DONE durability / publication separation
19. Brownfield/Greenfield adoption
20. No-runtime/no-new-family boundary
```

Use normative `MUST / MUST NOT / MAY / SHOULD` language matching the approved spec. The amendment must state that the stricter existing or Project-specific rule wins.

- [ ] **Step 3: Extend Core Governance adjacent to Progressive Verification**

In `Framework-Source/references/core-governance-rules.md`, add a dedicated **Risk-Tiered Feature Delivery Fast Path** subsection adjacent to `16.2 Progressive / Risk-Scoped Verification` so the reader sees:

```text
R0–R3 remains canonical Risk
→ derive LOW | MEDIUM | HIGH
→ apply common preflight/evidence reuse
→ apply tier review + verification floor
→ Task DONE completion checkpoint
→ RELEASE_FULL only at release/equivalent acceptance
→ INTEGRATION_GATE before applicable integration/publication
```

Core must include the HIGH sensitive-surface list, MEDIUM review triggers, recovery/parallelism constraints, and direct Git/GitHub boundary. Do not add a new Project Source object family.

- [ ] **Step 4: Extend SKILL operational behavior**

In `Framework-Source/SKILL.md`, directly after **Progressive Verification and Evidence Reuse**, add an operational section that tells an Agent exactly how to:

```text
1. run common invariant preflight once;
2. reuse still-valid stable evidence;
3. fresh-check volatile Git + R2/R3 prerequisites;
4. classify LOW/MEDIUM/HIGH;
5. execute the tier floor;
6. reclassify upward when scope/uncertainty grows;
7. checkpoint only when continuity needs durability;
8. finish Task DONE with completion commit;
9. stop at local DONE when publication authority is absent;
10. run INTEGRATION_GATE only when an authorized integration/publication action follows.
```

SKILL must explicitly say one-session LOW is an objective, not an SLA, and that bounded LOW work does not gain a Framework requirement for a standalone spec/plan when intent/acceptance are already sufficient. Higher-level tool/product design gates remain binding.

- [ ] **Step 5: Run normative-focused verifier**

Run:

```powershell
node E:\GitHub\ProjectFramework\.git\task051_verify.js structural E:\GitHub\ProjectFramework\.worktrees\task051-feature-delivery-fast-path
```

Expected at this checkpoint: normative/release checks pass; propagation/version-stamp checks may still fail and must be reported as the only remaining structural failures.

- [ ] **Step 6: Review normative diff and commit**

Run:

```powershell
git diff --check
git diff -- Framework-Source/FRAMEWORK-RELEASE.yaml Framework-Source/references/core-governance-rules.md Framework-Source/SKILL.md Framework-Source/references/framework-governance-amendment-260913-task051-feature-delivery-fast-path.md
```

Commit only those four paths:

```powershell
git add -- Framework-Source/FRAMEWORK-RELEASE.yaml Framework-Source/references/core-governance-rules.md Framework-Source/SKILL.md Framework-Source/references/framework-governance-amendment-260913-task051-feature-delivery-fast-path.md
git commit -m "feat(framework): define risk-tiered feature delivery fast path"
```

---

### Task 3: Propagate Framework 1.17 current guidance and maintained starters

**Files:**
- Modify: `README.md`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: `Framework-Source/templates/project-source-mockup/README.md`
- Modify: all 22 maintained `Framework-Source/templates/project-source-mockup/*.template.md` current Framework stamps
- Inspect unchanged: `Framework-Source/templates/PROJECT-BOOTSTRAP.md`
- Inspect unchanged: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md`
- Inspect unchanged: `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md`

**Interfaces:**
- Consumes: Task 2 normative contract.
- Produces: coherent user-facing/migration/starter distribution for Framework 1.17 without duplicating normative authority into thin adapters.

- [ ] **Step 1: Add root README current release summary**

Update **Current Release** to `1.17.0` and add a compact `Framework 1.17.0 Risk-Tiered Feature Delivery Fast Path` section that states:

```text
- LOW | MEDIUM | HIGH is derived workflow tier over R0–R3, not replacement Risk.
- LOW favors one-session focused verification + completion commit.
- MEDIUM broadens affected checks and conditionally requires independent review.
- HIGH preserves full sensitive-surface approval/review/verification obligations.
- RELEASE_FULL remains release/equivalent acceptance; INTEGRATION_GATE remains mutable-target integration gate.
- stable evidence reuse is state-bound; volatile/R2/R3 prerequisites are fresh checked.
- direct Git/GitHub may be repository-native when policy/authority allow; MCP is not a fake runtime requirement.
- no runtime/CI/bot/router/validator is introduced.
```

- [ ] **Step 2: Add the current `1.16.0 → 1.17.0` migration section**

Prepend a new current section to `Framework-Source/MIGRATION-NOTES.md` with:

```text
Affected distribution surfaces
- 1.17.0 / Schema 1.0.0 / format 3
- latest TASK-051 amendment
- Derived Delivery Tier and escalation semantics
- preflight evidence reuse / fresh-check rules
- review matrix
- verification boundary separation
- one-session/artifact/persistence scaling
- recovery/parallelism/direct Git/GitHub boundary
- no new files required in consuming Projects
- no auto-adoption by Brownfield Projects

Upgrade checklist
1. preserve local pin/current truth until governed promotion
2. preserve R0–R3 and authority/location gates
3. adopt LOW/MEDIUM/HIGH only as derived workflow classification
4. preserve stricter optional execution profiles
5. preserve release/integration gates and Task completion commit
6. do not synthesize publication authority
7. verify maintained starters/current guidance/scenarios 473–504
8. perform affected verification + final unchanged-candidate RELEASE_FULL for this Framework release
```

- [ ] **Step 3: Propagate normative summary to Framework templates**

Add concise current 1.17 Fast Path semantics to:

```text
Framework-Source/templates/00-project-source-framework.md
Framework-Source/templates/core-document-skeletons.md
Framework-Source/templates/project-source-mockup/README.md
```

The summary must preserve all classification/review/verification boundaries but remain shorter than Core/SKILL. Do not turn template summaries into a competing authority source.

- [ ] **Step 4: Stamp all 22 maintained starter templates to 1.17.0**

Replace only the maintained current stamp:

```text
project_source_framework_version: "1.16.0"
```

with:

```text
project_source_framework_version: "1.17.0"
```

in exactly these 22 files:

```text
00,01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,40,60,91,92
```

under `Framework-Source/templates/project-source-mockup/*.template.md`. Schema stamps remain `1.0.0`.

- [ ] **Step 5: Prove bootstrap/launcher non-changes**

Compare these files to `fc227f0` and keep them byte-identical unless a verifier demonstrates a concrete affected current reference:

```powershell
git diff fc227f0 -- Framework-Source/templates/PROJECT-BOOTSTRAP.md Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md
```

Expected: empty diff.

- [ ] **Step 6: Run structural GREEN**

Run:

```powershell
node E:\GitHub\ProjectFramework\.git\task051_verify.js structural E:\GitHub\ProjectFramework\.worktrees\task051-feature-delivery-fast-path
```

Expected: `TASK051_STRUCTURAL ... PASS`, including scenarios `1–504`, 22/22 starter stamps at 1.17.0, exact seven commands, unchanged thin launchers, and no forbidden runtime artifacts.

- [ ] **Step 7: Commit propagation**

Run `git diff --check`, inspect the exact diff, then stage only the files above and commit:

```powershell
git commit -m "docs(framework): propagate feature delivery fast-path contract"
```

---

### Task 4: Run required independent review and resolve findings before candidate freeze

**Files:**
- Review: approved spec + commits/diff from Tasks 1–3
- Modify only if findings require correction: affected Task 1–3 files
- Update: `docs/superpowers/PROJECT-TASKS.md` only if review state must be checkpointed before candidate freeze

**Interfaces:**
- Consumes: stable post-propagation candidate, approved spec, exact diff from branch base.
- Produces: `REVIEW_PASS` with no Critical/Important findings, or an explicit blocker/valid governed waiver record. Silent self-waiver is forbidden.

- [ ] **Step 1: Resolve reviewer eligibility before disclosure**

Use a reviewer distinct from the producing instance only if it is eligible under current authority/tool/disclosure/trust rules. AUTH-019 does **not** authorize external-AI/provider disclosure, so do not send repository/spec/diff to an external provider merely to satisfy this step.

If an eligible local/owned reviewer is available without external disclosure, provide only:

```text
approved spec path
branch base 7d7463b
current HEAD
branch diff base..HEAD
Framework-Source changed-file list
verification results so far
```

If no eligible independent reviewer exists, record `REVIEW_REQUIRED_BLOCKED`; do not freeze the candidate unless ACTOR-001 supplies an explicit governed review waiver. Reviewer absence itself is never a waiver.

- [ ] **Step 2: Review against exact acceptance questions**

The reviewer must answer at least:

```text
1. Any path allowing LOW to include R2/R3 completion action?
2. Any path where LOW/MEDIUM/HIGH becomes parallel Risk authority?
3. Any sensitive surface that can avoid HIGH?
4. Any missing MEDIUM review trigger or silent HIGH review waiver?
5. Any Task-boundary rule that accidentally removes RELEASE_FULL or INTEGRATION_GATE?
6. Any one-session shortcut that weakens completion commit/persistence?
7. Any parallelism rule that allows overlapping mutation without combined verification?
8. Any direct Git/GitHub wording that creates authority or bypasses tool policy?
9. Any Brownfield auto-adoption or self-host Root mutation?
10. Any new runtime/CI/router/validator/bot scope?
```

- [ ] **Step 3: Fix all Critical/Important findings and rerun structural checks**

For each accepted finding:

```text
edit minimum affected surface
→ run TASK051_STRUCTURAL
→ run git diff --check
→ commit focused fix with review-oriented message
```

Do not dismiss a technically valid finding merely to preserve schedule.

- [ ] **Step 4: Record review disposition**

Before candidate freeze, the implementation state must be one of:

```text
REVIEW_PASS / no Critical or Important findings
or
EXPLICIT_GOVERNED_WAIVER / exact scope and authority recorded
```

`REVIEW_REQUIRED_BLOCKED` is not eligible for candidate acceptance.

---

### Task 5: Run cumulative AFFECTED verification and freeze the final implementation candidate

**Files:**
- Verify all Task 1–4 production files
- Modify only to fix failed affected checks
- Do not create release evidence yet

**Interfaces:**
- Consumes: structural GREEN + review acceptance.
- Produces: exact frozen candidate HEAD/tree/Framework-Source tree with cumulative AFFECTED PASS.

- [ ] **Step 1: Run cumulative AFFECTED mode**

Run:

```powershell
node E:\GitHub\ProjectFramework\.git\task051_verify.js affected E:\GitHub\ProjectFramework\.worktrees\task051-feature-delivery-fast-path
git diff --check
git status --short
```

AFFECTED mode must verify at least:

```text
release 1.17.0 / schema 1.0.0 / format 3
latest amendment path and amendment completeness
Core/SKILL Derived Delivery Tier semantics
R0–R3 exact preservation
LOW/MEDIUM/HIGH classification + sensitive escalation
preflight reuse/fresh-check semantics
review matrix + reviewer unavailable rule
verification floors + RELEASE_FULL/INTEGRATION_GATE separation
Task DONE completion commit semantics
one-session/artifact/persistence scaling
recovery/RESULT_VERIFICATION_REQUIRED
parallelism + combined-candidate verification
Git/GitHub/MCP/tool-policy boundaries
Brownfield no-auto-adopt
22/22 current starter stamps
README/MIGRATION/current mockup summaries
scenarios 1–504 contiguous/unique
seven registered commands unchanged
TASK-042/TASK-043/TASK-045 response semantics preserved
thin launchers unchanged
root ProjectFramework self-host remains 1.16
historical spec/amendment/evidence paths unmodified except current lifecycle additions
no forbidden runtime/CI/router/validator artifacts
git diff --check
review disposition accepted
```

Expected: `TASK051_AFFECTED ... PASS`.

- [ ] **Step 2: Fix AFFECTED failures before freeze**

Any semantic failure invalidates the current candidate. Apply the minimum correction, rerun only the required focused checks, then rerun full `affected` mode until PASS.

- [ ] **Step 3: Ensure all implementation changes are committed**

Run:

```powershell
git status --short
```

Expected before freeze: clean working tree, or only explicitly ignored scratch verifier outside candidate state.

If a correction remains uncommitted, commit it with a focused message before proceeding. Do not create an empty “candidate” commit solely for bookkeeping.

- [ ] **Step 4: Capture frozen candidate identity**

Run:

```powershell
git rev-parse HEAD
git rev-parse HEAD^{tree}
git rev-parse HEAD:Framework-Source
```

Record the three exact IDs. From this point until RELEASE_FULL completes, no candidate file may change.

---

### Task 6: Run exactly one final RELEASE_FULL on the unchanged candidate

**Files:**
- Read/verify only; no candidate mutation during the successful release run
- Scratch verifier remains outside candidate tree

**Interfaces:**
- Consumes: exact frozen candidate with AFFECTED PASS and accepted independent review/waiver disposition.
- Produces: one state-bound `TASK051_RELEASE_FULL ... PASS_RUN_1` result for the exact unchanged candidate.

- [ ] **Step 1: Preflight candidate immutability**

Immediately before release mode run:

```powershell
git status --short
git rev-parse HEAD
git rev-parse HEAD^{tree}
git rev-parse HEAD:Framework-Source
```

Expected: identities exactly match Task 5 and candidate working tree is clean.

- [ ] **Step 2: Run release mode once**

Run exactly once on the final accepted candidate:

```powershell
$candidateHead = git rev-parse HEAD
node E:\GitHub\ProjectFramework\.git\task051_verify.js release-full E:\GitHub\ProjectFramework\.worktrees\task051-feature-delivery-fast-path $candidateHead
```

The verifier must internally reject a HEAD mismatch before semantic assertions. Expected successful result:

```text
TASK051_RELEASE_FULL ... PASS_RUN_1
```

Do not rerun an unchanged successful candidate “for confidence”.

- [ ] **Step 3: Handle release-run failure correctly**

If a semantic assertion fails:

```text
invalidate candidate
→ fix
→ focused verification
→ AFFECTED
→ commit corrected candidate
→ freeze new identity
→ run one new final RELEASE_FULL on corrected candidate
```

If the verifier process fails before semantic assertions due only to scratch-tool infrastructure, repair the scratch verifier, rerun AFFECTED on the unchanged candidate, document that no semantic release acceptance occurred, then perform the one semantic release run. Never represent an aborted verifier process as PASS evidence.

---

### Task 7: Persist release evidence and terminalize TASK-051 / OUT-019 locally

**Files:**
- Create: `docs/superpowers/evidence/2026-09-13-task-051-risk-tiered-feature-delivery-fast-path-release-full.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Promote TASK-051 Project Source successors for current `01/03/09/10/12/13/14/15/91` as materially applicable
- Preserve: `Project-Source/00-Project-Source-Framework-r004-260912-2344.md`
- Preserve: root `PROJECT-BOOTSTRAP.md`

**Interfaces:**
- Consumes: frozen candidate IDs, AFFECTED PASS, independent review disposition, RELEASE_FULL PASS_RUN_1.
- Produces: durable local TASK-051 DONE / OUT-019 ACHIEVED lifecycle with exact evidence and no publication claim.

- [ ] **Step 1: Write state-bound release evidence**

The evidence file must record:

```text
Task / Goal: TASK-051 / OUT-019
Framework release: 1.17.0 / Schema 1.0.0 / format 3
Design spec + plan paths
Goal checkpoint commit: 52ccd7b
Design checkpoint commit: fc227f0
TDD scenario range: 473–504; cumulative 1–504 contiguous/unique
RED result
STRUCTURAL result
Independent review or explicit governed waiver disposition
AFFECTED result
Candidate HEAD
Candidate tree
Framework-Source tree
RELEASE_FULL result exactly PASS_RUN_1
Task DONE contract verification
Root/Bootstrap self-host remains 1.16 pending future post-merge reconciliation
Issue #29 remains OPEN because AUTH-019 has no tracker/publication mutation authority
No push/PR/merge/tag/GitHub Release
No Root/Binding mutation
No runtime/daemon/router/watcher/CI/CD/validator/CLI
No external disclosure or secret persistence
```

Plan checkpoint persistence uses `EVD-100 / CHG-100`. Use `EVD-101 / CHG-101` for final implementation/release evidence and `EVD-102 / CHG-102` for terminal completion readback.

- [ ] **Step 2: Mark TASK-051 DONE without claiming publication**

Update the durable Task source to:

```text
Status: DONE
Implementation State: LOCAL_VERIFIED_COMPLETE / RELEASE_CANDIDATE_VERIFIED / NOT_PUBLISHED
Design: USER_APPROVED_FINAL_DESIGN / SELF_REVIEWED
Plan: IMPLEMENTATION_PLAN_EXECUTED
Review: accepted independent review or exact governed waiver disposition
Verification: RED → STRUCTURAL → AFFECTED PASS → RELEASE_FULL PASS_RUN_1
Publication State: NOT_AUTHORIZED / NOT_PUSHED / NOT_MERGED / NOT_RELEASED
Issue #29: OPEN unless separately authorized tracker mutation occurs
Exact Next Step: none for local TASK-051 completion
```

Backlog counts become `TODO=0 / IN_PROGRESS=0 / BLOCKED=0`.

- [ ] **Step 3: Terminalize Goal lifecycle**

Project Source current truth must end with:

```text
OUT-019 ACHIEVED
AUTH-019 TERMINATED
ACT-031 DONE
ENV-019 EXPIRED
TASK-051 DONE / VERIFIED_COMPLETE / LOCAL_ONLY
```

Successor revisions must archive predecessors, preserve Stable document IDs/Project UUID, keep `00`/Bootstrap at Framework 1.16.0, and route active `01/14` exactly to the new current files.

- [ ] **Step 4: Verify terminal successor set before commit**

Run bounded checks proving:

```text
active 01/03/09/10/12/13/14/15/91 route exactly
predecessors exist under archive and not active root
EVD-101/EVD-102 and CHG-101/CHG-102 resolve consistently
Task backlog counts are 0/0/0
TASK-051 DONE and OUT-019 terminal states agree
Framework-Source candidate tree equals the RELEASE_FULL-bound tree
00 + PROJECT-BOOTSTRAP still self-host 1.16
no remote publication occurred
git diff --check PASS
```

- [ ] **Step 5: Commit release evidence / terminal reconciliation locally**

Stage exact bounded evidence/lifecycle files only, then commit with this exact message:

```powershell
git commit -m "docs(task051): record verified local fast-path completion"
```

No push follows under AUTH-019.

- [ ] **Step 6: Fresh-read completion commit and clean working tree**

Run:

```powershell
git rev-parse HEAD
git log -1 --oneline
git status --short
git branch --show-current
git log --oneline --decorate -6
```

Then rerun the bounded terminal routing/lifecycle verifier against committed HEAD. Only after this fresh readback may TASK-051 local completion be externally claimed.

Expected final truth:

```text
TASK-051 DONE / VERIFIED_COMPLETE / LOCAL_ONLY
OUT-019 ACHIEVED
AUTH-019 TERMINATED
ACT-031 DONE
ENV-019 EXPIRED
Backlog TODO=0 / IN_PROGRESS=0 / BLOCKED=0
Framework distribution candidate 1.17.0 verified
ProjectFramework self-host pin remains 1.16.0
Issue #29 remains OPEN
No push/PR/merge/tag/release
```

---

## Plan Self-Review Checklist

Before execution, verify all of the following:

- every TASK-051 spec section maps to at least one Task above;
- scenarios `473–504` are all listed explicitly and current `1–472` collision check is preserved;
- release identity, amendment, Core, SKILL, README, migration, templates, 22 starter stamps, pressure scenarios, evidence, and lifecycle are all covered;
- no step treats LOW/MEDIUM/HIGH as authority or replacement Risk;
- review requirements cannot silently disappear when a reviewer is unavailable;
- `RELEASE_FULL` and `INTEGRATION_GATE` remain separate acceptance boundaries;
- Task DONE still requires observed completion commit;
- one-session optimization removes redundant ceremony rather than safety gates;
- direct Git/GitHub never creates publication authority or bypasses tool policy;
- ProjectFramework self-host Root/Bootstrap remain 1.16 during local candidate work;
- thin launchers and bootstrap template are explicitly protected from unnecessary expansion;
- scratch verifier is outside candidate tree and uses UTF-8 Node I/O;
- candidate mutation after release acceptance is treated as invalidation;
- terminal lifecycle/evidence occurs after the verified Framework candidate and does not rewrite the accepted Framework-Source tree;
- no plan step performs push/PR/merge/tag/release, destructive cleanup, external-AI disclosure, Root/Binding mutation, runtime/daemon/router/watcher/CI/CD/validator/CLI, or secret persistence.
