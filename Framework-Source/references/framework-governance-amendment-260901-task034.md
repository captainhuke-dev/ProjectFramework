# Framework Governance Amendment — TASK-034 Agent / Model Capability Profile

**Framework:** 1.12.0
**Schema:** 1.0.0
**Release format:** 3
**Status:** CURRENT / SET1_INCREMENTAL
**Task:** TASK-034 — Agent / Model Capability Profile

## 1. Purpose

Framework 1.12.0 adds a vendor-neutral Agent / Model Capability Profile under optional `Project-Execution/capabilities.md`. Tool eligibility and capability eligibility remain separate.

```text
Capability ≠ Authority
Capability eligibility ≠ Tool eligibility
Provider availability ≠ Disclosure permission
Model quality/ranking ≠ Project truth
```

## 2. Capability vocabulary

Canonical capability classes:

```text
REASONING | CODING | RESEARCH | REVIEW | COUNCIL
```

Execution-time capability availability:

```text
FULL | DEGRADED | UNAVAILABLE | UNKNOWN
```

These are execution/readiness labels only, not Project Source epistemic states, Task lifecycle, or authority.

## 3. Profile contract

`capabilities.md` defines work classes with `required_capabilities`, `preferred_capabilities`, provider scope, independent review, tool-profile reference, and failure mode.

```text
provider_scope: LOCAL_ONLY | LOCAL_OR_EXTERNAL | EXTERNAL_ALLOWED
independent_review: REQUIRED | OPTIONAL | NOT_REQUIRED
failure_mode: FAIL_CLOSED | DEGRADED_ALLOWED
```

`DEGRADED_ALLOWED` permits only the supported bounded subset; required review, Risk, authority, trust, and disclosure gates remain unchanged. `UNKNOWN` fails closed for materially sensitive requirements.

## 4. Tool, provider, and disclosure composition

A capable agent/model is not executable without an eligible tool path. An allowed tool does not prove the connected model satisfies capability requirements. External providers remain subject to TASK-026 disclosure classification, eligibility, minimization, redaction, secret prohibition, and bounded authorization.

```text
work capability requirements
+ active Tool/MCP Execution Profile
+ provider/disclosure eligibility
+ AUTH/Risk/shared-state gates
```

No component subsumes another.

## 5. Review semantics

`independent_review: REQUIRED` preserves a completion/integration review gate using an eligible reviewer distinct from the primary producing instance where practicable. Reviewer capability, availability, and independence must be observed rather than fabricated. Unavailable reviewer keeps the gate unresolved; it is never silently waived. User waiver, when allowed, is action-specific evidence and does not rewrite the standing profile.

## 6. Meeting and sensitive work

`MEETING_COUNCIL` may require `COUNCIL + REASONING`, but `[Meeting]` remains governed by TASK-024/TASK-026 and remains advisory. Security-sensitive work may require local-only processing, REVIEW, or independent review; these are eligibility constraints, not Risk acceptance or authority.

## 7. GREENFIELD/Brownfield

Capability profile adoption is optional/applicability-driven. GREENFIELD invents no routing policy from model availability. Brownfield does not infer capability requirements from prior provider use/vendor settings.

## 8. Runtime boundary

TASK-034 adds no model router, provider API integration, benchmark runner, automatic delegation, council runtime, or permission engine.
