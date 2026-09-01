# TASK-034 Agent / Model Capability Profile — Design

**Task:** TASK-034 — Agent / Model Capability Profile
**Design state:** USER_APPROVED_SET1_DIRECTION / WRITTEN_SPEC_APPROVED_BY_GOAL
**Set 1 position:** 3 of 5
**Depends on:** TASK-027
**Target Framework:** 1.12.0
**Project Source Schema:** 1.0.0
**Release format:** 3

## 1. Purpose

TASK-027 governs which execution tools/MCPs a Project permits. TASK-034 separately defines what agent/model capability classes are appropriate for categories of work, review, context, and disclosure without binding Project governance to one vendor or model name.

TASK-034 extends the shared optional profile directory:

```text
<Project-Root>/Project-Execution/
├── README.md
├── tools.md
└── capabilities.md
```

Core invariant:

```text
Capability ≠ Authority
Capability eligibility ≠ Tool eligibility
Provider availability ≠ Disclosure permission
Model quality/ranking ≠ Project truth
```

## 2. Capability vocabulary

The vendor-neutral capability classes are:

```text
REASONING
CODING
RESEARCH
REVIEW
COUNCIL
```

A profile MAY combine classes for one work category. The Framework does not define benchmark scores, vendor rankings, model leaderboards, or universal “best model” claims.

## 3. `capabilities.md` contract

A maintained profile uses task/work-category rules such as:

```yaml
profile_name: "default"
profile_state: "ACTIVE | DISABLED"
work_classes:
  - work_class: "IMPLEMENTATION"
    required_capabilities: ["REASONING", "CODING"]
    preferred_capabilities: ["REVIEW"]
    provider_scope: "LOCAL_ONLY | LOCAL_OR_EXTERNAL | EXTERNAL_ALLOWED"
    independent_review: "REQUIRED | OPTIONAL | NOT_REQUIRED"
    tool_profile_ref: "./tools.md"
    failure_mode: "FAIL_CLOSED | DEGRADED_ALLOWED"
review_trigger: "<EVENT_OR_NOT_APPLICABLE>"
```

Canonical work-class names MAY include `PLANNING`, `IMPLEMENTATION`, `RESEARCH`, `REVIEW`, `MEETING_COUNCIL`, and `SECURITY_SENSITIVE`. Projects may add clearly scoped custom work classes without redefining the capability vocabulary.

## 4. Capability availability states

For a concrete candidate agent/model at execution time, capability availability is reported as:

```text
FULL
DEGRADED
UNAVAILABLE
UNKNOWN
```

These are execution/readiness labels only. They are not Project Source epistemic states, Task lifecycle states, or authority states.

`DEGRADED` means the candidate can perform a bounded subset but does not fully satisfy the profile. `failure_mode: DEGRADED_ALLOWED` permits only the work scope that remains genuinely supported; required review and safety/authority gates remain unchanged. `UNKNOWN` fails closed for materially sensitive capability requirements.

## 5. Local versus external providers

`provider_scope` constrains where capability may be sourced:

- `LOCAL_ONLY` — external provider use is not eligible for this work class;
- `LOCAL_OR_EXTERNAL` — either is eligible if all other requirements are met;
- `EXTERNAL_ALLOWED` — external is allowed but not required.

Any external-model processing of Project context still follows TASK-026 disclosure classification, provider eligibility, minimization, redaction, secret prohibition, and bounded authorization. The capability profile never grants disclosure authority.

## 6. Tool-profile integration

A capable model is not executable if no eligible tool path exists for the required operation. Conversely, an allowed tool does not imply the connected agent/model satisfies required capability classes.

Resolution therefore composes:

```text
work-class capability requirements
+ active Tool/MCP Execution Profile
+ provider/disclosure eligibility
+ action-specific AUTH/Risk/shared-state gates
```

No component subsumes another.

## 7. Review semantics

`independent_review: REQUIRED` means materially accepting the work requires an independent review step using an eligible reviewer distinct from the primary producing instance where practicable. The profile does not fabricate reviewer capability, availability, or independence. If a required reviewer is unavailable, report the condition and preserve the applicable completion/integration gate rather than silently waiving it.

The user may explicitly waive a review requirement for a bounded action when existing governance permits; such waiver is action-specific evidence and does not rewrite the standing capability profile unless separately approved.

## 8. `[Meeting]` integration

`MEETING_COUNCIL` may require `COUNCIL` plus `REASONING`, but `[Meeting]` remains governed by TASK-024 and TASK-026. A council provider's ability to answer does not create authority, disclose extra Project context, or qualify it for unrelated implementation/review work automatically.

## 9. Sensitive/high-risk work

Projects may define stricter work classes such as `SECURITY_SENSITIVE` requiring `REASONING + REVIEW`, local-only processing, or independent review. These declarations are eligibility constraints, not a substitute for Risk acceptance, Decision authority, Tool policy, secrets handling, or trust-boundary rules.

TASK-037 later consumes these capability constraints when defining trust-boundary crossings.

## 10. GREENFIELD/Brownfield

The profile is optional/applicability-driven. GREENFIELD creates no model routing policy merely because models are available. Brownfield adoption never infers capability requirements from prior model use or vendor settings. Unknown provider/capability assumptions remain explicit until assessed.

## 11. Affected surfaces and verification

Implementation adds maintained `Framework-Source/templates/project-execution/capabilities.md` and updates current release/amendment/Core/SKILL/README/migration/templates/task/tests. No model router, provider API integration, benchmark runner, automatic delegation, council runtime, or permission engine is introduced.

Pressure/AFFECTED verification must prove capability/authority/tool/disclosure separation, local/external provider rules, FULL/DEGRADED/UNAVAILABLE/UNKNOWN behavior, independent-review semantics, Meeting boundary, unavailable reviewer behavior, Brownfield safety, and no runtime routing/provider implementation.
