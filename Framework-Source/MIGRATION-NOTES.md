# MIGRATION-NOTES

Per-release migration guidance for upgrading an initialized Project's Framework pin. These notes are routing/documentation aids, **not** normative authority — Core Governance and the latest amendment win on any conflict. Absence of a section for a transition means no notes exist yet; do not invent them.

## 1.20.0 → 1.21.0 (current)

### Affected distribution surfaces

- Framework identity becomes `1.21.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-059 V3 Forward-Port Runtime Control Contract.
- The **Durable Runtime Control Contract** is added as declarative record semantics: `RUNTIME_CONTRACT` (durable runtime-control binding: control generation, fence epoch, liveness, continuation policy, version pinning), `RUNTIME_EVENT` (Runtime Event Journal; append-only, sequence-ordered, runtime-owned namespace, strict writer isolation), `EXECUTION_CHECKPOINT` (derived recovery accelerator traceable to the journal), `EFFECT_POLICY` (mediation + idempotency/reversibility/reconciliation classes), `EFFECT_PERMIT` (short-lived, single-use, non-transferable, bound; never `AUTH-*`), and `RLM_EXECUTION_PROFILE` (provider-neutral recursion depth + hierarchical budgets) — all `record_version: "1.0"` as new record types.
- Supervisor/control generation: `Supervisor decision ≠ AUTH`; `Supervisor liveness ≠ Execution Ownership Grant`; `Heartbeat ≠ completion evidence`; a new control generation invalidates prior-generation leases/fences/permits without rewriting the Wave A V2 ownership epoch or canonical Task state; fence identity is the pair `(runtime_generation, fence_epoch).`
- Runtime liveness projection: lease/heartbeat is subordinate to the Framework 1.20 Execution Ownership Grant; no lease, heartbeat, or fence creates ownership or AUTH.
- Effect Gateway: mediated Material Effects transit `executor proposal → fresh authority/current-truth/precondition evaluation → Effect Permit → Gateway dispatch → source-native reconciliation`; direct uncontrolled paths for a mediated class are non-conforming; effect-surface closure is the mandated property.
- Ambiguity: no arbitrary exactly-once claims; `UNKNOWN → reconcile at source-native truth owner → APPLIED | NOT_APPLIED | PARTIAL | STILL_UNKNOWN`; unsafe blind retry is prohibited.
- Bounded continuation: finite continuation/retry budgets, wake conditions, explicit `WAIT | BLOCKED | MANUAL_RESOLUTION_REQUIRED | BUDGET_EXHAUSTED | WAITING_FOR_REAUTHORIZATION` dispositions; no automatic continuation after authority/state-binding/contract invalidation; exhaustion never implies Task DONE.
- Cancellation/compensation: `Cancellation ≠ rollback`; `Compensation ≠ history erasure`; compensation is a new governed effect with its own authority, permit, budget, evidence, and reconciliation.
- Version pinning: `runtime_contract_version` + `event_schema_version`; upgrades classify `BACKWARD_COMPATIBLE | REQUIRES_MIGRATION | INCOMPATIBLE`; incompatible code never silently reinterprets historical runtime events.
- Security boundary: no raw secret values in journal/checkpoint/evidence (`REFERENCE_ONLY | REDACTED | HASH_ONLY | classified metadata`); model/tool output is untrusted; runtime-owned events use a separate namespace; stale generation/epoch/permit attempts fail closed.
- AI-ControlTower handoff: the Python 3.14 Supervisor reference runtime is a separate AI-ControlTower Task against this conformance boundary; Prime Agent remains an optional mapping to the RLM/long-horizon Executor Profile; canonical-source cutover starts only after the amendment §18 evidence chain.
- Five optional TASK-059 starters are maintained under `templates/project-execution/`: `runtime-contract.md`, `runtime-event-journal.md`, `execution-checkpoint.md`, `effect-policy.md`, `rlm-executor-profile.md`.
- Adoption is additive and applicability-driven. Non-ControlTower Projects remain valid ProjectFramework Projects without adopting any runtime contract.
- No new Project Source semantic slot, Stable-ID family, Registered Command, Risk level, Task lifecycle value, or release-descriptor format changes.
- Wave A V2 remains authoritative and is extended compositionally, never replaced. Wave C semantics (Release Transaction, deployment saga) and cryptographic producer authentication remain excluded.

### Upgrade checklist

1. Preserve the initialized Project's local pin, current truth, Stable IDs, Project-specific rules, bindings, and history until governed promotion.
2. Preserve canonical `R0–R3` and all existing authority/risk/disclosure/secret/publication gates; 1.21 contracts may only compose with them, never weaken them.
3. Preserve Framework 1.20 Wave A V2 semantics (Compositional State Binding Hub, ownership/fencing, CAS transitions, Result Acceptance, Verification Validity) as authoritative; TASK-059 extends them compositionally.
4. Adopt TASK-059 runtime contracts only when an execution runtime is applicable; do not materialize empty contract files for completeness.
5. Do not retrofit historical/Brownfield Tasks or executions with invented journal, checkpoint, permit, or RLM state; unknown mappings remain `UNKNOWN.`
6. Preserve the distinctness of canonical Task lifecycle, operational execution state, Verification result (`PASS | FAIL | UNKNOWN`), Verification Validity (`CURRENT | STALE | INVALIDATED | UNKNOWN`), and Task DONE.
7. Preserve the invariants: `Effect Permit ≠ AUTH-*`; `Supervisor decision ≠ AUTH`; `Heartbeat ≠ completion evidence`; `Cancellation ≠ rollback`; `Compensation ≠ history erasure`; `Prime Agent role ≠ ProjectFramework dependency.`
8. Verify scenarios `591–620` while preserving cumulative scenarios `1–620` contiguous/unique.
9. For this Framework release, run cumulative affected verification then one final `RELEASE_FULL` on the exact unchanged accepted candidate.

---

## 1.19.0 → 1.20.0 (previous)

### Affected distribution surfaces

- Framework identity becomes `1.20.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-058 Wave A V2 Deterministic Execution Foundation.
- The **Compositional State Binding Hub** is added as declarative record semantics: `REVISION_SET`, `EXECUTION_INPUT_MANIFEST`, `EXECUTION_STATE_BINDING`, `EXECUTION_OWNERSHIP_GRANT` / `EXECUTION_OWNERSHIP_EVIDENCE`, `OPERATIONAL_TRANSITION`, `RESULT_ACCEPTANCE`, and `VERIFICATION_VALIDITY_EVALUATION` (all `record_version: "1.0"` as new record types).
- V2 required shapes: Task Contract `contract_version: "2.0"`, Task Record `record_version: "2.0"`, Verification Record `record_version: "2.0"`. Existing `1.0` artifacts remain valid under their original contract and are never rewritten in place.
- Canonical execution composition: Task Ready Gate PASS → eligible executor (filter-before-rank) → coordination claim → Execution Ownership Grant + scoped epoch + required fencing assurance → finalize immutable Execution State Binding → CAS `CLAIMED → EXECUTING` → Task Record observation → Generic Result Identity / Result Set → fresh Result Acceptance → Verification Basis/Evidence → `PASS | FAIL | UNKNOWN` → Verification Validity `CURRENT | STALE | INVALIDATED | UNKNOWN.`
- `Resource Identity ≠ Locator ≠ Revision`; `Coordination Claim ≠ Execution Ownership Grant`; `Task Record observation ≠ Result Acceptance`; `Verification PASS ≠ Verification Validity CURRENT`; `COORDINATION_ONLY < ACCEPTANCE_FENCED < SIDE_EFFECT_FENCED.`
- Seven optional Wave A V2 starters are maintained under `templates/project-execution/`: `revision-set.md`, `execution-input-manifest.md`, `execution-state-binding.md`, `execution-ownership.md`, `operational-transition-record.md`, `result-acceptance.md`, `verification-validity.md`; `task-contract.md`, `task-record.md`, `verification-record.md`, `project-adapter.md`, and `integration-reconciliation.md` gain explicit V2 sections with v1 compatibility preserved.
- Adoption is additive and applicability-driven. Non-ControlTower Projects remain valid ProjectFramework Projects without adopting any Wave A V2 contract.
- No new Project Source semantic slot, Stable-ID family, Registered Command, Risk level, Task lifecycle value, or release-descriptor format changes.
- Wave B/C semantics (Resume Eligibility, Continuation Budget, Memory Snapshot/automatic continuation, cryptographic producer authentication, Release Transaction/deployment-saga) and all runtime implementation remain excluded.

### Upgrade checklist

1. Preserve the initialized Project's local pin, current truth, Stable IDs, Project-specific rules, bindings, and history until governed promotion.
2. Preserve canonical `R0–R3` and all existing authority/risk/disclosure/secret/publication gates; 1.20 contracts may only compose with them, never weaken them.
3. Adopt Wave A V2 execution contracts only when applicable; do not materialize empty contract files for completeness.
4. Do not retrofit historical/Brownfield Tasks with invented Revision Sets, Input Manifests, State Bindings, ownership epochs, Result Acceptances, or Validity Evaluations; unknown mappings remain `UNKNOWN.`
5. Preserve the distinctness of canonical Task lifecycle, operational execution state, Verification result (`PASS | FAIL | UNKNOWN`), Verification Validity (`CURRENT | STALE | INVALIDATED | UNKNOWN`), and Task DONE.
6. Preserve the grant-before-binding order, fresh Result Acceptance before `VERIFYING` and again before `VERIFIED` promotion, and `RESULT_VERIFICATION_REQUIRED` unknown-effect semantics.
7. Verify scenarios `557–590` while preserving cumulative scenarios `1–590` contiguous/unique.
8. For this Framework release, run cumulative affected verification then one final `RELEASE_FULL` on the exact unchanged accepted candidate.

---

## 1.18.0 → 1.19.0


### Affected distribution surfaces

- Framework identity becomes `1.19.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-057 AI-ControlTower Governance Support Layer.
- Declarative execution contracts are added: `PLAN | TASK | VERIFY` modes, Plan Contract, Task Contract, nested Execution Envelope, mandatory Expected IPOCV, Task Record / Actual IPOCV, state-bound Verification Record, Task Ready Gate, operational execution state, Multica coordination boundary, Executor Profile / Project Adapter, filter-before-rank selection, exact-SHA verification, fresh `INTEGRATION_GATE`, and integration reconciliation.
- `R4_CTX` / `current_truth_context` is execution-time current truth, not a Risk level; canonical Risk remains exactly `R0–R3.`
- `Contract ≠ Authority`; `Eligibility ≠ Authority`; `Claim ≠ Authority`; `Verification PASS ≠ Task DONE`; Execution State never mutates canonical Task lifecycle; `VERIFIED ≠ INTEGRATION_ELIGIBLE ≠ MERGED.`
- Seven optional declarative starters are maintained under `templates/project-execution/`: `plan-contract.md`, `task-contract.md`, `task-record.md`, `verification-record.md`, `executor-profile.md`, `project-adapter.md`, `integration-reconciliation.md.`
- Adoption is additive and applicability-driven. Non-ControlTower Projects remain valid ProjectFramework Projects without adopting any contract.
- No new Project Source semantic slot, Stable-ID family, Registered Command, or release-descriptor format changes.
- No AI-ControlTower runtime, Multica runtime, Control Plane, scheduler, queue, database, state engine, router, executable adapter, merge bot, CI runner, API server, automatic DONE/reconciliation worker, Structured Core, Generated Governance, or Transaction Mode runtime is introduced.

### Upgrade checklist

1. Preserve the initialized Project's local pin, current truth, Stable IDs, Project-specific rules, bindings, and history until governed promotion.
2. Preserve canonical `R0–R3` and all existing authority/risk/disclosure/secret/publication gates; 1.19 contracts may only compose with them, never weaken them.
3. Adopt declarative contracts only when AI-ControlTower/Multica consumption is applicable; do not materialize empty contract files for completeness.
4. Do not retrofit historical/Brownfield Tasks with reconstructed Plan Contracts, IPOCV, Task Records, Executor Profiles, or Project Adapters; unknown mappings remain `UNKNOWN.`
5. Preserve the distinctness of canonical Task lifecycle, operational execution state, Verification PASS, and Task DONE.
6. Preserve `INTEGRATION_GATE`, exact-SHA candidate binding, and `RESULT_VERIFICATION_REQUIRED` unknown-result semantics.
7. Verify scenarios `529–556` while preserving cumulative scenarios `1–556` contiguous/unique.
8. For this Framework release, run cumulative affected verification then one final `RELEASE_FULL` on the exact unchanged accepted candidate.

---

## 1.17.0 → 1.18.0

### Affected distribution surfaces

- Framework identity becomes `1.18.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-052 Project Upgrade One-Session Fast Path.
- `[Project Upgrade]` performs fresh comparison, cumulative assessment, `FAST_PATH | ASSESSED_PATH | MAJOR_MIGRATION_REQUIRED` classification, one-session eligibility, and exact Preview in one read-only pass; the separate prepare prompt is removed.
- One explicit Human mutation approval bound to the exact Preview/candidate remains mandatory before Material mutation.
- Eligible `FAST_PATH` and bounded compatible `ASSESSED_PATH` may execute as one bounded successor/archive/routing transaction; `MAJOR_MIGRATION_REQUIRED` remains outside the one-session fast path.
- Framework Release Acceptance and Project Upgrade Acceptance are separate proof domains. Exact valid state-bound `RELEASE_FULL` evidence may be reused for an unchanged target, while Project-specific affected/result verification remains mandatory.
- Evidence mismatch, target change, stale/contradictory evidence, or unbounded impact invalidates reuse. Consuming-upgrade `RELEASE_FULL` budget is zero with exact reusable proof and at most one when genuinely required on the exact unchanged candidate.
- Material Preview/candidate/scope/authority/rollback changes require re-Preview/reapproval; deterministic revision/timestamp/filename/routing values implied by the approved transaction do not.
- Interruption recovery reuses still-valid comparison/assessment/release evidence and reconstructable durable state; unknown shared/non-idempotent results use `RESULT_VERIFICATION_REQUIRED` before retry.
- `INTEGRATION_GATE` remains mandatory immediately before applicable mutable-target integration/publication.
- Canonical ProjectFramework integration and self-host reconciliation may chain only when one exact Preview and authority cover both; missing Root authority stops at `RECONCILIATION_REQUIRED`.
- Existing initialized Projects do not auto-adopt 1.18. No runtime updater, CI/CD mutator, bot, scheduler, router, validator/CLI, or new state/Stable-ID family is introduced.

### Upgrade checklist

1. Preserve current Project identity/pin, Project-specific truth/rules, Stable IDs, bindings, history, and rollback basis until the exact Preview is approved.
2. Run `[Project Upgrade]` to produce cumulative assessment + exact Preview without a separate prepare round-trip.
3. Approve the exact mutation transaction once; reapprove only after material approved assumptions change.
4. Reuse exact Framework release proof only when target tree/content and material assumptions match committed state-bound evidence.
5. Always run Project affected/result verification after mutation, even when release proof is reused.
6. Preserve `INTEGRATION_GATE` before mutable-target action and all independent publication/Root/Binding/security authority gates.
7. Verify scenarios `505–528` while preserving cumulative scenarios `1–528` contiguous/unique.

### Affected distribution surfaces

- Framework identity becomes `1.17.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-051 Risk-Tiered Feature Delivery Fast Path.
- `LOW | MEDIUM | HIGH` is Derived Delivery Tier workflow vocabulary over canonical `R0–R3`; it never replaces Risk or grants authority.
- Tier derivation composes Risk, affected scope, blast radius, sensitive surfaces, rollback, uncertainty, and evidence quality; uncertainty escalates rather than silently downgrades.
- Common invariant preflight permits state-bound reuse of still-valid stable governance/location evidence while volatile Git state and applicable R2/R3 authority/target prerequisites remain fresh-check obligations.
- Review floor is LOW not-required by default, MEDIUM conditional, HIGH required absent an explicit governed exact-scope waiver; reviewer unavailability is never a waiver.
- Task verification is tiered while acceptance boundaries remain distinct: Task affected verification/completion commit ≠ `RELEASE_FULL` ≠ `INTEGRATION_GATE`.
- One-session LOW delivery is an objective, not an SLA; redundant rereads/checkpoints/prompts are reduced without removing safety gates.
- Interruption recovery selectively invalidates evidence; unknown potentially-applied non-idempotent results use `RESULT_VERIFICATION_REQUIRED` before retry.
- Parallel mutation requires positive independence evidence plus final combined-candidate verification; HIGH mutation is serialized by default.
- Direct Git/GitHub may handle repository-native state when tool policy/identity/authority allow; MCP is not a prerequisite merely for nonexistent runtime/process/UI state.
- No new Project Source file is required in consuming Projects; optional `Project-Execution/` profiles remain stricter overlays when present.
- Existing initialized Projects do not auto-adopt 1.17 and remain pinned until governed Direct-to-Latest `[Project Upgrade]`.
- No runtime service, CI/CD, bot, router, watcher, scheduler, validator/CLI, policy engine, credential store, new Risk family, Stable-ID family, or Registered Command is introduced.

### Upgrade checklist

1. Preserve the initialized Project's local pin, current truth, Stable IDs, Project-specific rules, bindings, and history until governed promotion.
2. Preserve canonical `R0–R3`, AUTH/location/trust/disclosure/secret/destructive/production/publication gates; Derived Delivery Tier may only make workflow stricter.
3. Adopt `LOW | MEDIUM | HIGH` only as derived feature-delivery classification; do not materialize a parallel Risk or Stable-ID family.
4. Preserve any stricter active optional tool/capability/trust profile; absence of an optional profile creates no new authority.
5. Preserve completion-commit semantics plus distinct `RELEASE_FULL` and `INTEGRATION_GATE` boundaries.
6. Do not synthesize push/PR/merge/release/deployment authority from delivery tier or direct Git/GitHub eligibility.
7. Verify current guidance, maintained starters, and pressure scenarios `473–504` while preserving scenarios `1–504` contiguous/unique.
8. For this Framework release, run cumulative affected verification then one final `RELEASE_FULL` on the exact unchanged accepted candidate.

---

## 1.15.0 → 1.16.0 (previous)

### Affected distribution surfaces

- Framework identity remains `1.16.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-049 Canonical Self-Hosting Release Reconciliation, layered on TASK-048 Project Path Workspace & MCP Routing.
- `[Project Path]` becomes a strict eight-section interface: `Framework Path → Git Path → Storage Path → Develop Workspace → Production Workspace → MCP Execution → Build / Deployment Mapping → Continuity`.
- `FRAMEWORK-001` Project Location Binding remains narrow: repository + environment-scoped Local Workspace binding/routing only. It does not acquire workspace-role, source-mutation, active Develop, Canonical Implementation Source, or Production runtime authority.
- `40 Technical Design` / Development Workspace Contract gains explicit active Local/Remote Durable Develop Workspace semantics plus symmetric relocation and one-active-workspace-per-scope behavior.
- `60 Deployment Plan` gains exact Production applicability `APPLICABLE | NOT_APPLICABLE | VERIFICATION_REQUIRED`, explicit Production role, direct-source-mutation prohibition, artifact identity, mapping, and resulting-state verification.
- `Project-Execution/tools.md` adds `failback_policy: CHECKPOINT_FAILBACK`; ordered fallback remains explicit-only through `fallback_order` and never expands from recency, similarity, ranking, or connected state.
- `Project-Execution/fallback-log.md` is optional/applicability-driven append-only incident history for actual fallback/recovery events; it is not Project Source authority, credentials, selection policy, or a Stable-ID registry.
- Unknown potentially-applied side effects use `RESULT_VERIFICATION_REQUIRED`; unprovable resulting state fails closed instead of blindly retrying.
- Brownfield existing workspaces may become Develop only with evidence; Production is never inferred from an existing path; connected/recent MCPs never become fallback automatically.
- Ordinary initialized consuming Projects remain pinned until governed `[Project Upgrade]`; canonical ProjectFramework self-host reconciliation does not broaden this rule.
- The verified canonical `captainhuke-dev/ProjectFramework` repository is the narrow self-host exception: after a verified Framework release merge to canonical `main`, its own active Root/Project Source/Bootstrap must reconcile to the same release as a mandatory governed post-merge step. Unresolved state is `RECONCILIATION_REQUIRED`; no redundant `[Project Upgrade]` is required for that canonical same-release self-host transition.
- TASK-048 adds no background router/watcher, credential store, validator/CLI, deployment engine, CI/CD, scheduler, daemon, or runtime failover subsystem.

### Upgrade checklist

1. Preserve the initialized Project's current Framework pin, Stable IDs, Project-specific rules, bindings, current truth, and history until governed promotion.
2. Use Direct-to-Latest cumulative comparison; do not replay intermediate release migrations merely because they exist.
3. Preserve Project Location Binding as routing-only. Map Develop role/type/durability/active-workspace semantics into applicable `40`, not `FRAMEWORK-001`.
4. Classify Production exactly: explicit no-Production truth = `NOT_APPLICABLE`; declared-but-unresolved target = `APPLICABLE + NOT_VERIFIED`; unknown applicability = `VERIFICATION_REQUIRED + NOT_VERIFIED`.
5. For Local ↔ Remote Durable relocation, checkpoint required source state, verify repository/source identity + intended revision + durability + working-tree state, promote `40`, and revise `FRAMEWORK-001` only for a real persistent Local Workspace Binding delta.
6. If adopting ordered MCP fallback, declare exact Primary + `fallback_order`, materialize `fallback-log.md`, and preserve `CHECKPOINT_FAILBACK` / unknown-result verification. Do not infer fallback from connected/recent tools.
7. Preserve the seven-command registry, TASK-043 command completeness, TASK-045 response close, and all independent authority/push/Root/Binding/disclosure/secret gates.
8. Verify affected surfaces progressively, then run one final `RELEASE_FULL` on the unchanged target candidate. FAST_PATH state-bound evidence reuse remains available only under its existing exact-tree rules.

---

## 1.14.0 → 1.15.0 (previous)

### Affected distribution surfaces

- Framework identity becomes `1.15.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-045 Response Close + Next Goal.
- Mandatory visible response-close fields change from `[Next Action] → [Chat] → [Reason] → [Required Read]` to `[Next Action] → [Next Goal] → [Reason]`; nothing follows `[Reason]`.
- `[Chat]` and `[Required Read]` are removed only from the mandatory visible close. `09 Handoff` may still preserve Chat Continuity, Required Read Before Continue, exact resume pointers, and `authority_transfer: false`.
- `[Next Goal]` is presentation-only. A displayed suggestion never creates or changes `OUT-* / AUTH-* / ACT-* / ENV-*`; only an explicit Human `[Goal]` invocation does.
- A non-`ไม่มี` suggestion is one copy-ready `[Goal] ...` or `[Goal] CHANGE ...` command for a sufficiently bounded, grounded outcome. No-next-action, redundant active-Goal, ambiguous/conflicting, ungrounded high-risk, and persistence-recovery cases use `ไม่มี`.
- `[Next Goal]` never synthesizes push/publication, destructive, Root/Binding, external-disclosure, R3, or secret-value opt-ins.
- TASK-042 remains the unskippable final-response control-flow invariant; TASK-043 Command Contract Completeness Gate still runs before the revised Response Close Completeness Gate.
- Registered commands remain exactly seven. No new semantic slot, Stable-ID family, parser, middleware, UI hook, validator/CLI, bot, scheduler, watcher, daemon, or runtime enforcement is introduced.
- Historical pre-1.15 examples/evidence remain provenance and are not globally rewritten.

### Upgrade checklist

1. Preserve the initialized Project's valid local pin until governed `[Project Upgrade]` promotion; upstream 1.15 does not silently alter Brownfield response behavior.
2. Update current response-close guidance to exactly the two headings plus `[Next Action]`, `[Next Goal]`, `[Reason]`, in that order, with nothing after `[Reason]`.
3. Remove mandatory visible `[Chat]`/`[Required Read]` requirements without deleting internal Handoff continuation/read-routing semantics.
4. Preserve `[Goal]` authority rules: suggestion ≠ invocation ≠ authorization. Do not synthesize Goal records during upgrade.
5. Preserve TASK-042/TASK-043 gate ordering and the exact seven-command registry.
6. Keep thin launchers thin when they do not duplicate the old four-field payload; do not expand them merely for TASK-045.
7. Verify maintained starter stamps/current guidance, scenarios `421–432`, full affected scope, and one final unchanged-candidate `RELEASE_FULL`.
8. Direct-to-Latest remains valid; historical 1.14 response examples remain provenance rather than rewrite targets.

---

## 1.13.0 → 1.14.0 (previous)

### Affected distribution surfaces

- Framework identity becomes `1.14.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is the Federated Change Intelligence Suite.
- TASK-036 defines optional root `Project-Change-Feed/` as a derived, non-authoritative, bounded, rebuildable projection with maintained starter templates.
- Projection states are exactly `CURRENT | STALE | REBUILD_REQUIRED | UNAVAILABLE`; feed change kinds are `STABLE_ID_CHANGE | DOCUMENT_CHANGE | RELATION_CHANGE | LIFECYCLE_CHANGE | EVIDENCE_CHANGE | RELEASE_PUBLICATION_CHANGE | OTHER_MATERIAL_CHANGE`.
- A source checkpoint supports incremental `since` routing; source-native ordering outranks timestamp guessing. Retention is bounded; gaps rebuild from authoritative/source-native history or remain `UNKNOWN / VERIFICATION_REQUIRED`.
- Existing initialized Projects do not auto-create `Project-Change-Feed/`; adoption is applicability-driven and separately governed.
- TASK-030 adds evidence-based relation reconciliation over existing `92 / REL-*`; counterpart discovery never grants cross-Project write authority.
- Reciprocal compatibility remains TASK-022 exact; `DEPENDS_ON` and `SUPPORTS` remain directional with no universal inverse; `CORROBORATED` requires authoritative current evidence from both Projects.
- Unavailable/stale counterpart evidence uses `VERIFICATION_REQUIRED`; incompatible authoritative assertions use `CONFLICTED` plus existing `CONFLICT-*`; TASK-029/TASK-031 remain dependency-gated.
- TASK-029 adds advisory impact classification `DIRECT | POTENTIAL | UNKNOWN`; a `DIRECT` claim requires authoritative/current evidence and cannot rest solely on feed/OpenViking/Knowledge/derived traversal.
- Impact analysis preserves canonical `REL-* / DEP-* / REQ-* / DEC-* / EVD-*` homes and never grants cross-Project mutation/upgrade/approval/publication authority.
- TASK-031 adds vendor-neutral notification eligibility, exact urgency `ROUTINE | ATTENTION | URGENT`, governed recipient resolution, acknowledgement/escalation/dedup semantics, and explicit failure/stale handling.
- Notification urgency is presentation-only; recipient/ack/escalation never grant authority; actual delivery/disclosure remains separately governed and no delivery runtime or notification Stable-ID family is introduced.
- No watcher, crawler, webhook, daemon, scheduler, event bus, queue, CDC, Git hook, background agent, new command, new Stable-ID family, or cross-Project mutation runtime is introduced.

### Upgrade checklist

1. Preserve active local Framework pin/current truth until governed Direct-to-Latest promotion.
2. Treat `Project-Change-Feed/` as optional derived routing only; never replace `10 Change Log`, Project Source, Git/source-native history, or `EVD-*`.
3. If adopting the feed, declare projection checkpoint/retention and rebuild from authoritative/source-native pointers; corrupt state becomes `REBUILD_REQUIRED` rather than authority repair.
4. Do not infer full historical coverage when a requested `since` checkpoint falls outside retention; rebuild or report the unavailable portion explicitly.
5. Preserve the exact seven-command registry and existing TASK-022/TASK-028/TASK-032 authority boundaries.
6. Do not synthesize feed content, runtime automation, notification delivery, impact records, reciprocal relation assertions, or cross-Project changes during upgrade. Relation reconciliation only changes an owning Project under its applicable authority.
7. Direct-to-Latest remains valid; final cumulative suite verification still requires affected checks and one unchanged-candidate `RELEASE_FULL`.

---

## 1.12.2 → 1.13.0

### Affected distribution surfaces

- Framework identity becomes `1.13.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-028 + TASK-032 Integrity & Remediation Suite.
- `[Project Audit]` is added as a Registered Command and Strict Governed Interface with exact top-level order `Scope → Health → Categories → Findings → Unknowns → Evidence → Repair Routes → Continuity`.
- Audit health reuses `GREEN | AMBER | RED | UNKNOWN`; current/volatile evidence follows existing freshness rules and unresolved evidence remains `UNKNOWN / VERIFICATION_REQUIRED`.
- Audit findings are presentation only and reuse existing canonical homes/routes; no `AUDIT-*` / `FINDING-*` family is created and `Audit finds ≠ Audit fixes`.
- TASK-032 remediation workflow is dependency-ordered after TASK-028 and requires an explicit remediation request/Goal or other applicable authorization; audit findings alone do not activate mutation.
- Remediation resolves canonical owner/home, `R0–R3`, applicable authority, prerequisites/freshness, ordered actions, rollback/reversibility, direct resulting-state verification, affected re-audit/result confirmation, and evidence/lifecycle updates. Existing `ISS/DRIFT/CONFLICT/MIG/CR/ACT/AUTH/ENV/DEC/REQ` homes are reused.
- Semantic conflicts are routed to Decision/Change/Conflict governance rather than auto-repaired; `ACT DONE ≠ repair outcome verified`; R2/R3 and other explicit gates remain independent.
- No issue/repair object, remediation ID family, repair command, validator/scanner/CLI, daemon, repair bot, auto-fix, or runtime enforcement is generated.

### Upgrade checklist

1. Preserve the initialized Project's valid local pin and current truth; adopt 1.13.0 only through governed `[Project Upgrade]` / Direct-to-Latest promotion.
2. Add `[Project Audit]` to current command discovery and preserve the exact strict dimension order and read-only/no-auto-fix boundary.
3. Keep optional audit categories applicability-driven; do not synthesize missing `92`, Project Knowledge, or Execution-profile surfaces solely for audit completeness.
4. Treat findings as bounded command results; durable issues/drift/conflicts/migrations/changes use their existing canonical homes only through separately authorized work.
5. For an authorized repair, classify the canonical owner and Risk before mutation; declare rollback/reversibility; verify direct resulting state plus affected references; then re-audit/confirm the affected category before closure.
6. Preserve TASK-042 response-close and TASK-043 command-gate semantics unchanged.
7. Verify scenarios `1–380`, current starter stamps, command registry, historical TASK-042/TASK-043 artifacts, local-pin/history preservation, no-runtime expansion, cumulative AFFECTED, and one final unchanged-candidate `RELEASE_FULL`.

---

## 1.12.1 → 1.12.2

### Affected distribution surfaces

- Framework identity becomes `1.12.2`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-043 Registered Command Strict-Interface & Contract Completeness Hardening.
- Core Governance and SKILL define recognized Registered Commands as Strict Governed Interfaces: semantic equivalence alone does not satisfy governed structure/order/tokens/freshness/fail-closed representation.
- A new semantic Command Contract Completeness Gate validates recognized-command bodies before the existing TASK-042 Response Close Completeness Gate; TASK-042 remains the final global pre-emit close validation.
- Current `[Project Status]` Core/SKILL/root-template summaries align on `Identity → Health → Remain Tasks → Git Sync → Working Tree → Verification → Blockers → Continuity`.
- Scenarios `351–356` cover correct-information/wrong-protocol, narrative replacement, missing evidence, style conflict, ordered gates, and Core/SKILL alignment.
- No command identity, semantic slot, Stable-ID family, lifecycle/authority family, parser, runtime interceptor/middleware, validator/CLI, hook, bot, scheduler, watcher, or daemon is introduced.

### Upgrade checklist

1. Preserve the initialized Project's valid local Framework pin until governed `[Project Upgrade]` promotion; upstream movement does not silently harden Brownfield command behavior.
2. Adopt the Strict Governed Interface rule for commands registered by the selected target Framework; do not promote unbracketed ordinary language into command identity.
3. Preserve governed command dimensions/order/tokens/freshness and explicit `UNKNOWN` / `VERIFICATION_REQUIRED` representation when evidence is unavailable.
4. Run Command Contract Completeness Gate before TASK-042 Response Close Completeness Gate; preserve the existing mandatory close format and exceptional-path invariant.
5. Align current `[Project Status]` summaries through `Continuity`; preserve historical older wording as provenance rather than rewriting archives.
6. Keep prose flexibility only where the active command contract does not define stricter structure.
7. Verify scenarios `1–356`, current starter stamps, unchanged command registry, TASK-042 preservation, local-pin/history preservation, no-runtime expansion, affected checks, and one final unchanged-candidate `RELEASE_FULL`.
8. Direct-to-Latest remains valid.

---

## 1.12.0 → 1.12.1

### Affected distribution surfaces

- Framework identity becomes `1.12.1`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-042 Response Finalization Hardening forward-port.
- ChatGPT/Claude thin launchers bootstrap before the first Project-governed response in each chat; read-only/status/diagnostic/failure-report responses are not exempt; full Core Governance is not duplicated into launchers.
- Core Governance / SKILL make Response Close Completeness Gate an unskippable final-response control-flow invariant across early-return, tool/MCP failure, connector unavailable, timeout, partial-result, refusal/blocked action, persistence failure, and exception-recovery paths.
- Original TASK-042 scenarios `269–280` are historical to the 1.9.x branch; cumulative 1.12.x integration uses scenarios `339–350` to avoid collision with TASK-025/Set 1 scenarios `269–338`.
- Maintained Project Source starter stamps become Framework `1.12.1` / Schema `1.0.0`; TASK-025 Project Knowledge and Set 1 Project Execution / release / trust semantics remain intact.
- No runtime middleware/interceptor, transport hook, validator service/CLI, daemon, scheduler, watcher, UI automation, or vendor runtime component is introduced.

### Upgrade checklist

1. Preserve the initialized Project's valid local pin until governed `[Project Upgrade]` promotion; upstream movement never auto-upgrades Brownfield Projects.
2. Update thin adapter wording so Project Bootstrap resolves before the first Project-governed response when available; non-Material diagnostics are not exempt.
3. Preserve exact mandatory response-close headings, fields, order, lifecycle tokens, and coupling; TASK-042 changes timing/control-flow coverage, not the close format.
4. Preserve all Framework 1.12.0 Task dependency, Tool/MCP, capability, publication, trust, Project Knowledge, disclosure, secret, and authority boundaries.
5. Verify cumulative scenarios `1–350`, current starter stamps, launcher parity/size, historical evidence, and one final unchanged-candidate `RELEASE_FULL`.
6. Direct-to-Latest remains valid.

---

## 1.10.0 → 1.12.0

### Affected distribution surfaces

- Framework identity becomes `1.12.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-037 Security & Trust Boundary Contract.
- TASK-033 adds explicit Task dependency/readiness/priority metadata without creating Project-management `DEP-*`, scheduling, or execution authority.
- TASK-027 adds optional `Project-Execution/README.md` + `tools.md` for deterministic Tool/MCP eligibility/fallback/failure policy; Tool policy ≠ Location ≠ Authority.
- TASK-034 adds optional `Project-Execution/capabilities.md` for vendor-neutral capability/provider/review eligibility; Capability ≠ Authority and external use still follows TASK-026.
- TASK-035 adds orthogonal Implementation/Integration/Repository Publication/Release/Artifact Publication/Deployment dimensions plus RC/evidence/integration semantics; `commit ≠ push` and publication authority remains separate.
- TASK-037 adds optional `Project-Execution/trust.md` for trust/crossing/privileged/UNKNOWN fail-closed governance; TASK-026 and `17 Secret Reference Registry` remain canonical for disclosure/secrets.
- Scenarios `289–338` cover Set 1 behavior; maintained Project Source starter stamps become Framework `1.12.0` / Schema `1.0.0`.
- ChatGPT/Claude thin launchers remain unchanged; no scheduler/router/provider/CI-CD/scanner/policy-engine/runtime enforcement is added.

### Upgrade checklist

1. Run `[Project Upgrade]`; preserve the initialized Project's local Framework/Schema pin until governed promotion.
2. Assess Task dependency metadata separately from Project-management `DEP-*`; do not infer Task edges from numbering/proximity.
3. Evaluate whether `Project-Execution/` is applicable. Do not create default allow-all/restrictive tools, model capability, or trust profiles without approved facts.
4. If tool policy is adopted, verify Project authority/location first; then apply deterministic PRIMARY/allow/disallow/fallback/failure behavior. Store no credentials/secrets.
5. If capability policy is adopted, keep Tool eligibility, model capability, provider/disclosure eligibility, and authority separate. Required independent review remains evidence-backed.
6. Map existing release practices to orthogonal publication dimensions without rewriting historical facts or inventing RC identities/tags/approvals.
7. If trust policy is adopted, classify only evidenced surfaces; UNKNOWN sensitive crossings fail closed. Prior successful use never proves trust.
8. Preserve TASK-026 disclosure/minimization/secret prohibitions and `17 Secret Reference Registry` reference-only semantics across external/tool/model/trust flows.
9. Do not auto-create routers, schedulers, CI/CD, release bots, deployment automation, scanners, policy engines, secret stores, or runtime enforcement.
10. Verify current starter stamps, Project-Execution templates, scenario coverage, local pin/history preservation, and affected Framework surfaces; run one final unchanged-candidate `RELEASE_FULL`.
11. Direct-to-Latest remains valid: older Projects assess cumulative current→1.12.0 semantics without mandatory replay of intermediate releases.

---

## 1.9.0 → 1.10.0

### Affected distribution surfaces

- Framework identity becomes `1.10.0`; Schema stays `1.0.0`; release format stays `3`; latest amendment is TASK-025 Project Knowledge Layer.
- Core Governance / SKILL / README define optional `Project-Knowledge/` outside Project Source authority, exact maintenance states, provenance, index/log operations, promotion gate, disclosure/Meeting/Evidence/Project Graph/OpenViking boundaries.
- `templates/project-knowledge/` adds maintained starter source for Knowledge README/index/log/page representation.
- Project Source starter templates remain semantic-slot starters but their current Framework stamps become 1.10.0; no new semantic slot is added.
- scenarios `269–288` cover authority separation, provenance, maintenance operations/states, promotion, integration boundaries, optionality, and no-runtime/no-secret behavior.
- ChatGPT/Claude thin vendor launchers are unchanged by TASK-025.

### Upgrade checklist

1. Run `[Project Upgrade]`; preserve the initialized Project's local Framework pin and current Project Source until governed promotion.
2. Evaluate whether a Project Knowledge layer is actually useful. Absence remains valid; do not create it merely because target 1.10.0 supports it.
3. If adoption is desired, Preview root `Project-Knowledge/` creation and any Project Source routing pointer after active authority resolution.
4. Do not bulk-migrate historical notes, chats, Meeting transcripts, or files as accepted Knowledge. Candidate material requires provenance review and may remain source-native.
5. Maintain `Project Knowledge ≠ Project Authority`. Knowledge page state, retrieval rank, model consensus, or recency never changes Requirements/Decisions/Risks/Relations automatically.
6. Knowledge→Governance promotion identifies the canonical Project Source owner, verifies evidence, obtains applicable authority, then mutates only that owner.
7. External use of Knowledge still follows TASK-026 disclosure/provider/minimization/secret rules. Project Knowledge maintenance authority grants no external disclosure.
8. Knowledge cross-links do not create `REL-*`; OpenViking keeps `PROJECT_SOURCE_AUTHORITY` separate from `PROJECT_KNOWLEDGE_ADVISORY` and remains derived/rebuildable.
9. No wiki engine, vector DB, embedding service, watcher, crawler, MCP wiki service, validator/CLI, scheduler, or runtime daemon is required or authorized by this migration.
10. Verify Knowledge template integrity, optionality, local pin/promotion result, current starter stamps, pressure scenarios, and affected current Framework surfaces; run one final unchanged-candidate `RELEASE_FULL` under existing evidence rules.
11. Direct-to-Latest remains valid: older Projects assess cumulative current→1.10.0 target semantics without mandatory replay of intermediate releases while preserving applicable migration constraints/history.

---

## 1.8.0 → 1.9.0

### Affected distribution surfaces

- `FRAMEWORK-RELEASE.yaml` — Framework version becomes `1.9.0`; latest amendment points to TASK-041 Portable Installation Bootstrap & Project Settings Handoff; Schema remains `1.0.0` and release format remains `3`
- `CHATGPT-PROJECT-INSTRUCTIONS.md` / `CLAUDE-PROJECT-INSTRUCTIONS.md` — current maintained vendor launchers become thin two-binding adapters instead of five-field/full-governance copies
- `templates/project-location-bootstrap.md` — user-facing Project Settings layer becomes `ProjectFramework Upstream` + verified absolute `Project Bootstrap`; internal `framework_source`, `remote_location`, `file_storage_locations`, `mcp_location`, `local_workspace`, and dynamic branch/worktree semantics remain available
- `templates/PROJECT-BOOTSTRAP.md` — documents Project Settings primary entry plus consuming README managed fallback and preserves locator-only / active-`FRAMEWORK-001` authority boundary
- upstream `README.md` — canonical GREENFIELD installation documentation, exact response-close pattern, and one repository-local managed bootstrap fallback
- consuming Project root `README.md` — governed adoption creates or maintains exactly one `PROJECTFRAMEWORK-BOOTSTRAP` managed block with relative `Project Bootstrap: ./PROJECT-BOOTSTRAP.md`; Project content outside markers remains Project-owned
- root/skeleton/mockup starters — Framework `1.9.0` GREENFIELD resulting state, descriptive Project Settings handoff guidance, and current starter stamps
- `tests/pressure-scenarios.md` — scenarios `249–268` cover install intent, two-binding handoff, absolute-path verification, README marker integrity, fallback portability, authority separation, thin launchers, Brownfield safety, and no-runtime/no-authority synthesis
- historical 1.8.0 amendments/specs/plans/evidence/full launcher captures remain provenance and are not globally rewritten

### Upgrade checklist

1. Run `[Project Upgrade]`; fresh-compare the initialized Project's valid local `FRAMEWORK-001` pin with target Framework `1.9.0`. `ProjectFramework Upstream: https://github.com/captainhuke-dev/ProjectFramework` is upstream discovery/upgrade input only, not consuming Project repository or authority.
2. Preserve current truth, Stable IDs, Project-specific rules, Project Location Binding, Local Workspace Binding, history, authorization, and local Framework/Schema pin until governed promotion. Upstream movement never auto-adopts 1.9.0.
3. Preview the portable-bootstrap adoption effects: thin vendor adapter, root `PROJECT-BOOTSTRAP.md` relationship, and consuming managed README block. Existing README content outside the managed marker pair must be preserved.
4. For a consuming README with no managed block, append exactly one block; for exactly one valid block, update only the managed body. Duplicate or malformed marker structures fail closed to repair; never choose by recency/position/similarity.
5. Project Settings uses a **verified absolute** `Project Bootstrap` path for the current environment. The consuming README uses portable relative `./PROJECT-BOOTSTRAP.md`. If the absolute path cannot be verified, report `VERIFICATION_REQUIRED`; do not fabricate a copy-ready value.
6. Preserve internal Git/Drive/File Storage/MCP/Workspace semantics and `[Project Path]`. Thin Project Settings removes legacy five labels only as mandatory current vendor fields; it does not delete location governance.
7. Apply local Project Source/root/README mutations only after the applicable upgrade Preview and approval. Do not claim GPT/Claude/Hermes/other vendor settings were changed unless an external settings action was actually executed and verified.
8. After governed adoption, regenerate and present the copy-ready Project Settings block:

```text
ProjectFramework Upstream: https://github.com/captainhuke-dev/ProjectFramework
Project Bootstrap: <VERIFIED_ABSOLUTE_PROJECT_BOOTSTRAP_PATH>

ProjectFramework Bootstrap Rule:
Read Project Bootstrap before Material Project work.
If Project Bootstrap cannot be resolved, use the Project README managed bootstrap block as fallback.
ProjectFramework Upstream is for Framework discovery/upgrade only; it never replaces local Project Source authority.
```

9. Keep active local `FRAMEWORK-001` as Project governance authority. Settings, managed README, fixed upstream, and root bootstrap remain discovery/locator surfaces and never transfer `AUTH-*`, Risk, branch/integration, implementation, runtime, publication, secret, or disclosure authority.
10. Do not synthesize Goal/OUT/AUTH/ENV/Meeting/provider/disclosure/secret-value/runtime/daemon state from adoption. Actual secret values remain forbidden.
11. Verify README marker integrity, locator chain, local pin/promotion result, maintained adapter semantics, and affected Project truth. Use one final `RELEASE_FULL` on the unchanged target candidate per existing evidence rules.
12. Direct-to-Latest remains valid; Projects pinned before 1.8.0 assess cumulative current→1.9.0 target state without mandatory intermediate replay while preserving applicable migration constraints/history.

---

## 1.7.0 → 1.8.0

### Affected distribution surfaces

- repository package root — canonical upstream distribution path changes from `managing-project-source/` to `Framework-Source/`; no live old-root alias remains
- `FRAMEWORK-RELEASE.yaml` — Framework version `1.8.0`; latest amendment pointer moves through TASK-038 distribution-root migration, TASK-039 persistent `[Goal]`, TASK-024 `[Meeting]`, TASK-026 External AI Context & Disclosure Governance, and TASK-040 canonical `[Session]` command naming
- current Core Governance / SKILL / README / launcher and maintained starter routing — current reusable Framework path is `Framework-Source/`; bounded session/task pre-approval uses canonical command `[Session]` backed by unchanged `ENV-*` semantics
- `12 Authorization Registry`, `15 Action Registry`, conditional `91 Project Management Control`, `03 Current State`, and `09 Handoff` starters — persistent Goal uses `OUT-* / AUTH-* / ACT-* / ENV-*` with `authority_transfer: false`; no `GOAL-*` family
- `13 Evidence Registry` and command/help surfaces — material Meeting use may persist as advisory `EVD-*`; no `MEETING-*` family, provider JSON authority, automatic conversation, credential, runtime, or disclosure authority is introduced
- `12 Authorization Registry`, `13 Evidence Registry`, and `17 Secret Reference Registry` starter guidance — external-AI disclosure reuses bounded `AUTH-* / EVD-* / SECRET-*`; classes are `EXTERNAL_OK | EXTERNAL_REVIEW | DO_NOT_DISCLOSE | UNCLASSIFIED`; provider eligibility is separate; no `DISC-*` family/slot is introduced
- historical amendments/specs/plans/evidence — old-path text remains historical provenance when it was true at capture time; do not globally rewrite it
- ProjectFramework's own current Project Source — reconcile current distribution-location statements through governed revisions without auto-upgrading its local Framework pin
- `tests/pressure-scenarios.md` — scenarios 181–188 cover distribution-root migration; 189–211 persistent Goal; 212–227 `[Meeting]`; 228–245 external-AI disclosure classification/authorization/provider/secret/minimization/redaction/consumer/Brownfield boundaries

### Upgrade checklist

1. Run `[Project Upgrade]`; fresh-compare the initialized Project's local pin with target `1.8.0` using Direct-to-Latest assessment/Preview rules.
2. Preserve local `FRAMEWORK-001`, Project-specific rules, bindings, Stable IDs, current truth, and history. The upstream directory rename does not itself rewrite an initialized Project.
3. Treat `Framework-Source/` as the target release's canonical reusable upstream package root. Do not infer a live fallback at `managing-project-source/`.
4. Update only current references that actually depend on the canonical upstream distribution path. Do not cosmetically rewrite historical amendments, completed evidence, or archived revisions.
5. Keep deployed `<Project-Root>/PROJECT-BOOTSTRAP.md` routing to the Project's active `Project-Source/00 → 01 → 03`, with `09` continuation. The Framework distribution root is not Project authority.
6. External scripts, bookmarks, deep links, or vendor configuration that hard-code `managing-project-source/...` require explicit update when applicable; the Framework does not mutate external consumers automatically.
7. If the consuming Project maintains repository-local current provenance/routing that names the upstream package root, migrate that current truth through its normal governed revision/MIG/evidence flow.
9. Do **not** synthesize a persistent Goal from old free-text goals, backlog items, Handoff prose, an existing `OUT-*`, or prior “continue” messages. A persistent Goal exists only after explicit `[Goal]` invocation/adoption under the active contract.
10. Preserve existing `OUT-*`, `AUTH-*`, `ACT-*`, and `ENV-*` records. TASK-039 adds composition semantics; it does not migrate them into a `GOAL-*` family.
11. If `[Goal]` is explicitly adopted, materialize/resolve Goal `OUT-*` and `AUTH-*` through their canonical homes; conditional `91` becomes applicable only when Goal/outcome truth is material.
12. Default local Goal authority may cover bounded local development unless narrowed; push, destructive actions, Root/Binding mutation, and external disclosure remain exact opt-ins and higher-level controls still apply.
13. Do **not** synthesize a Meeting from prior AI transcripts, backlog, Handoff, existing `EVD-*`, or provider conversation JSON. `[Meeting]` begins only from an explicit bracketed invocation under the active contract.
14. Treat the explicit Meeting question as the default outbound payload. Additional Project context remains minimum-necessary and separately disclosure-authorized; actual secret values remain prohibited.
15. Preserve existing external-AI/evidence records. Material Meeting use may reference/persist advisory `EVD-*`; do not migrate provider JSON into Project Source or create `MEETING-*` records.
16. Council majority/ranking/Chairman synthesis remains advisory and never becomes automatic approval, `AUTH-*`, `DEC-*`, `REQ-*`, Risk acceptance, or mutation authority.
17. Governance adoption does not require installing/running llm-council, provisioning OpenRouter credentials, or creating conversations. Provider runtime remains optional/applicability-driven.
18. `[Goal]` / `ENV-*` execution authority does not imply outbound Project-context disclosure authority for `[Meeting]`.
19. Preserve existing `AUTH-*`, `EVD-*`, and `SECRET-*`; do not create `DISC-*`, mass-classify historical content as `EXTERNAL_OK`, or synthesize standing disclosure authority from prior AI usage, credentials, chats, Meetings, Goals, or “continue” wording.
20. Use `[Session]` as the current registered command for bounded session/task `ENV-*` scope. The older longer command name is historical provenance only and is not a current registered alias.
20. Reassess external provider/tool eligibility prospectively when next used. `UNCLASSIFIED` protected Project context and materially unresolved provider policy/identity fail closed for automatic external disclosure.
21. Governance adoption does not require a runtime redactor/router/proxy, DLP scanner, disclosure gateway, provider credential setup, or automatic outbound calls.
8. Verify affected scope and run one final `RELEASE_FULL` on the unchanged target candidate before promoting the upgrade.

---

## 1.6.0 → 1.7.0

### Affected distribution surfaces

- `FRAMEWORK-RELEASE.yaml` — Framework version `1.7.0`; latest amendment pointer moves to TASK-023; root bootstrap template becomes a declared entrypoint
- `references/framework-governance-amendment-260829-task023.md` / `core-governance-rules.md` / `SKILL.md` — vendor-neutral Project-root discovery contract and authority/failure boundaries
- `templates/PROJECT-BOOTSTRAP.md`, `templates/project-location-bootstrap.md`, root/skeleton/mockup templates — GREENFIELD root bootstrap, legacy `PROJECT-CONFIG.md` separation, and canonical `00 → 01 → 03` routing with `09` continuation
- `CHATGPT-PROJECT-INSTRUCTIONS.md` / `CLAUDE-PROJECT-INSTRUCTIONS.md` — optional thin adapters that prefer `PROJECT-BOOTSTRAP.md` when Project-root access exists
- `tests/pressure-scenarios.md` — root discovery, authority, GREENFIELD/Brownfield, contradiction, no-filesystem, stable-filename, volatile-state, and vendor-independence coverage
- `README.md` — current release identity and self-bootstrapping Project explanation

### Upgrade checklist

1. Run `[Project Upgrade]`; fresh-compare the active local pin with target `1.7.0` using Direct-to-Latest classification/Preview rules.
2. Preserve Project-specific rules, bindings, Stable IDs, history, current semantic slots, existing optional `PROJECT-CONFIG.md`, and all current authority homes.
3. Include creation of `<Project-Root>/PROJECT-BOOTSTRAP.md` in the upgrade Preview; do not create it merely because upstream `main` advanced.
4. Apply only with the mutation authority required by the existing upgrade contract. Materialize the root file from the `1.7.0` template using the Project's real relative Project Source root.
5. Verify the new root bootstrap resolves the existing active `00 / FRAMEWORK-001`, then `01`, then `03`; resolve `09 Handoff` for continuation when applicable.
6. Treat `PROJECT-BOOTSTRAP.md` as discovery/locator only. It does not replace Project Location Binding, current branch/worktree, Integration Target, Implementation Source, Runtime authority, or `AUTH-*`/Risk authority.
7. If root bootstrap, vendor adapter, `PROJECT-CONFIG.md`, or active root binding contradict materially, fail closed for affected mutation and route resolution through existing governance; do not choose by recency.
8. Verify affected scope and run one final `RELEASE_FULL` on the unchanged target candidate; record material adoption in `16 Migration Registry` when applicable.

---

## 1.5.0 → 1.6.0

### Affected distribution surfaces

- `FRAMEWORK-RELEASE.yaml` — Framework version `1.6.0`; latest amendment pointer moves to TASK-022
- `references/framework-governance-amendment-260828-task022.md` / `core-governance-rules.md` / `SKILL.md` — standard conditional `92 Project Graph`, `REL-*`, late-binding and AI-ControlTower/OpenViking derived-index contract
- `templates/00-project-source-framework.md`, `templates/core-document-skeletons.md`, `templates/project-source-mockup/` — Project Graph applicability/routing and new `92-Project-Graph.template.md`
- `tests/pressure-scenarios.md` — relation authority, late-binding, rebuild, collision, merge/split, and extension-type pressure coverage
- `README.md` — release identity and Federated Project Graph explanation

### Upgrade checklist

1. Run `[Project Upgrade]`; fresh-compare the active local pin with target `1.6.0` and use Direct-to-Latest classification/Preview rules.
2. Preserve Project-specific rules, bindings, Stable IDs, history, and current authoritative homes; `REL-*` does not absorb `DEP-*`, `DEC-*`, `REQ-*`, `DRIFT-*`, or `CONFLICT-*` payloads.
3. Inspect active slot `92`. If custom content already occupies it, fail closed to `MIG-*`; preserve identity/history/references and relocate only through approved migration before standard `92` activation.
4. Do not create `92` merely for completeness. Materialize it only when Project relation truth is applicable; Projects may bind relations later.
5. Preserve immutable `project_uuid` as relation endpoint identity. Relation topology does not rewrite repository/workspace/runtime/integration/implementation bindings.
6. Treat AI-ControlTower/OpenViking as derived/rebuildable indexing only; do not migrate canonical Project relation truth into OpenViking.
7. Verify affected scope and run one final `RELEASE_FULL` on the unchanged target candidate; record the upgrade in `16 Migration Registry` when material.

---

## 1.3.1 → 1.4.0

### Affected distribution surfaces

- `FRAMEWORK-RELEASE.yaml` — version bump; new optional `migration_notes` / `upgrade_preview_template` fields
- `references/framework-governance-amendment-260825-task020.md` — new latest amendment
- `MIGRATION-NOTES.md`, `templates/upgrade-preview.md` — new files
- `SKILL.md` / `core-governance-rules.md` — FAST_PATH scope rule, launcher compaction policy, `[Project Upgrade]` report content contract
- `README.md` — current release identity

### Upgrade checklist

1. Run `[Project Upgrade]`; confirm `UPGRADE_AVAILABLE` with target `1.4.0`.
2. Classify: projects pinned at `1.3.x` are normally `FAST_PATH` (additive governance only; Schema unchanged).
3. Preview using `templates/upgrade-preview.md`; preservation checklist must show local pin, Stable IDs, Project rules, bindings, history all preserved.
4. Obtain explicit mutation approval after Preview.
5. Apply: update the local pin/amendment pointer to the target release; add nothing else.
6. Verify per the FAST_PATH scope rule: if the exact target tree carries committed state-bound evidence, proportional confirmation suffices; otherwise one full verification.
7. Record outcome in `16 Migration Registry` (`MIG-*`) with evidence.

### Notes for older transitions

- `1.4.0 → 1.5.0`: additive ChatGPT→MCP continuity governance; use governed Direct-to-Latest assessment from current sources.
- `1.3.0 → 1.3.1`: additive `[Project Upgrade]` command registration; FAST_PATH typical.
- Earlier transitions: no migration notes exist (`UNKNOWN`); use governed Direct-to-Latest assessment from current sources.
