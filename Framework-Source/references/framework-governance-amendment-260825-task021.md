---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.4.0"
project_source_framework_version: "1.5.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_EXPLICIT_IMPLEMENTATION_APPROVAL_2026-08-25"
compatibility: "BACKWARD_COMPATIBLE_MCP_CONTINUITY_GOVERNANCE"
---

# Framework 1.5.0 Amendment — ChatGPT→MCP Continuity

Framework `1.5.0` preserves `1.4.0` unless refined here; Project Source Schema stays `1.0.0`; release format stays `3`. No new semantic document slot and no new lifecycle/authority state family is created; the command registry gains one command and `15 Action Registry` gains one entry family (`ENV-*`).

## 1. Continuation Contract

At every Logical Checkpoint on Material work, the agent MUST persist a **Resume Block** into `09 Handoff` (mirrored as a one-line status in `03 Current State`) containing exactly: active task ID, last completed step, next step, open blockers, and the active Envelope reference (`ENV-*`) if any. A fresh session — ChatGPT, Claude, or any agent with MCP access to the Project Source — MUST be able to resume Material work from the Resume Block alone within one read, with no chat-history dependency. Failure to persist follows existing `PERSISTENCE_PENDING` semantics; no new failure state is created.

## 2. Pre-Approved Action Envelope — `[Session Envelope]`

The registered command list gains exactly:

```text
[Session Envelope] : declare, show, or close the user-pre-approved scope of operations for the current session/task
```

- `declare` records an explicit Envelope (`ENV-*` entry in `15 Action Registry`): allowed operation types, target surfaces, expiry (session end / task completion / explicit time), and prohibited zones.
- `show` displays the active Envelope and remaining validity; `close` ends it early.
- An Envelope never overrides fail-closed governance: location/binding changes, Root Governance mutation, schema/slot authority, secret handling, and push keep their own approval gates regardless of any Envelope.
- Ambiguous or out-of-scope operations fail closed to normal approval. One-off exact-target instructions remain action-specific as before.

This converts repeated per-step approvals into a single bounded pre-approval while keeping unpredictable actions governed.

## 3. MCP Resume Semantics

Material MCP operations that mutate state SHOULD be structured as idempotent steps: re-executing an already-applied step produces no duplicate effect. Non-idempotent operations MUST record pre-execution intent in the current Checkpoint before the call, so a connection drop cannot cause silent double-execution without evidence. After any drop, work resumes from the last persisted Resume Block/Logical Checkpoint — never from memory of the dropped session. This is a contract for runtime implementations (including future persistent relay runtimes); this Framework defines it and implements none of it.

## 4. Continuity health in `[Project Status]`

`[Project Status]` gains a **Continuity** dimension reporting: freshness of the latest Resume Block (`FRESH | STALE | NONE`), the active Envelope (`ENV-*`, valid/expired), and a repeated-break indicator when handoffs show the same link breaking across consecutive checkpoints (surfaced as an `ISS-* KNOWLEDGE_DEBT` candidate). All vocabulary reuses existing families.

## Non-goals

No relay/runtime implementation, validator product, CLI, hook, bot, CI/CD, scheduler, watcher, or automation artifact. Existing initialized Projects remain locally pinned and do not auto-upgrade.
