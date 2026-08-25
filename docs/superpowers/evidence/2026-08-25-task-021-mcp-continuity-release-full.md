# TASK-021 ChatGPT→MCP Continuity (Framework 1.5.0) — RELEASE_FULL Evidence

Captured: `2026 whole-process 2026-08-25` (Asia/Bangkok)

Branch: `task-021-mcp-continuity`
Base: `main` at `ba4db29` (after TASK-020 publication records)

## Release identity

- Framework: **1.5.0** (previous 1.4.0) · Schema: **1.0.0** (unchanged) · release format **3**
- Latest amendment: `references/framework-governance-amendment-260825-task021.md` (approval basis: USER_EXPLICIT_IMPLEMENTATION_APPROVAL_2026-08-25)

## Implemented scope (all four design items)

1. **Continuation Contract** — every Logical Checkpoint on Material work persists a Resume Block into `09 Handoff` (task ID, last completed step, next step, blockers, active `ENV-*`), mirrored one-line in `03 Current State`; any fresh session resumes within one read; failure reuses `PERSISTENCE_PENDING`. Resume Block format added to core skeletons and mockup `09`.
2. **`[Session Envelope]`** — fourth registered command; declares/shows/closes a user-pre-approved bounded scope (`ENV-*` in `15 Action Registry`, with expiry + prohibited zones). Envelopes never override fail-closed governance (location/binding, Root Governance, schema authority, secrets, push keep own gates). Format note added to mockup `15`.
3. **MCP Resume Semantics** — mutations idempotent where possible; non-idempotent calls record pre-execution intent before the call; after drops, resume from persisted checkpoint truth, never session memory. Contract only — no runtime implemented.
4. **`[Project Status]` Continuity dimension** — Resume Block freshness (`FRESH | STALE | NONE`), active Envelope validity, repeated-break indicator (`ISS-* KNOWLEDGE_DEBT` candidate).

## Commits

- `e9c65f2` — feat: release framework 1.5.0 mcp continuity governance
- `bbf82d2` — fix: align skill latest-amendment required read with 1.5.0 descriptor

## Verification (actual runs)

First full run: `RELEASE_FULL FAIL 23/24` — real finding: `SKILL.md → Required References` still began with the Framework 1.3.1 amendment instead of the new latest amendment. Corrected in `bbf82d2`; the earlier candidate evidence was invalidated by that semantic edit.

Rerun on corrected unchanged candidate (`bbf82d2`): **`RELEASE_FULL PASS 23/23`** covering identity, amendment pointer/SKILL alignment, Continuation Contract presence, Resume Block format in skeletons, all 4 registered commands across gov/SKILL/both launchers, Envelope fail-closed boundary, `ENV-*` template support, idempotency/intent rules, Status Continuity dimension, launchers (4,487/4,486 ≤4,500; byte-identical markers; canonical tokens intact), README identity+section, template metadata 23/23 at 1.5.0, scenarios 136–162 exactly once each, reserved slots/slot 91 intact, md/yaml-only scope, prior amendments untouched, `git diff --check` clean, clean worktree.

`commit ≠ push`: push performed only after this evidence per user's standing workflow approval. `INTEGRATION_GATE: NOT_APPLICABLE` — direct merge to `main` per established pattern.
