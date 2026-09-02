# TASK-025 Project Knowledge Layer / Compounding Knowledge Contract — Design

**Task:** TASK-025 — Project Knowledge Layer / Compounding Knowledge Contract
**Design state:** USER_APPROVED_DESIGN / WRITTEN_SPEC_APPROVED
**Approval basis:** User `[Goal] ทำจนจบ task` on 2026-09-01; proceed without design changes.
**Target Framework:** 1.10.0
**Project Source Schema:** 1.0.0
**Release format:** 3
**Source concept:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (`llm-wiki`)
**Scope:** documentation/governance architecture only; no wiki engine, vector database, UI, watcher, crawler, auto-ingest daemon, embedding pipeline, MCP wiki service, or runtime automation.

## 1. Problem and intent

ProjectFramework already distinguishes governed current truth, evidence, continuity, Project relations, and advisory Meeting output. It does not yet provide a durable home for research synthesis, comparisons, exploratory conclusions, learned context, and reusable reasoning that should compound over time without becoming authoritative `REQ-*`, `DEC-*`, `ISS-*`, `DRIFT-*`, `CONFLICT-*`, `RISK-*`, or other Project Source truth automatically.

TASK-025 adapts the `llm-wiki` compounding-knowledge pattern while preserving ProjectFramework authority boundaries. The source concept describes three layers—raw sources, an LLM-maintained Markdown wiki, and a schema/instruction layer—plus `index.md`, chronological `log.md`, and ingest/query/lint operations. ProjectFramework adopts those useful patterns but does not copy the source concept's implementation assumptions blindly.

The governing invariant is:

```text
Project Knowledge ≠ Project Authority
Derived synthesis ≠ Evidence ≠ Governed Project truth
Retrieval rank/confidence/recency ≠ Authority
Knowledge promotion ≠ automatic mutation
```

## 2. Chosen architecture

### 2.1 Recommended approach — Derived Markdown Knowledge Layer

When applicable, a consuming Project may materialize a root-level optional directory:

```text
<Project-Root>/Project-Knowledge/
```

This directory is outside the `Project-Source/00–99` semantic namespace. It has no Project Source semantic slot and never becomes `FRAMEWORK-001` or another governance root.

Maintained knowledge layout:

```text
Project-Knowledge/
├── README.md        # knowledge-layer schema, authority boundary, conventions
├── index.md         # content-oriented catalog of knowledge pages
├── log.md           # chronological append-only ingest/query/file/lint/maintenance history
└── pages/
    └── <domain-or-topic>/<page>.md
```

No `raw/` directory is mandatory. Raw/source material remains in its authoritative or source-native location whenever possible: repository files, external documents, web sources, Meeting evidence, `EVD-*`, datasets, or governed storage. Knowledge pages reference those sources rather than duplicating them merely to support synthesis.

A Project may deliberately retain source copies for offline/reproducibility reasons, but such copies are source artifacts governed by their own storage/provenance rules and do not become authoritative merely because they sit under or near Project Knowledge.

### 2.2 Rejected alternatives

**Knowledge inside Project Source semantic slots** is rejected. Advisory synthesis would become too easy to confuse with Project authority and would create pressure to duplicate canonical homes such as `REQ-*`, `DEC-*`, `ISS-*`, `DRIFT-*`, `CONFLICT-*`, `RISK-*`, and `REL-*`.

**OpenViking/RAG/index-first authority** is rejected. Search/index tooling may assist discovery, but a derived index must remain rebuildable and non-authoritative. Project Knowledge must remain reconstructable from durable Markdown plus source pointers without requiring a vector database, graph database, MCP server, or ranking engine.

## 3. Knowledge page contract

Each maintained page is LLM-maintainable Markdown with compact YAML frontmatter. Required fields are:

```yaml
knowledge_page_id: "<UUID_OR_STABLE_OPAQUE_ID>"
title: "<TITLE>"
knowledge_state: "CURRENT | REVIEW_DUE | STALE | CONTRADICTED | SUPERSEDED | RETIRED"
created_at: "<ISO8601>"
updated_at: "<ISO8601>"
source_refs:
  - "<SOURCE_OR_EVIDENCE_POINTER>"
related_project_source_refs:
  - "<OPTIONAL_STABLE_ID_OR_CANONICAL_DOC_POINTER>"
related_knowledge:
  - "<OPTIONAL_KNOWLEDGE_PAGE_ID_OR_RELATIVE_LINK>"
review_trigger: "<EVENT_OR_CONDITION_OR_NOT_APPLICABLE>"
```

`knowledge_page_id` is a Knowledge-layer identifier only. It is not a Project Source Stable-ID family, cannot be cited as Project authority, and does not claim a semantic slot.

Recommended page body sections are applicability-driven rather than universally mandatory:

```text
Summary
Key Findings
Synthesis / Interpretation
Sources / Provenance
Contradictions / Uncertainty
Related Knowledge
Governance Relevance / Promotion Candidates
Review Notes
```

A page may contain multiple claims with different certainty. Page-level `knowledge_state` describes maintenance state, not truth certainty. Material claim uncertainty remains explicit in prose/source attribution; do not manufacture numeric confidence scores.

## 4. Source and provenance model

Source provenance is mandatory for material synthesized claims. `source_refs` may point to:

```text
repository path + commit/tree when material
Project Source Stable ID or document
EVD-* evidence record
Meeting evidence/result pointer
external URL/document identifier
provider-native file/object identity
user-confirmed source reference
```

A Knowledge page may synthesize multiple sources. The page must distinguish source-derived statements from LLM inference/interpretation when that distinction matters.

Knowledge does not copy authoritative Project Source records merely to make them searchable. It references them. If a source is removed, unavailable, stale, or contradicted, the affected knowledge page is reviewed and may move to `REVIEW_DUE`, `STALE`, or `CONTRADICTED`.

## 5. Index and log semantics

### 5.1 `index.md`

`index.md` is content-oriented. It catalogs active/reviewable knowledge pages with relative link, title, one-line description, knowledge state, and optional source-count/updated-at metadata.

It is updated whenever a page is created, renamed, materially reclassified, superseded, retired, or removed through an authorized maintenance flow.

The index is navigation metadata, not authority. Search ranking or index ordering never decides Project truth.

### 5.2 `log.md`

`log.md` is chronological and append-only for material Knowledge operations. Entries use a parseable heading convention:

```text
## [YYYY-MM-DD] ingest | <source title>
## [YYYY-MM-DD] query-file | <knowledge page/title>
## [YYYY-MM-DD] lint | <scope>
## [YYYY-MM-DD] maintain | <scope>
```

A transient query that neither changes Knowledge nor produces a filed result does not require a log entry. The log is not an MCP/tool transcript and does not store private chain-of-thought or raw tool payloads.

## 6. Knowledge operations

### 6.1 Ingest

```text
identify source + provenance
→ read/minimize relevant material
→ compare with existing Knowledge
→ create/update affected pages
→ update cross-links
→ update index.md
→ append one log.md entry
→ surface material contradictions or governance-relevant candidates
```

Ingest never promotes synthesis into Project Source automatically.

### 6.2 Query / File

The Agent reads `index.md`, relevant pages, then source/evidence as needed. A useful answer may be filed back into Knowledge only when it adds reusable synthesis rather than duplicating an existing page.

Filing a query result is a Knowledge mutation. It uses the same provenance/cross-link/index/log rules as ingest.

### 6.3 Lint

Knowledge lint is advisory maintenance. It checks for:

```text
contradictory pages/claims
stale/review-due pages
orphan pages
broken/missing cross-links
important repeated concepts without a page
missing or weak provenance
superseded sources
knowledge-to-governance candidates that were never reviewed
```

Lint findings do not auto-create Project Source `ISS-*`, `DRIFT-*`, or `CONFLICT-*`. When a finding becomes materially governance-relevant, route it through the existing canonical family and authority flow.

## 7. Contradiction, staleness, and supersession

Knowledge contradiction is not automatically a Project Source `CONFLICT-*` because competing advisory interpretations may coexist without authoritative Project disagreement.

Use:

```text
CURRENT       = maintained and not known stale
REVIEW_DUE    = review trigger/date/source change requires reassessment
STALE         = material source/context freshness is insufficient
CONTRADICTED  = material sources/knowledge claims disagree and synthesis is unresolved
SUPERSEDED    = a newer knowledge page/revision replaces this page for normal use
RETIRED       = intentionally removed from current knowledge navigation while history remains
```

When the contradiction concerns authoritative Project truth or materially mismatched truth domains, existing Project Source `DRIFT-*` / `CONFLICT-*` semantics apply in their canonical homes after the applicable governance threshold is met.

## 8. Knowledge → Governance promotion gate

A Knowledge page may identify a **promotion candidate**, but no Knowledge-layer status is equivalent to approval.

Promotion flow:

```text
knowledge finding / candidate
→ identify target canonical Project Source home
→ verify source/evidence needed for governed claim
→ assess affected REQ/DEC/RISK/ISS/DRIFT/CONFLICT/REL/etc.
→ obtain applicable user/authority/decision approval
→ mutate only the canonical Project Source owner through normal revision/validation/promotion flow
→ optionally add EVD-* pointer to the Knowledge page/source set when materially useful
→ update Knowledge page to reference the governed result
```

The Knowledge page is not copied wholesale into `EVD-*`. Evidence preserves minimum reconstructable provenance, not an entire advisory corpus by default.

## 9. Integration boundaries

### 9.1 TASK-023 bootstrap

`PROJECT-BOOTSTRAP.md` continues to route Project authority first:

```text
PROJECT-BOOTSTRAP.md → FRAMEWORK-001 → 01 → 03 → task-specific routing → 09
```

Project Knowledge never precedes or replaces this path. If `Project-Knowledge/` is materialized, active Project Source may expose an advisory pointer after authority resolves—for example from `01` routing or task-specific guidance. A fresh Agent reads Knowledge only when the task benefits from it.

### 9.2 TASK-024 `[Meeting]`

Meeting output remains advisory. Material Meeting results may be cited through existing `EVD-*` or source-native result pointers and can feed Knowledge synthesis. Provider JSON or council output never becomes Project authority or automatic Knowledge truth merely because it was produced by multiple models.

### 9.3 TASK-026 external-AI disclosure

Local/advisory Knowledge is not automatically externally disclosable. Sending Knowledge to an external AI/model/provider follows the same classification, provider eligibility, minimization, secret prohibition, and bounded authorization rules as any other Project context.

### 9.4 `13 Evidence`

Evidence and Knowledge remain distinct:

```text
EVD-* = evidence basis / reconstructable support for governed use
Project Knowledge = derived/advisory synthesis for reuse and exploration
```

A page may reference `EVD-*`; `EVD-*` may point to a Knowledge page when that page materially informed a governed decision, but neither becomes the other.

### 9.5 `03 Current State` and `09 Handoff`

`03` and `09` may reference the Knowledge root, an especially relevant page, or Knowledge maintenance blocker only when it is material to current work/continuation. They do not mirror Knowledge content.

### 9.6 `92 Project Graph`

Knowledge cross-links are advisory content links, not `REL-*`. Claims that Projects are related do not become Project Graph assertions until promoted through normal `92` governance.

### 9.7 AI-ControlTower / OpenViking

AI-ControlTower/OpenViking may index both layers only when it preserves an explicit content-class boundary:

```text
PROJECT_SOURCE_AUTHORITY
PROJECT_KNOWLEDGE_ADVISORY
```

OpenViking remains `DERIVED_ONLY` and rebuildable. It may search/index/traverse Knowledge, but ranking, vector similarity, recency, graph centrality, or combined retrieval never promotes Knowledge to Project authority. Cross-Project knowledge retrieval also preserves each source Project's disclosure/authority boundaries.

## 10. GREENFIELD and Brownfield behavior

Project Knowledge is **optional/applicability-driven**. It is not added to mandatory Project Source slots and is not created merely to make a Project look complete.

### GREENFIELD

The Preview evaluates whether a compounding Knowledge layer is useful. If applicable and approved, create the Knowledge root after active `FRAMEWORK-001` and the mandatory Project Source are established. The resulting Project Source may add a pointer to the Knowledge root without making it authority.

If not applicable, no `Project-Knowledge/` directory is created.

### Brownfield

Existing initialized Projects remain pinned and do not receive Project Knowledge automatically when upstream changes. Adoption uses governed `[Project Upgrade]` or another explicit Project change/Preview that preserves current Project Source, repository/storage bindings, existing docs, and history.

Migration does not reinterpret historical notes/chats/files as authoritative or as automatically accepted Knowledge. Imported candidate knowledge requires provenance review before it becomes maintained Knowledge.

## 11. Security, disclosure, and secrets

Project Knowledge never stores actual secret values merely because a source contains them. Use existing `SECRET-*` reference semantics when a governed reference is required. Source excerpts are minimized; sensitive material remains at its authoritative/source-native location unless explicit storage/disclosure authority says otherwise.

Knowledge maintenance authority does not imply external disclosure authority, Project Source mutation authority, push/publication authority, Root/Binding authority, or runtime authority.

## 12. Versioning and release classification

TASK-025 is reclassified from the original roadmap placeholder `1.9.0` to **Framework 1.10.0 / Schema 1.0.0 / release format 3** because it adds a new optional Framework interface and maintained representation after the already-released 1.9.0 line. It is additive and does not require a Project Source schema bump or semantic-slot change.

Existing initialized Projects remain pinned and opt into the layer through governed migration/adoption.

## 13. Affected Framework surfaces

Implementation should update only current maintained surfaces needed to express the contract:

```text
Framework-Source/FRAMEWORK-RELEASE.yaml
Framework-Source/references/framework-governance-amendment-<task025>.md
Framework-Source/references/core-governance-rules.md
Framework-Source/SKILL.md
Framework-Source/MIGRATION-NOTES.md
README.md
Framework-Source/templates/00-project-source-framework.md
Framework-Source/templates/core-document-skeletons.md
Framework-Source/templates/project-source-mockup/README.md
Framework-Source/templates/project-knowledge/* (new maintained starter/template source)
Framework-Source/tests/pressure-scenarios.md
docs/superpowers/PROJECT-TASKS.md
Project Source lifecycle/evidence records for ProjectFramework development
```

Thin vendor launchers should change only if the Knowledge contract materially needs bootstrap routing there. Default design says **no launcher expansion**: first resolve Project authority, then discover Knowledge from Project routing when relevant.

## 14. Verification strategy

TDD implementation should add pressure scenarios after the current scenario range and prove at least:

```text
Project Knowledge ≠ Project Authority
raw/source pointers remain authoritative/source-native
no automatic Knowledge→REQ/DEC/etc promotion
index/log/page conventions
staleness/contradiction/supersession semantics
Meeting advisory ingestion boundary
EVD vs Knowledge separation
TASK-026 disclosure enforcement for external Knowledge use
Knowledge links ≠ REL-* assertions
OpenViking content-class separation + DERIVED_ONLY behavior
GREENFIELD optionality
Brownfield no-auto-adoption
no secret values
no vector DB/runtime/daemon/CLI/MCP/wiki engine created by Framework contract
Framework 1.10.0 / Schema 1.0.0 maintained starter alignment
historical provenance preserved
```

Implementation uses RED first, affected verification, one final unchanged-candidate `RELEASE_FULL`, state-bound evidence, and Verified Task Completion Checkpoint before TASK-025 can be `DONE`.

## 15. Acceptance criteria

The design is acceptable when it establishes all of the following without creating parallel Project authority:

1. clear `Project Knowledge ≠ Project Authority` boundary;
2. optional root `Project-Knowledge/` representation with schema/index/log/pages;
3. source/provenance requirements and no mandatory raw duplication;
4. maintenance states and contradiction/staleness behavior;
5. ingest/query-file/lint operations;
6. explicit Knowledge→Governance promotion gate;
7. TASK-023/TASK-024/TASK-026/Evidence/03/09/92/OpenViking boundaries;
8. GREENFIELD/Brownfield behavior;
9. secrets/disclosure/authority separation;
10. Framework 1.10.0 additive release classification;
11. documentation/governance-only implementation boundary;
12. pressure-scenario and release-verification plan.
