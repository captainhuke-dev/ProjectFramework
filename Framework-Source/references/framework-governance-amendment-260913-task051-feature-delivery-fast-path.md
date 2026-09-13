# Framework Governance Amendment — TASK-051 Risk-Tiered Feature Delivery Fast Path

Date: `2026-09-13`
Framework target: `1.17.0`
Schema: `1.0.0`
Release format: `3`
Source Task: `TASK-051`
Source Issue: GitHub Issue `#29` — `TODO: Design risk-tiered Feature Delivery Fast Path`

## 1. Scope and Release Classification

Framework `1.17.0` adds a governed **Risk-Tiered Feature Delivery Fast Path** for normal feature work. The release is backward-compatible and additive: it changes no Project Source semantic slot, Stable-ID family, Registered Command, Project Source Schema, release descriptor format, or canonical Risk family.

The Fast Path composes existing ProjectFramework primitives. It does not create a scheduler, merge bot, CI/CD pipeline, background watcher, validator/CLI, MCP router, policy engine, or autonomous delivery runtime.

## 2. Canonical Risk Is Unchanged

Canonical Risk remains exactly:

```text
R0 READ_ONLY
R1 REVERSIBLE_LOCAL
R2 SHARED_STATE
R3 EXTERNAL_OR_IRREVERSIBLE
```

`LOW | MEDIUM | HIGH` is a **Derived Delivery Tier** used only to choose the minimum feature-delivery workflow. It is not Project Risk authority, lifecycle state, Epistemic Status, Git freshness, or a Stable-ID family.

Delivery tier MAY make a workflow stricter. It MUST NOT lower or bypass canonical Risk, `AUTH-*`, `DEL-*`, Root Governance, Project Location Binding, trust, disclosure, secret, destructive, production, publication, or platform/tool gates. When requirements differ, the stricter applicable rule wins.

## 3. Delivery Tier Classification

Derive delivery tier from the highest applicable `R0–R3` action risk plus affected scope, dependency blast radius, sensitive-surface flags, uncertainty, rollback, and current evidence quality.

### LOW

A Material feature is eligible for `LOW` only when all required completion actions are `R0` or `R1`, target identity is verified, scope is narrow and bounded, dependencies/invariants are known, rollback is straightforward, no shared/external mutation is required for local Task completion, no HIGH sensitive-surface trigger applies, verification is available, and uncertainty is low.

A required `R2` action is never LOW. A required `R3` action is always HIGH.

### MEDIUM

Use `MEDIUM` when the outcome remains bounded but spans multiple coupled surfaces/dependencies, requires broader compatibility verification, has non-trivial rollback, or includes an exact-target authorized `R2` shared-state action. MEDIUM MUST NOT contain a required `R3` action.

### HIGH

Use `HIGH` when any required action is `R3`; when destructive/irreversible effects exist; when blast radius is wide, unknown, or cannot be bounded confidently; or when a controlling sensitive surface changes.

## 4. Sensitive-Surface HIGH Escalation

A change that alters controlling semantics of any of the following is HIGH even when the file mutation itself is reversible R1:

- Root Governance / `FRAMEWORK-001`;
- Project Location Binding;
- bootstrap authority or authority-routing semantics;
- Risk, authorization, delegation, or approval semantics;
- security, trust, disclosure, or secret-handling policy;
- Schema or Stable-ID compatibility;
- destructive/irreversible policy;
- production/deployment safety boundaries;
- cross-Project write authority;
- release/integration acceptance controls; or
- review/verification gate semantics, including this Feature Delivery Fast Path.

A documentation correction that does not alter controlling semantics is classified by normal scope/blast-radius rules rather than by filename alone.

## 5. Highest-Tier Outcome and Anti-Splitting Rule

The bounded outcome is governed by the highest required delivery tier.

Work MAY be split into independently tiered packages only when each package has an independently completable outcome, no hidden sequencing dependency, no shared mutable prerequisite that couples acceptance, no safety invariant requiring joint acceptance, and separate evidence that can truthfully prove each result.

An Agent MUST NOT split MEDIUM/HIGH work into LOW fragments merely to avoid review, approval, verification, or authority gates.

## 6. Common Invariant Preflight

Before Material feature mutation, run one **common invariant preflight** that resolves enough current truth to begin safely:

1. active Project Bootstrap and valid `FRAMEWORK-001`;
2. exact Project/repository/workspace and Canonical Implementation Source when applicable;
3. active Goal/`AUTH-*`/`ENV-*` scope covering the intended mutation;
4. current branch/worktree/HEAD/working-tree state for Git-backed work;
5. affected scope, dependency impact, and sensitive surfaces;
6. highest applicable canonical `R0–R3` Risk;
7. derived `LOW | MEDIUM | HIGH` delivery tier;
8. required review and verification floor;
9. rollback/revert route for R1/R2 work; and
10. stricter Project/tool/capability/trust/disclosure overlays when present.

The common invariant preflight is a bounded decision step. It is not a requirement to reread every stable governance document before every micro-step.

## 7. State-Bound Preflight Evidence Reuse

Still-valid state-bound evidence MAY be reused while the evidence's bound revision, identity, candidate, dependencies, and material assumptions remain unchanged.

Reusable evidence may include Project UUID/repository identity, active `FRAMEWORK-001` revision, stable Project Location Binding values, stable Task/Requirement/Decision scope, applicable tool/capability profile revision, exact commit/tree identity, and previously proven affected-scope assumptions.

Reuse MUST be selectively invalidated when a material bound assumption changes. Unknown validity fails closed to reread/reverification or higher delivery tier.

The following remain fresh-check obligations when applicable:

- current branch/worktree/HEAD/working-tree state before Material Git work;
- applicable R2/R3 authority immediately before the shared/external mutation;
- exact remote/shared target identity before action;
- reviewer eligibility/availability when required and potentially stale;
- current Canonical Integration Target/Base Freshness at `INTEGRATION_GATE`; and
- resulting external/runtime state for R3.

## 8. Minimum Preflight by Tier

### LOW

LOW MUST have verified Project/repository/workspace identity, active in-scope authority for the local R1 work, fresh volatile Git observation, bounded affected scope, clear rollback, and known verification route. Stable governance/location evidence MAY be reused when unchanged.

### MEDIUM

MEDIUM MUST satisfy LOW preflight plus explicit cross-surface/dependency impact, broader verification plan, review-trigger evaluation, and fresh exact authority/target checks immediately before any R2 action.

### HIGH

HIGH MUST fresh-read applicable authority and sensitive prerequisites at the point required by existing governance, verify exact target identity, preserve required Preview/approval gates, establish recovery/rollback, resolve required independent review, and define strong resulting-state verification before mutation/acceptance.

## 9. Review Policy

The delivery tier supplies a minimum review floor. Stricter active Project/capability/trust rules remain binding.

### LOW

Independent review is `NOT_REQUIRED` by default. Producer self-review plus focused affected verification is sufficient when no stricter rule applies.

### MEDIUM

Independent review is `OPTIONAL` by default and becomes `REQUIRED` when a material trigger exists, including:

- unfamiliar subsystem or unclear ownership boundary;
- broad or multi-surface semantic coupling;
- weak or missing automated verification for affected behavior;
- concurrency/ordering complexity;
- security/trust adjacency;
- non-trivial migration/backward-compatibility exposure;
- important user-facing protocol/interface semantics;
- material assumptions that cannot be directly tested;
- an active capability/Project policy requiring review; or
- material Agent uncertainty affecting acceptance confidence.

### HIGH

Independent review is `REQUIRED` by default. A required reviewer must be distinct from the primary producing instance where practicable and eligible under applicable capability, disclosure, trust, and tool rules.

Reviewer unavailability is not an implicit waiver. The applicable acceptance/integration gate remains blocked until an eligible reviewer is available or valid authority grants an explicit governed waiver.

A governed waiver MUST be bounded to the exact scope/action/candidate for which it is granted and MUST NOT become a standing review exemption silently.

## 10. Review Evidence Validity

Review evidence is state-bound. Candidate/tree/content changes in reviewed scope, semantic target movement affecting assumptions, conflict-resolution/rebase results, newly discovered dependency impact, changed Requirement/Decision/Risk premise, or changed reviewer eligibility invalidate affected review evidence.

Non-semantic target movement that does not invalidate review assumptions may require freshness confirmation rather than unconditional repeat review, consistent with existing evidence-reuse and `INTEGRATION_GATE` semantics.

## 11. Per-Tier Task Verification

### LOW

LOW Task acceptance MUST include `TASK_LOCAL_FAST` or equivalent focused affected checks, direct tests/checks for changed behavior when available, directly affected dependency/invariant checks, diff hygiene for Git-backed changes, direct resulting-state confirmation, understood working-tree state, and an observed durable completion commit before Material Git-backed Task `DONE`.

LOW does not require `RELEASE_FULL` solely because the Task is a feature.

### MEDIUM

MEDIUM Task acceptance MUST include broader affected/dependency/invariant verification, required triggered review, direct resulting-state confirmation including exact shared result for any authorized R2 action, diff hygiene, an observed completion commit, and selective reverification of evidence invalidated during implementation/review.

If impact can no longer be bounded, reclassify HIGH before acceptance.

### HIGH

HIGH Task acceptance MUST include comprehensive affected/risk-scoped verification, required independent review absent valid governed waiver, all applicable Preview/explicit approval gates, fresh applicable authority/target checks, explicit recovery/rollback, strong resulting-state postflight, and an observed durable completion commit for Git-backed implementation.

## 12. Task Acceptance vs RELEASE_FULL vs INTEGRATION_GATE

These acceptance boundaries remain distinct:

```text
Task acceptance
  → delivery-tier minimum affected verification

Logical Checkpoint
  → CHECKPOINT_INTEGRITY only when durable continuation is needed

Release/equivalent semantic acceptance
  → RELEASE_FULL once on the exact final unchanged candidate

Integration/publication against a mutable canonical target
  → INTEGRATION_GATE
```

A Framework Release Candidate still requires `RELEASE_FULL` even when every contributing Task was LOW. A passing `RELEASE_FULL` does not permanently prove mutable target freshness; `INTEGRATION_GATE` still re-resolves current target/Base Freshness/evidence validity immediately before applicable integration/publication.

## 13. One-Session Delivery and Artifact Scaling

For eligible LOW work, the preferred one-session flow is:

```text
resolve active Goal/scope
→ reuse still-valid stable Project evidence
→ fresh-observe volatile Git state
→ classify R0/R1 + LOW
→ implement
→ focused affected verification
→ producer self-review
→ direct resulting-state check
→ completion commit
→ fresh-read commit + clean/explained tree
→ Task DONE
```

One-session delivery is an objective, not an SLA.

The Agent SHOULD avoid redundant stable-governance rereads, one-checkpoint-per-edit persistence, repeated Framework-level approval prompts already covered by active Goal/AUTH for R1 work, unnecessary independent review, and Task-boundary release verification.

ProjectFramework does not itself require a standalone architectural spec/implementation plan for a bounded LOW change to an existing flow when Task/Goal intent and acceptance criteria are already sufficient. Higher-level product/tool/development workflows may impose their own design gate and remain binding.

MEDIUM uses a short durable design/plan when cross-surface sequencing, compatibility, rollback, or review scope materially benefits. HIGH preserves the full applicable design/Preview/approval/plan workflow.

## 14. Logical Checkpoints and Persistence Scaling

Fast Path reduces redundant persistence, not durable continuity.

Use a Logical Checkpoint when continuation state must survive interruption, handoff, or material phase transition. For one-session LOW work with no handoff/interruption, the completion commit plus final lifecycle/evidence update may be the principal durable checkpoint.

When a checkpoint is needed, persist the minimum usable continuation state and use `CHECKPOINT_INTEGRITY`; Logical Checkpoint still does not imply `RELEASE_FULL`.

## 15. Interruption and Recovery

After interruption of Git-backed work, fresh-read branch/worktree/HEAD/working-tree state, resolve the last durable checkpoint/completion commit, compare candidate/tree identity with bound evidence, reuse still-valid unaffected evidence, and rerun only invalidated/newly affected checks while impact remains bounded.

A non-Git execution/session failure does not by itself invalidate Git evidence bound to an unchanged commit/tree.

For a non-idempotent external/shared action whose submission result is unknown, set `RESULT_VERIFICATION_REQUIRED`, verify resulting state before retry, and fail closed if the result cannot be proven. Missing response never authorizes a blind retry.

## 16. Parallelism and Combined Candidate

Independent read-only discovery, research, test groups, dependency analysis, and review MAY run in parallel against the same stable candidate when no ordering dependency exists.

Parallel mutation requires positive evidence of independence: no overlapping owner/files/records unless a deterministic merge contract exists, no sequencing dependency, no shared external side effect, no coupled safety invariant requiring joint acceptance, and known base/candidate identity.

Even when disjoint LOW mutation is performed in parallel, the final **combined candidate** MUST receive affected verification covering the composition. Sub-work evidence does not automatically prove the combined candidate.

MEDIUM mutation requires stronger dependency/scope proof. HIGH mutation is serialized by default; independent read/review analysis may still run in parallel against a stable checkpoint.

If independence is uncertain, serialize.

## 17. Direct Git/GitHub and MCP Boundary

For repository-native state, **direct Git/GitHub** operations MAY be used when Project/repository identity is verified, active tool policy permits the route, exact action authority exists, platform/tool confirmation requirements are satisfied, and no material non-repository runtime/process/UI state must be observed through another owner.

ProjectFramework is documentation/governance-first and has no application runtime merely because a repository exists. MCP MUST NOT be retained solely to represent nonexistent runtime/process/UI state.

Direct Git/GitHub eligibility never grants authority. It does not bypass an active `Project-Execution/tools.md` policy, secrets/disclosure rules, R2/R3 gates, or publication authority. Push/PR/merge remain shared-state actions requiring exact authority and applicable `INTEGRATION_GATE`.

MCP remains appropriate when it is the declared/required owner for actual material non-repository state or when active tool policy requires it.

## 18. Tool Capability Trust and Disclosure Overlays

`Project-Execution/` remains optional/applicability-driven. Fast Path works without optional profiles.

When present:

- `tools.md` constrains eligible execution routes;
- `capabilities.md` may make capability/review requirements stricter;
- `trust.md` constrains material crossings; and
- outbound external-provider use remains subject to disclosure governance.

Absence of an optional profile does not create authority and does not fabricate a permissive external/disclosure policy.

## 19. Task DONE and Publication Separation

A Material Git-backed Task may become `DONE` only when the intended bounded result exists, applicable tier verification passes, required review is complete or validly waived, resulting state is directly confirmed, required evidence is persisted, the result exists in observed durable commit(s), and working-tree state is clean or understood.

`WIP commit ≠ Task DONE` remains binding.

Task DONE remains distinct from `MERGED`, `PUSHED`, `RELEASED`, artifact publication, and deployment. Fast Path never makes LOW delivery an implicit publication grant.

## 20. Brownfield Greenfield and No-Runtime Boundary

GREENFIELD Projects created under Framework 1.17 inherit this workflow through the normal current Framework distribution.

Existing Brownfield Projects do not auto-adopt 1.17. They remain pinned and receive Fast Path semantics only through governed Direct-to-Latest `[Project Upgrade]`.

Framework 1.17 adds no new Project Source Stable-ID family, semantic slot, Registered Command, runtime service, scheduler, watcher, queue, CI/CD system, merge/release bot, policy engine, validator/CLI, MCP failover router, credential store, or persistent database.

The Feature Delivery Fast Path is a Human/Agent governance workflow contract built from existing authority, Risk, evidence, verification, continuation, and publication semantics.
