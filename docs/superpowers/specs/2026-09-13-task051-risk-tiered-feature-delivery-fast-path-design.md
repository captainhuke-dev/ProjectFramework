# TASK-051 Risk-Tiered Feature Delivery Fast Path — Design

Date: `2026-09-13` (Asia/Bangkok)
Task: `TASK-051`
Source issue: GitHub Issue `#29` — `TODO: Design risk-tiered Feature Delivery Fast Path`
Design state: `USER_APPROVED_FINAL_DESIGN / WRITTEN_SPEC_SELF_REVIEWED`
Implementation state: `NOT_STARTED`
Approval basis: ACTOR-001 chose Derived Delivery Tier option A, authority-gated Continuous Delivery option B, conditional MEDIUM review option B, tier + acceptance-boundary verification option B, then instructed the Agent to choose all remaining recommended design options and complete the Goal without repeated option prompts.
Goal lifecycle: `OUT-019 / AUTH-019 / ACT-031 / ENV-019`
Base repository: `captainhuke-dev/ProjectFramework`
Task branch: `task051-feature-delivery-fast-path`
Task branch base: `7d7463b` (local TASK-050 terminal reconciliation; canonical `origin/main` baseline remains `4039be4`)
Target release: Framework `1.17.0` / Schema `1.0.0` / release format `3`
Release classification: `BACKWARD_COMPATIBLE_FEATURE_DELIVERY_WORKFLOW_CONTRACT`

## 1. Purpose

Define a deterministic **Feature Delivery Fast Path** that allows genuinely low-risk feature work to reach durable Task completion in one working session where appropriate, without weakening ProjectFramework authority, location, evidence, release, integration, security, or completion semantics.

The design addresses GitHub Issue #29 directly:

1. define `LOW | MEDIUM | HIGH` delivery classes and blast-radius criteria;
2. define minimum authority/location preflight per class;
3. define when stable governance/location evidence can be reused instead of reread;
4. define verification and review requirements per class;
5. define when independent review is mandatory, conditional, or unnecessary;
6. preserve Material Git-backed Task `DONE` as affected verification PASS plus an observed completion commit;
7. preserve Preview/explicit approval and stricter gates for governance authority, bootstrap, Root/Binding, security, destructive, production, external, or otherwise high-risk changes;
8. define interruption/recovery so unrelated non-Git failures do not invalidate still-valid Git evidence;
9. define safe parallelism without weakening combined-candidate evidence; and
10. clarify when direct Git/GitHub repository operations are appropriate so MCP is not retained merely to represent nonexistent application runtime/process/UI state.

This is a workflow/governance contract. It does not implement a scheduler, CI system, policy engine, review bot, merge bot, daemon, router, validator, or runtime orchestration service.

## 2. Problem

ProjectFramework already has strong progressive verification and evidence reuse, but normal feature delivery can still inherit release-grade ceremony too early.

The current Framework already provides:

- canonical `R0 READ_ONLY | R1 REVERSIBLE_LOCAL | R2 SHARED_STATE | R3 EXTERNAL_OR_IRREVERSIBLE`;
- `TASK_LOCAL_FAST`, `CHECKPOINT_INTEGRITY`, `RELEASE_FULL`, and `INTEGRATION_GATE`;
- state-bound evidence reuse and selective invalidation;
- Base Freshness and `Mergeable ≠ Acceptable`;
- Material Git-backed Task completion commits;
- persistent `[Goal]` authority and continuation semantics;
- risk-tiered postflight;
- optional capability profiles with `independent_review: REQUIRED | OPTIONAL | NOT_REQUIRED`;
- tool/MCP eligibility profiles;
- strict publication-state separation: Task DONE ≠ MERGED ≠ PUSHED ≠ RELEASED; and
- checkpoint/recovery semantics including unknown-result verification.

What is missing is one feature-delivery contract that composes these primitives into a predictable fast path. Without that contract, an Agent can over-read governance, over-persist intermediate state, over-review bounded changes, or run release-level verification at Task boundaries where focused affected verification would be sufficient.

## 3. Design Goals

The contract MUST:

- materially reduce elapsed ceremony for genuinely low-risk work;
- preserve canonical Risk `R0–R3` and existing authority rules;
- make LOW/MEDIUM/HIGH deterministic enough for two competent Agents to reach the same class from the same evidence;
- make uncertainty escalate rather than silently downgrade risk;
- separate Task acceptance from release acceptance and integration acceptance;
- reuse still-valid state-bound evidence rather than mechanically rereading unchanged stable sources;
- allow one-session implementation without repeated Framework-level approval prompts when an active Goal/AUTH already covers the bounded scope;
- permit direct Git/GitHub repository operations when they are the natural state owner and current tool policy permits them;
- preserve fail-closed behavior for unknown authority, location, blast radius, reviewer capability, target freshness, or side-effect result;
- preserve auditability through bounded evidence rather than transcript dumping; and
- remain documentation/governance-first with no runtime enforcement dependency.

## 4. Non-Goals

TASK-051 does NOT:

- replace `R0–R3` with another risk family;
- create a new Stable-ID family for delivery tiers;
- make LOW an authority class;
- make LOW equivalent to merge/push permission;
- auto-merge, auto-push, auto-release, or auto-deploy;
- make every R1 change LOW or every R2 change MEDIUM mechanically;
- waive Root Governance, Project Location Binding, bootstrap, security, disclosure, secret, destructive, production, or R2/R3 gates;
- eliminate `RELEASE_FULL` from release/equivalent acceptance;
- eliminate `INTEGRATION_GATE` before integration/publication against a mutable target;
- guarantee that every LOW feature finishes in one session;
- require `Project-Execution/` profiles to exist before Fast Path can be used;
- require MCP merely because an MCP exists;
- add a task scheduler, multi-agent orchestrator, queue, watcher, CI/CD system, validator/CLI, review service, or deployment runtime; or
- auto-upgrade initialized Brownfield Projects to Framework 1.17.

## 5. Chosen Architecture

Chosen architecture: **Derived Delivery Tier over canonical Risk, with tiered Task acceptance and unchanged release/integration boundaries.**

```text
active Project authority / identity / location
+ active Goal/AUTH scope
+ highest applicable R0-R3 action risk
+ affected scope and dependency blast radius
+ sensitive-surface flags
+ uncertainty / evidence quality
+ stricter Project/tool/capability/trust overlays when present

        ↓

Derived Delivery Tier
LOW | MEDIUM | HIGH

        ↓

minimum feature-delivery workflow
preflight → implementation → verification/review → commit → postflight → Task DONE

        ↓ only when separately authorized

INTEGRATION_GATE → push/PR/merge/publication action

        ↓ at release/equivalent acceptance boundary

RELEASE_FULL on the exact final unchanged release candidate
```

`LOW | MEDIUM | HIGH` is workflow vocabulary only. It is not Project lifecycle state, Epistemic Status, Git freshness state, AUTH state, or a Stable-ID family.

## 6. Rejected Alternatives

### 6.1 Direct mapping `R0/R1 → LOW`, `R2 → MEDIUM`, `R3 → HIGH`

Rejected as insufficient because blast radius, sensitive surfaces, uncertainty, and dependency impact can make an R1 change materially unsafe for LOW treatment.

### 6.2 Separate LOW/MEDIUM/HIGH risk model parallel to `R0–R3`

Rejected because it would create competing Risk semantics and ambiguity over which system controls authority, preflight, postflight, and escalation.

### 6.3 LOW implies automatic publication

Rejected because delivery efficiency must not synthesize push/merge/publication authority. `commit ≠ push ≠ merge ≠ release` remains binding.

### 6.4 Capability-profile-only review

Rejected as incomplete because a Project without optional `Project-Execution/capabilities.md` must still have a deterministic minimum review contract. Optional profiles remain stricter overlays.

### 6.5 Evidence-driven verification with no tier floor

Rejected because it would keep the current ambiguity: two Agents could select materially different minimum verification for the same change.

## 7. Canonical Risk Remains `R0–R3`

Delivery classification never weakens existing Risk semantics:

```text
R0 READ_ONLY
R1 REVERSIBLE_LOCAL
R2 SHARED_STATE
R3 EXTERNAL_OR_IRREVERSIBLE
```

Rules:

1. determine highest applicable canonical Risk for the actions required by the bounded outcome;
2. derive delivery tier from that Risk plus blast radius, sensitive surfaces, and uncertainty;
3. apply all existing authority rules for that Risk independently;
4. apply the delivery-tier workflow as an additional minimum; and
5. when rules conflict, the stricter requirement wins.

A delivery tier may **escalate** required workflow. It may never downgrade or bypass canonical Risk, authority, binding, trust, disclosure, secret, publication, destructive, or platform/tool gates.

## 8. Delivery Tier Classification

### 8.1 LOW

LOW is eligible only when all material conditions are true:

- required mutation is `R1 REVERSIBLE_LOCAL` or lower;
- target Project/repository/workspace identity is verified;
- scope is narrow and bounded;
- affected dependencies/invariants are known and limited;
- the change has an obvious durable rollback/revert path;
- no shared/external side effect is required for Task completion;
- no HIGH sensitive-surface flag applies;
- verification route is known and available;
- uncertainty is low; and
- current Project-specific rules do not require stronger treatment.

Typical LOW examples include a bounded implementation bug fix, small additive local feature, isolated documentation behavior change, or a narrow test-backed local refactor that does not alter authority/safety/publication semantics.

### 8.2 MEDIUM

MEDIUM applies when impact is still bounded but at least one of the following is true:

- the change is R1 but spans multiple coupled surfaces/dependencies;
- the change includes a bounded R2 shared-state action with exact target and applicable authority;
- semantics are additive but cross-surface consistency matters;
- rollback is known but not trivial;
- verification must cover multiple dependency/invariant groups;
- review value is material even when not automatically mandatory; or
- uncertainty is material but still bounded enough to avoid HIGH.

MEDIUM MUST NOT include R3 action as part of its required completion path.

### 8.3 HIGH

HIGH applies when any of the following is true:

- any required action is R3;
- destructive or materially irreversible effect;
- Root Governance / `FRAMEWORK-001` authority semantics;
- Project Location Binding mutation;
- bootstrap authority/routing semantics;
- security/trust/disclosure/secret-handling policy semantics;
- schema or Stable-ID compatibility semantics;
- production/deployment mutation or production-source mutation concern;
- cross-Project mutation;
- release/publication policy changes that alter safety/authority guarantees;
- Fast Path / verification / review gate semantics themselves are materially changed;
- blast radius is wide, cannot be bounded confidently, or crosses unknown dependencies;
- required evidence is materially incomplete/conflicted; or
- uncertainty is high enough that MEDIUM cannot be proven.

HIGH does not mean work is forbidden. It means the Feature Delivery Fast Path cannot reduce the stricter approval/review/verification obligations.

## 9. Highest-Tier Outcome Rule

A Task is governed by the highest delivery tier required by its bounded outcome.

An Agent MAY split work into independently tiered Tasks/actions only when independence is evidenced by all of:

- distinct desired outcomes or independently completable work packages;
- no hidden sequencing dependency;
- no shared mutable prerequisite that couples acceptance;
- no cross-package safety invariant requiring joint acceptance; and
- separate evidence can truthfully prove each result.

Artificially splitting a HIGH/MEDIUM outcome into LOW fragments to avoid review, approval, or verification is prohibited.

## 10. Sensitive-Surface Escalation

The following are mandatory HIGH triggers when the proposed change alters their controlling semantics, not merely because a file contains related documentation:

- Root/Project governance authority;
- bootstrap or authority-routing behavior;
- Project Location Binding;
- Risk/authorization/approval semantics;
- security/trust boundary semantics;
- secret handling or outbound disclosure semantics;
- schema/Stable-ID compatibility;
- destructive/irreversible policy;
- production/deployment safety boundary;
- release/integration verification or review gates; and
- cross-Project write authority.

A documentation-only correction that merely clarifies text without changing these controlling semantics may remain LOW or MEDIUM based on normal scope/blast-radius rules.

## 11. Common Invariant Preflight

Before any Material feature mutation, every tier performs one common preflight sufficient to establish:

1. active Project bootstrap and `FRAMEWORK-001` authority are resolved;
2. exact Project/repository/workspace and Canonical Implementation Source are resolved when applicable;
3. active Goal/AUTH/ENV scope covers the intended local mutation;
4. current branch/worktree and relevant Git baseline are observed;
5. affected scope, dependency impact, and sensitive surfaces are identified;
6. highest applicable `R0–R3` is identified;
7. `LOW | MEDIUM | HIGH` is derived and recorded in Task/working evidence when Material;
8. required review and verification floor are known before implementation;
9. rollback/revert route is known for R1/R2 work; and
10. stricter Project/tool/capability/trust/disclosure rules are applied when those optional profiles are active.

This preflight is a bounded decision record, not a requirement to reread every governance file on every small change.

## 12. State-Bound Preflight Evidence Reuse

Stable authority/location/governance reads MAY be reused inside a continuing Goal/session when the evidence is explicitly bound to unchanged material assumptions.

Reusable evidence may include:

- Project UUID and repository identity;
- active `FRAMEWORK-001` revision;
- stable Project Location Binding values;
- stable task/requirement/decision scope;
- tool/capability profile revision when applicable;
- exact candidate/commit/tree identity;
- previously established affected-scope assumptions; and
- prior verification evidence bound to the same candidate state.

Reuse is invalidated selectively when a material assumption changes.

Always fresh-check when required by existing semantics, including:

- current branch/worktree and working-tree state before Material Git work;
- R2/R3 applicable authority immediately before required shared/external mutation;
- mutable integration target at `INTEGRATION_GATE`;
- target identity before remote/shared action;
- reviewer eligibility/availability when required and potentially stale;
- runtime/external resulting state for R3; and
- any prerequisite whose freshness class or observed drift makes reuse unsafe.

Unknown evidence validity fails closed to reread/reverify or higher tier; it never defaults to reuse.

## 13. Per-Tier Minimum Preflight

| Dimension | LOW | MEDIUM | HIGH |
|---|---|---|---|
| Bootstrap/Project authority | resolved; stable evidence may be reused if unchanged | resolved; refresh affected authority when material | fresh-read applicable authority and sensitive prerequisites |
| Project/repo/workspace identity | exact and verified | exact and verified | exact and freshly confirmed where risk requires |
| Canonical Risk | R0/R1 only for required completion actions | R1/R2; no required R3 | any; R3 or sensitive trigger makes HIGH |
| Blast radius | narrow/bounded | bounded multi-surface/dependency | wide, sensitive, unknown, or unbounded |
| Rollback | obvious revert/prior revision | explicit rollback route | explicit recovery/rollback plus stricter approval where applicable |
| Review plan | known; independent review default NOT_REQUIRED | conditional review decision recorded | independent review REQUIRED absent explicit governed waiver |
| Verification plan | focused affected checks | broader affected/dependency checks | comprehensive affected/risk checks + stronger acceptance gates |
| Shared/external authority | not required for local Task DONE | fresh exact authority for R2 action | exact fresh authority/approval for all applicable R2/R3 actions |

## 14. Review Policy

The delivery tier supplies a minimum review policy while optional Project capability rules may be stricter.

### 14.1 LOW review

Default: `independent_review: NOT_REQUIRED`.

Self-review plus focused verification is sufficient unless another active Project rule independently requires review.

### 14.2 MEDIUM review

Default: `OPTIONAL`, promoted to `REQUIRED` by any material trigger such as:

- unfamiliar subsystem or unclear ownership boundary;
- broad/multi-surface semantic coupling;
- weak or missing automated verification for the affected behavior;
- concurrency/ordering complexity;
- security/trust adjacency even if the change does not alter security policy itself;
- non-trivial migration/backward-compatibility exposure;
- important user-facing protocol/interface semantics;
- material assumptions that cannot be directly tested;
- reviewer requirement in active capability/project policy; or
- Agent uncertainty that materially affects acceptance confidence.

When no trigger exists, MEDIUM may complete with producer self-review plus the required affected verification.

### 14.3 HIGH review

Default: `independent_review: REQUIRED`.

A required independent reviewer must be distinct from the primary producing instance where practicable and eligible for the work under active capability/disclosure/trust rules.

Reviewer unavailability is NOT a waiver. Work remains blocked at the applicable acceptance/integration gate unless ACTOR-001 or another valid authority supplies an explicit governed waiver permitted by higher-level rules.

A waiver must be evidence-backed and action/scope-specific; it must not silently change the default contract.

## 15. Review Evidence Validity

Review is state-bound.

A review remains reusable only while the reviewed candidate and material assumptions remain unchanged.

The following invalidate affected review evidence:

- candidate/tree/content change in reviewed scope;
- semantic target movement affecting assumptions;
- conflict resolution or rebase result changing reviewed behavior;
- newly discovered dependency impact;
- changed requirement/Decision/Risk premise; or
- changed reviewer eligibility where that eligibility is material.

Non-semantic target movement that does not alter reviewed assumptions may require only freshness confirmation, consistent with existing `INTEGRATION_GATE` semantics.

## 16. Verification Architecture

TASK-051 preserves the current separation:

```text
Task acceptance
  → delivery-tier minimum affected verification

Logical checkpoint
  → CHECKPOINT_INTEGRITY when a checkpoint is actually needed

Release/equivalent acceptance
  → RELEASE_FULL once on the final unchanged candidate

Integration/publication against mutable target
  → INTEGRATION_GATE
```

A LOW Task is not forced through release-grade verification merely because it is a feature.

A LOW Task that becomes part of a Framework Release Candidate is still included in the release-level `RELEASE_FULL` at the release boundary.

## 17. LOW Verification Floor

LOW requires at minimum:

- `TASK_LOCAL_FAST` or equivalent focused affected checks;
- tests/checks directly exercising changed behavior when such tests exist;
- checks for directly affected dependencies/invariants;
- `git diff --check` or equivalent diff hygiene for Git-backed text/code changes;
- direct resulting-state confirmation;
- no unexplained working-tree residue affecting the result; and
- an observed durable completion commit before Material Git-backed Task `DONE`.

No independent review or `RELEASE_FULL` is required at the LOW Task boundary solely because the Task exists.

## 18. MEDIUM Verification Floor

MEDIUM requires at minimum:

- broader AFFECTED verification across materially coupled surfaces/dependencies;
- explicit compatibility/invariant checks for cross-surface semantics;
- required review when MEDIUM review triggers apply;
- direct resulting-state confirmation, including exact remote/shared result for any authorized R2 action;
- diff hygiene;
- observed durable completion commit; and
- selective reverification of any evidence invalidated by changes during implementation/review.

If impact cannot remain bounded, reclassify HIGH before acceptance.

## 19. HIGH Verification Floor

HIGH requires at minimum:

- comprehensive affected/risk-scoped verification appropriate to the change;
- required independent review absent an explicit governed waiver;
- all existing Preview/explicit approval gates applicable to the sensitive operation;
- fresh applicable authority and target checks;
- explicit rollback/recovery plan;
- strong postflight proving resulting external/runtime/shared state when applicable;
- release/equivalent acceptance verification required by the active Framework path; and
- observed durable completion commit for Git-backed implementation.

When HIGH work produces a Framework Release Candidate, one final `RELEASE_FULL` on the unchanged candidate remains mandatory.

## 20. Release Acceptance Boundary

Framework `1.17.0` does not redefine `RELEASE_FULL`.

A completed Framework Release Candidate or equivalent semantic acceptance point receives one final current-distribution `RELEASE_FULL` on the exact unchanged candidate, subject to existing state-bound evidence-reuse rules.

The full run is not repeated merely because:

- multiple LOW/MEDIUM Tasks contributed to the same unchanged candidate;
- an exact verified transport occurred; or
- a previously verified candidate remains byte/tree-identical with unchanged material assumptions.

Any candidate mutation after full verification invalidates the affected/full evidence as current Framework rules already require.

## 21. Integration / Publication Boundary

Fast Path does not create publication authority.

One session MAY continue from local Task completion through push/PR/merge only when all are true:

1. active Goal/AUTH already covers the exact remote action and exact governed target;
2. current tool/platform rules permit the action;
3. repository/binding/target identity is verified;
4. `INTEGRATION_GATE` is run immediately before the mutable-target action;
5. prior Task/release/review evidence remains valid; and
6. any R2/R3/shared/external approval requirement is independently satisfied.

If publication is not authorized, the Fast Path ends successfully at local verified Task `DONE`. That is not a failure or incomplete local implementation state.

## 22. One-Session Delivery Contract

For eligible LOW work, the desired default flow is:

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

The Agent SHOULD avoid artificial ceremony that does not improve safety for LOW work, including:

- rereading stable governance sources solely because a new micro-step started;
- creating standalone design/spec/plan documents for every bounded change when the Task/Goal already contains sufficient intent and acceptance criteria;
- persisting a new Project Source revision after every small edit;
- running unrelated full-distribution verification before Task completion;
- requesting repeated Framework-level approval for already-authorized R1 work inside an active Goal; or
- forcing an independent reviewer when no active rule or trigger requires one.

One-session delivery is an objective, not an SLA. External blockers, platform/tool confirmations, test failures, reviewer requirements, changed requirements, target drift, or interrupted sessions may legitimately extend work.

## 23. Design / Plan Artifact Scaling

Feature delivery artifact depth is proportional to complexity and tier.

### LOW

A separate durable architectural spec or implementation plan is NOT required by ProjectFramework when:

- intent and acceptance criteria are already explicit in Task/Goal;
- no new public/governed interface or architecture is introduced;
- affected scope is narrow; and
- implementation can be safely understood and verified from the bounded Task context.

Tool/provider workflows may impose their own design gate; such higher-level rules remain binding.

### MEDIUM

Use a short design/plan when cross-surface sequencing, compatibility, rollback, or review scope benefits from durable structure. A full architectural spec is required when the change introduces a material interface/architecture contract.

### HIGH

Use the existing full design/approval/plan workflow appropriate to the affected governance or architecture. Fast Path never uses HIGH classification to justify skipping required Preview or explicit approval.

## 24. Persistence and Logical Checkpoints

Fast Path reduces redundant persistence, not durable continuity.

A Logical Checkpoint is required when material continuation state must survive interruption, handoff, or phase transition. It is not required after every micro-step.

For LOW one-session work with no handoff/interruption, the Task completion commit plus final lifecycle/evidence update may be the principal durable checkpoint.

When a checkpoint is needed:

- persist the minimum current usable state/pointers;
- use `CHECKPOINT_INTEGRITY` rather than blanket release regression;
- record exact next action/blocker;
- preserve active Goal/AUTH/ENV pointers; and
- never treat unpersisted in-session memory as durable truth after interruption.

## 25. Interruption and Recovery

Recovery follows durable state, not chat memory.

### 25.1 Git-backed work

After interruption:

1. fresh-read branch/worktree/HEAD/working-tree state;
2. resolve the last durable completion/checkpoint commit;
3. compare observed candidate/tree with evidence bindings;
4. reuse still-valid unaffected evidence;
5. rerun only invalidated/newly affected checks when impact remains bounded; and
6. escalate verification/tier if impact becomes unknown or unbounded.

A non-Git tool/session failure does not by itself invalidate Git evidence bound to an unchanged commit/tree.

### 25.2 Non-idempotent or external side effects

Before a non-idempotent side effect, record intent/checkpoint as required by existing MCP/continuity semantics.

Connection loss after possible submission yields `RESULT_VERIFICATION_REQUIRED`. Verify resulting state before retry. If the result cannot be proven, fail closed rather than repeating a potentially duplicate effect.

## 26. Parallelism Contract

Parallelism is allowed only when evidence integrity remains composable.

### 26.1 Always preferred parallel work

The following may run in parallel when they do not depend on one another:

- read-only discovery;
- independent research/context reads;
- independent test/verification groups against the same frozen candidate;
- independent review of a stable candidate; and
- analysis of disjoint affected dependencies.

### 26.2 Parallel mutation

Parallel mutation requires explicit proof that work packages are disjoint enough to combine safely:

- no overlapping files/records or shared mutable owner unless a deterministic merge contract exists;
- no sequencing dependency;
- no shared external side effect;
- no common invariant that can only be evaluated after both changes;
- each work package has a known base/candidate identity; and
- final combined candidate receives affected verification covering the composition.

Sub-work evidence is not automatically acceptance evidence for the combined candidate.

### 26.3 Tier defaults

- LOW: parallel read/test work is encouraged; disjoint local mutation may be parallel when independence is evidenced.
- MEDIUM: parallel mutation requires stronger dependency/scope proof; otherwise parallelize read/review/test only.
- HIGH: mutation is serialized by default. Independent review or read-only analysis may be parallel against a stable checkpoint, but safety-critical mutation is not parallelized merely for speed.

If independence is uncertain, serialize.

## 27. Direct Git / GitHub Repository Operations

ProjectFramework is documentation/governance-first and has no application runtime merely because the repository exists.

For repository-native state, direct Git/GitHub operations MAY be the natural execution route when:

- Project/repository identity is verified;
- active tool policy does not disallow that route;
- exact action authority exists;
- platform/tool confirmation rules are satisfied; and
- no material non-repository runtime/UI/process state must be observed through another owner.

Examples include:

- reading repository files/history/refs;
- branch/worktree operations;
- local commits;
- remote ref/read operations;
- GitHub Issue/PR reads; and
- authorized GitHub shared-state actions.

MCP MUST NOT be retained solely to represent nonexistent runtime/process/UI state.

However:

- direct Git/GitHub does not bypass Project Tool/MCP Execution Profile when one is active;
- direct Git/GitHub does not grant authority;
- connected/recent/similar tools never become eligible automatically;
- secrets/credentials remain outside Project Source;
- push/merge/publication remain shared-state actions with their own authority; and
- MCP or another tool remains appropriate when it is the declared owner/route for material non-repository state or an active Project execution profile requires it.

## 28. Tool / Capability / Trust Overlay

`Project-Execution/` remains optional/applicability-driven.

Fast Path MUST function without optional profiles. When profiles exist, they constrain the delivery contract:

- `tools.md` constrains eligible execution routes;
- `capabilities.md` may make independent review or capability classes stricter;
- `trust.md` may constrain data/code/artifact/execution crossings; and
- TASK-026 disclosure rules remain independent for external providers.

Absence of an optional profile does not fabricate permissive policy beyond the base Framework contract.

## 29. Task DONE Contract

TASK-051 preserves current Material Git-backed Task completion semantics.

A Material Git-backed feature Task may be `DONE` only when:

1. intended bounded result exists;
2. applicable tier minimum verification passes;
3. required review is complete or an explicit valid waiver is recorded;
4. resulting state is directly confirmed at the tier-appropriate depth;
5. required evidence is persisted;
6. required result exists in observed durable commit(s);
7. working tree is clean or remaining changes are explicitly unrelated/explained; and
8. blockers/next action/current lifecycle are truthful.

`WIP commit ≠ Task DONE` remains binding.

Task DONE does not imply MERGED, PUSHED, RELEASED, ARTIFACT_PUBLISHED, or DEPLOYED.

## 30. Mid-Task Reclassification

Delivery tier is not permanently fixed at Task start.

Reclassify upward when implementation reveals:

- broader affected scope;
- R2/R3 side effects not previously known;
- sensitive-surface impact;
- changed requirement/Decision/Risk premise;
- unexpected dependency coupling;
- insufficient rollback;
- review trigger;
- unknown target/result; or
- uncertainty that invalidates the current class.

Down-classification after new evidence is allowed only before acceptance when the Agent can positively prove that the higher-risk assumption was false and no higher-tier action/effect occurred. It cannot retroactively erase required evidence/approval for an action already performed.

## 31. Failure / Fail-Closed Conditions

Affected Fast Path work fails closed when:

- active Project authority cannot be resolved;
- required binding/location/implementation source is unresolved;
- active Goal/AUTH does not cover the intended mutation;
- delivery tier cannot be safely classified;
- blast radius is unknown/unbounded;
- LOW would require R2/R3 action for completion;
- HIGH required review is unavailable and no valid waiver exists;
- required verification route is unavailable or materially inconclusive;
- candidate/evidence identity cannot be proven;
- remote/shared action target is unresolved;
- `INTEGRATION_GATE` cannot prove acceptable freshness/evidence validity;
- non-idempotent external result is unknown and cannot be verified; or
- higher-level system/tool/platform safety rules block the operation.

Independent in-scope work may continue when the blocker affects only one separable action and continuation is safe.

## 32. Brownfield and Greenfield Behavior

Framework 1.17 adds a workflow contract, not mandatory new Project files or Stable-ID families.

GREENFIELD Projects created under 1.17 inherit the Fast Path semantics through the normal Framework root/template set.

Existing initialized Projects do not auto-adopt 1.17. They remain pinned and receive the new contract only through governed `[Project Upgrade]` / Direct-to-Latest semantics.

No Brownfield Project is required to create `Project-Execution/` merely to use base Fast Path semantics.

## 33. ProjectFramework Canonical Self-Host Boundary

During TASK-051 local implementation:

- Framework distribution may advance to a verified Framework 1.17.0 candidate;
- active ProjectFramework Project Source and `PROJECT-BOOTSTRAP.md` remain pinned to 1.16.0;
- this is not drift requiring immediate local Root mutation because canonical self-host reconciliation is governed by the existing TASK-049 post-merge contract; and
- after a verified 1.17 release is merged to canonical `main`, a separately authorized canonical self-host reconciliation is required before release integration is fully reconciled.

OUT-019 does not authorize that future Root/self-host promotion.

## 34. Version / Compatibility Classification

Target: Framework `1.17.0` / Schema `1.0.0` / release format `3`.

Reason for minor release:

- introduces new additive workflow vocabulary and delivery behavior;
- does not change semantic slots;
- does not add a Stable-ID family;
- does not add a Registered Command;
- does not remove an existing interface;
- preserves `R0–R3`, AUTH, Project Location Binding, release/publication state separation, and existing migration/pinning semantics; and
- initialized Projects do not auto-adopt the new contract.

No Schema bump is required.

## 35. Normative Framework Surfaces

Implementation should update the minimum current surfaces needed to make the contract coherent:

- `Framework-Source/FRAMEWORK-RELEASE.yaml`;
- `Framework-Source/MIGRATION-NOTES.md`;
- new current amendment `Framework-Source/references/framework-governance-amendment-260913-task051-feature-delivery-fast-path.md`;
- `Framework-Source/references/core-governance-rules.md`;
- `Framework-Source/SKILL.md`;
- root `README.md` current-release / Fast Path guidance;
- `Framework-Source/templates/00-project-source-framework.md`;
- `Framework-Source/templates/core-document-skeletons.md`;
- maintained concrete starter/mockup surfaces that carry current Framework version/summary text;
- pressure scenarios; and
- TASK-051 task/evidence/current-state lifecycle records.

Current historical amendments/specs/plans/evidence remain unchanged when their prior semantics were true at capture time.

Vendor thin launchers should change only if the active launcher contract actually embeds affected Fast Path semantics or version-bound text. Do not expand thin launchers merely to duplicate Core/SKILL policy.

## 36. Pressure Scenario Contract

Allocate the next contiguous scenario range after current `1–472`.

Recommended TASK-051 range: `473–504` (32 scenarios).

Coverage must include at least:

1. LOW derived from bounded R1 without sensitive flags;
2. R1 escalated to MEDIUM by multi-surface blast radius;
3. R1 escalated to HIGH by sensitive authority semantics;
4. R2 never LOW;
5. R3 always HIGH;
6. uncertainty escalates rather than downgrades;
7. no parallel LOW/MEDIUM/HIGH Risk family replacement for R0–R3;
8. common preflight reuse of stable evidence;
9. volatile Git state fresh-check despite reused governance;
10. fresh R2/R3 authority before mutation;
11. LOW focused verification without Task-boundary RELEASE_FULL;
12. MEDIUM broader affected verification;
13. HIGH comprehensive verification;
14. release candidate still requires RELEASE_FULL;
15. INTEGRATION_GATE remains separate from RELEASE_FULL;
16. LOW independent review not required by default;
17. MEDIUM trigger makes independent review required;
18. HIGH reviewer unavailable is not waiver;
19. explicit governed HIGH review waiver remains bounded;
20. one-session LOW avoids redundant Project-level prompts/checkpoints;
21. LOW artifact scaling does not require formal spec/plan for bounded existing flow;
22. HIGH preserves Preview/explicit approval;
23. non-Git failure does not invalidate unchanged Git evidence;
24. unknown external result requires result verification before retry;
25. safe parallel read/test work;
26. disjoint LOW mutation parallelism with combined-candidate verification;
27. overlapping/uncertain parallel mutation serializes;
28. HIGH mutation serialized by default;
29. direct Git/GitHub repo-native operation allowed when policy/authority permit;
30. MCP not required for nonexistent runtime state;
31. direct Git/GitHub never grants push/merge authority; and
32. Task DONE remains completion commit + tier verification and is distinct from publication.

Scenario numbering must be collision-checked before implementation.

## 37. Verification Strategy for TASK-051 Implementation

TASK-051 itself changes the Framework verification/review workflow contract, so the implementation is HIGH under the proposed sensitive-surface rule. Current Framework 1.16 rules govern implementation until 1.17 is accepted.

Implementation verification therefore uses:

1. TDD RED pressure scenarios first;
2. focused structural checks after each normative/propagation phase;
3. cumulative AFFECTED verification covering release identity, Core, SKILL, amendment, README, migration, templates/starters, scenario numbering, historical preservation, no-runtime boundary, Task/Project Source truth, and diff hygiene;
4. freeze one final Framework 1.17.0 candidate;
5. run exactly one final `RELEASE_FULL` on that unchanged candidate;
6. bind release evidence to candidate HEAD/tree/Framework-Source tree;
7. commit release evidence and Task/Goal terminal reconciliation locally; and
8. fresh-observe completion commit + clean/explained tree before external completion claim.

Any candidate mutation after `RELEASE_FULL` invalidates the final candidate and requires affected reverification, a new freeze, and a new final run on the corrected candidate.

## 38. Implementation Boundary

Authorized implementation is Markdown/YAML governance/documentation plus local verification tooling used only as scratch evidence.

Do NOT add:

- executable Fast Path runtime;
- task scheduler;
- autonomous agent orchestrator;
- CI/CD pipeline;
- merge/release bot;
- policy engine;
- background watcher;
- MCP router/failover runtime;
- credential store;
- persistent database;
- validator/CLI as a new Framework product requirement; or
- external AI review calls without separately valid disclosure authority.

Scratch verification code may exist in ignored/non-candidate working state when useful, but is not part of Framework distribution unless separately designed and approved.

## 39. Publication Boundary for OUT-019

AUTH-019 authorizes verified local completion only.

The following remain outside current Goal authority:

- push branch;
- create/update PR as a Material shared-state delivery action;
- merge to `main`;
- tag;
- GitHub Release;
- canonical self-host Root promotion to 1.17;
- destructive branch/worktree cleanup; and
- deployment/publication outside repository-local commits.

If later explicitly authorized, those operations must fresh-resolve target/authority and run applicable `INTEGRATION_GATE` / post-publication reconciliation.

## 40. Completion Criteria

TASK-051 design/implementation is acceptable when all of the following are true:

1. `LOW | MEDIUM | HIGH` is defined as Derived Delivery Tier, not a parallel Risk family;
2. LOW/MEDIUM/HIGH classification and blast-radius escalation are deterministic;
3. sensitive surfaces force HIGH when controlling safety/authority semantics change;
4. common preflight + state-bound reuse is normative;
5. R2/R3 fresh-authority behavior is preserved;
6. review policy is LOW not required / MEDIUM conditional / HIGH required absent valid waiver;
7. Task verification is tiered while release acceptance still uses `RELEASE_FULL`;
8. `INTEGRATION_GATE` remains separate and mandatory where applicable;
9. Task DONE remains affected verification + observed completion commit for Material Git-backed work;
10. one-session LOW delivery avoids unnecessary rereads, checkpoints, formal artifacts, and approval prompts;
11. interruption/recovery selectively preserves valid Git evidence;
12. unknown non-idempotent result verifies before retry;
13. safe parallelism is evidence-based and combined-candidate verification is explicit;
14. direct Git/GitHub repo-native operations are permitted only within tool/authority boundaries;
15. MCP is not treated as required runtime state when no such state exists;
16. Brownfield Projects do not auto-adopt 1.17;
17. current self-host remains 1.16 until separately authorized post-merge reconciliation;
18. pressure scenarios cover the new contract;
19. cumulative AFFECTED passes;
20. exactly one final `RELEASE_FULL` passes on the unchanged accepted candidate;
21. release evidence is state-bound and durable;
22. TASK-051 / OUT-019 terminal lifecycle is persisted locally; and
23. no unauthorized publication, Root/Binding mutation, runtime automation, external disclosure, or secret persistence occurs.

## 41. Spec Self-Review Checklist

The written spec must pass before implementation planning:

- completeness scan is clean and no unresolved design choice remains;
- no competing Risk family;
- no implicit publication authority;
- no contradiction between one-session delivery and Task DONE durability;
- no contradiction between tier verification and release/integration gates;
- no silent waiver of independent review;
- no MCP-required assumption for nonexistent runtime state;
- no bypass of optional stricter tool/capability/trust profiles;
- no auto-upgrade of Brownfield Projects;
- no accidental self-host Root promotion in OUT-019;
- clear pressure scenario range with no known collision;
- implementation scope is achievable as one implementation plan; and
- publication boundary remains explicit.
