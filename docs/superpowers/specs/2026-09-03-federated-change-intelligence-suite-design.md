# TASK-036 + TASK-030 + TASK-029 + TASK-031 Federated Change Intelligence Suite — Design

Date: `2026-09-03` (Asia/Bangkok)
Tasks: `TASK-036 + TASK-030 → TASK-029 → TASK-031`
Design state: `USER_APPROVED_DIRECTIONS / GOAL_SELECTED / WRITTEN_SPEC_APPROVED_BY_GOAL`
Approval basis: the Task registry already contains approved directions for TASK-036, TASK-030, TASK-029, and TASK-031, and the user explicitly invoked `[Goal] ดำเนินการต่อเนื่อง` after local verified Framework 1.13.0 completion. This Goal selects the related approved backlog directions for continuous bounded local execution. Push/publication/merge remain outside the Goal.

## 1. Baseline, stacked-work boundary, and release classification

Local verified suite baseline at Goal adoption:

```text
Parent branch: task028-032-integrity-remediation-suite
Parent completion: 6c97832c162aecd01b848465f6d53cc433c12cf0
Framework: 1.13.0
Schema: 1.0.0
release format: 3
Framework-Source tree: 61c27afad2bb794e54561e422b928fc777186585
pressure scenarios: 1–380
Registered Commands: 7 including [Project Audit]
Publication of parent suite: NOT_PUSHED
origin/main: a5e73faf3d13ed8baad6a259c52e15efc981804f
```

This suite is explicit **STACKED_WORK** on the unpublished verified Framework 1.13.0 parent. If publication is later authorized, parent integration/publication must precede or be included safely before this child suite; no branch relationship is inferred as publication authority.

The cumulative target is **Framework 1.14.0 / Schema 1.0.0 / release format 3**. This is a minor release because it adds four substantial governance capabilities and one optional derived distribution surface while preserving Project Source Schema, semantic slots, command registry, Stable-ID families, and runtime boundaries.

Older roadmap target labels (`1.9.0` / `1.11.0`) are historical planning values and are reclassified because the verified local Framework has advanced to 1.13.0.

## 2. Chosen suite architecture

The dependency model is:

```text
TASK-036 Project Change/Event History Feed ──┐
                                             ├→ TASK-029 Cross-Project Impact Analysis → TASK-031 Notification Contract
TASK-030 Relation Reconciliation ────────────┘                   ↑
                     └────────────────────────────────────────────┘
```

TASK-036 and TASK-030 are parallel foundation streams. TASK-029 starts only after both foundations have focused completion checkpoints. TASK-031 starts after TASK-029 plus TASK-030 are complete; TASK-036 may supply bounded event-routing input to notifications but is not a substitute for authoritative event sources.

Central invariants:

```text
Change feed ≠ Project history authority
Derived event ≠ canonical Project truth
Relation discovery ≠ reciprocal assertion
CORROBORATED ≠ central approval
Impact analysis ≠ cross-Project mutation
Potential impact ≠ confirmed direct impact
Notification ≠ approval ≠ authority
Acknowledgement ≠ acceptance ≠ mutation permission
Delivery success ≠ Project outcome success
```

### Alternatives considered

1. **One central graph/event database as canonical truth** — rejected because it would displace Project-local authority and violate OpenViking `DERIVED_ONLY`.
2. **Independent releases for each Task** — valid but rejected for this Goal because feed/reconciliation/impact/notification semantics have strong interface coupling and would duplicate propagation/release gates.
3. **Chosen: one cumulative Framework 1.14.0 release with four focused Task checkpoints** — preserves dependency ordering, keeps each Task independently verifiable, and shares one final unchanged-candidate release acceptance.

## 3. TASK-036 — optional Project Change Feed surface

Framework 1.14.0 defines an optional root-level derived surface:

```text
<Project-Root>/Project-Change-Feed/
├── README.md
└── feed.md
```

The Framework distribution maintains starter sources under:

```text
Framework-Source/templates/project-change-feed/
```

`Project-Change-Feed/` is outside `Project-Source/00–99`, outside Root Governance, and outside canonical history authority. It is created only when an incremental consumer materially benefits and adoption is approved/applicable. Absence is valid.

Authority separation is exact:

```text
Project-Change-Feed ≠ Project Source
Project-Change-Feed ≠ 10 Change Log
Project-Change-Feed ≠ Git/source-native history
Project-Change-Feed ≠ Evidence
Project-Change-Feed ≠ Project Knowledge
Project-Change-Feed ≠ OpenViking authority
```

The feed is fully rebuildable and disposable. Loss or corruption of the feed cannot make current Project truth unreconstructable.

## 4. Change-feed projection identity and state

`README.md` defines the projection contract and may carry compact derived-layer metadata such as:

```yaml
feed_projection_id: "<UUID_OR_STABLE_OPAQUE_DERIVED_ID>"
project_uuid: "<PROJECT_UUID>"
projection_state: "CURRENT | STALE | REBUILD_REQUIRED | UNAVAILABLE"
source_checkpoint:
  repository_ref: "<COMMIT_OR_UNKNOWN_OR_NOT_APPLICABLE>"
  project_source_manifest_ref: "<ACTIVE_14_POINTER_OR_UNKNOWN>"
  change_log_ref: "<ACTIVE_10_POINTER_OR_UNKNOWN>"
generated_at: "<ISO8601_OR_UNKNOWN>"
retention_policy: "<BOUNDED_POLICY_DESCRIPTION>"
```

`feed_projection_id` is derived-layer identity only. It is not a Project Source Stable ID, authorization object, evidence ID, or externally meaningful authority token.

Projection state meanings:

- `CURRENT` — current projection is supported by its declared source checkpoint.
- `STALE` — projection is known to lag authoritative/current sources.
- `REBUILD_REQUIRED` — projection integrity/checkpoint continuity is not safely reusable; discard/rebuild from authoritative sources.
- `UNAVAILABLE` — the projection cannot currently be read/materialized; authoritative sources remain the fallback.

These are derived-surface maintenance labels only, not Project lifecycle or health states.

## 5. Change-feed entry contract

`feed.md` is a bounded chronological projection. Each material entry records at least:

```text
Sequence within current projection generation
Source checkpoint / source-native ordering pointer
Change kind
Subject refs
Authoritative/source refs
Concise changed-state summary
Observed/materialized time when known
```

Exact change-kind vocabulary:

```text
STABLE_ID_CHANGE
DOCUMENT_CHANGE
RELATION_CHANGE
LIFECYCLE_CHANGE
EVIDENCE_CHANGE
RELEASE_PUBLICATION_CHANGE
OTHER_MATERIAL_CHANGE
```

An entry reports changed references and concise deltas; it does not duplicate whole authoritative objects and does not infer acceptance, impact, notification eligibility, or authority merely from change detection.

`Sequence` is projection-local ordering only and is never a canonical event ID. No `EVENT-*`, `FEED-*`, `CHANGE-EVENT-*`, or parallel Project Source Stable-ID family is created.

## 6. Incremental `since` / checkpoint semantics

A consumer may request changes **since** a previously observed source checkpoint. The checkpoint is a source-pointer bundle, not authority:

```text
repository/source-native ref when material
+ active Project Source Manifest pointer
+ active Change Log pointer
+ projection generation/context when useful
```

Ordering prefers source-native ordering over wall-clock recency. Git-backed changes use commit ancestry/order when material; Project Source history uses revision/current routing; equal/ambiguous timestamps never decide authoritative order by themselves.

If a requested checkpoint falls outside the retained feed window, the implementation must either rebuild the needed delta from authoritative history or return explicit `UNKNOWN / VERIFICATION_REQUIRED` for the unavailable portion. It must not pretend the retained feed is complete.

## 7. Rebuildability, stale/corrupt feed, and retention

Rebuild inputs are authoritative/source-native Project facts, including as applicable:

- Project Source current/history and `10 Change Log`;
- Git/source-native history;
- current `REL-*` / `92` relation history;
- durable `EVD-*` pointers;
- release/publication evidence when material.

Project Knowledge and OpenViking may assist discovery but are not sufficient authority for reconstruction.

Retention is explicitly bounded. A Project may declare a count/time/window policy appropriate to its scale; Framework 1.14.0 does not mandate one universal number. Dropping old derived entries does not delete authoritative history. A consumer requiring an older delta must rebuild from source history or fail explicitly when source history itself is unavailable.

The feed is not a raw MCP transcript, audit log of every tool call, private reasoning store, or unbounded execution trace.

## 8. TASK-030 — relation reconciliation workflow

Relation reconciliation is a governance workflow over existing `92 Project Graph` / `REL-*`; it creates no new relation family and no cross-Project write authority.

Workflow:

```text
identify local REL-* candidate
→ discover counterpart Project by immutable project_uuid
→ resolve counterpart authoritative 92 / REL-* when available
→ verify endpoint UUIDs + current source pointers + evidence freshness
→ evaluate compatibility under existing relation semantics
→ classify local assertion disposition using existing ASSERTED | CORROBORATED | CONFLICTED | RETIRED semantics
→ persist local change only with applicable local authority
→ never synthesize/write the counterpart Project's assertion
```

Discovery may use AI-ControlTower/OpenViking, Project Graph indexes, Knowledge, repositories, or configured connectors as routing assistance only. Material reconciliation claims require authoritative Project-local evidence.

## 9. Reciprocal compatibility rules

Framework 1.14.0 preserves TASK-022 exactly.

Guaranteed reciprocal-compatible core pairs are only:

```text
A PARENT_OF B  ↔ B CHILD_OF A
A CHILD_OF B   ↔ B PARENT_OF A
A PEER_OF B    ↔ B PEER_OF A
A RELATED_TO B ↔ B RELATED_TO A
```

`DEPENDS_ON` and `SUPPORTS` remain directional. Framework 1.14.0 does **not** invent a universal `DEPENDS_ON ↔ SUPPORTS` inverse rule. A derived index may show traversal relationships, but only independently asserted authoritative truth with compatible semantics may support corroboration.

Namespaced relation types require their owning Project/domain semantics; central similarity/ranking cannot infer reciprocal compatibility.

## 10. Evidence requirements for `CORROBORATED`

A local `REL-*` may move to `CORROBORATED` only when evidence resolves at least:

```text
local Project UUID + current local REL-* pointer
counterpart Project UUID + current counterpart REL-* pointer
matching endpoint UUIDs
compatible relation type/direction under governed semantics
authoritative/current source references for both assertions
freshness/review evidence sufficient for the claim
```

Derived inverse edges, OpenViking normalization, search rank, similarity, central confidence, repository proximity, naming similarity, or timestamp recency alone are insufficient.

Temporary counterpart unavailability never auto-retires a valid local assertion. If current corroboration cannot be freshly revalidated, report verification uncertainty separately; do not fabricate freshness or silently rewrite assertion state.

## 11. Conflict and unavailable counterpart behavior

Incompatible authoritative assertions preserve both Projects' truth and use `CONFLICTED` plus existing `CONFLICT-*` when managed resolution is material. Do not choose by recency, ranking, confidence, central index, or which Project is easier to mutate.

Stale/orphan derived state may use existing `DRIFT-*`. Migration/lineage/slot changes reuse `MIG-*`. Reconciliation never creates graph-specific conflict/drift families.

A counterpart that is unavailable, inaccessible, unbound, stale, or unresolved produces explicit `VERIFICATION_REQUIRED` for corroboration-sensitive claims while preserving what is still known locally.

## 12. TASK-029 — cross-Project impact analysis contract

Impact analysis consumes changed subjects and governed relation/dependency context to identify Projects/scopes that require review. It is advisory and creates no `[Impact]` command, impact Stable-ID family, or cross-Project mutation authority.

Exact impact classification:

```text
DIRECT
POTENTIAL
UNKNOWN
```

- `DIRECT` — authoritative evidence explicitly connects the changed source/subject to an affected Project/scope through current relation/dependency/requirement/decision or equivalent governed pointer.
- `POTENTIAL` — a plausible governed traversal/path exists but evidence is incomplete, indirect, conditional, stale, or requires target review before direct impact can be confirmed.
- `UNKNOWN` — required relation/source/counterpart evidence cannot be resolved sufficiently.

`NO_MATERIAL_IMPACT_FOUND` may be used as a report conclusion only after the assessed scope/evidence is explicit; it is not a fourth impact classification and never proves universal absence outside assessed scope.

## 13. Impact provenance and reasoning

Each material impact result reports:

```text
Changed source/subject refs
Affected Project UUID / scope when resolvable
Impact classification
Reasoning path using governed relation/dependency/requirement pointers
Authoritative/current evidence refs
Unknown/stale/conflict limitations
Review-required disposition
```

A `DIRECT` claim must not rest solely on Project-Change-Feed or OpenViking. The feed is incremental routing evidence; OpenViking is traversal/index assistance. Material claims trace back to authoritative/source-native Project evidence.

`DEP-*` remains canonical dependency-management payload in `91`; `REL-*` is relation input in `92`; `REQ-*`, `DEC-*`, Risk, Issue, Evidence, and other canonical homes remain unchanged.

## 14. Impact analysis authority boundary

```text
Impact detected in Project A
≠ permission to edit Project B
≠ permission to upgrade Project B
≠ approval in Project B
≠ authority to create/close Project B records
≠ publication/deployment authority
```

Impact analysis may recommend review, identify the target canonical home, and produce bounded evidence. Any target-Project mutation requires that Project's binding/authority/Risk/approval flow.

Merges/splits/retired relations are assessed through existing identity/lineage/MIG rules; predecessor edges are not blindly inherited.

## 15. TASK-031 — event and notification governance contract

TASK-031 defines when a material Project event is notification-worthy and how routing/acknowledgement/escalation evidence works. It adds no email/Slack/webhook sender, watcher, scheduler, daemon, queue, notification bot, or mandatory notification Stable-ID family.

Candidate event sources include, when material:

```text
Project Audit RED/AMBER/UNKNOWN finding
DIRECT/POTENTIAL/UNKNOWN impact requiring review
REL-* reconciliation conflict or material corroboration change
RISK / DEP / ISS / DRIFT / CONFLICT material transition
Goal/Action blocker requiring owner attention
release/publication/deployment material transition
other governed event explicitly declared notification-worthy
```

A Project-Change-Feed entry may route candidates but does not itself make an event notification-worthy.

## 16. Notification eligibility and urgency

Notification eligibility considers:

```text
materiality of the source event
current owner/recipient relevance
whether action/review is required
source evidence freshness
whether equivalent notification is already outstanding
declared Project notification policy when present
```

Notification urgency uses exact presentation-only values:

```text
ROUTINE | ATTENTION | URGENT
```

These values describe communication priority only. They do not replace Risk `R0–R3`, audit health, issue severity, authority, lifecycle state, or provider priority classes. Source severity/risk remains in its canonical source record.

## 17. Recipient resolution, acknowledgement, escalation, deduplication

Recipient resolution prefers governed/current Project ownership and responsibility evidence such as canonical object owner, `11 Actor Registry`, explicit Goal/Action owner, or user-selected recipient. `Responsibility ≠ Authority`; being a recipient grants no permission.

If recipient identity cannot be resolved safely, report `VERIFICATION_REQUIRED`; do not guess from email-like strings, Git authorship, chat participants, or recent activity.

Acknowledgement evidence, when material, identifies the source event, recipient, channel/provider-native pointer if applicable, acknowledgement time, and limitations. Acknowledgement means the signal was received/reviewed; it does not mean the underlying change/risk/decision was accepted.

Escalation is policy-driven and may occur when a material event remains unacknowledged or urgency rises. Escalation never grants authority and never broadens disclosure scope.

Deduplication keys must be source-based — source event identity/pointers + affected scope + recipient context — rather than free-text similarity alone. A materially changed source event is not suppressed merely because wording is similar.

## 18. Notification failure and stale handling

Unresolved recipient, unavailable delivery channel, provider failure, repeated delivery uncertainty, or stale source evidence remain explicit. If a real external delivery succeeds but durable Project reconciliation fails, use existing `PERSISTENCE_PENDING` semantics when required.

Notification failure does not erase the source event. Delivery success does not prove the underlying Project issue/impact/risk/outcome is resolved.

No external delivery occurs merely because this Framework contract exists; actual external disclosure/delivery remains separately authorized and subject to TASK-026/trust/tool constraints.

## 19. Cross-Task integration

### TASK-036 → TASK-029

Change Feed narrows the set of changed source refs for incremental impact analysis. Impact analysis revalidates material claims against authoritative sources.

### TASK-030 → TASK-029

Reconciled/current relation evidence improves impact confidence. `CONFLICTED` / unavailable relations constrain results to `POTENTIAL` or `UNKNOWN` where direct evidence is insufficient.

### TASK-029 + TASK-030 + TASK-028 → TASK-031

Audit findings, impact review requirements, and relation conflicts/corroboration changes are notification candidate events. Notification semantics never upgrade their authority.

### TASK-036 → TASK-031

The feed may route incremental event candidates and dedup/source checkpoints. Notification eligibility still comes from the authoritative source event and TASK-031 policy.

### Project Knowledge

Knowledge may consume feed/impact/reconciliation results as advisory synthesis with provenance. Feed entries are not Knowledge truth; Knowledge promotion still uses canonical-owner evidence/authority.

### AI-ControlTower / OpenViking

Central traversal/indexing remains `DERIVED_ONLY` and rebuildable. It may correlate feed checkpoints, relations, candidate impacts, or notification routing hints, but cannot become Project authority or cross-Project mutation authority.

## 20. Framework surfaces

Expected normative/current surfaces:

- `Framework-Source/FRAMEWORK-RELEASE.yaml`
- new `Framework-Source/references/framework-governance-amendment-260903-federated-change-intelligence.md`
- `Framework-Source/references/core-governance-rules.md`
- `Framework-Source/SKILL.md`
- `Framework-Source/MIGRATION-NOTES.md`
- root `README.md`
- `Framework-Source/templates/00-project-source-framework.md`
- `Framework-Source/templates/core-document-skeletons.md`
- `Framework-Source/templates/project-source-mockup/README.md`
- `Framework-Source/templates/project-source-mockup/00-Project-Source-Framework.template.md`
- new `Framework-Source/templates/project-change-feed/README.md`
- new `Framework-Source/templates/project-change-feed/feed.md.template`
- relevant `Framework-Source/templates/project-knowledge/` guidance when current template integration requires it
- all maintained Project Source starter release stamps to Framework 1.14.0
- `Framework-Source/tests/pressure-scenarios.md`
- Task/Project Source lifecycle/evidence and suite spec/plan/evidence.

Thin ChatGPT/Claude launchers should remain unchanged unless verification proves a current bootstrap requirement; parity and size ceiling remain gates.

No new Project Source semantic slot is added. No Registered Command is added or renamed; the command registry remains exactly seven commands from Framework 1.13.0.

## 21. Pressure-scenario contract

Reserve scenarios `381–420` for this suite.

### TASK-036 — 381–390

1. Feed never replaces Change Log/Git/Project Source authority.
2. Feed checkpoint outside retention triggers rebuild/unknown, never silent truncation.
3. Corrupt feed is discarded/rebuilt, not treated as history truth.
4. Source-native ordering outranks timestamp guessing.
5. Feed entry is not Stable ID/Evidence/impact decision.
6. Feed remains bounded and not raw tool transcript.
7. Missing optional feed does not invalidate Project.
8. OpenViking/Knowledge cannot become feed authority.
9. Feed rebuild uses authoritative/source-native pointers.
10. Feed adoption never creates runtime watcher/crawler.

### TASK-030 — 391–400

1. Reciprocal corroboration requires authoritative counterpart assertion.
2. Derived inverse edge cannot corroborate.
3. Only governed reciprocal pairs are assumed.
4. `DEPENDS_ON/SUPPORTS` inverse is not invented.
5. Endpoint UUID mismatch blocks corroboration.
6. Counterpart unavailable does not auto-retire local relation.
7. Contradiction becomes `CONFLICTED`, not recency winner.
8. Reconciliation never writes another Project's assertion.
9. OpenViking central confidence never grants corroboration.
10. Namespaced types require owned semantics.

### TASK-029 — 401–410

1. DIRECT impact requires authoritative connecting evidence.
2. Derived/feed-only evidence cannot prove DIRECT impact.
3. POTENTIAL stays distinct from DIRECT.
4. UNKNOWN remains explicit for unavailable counterpart/source.
5. Impact never mutates another Project.
6. REL input does not duplicate DEP/REQ/DEC payload.
7. Stale/conflicted relations constrain confidence.
8. Merge/split does not clone predecessor impact relations automatically.
9. No-material-impact conclusion is bounded to assessed scope.
10. OpenViking traversal is candidate discovery only.

### TASK-031 — 411–420

1. Notification never grants approval/authority.
2. Recipient responsibility never grants authority.
3. Unresolved recipient stays VERIFICATION_REQUIRED.
4. Acknowledgement does not accept underlying change.
5. Escalation does not expand disclosure/authority.
6. Dedup uses source identity, not text similarity alone.
7. Materially changed source event is not silently deduped.
8. Delivery failure preserves source event truth.
9. Delivery success does not prove outcome resolution.
10. Framework contract creates no email/Slack/webhook/scheduler runtime.

## 22. Verification and Task checkpoint strategy

Use TDD and dependency checkpoints:

1. Add scenarios `381–420` and structural verifier; observe expected RED before production semantic edits.
2. Implement TASK-036 and TASK-030 foundations; each gets focused verification and completion checkpoint.
3. Only after both foundation checkpoints, activate/implement TASK-029; focused verification and checkpoint.
4. Only after TASK-029 + TASK-030 completion, activate/implement TASK-031; focused verification.
5. Propagate Framework 1.14.0 templates/starter stamps and run cumulative AFFECTED.
6. Run prospective full branch diff hygiene against stacked parent and relevant canonical base.
7. Freeze final candidate and record candidate HEAD/tree/Framework-Source tree.
8. Run exactly one final `RELEASE_FULL` on unchanged candidate.
9. Commit release evidence only; preserve Framework-Source candidate tree.
10. Terminalize TASK-036/030/029/031, OUT-008/AUTH-008/ACT-020/ENV-008 and fresh-observe completion commit.

The final RELEASE_FULL is not rerun on an unchanged valid candidate. Candidate defects invalidate the candidate, require correction + affected re-verification + new freeze, then one final run on the corrected candidate.

## 23. Backward compatibility and migration

Framework 1.14.0 is additive and backward-compatible at Schema 1.0.0.

- Existing initialized Projects remain pinned and do not automatically acquire `Project-Change-Feed/`.
- Direct-to-Latest upgrade is the adoption path.
- Feed absence is valid unless a Project explicitly adopts it for an incremental consumer.
- Existing `92` relation truth is preserved; reconciliation does not mass-change `ASSERTED` to `CORROBORATED`.
- Brownfield relation assertions require fresh counterpart evidence before any state change.
- No notification recipient, delivery channel, standing external disclosure authority, impact record, or feed content is synthesized during upgrade.
- Historical amendments/specs/evidence are preserved as historical truth.

## 24. Non-goals

This suite does **not** create:

- watcher, crawler, webhook, daemon, background agent, scheduler, event bus, queue, CDC runtime, graph-sync runtime;
- email/Slack/Teams/SMS/webhook delivery or notification bot;
- cross-Project write/mutation/upgrade/approval propagation;
- `[Impact]`, `[Notify]`, `[Reconcile]`, `[Feed]`, or another Registered Command;
- `EVENT-*`, `FEED-*`, `IMPACT-*`, `NOTIFY-*`, `RECON-*`, or another Project Source Stable-ID family;
- a central canonical graph/history/event database;
- automatic `REL-*` reciprocal creation or automatic corroboration;
- automatic issue/risk/drift/conflict/change-request creation from feed/impact/notification analysis;
- automatic Project Knowledge promotion;
- publication/push/merge authority;
- external disclosure authority or secret-value storage.

## 25. Acceptance criteria

The suite is acceptable when:

1. Framework 1.14.0 defines optional `Project-Change-Feed/` as bounded/rebuildable/non-authoritative with source checkpoint and retention semantics.
2. Feed entries represent material source changes without new Project Source Stable-ID/event authority.
3. TASK-030 preserves TASK-022 exact relation vocabulary/reciprocal rules, requires authoritative counterpart evidence for `CORROBORATED`, and never writes another Project's assertion automatically.
4. `DEPENDS_ON/SUPPORTS` inverse is not invented.
5. TASK-029 defines `DIRECT | POTENTIAL | UNKNOWN` with provenance/review requirements and no cross-Project mutation.
6. Feed/OpenViking alone cannot prove a material DIRECT impact.
7. TASK-031 defines notification eligibility, `ROUTINE | ATTENTION | URGENT`, recipient/ack/escalation/dedup/failure semantics while preserving `notification ≠ approval ≠ authority`.
8. No notification delivery/runtime or new notification Stable-ID family is created.
9. TASK dependency checkpoints enforce TASK-036 + TASK-030 → TASK-029 → TASK-031.
10. Registered Command set remains exactly the existing seven commands.
11. Scenarios `381–420` are contiguous/unique and GREEN after implementation.
12. Maintained starter/template/release/migration surfaces agree on Framework 1.14.0 and preserve local Project Source pin 1.7.0.
13. TASK-042/TASK-043/TASK-028/TASK-032 historical/current invariants remain preserved.
14. Cumulative AFFECTED and one final unchanged-candidate RELEASE_FULL pass, release evidence is committed, and OUT-008 lifecycle terminalizes with an observed completion commit.
15. Publication remains NOT_PUSHED unless separately authorized.
