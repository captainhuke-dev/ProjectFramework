# TASK-021 Design Spec — ChatGPT→MCP Continuity (Continuous System Management)

Date: 2026-08-25 · Status: `DRAFT — AWAITING USER APPROVAL` · Target release: **Framework 1.5.0 / Schema 1.0.0**

## Problem

System management driven through ChatGPT → MCP stops frequently. Root causes are distinct and need distinct fixes:

| # | Root cause | Today's behavior |
|---|---|---|
| A | ChatGPT session/conversation expiry | In-chat context lost; a fresh session must rediscover state by interrogation |
| B | MCP connection drop mid-task | Partial operations; restart from scratch or guess progress |
| C | Per-step approval gates | Continuous flows stop repeatedly for approvals that are predictable in advance |

## Design — four items

### 1. Continuation Contract (fixes A)

New normative rule (Core Governance, persistence section + SKILL):

- Every Logical Checkpoint on Material work MUST write a **Resume Block** into `09 Handoff` (and mirror one-line status into `03 Current State`) containing exactly: active task ID, last completed step, next step, open blockers, and the envelope reference if one is active.
- A fresh session (ChatGPT, Claude, or any agent with MCP access to the Project Source) MUST be able to resume Material work from the Resume Block alone within one read — no chat-history dependency.
- Resume Block is plain Markdown table rows; no new file format, no new semantic slot (`09` already owns handoff).
- Failure to persist the Resume Block = existing `PERSISTENCE_PENDING` semantics; nothing new.

### 2. Pre-Approved Action Envelope — `[Session Envelope]` (fixes C)

New registered command (added to the 16.4 registry alongside `[Project Status]`, `[Project Path]`, `[Project Upgrade]`):

```text
[Session Envelope] : declare, show, or close the user-pre-approved scope of operations for the current session/task
```

Semantics:

- `declare` — user states scope in natural language; the agent writes it as an explicit Envelope entry in `15 Action Registry` (`ENV-*` Stable-ID family, reusing existing registry conventions): allowed operation types, target surfaces, expiry (session end / task done / explicit time), and prohibited zones.
- `show` — display the active Envelope and remaining validity.
- `close` — end the Envelope early.

Hard boundaries (never overridable by any Envelope):

- No location/binding changes, no Root Governance mutation, no schema/slot authority, no secret handling, no push — these keep their own approval gates.
- Anything ambiguous or outside the declared types fails closed to normal approval.
- One-off exact-target instructions remain action-specific as today; Envelope is persistent-but-bounded, recorded and auditable in `15`.

This converts "approve each step" into "approve the boundary once" while keeping fail-closed governance for everything unpredictable.

### 3. MCP Resume Semantics (fixes B)

Normative requirement (Core Governance, connector/persistence section):

- Material MCP operations that mutate state SHOULD be structured as idempotent steps: repeating an already-applied step produces no duplicate effect.
- Each step declares its resume checkpoint: after a connection drop, work resumes from the last persisted Logical Checkpoint/Resume Block — never from memory of the dropped session.
- Non-idempotent operations (e.g., "send message", "create record") MUST record pre-execution intent in the current Checkpoint before the call, so a drop cannot cause silent double-execution without evidence.
- This is a contract for runtime implementations (including the future lnwjud Persistent MCP Relay) — ProjectFramework defines it, does not implement it.

### 4. Continuity health fields in `[Project Status]`

Extend the existing Status dimensions with a **Continuity** dimension:

- Age/freshness of the latest Resume Block (`FRESH | STALE | NONE`)
- Active Envelope (`ENV-*`, valid/expired)
- Repeated-break indicator when handoffs show the same link breaking across consecutive checkpoints (surfaced as `ISS-* KNOWLEDGE_DEBT` candidate)

Vocabulary reuses existing families only — no new lifecycle/state family.

## Surfaces touched

- `references/core-governance-rules.md` — Continuation Contract, Resume Semantics, Envelope boundaries (16.4 registry + persistence sections)
- `SKILL.md` — command registry, operational summaries
- `templates/core-document-skeletons.md` + mockup templates `03`, `09`, `15` — Resume Block row format, `ENV-*` entries
- Launchers — compact mention of `[Session Envelope]` + Resume Block rule (watch the 4,500 ceiling)
- `README.md` — release identity 1.5.0 + section
- `tests/pressure-scenarios.md` — scenarios 158–162
- `FRAMEWORK-RELEASE.yaml` — version bump

## Constraints

Documentation/governance only — no relay/runtime implementation, validator, CLI, automation artifact. Schema stays `1.0.0`; canonical tokens unchanged; historical amendments untouched; launchers ≤4,500 byte-identical markers; `commit ≠ push`. Runtime implementation (outbound WS relay) remains lnwjud scope, contract-compatible with item 3.

## Verification plan

1. Pressure scenarios 158–162 (one per item + boundary case: Envelope attempting to override fail-closed governance).
2. Structural checks: registry contains exactly 4 commands everywhere; Resume Block format present in skeletons/templates; Envelope boundary wording in normative sources; launchers compliant.
3. AFFECTED → one RELEASE_FULL → evidence → task reconciliation.

## Release identity decision requested

Recommend **1.5.0**: adds a new registered command + new Stable-ID family (`ENV-*`) — more than a patch; still backward compatible.
