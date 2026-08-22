---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.2.3"
project_source_framework_version: "1.2.4"
project_source_schema_version: "1.0.0"
approved_at: "2026-08-22T14:40:00+07:00"
approval_basis: "USER_EXPLICIT_APPROVAL"
compatibility: "backward-compatible governance/documentation change"
---

# Framework Governance Amendment — Project Location Binding, Chat Closure Consistency, and Mandatory Response Close

## Binding Change

Framework `1.2.4` adds **Project Location Binding**, **Chat Closure Consistency**, and a clearer **Mandatory Response Close** contract while preserving Project Source Schema `1.0.0`, the existing semantic-slot namespace, existing Stable-ID families, Project-local Framework pinning, Framework `1.2.1` Externalized Working Memory / Chat Lifecycle semantics, Framework `1.2.2` Canonical Integration Target / Base Freshness semantics, and Framework `1.2.3` Canonical Implementation Source / Runtime Authority semantics.

The binding changes are as follows.

## 1. Project Location Binding

1. The canonical home of **Project Location Binding** for an initialized Project is the active local `00 Project Source Framework` / `FRAMEWORK-001`. `03 Current State` and `09 Handoff` MAY reference the binding but MUST NOT maintain an independent authoritative copy.
2. GitHub and Google Drive bindings are independent. Each applicable system MUST resolve to exactly one state:
   - `BOUND`
   - `NOT_APPLICABLE`
   - `VERIFICATION_REQUIRED`
3. `BOUND` means the Project has sufficient durable routing identity for Material Project work through that system. Minimum durable routing identity is:
   - GitHub: repository owner/name **or** canonical repository URL.
   - Google Drive: project-root folder ID **or** canonical folder URL.
4. A display name, textual Drive path, recent repository activity, chat memory, connector ranking, or search result alone is insufficient to establish `BOUND`.
5. When a system is `BOUND`, Material mutation MUST target the declared durable routing identity when comparison is possible. A material target mismatch blocks the affected mutation until resolved; existing `DRIFT-*` semantics apply when expected-alignment domains materially disagree.
6. `VERIFICATION_REQUIRED` is fail-closed for Material mutation. Read/search/discovery, candidate comparison, and user confirmation needed to resolve the location MAY proceed, but the Agent MUST NOT perform Material mutation through the unresolved system by default.
7. A User Explicit Instruction that names an exact target MAY authorize that one otherwise-authorized action while the persistent binding remains `VERIFICATION_REQUIRED`. The action-specific instruction MUST NOT silently promote the binding to `BOUND` or persistently rewrite Project Location Binding.
8. `NOT_APPLICABLE` means that connector/system is outside the Project's declared working-location contract. Material Project work through that system is blocked by default until an explicitly approved binding/scope change is promoted through Root Governance.
9. Changing an active Project Location Binding is a **Root Governance mutation**. It requires User Explicit Approval and the existing governed `FRAMEWORK-001` revision → validate → promote → supersede/archive flow.
10. Connector discovery, recent activity, search ranking, a newly accessible repository/folder, or another Project's location MUST NOT transfer routing authority or silently rewrite the active binding.
11. Observed location evidence that contradicts the active binding is observation/evidence, not automatic authority transfer. The Agent MUST stop the affected mutation, disclose the mismatch, and preserve existing conflict/drift handling.
12. Project Location Binding answers **where** Project work belongs. Existing `AUTH-*` / `DEL-*`, approval, and risk rules continue to answer **who may mutate what**. Location Binding grants no independent mutation authority.
13. Project-specific repository, Drive-root, and progress-pointer values belong in local `FRAMEWORK-001`; platform launchers only instruct the Agent to resolve the local binding and MUST NOT become a second Project-specific location source of truth.
14. Google Drive folder/file IDs or canonical URLs are preferred durable routing identities when available. A human-readable display path is descriptive only. Existing source-native persistence rules remain unchanged: Material work persists at Logical Checkpoints to the source-native owner, using the existing designated progress Markdown or one stable `PROJECT-PROGRESS.md` continuation cache only when required.

## 2. Separation from Git and Implementation Authority

Project Location Binding is a repository/container routing boundary and MUST remain distinct from current Git execution state and implementation authority:

```text
Repository Binding
≠ current branch/worktree
≠ Canonical Integration Target
≠ Canonical Implementation Source
```

Framework `1.2.4` MUST NOT add `canonical_branch` or any equivalent parallel branch authority to Project Location Binding.

Framework `1.2.2` continues to govern Canonical Integration Target, `FRESH | STALE_NON_SEMANTIC | STALE_SEMANTIC | UNKNOWN`, `BASE_STALE`, `REBASE_REQUIRED`, `FORWARD_PORT_REQUIRED`, `STACKED_WORK`, and the Pre-Merge Base Freshness Gate. **Mergeable ≠ Acceptable.**

Framework `1.2.3` continues to govern Canonical Implementation Source and Runtime Truth independently. Binding a GitHub repository does not by itself determine which source path or workspace is authoritative `IMPLEMENTATION` Truth.

## 3. Initialized-Project and GREENFIELD Behavior

For an initialized Project, after resolving active local `FRAMEWORK-001`, the Agent MUST read Project Location Binding before Material GitHub or Google Drive work and apply the state contract above.

A GREENFIELD Project has no active local `FRAMEWORK-001`; therefore pre-binding discovery is limited to read/search/inspection needed to identify candidate locations. The bootstrap sequence is:

```text
canonical Framework bootstrap read
→ discovery/read-only inspection of candidate Project locations when needed
→ Preview proposed GitHub/Drive Project Location Binding
→ explicit user approval
→ first Material Project-Source write creates active 00 / FRAMEWORK-001 with the approved binding
→ subsequent Material connector work resolves and obeys that active binding
```

The Preview MUST classify each applicable system as `BOUND`, `NOT_APPLICABLE`, or `VERIFICATION_REQUIRED`. An unresolved applicable system remains fail-closed for Material mutation through that connector. Initial creation and major structural migration retain the existing Preview → explicit approval → write gate.

## 4. Chat Closure Consistency

Framework `1.2.4` strengthens the existing `CONTINUE_CURRENT_CHAT | START_NEW_CHAT` lifecycle contract with these binding invariants:

1. If `[Next Action]` is exactly `ไม่มีขั้นตอนถัดไป`, `[Chat]` MUST be `START_NEW_CHAT`.
2. If `[Chat]` is `CONTINUE_CURRENT_CHAT`, `[Next Action]` MUST contain one concrete continuation action and MUST NOT be `ไม่มีขั้นตอนถัดไป`.
3. `PERSISTENCE_PENDING` MUST pair with `CONTINUE_CURRENT_CHAT` and one concrete persistence/recovery Next Action. `PERSISTENCE_PENDING + ไม่มีขั้นตอนถัดไป` is invalid.
4. `START_NEW_CHAT` MAY pair with a concrete Next Action when required Material state is durably persisted and the next work is safely resumable from external durable state plus Required Read pointers.
5. `START_NEW_CHAT` remains a continuation-safety recommendation, not a claim that the platform forces chat navigation.
6. The existing persistence gate remains binding: `START_NEW_CHAT` MUST NOT be recommended as continuation-safe while required Material state is `PERSISTENCE_PENDING`.

## 5. Mandatory Response Close

Every Framework-governed response continues to end with exactly two headings, in order, with nothing after the second section. Framework `1.2.4` standardizes the field display under the second heading as four separate Markdown paragraphs:

```text
### ทำอะไรไป?

<concise statement of what was done or determined>

### และถัดไปคืออะไร?

[Next Action]: <one exact next action or ไม่มีขั้นตอนถัดไป>

[Chat]: CONTINUE_CURRENT_CHAT | START_NEW_CHAT

[Reason]: <concise reason>

[Required Read]: <canonical locations or ไม่มี>
```

The canonical lifecycle tokens remain unescaped `CONTINUE_CURRENT_CHAT` and `START_NEW_CHAT`; any Markdown escaping is presentation-only and MUST NOT create a different state vocabulary.

## 6. Migration and Backward Compatibility

1. Project Source Schema remains `1.0.0`.
2. Framework `1.2.4` adds no semantic slot, Stable-ID namespace, Project lifecycle state, Git freshness state, or new authority family.
3. Existing initialized Projects remain governed by their locally pinned active `FRAMEWORK-001`; upstream Framework `1.2.4` does not auto-upgrade them.
4. Migration to `1.2.4` MUST NOT invent Project locations. Known repository/folder IDs or URLs must come from actual Project sources, connector/system observation, or explicit user confirmation.
5. During migration, each GitHub/Drive system is classified `BOUND`, `NOT_APPLICABLE`, or `VERIFICATION_REQUIRED`; insufficient identity remains explicit uncertainty rather than fabricated certainty.
6. Migration MUST NOT create or migrate a `canonical_branch` field and MUST preserve Canonical Integration Target semantics separately.
7. Continuation documents SHOULD reference the active root binding rather than duplicate Project-location authority.
8. Canonical Implementation Source semantics remain independent and unchanged.
9. Actual secrets, access tokens, and connector credentials remain forbidden in Project Source and Framework artifacts.
10. Historical amendments/specs remain historical and are not rewritten.

## Scope Boundary

This amendment changes governance, routing, continuation, and response-format semantics only. It does not authorize or add connector synchronization, repository/folder auto-selection, application source code, Docker/runtime artifacts, scripts, validators, CLI tooling, Git hooks, CI/CD, bots, schedulers, background automation, branch-protection automation, or runtime enforcement.

All prior Framework invariants that are not explicitly amended above remain binding.
