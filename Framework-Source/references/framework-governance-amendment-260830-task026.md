---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.8.0"
project_source_framework_version: "1.8.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_APPROVED_WRITTEN_SPEC_2026-08-30"
compatibility: "BACKWARD_COMPATIBLE_EXTERNAL_AI_DISCLOSURE_GOVERNANCE"
---

# Framework 1.8.0 Amendment — External AI Context & Disclosure Governance

Framework `1.8.0` preserves TASK-038 `Framework-Source/` naming, TASK-039 persistent `[Goal]`, TASK-024 `[Meeting]`, and all prior Framework rules unless refined here. Project Source Schema remains `1.0.0`; release format remains `3`.

TASK-026 defines one canonical **Compositional Disclosure Boundary** for Project context sent to external AI/model/provider/tool consumers. It adds no `DISC-*` Stable-ID family, semantic slot, authorization family, mandatory per-object metadata field, runtime gateway, redactor, router, DLP engine, or secret store.

Core invariants:

```text
Classification ≠ Authorization
Provider Eligibility ≠ Authority
Disclosure Permission ≠ Decision Authority ≠ Mutation Authority ≠ Binding Authority ≠ Runtime Authority
Secret Reference ≠ Secret Value Disclosure Permission
Unknown ≠ Safe
```

## 1. Canonical disclosure classes

Every outbound Project-context portion resolves, when material, to one of:

```text
EXTERNAL_OK
EXTERNAL_REVIEW
DO_NOT_DISCLOSE
UNCLASSIFIED
```

- `EXTERNAL_OK` — eligible for an eligible provider/tool when purpose, minimum-context, redaction/minimization, and applicable authorization requirements pass. This class is **not itself authorization** to execute an external call.
- `EXTERNAL_REVIEW` — requires current explicit disclosure authority bounded to provider/tool, purpose, and content/source scope.
- `DO_NOT_DISCLOSE` — ordinary ProjectFramework external-AI workflows must not transmit the content. Goal, Envelope, tool capability, provider availability, or local access never silently overrides it.
- `UNCLASSIFIED` — eligibility is unresolved. Automatic outbound disclosure of protected Project content fails closed; safe local reasoning/work may continue.

Use-time defaults are conservative:

1. actual secret values are effectively `DO_NOT_DISCLOSE` under ordinary external-AI workflows;
2. `SECRET-*` metadata/reference is not permission to reveal the underlying value;
3. text the user explicitly supplies as the exact payload of an external-AI invocation is authorized as that action-specific input only when not otherwise prohibited and higher-level controls permit it;
4. additional Project content not explicitly supplied for that invocation remains `UNCLASSIFIED` unless current governance resolves another class;
5. public/upstream content may be `EXTERNAL_OK` only when its public nature is actually established;
6. derived summaries inherit the strictest relevant source constraint unless the approved transformation demonstrably removes protected content sufficiently.

Brownfield adoption performs no blanket historical classification.

## 2. Authorization composition

Disclosure authorization reuses existing `AUTH-*` semantics in `12 Authorization Registry`. A standing external-AI disclosure `AUTH-*`, when materialized, resolves at minimum:

```text
Grantor
Grantee / consumer
Provider / tool / provider class
Allowed content/source scope
Allowed disclosure class(es)
Purpose / permitted use
Minimum-context / redaction conditions
Forbidden content / effects
Start
Expiry / termination / revocation
Risk ceiling when applicable
Evidence / approval reference
Status
```

A standing authorization is provider-, purpose-, class-, and content/source-scoped. It never generalizes across Projects, providers, purposes, sensitivity classes, or validity windows without authority that actually covers the expanded scope.

An exact User Explicit Instruction may authorize **one** disclosure action when the provider/tool is sufficiently identified or uniquely resolvable, the content/payload scope is bounded, the purpose is clear enough for fail-closed evaluation, and all other rules pass. One-off authority does not silently create standing `AUTH-*`.

## 3. Provider/tool eligibility

Provider/tool eligibility is independent of both classification and Project authority. Presentation/workflow labels are exactly:

```text
ELIGIBLE
LIMITED
INELIGIBLE
VERIFICATION_REQUIRED
```

- `ELIGIBLE` — the provider/tool may receive the relevant allowed class/scope under valid disclosure authority.
- `LIMITED` — only specifically bounded classes/scopes/purposes are eligible.
- `INELIGIBLE` — the provider/tool must not receive the affected Project context.
- `VERIFICATION_REQUIRED` — material identity/policy/tenant/capability evidence is unresolved; protected outbound context fails closed.

Eligibility may depend on provider/tool identity, account/tenant boundary, retention/training policy when material, deployment locality, authentication state, organizational policy, or other governed evidence.

Provider availability never implies eligibility. Provider/model capability never grants disclosure authority. Provider eligibility never grants Decision, Risk, mutation, publication, binding, runtime, or other Project authority.

## 4. Outbound context decision flow

Every external-AI consumer follows one semantic flow:

```text
consumer requests external AI context
→ identify exact purpose + provider/tool
→ identify candidate source/context
→ classify each portion
→ remove secret values + DO_NOT_DISCLOSE material
→ minimize to the smallest useful subset
→ redact/generalize where allowed and sufficient
→ resolve provider/tool eligibility
→ resolve standing AUTH-* or exact action-specific disclosure basis
→ evaluate mixed-sensitivity portions independently
→ send only the authorized + eligible subset
→ surface blocked/omitted portions when material
→ persist EVD-* only when disclosure/result is governance-relevant
```

A consumer never bypasses this boundary merely because it can read Project Source, repository/workspace files, chat history, Project Knowledge, an index, or another Project through relation traversal.

## 5. Minimum necessary context

Preferred order from least to most expansive:

```text
1. user-supplied invocation text
2. concise factual extracts
3. bounded summaries with source references
4. selected document sections
5. whole documents only when genuinely necessary + fully authorized
6. whole Project/repository export only under exact exceptional authority + no prohibition
```

Convenient access to a repository, workspace, archive, index, graph, or chat history is never evidence that all of it is necessary.

## 6. Redaction, transformation, and mixed sensitivity

A transformation is acceptable only when protected content is actually removed/generalized sufficiently for the resulting payload, the result remains useful/truth-preserving for the declared purpose, provenance can remain bounded without reproducing restricted payload, and the transformation does not leak through metadata, examples, filenames, hashes, quoted fragments, hidden prompts, logs, attachments, or other channels.

If redaction adequacy is materially uncertain, the affected portion remains blocked.

Mixed-sensitivity context is **partitioned**, not promoted by the least restrictive portion and not globally blocked by one restricted portion when independent safe content remains useful.

Example:

```text
EXTERNAL_OK paragraph
+ EXTERNAL_REVIEW architecture detail
+ DO_NOT_DISCLOSE secret value
+ UNCLASSIFIED operational note
```

Evaluate each portion independently. Send only the authorized + eligible subset when the result remains useful and not misleading. If omission makes the outbound task materially misleading/unusable, fail closed rather than silently expanding disclosure scope.

## 7. Secret boundary

`17 Secret Reference Registry` remains the canonical home of `SECRET-*` metadata only. TASK-026 creates no secret storage.

Actual secret values must never be persisted in Project Source, Handoff, Evidence, plans, disclosure logs, prompts, exports, or provider context merely because a runtime can access them. A `SECRET-*` identifier may be disclosed only as metadata when otherwise allowed/useful; it does not grant access to or disclosure of the underlying value.

Environment variables, tokens, API keys, cookies, private keys, recovery codes, passwords, and equivalent credential values must be excluded or sufficiently redacted from external-AI context.

## 8. Material evidence and provenance

Exploratory low-materiality calls need no synthetic permanent record merely because an external model was used.

When disclosure materially informs Project truth, a Decision, Requirement, Risk, architecture, audit claim, or other governed evidence, persist minimum reconstructable `EVD-*` / source-native evidence. Material disclosure evidence may resolve:

```text
Evidence Type: EXTERNAL_AI_DISCLOSURE / ADVISORY_CONTEXT
Captured At / Captured By
Consumer / workflow
Purpose
Provider / tool identity
Provider eligibility state/evidence
Source pointers / bounded context scope
Disclosure class(es)
Authorization basis: AUTH-* or exact action-specific instruction reference
Minimization / redaction performed
Blocked/omitted portions when material
Result/artifact pointer
Epistemic Status
```

Never persist the complete sensitive payload merely to prove it was disclosed. Evidence must not become a duplicate leak channel.

## 9. Consumer integration

### `[Meeting]`

The explicit user-supplied Meeting question remains the default action-specific input. Additional Project context must pass TASK-026 classification, minimum-context, provider eligibility, and authorization rules. A verified/available llm-council provider does not grant disclosure authority. Council output remains advisory after disclosure succeeds.

### Project Knowledge

Local advisory/non-authoritative Project Knowledge is not automatically externally disclosable. Every external-model processing request enters this boundary independently of Knowledge authority status.

### Project Graph / OpenViking

OpenViking remains `DERIVED_ONLY`. Relation/index visibility never grants outbound disclosure authority. Cross-Project content is evaluated under each source Project's authority; Project A cannot grant disclosure authority over Project B merely because a `REL-*` edge exists.

### `[Goal]`, `ENV-*`, Tool/MCP, model capability

```text
Goal AUTH-* ≠ external disclosure AUTH-*
ENV-* ≠ external disclosure permission
Tool/MCP access ≠ disclosure permission
Model capability ≠ disclosure permission
Repository/workspace access ≠ disclosure permission
Provider availability ≠ provider eligibility
```

A Goal may explicitly include a bounded disclosure grant only when exact provider/content/purpose scope is sufficiently defined and represented consistently with this contract. Generic local-development Goal authority never implies outbound disclosure.

## 10. Fail-closed behavior

Block the affected outbound disclosure when any material prerequisite is unresolved, including:

- protected Project content is `UNCLASSIFIED`;
- provider/tool is `INELIGIBLE` or material eligibility is `VERIFICATION_REQUIRED`;
- standing/action-specific disclosure authority is absent, expired, ambiguous, or scope-mismatched;
- provider identity materially differs from the authorization/evidence basis;
- mixed-sensitivity partition cannot be performed safely;
- redaction adequacy is uncertain;
- secret-value leakage cannot be excluded;
- required provider policy/freshness evidence is unavailable;
- requested scope materially exceeds minimum necessary context.

Failing closed for outbound disclosure does not automatically block independent safe local work.

## 11. GREENFIELD and Brownfield

Framework `1.8.0` GREENFIELD starters expose disclosure semantics but do not automatically create:

```text
standing disclosure AUTH-*
provider eligibility grants
provider credentials/accounts
provider routing
redaction runtime
external disclosure logs
blanket EXTERNAL_OK classifications
```

New Project content remains unresolved for external use unless current rules/source-specific evidence resolve it otherwise.

Brownfield upgrade preserves current Project truth, authorization records, secret references, external-AI evidence, and provider configuration. It must not mass-classify historical content as `EXTERNAL_OK`, synthesize standing disclosure `AUTH-*` from prior AI use/Meeting/Goal/chats/credentials, migrate actual secret values into Project Source/Evidence, or treat prior provider integration as automatically eligible. Existing external-AI usage may be assessed prospectively when next used; governance adoption does not require runtime/provider installation.

## 12. Runtime, schema, and compatibility boundary

TASK-026 is documentation/governance-only. It does not implement:

```text
runtime redaction engine
provider router/proxy
MCP disclosure gateway
AI-call interception layer
secret manager
DLP scanner
classification database
background crawler/watcher
automatic outbound calls
automatic credential provisioning
CI/CD/deployment automation
```

This is a backward-compatible Framework `1.8.0` semantic expansion. Schema remains `1.0.0`; release format remains `3`; no semantic slot, Stable-ID family, mandatory per-object classification field, or runtime enforcement mechanism is added.

If implementation proves that durable per-object classification requires an incompatible schema field or new canonical family/slot, stop and reclassify rather than forcing Schema `1.0.0`.
