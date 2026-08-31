# TASK-026 External AI Context & Disclosure Governance — Design

Date: `2026-08-30` (Asia/Bangkok)
Task: `TASK-026`
Design state: `USER_APPROVED_DESIGN / WRITTEN_SPEC_APPROVED`
Approval basis: the Compositional Disclosure Boundary architecture was presented after TASK-024 completion and approved for continuous execution; after the written spec was materialized, self-reviewed, committed, and persisted, the user again explicitly instructed continued execution on `2026-08-30`, approving the written spec and releasing the implementation-planning gate. Higher-level system/tool/platform gates remain binding.
Target release: Framework `1.8.0` / Schema `1.0.0` / release format `3`

## 1. Purpose

ProjectFramework needs one canonical outbound AI context/disclosure contract for `[Meeting]`, Project Knowledge, OpenViking/cross-Project indexing, and future external-model consumers.

The contract must answer three different questions without collapsing them:

```text
What information is this?          = disclosure classification
May this actor/tool/provider send it? = authorization / provider eligibility
What evidence proves what happened?  = EVD-* / source-native evidence
```

The central invariant is:

```text
Disclosure Permission ≠ Decision Authority ≠ Mutation Authority ≠ Binding Authority ≠ Runtime Authority
```

A consumer may be authorized to disclose a bounded context payload without gaining authority to change requirements, decisions, bindings, code, runtime state, publication state, or Project truth.

## 2. Chosen architecture: Compositional Disclosure Boundary

Three approaches were considered:

1. **New `DISC-*` registry/family** — rejected because it would create a parallel authoritative family and likely require unnecessary schema/slot expansion.
2. **Put classification and permission together in `AUTH-*`** — rejected because information sensitivity/eligibility and authorization are different semantic dimensions. Classification can remain true after an authorization expires; authorization can vary by provider/purpose without changing the data itself.
3. **Compositional Disclosure Boundary** — selected. Disclosure semantics compose existing homes instead of creating a new Stable-ID family or semantic slot.

Canonical composition:

```text
Disclosure classification semantics = Framework contract attached to source/context at use time or by existing governed metadata where available
AUTH-* in 12                       = durable disclosure permission when standing authority is required
exact user instruction             = action-specific disclosure basis when sufficiently precise and otherwise allowed
SECRET-* in 17                     = secret metadata/reference only; actual secret values remain forbidden
EVD-* in 13                        = material evidence of disclosure decision/execution when needed
consumer-specific command/workflow = requests context through this boundary; never owns disclosure authority
```

TASK-026 adds no `DISC-*` Stable-ID family and no semantic slot.

## 3. Disclosure classification vocabulary

Canonical disclosure classes are:

```text
EXTERNAL_OK
EXTERNAL_REVIEW
DO_NOT_DISCLOSE
UNCLASSIFIED
```

### `EXTERNAL_OK`

The information may be sent to an eligible external provider when all other constraints pass: purpose is legitimate/in-scope, provider/tool eligibility is resolved, minimum-necessary context is used, redaction/minimization rules are satisfied, and no more restrictive object-specific rule applies.

`EXTERNAL_OK` does not itself grant authorization to execute an external call. It means the information is eligible for such disclosure under otherwise-valid authority.

### `EXTERNAL_REVIEW`

External disclosure requires current explicit disclosure authority for the provider/tool, purpose, and content scope. Standing `AUTH-*` or an exact action-specific User Explicit Instruction may supply the basis when otherwise compliant.

A generic instruction such as “continue the project” or a generic Goal authority does not satisfy this class.

### `DO_NOT_DISCLOSE`

The information must not be sent to an external AI/provider under ordinary ProjectFramework workflows. A command, Goal, Session Envelope, tool capability, repository access, model capability, or provider availability never silently overrides this classification.

A future design may define exceptional governance for legally/organizationally approved declassification or substitution, but TASK-026 does not introduce such an override mechanism.

### `UNCLASSIFIED`

Disclosure eligibility is unresolved. Automatic outbound disclosure fails closed. Read/local reasoning may continue when safe. The classification may later resolve from canonical rules, source-specific metadata, explicit user classification, or another governed authority source.

`UNCLASSIFIED` is not equivalent to `EXTERNAL_OK` and must never be treated as “probably safe”.

## 4. Default classification rules

TASK-026 must avoid pretending every historical Project artifact already carries a classification field.

Default rules are therefore conservative and use-time driven:

1. Actual secret values are effectively `DO_NOT_DISCLOSE` for external AI workflows under this Framework contract.
2. A `SECRET-*` reference/identifier is not the secret value and is not permission to reveal the value it references.
3. Text the user explicitly supplies as the exact payload of an external-AI invocation is authorized as that action-specific input only, subject to higher-level safety/tool/platform constraints and any explicit prohibition.
4. Additional Project content not explicitly supplied for the invocation is `UNCLASSIFIED` unless current governance resolves another class.
5. Existing public/upstream Framework text may be `EXTERNAL_OK` when its public nature is actually established and no Project-specific restriction applies; public-looking content must not be guessed public from memory.
6. Derived summaries inherit the strictest relevant source constraint unless the transformation demonstrably removes protected content under the approved minimization/redaction rule.

No Brownfield migration mass-labels historical files as safe.

## 5. Authorization model

Disclosure authorization remains in existing Authority semantics.

A standing external-AI disclosure `AUTH-*`, when materialized, resolves at minimum:

```text
Grantor
Grantee / consuming actor or workflow
Provider / tool / provider class
Allowed content scope or source scope
Allowed disclosure class(es)
Purpose / permitted use
Minimum-context / redaction conditions
Forbidden content/effects
Start
Expiry / termination / revocation
Risk ceiling where applicable
Evidence / approval reference
Status
```

A disclosure authorization is bounded by both its content scope and provider/purpose scope. It must not be generalized from one provider to another, one Project to another, one purpose to another, or one sensitivity class to another.

An exact User Explicit Instruction can authorize one disclosure action when it identifies the intended provider/tool or otherwise uniquely resolves it, the content/payload scope, and the purpose sufficiently for a fail-closed decision. That action-specific instruction does not automatically create standing `AUTH-*`.

## 6. Provider and tool eligibility

Provider/tool eligibility is independent of data classification.

A provider profile may be eligible for `EXTERNAL_OK` but not `EXTERNAL_REVIEW`; another may be entirely unresolved. Eligibility may depend on provider identity, tool identity, account/tenant boundary, retention/training policy when known and material, deployment locality, authentication state, organizational policy, or other governed evidence.

Provider/tool eligibility uses these presentation states:

```text
ELIGIBLE
LIMITED
INELIGIBLE
VERIFICATION_REQUIRED
```

These are disclosure-workflow labels only, not new Project lifecycle or authority families.

Rules:

- `ELIGIBLE` — provider/tool may receive the relevant allowed class/scope under valid authority.
- `LIMITED` — only the stated bounded classes/scopes/purposes are eligible.
- `INELIGIBLE` — the provider/tool must not receive the affected Project context.
- `VERIFICATION_REQUIRED` — provider identity/policy/capability is unresolved; protected outbound disclosure fails closed.

Provider availability never implies eligibility. Provider eligibility never grants mutation/Decision authority.

## 7. Outbound context decision flow

Every external-model consumer uses one semantic flow:

```text
consumer requests external AI context
→ identify exact purpose and target provider/tool
→ identify candidate source/context
→ classify each context portion
→ remove secret values and forbidden material
→ minimize to the smallest useful subset
→ redact/generalize where allowed and useful
→ resolve provider/tool eligibility
→ resolve standing AUTH-* or exact action-specific disclosure basis
→ evaluate mixed-sensitivity portions independently
→ send only the authorized + eligible subset
→ surface omitted/blocked portions when material
→ record EVD-* only when disclosure/result is materially governance-relevant
```

Consumers do not bypass the boundary by reading unrestricted Project Source and sending it directly.

## 8. Minimum-necessary context

Minimum necessary means the smallest bounded information set that materially supports the declared external-AI purpose.

Preferred order:

1. user-supplied invocation text;
2. concise factual extracts;
3. bounded summaries with source references;
4. selected document sections;
5. whole documents only when genuinely necessary and fully authorized;
6. whole Project/repository export only under exact exceptional authority and no applicable prohibition.

The convenient availability of a full repository, workspace, index, archive, or chat history is never evidence that all of it is necessary.

## 9. Redaction and transformation semantics

Redaction/minimization may remove or generalize data before disclosure, but transformation must not be used to falsely claim sensitive content is safe.

A transformation is acceptable only when:

- the protected content is actually removed or generalized sufficiently for the resulting payload;
- the output remains useful for the declared purpose;
- provenance can still identify the source class without reproducing restricted payload;
- the process does not leak the restricted value through metadata, examples, filenames, hashes, quoted fragments, hidden prompts, logs, or attachments.

If redaction adequacy is uncertain for materially sensitive content, that portion remains blocked.

## 10. Mixed-sensitivity context

Mixed context is handled by partitioning, not by weakest-link promotion.

Example:

```text
EXTERNAL_OK paragraph
+ EXTERNAL_REVIEW architecture detail
+ DO_NOT_DISCLOSE secret value
+ UNCLASSIFIED operational note
```

The system evaluates each portion independently. It may send only the allowed subset if that subset remains useful and truth-preserving. The presence of one restricted portion does not force unrelated safe local work to stop; conversely, the presence of one safe portion does not make the whole payload safe.

If the omitted context makes the outbound task misleading or unusable, the external call fails closed with an explicit limitation rather than silently sending more.

## 11. Secret boundary

`17 Secret Reference Registry` remains the canonical home of `SECRET-*` metadata only. TASK-026 does not create secret storage.

Rules:

- actual secret values are never persisted in Project Source, Handoff, evidence, plans, disclosure logs, prompts, or exports;
- a `SECRET-*` reference may be disclosed only as metadata when otherwise allowed and useful;
- a secret reference does not grant access to or disclosure of the underlying value;
- environment variables, credential stores, tokens, cookies, API keys, private keys, recovery codes, passwords, and equivalent values must not be copied into external AI context merely because the runtime can access them;
- secret-bearing source text must be redacted or excluded before outbound disclosure.

## 12. Evidence and provenance

Not every external AI call requires a permanent disclosure record. Exploratory low-materiality calls may remain transient when no Project truth relies on them and no policy requires persistence.

When disclosure materially informs Project truth, a Decision, Requirement, Risk, architecture, evidence claim, or later audit, persist the minimum reconstructable evidence as `EVD-*` or a source-native evidence pointer.

Material disclosure evidence may resolve:

```text
Evidence Type: EXTERNAL_AI_DISCLOSURE / ADVISORY_CONTEXT
Captured At
Captured By
Consumer / workflow
Purpose
Provider / tool identity
Provider eligibility state/evidence
Source pointers / bounded context scope
Disclosure class(es)
Authorization basis (`AUTH-*` or exact action-specific instruction reference)
Minimization / redaction performed
Blocked/omitted classes or portions when material
Result/artifact pointer
Epistemic Status
```

Do not persist the full sensitive payload merely to prove it was disclosed. Evidence should prove the governed decision boundary without becoming a duplicate leak channel.

## 13. Relationship to `[Meeting]`

TASK-024 `[Meeting]` becomes the first concrete consumer of TASK-026.

The explicit Meeting question remains the default action-specific input. Any additional Project context requested by `[Meeting]` must go through TASK-026 classification, minimization, provider eligibility, and authorization rules.

The llm-council provider profile being available or verified does not grant disclosure authority. Goal/ENV/Meeting invocation does not make unrelated Project Source externally eligible.

Council output remains advisory after disclosure succeeds; disclosure permission never promotes council output into Project authority.

## 14. Relationship to Project Knowledge

TASK-025 Project Knowledge, once designed/implemented, must distinguish local knowledge maintenance from external-model processing.

Local knowledge content does not become externally disclosable merely because it is advisory/non-authoritative. Each external use still enters this disclosure boundary.

Knowledge pages may carry or derive disclosure hints in a future compatible design, but TASK-026 does not create a separate Knowledge authority system or pre-authorize external processing of all Project Knowledge.

## 15. Relationship to OpenViking / Project Graph

OpenViking is `DERIVED_ONLY` cross-Project indexing under AI-ControlTower scope, not Project authority. Derived/index role does not imply export permission.

Before Project content is sent to an external index/model service, the source Project's disclosure classification, minimization, provider eligibility, and authorization rules still apply.

Cross-Project context must be evaluated per authoritative source Project. One Project cannot grant disclosure authority for another Project merely because a graph relation exists.

## 16. Relationship to `[Goal]`, `ENV-*`, Tool/MCP and model capability

Execution authority and disclosure authority remain separate:

```text
Goal AUTH-* ≠ external disclosure AUTH-*
ENV-* ≠ external disclosure permission
Tool access ≠ disclosure permission
Model capability ≠ disclosure permission
Repository/workspace access ≠ disclosure permission
Provider availability ≠ provider eligibility
```

A Goal may explicitly include a bounded disclosure grant only when the exact content/provider/purpose scope is sufficiently defined and the authorization is represented consistently with this contract. Generic local-development Goal authority never implies outbound disclosure.

TASK-027 Tool/MCP Execution Profile and TASK-034 Agent/Model Capability Profile may constrain which tools/models can participate, but neither may expand disclosure scope beyond TASK-026.

## 17. Fail-closed behavior

The affected outbound disclosure is blocked when any material prerequisite is unresolved, including:

- source classification is `UNCLASSIFIED` for protected Project content;
- provider/tool eligibility is `VERIFICATION_REQUIRED` or `INELIGIBLE`;
- required standing/action-specific authority is absent or ambiguous;
- mixed-sensitivity partition cannot be made safely;
- redaction adequacy is uncertain;
- secret-value leakage cannot be excluded;
- provider identity materially differs from the authorization/evidence basis;
- provider policy/freshness is required by governance but unavailable;
- requested scope materially exceeds minimum necessary context.

Failing closed for outbound disclosure does not automatically block independent safe local work.

## 18. GREENFIELD behavior

Framework `1.8.0` GREENFIELD starters expose disclosure semantics but do not automatically create:

```text
standing disclosure AUTH-*
provider eligibility grants
external-AI accounts/credentials
provider routing
redaction runtime
external disclosure logs
blanket EXTERNAL_OK classifications
```

New Project content remains unclassified for external use unless current Framework/source-specific rules resolve it otherwise.

## 19. Brownfield behavior

Brownfield upgrade preserves existing Project truth, authorization records, secret references, external-AI evidence, and provider configuration.

Upgrade must not:

- reinterpret old content as `EXTERNAL_OK` merely because the new vocabulary exists;
- synthesize standing disclosure `AUTH-*` from historical AI use, chat transcripts, Meeting activity, provider credentials, or “continue” wording;
- migrate actual secret values into `17` or Evidence;
- assume existing provider integrations are eligible under the new contract without current evidence;
- require runtime/provider installation simply to adopt governance semantics.

Existing external-AI usage may be assessed prospectively when next used; no mandatory mass reclassification is required for Framework adoption.

## 20. Framework surfaces affected by implementation

If the written spec is approved, implementation is expected to affect only documentation/governance surfaces required for the disclosure contract, including as applicable:

- `Framework-Source/FRAMEWORK-RELEASE.yaml`
- a TASK-026 Framework `1.8.0` amendment
- `Framework-Source/references/core-governance-rules.md`
- `Framework-Source/SKILL.md`
- `Framework-Source/templates/00-project-source-framework.md`
- `Framework-Source/templates/core-document-skeletons.md`
- `Framework-Source/templates/project-source-mockup/12-Authorization-Registry.template.md`
- `Framework-Source/templates/project-source-mockup/13-Evidence-Registry.template.md`
- `Framework-Source/templates/project-source-mockup/17-Secret-Reference-Registry.template.md`
- `Framework-Source/templates/project-source-mockup/README.md`
- `README.md`
- `Framework-Source/MIGRATION-NOTES.md`
- ChatGPT/Claude launchers only if the contract can be represented while retaining shared-body parity and the current `<=4,500` character ceiling
- `Framework-Source/tests/pressure-scenarios.md`
- Task/design/plan/evidence records

TASK-026 implementation does **not** include unless separately approved:

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

## 21. Release classification

TASK-026 is designed as a backward-compatible Framework `1.8.0` governance expansion with Project Source Schema `1.0.0` and release format `3`.

Rationale:

- no semantic slot is added;
- no Stable-ID family is added;
- existing `AUTH-*`, `EVD-*`, and `SECRET-*` homes are reused;
- disclosure classes and provider eligibility are semantic workflow vocabulary rather than mandatory new frontmatter fields;
- runtime enforcement remains out of scope.

If implementation proves that durable per-object classification requires an incompatible schema field or new canonical family/slot, stop and reclassify rather than silently forcing Schema `1.0.0`.

## 22. Verification strategy

Affected verification must prove at minimum:

1. Canonical disclosure classes are exactly `EXTERNAL_OK | EXTERNAL_REVIEW | DO_NOT_DISCLOSE | UNCLASSIFIED`.
2. `UNCLASSIFIED` fails closed for automatic protected outbound Project context.
3. Actual secret values remain prohibited and `SECRET-*` references are not disclosure permission.
4. Classification is separate from authorization and provider eligibility.
5. Standing disclosure authority uses existing `AUTH-*`; no `DISC-*` family/slot is introduced.
6. Exact action-specific User Instruction is bounded and does not silently become standing authority.
7. Provider/tool eligibility resolves independently and unavailable policy/identity fails closed when material.
8. Minimum-necessary context precedes external transmission.
9. Mixed-sensitivity context is partitioned; safe portions are not promoted by restricted portions and restricted portions are not leaked by safe portions.
10. Redaction uncertainty fails closed for the affected content.
11. Disclosure permission does not grant Decision, mutation, binding, runtime, publication, or Risk authority.
12. `[Meeting]` extra Project context routes through TASK-026 while the explicit question remains the default action-specific input.
13. `[Goal]`/`ENV-*`, tool access, model capability, repository access, and provider availability do not imply disclosure authority.
14. Project Knowledge/OpenViking consumers cannot bypass source-Project disclosure governance.
15. Material evidence uses `EVD-*`/source-native pointers without persisting full sensitive payload by default.
16. GREENFIELD creates no blanket disclosure grant/provider credential/classification records.
17. Brownfield does not retroactively mark historical content safe or synthesize disclosure authority.
18. No runtime redactor/router/proxy/scanner is added by this documentation/governance Task.
19. Launchers remain byte-identical in shared marker body and `<=4,500` characters if modified.
20. Historical amendments/evidence outside selected current mutable surfaces remain unchanged.
21. `git diff --check` passes and one final `RELEASE_FULL` runs on the unchanged candidate.

Pressure scenarios should include: unclassified auto-send, secret-value leakage, `SECRET-*` reference confusion, generic Goal disclosure overreach, exact one-off disclosure, standing provider-scoped `AUTH-*`, provider mismatch, provider policy unknown, mixed-sensitivity partition, failed redaction, whole-repo convenience dump, Meeting extra-context routing, Knowledge external-processing routing, OpenViking cross-Project authority overreach, evidence leak-through, Brownfield auto-classification, and classification/authorization confusion.

## 23. Acceptance criteria

TASK-026 is acceptable when every external-AI consumer can determine a bounded context payload through one consistent classification/minimization/provider-eligibility/authorization flow, protected/unknown data fails closed, actual secret values remain excluded, material disclosure is reconstructable without duplicating sensitive payload, and disclosure never becomes a shortcut to Project authority.

Key invariants:

```text
Classification ≠ Authorization
Provider Eligibility ≠ Authority
Disclosure Permission ≠ Project Mutation Permission
Secret Reference ≠ Secret Value Disclosure Permission
Unknown ≠ Safe
```

## 24. Non-goals

TASK-026 does not implement a DLP product, runtime redactor, provider gateway, policy engine, provider-account manager, secret store, model router, network interceptor, compliance certification program, automatic data classification engine, or universal rule that all Project data may be sent to AI.
