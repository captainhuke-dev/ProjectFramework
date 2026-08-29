---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.2.4"
project_source_framework_version: "1.2.5"
project_source_schema_version: "1.0.0"
approved_at: "2026-08-22T18:23:00+07:00"
approval_basis: "USER_EXPLICIT_APPROVAL"
compatibility: "BACKWARD_COMPATIBLE_AGENT_CONTINUITY_PROGRESSIVE_VERIFICATION_AND_LOCAL_WORKSPACE_BINDING"
---

# Framework Governance Amendment — Agent Continuity, Progressive Verification, Local Workspace Binding, and Response Close Completeness

## Binding Change

Framework `1.2.5` adds four coordinated governance/workflow improvements while preserving Project Source Schema `1.0.0`, the existing semantic-slot namespace, existing Stable-ID families, Project-local Framework pinning, and Framework `1.2.1–1.2.4` semantics except where explicitly refined below.

## 1. Verified Task Completion Checkpoint

1. For a Material Task / `ACT-*` that materially mutates a Git-backed Canonical Implementation Source or another authoritative repository artifact, durable `DONE` requires a **Verified Task Completion Checkpoint**.
2. A Verified Task Completion Checkpoint requires: the governed Task scope is complete; applicable affected-scope/risk verification passed; the required completed state is represented by observed Git commit(s); no required completed result exists only as uncommitted working-tree state; remaining working-tree changes are understood; and the completion commit identity is observed rather than fabricated.
3. Read-only discovery, analysis, review, or another Task with no repository mutation does not require a synthetic commit merely to finish.
4. Failed, blocked, cancelled, or incomplete work cannot use commit existence as proof of `DONE`. `WIP commit ≠ Task DONE`.
5. One Task may use multiple coherent commits. The Framework does not require exactly one commit per Task.
6. **`commit ≠ push`**. A local commit establishes a durable Git checkpoint in the current repository; remote publication is a separate shared-state/authority action.
7. Cross-environment handoff is continuation-safe only when the receiving execution environment can obtain the completion commit through the same durable repository or another governed shared/remote transfer.
8. A completion commit proves durable completion of governed work only. Existing `ACT DONE ≠ MS REACHED ≠ OUT ACHIEVED` remains binding.

## 2. Progressive / Risk-Scoped Verification and Evidence Reuse

1. Verification depth is determined by affected scope, dependency impact, and existing `R0 / R1 / R2 / R3` risk semantics, not by Task count or a blanket rule to rerun every check.
2. Framework workflow vocabulary may use `TASK_LOCAL_FAST`, `CHECKPOINT_INTEGRITY`, `RELEASE_FULL`, and `INTEGRATION_GATE`. These are workflow labels only, not Project lifecycle states, Epistemic Status values, Git freshness states, or Stable-ID families.
3. `TASK_LOCAL_FAST` means the minimum sufficient checks needed to prove the affected behavior/invariants at the Task's applicable risk level.
4. `CHECKPOINT_INTEGRITY` means durable continuation integrity: usable result persisted, completion commits identifiable when applicable, working-tree state understood, blockers/pending state known, Exact Next Action and Required Read durable, plus only materially affected cross-surface checks. **Logical Checkpoint ≠ RELEASE_FULL**.
5. `RELEASE_FULL` is reserved for a completed Release Candidate or equivalent semantic acceptance boundary and verifies the current distribution/candidate as a whole once per unchanged candidate state, subject to stricter Project rules.
6. Reusable verification evidence is state-bound. When material it identifies the candidate/source identity or Git HEAD/tree, affected scope/profile/invariants, result, captured time, and relevant dependency/integration-target assumptions.
7. Fresh evidence may be reused while the state/assumptions it proves remain materially unchanged.
8. Candidate/source changes, materially changed dependencies, semantic target movement, changed verification criteria, contradicting evidence, or unbounded uncertainty selectively invalidate affected evidence. If impact cannot be bounded safely, verification escalates.
9. `INTEGRATION_GATE` re-resolves the current Canonical Integration Target, applies Framework `1.2.2` Base Freshness, and checks evidence validity before acceptance. It reruns only invalidated/newly affected checks unless impact cannot be bounded safely.
10. Exact fast-forward/integration to an already verified candidate tree normally requires resulting-state confirmation rather than unconditional `RELEASE_FULL` rerun. Rebase, conflict resolution, merge-time edits, semantic target movement, or another tree-changing operation triggers affected/full reverification as required.
11. `Mergeable ≠ Acceptable` remains binding.

## 3. Environment-Scoped Local Workspace Binding

1. Active local `FRAMEWORK-001` remains the canonical home of Project Location Binding and now MAY contain one or more **Local Workspace Binding** entries scoped to declared execution environments.
2. Local Workspace Binding answers **where a local execution surface may operate for Material Project work**. It does not define implementation, branch, integration, or runtime authority.
3. Each applicable local environment reuses exactly `BOUND | NOT_APPLICABLE | VERIFICATION_REQUIRED`.
4. `BOUND` requires a verified or user-confirmed absolute canonical local Project/workspace path for that environment. For Git-backed work, repository owner/name or canonical URL SHOULD be cross-checked when practical so path/folder-name coincidence does not silently bind the wrong clone.
5. `VERIFICATION_REQUIRED` permits read/list/search/inspect needed to resolve the workspace but blocks Material local/MCP mutation by default.
6. `NOT_APPLICABLE` blocks Material local/MCP Project work for that declared scope/environment until an explicitly approved Root Governance binding/scope revision.
7. A User Explicit Instruction naming one exact local target MAY authorize that one otherwise-permitted action under existing one-off-target semantics; it does not persistently rewrite Local Workspace Binding.
8. Persistent Local Workspace Binding change is a `FRAMEWORK-001` Root Governance mutation requiring User Explicit Approval and the existing revision → validate → promote → supersede/archive flow.
9. MCP `workspaceId`, editor handles, active/recent workspace lists, search ranking, and similar tool/runtime identifiers are observed routing evidence only. They are never canonical Project identity and never transfer persistent routing authority.
10. A Project MAY use different Local Workspace Binding paths across workstations, VMs, WSL distributions, Dev Containers, remote durable workspaces, or other execution environments. One global absolute path is not required.
11. If local execution is applicable but no verified entry can be resolved for the current environment, the effective local binding is `VERIFICATION_REQUIRED`.
12. Required semantic separation is preserved:

```text
Repository Location Binding
≠ Local Workspace Binding
≠ current branch/worktree
≠ Canonical Integration Target
≠ Canonical Implementation Source
≠ Runtime Location
```

13. Local Workspace Binding may reference the same physical path as Canonical Implementation Source in a simple Git Project, but value alignment never collapses the distinct meanings or authorities.

## 4. Response Close Completeness Gate

1. Every Framework-governed assistant response MUST perform a lightweight **Response Close Completeness Gate** immediately before emit.
2. The gate verifies the assistant final-response representation contains exactly the two mandatory headings in order and exactly one `[Next Action]:`, `[Chat]:`, `[Reason]:`, and `[Required Read]:` as separate Markdown paragraphs in that order.
3. `[Chat]` contains exactly one canonical lifecycle token: `CONTINUE_CURRENT_CHAT` or `START_NEW_CHAT`.
4. Existing Chat Closure Consistency remains binding: `ไม่มีขั้นตอนถัดไป` pairs only with `START_NEW_CHAT`; `CONTINUE_CURRENT_CHAT` requires one concrete Next Action; `PERSISTENCE_PENDING` requires `CONTINUE_CURRENT_CHAT` plus one concrete persistence/recovery action.
5. `[Required Read]` is the final governed response content; nothing follows the mandatory close.
6. Missing, duplicate, malformed, out-of-order, or semantically contradictory mandatory-close content means the assistant response is incomplete and must be corrected before emit.
7. The gate verifies the assistant response representation only. It MUST NOT claim visibility into downstream transport, application rendering, or UI transformation.
8. A user-reported rendered omission remains valid regression evidence, but the exact loss layer remains `UNVERIFIED` unless independently observed. Framework must not fabricate whether generation, transport, or rendering caused the omission.

## 5. Handoff, Evidence, and Preflight Integration

1. When material to continuation, `09 Handoff` may reference observed repository identity, active Local Workspace Binding, current branch/worktree, verified HEAD, working-tree state, last completed Task/ACT, completion commit(s), verification result/evidence pointer, remote reachability when needed, and Exact Next Action.
2. These observations grant no authority by themselves and do not redefine Repository Location Binding, Canonical Integration Target, or Canonical Implementation Source.
3. Reusable verification evidence is registered as formal `EVD-*` only when its importance/risk requires durable evidence registration. Routine Task-local checks do not require a new `EVD-*` merely because they ran.
4. Before Material local/MCP mutation, preflight resolves the applicable Local Workspace Binding in addition to existing Project Location Binding, Authority, Risk, Requirements/Decisions, and Git/workspace checks.

## 6. GREENFIELD and Migration

1. GREENFIELD discovery may inspect candidate GitHub/Drive/local workspaces read-only. Preview includes applicable local environment binding states/identities before explicit approval and first active `00` creation.
2. Existing initialized Projects remain governed by their locally pinned Framework and do not auto-upgrade.
3. Migration to `1.2.5` MUST NOT invent local paths, environment scope identities, completion commit provenance, verification evidence, repository origins, or MCP workspace identifiers.
4. For an applicable local environment: verified/user-confirmed path → `BOUND`; local execution applicable but unresolved → `VERIFICATION_REQUIRED`; local execution outside declared scope → `NOT_APPLICABLE`.

## 7. Compatibility and Scope Boundary

Framework `1.2.5` adds no semantic slot, Stable-ID namespace, Project lifecycle state, Git freshness state, authority family, executable validator, hook, bot, CI/CD workflow, scheduler, background agent, filesystem watcher, automatic workspace selector, merge queue, or runtime enforcement service.

All prior Framework invariants not explicitly amended above remain binding. Historical amendments/specs remain historical and are not rewritten.
