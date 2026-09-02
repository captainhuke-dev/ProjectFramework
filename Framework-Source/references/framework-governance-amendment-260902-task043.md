# Framework Governance Amendment — TASK-043 Registered Command Strict-Interface & Contract Completeness Hardening

**Framework:** 1.12.2
**Schema:** 1.0.0
**Release Format:** 3
**Task:** TASK-043 — Registered Command Strict-Interface & Contract Completeness Hardening
**Scope:** Documentation/governance semantic hardening only

## 1. Purpose

Framework 1.12.2 closes the remaining execution gap between a Registered Command's defined semantics and an Agent's final command response. A response may contain true or useful facts and still be noncompliant when it replaces the governed command interface with an equivalent narrative, omits/reorders required dimensions, renames canonical tokens, hides unavailable evidence by dropping a field, or substitutes stale memory for required fresh observation.

TASK-043 does not change Registered Command identity, add a command, or replace TASK-042 final-response hardening. It makes command-body protocol compliance explicit and repairs verified current Core/SKILL drift for `[Project Status]` `Continuity`.

## 2. Registered Command Strict Governed Interface

A recognized Registered Command is a **Strict Governed Interface**, not merely a natural-language request for equivalent information. Once command identity is resolved, the Agent MUST execute the active local command contract.

When the active command contract governs an element, the Agent MUST preserve:

- Registered Command identity;
- required dimensions/sections;
- governed dimension/section order;
- canonical status/report tokens and vocabulary;
- command-specific freshness requirements;
- explicit unavailable-evidence representation;
- command-specific authority/mutation boundaries; and
- composition with the mandatory Framework response-close contract.

Semantic equivalence alone is insufficient. The Agent MUST NOT replace the governed interface with an equivalent narrative, renamed/reordered dashboard, omitted required dimension, unsupported inference, or stale-memory reconstruction unless the active command contract explicitly permits that variation.

Missing evidence changes the represented value; it does not remove a governed field. Use `UNKNOWN`, `VERIFICATION_REQUIRED`, or another command-specific fail-closed state as applicable.

## 3. Flexible Presentation Boundary

Strict interface does not require deterministic wording. Unless the active command contract says otherwise, the Agent MAY adapt explanatory prose, language, sentence length, concise rationale, optional notes, and table/key-value presentation when those choices do not displace or weaken governed structure.

When uncertain whether an element is structural or stylistic, preserve the canonical command structure.

## 4. Command Contract Completeness Gate

Every recognized Registered Command MUST pass a lightweight **Command Contract Completeness Gate** on the command-body representation before the existing TASK-042 global Response Close Completeness Gate.

Minimum checks are:

```text
Registered command identity resolved?                       YES
Active local command contract resolved?                     YES
Required dimensions/sections present?                       YES
Governed order preserved?                                   YES
Freshness satisfied or unavailable evidence explicit?       YES
Canonical tokens/vocabulary preserved?                      YES
Unsupported inference/stale-memory substitution absent?     YES
Command-specific authority boundaries preserved?            YES
```

If a required check fails, correct the command body before final emit. If the active local command contract cannot be resolved safely, do not silently downgrade the invocation into an ordinary summary and do not reconstruct missing rules from memory. Preserve the command structure that active authority supports and represent unresolved elements with the applicable fail-closed state.

The ordered finalization path for a recognized Registered Command is:

```text
Recognize
→ Resolve Contract
→ Fresh Observe
→ Materialize Governed Structure
→ Populate
→ Command Contract Completeness Gate → Response Close Completeness Gate → Emit
```

The command gate validates command body/interface compliance. TASK-042's Response Close Completeness Gate remains the final global pre-emit validation for the mandatory two-heading/four-field response close.

## 5. `[Project Status]` Current-Surface Alignment

Framework 1.12.2 preserves the already-current Core Governance `[Project Status]` dimension contract and aligns current maintained SKILL/root-template summaries to it:

```text
Identity → Health → Remain Tasks → Git Sync → Working Tree → Verification → Blockers → Continuity
```

`Continuity` keeps its existing semantics: Resume Block freshness, active Envelope validity when applicable, and repeated-break indication. TASK-043 changes no Continuity vocabulary or lifecycle family.

Unavailable evidence remains explicit `UNKNOWN` / `VERIFICATION_REQUIRED`; it does not authorize omission of an applicable dimension.

## 6. TASK-042 Composition

TASK-042 remains fully binding. TASK-043 adds a command-specific body gate before TASK-042's global final-response gate; it does not alter TASK-042 bootstrap timing, exceptional-path coverage, mandatory close labels, lifecycle coupling, or no-early-return invariant.

```text
Recognized Registered Command response
→ Command Contract Completeness Gate
→ Response Close Completeness Gate
→ Emit
```

A perfect mandatory response close cannot make an incomplete Registered Command body compliant, and a command-complete body still must pass the global response-close gate.

## 7. Brownfield / Upgrade Behavior

Existing initialized Projects remain governed by their locally pinned Framework. Upstream 1.12.2 does not silently rewrite older command contracts.

Governed `[Project Upgrade]` adoption preserves local `FRAMEWORK-001`, Stable IDs, Project-specific rules, bindings, history, authority, and existing Direct-to-Latest controls. Current command summaries may be aligned as part of the approved target migration; historical amendments/specs/plans/evidence remain historical provenance.

## 8. No Runtime Expansion

This amendment adds no parser service, executable response schema, validator/CLI, interceptor, middleware, hook, bot, CI/CD, scheduler, watcher, daemon, tool implementation, vendor UI automation, or other runtime enforcement. It creates no new semantic slot, Stable-ID family, lifecycle state, authority family, Epistemic Status, health state, Git freshness state, or Registered Command.

## 9. Verification Contract

Framework 1.12.2 release acceptance must prove:

- scenarios `351–356` cover correct-information/wrong-protocol, narrative replacement, missing fresh evidence, style conflict, gate ordering, and Core/SKILL alignment;
- cumulative scenario numbering remains contiguous and unique;
- Core and SKILL state the Strict Governed Interface and Command Contract Completeness Gate semantics;
- Core and SKILL align `[Project Status]` through `Continuity`;
- Command Contract Completeness Gate precedes TASK-042 Response Close Completeness Gate in the recognized-command execution path;
- TASK-042 semantics remain present and unchanged in meaning;
- the Registered Command registry does not grow;
- current maintained Framework release/starter surfaces are aligned to `1.12.2` where release identity is carried;
- ProjectFramework's own local Project Source pin remains `1.7.0` / Schema `1.0.0`;
- no runtime/validator/parser implementation is introduced;
- affected verification passes; and
- exactly one final `RELEASE_FULL` passes on the unchanged release candidate before release evidence is committed.

## 10. Authority Boundary

Stricter command protocol compliance grants no mutation, push/publication, destructive-operation, Root/Binding, runtime, secret-value, or external-disclosure authority. Existing system/developer/tool/safety/authentication controls and Framework authority/risk rules remain independently binding.
