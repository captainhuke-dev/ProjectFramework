# Framework Governance Amendment — TASK-025 Project Knowledge Layer

**Framework:** 1.10.0
**Schema:** 1.0.0
**Release format:** 3
**Status:** CURRENT / APPROVED
**Task:** TASK-025 — Project Knowledge Layer / Compounding Knowledge Contract

## 1. Purpose

Framework 1.10.0 adds an optional, Markdown-first **Project Knowledge Layer** for reusable research synthesis, comparisons, exploratory conclusions, Meeting-derived insights, and learned context that should compound over time without becoming Project authority automatically.

The governing invariants are:

```text
Project Knowledge ≠ Project Authority
Derived synthesis ≠ Evidence ≠ Governed Project truth
Retrieval rank/confidence/recency ≠ Authority
Knowledge promotion ≠ automatic mutation
```

This amendment is additive. Project Source Schema remains 1.0.0; release format remains 3; no Project Source semantic slot is added.

## 2. Optional Project Knowledge representation

When applicable and approved, a consuming Project may materialize:

```text
<Project-Root>/Project-Knowledge/
├── README.md
├── index.md
├── log.md
└── pages/
```

`Project-Knowledge/` exists outside `Project-Source/00–99`, has no Root Governance authority, and never precedes `PROJECT-BOOTSTRAP.md → active FRAMEWORK-001 → 01 → 03` authority resolution.

Framework maintains starter/template source under `Framework-Source/templates/project-knowledge/`; that distribution template is not an active consuming-Project Knowledge instance.

## 3. Knowledge page contract

Maintained pages use compact YAML frontmatter with:

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

`knowledge_page_id` is Knowledge-layer identity only. It is not Project Source identity or approval authority.

Exact maintenance states are:

```text
CURRENT | REVIEW_DUE | STALE | CONTRADICTED | SUPERSEDED | RETIRED
```

These states describe maintenance/navigation state, not truth certainty. Material claim uncertainty remains explicit in content/provenance.

## 4. Provenance and source ownership

Material synthesized claims require reconstructable `source_refs`. Sources may be repository paths plus commit/tree when material, Project Source records, `EVD-*`, Meeting result pointers, external URLs/document IDs, provider-native file/object IDs, or user-confirmed source references.

Raw/source material remains in its authoritative or source-native location by default. Project Knowledge references source material rather than requiring bulk duplication. Deliberately retained copies remain governed source artifacts and gain no authority from proximity to Knowledge.

Knowledge pages distinguish source-derived statements from LLM synthesis/interpretation when that distinction matters.

## 5. Index and log

`index.md` is content-oriented navigation metadata. It catalogs maintained pages and may show relative link, title, concise description, knowledge state, source count, and updated time. Ordering/ranking never decides Project truth.

`log.md` is chronological and append-only for material Knowledge operations using:

```text
## [YYYY-MM-DD] ingest | <source title>
## [YYYY-MM-DD] query-file | <knowledge page/title>
## [YYYY-MM-DD] lint | <scope>
## [YYYY-MM-DD] maintain | <scope>
```

Transient reads/queries that do not mutate Knowledge or file a reusable result require no log entry. The Knowledge log is not an MCP/tool transcript, raw search dump, or private chain-of-thought store.

## 6. Operations

### Ingest

```text
identify source + provenance
→ read/minimize relevant material
→ compare with existing Knowledge
→ create/update affected pages
→ update cross-links
→ update index.md
→ append one material log entry
→ surface contradictions/promotion candidates
```

Ingest never promotes synthesis into Project Source automatically.

### Query / file

A useful answer may be filed when it adds reusable synthesis. Filing is a Knowledge mutation and follows provenance, links, index, and log rules.

### Lint

Knowledge lint checks contradictions, stale/review-due pages, orphan/broken links, missing repeated concepts, weak/missing provenance, superseded sources, and unreviewed governance-relevance candidates. Lint findings remain advisory until materially routed through an existing canonical Project Source family and authority flow.

## 7. Contradiction, staleness, and supersession

Knowledge disagreement does not automatically create Project Source conflict. Advisory disagreement may remain in `CONTRADICTED` Knowledge state while governed Project truth is unaffected.

Use Project Source `DRIFT-*` / `CONFLICT-*` only when authoritative truth domains materially disagree under existing semantics.

## 8. Knowledge→Governance promotion gate

Knowledge may surface a promotion candidate, but no Knowledge state is approval. Promotion is:

```text
knowledge finding/candidate
→ identify target canonical Project Source home
→ verify evidence required for governed claim
→ assess affected REQ/DEC/RISK/ISS/DRIFT/CONFLICT/REL/etc.
→ obtain applicable authority/approval
→ mutate only the canonical owner through normal governed flow
→ preserve minimum evidence/reference linkage
→ update Knowledge to reference the governed result
```

Knowledge pages are not copied wholesale into Evidence by default.

## 9. Integration boundaries

### TASK-023 bootstrap

Project authority resolves first. Project Knowledge may be discovered from current routing only after active `FRAMEWORK-001` resolves and only when useful to the task.

### TASK-024 Meeting

Meeting output remains advisory. Material Meeting results may feed Knowledge through bounded evidence/source pointers, but provider JSON, council majority, or Chairman synthesis never becomes Project authority or automatic Knowledge truth.

### TASK-026 disclosure

Local/advisory Knowledge is not automatically externally disclosable. External-model use independently applies classification, provider eligibility, minimization/redaction, secret prohibition, and bounded disclosure authorization.

### Evidence

```text
EVD-* = reconstructable evidence basis for governed use
Project Knowledge = derived/advisory reusable synthesis
```

References may cross between layers without collapsing their roles.

### Current State and Handoff

`03` / `09` may point to the Knowledge root, a materially relevant page, or a maintenance blocker when useful; they do not mirror Knowledge content.

### Project Graph

Knowledge cross-links are advisory content links, not `REL-*`. Project relation claims enter `92` only through existing relation governance.

### AI-ControlTower / OpenViking

Cross-layer indexing preserves explicit content class:

```text
PROJECT_SOURCE_AUTHORITY
PROJECT_KNOWLEDGE_ADVISORY
```

OpenViking remains `DERIVED_ONLY` and rebuildable. Vector similarity, retrieval rank, recency, graph centrality, or combined search never transfers authority. Cross-Project retrieval preserves each source Project's disclosure and authority boundaries.

## 10. GREENFIELD and Brownfield

Project Knowledge is optional/applicability-driven. GREENFIELD Preview evaluates usefulness; if applicable and approved, Knowledge is materialized only after active `FRAMEWORK-001` and mandatory Project Source exist. Absence of Project Knowledge is valid when not applicable.

Existing initialized Projects remain pinned and do not receive Project Knowledge automatically. Brownfield adoption uses governed `[Project Upgrade]` or another explicit Project change/Preview. Historical notes/chats/files are not automatically reinterpreted as maintained Knowledge or governed truth; candidate material requires provenance review.

## 11. Secrets and authority

Actual secret values are never stored in Project Knowledge merely because sources contain them. Existing `SECRET-*` reference semantics apply when a governed reference is required.

Knowledge maintenance authority does not imply external disclosure, Project Source mutation, push/publication, Root/Binding, Decision, Risk acceptance, or runtime authority.

## 12. Implementation boundary

Framework 1.10.0 defines documentation/governance/templates only. It does not authorize or create a wiki engine, vector database, UI, watcher, crawler, auto-ingest daemon, embedding pipeline, MCP wiki service, validator/CLI, scheduler, or runtime automation.

Existing initialized Projects never auto-upgrade merely because upstream advances.
