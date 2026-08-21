# MCP Material Persistence and Chat Lifecycle Design

Date: 2026-08-21
Status: DESIGN APPROVED IN CHAT / WRITTEN SPEC REVIEW PENDING
Repository: `captainhuke-dev/ProjectFramework`

## 1. Purpose

Reduce Web Chat context growth and continuation latency by treating Chat as a temporary interaction/execution surface rather than long-term Project memory. Material work performed through MCP/connectors must be persisted at logical checkpoints to an external canonical working source so a later session can continue without depending on the old chat transcript.

This design also standardizes an explicit recommendation at the end of every response for whether to continue in the current chat or start a new chat.

## 2. Scope

This feature governs:

1. Classification of MCP activity as Material or Transient.
2. Persistence of Material Project Work to GitHub or Google Drive working sources.
3. Compact chat responses after MCP work.
4. Continuation state and handoff pointers.
5. Chat lifecycle recommendation: `CONTINUE_CURRENT_CHAT` or `START_NEW_CHAT`.
6. Persistence safety before recommending a new chat.
7. Launcher wording while preserving the existing 4,500-character limit.

## 3. Non-Goals

This feature does not:

- create an MCP transcript/archive;
- require persistence for every connector read/search;
- make Chat a canonical source of Project truth;
- introduce a scheduler, background agent, validator, or runtime automation;
- duplicate authoritative content into multiple stores;
- change existing authority, approval, migration, Stable-ID, or secret-handling rules;
- make upstream Framework material override a locally pinned `FRAMEWORK-001`.

## 4. Terminology

### 4.1 Material Project Work

MCP activity is Material when it produces or changes information required for reliable continuation, governance, decision-making, or execution. Examples include:

- current state change;
- completed or pending work;
- Decision, Requirement, Issue, Drift, Risk, Assumption, Milestone, Outcome, Dependency, Change Request, or Gate state;
- artifact creation or modification;
- material evidence or finding;
- blocker;
- verified source/runtime fact needed by later work;
- exact next action or continuation dependency.

### 4.2 Transient MCP Activity

MCP reads/searches/comparisons are Transient when their intermediate detail is not required for future continuation or current Project truth. Examples include exploratory queries, redundant reads, discarded search results, and intermediate comparisons.

### 4.3 Logical Checkpoint

A logical checkpoint is the point at which a coherent unit of Material Project Work has reached a stable-enough state to persist. Persistence is checkpoint-based, not tool-call-based.

## 5. Core Contract: Externalized Working Memory

Chat MUST NOT become persistent working memory merely because MCP/connectors were used.

When MCP activity produces Material Project Work:

1. Accumulate transient tool detail only as needed for the current reasoning/execution step.
2. At a logical checkpoint, persist the current usable result to the correct external working source.
3. Keep the Chat response compact: outcome, canonical location/pointer, blocker if any, exact next action, and chat recommendation.
4. Do not paste raw MCP payloads, long search results, full diffs, or repetitive intermediate state into Chat unless the user explicitly requests them or they are necessary to obtain approval/resolve ambiguity.

Transient MCP activity does not require persistence.

## 6. GitHub Persistence

When Material Project Work is associated with a GitHub-backed Project, persist it in that repository using the canonical semantic home or actual artifact that owns the state.

Where Project Source exists, examples include:

- `03 Current State` → current snapshot;
- `04 Decision Log` → `DEC-*`;
- `05 Requirements` → `REQ-*`;
- `08 Open Issues` → `ISS-* / DRIFT-* / CONFLICT-*`;
- `09 Handoff` → continuation contract;
- `10 Change Log` → applied/observed `CHG-*` history;
- `13 Evidence Registry` → `EVD-*`;
- `15 Action Registry` → `ACT-*`;
- `91 Project Management Control` → `RISK-* / ASM-* / MS-* / OUT-* / DEP-* / CR-* / GATE-*`.

If the Material result is source code, configuration, documentation, or another repository artifact, the artifact itself remains its natural canonical location. Project Source should reference it when needed rather than duplicate it.

`09 Handoff` MUST remain a continuation contract, not a full MCP activity log. Store only continuation-relevant summary, pointers, warnings, required read order, and exact next action.

## 7. Google Drive Persistence

For a Drive-oriented Project, use an existing Project progress Markdown file when one already exists. Do not create a duplicate progress ledger.

When none exists and Material MCP work requires durable continuation state, establish one stable progress Markdown file, recommended name:

`PROJECT-PROGRESS.md`

The progress file is a Continuation Cache / Progress Ledger, not Root Governance and not an alternative source of truth.

Minimum structure:

```text
# Project Progress

Last Updated:
Current Objective:

## Current State

## Material Work Completed

## Decisions / Findings

## Artifacts / Source Locations

## Blockers / Pending

## Exact Next Action

## Chat Continuity
CONTINUE_CURRENT_CHAT | START_NEW_CHAT
Reason:
Required Read Before Continue:
```

The file MUST NOT become a dump of MCP parameters, raw connector responses, long search result sets, intermediate reasoning, or duplicate authoritative document content.

If Google Drive stores the authoritative business artifact, the progress file references that artifact and records only enough current state for continuation.

## 8. Projects Using Both GitHub and Google Drive

Use source-native ownership and avoid a third source of truth.

Typical split:

- GitHub: implementation/source/repository Project Source and code-centric truth.
- Google Drive: business/collaborative artifacts and Drive-side continuation summary.

Cross-system continuation uses pointers/references rather than copying full content between systems.

One object type retains one authoritative home. The progress ledger and Handoff may reference authoritative sources but do not silently replace them.

## 9. Persistence Failure

If Material Project Work should be persisted but the destination cannot be written:

- record/report `PERSISTENCE_PENDING` or equivalent explicit state;
- state what remains unpersisted and where it should go;
- do not claim continuation safety;
- default to `CONTINUE_CURRENT_CHAT` until the necessary Material state is persisted.

A direct user instruction may override the recommendation to remain in the current chat, but the persistence risk must be disclosed.

## 10. Chat Lifecycle Policy

Every response governed by the Project launcher must recommend exactly one of:

```text
CONTINUE_CURRENT_CHAT
START_NEW_CHAT
```

### 10.1 Continue Current Chat

Recommend `CONTINUE_CURRENT_CHAT` when continuation benefits from immediate conversational context and there is no material reason to hand off, including:

- same objective/task;
- short clarification still required;
- current design/approval loop is active;
- Material checkpoint has not yet been reached;
- Chat/tool burden is still manageable;
- switching chats would add more overhead than value.

### 10.2 Start New Chat

Recommend `START_NEW_CHAT` when at least one material reason applies, including:

- a logical/material checkpoint is complete;
- phase changes (for example Design → Implementation, Implementation → Verification, Investigation → Remediation);
- objective/workstream changes materially;
- MCP/tool output has made the chat operationally heavy;
- handoff to a new agent/session is appropriate;
- prior assumptions/context may be superseded and could mislead continuation;
- a substantial new work package begins.

Do not use hard message-count/token-count thresholds that agents cannot reliably observe across platforms.

## 11. Persistence Gate Before New Chat

For Material Project Work, the Framework MUST NOT recommend `START_NEW_CHAT` until the minimum continuation state is durably available outside the chat.

Required gate:

```text
Material work persisted?      YES
Current state usable?         YES
Pending/blocker recorded?     YES
Exact next action recorded?   YES
Required read location known? YES
```

If any required item is NO, recommend `CONTINUE_CURRENT_CHAT` unless the user explicitly directs otherwise with the risk disclosed.

A new chat MUST NOT require the old chat transcript as a prerequisite for Project continuation.

## 12. New Chat Bootstrap

A new chat should bootstrap from persisted state rather than copied chat summaries.

GitHub Project default read pattern:

```text
00 → 01 → 03
→ 09 when continuation context is required
→ files routed by 01 / Exact Next Action
```

Drive-oriented Project default read pattern:

```text
Project governance/current source
→ PROJECT-PROGRESS.md (or existing designated progress file)
→ Required Read pointers
→ Exact Next Action
```

A short continuation prompt is sufficient, for example:

`Continue this Project from its canonical Project Source. Read the current continuation state and perform the Exact Next Action.`

## 13. Mandatory Response Close

Preserve the existing two mandatory headings in this exact order:

```text
ทำอะไรไป?

และถัดไปคืออะไร?
```

The second section must include at least:

```text
Next Action: <one exact next action>
Chat: CONTINUE_CURRENT_CHAT | START_NEW_CHAT
Reason: <concise reason>
Required Read: <locations, or ไม่มี>
```

If no next action remains, state that explicitly while still providing the chat recommendation.

No content may appear after the second section.

## 14. Launcher Constraint

`CHATGPT-PROJECT-INSTRUCTIONS.md` and `CLAUDE-PROJECT-INSTRUCTIONS.md` remain compact bootstrap launchers.

The complete content intended for the Project instruction field MUST remain at or below 4,500 Unicode characters. Detailed MCP persistence and chat lifecycle semantics belong in canonical Framework sources; the launchers should carry only the minimum binding pointer/summary necessary to require read-through.

The shared-contract text between platform markers MUST remain byte-identical.

## 15. Framework Integration Points

Implementation is expected to update, at minimum:

- `managing-project-source/SKILL.md` — operational workflow and quick-reference behavior;
- `managing-project-source/references/core-governance-rules.md` — normative MCP persistence/chat lifecycle contract;
- `managing-project-source/templates/project-source-mockup/09-Handoff.template.md` — chat continuity fields/persistence state where appropriate;
- `managing-project-source/tests/pressure-scenarios.md` — regression scenarios for chat bloat, persistence, failure, duplication, and chat switching;
- `managing-project-source/CHATGPT-PROJECT-INSTRUCTIONS.md` — compact binding summary/read-through while staying <=4,500 characters;
- `managing-project-source/CLAUDE-PROJECT-INSTRUCTIONS.md` — byte-identical shared contract and <=4,500 characters.

A Framework governance amendment and release metadata/version update should be evaluated during implementation according to existing release policy; they are not assumed automatically by this design.

## 16. Verification Scenarios

The implementation should cover at least these behavioral cases:

1. **Transient Read Pressure** — multiple GitHub/Drive searches produce no Material state; no persistence write is required.
2. **GitHub Material Checkpoint** — several reads and edits culminate in a material result; persist once at the logical checkpoint, not once per MCP call.
3. **Drive Progress Continuation** — Material Drive work updates the existing progress `.md`; no duplicate progress file is created.
4. **No Transcript Dump** — raw MCP payloads/search results are not copied into Project Source/progress merely for audit convenience.
5. **Cross-System Ownership** — GitHub and Drive artifacts reference each other without duplicating authoritative state.
6. **Persistence Failure** — required write fails; response reports pending persistence and recommends current chat.
7. **Phase Transition** — persisted Design checkpoint recommends `START_NEW_CHAT` for Implementation with a Required Read list.
8. **Clarification Loop** — unresolved design clarification recommends `CONTINUE_CURRENT_CHAT`.
9. **New Chat Independence** — continuation can proceed from persisted state without requiring the old chat transcript.
10. **Launcher Limit** — both platform launcher contents remain <=4,500 Unicode characters and shared contract is byte-identical.
11. **Mandatory Close** — clarification, status, error, refusal, and completion responses all end with the required headings plus Chat/Reason/Required Read fields.

## 17. Compatibility and Safety

- Existing initialized Projects remain pinned to their approved local Framework version; no automatic upgrade.
- Existing Project-specific progress files should be adopted by reference rather than replaced solely to match the suggested filename.
- This feature changes governance/workflow semantics only; it does not authorize application implementation or automation.
- Actual secrets remain prohibited from Project Source/progress files.
- Existing authority and approval gates remain binding for external writes.

## 18. Acceptance Criteria

The feature is complete when:

1. Framework normative/operational documents distinguish Material vs Transient MCP activity.
2. Material MCP work is required to persist at logical checkpoints to source-native external state.
3. GitHub and Google Drive persistence semantics are explicit and avoid duplicate source-of-truth state.
4. Persistence failure blocks a safe-new-chat recommendation by default.
5. Every governed response includes an exact next action plus chat recommendation, reason, and Required Read.
6. New Chat continuation is designed to operate from persisted state without old-chat dependency.
7. Both platform launchers remain <=4,500 Unicode characters and their shared contract remains byte-identical.
8. Pressure scenarios cover the new failure modes.
