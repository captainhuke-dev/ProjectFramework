# Project Upgrade One-Session Fast Path Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver ProjectFramework `1.18.0` with a governed Project Upgrade One-Session Fast Path that turns compatible upgrades into one comparison/assessment, one exact Preview, one explicit mutation approval, one bounded mutation batch, one affected verification phase, one completion commit, and one terminal readback while reusing exact valid Framework release proof instead of rerunning it in the wrong proof domain.

**Architecture:** Extend the existing `[Project Upgrade]` Direct-to-Latest contract rather than adding a new command or state family. The command remains read-only through comparison/assessment/Preview, but removes the intermediate “prepare?” prompt; approved compatible `FAST_PATH` and bounded `ASSESSED_PATH` upgrades execute as one state-bound transaction. Framework Release Acceptance remains separate from Project Upgrade Acceptance, so exact valid upstream `RELEASE_FULL` evidence may be reused while Project-specific resulting-state verification remains mandatory; `INTEGRATION_GATE` stays fresh and separate before mutable-target actions.

**Tech Stack:** Markdown/YAML governance artifacts, Git, Node.js scratch verification scripts under ignored `.superpowers/sdd/task052/`, Project Source lifecycle/evidence records.

**Spec:** `docs/superpowers/specs/2026-09-13-project-upgrade-one-session-fast-path-design.md`

## Global Constraints

- Target Framework exactly `1.18.0`; Schema remains `1.0.0`; release format remains `3`.
- Existing upgrade path vocabulary remains exactly `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED`.
- `[Project Upgrade]` invocation remains read-only until one explicit Human mutation approval bound to the exact Preview/candidate.
- `FAST_PATH` and bounded compatible `ASSESSED_PATH` may be one-session eligible; `MAJOR_MIGRATION_REQUIRED` is never one-session eligible.
- Framework Release Acceptance and Consuming Project Upgrade Acceptance remain distinct proof domains.
- Exact reusable upstream `RELEASE_FULL` proof may replace a consuming-upgrade release rerun only when the observed target identity/tree exactly matches the evidence binding and all material assumptions remain valid.
- Project affected verification remains mandatory after release-proof reuse.
- `INTEGRATION_GATE` remains mandatory immediately before applicable mutable-target integration/publication.
- Deterministic revision/timestamp/filename/routing generation already covered by the approved Preview does not require reapproval; material semantic/candidate/authority/rollback delta does.
- Canonical ProjectFramework integration + self-host reconciliation may chain only when the same exact Preview and authority already cover both; otherwise stop at the first unauthorized boundary.
- Brownfield Projects never auto-adopt Framework 1.18.
- TASK-052 implementation is HIGH under Framework 1.17 and requires independent review before candidate acceptance absent a valid governed waiver.
- Current Goal authorizes local design/plan/Framework documentation-governance implementation/tests/review/verification/evidence/local commits only; it does not authorize push/PR/merge/tag/GitHub Release or actual Root self-host promotion to 1.18.
- Active ProjectFramework `FRAMEWORK-001` and root `PROJECT-BOOTSTRAP.md` remain self-host pinned to Framework `1.16.0` throughout this local TASK-052 implementation.
- No runtime upgrade engine, bot, daemon, scheduler, validator/CLI, CI/CD mutator, MCP upgrade router, credential store, background watcher, or persistent service/database is introduced.
- Pressure scenarios `505–528` are reserved for TASK-052; scenarios `1–504` must remain contiguous and unique.
- Deliberate ancestry is `STACKED_WORK` on TASK-051 terminal commit `26fbb3c0ff298b183f23c7dabe5132dc11002185`; TASK-051 verified Framework 1.17 candidate/evidence remains historical and must not be rewritten.

---

## File Map

### Normative/current Framework surfaces

- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml` — bump current distribution to Framework `1.18.0`, keep Schema `1.0.0` / format `3`, route latest amendment to TASK-052.
- Create: `Framework-Source/references/framework-governance-amendment-260913-task052-project-upgrade-one-session-fast-path.md` — concise normative delta for command flow, transaction binding, proof-domain reuse, recovery, and self-host chaining.
- Modify: `Framework-Source/references/core-governance-rules.md` — canonical `[Project Upgrade]` and canonical self-host reconciliation semantics.
- Modify: `Framework-Source/SKILL.md` — operational command flow and workflow quick-reference behavior.
- Modify: `Framework-Source/templates/upgrade-preview.md` — exact state-bound transaction fields/fingerprint and one-session/evidence-reuse/stop-boundary representation.

### Propagation/current distribution surfaces

- Modify: `README.md` — Current Release 1.18 and concise One-Session Upgrade Fast Path summary.
- Modify: `Framework-Source/MIGRATION-NOTES.md` — current `1.17.0 → 1.18.0` guidance.
- Modify: `Framework-Source/templates/00-project-source-framework.md` — current root starter summary of upgrade flow.
- Modify: `Framework-Source/templates/core-document-skeletons.md` — current reusable skeleton guidance where upgrade semantics are summarized.
- Modify: `Framework-Source/templates/project-source-mockup/README.md` — current starter-release summary.
- Modify: all 22 `Framework-Source/templates/project-source-mockup/*.template.md` files carrying `project_source_framework_version` — stamp to `1.18.0`.
- Preserve byte/content unless separately proven necessary: `Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md`, `Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md`, `Framework-Source/templates/PROJECT-BOOTSTRAP.md`.

### Tests/evidence/lifecycle

- Modify: `Framework-Source/tests/pressure-scenarios.md` — append scenarios `505–528` exactly once.
- Scratch only, ignored/non-candidate: `.superpowers/sdd/task052/verify.js` — RED/STRUCTURAL/AFFECTED/RELEASE_FULL checks.
- Create after final verification: `docs/superpowers/evidence/2026-09-13-task-052-project-upgrade-one-session-fast-path-release-full.md`.
- Modify: `docs/superpowers/PROJECT-TASKS.md`.
- Promote TASK-052 Project Source successors for current `01/03/09/10/12/13/14/15/91` when checkpoint/terminal truth materially changes.
- Preserve: `Project-Source/00-Project-Source-Framework-r004-260912-2344.md` and root `PROJECT-BOOTSTRAP.md` throughout local candidate work.

---

### Task 1: Add TASK-052 pressure scenarios and establish RED

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`
- Create scratch only: `.superpowers/sdd/task052/verify.js`

**Interfaces:**
- Consumes: approved TASK-052 spec; current scenarios `1–504`; current Framework 1.17 contract.
- Produces: exact scenario range `505–528` and a deterministic verifier that proves the new production contract is absent before implementation.

- [ ] **Step 1: Append scenarios 505–528 exactly as allocated by the spec**

Add exactly these scenario headings in order:

```text
505 compare + assessment + Preview without prepare prompt
506 exact Preview still requires explicit mutation approval
507 eligible FAST_PATH uses one mutation batch
508 bounded compatible ASSESSED_PATH is one-session eligible
509 MAJOR_MIGRATION_REQUIRED is ineligible
510 FAST_PATH reuses exact valid release evidence
511 bounded ASSESSED_PATH reuses exact valid release evidence
512 target-tree mismatch blocks reuse
513 post-evidence target mutation invalidates reuse
514 Project affected verification remains mandatory
515 uninterrupted transaction avoids per-document checkpoints
516 interruption reuses unchanged evidence
517 reconstructable partial transaction resumes unfinished work
518 unknown shared/non-idempotent result requires RESULT_VERIFICATION_REQUIRED
519 material Preview delta requires re-Preview/reapproval
520 deterministic generated metadata does not require reapproval
521 canonical integration + self-host chains with exact authority
522 integration-only authority stops at RECONCILIATION_REQUIRED
523 local-only authority stops before integration
524 INTEGRATION_GATE remains mandatory
525 completion requires observed durable commit
526 Brownfield no-auto-upgrade
527 no runtime upgrade automation
528 normal verification budget forbids repeated RELEASE_FULL without invalidation
```

Each scenario must contain Prompt, Temptation, Pass, Fail, and GREEN expectation sections consistent with the design spec.

- [ ] **Step 2: Create scratch verifier with explicit modes**

Create `.superpowers/sdd/task052/verify.js` with modes:

```text
red
structural
affected
release-full
```

The verifier must at minimum:

```javascript
const expectedScenarioCount = 528;
const task052Start = 505;
const task052End = 528;
const targetFramework = '1.18.0';
const schema = '1.0.0';
const releaseFormat = 3;
```

RED mode must pass only when all are true:

```text
scenarios 1–528 are contiguous and unique
Scenario 505 and 528 exist
FRAMEWORK-RELEASE is still 1.17.0
TASK-052 amendment is absent
Core does not yet contain the TASK-052 one-session upgrade marker
SKILL does not yet contain the TASK-052 one-session upgrade marker
README does not yet advertise Framework 1.18
```

- [ ] **Step 3: Run RED**

Run:

```powershell
node .superpowers/sdd/task052/verify.js red E:\GitHub\ProjectFramework\.worktrees\task051-feature-delivery-fast-path
```

Expected terminal line:

```text
TASK052_RED <all checks>/PASS PASS_EXPECTED_MISSING_CONTRACT
```

Exit code must be `0`; RED mode itself proves missing production behavior, not a broken baseline.

- [ ] **Step 4: Confirm diff hygiene**

Run:

```powershell
git diff --check
```

Expected: exit `0` and no output.

- [ ] **Step 5: Commit RED scenarios**

```powershell
git add Framework-Source/tests/pressure-scenarios.md
git commit -m "test(task052): add one-session upgrade fast-path scenarios"
```

Do not commit the scratch verifier.

---

### Task 2: Implement the normative Framework 1.18 upgrade transaction contract

**Files:**
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Create: `Framework-Source/references/framework-governance-amendment-260913-task052-project-upgrade-one-session-fast-path.md`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`
- Modify: `Framework-Source/templates/upgrade-preview.md`

**Interfaces:**
- Consumes: scenarios `505–528`, approved spec, Framework 1.17 `[Project Upgrade]` / evidence reuse / self-host rules.
- Produces: canonical Framework 1.18 normative contract consumed by all propagation and final verification tasks.

- [ ] **Step 1: Bump release descriptor and amendment pointer**

Set exactly:

```yaml
release_format_version: 3
framework_version: "1.18.0"
schema_version: "1.0.0"
latest_framework_amendment: "references/framework-governance-amendment-260913-task052-project-upgrade-one-session-fast-path.md"
```

Preserve canonical repository/branch, migration notes pointer, upgrade Preview template pointer, assurance policy, and all unrelated descriptor fields.

- [ ] **Step 2: Add TASK-052 amendment with the normative delta**

The amendment must explicitly state all of the following:

```text
[Project Upgrade] remains read-only through exact Preview
UPGRADE_AVAILABLE no longer asks a separate prepare question
read-only comparison + cumulative assessment + path classification + Preview happen in one command pass
one explicit mutation approval is required and state-bound to exact Preview/candidate
ONE_SESSION_ELIGIBLE is working vocabulary only, never a new state/ID family
FAST_PATH and bounded compatible ASSESSED_PATH may qualify
MAJOR_MIGRATION_REQUIRED never qualifies
approved eligible mutation executes as one bounded successor/archive/routing transaction
per-document checkpoints are not required absent a real continuation boundary
Framework Release Acceptance != Consuming Project Upgrade Acceptance
exact valid target RELEASE_FULL evidence may be reused for both FAST_PATH and bounded ASSESSED_PATH
Project affected verification remains mandatory
mismatched/stale/unverifiable release evidence cannot be reused
RELEASE_FULL budget is 0 with valid reusable proof, otherwise at most 1 when genuinely required
material Preview/candidate/scope/authority/rollback changes require re-Preview/reapproval
deterministic revision/timestamp/filename/routing generation does not
interruption reuses unchanged comparison/assessment/release evidence and reconstructable durable state
unknown non-idempotent/shared outcome uses RESULT_VERIFICATION_REQUIRED before retry
canonical integration + self-host reconciliation may chain under one exact Preview/authority
missing Root authority stops at RECONCILIATION_REQUIRED
local-only authority stops before integration without invalidating local completion
INTEGRATION_GATE remains mandatory before mutable-target actions
Brownfield no-auto-upgrade remains binding
no runtime automation is introduced
```

- [ ] **Step 3: Replace the current Core `[Project Upgrade]` flow with the one-session contract**

In `Framework-Source/references/core-governance-rules.md`, update the existing `[Project Upgrade]` section so the canonical sequence is:

```text
resolve valid active local FRAMEWORK-001
→ fresh-resolve exact target candidate
→ compare current→target
→ cumulative assessment
→ classify FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED
→ determine one-session eligibility
→ materialize exact Preview
→ request one explicit mutation approval
→ if approved and still valid: bounded mutation transaction
→ Project affected verification
→ completion commit
→ terminal readback
```

Remove the semantic requirement to ask “prepare?” before assessment/Preview.

Preserve exact report labels:

```text
UP_TO_DATE | UPGRADE_AVAILABLE | SOURCE_DIVERGENCE | VERIFICATION_REQUIRED
```

- [ ] **Step 4: Generalize exact release-evidence reuse from FAST_PATH-only to eligible FAST_PATH + bounded ASSESSED_PATH**

Replace the old FAST_PATH-only rule with proof-domain semantics:

```text
exact target candidate/tree + committed current RELEASE_FULL evidence + unchanged material assumptions
→ reuse Framework release proof
→ run Project upgrade affected/result verification

mismatch/stale/unknown/change
→ release proof not reusable
→ run applicable current verification; at most one final RELEASE_FULL on exact unchanged candidate when required
```

Explicitly state that reuse never replaces Project-specific migration verification.

- [ ] **Step 5: Update canonical self-host reconciliation to allow chaining**

Preserve all existing eligibility and Root authority rules, but add:

```text
same exact approved Preview + authority covers integration and self-host
→ INTEGRATION_GATE
→ integration
→ fresh merged-result verification
→ immediate Root/Project Source/Bootstrap reconciliation
→ affected postflight
→ terminal reconciliation
```

Do not require a second `[Project Upgrade]`, Preview, or approval when the merged result exactly matches the already-approved self-host delta.

If Root authority is absent, preserve:

```text
RECONCILIATION_REQUIRED
```

and stop before Root mutation.

- [ ] **Step 6: Update SKILL operational flow**

In `Framework-Source/SKILL.md`, update the current `[Project Upgrade]` workflow rule so implementers follow exactly the Core contract above, including:

```text
single read-only compare/assessment/Preview pass
one explicit mutation approval
one bounded mutation transaction
proof-domain release-evidence reuse
Project affected verification
one completion commit
terminal readback
fresh INTEGRATION_GATE before mutable-target action
self-host chaining only with exact authority
```

Do not duplicate long rationale from Core; keep operational language concise.

- [ ] **Step 7: Upgrade Preview template becomes the exact transaction contract**

Ensure `Framework-Source/templates/upgrade-preview.md` contains explicit fields for:

```text
Current Project / current Framework+Schema pin
Exact Target Framework / Schema / release format
Target source/ref/tree/content identity
Path Classification
One-Session Eligibility
Affected Project Source / Root / Bootstrap surfaces
Preservation Invariants
Rollback / Recovery Route
Framework Release Evidence Reuse Decision + binding
Project Upgrade Verification Plan
Publication / Integration Scope
Canonical Self-Host Applicability
Exact Mutation Authority Requested
Known Stop Boundaries
Preview Fingerprint / material assumptions
```

The template must state that Human approval binds to the exact Preview/candidate and that material deltas require re-Preview/reapproval.

- [ ] **Step 8: Run STRUCTURAL verifier**

Run:

```powershell
node .superpowers/sdd/task052/verify.js structural E:\GitHub\ProjectFramework\.worktrees\task051-feature-delivery-fast-path
```

At this point expected failures may only be propagation/starter/version-summary checks assigned to Task 3. Normative contract checks must pass.

- [ ] **Step 9: Commit normative contract**

```powershell
git add Framework-Source/FRAMEWORK-RELEASE.yaml Framework-Source/references/framework-governance-amendment-260913-task052-project-upgrade-one-session-fast-path.md Framework-Source/references/core-governance-rules.md Framework-Source/SKILL.md Framework-Source/templates/upgrade-preview.md
git commit -m "feat(framework): define one-session project upgrade fast path"
```

---

### Task 3: Propagate Framework 1.18 current guidance and starter state

**Files:**
- Modify: `README.md`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: `Framework-Source/templates/project-source-mockup/README.md`
- Modify: all 22 `Framework-Source/templates/project-source-mockup/*.template.md`
- Preserve: thin launchers + distribution bootstrap template

**Interfaces:**
- Consumes: Task 2 canonical contract.
- Produces: coherent Framework 1.18 current distribution/starter representation with no duplicated authority.

- [ ] **Step 1: Update README Current Release and concise 1.18 summary**

Set current release to `1.18.0 / Schema 1.0.0` and add a compact section stating:

```text
[Project Upgrade] now produces compare + cumulative assessment + exact Preview in one read-only pass
one explicit mutation approval remains mandatory
eligible FAST_PATH and bounded compatible ASSESSED_PATH may complete in one session
exact valid release proof is reused while Project-specific affected verification remains mandatory
MAJOR remains outside the fast path
INTEGRATION_GATE remains fresh and separate
canonical integration + self-host may chain only under exact Preview/authority
no runtime updater/CI/bot/CLI is introduced
```

- [ ] **Step 2: Add current migration section `1.17.0 → 1.18.0`**

The migration section must identify affected surfaces and tell existing Projects:

```text
no auto-upgrade
run [Project Upgrade]
command performs read-only cumulative assessment + exact Preview without separate prepare prompt
approve exact mutation Preview once
reuse exact release proof only when evidence/tree binding matches
always verify Project migration result
MAJOR path retains stronger migration workflow
```

- [ ] **Step 3: Update maintained current root/skeleton/mockup summaries**

Add concise 1.18 upgrade semantics to:

```text
Framework-Source/templates/00-project-source-framework.md
Framework-Source/templates/core-document-skeletons.md
Framework-Source/templates/project-source-mockup/README.md
```

Do not turn these into second normative copies of Core.

- [ ] **Step 4: Stamp all 22 maintained starter templates to 1.18.0**

Replace only current starter frontmatter occurrences:

```yaml
project_source_framework_version: "1.17.0"
```

with:

```yaml
project_source_framework_version: "1.18.0"
```

Do not rewrite historical documents or active self-host Project Source.

- [ ] **Step 5: Prove thin/bootstrap surfaces unchanged**

Compare against plan checkpoint commit `5adc2ed`:

```powershell
git diff --exit-code 5adc2ed -- Framework-Source/CHATGPT-PROJECT-INSTRUCTIONS.md Framework-Source/CLAUDE-PROJECT-INSTRUCTIONS.md Framework-Source/templates/PROJECT-BOOTSTRAP.md
```

Expected: exit `0`.

- [ ] **Step 6: Run STRUCTURAL GREEN**

Run:

```powershell
node .superpowers/sdd/task052/verify.js structural E:\GitHub\ProjectFramework\.worktrees\task051-feature-delivery-fast-path
```

Expected terminal line:

```text
TASK052_STRUCTURAL <all checks>/PASS
```

Also run:

```powershell
git diff --check
```

Expected exit `0`.

- [ ] **Step 7: Commit propagation**

```powershell
git add README.md Framework-Source/MIGRATION-NOTES.md Framework-Source/templates/00-project-source-framework.md Framework-Source/templates/core-document-skeletons.md Framework-Source/templates/project-source-mockup
git commit -m "docs(framework): propagate one-session upgrade fast-path contract"
```

---

### Task 4: Independent review, cumulative AFFECTED verification, and candidate freeze

**Files:**
- No production mutation expected unless review finds a real defect.
- Scratch: `.superpowers/sdd/task052/review-pass.md`

**Interfaces:**
- Consumes: stable Task 1–3 implementation candidate.
- Produces: state-bound independent review acceptance plus AFFECTED PASS and frozen candidate HEAD/tree/Framework-Source tree for Task 5.

- [ ] **Step 1: Freeze mutation while independent review runs**

Observe candidate identifiers:

```powershell
git rev-parse HEAD
git rev-parse HEAD^{tree}
git rev-parse HEAD:Framework-Source
git status --short
```

Working tree must be clean before review acceptance.

- [ ] **Step 2: Independent reviewer checks exactly these acceptance questions**

Reviewer must be distinct from the producing instance where practicable and return PASS/FAIL for:

```text
1. prepare round-trip is removed but mutation approval remains explicit
2. one-session eligibility includes FAST + bounded ASSESSED and excludes MAJOR
3. exact Preview/candidate approval is state-bound
4. deterministic generated metadata does not trigger reapproval, material semantic delta does
5. mutation batching does not remove interruption durability
6. release proof and Project migration proof are distinct domains
7. exact valid RELEASE_FULL evidence is reusable for FAST and bounded ASSESSED only
8. Project affected verification remains mandatory
9. evidence mismatch/change invalidates reuse
10. RELEASE_FULL budget is 0 reusable / max 1 genuinely required
11. INTEGRATION_GATE remains mandatory
12. canonical integration+self-host chaining never fabricates Root/publication authority
13. integration-only authority stops at RECONCILIATION_REQUIRED
14. local-only authority stops successfully before integration
15. Brownfield no-auto-upgrade and no-runtime boundaries remain
```

Acceptance requires:

```text
Critical = 0
Important = 0
REVIEW_PASS
```

Write scratch marker with exact reviewer identity and reviewed candidate HEAD.

- [ ] **Step 3: If review finds a real defect, fix once and invalidate prior review**

Any candidate semantic change after review requires:

```text
rerun STRUCTURAL
new independent review bound to new HEAD
```

Do not stack review-of-review loops when no candidate change occurred.

- [ ] **Step 4: Run cumulative AFFECTED**

Run:

```powershell
node .superpowers/sdd/task052/verify.js affected E:\GitHub\ProjectFramework\.worktrees\task051-feature-delivery-fast-path
```

AFFECTED must prove at least:

```text
scenarios 1–528 contiguous/unique
Framework 1.18 / Schema 1.0.0 / release format 3
latest TASK-052 amendment routing
Core/SKILL/Preview template normative contract
README/MIGRATION-NOTES/current starter propagation
22/22 starter stamps at 1.18
thin launchers and distribution bootstrap template unchanged from 5adc2ed
TASK-051 historical amendment/spec/evidence preserved
active self-host 00 + PROJECT-BOOTSTRAP still 1.16
no executable/runtime/CI artifact introduced
independent review marker valid and bound to current HEAD
git diff --check baseline..HEAD
clean candidate worktree
```

Expected terminal line:

```text
TASK052_AFFECTED <all checks>/PASS
```

- [ ] **Step 5: Freeze exact Framework 1.18 candidate**

Record:

```powershell
git rev-parse HEAD
git rev-parse HEAD^{tree}
git rev-parse HEAD:Framework-Source
```

These exact identifiers become the only valid Task 5 `RELEASE_FULL` target. No production candidate mutation is allowed afterward without invalidating Task 4 and rerunning affected review/verification.

---

### Task 5: Run exactly one final Framework 1.18 RELEASE_FULL

**Files:**
- No production changes.
- Scratch verifier only.

**Interfaces:**
- Consumes: exact frozen HEAD/tree/Framework-Source tree from Task 4.
- Produces: `PASS_RUN_1` state-bound release acceptance for the TASK-052-created Framework 1.18 candidate.

- [ ] **Step 1: Fresh-confirm frozen candidate before the run**

Run:

```powershell
git status --short
git rev-parse HEAD
git rev-parse HEAD^{tree}
git rev-parse HEAD:Framework-Source
```

All identifiers must exactly match Task 4 and worktree must be clean.

- [ ] **Step 2: Run RELEASE_FULL once**

Run:

```powershell
node .superpowers/sdd/task052/verify.js release-full E:\GitHub\ProjectFramework\.worktrees\task051-feature-delivery-fast-path <FROZEN_HEAD>
```

Expected terminal line:

```text
TASK052_RELEASE_FULL <all checks>/PASS PASS_RUN_1
```

This is the only full release run for the unchanged Task 4 candidate.

- [ ] **Step 3: If RELEASE_FULL fails, do not rerun unchanged candidate blindly**

Classify the failure:

```text
verifier defect only → fix scratch verifier, prove candidate bytes unchanged, then rerun without calling the first run product failure
candidate/product defect → fix candidate, invalidate Task 4 review/AFFECTED/freeze, repeat Task 4 then one final run on corrected candidate
environment/transient evidence failure → verify whether evidence became invalid; do not infer PASS
```

Any product candidate mutation requires a new freeze and new final run identity.

---

### Task 6: Persist durable release evidence and terminalize TASK-052 locally

**Files:**
- Create: `docs/superpowers/evidence/2026-09-13-task-052-project-upgrade-one-session-fast-path-release-full.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Promote current Project Source successors for `01/03/09/10/12/13/14/15/91`
- Preserve: active `00` and root `PROJECT-BOOTSTRAP.md`

**Interfaces:**
- Consumes: independent REVIEW_PASS, AFFECTED PASS, frozen candidate IDs, `RELEASE_FULL PASS_RUN_1`.
- Produces: durable local `TASK-052 DONE / OUT-020 ACHIEVED` truth and observed completion commit without publication claim.

- [ ] **Step 1: Write state-bound release evidence**

The durable evidence file must record exactly:

```text
Task / Goal: TASK-052 / OUT-020
Framework: 1.18.0 / Schema 1.0.0 / release format 3
Spec path and commit 5adc2ed
Plan path and plan checkpoint commit
STACKED_WORK parent: TASK-051 terminal 26fbb3c
Scenario range 505–528; cumulative 1–528 contiguous/unique
RED result
STRUCTURAL result
Independent reviewer identity + REVIEW_PASS disposition
AFFECTED result
Frozen candidate HEAD/tree/Framework-Source tree
RELEASE_FULL result PASS_RUN_1
active ProjectFramework 00 + PROJECT-BOOTSTRAP remain 1.16
no push/PR/merge/tag/GitHub Release
no actual Root/self-host promotion to 1.18
no Project Location Binding mutation
no runtime/daemon/router/watcher/CI-CD/validator/CLI
no external disclosure or secret persistence
```

Use the next available evidence/change IDs fresh-resolved from active Project Source; do not assume future numeric IDs before inspection.

- [ ] **Step 2: Mark TASK-052 DONE locally without claiming publication**

Set durable task truth to:

```text
Status: DONE
readiness: DONE / VERIFIED_COMPLETE / LOCAL_ONLY
Implementation State: LOCAL_VERIFIED_COMPLETE / RELEASE_CANDIDATE_VERIFIED / NOT_PUBLISHED
Design: USER_APPROVED_FINAL_DESIGN / WRITTEN_SPEC_SELF_REVIEWED
Plan: IMPLEMENTATION_PLAN_EXECUTED
Review: REVIEW_PASS / exact reviewer identity
Verification: RED → STRUCTURAL → AFFECTED PASS → RELEASE_FULL PASS_RUN_1
Publication State: NOT_AUTHORIZED / NOT_PUSHED / NOT_MERGED / NOT_RELEASED
Exact Next Step: none for local TASK-052 completion
```

Backlog counts become `TODO=0 / IN_PROGRESS=0 / BLOCKED=0` unless another Task was independently added meanwhile; fresh-resolve before writing.

- [ ] **Step 3: Terminalize Goal lifecycle**

Current truth must end with:

```text
OUT-020 ACHIEVED
AUTH-020 TERMINATED
ACT-032 DONE
ENV-020 EXPIRED
TASK-052 DONE / VERIFIED_COMPLETE / LOCAL_ONLY
```

Preserve predecessor history and route active `01/14` exactly to the new current successors. Keep active `FRAMEWORK-001` and root Bootstrap at Framework 1.16.

- [ ] **Step 4: Run bounded terminal pre-commit verifier**

Verify:

```text
all successor supersedes pointers are exact and non-self-referential
active 01/03/09/10/12/13/14/15/91 route exactly
predecessors are archived and absent from active root
Task/Goal lifecycle agrees
Evidence/Change IDs resolve consistently
backlog counts are fresh and truthful
Framework-Source tree equals RELEASE_FULL-bound tree
active 00 + root PROJECT-BOOTSTRAP remain 1.16
no publication occurred
git diff --check passes
```

- [ ] **Step 5: Commit terminal reconciliation locally**

Stage only exact evidence/lifecycle files and commit:

```powershell
git commit -m "docs(task052): record verified local upgrade fast-path completion"
```

No push follows under current Goal authority.

- [ ] **Step 6: Fresh-read completion commit and clean tree**

Run:

```powershell
git rev-parse HEAD
git log -1 --oneline
git status --short
git branch --show-current
git log --oneline --decorate -8
```

Then rerun the bounded terminal verifier against committed HEAD. Only after fresh committed readback may local TASK-052 completion be externally claimed.

---

## Plan Self-Review Checklist

Before execution, confirm all of the following:

1. Every spec Completion Criterion 1–25 maps to at least one task above.
2. Scenario range is exactly `505–528` and cumulative target is `1–528`.
3. RED occurs before production Framework mutation.
4. `[Project Upgrade]` remains read-only through exact Preview.
5. Separate “prepare?” prompt is removed from the target command flow.
6. One explicit mutation approval remains mandatory.
7. FAST + bounded ASSESSED eligibility and MAJOR exclusion are explicit.
8. Material Preview delta versus deterministic generated metadata behavior is explicit.
9. One bounded mutation batch and no per-document checkpoint requirement are explicit.
10. Framework Release Acceptance and Project Upgrade Acceptance stay distinct.
11. Exact release-proof reuse is conditional and Project affected verification remains mandatory.
12. Evidence mismatch/change invalidation is explicit.
13. RELEASE_FULL budget is `0 reusable / max 1 genuinely required` for consuming upgrades.
14. TASK-052 itself still gets one final Framework 1.18 RELEASE_FULL because it creates a release candidate.
15. Interruption/recovery and RESULT_VERIFICATION_REQUIRED behavior are covered.
16. INTEGRATION_GATE remains mandatory before mutable-target actions.
17. Canonical self-host chaining and both stop boundaries are covered.
18. Brownfield no-auto-upgrade remains explicit.
19. No runtime automation/CLI/CI/CD expansion appears.
20. Thin launchers and distribution Bootstrap template are preserved unless a proven current-contract need appears.
21. Active ProjectFramework Root/Bootstrap remain 1.16 under current Goal.
22. Independent review is mandatory for TASK-052 implementation candidate.
23. Terminal completion requires durable commit and fresh readback.
24. Publication/Root/Binding/external-disclosure/secret boundaries remain excluded.
25. No unresolved implementation placeholder or cross-task shorthand remains.
