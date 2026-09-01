# TASK-025 Project Knowledge Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement Framework 1.10.0 as an optional Markdown-first Derived Project Knowledge Layer that compounds reusable synthesis while remaining explicitly non-authoritative and provenance-aware.

**Architecture:** Keep Project Knowledge outside `Project-Source/00–99` at optional consuming-Project root `Project-Knowledge/`. Framework owns only the governance contract and maintained starter templates: Knowledge pages/index/log are advisory Markdown, source pointers remain source-native, Knowledge→Governance uses an explicit promotion gate, and OpenViking remains derived/rebuildable. No runtime wiki/vector/index service is introduced.

**Tech Stack:** Markdown, YAML, Git, Python scratch verification scripts only; no application/runtime implementation.

**Spec:** `docs/superpowers/specs/2026-09-01-task025-project-knowledge-layer-design.md`

## Global Constraints

- Target Framework `1.10.0` / Schema `1.0.0` / release format `3`.
- `Project Knowledge ≠ Project Authority`; `Derived synthesis ≠ Evidence ≠ Governed Project truth`.
- Optional consuming-Project representation is root-level `Project-Knowledge/`, outside Project Source semantic slots and Stable-ID families.
- Knowledge page identity is Knowledge-layer-only; no `KNOW-*` Project Source Stable-ID family is created.
- Required maintained Knowledge states: `CURRENT | REVIEW_DUE | STALE | CONTRADICTED | SUPERSEDED | RETIRED`.
- Maintained operations: ingest, query/file, lint; `log.md` is chronological append-only for material Knowledge operations, not a tool transcript.
- Source/provenance pointers are mandatory for material synthesized claims; raw duplication is not mandatory.
- Knowledge→Governance promotion always resolves a canonical Project Source owner and applicable authority; no automatic promotion.
- `[Meeting]`, `EVD-*`, `03`, `09`, `REL-* / 92`, TASK-026 disclosure, and OpenViking remain separate authority domains.
- OpenViking stays `DERIVED_ONLY` / rebuildable and distinguishes `PROJECT_SOURCE_AUTHORITY` from `PROJECT_KNOWLEDGE_ADVISORY`.
- GREENFIELD Knowledge is optional/applicability-driven; Brownfield adoption is governed and never automatic.
- Actual secret values remain forbidden.
- No wiki engine, vector database, UI, watcher, crawler, auto-ingest daemon, embedding pipeline, MCP wiki service, validator/CLI, scheduler, or runtime automation.
- No vendor launcher expansion unless a verified implementation need emerges; current plan expects no launcher changes.
- Observed repository correction: fresh `origin/main` contains 22 maintained Project Source mockup template files (`00–17` + `40/60/91/92`), not 24; verification uses the observed 22-file set.
- ProjectFramework local Project Source pin remains Framework `1.7.0` / Schema `1.0.0`.
- Push/publication is not authorized by `AUTH-003`.
- Use TDD: pressure scenarios/verifier first, observe RED before Framework contract mutation.
- Final acceptance uses AFFECTED verification followed by one final unchanged-candidate `RELEASE_FULL`; release evidence binds exact candidate HEAD/tree/Framework-Source tree.

---

### Task 1: Encode Project Knowledge Governance Pressure Contract (RED)

**Files:**
- Modify: `Framework-Source/tests/pressure-scenarios.md`
- Create scratch only: `.worktrees/.task025-scratch/task025_red_verify.py`

**Interfaces:**
- Consumes: Framework 1.9.0 current distribution and approved TASK-025 spec.
- Produces: scenarios `269–288` plus structural expectations used by Tasks 2–4.

- [ ] **Step 1: Append scenarios 269–288 before production changes**

Add Prompt / Temptation / Pass / Fail / GREEN expectation for exactly these themes:

```text
269 Project Knowledge ≠ Project Authority
270 Project-Knowledge/ is optional and outside Project Source slots
271 Knowledge page ID is not Project Source Stable-ID authority
272 material synthesized claims require source_refs/provenance
273 raw/source-native material is referenced, not obligatorily copied
274 index.md is navigation metadata, not truth ranking
275 log.md is append-only material-operation history, not tool transcript/CoT
276 ingest updates pages/links/index/log but never auto-promotes governance
277 query/file mutation obeys provenance/index/log rules
278 lint findings remain advisory until routed to canonical governance family
279 Knowledge maintenance states are exact and do not equal truth certainty
280 Knowledge contradiction does not automatically create Project CONFLICT
281 Knowledge→Governance promotion resolves canonical home + evidence + authority
282 Meeting output remains advisory before Knowledge filing
283 EVD-* evidence and Knowledge synthesis remain distinct
284 external Knowledge use still crosses TASK-026 disclosure boundary
285 Knowledge cross-links are not REL-* assertions
286 OpenViking preserves PROJECT_SOURCE_AUTHORITY vs PROJECT_KNOWLEDGE_ADVISORY and DERIVED_ONLY behavior
287 GREENFIELD optionality + Brownfield no-auto-adoption
288 no secret values and no wiki/vector/runtime/daemon/CLI/MCP implementation
```

- [ ] **Step 2: Write structural RED verifier**

The scratch verifier must assert at least:

```python
framework_version == "1.10.0"
schema_version == "1.0.0"
release_format_version == 3
latest amendment points to TASK-025
scenarios == list(range(1, 289))
Core and SKILL contain Project Knowledge authority/provenance/state/promotion/integration contracts
Framework-Source/templates/project-knowledge/ contains README.md, index.md, log.md, page-template.md
page-template frontmatter contains knowledge_page_id, knowledge_state, source_refs, related_project_source_refs, related_knowledge, review_trigger
no KNOW-* Project Source Stable-ID family
no runtime implementation artifact is introduced
```

- [ ] **Step 3: Run RED verifier and observe expected failure**

Run:

```text
python E:\GitHub\ProjectFramework\.worktrees\.task025-scratch\task025_red_verify.py
```

Expected: FAIL because current Framework is 1.9.0 and Project Knowledge implementation/templates do not yet exist. Failure must be feature-missing, not script/runtime error.

- [ ] **Step 4: Verify scenario numbering and diff hygiene**

Confirm scenarios are contiguous/unique `1–288`; run `git diff --check`.

- [ ] **Step 5: Commit RED contract**

```text
git add Framework-Source/tests/pressure-scenarios.md
git commit -m "test: define project knowledge governance scenarios"
```

---

### Task 2: Implement Framework 1.10.0 Normative Project Knowledge Contract

**Files:**
- Modify: `Framework-Source/FRAMEWORK-RELEASE.yaml`
- Create: `Framework-Source/references/framework-governance-amendment-260901-task025.md`
- Modify: `Framework-Source/references/core-governance-rules.md`
- Modify: `Framework-Source/SKILL.md`

**Interfaces:**
- Consumes: Task 1 RED expectations and approved spec.
- Produces: canonical authority/provenance/lifecycle/promotion/integration semantics for Task 3 templates and docs.

- [ ] **Step 1: Bump release descriptor**

Set exactly:

```yaml
framework_version: "1.10.0"
schema_version: "1.0.0"
release_format_version: 3
latest_framework_amendment: "references/framework-governance-amendment-260901-task025.md"
```

Keep canonical repository/entrypoint semantics unchanged.

- [ ] **Step 2: Add TASK-025 amendment**

The amendment must define:

```text
Project Knowledge ≠ Project Authority
optional Project-Knowledge/ outside 00–99
page schema and exact knowledge_state vocabulary
source_refs provenance and no mandatory raw duplication
index.md + append-only log.md
operations ingest / query-file / lint
contradiction/staleness/supersession semantics
explicit Knowledge→Governance promotion gate
TASK-023 / TASK-024 / TASK-026 / EVD / 03 / 09 / 92 / OpenViking boundaries
PROJECT_SOURCE_AUTHORITY vs PROJECT_KNOWLEDGE_ADVISORY retrieval class
GREENFIELD optionality / Brownfield no-auto-adoption
secrets/no-runtime boundary
```

- [ ] **Step 3: Extend Core Governance**

Add a dedicated Project Knowledge section after current bootstrap/command/integration boundaries. Reuse existing Project Source canonical families instead of creating Knowledge authority families. Add Project Knowledge to integrity checks as optional/advisory when materialized.

- [ ] **Step 4: Update SKILL operational guidance**

Add Project Knowledge discovery/use only after active Project authority resolves, plus ingest/query-file/lint and promotion/disclosure boundaries. Add quick-reference guidance without expanding vendor launchers.

- [ ] **Step 5: Run focused Task-2 verifier**

Verify release/amendment/Core/SKILL semantics, exact vocabulary, no `KNOW-*`, no schema/slot/runtime expansion. Task 3 template/README/migration checks may still fail.

- [ ] **Step 6: Commit normative implementation**

```text
git add Framework-Source/FRAMEWORK-RELEASE.yaml Framework-Source/references/framework-governance-amendment-260901-task025.md Framework-Source/references/core-governance-rules.md Framework-Source/SKILL.md
git commit -m "docs: define project knowledge governance"
```

---

### Task 3: Add Maintained Knowledge Templates and Propagate Current Guidance

**Files:**
- Create: `Framework-Source/templates/project-knowledge/README.md`
- Create: `Framework-Source/templates/project-knowledge/index.md`
- Create: `Framework-Source/templates/project-knowledge/log.md`
- Create: `Framework-Source/templates/project-knowledge/page-template.md`
- Modify: `README.md`
- Modify: `Framework-Source/MIGRATION-NOTES.md`
- Modify: `Framework-Source/templates/00-project-source-framework.md`
- Modify: `Framework-Source/templates/core-document-skeletons.md`
- Modify: `Framework-Source/templates/project-source-mockup/README.md`
- Modify maintained `Framework-Source/templates/project-source-mockup/*.template.md` Framework-version stamps `1.9.0 → 1.10.0`

**Interfaces:**
- Consumes: Task 2 normative contract.
- Produces: reusable documentation/template representation for consuming Projects and complete current distribution alignment.

- [ ] **Step 1: Create `templates/project-knowledge/README.md`**

Document optional materialization, directory layout, authority boundary, source/provenance rules, exact knowledge states, ingest/query-file/lint, Knowledge→Governance promotion, disclosure/secrets, OpenViking classification, and Brownfield safety. State clearly this folder is a Framework starter source, not an active Project Knowledge instance.

- [ ] **Step 2: Create `index.md` and `log.md` starter templates**

`index.md` must include columns/fields for relative link, title, description, `knowledge_state`, optional source count and updated time. `log.md` must document exact heading forms:

```text
## [YYYY-MM-DD] ingest | <source title>
## [YYYY-MM-DD] query-file | <knowledge page/title>
## [YYYY-MM-DD] lint | <scope>
## [YYYY-MM-DD] maintain | <scope>
```

- [ ] **Step 3: Create `page-template.md`**

Frontmatter must include:

```yaml
knowledge_page_id: "<UUID_OR_STABLE_OPAQUE_ID>"
title: "<TITLE>"
knowledge_state: "CURRENT | REVIEW_DUE | STALE | CONTRADICTED | SUPERSEDED | RETIRED"
created_at: "<ISO8601>"
updated_at: "<ISO8601>"
source_refs:
  - "<SOURCE_OR_EVIDENCE_POINTER>"
related_project_source_refs: []
related_knowledge: []
review_trigger: "<EVENT_OR_CONDITION_OR_NOT_APPLICABLE>"
```

Body includes Summary, Key Findings, Synthesis / Interpretation, Sources / Provenance, Contradictions / Uncertainty, Related Knowledge, Governance Relevance / Promotion Candidates, Review Notes.

- [ ] **Step 4: Propagate current guidance**

Update README/root template/skeleton/mockup README to expose the optional `Project-Knowledge/` layer only after Project authority resolves. Do not add a semantic slot or make Knowledge mandatory.

- [ ] **Step 5: Update maintained starter stamps**

All current maintained mockup template files that declare `project_source_framework_version` become `1.10.0`; Schema remains `1.0.0`. Historical artifacts are untouched.

- [ ] **Step 6: Add migration notes `1.9.0 → 1.10.0`**

Cover optional adoption, Preview/approval, no bulk migration of notes/chats, provenance review, no automatic Knowledge→Governance promotion, no external disclosure expansion, no runtime dependencies, and Direct-to-Latest compatibility.

- [ ] **Step 7: Run Task-3 verifier**

Verify templates, page schema, exact states/log headings, 22 maintained starter stamps, current docs, Brownfield/authority/no-runtime rules, no launcher changes, and historical preservation.

- [ ] **Step 8: Commit templates/propagation**

```text
git add README.md Framework-Source/templates Framework-Source/MIGRATION-NOTES.md
git commit -m "docs: add project knowledge starter templates"
```

---

### Task 4: Green Contract, Comprehensive AFFECTED Verification, and Candidate Freeze

**Files:**
- Modify: `docs/superpowers/PROJECT-TASKS.md`
- Scratch verification only: `.worktrees/.task025-scratch/`

**Interfaces:**
- Consumes: Tasks 1–3 completed Framework distribution.
- Produces: exact release candidate identities and AFFECTED evidence inputs.

- [ ] **Step 1: Run original RED verifier as GREEN**

Expected: all Task-1 structural expectations PASS.

- [ ] **Step 2: Run comprehensive AFFECTED verifier**

Cover at least:

```text
Framework 1.10.0 / Schema 1.0.0 / release format 3 / latest amendment
scenarios 1–288 contiguous + TASK-025 scenario semantics
Project Knowledge authority separation and no KNOW-* family/semantic slot
Knowledge states/page schema/index/log/operations/provenance
promotion gate + canonical Project Source homes
Meeting/EVD/disclosure/03/09/92/OpenViking boundaries
PROJECT_SOURCE_AUTHORITY vs PROJECT_KNOWLEDGE_ADVISORY
GREENFIELD optionality / Brownfield no-auto-adoption
actual secret values forbidden
4 maintained Project Knowledge template files
22 Project Source starter stamps at 1.10.0/1.0.0
vendor launchers unchanged from branch base
no executable/runtime/CI/CLI/vector/wiki/MCP artifacts
historical prior amendments/specs/evidence preserved
ProjectFramework local Project Source pin 1.7.0/1.0.0
git diff --check
```

- [ ] **Step 3: Update TASK-025 execution metadata**

Record RED, implementation commits, GREEN/AFFECTED results, release target, and candidate-next state. Keep publication `NOT_PUSHED`.

- [ ] **Step 4: Re-run AFFECTED after metadata update**

Must remain PASS.

- [ ] **Step 5: Commit final implementation candidate**

```text
git add docs/superpowers/PROJECT-TASKS.md Framework-Source README.md
git commit -m "docs: complete project knowledge implementation"
```

- [ ] **Step 6: Freeze candidate identities**

Capture exact:

```text
Candidate HEAD
Candidate tree
Framework-Source tree
working tree clean
```

No Framework/current-contract mutation after freeze until final RELEASE_FULL completes or candidate evidence is explicitly invalidated.

---

### Task 5: Final RELEASE_FULL, Evidence, and Terminal Goal Reconciliation

**Files:**
- Create: `docs/superpowers/evidence/2026-09-01-task-025-project-knowledge-release-full.md`
- Modify governed Project Source `01/03/09/10/12/13/14/15/91` via revision/validate/promote/archive
- Modify: `PROJECT-BOOTSTRAP.md`
- Modify: `docs/superpowers/PROJECT-TASKS.md`

**Interfaces:**
- Consumes: frozen Task-4 candidate.
- Produces: state-bound release evidence and terminal local Task/Goal truth.

- [ ] **Step 1: Run one final RELEASE_FULL on frozen candidate**

Bind the verifier to candidate HEAD/tree/Framework-Source tree. Require AFFECTED PASS and no candidate mutation.

- [ ] **Step 2: Write and commit release evidence**

Record design/spec/plan, RED→GREEN, AFFECTED, RELEASE_FULL, scenarios 1–288, template counts, exact candidate/tree identities, failed-candidate/harness events if any, and `Publication: NOT_PUSHED`.

- [ ] **Step 3: Prepare terminal Project Source revisions**

Set:

```text
TASK-025 DONE
ACT-013 DONE
OUT-003 ACHIEVED
AUTH-003 TERMINATED
ENV-003 EXPIRED
Execution State READY
Publication NOT_PUSHED
Exact Next Action ไม่มีขั้นตอนถัดไป
Chat START_NEW_CHAT
```

Preserve ProjectFramework local Project Source pin `1.7.0`.

- [ ] **Step 4: Validate/promote terminal revisions**

Verify bootstrap/Index/Manifest routing, current Stable-ID resolution, candidate/evidence pointers, Goal terminal semantics, no Framework-Source drift after candidate, no uncommitted required state, and `git diff --check`.

- [ ] **Step 5: Commit terminal lifecycle reconciliation**

```text
git add PROJECT-BOOTSTRAP.md Project-Source docs/superpowers/PROJECT-TASKS.md
git commit -m "docs: complete task 025 lifecycle"
```

- [ ] **Step 6: Fresh final verification before completion claim**

Verify observed completion commit, parent evidence/candidate chain, Framework-Source tree equals release evidence, working tree clean, TASK/OUT/AUTH/ACT/ENV terminal states, and no remote TASK-025 publication.

- [ ] **Step 7: Finish branch without publication**

Keep `task025-project-knowledge` and its worktree intact. Do not push/create PR/merge unless the user later gives explicit publication intent.
