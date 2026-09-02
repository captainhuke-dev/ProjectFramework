# TASK-028 + TASK-032 Integrity & Remediation Suite — Design

Date: `2026-09-02` (Asia/Bangkok)
Tasks: `TASK-028` then `TASK-032`
Design state: `USER_APPROVED_DIRECTIONS / GOAL_SELECTED / WRITTEN_SPEC_APPROVED_BY_GOAL`
Approval basis: the Task registry already contains approved directions for TASK-028 and TASK-032, and the user explicitly invoked `[Goal] ทำ Task-028 และตาม Task-032 จนกว่าจะเสร็จ` on 2026-09-02. That Goal selects those approved directions for continuous bounded execution. Push/publication remains outside the Goal.

## 1. Baseline and release classification

Canonical baseline at suite creation:

```text
origin/main: a5e73faf3d13ed8baad6a259c52e15efc981804f
Framework: 1.12.2
Schema: 1.0.0
release format: 3
pressure scenarios: 1–356
Registered Commands: [Project Status], [Project Path], [Project Upgrade], [Session], [Goal], [Meeting]
TASK-028: TODO / approved direction / design spec required
TASK-032: TODO / approved direction / design spec required
```

The cumulative suite target is **Framework 1.13.0 / Schema 1.0.0 / release format 3**. This is a minor release because TASK-028 adds a new public Registered Command, `[Project Audit]`. TASK-032 adds governance/workflow semantics without a new command, semantic slot, Stable-ID family, authority family, or executable remediation service.

The older roadmap placeholders (`1.10.0`) are historical planning values and are reclassified because canonical Framework has already advanced to 1.12.2.

## 2. Chosen suite architecture

The suite is dependency-ordered:

```text
TASK-028 [Project Audit]
  read-only inspection
  → findings + evidence + unknowns + governed repair routes
  → TASK-028 focused verification + completion checkpoint
  → TASK-032 becomes READY

TASK-032 Governed Repair / Remediation
  authorized proposal/execution
  → resulting-state verification
  → affected re-audit
  → cumulative suite verification/release
```

The central invariant is exact:

```text
Audit finds ≠ Audit fixes
Finding ≠ Issue/Drift/Conflict/Migration record
Repair proposal ≠ Repair authority
ACT DONE ≠ repair outcome verified
```

TASK-028 may diagnose and recommend an existing canonical route, but it performs no Project mutation. TASK-032 governs how a separately authorized repair is proposed, executed, rolled back when applicable, verified, and re-audited.

### Alternatives considered

1. **One combined audit-and-fix command** — rejected. It would collapse read-only diagnosis into mutation authority and defeat the explicit TASK-028 boundary.
2. **Separate 1.13.x releases for TASK-028 and TASK-032** — valid but rejected for this Goal. It would duplicate release propagation and make TASK-032 consume a just-released interface while both Tasks are intentionally selected as one dependency suite.
3. **Chosen: one cumulative 1.13.0 release with two Task completion checkpoints** — preserves TASK-028 → TASK-032 ordering while sharing one amendment, release propagation, cumulative AFFECTED pass, and one final unchanged-candidate RELEASE_FULL.

## 3. TASK-028 — `[Project Audit]` command identity and intent

Canonical command identity:

```text
[Project Audit]
```

Literal `[` and `]` are required; matching inside brackets is case-insensitive under existing Registered Command rules. Canonical display remains `[Project Audit]`.

Invocation forms:

```text
[Project Audit]
[Project Audit] <explicit bounded focus>
```

The bare command audits the current Project across all applicable categories for which authoritative/current evidence can be resolved. A trailing user focus narrows the audit; it never expands authority or causes mutation.

`[Project Audit]` is always **read-only**. It does not repair, migrate, rewrite, create/close canonical issue objects, push, change bindings, resolve conflicts, or materialize authority.

## 4. `[Project Audit]` Strict Governed Interface

TASK-043 remains binding. `[Project Audit]` is a Registered Command and therefore a Strict Governed Interface.

Required top-level dimensions are exact and ordered:

```text
Scope
→ Health
→ Categories
→ Findings
→ Unknowns
→ Evidence
→ Repair Routes
→ Continuity
```

Every recognized `[Project Audit]` response keeps those dimensions in that order. Semantic-equivalent narrative replacement is not compliant. If no item exists for a dimension, the dimension still appears with an explicit empty/none representation. If evidence is unavailable, the governed dimension remains and uses `UNKNOWN` / `VERIFICATION_REQUIRED` as applicable.

The Registered Command pipeline remains:

```text
Recognize
→ Resolve Contract
→ Fresh Observe
→ Materialize Governed Structure
→ Populate
→ Command Contract Completeness Gate
→ Response Close Completeness Gate
→ Emit
```

The command-specific gate runs before TASK-042's global close gate and does not replace it.

## 5. Audit health vocabulary

Audit category health reuses the existing Project health vocabulary exactly:

```text
GREEN | AMBER | RED | UNKNOWN
```

No new audit lifecycle or severity family is created.

Interpretation:

- `GREEN` — required evidence for the category is sufficiently resolved and no material inconsistency is found.
- `AMBER` — a material but non-invalidating stale/reference/consistency concern exists and requires review or bounded remediation.
- `RED` — a material contradiction, broken current reconstructability, invalid authority/routing condition, or other defect blocks safe reliance on the affected scope.
- `UNKNOWN` — required evidence cannot be resolved sufficiently to assess the category; `UNKNOWN` never means healthy.

There is no opaque global numeric score. `Health` presents the category state matrix plus concise reasons. Consumers may notice the worst category, but the Framework does not invent a hidden aggregate algorithm.

## 6. Audit categories

`Categories` evaluates applicable categories in this canonical order:

1. **Bootstrap & Identity** — root bootstrap resolution, active `FRAMEWORK-001`, Project identity, authority-entry chain.
2. **Routing & Current State** — active `01`, `03`, `09`, `14`, active-file routing, current-vs-history separation, continuation consistency.
3. **Canonical Records & Stable IDs** — current Stable-ID resolvability, canonical object homes, active current payload availability without archive dependence.
4. **Bindings & Git Freshness** — Project Location Binding state, environment-local routing, current branch/worktree, canonical target freshness when material, repository identity, unsupported fallback/inference.
5. **Continuity & Persistence** — Handoff/current action consistency, Material persistence state, stale continuation, `PERSISTENCE_PENDING` correctness.
6. **Conditional Surfaces & Migration** — applicable `06–08`, `40`, `60`, `91`, `92`, Brownfield/migration requirements, occupied-slot/collision handling when material.
7. **Relations, Knowledge & Execution Profiles** — only when applicable: `REL-*` / Project Graph, Project Knowledge, Tool/MCP Execution Profile, Agent/Model Capability Profile, Release/Publication and Trust surfaces.

Applicability follows existing Framework rules. Optional categories/surfaces are not fabricated merely to make the audit appear complete. Their absence is a finding only when the active Project contract says they are applicable/required.

## 7. Findings are presentation, not a new canonical object family

An audit finding is a bounded command result, not a Stable ID and not Project authority. Do not create `AUDIT-*`, `FINDING-*`, or similar canonical families.

Each material finding reports enough information for review:

```text
Category
Observed condition
Health state (AMBER | RED | UNKNOWN as applicable)
Authoritative/current source pointer(s)
Why it matters
Existing canonical object/home if already materialized
Governed repair route or investigation route
```

The audit may reference existing `ISS-*`, `DRIFT-*`, `CONFLICT-*`, `MIG-*`, `RISK-*`, `DEP-*`, `CR-*`, or other records. It must not create, change, close, or accept any of them.

If a finding should become durable Project truth, that happens only through a separate authorized governed action using the existing canonical home.

## 8. Bounded output without silent loss

The command output must be usable for human review without becoming an unbounded dump.

Allowed bounding techniques:

- aggregate repetitive findings that share the same root cause while preserving count and affected scope;
- summarize evidence ranges/pointers rather than copying entire source documents;
- order material findings before informational context;
- narrow by explicit user focus;
- report additional finding counts and an exact follow-up scope when the detailed set cannot reasonably fit in one response.

The command must not silently discard material `RED`, `AMBER`, or `UNKNOWN` findings. Bounding is presentation compaction, not evidence suppression.

## 9. Freshness and unknown handling

Audit freshness follows the existing truth/freshness contracts:

- stable/current Project Source records may be reused when their evidence remains valid;
- volatile Git/worktree/remote/runtime/binding facts are freshly observed when they affect the category;
- unavailable connector/tool/runtime evidence remains explicit as `UNKNOWN / VERIFICATION_REQUIRED`;
- one unavailable source does not erase other category results;
- the command never reconstructs missing active contracts from memory or assumes a healthy state from absence of evidence.

A tool failure does not automatically become `PERSISTENCE_PENDING`; that state remains reserved for required durable continuation state that is actually unpersisted.

## 10. `Repair Routes` dimension

`Repair Routes` is advisory routing only. It identifies the existing canonical home/gate needed if the user later chooses remediation.

Examples:

```text
stale current-vs-expected truth      → DRIFT-* / existing owner
competing authoritative semantics    → CONFLICT-* + Decision/approval as applicable
migration/collision requirement      → MIG-*
material issue                       → ISS-*
material proposed change             → CR-* when change-control semantics apply
execution work                       → ACT-* / ENV-* under valid AUTH-*
Root/Binding mutation                → explicit approval + FRAMEWORK-001 revision flow
shared/external mutation             → applicable R2/R3 authority and target checks
```

The audit never creates these objects merely by naming a route.

## 11. TASK-032 — Governed Project Repair / Remediation

TASK-032 adds no Registered Command. It defines the governance workflow used after a finding or other integrity defect is selected for repair.

A repair begins only from an explicit remediation request/Goal/valid authorization. An audit result by itself is not permission.

A remediation proposal resolves at least:

```text
Source finding / evidence
Affected scope
Canonical owner/home
Desired resulting state
Risk class (R0–R3)
Applicable authority / approval
Prerequisites and freshness checks
Ordered repair actions
Reversibility / rollback
Verification of resulting state
Affected re-audit / resulting-state confirmation
Evidence and lifecycle updates
```

This proposal can be represented using existing `CR-*`, `ACT-*`, `AUTH-*`, `ENV-*`, issue/drift/conflict/migration records, and relevant Decisions/Requirements. No `REPAIR-*`, `REM-*`, or parallel remediation Stable-ID family is added.

## 12. Repair classification and canonical owner

Before mutation, determine the defect type and current canonical owner.

Examples:

- stale derived/current routing metadata → repair the current owning document through normal revision/promotion/history flow;
- material truth mismatch → existing `DRIFT-*` semantics;
- competing authoritative truth → `CONFLICT-*`; do not pick a winner by recency;
- migration/slot collision → `MIG-*`;
- proposed material scope/behavior change → `CR-*`/Decision path as applicable;
- plain execution defect with already-approved intended state → bounded `ACT-*` under valid `AUTH-*`.

Repair never moves authoritative payload into the wrong home merely because it is convenient.

## 13. Authority, Risk, and mutation boundary

TASK-032 reuses existing Risk/authority rules:

```text
R0 READ_ONLY
R1 REVERSIBLE_LOCAL
R2 SHARED_STATE
R3 EXTERNAL_OR_IRREVERSIBLE
```

A valid repair authority must cover the exact affected scope and operation. Goal/ENV authority may be used only when it already covers the repair. Push/publication, destructive operations, Root/Binding mutation, external disclosure, and irreversible effects remain separately bounded according to existing contracts.

Correct diagnosis does not grant repair authority. Capability, Tool availability, repository access, Project Graph visibility, Knowledge content, and audit severity do not grant authority either.

## 14. Semantic conflicts are not auto-repairable

When a defect is a genuine disagreement over intended requirements, accepted Decisions, architecture, authority, Risk acceptance, relation truth, or other semantic policy, remediation must not silently choose one value.

Route to the existing Decision/Change/Conflict path with required user/owner authority. A repair workflow may prepare evidence and a proposal, but semantic resolution is a governed decision, not housekeeping.

## 15. Reversibility and rollback

A repair proposal states the rollback/recovery approach when practical.

- R1/local reversible changes should identify the prior durable state or revision that can be restored.
- Git-backed repairs preserve commits/history rather than relying on destructive reset as the normal completion path.
- R2/R3 or materially irreversible repairs require the applicable explicit authority and resulting-state verification.
- If rollback cannot be meaningful, that limitation is explicit before execution.

Rollback does not substitute for fixing the canonical source correctly; it is a recovery boundary.

## 16. Post-repair verification and re-audit

Repair completion requires fresh resulting-state evidence appropriate to the affected scope.

Required sequence:

```text
execute authorized repair
→ verify direct resulting state
→ verify affected references/dependencies
→ re-audit the affected audit category/categories or perform equivalent resulting-state confirmation
→ update evidence/current lifecycle records
→ only then close the repair action / related finding route when justified
```

`ACT DONE ≠ repair outcome verified`. A command/tool returning success is insufficient when the intended current truth is not freshly confirmed.

Re-audit is read-only and does not create a loop that self-authorizes further fixes. New findings require their own classification/authority.

## 17. Relationship between TASK-028 and TASK-032 lifecycle

TASK-028 must complete first.

TASK-028 completion checkpoint requires:

- `[Project Audit]` normative contract implemented;
- Registered Command surfaces aligned;
- strict dimension order and read-only boundary verified;
- audit-focused pressure scenarios GREEN;
- affected command/template surfaces pass focused verification;
- completion commit observed.

After that checkpoint:

```text
TASK-028 → DONE
TASK-032 readiness → READY
TASK-032 → IN_PROGRESS
OUT-007 remains ACTIVE
```

TASK-032 then implements remediation semantics and focused verification. The cumulative suite remains open until final 1.13.0 AFFECTED + unchanged-candidate RELEASE_FULL + release evidence + terminal Project Source reconciliation are complete.

## 18. Framework surfaces

Expected current surfaces:

### Normative / release

- `Framework-Source/FRAMEWORK-RELEASE.yaml`
- new `Framework-Source/references/framework-governance-amendment-260902-task028-task032.md`
- `Framework-Source/references/core-governance-rules.md`
- `Framework-Source/SKILL.md`
- `Framework-Source/MIGRATION-NOTES.md`

### User/distribution surfaces

- root `README.md`
- `Framework-Source/templates/00-project-source-framework.md`
- `Framework-Source/templates/core-document-skeletons.md`
- maintained `Framework-Source/templates/project-source-mockup/` current starter stamps and relevant README/root pointer text

The thin ChatGPT/Claude launchers do not contain the command registry and SHOULD remain unchanged unless verification proves a current command-discovery requirement there. Their parity/size is still checked.

### Validation / lifecycle

- `Framework-Source/tests/pressure-scenarios.md`
- `docs/superpowers/PROJECT-TASKS.md`
- suite spec/plan/release evidence
- active Project Source Goal/action/evidence/lifecycle revisions

No executable implementation artifact is in scope.

## 19. Pressure-scenario contract

Reserve scenarios `357–380` for this suite.

TASK-028 scenarios cover:

- literal brackets and case-insensitive command identity;
- strict top-level dimension order;
- read-only/no-auto-fix behavior;
- cross-surface `00/01/03/09/14` integrity;
- unresolved Stable IDs/canonical homes;
- fresh Git/binding evidence and explicit unknowns;
- conditional `REL-*`/Knowledge/Execution-profile applicability;
- findings are not Stable IDs;
- reuse of existing issue/drift/conflict/migration families;
- bounded aggregation without silent material loss;
- partial/unavailable source behavior;
- style/narrative requests cannot weaken the Registered Command interface;
- command gate still precedes response-close gate;
- audit does not mutate registries merely to persist findings.

TASK-032 scenarios cover:

- explicit remediation authority requirement;
- repair through canonical owner/home;
- R2/R3/shared/irreversible gates remain independent;
- semantic conflict requires Decision/approval instead of auto-repair;
- reversibility/rollback declaration;
- direct post-repair verification;
- affected re-audit/resulting-state confirmation;
- `ACT DONE ≠ repair outcome verified`;
- no new remediation Stable-ID family/repair command;
- no runtime validator/scanner/auto-fix/repair bot is implied.

## 20. Verification strategy

Use TDD in dependency order.

1. Add scenarios `357–380` and a scratch structural verifier before production semantic edits.
2. Observe expected RED for absent 1.13.0 audit/remediation contracts while baseline invariants remain GREEN.
3. Implement TASK-028 normative/command surfaces first.
4. Run focused TASK-028 verification and commit its completion checkpoint before activating TASK-032.
5. Implement TASK-032 remediation semantics.
6. Run focused TASK-032 verification.
7. Propagate release/template/starter surfaces and run cumulative AFFECTED verification.
8. Freeze the final Framework 1.13.0 candidate and capture candidate/tree/Framework-Source-tree identity.
9. Run exactly one final `RELEASE_FULL` on the unchanged candidate.
10. Commit release evidence, terminalize TASKs/OUT/AUTH/ACT/ENV, and observe the completion commit.

The final RELEASE_FULL is not rerun on an unchanged valid candidate. A candidate defect invalidates the candidate and requires correction, affected re-verification, a new candidate identity, then a new final RELEASE_FULL.

## 21. Backward compatibility and migration

Framework 1.13.0 is additive and backward-compatible at Schema 1.0.0.

- Existing initialized Projects remain pinned and do not gain `[Project Audit]` automatically.
- `[Project Upgrade]`/Direct-to-Latest remains the adoption path.
- Brownfield Projects do not receive generated issue/repair records merely because the new audit command exists.
- Existing command contracts remain unchanged except command-help/registry surfaces gaining `[Project Audit]`.
- TASK-042 response-close and TASK-043 strict-interface semantics remain unchanged and compose with the new command.
- Historical amendments/specs/evidence remain historical; do not rewrite them to mention 1.13.0.

## 22. Non-goals

This suite does **not** create:

- validator, scanner, linter executable, CLI, audit daemon, watcher, scheduler, background agent;
- automatic Project repair, repair bot, auto-migration, auto-conflict resolution;
- a `[Project Repair]` command or any repair command;
- `AUDIT-*`, `FINDING-*`, `REPAIR-*`, `REM-*`, or another Stable-ID family;
- automatic `ISS-* / DRIFT-* / CONFLICT-* / MIG-* / CR-*` creation from an audit;
- email/Slack/webhook notification semantics (TASK-031 remains separate);
- cross-Project impact/reconciliation execution (TASK-029/TASK-030 remain separate);
- push/publication authority, destructive authority, Root/Binding authority, or external disclosure authority.

## 23. Acceptance criteria

The suite is acceptable when:

1. `[Project Audit]` is registered and behaves as a Strict Governed Interface with exact top-level order `Scope → Health → Categories → Findings → Unknowns → Evidence → Repair Routes → Continuity`.
2. Audit category health reuses `GREEN | AMBER | RED | UNKNOWN` and unavailable evidence stays explicit.
3. Audit is read-only and never creates/fixes canonical records automatically.
4. Findings route to existing canonical homes without a new finding/audit family.
5. TASK-032 defines a complete remediation proposal/authority/Risk/rollback/verification/re-audit contract using existing homes.
6. Semantic conflicts cannot be auto-repaired.
7. TASK-028 reaches verified completion before TASK-032 implementation is treated as active.
8. Scenarios `357–380` are contiguous/unique and GREEN after implementation.
9. Current command registry, Core/SKILL/root template/README/release/migration/starter surfaces agree on Framework 1.13.0.
10. TASK-042/TASK-043 semantics and historical artifacts remain preserved.
11. No executable audit/repair runtime or new Stable-ID family exists.
12. Cumulative AFFECTED and one final unchanged-candidate RELEASE_FULL pass, release evidence is committed, and Goal lifecycle is terminally reconciled with observed completion commit.
