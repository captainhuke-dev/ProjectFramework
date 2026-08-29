# TASK-024 `[Meeting]` LLM Council Command — Design

Date: `2026-08-29` (Asia/Bangkok)
Task: `TASK-024`
Design state: `USER_APPROVED_DESIGN / WRITTEN_SPEC_REVIEW_REQUIRED`
Approval basis: after the proposed architecture and boundaries were presented, the user instructed the Agent to continue without further approval prompts on `2026-08-29`. This approves the presented TASK-024 design direction and permits materializing/self-reviewing this spec. The written-spec review gate remains required before implementation planning.
Target release: Framework `1.8.0` / Schema `1.0.0` / release format `3`

## 1. Purpose

ProjectFramework needs a registered `[Meeting]` command for cases where a Project question benefits from multiple independent model perspectives, peer evaluation, disagreement surfacing, and a synthesized advisory recommendation.

The command must improve decision support without creating a second authority system. Council output is evidence/advice only:

```text
Council Recommendation
≠ User Approval
≠ AUTH-*
≠ DEC-*
≠ REQ-* change
≠ Project mutation permission
```

A recommendation that would change governed Project truth still enters the existing Decision, Requirement, Risk, Architecture, Authority, Task, migration, or other applicable workflow.

## 2. Verified llm-council provider snapshot

TASK-024 design is bound to direct observation of the configured source repository rather than inferred upstream behavior.

Observed repository:

```text
Repository: captainhuke-dev/llm-council
Repository type: public GitHub fork
Parent/source: karpathy/llm-council
Default branch: master
Observed fork master commit: 92e1fccb1bdcf1bab7221aa9ed90f9dc72529131
Observed fork tree: 221d8afb6eca87537282d509971c505119390e0b
Observed parent master commit: 92e1fccb1bdcf1bab7221aa9ed90f9dc72529131
Observed divergence at design capture: none on compared master heads
```

Observed application architecture:

```text
Backend: FastAPI / Python
Frontend: React + Vite
Provider transport: OpenRouter HTTP API
Council model configuration: backend/config.py
Conversation persistence: JSON files under data/conversations/
Backend local port: 8001
Frontend local port: 5173
```

Observed council workflow:

```text
Stage 1 — send the user query independently to configured council models
Stage 2 — anonymize Stage-1 responses and ask council models to review/rank them
Stage 3 — ask the configured Chairman model to synthesize a final answer
```

Observed backend interfaces include:

```text
POST /api/conversations
GET  /api/conversations
GET  /api/conversations/{conversation_id}
POST /api/conversations/{conversation_id}/message
POST /api/conversations/{conversation_id}/message/stream
```

The synchronous message endpoint returns `stage1`, `stage2`, `stage3`, and `metadata`. The streaming endpoint emits stage progress/results over Server-Sent Events. The design treats synchronous complete-result behavior as the minimum provider interface; SSE is an optional delivery optimization, not a ProjectFramework semantic dependency.

The provider currently has no verified ProjectFramework-specific MCP contract, Project authority contract, or provider-side Project Source integration. TASK-024 must not pretend such an interface already exists.

## 3. Chosen architecture: Thin Council Provider Adapter

Three approaches were considered:

1. **Direct UI/storage coupling** — make llm-council conversation JSON/UI state part of ProjectFramework Meeting state. Rejected because provider storage would become hidden Project truth and tightly couple governance to one app topology.
2. **Reimplement council inside ProjectFramework** — copy/duplicate the orchestration logic into Framework sources. Rejected because ProjectFramework is documentation/governance first and should not fork provider runtime logic as part of a command contract.
3. **Thin Council Provider Adapter** — selected. `[Meeting]` is a ProjectFramework command/interface contract. `captainhuke-dev/llm-council` is the first verified advisory provider profile. A capable runtime/Agent may call the provider, normalize its output, and return/persist advisory evidence without making provider runtime/storage authoritative.

Core separation:

```text
ProjectFramework `[Meeting]` semantics = canonical Framework contract
llm-council runtime/API              = external advisory provider implementation
llm-council conversation storage     = provider-local state, never Project authority
normalized Meeting result            = advisory output/evidence candidate
Project decisions/requirements       = existing Project Source authority homes
```

A future provider adapter may replace the current FastAPI/OpenRouter path without changing `[Meeting]` semantics as long as it satisfies the normalized provider/result contract.

## 4. Registered command identity

Canonical display form:

```text
[Meeting]
```

Literal `[` and `]` are required. Registered-name matching inside brackets is case-insensitive according to the existing Project command contract.

Unbracketed words such as `meeting`, `council`, `ask several models`, or similar prose do not automatically invoke the registered command.

Minimum supported user intent:

```text
[Meeting] <topic/question>
```

The Framework may accept natural-language variants after `[Meeting]`, such as asking to review a proposal, compare options, identify risks, or challenge an assumption. TASK-024 does not require literal subcommands.

## 5. Meeting input and context boundary

The text explicitly supplied as part of the `[Meeting]` invocation is authorized as the Meeting question/input itself.

This does **not** create blanket permission to transmit unrelated Project Source or repository content to an external provider.

Context rules:

1. Start with the explicit Meeting question/input.
2. Add Project context only when it is materially relevant and the outbound disclosure is authorized under applicable governance.
3. Use minimum necessary context; prefer concise extracted facts/references over whole documents or repository dumps.
4. Preserve provenance of context used when a Meeting result becomes material evidence.
5. Never transmit actual secret values merely because they are relevant to the question.
6. A `SECRET-*` reference is not disclosure permission for the referenced value.
7. When disclosure authority/classification is unresolved, block the outbound-context portion rather than assuming `[Meeting]` authorizes it.

TASK-026 External AI Context & Disclosure Governance remains the intended canonical disclosure contract when implemented. Before TASK-026 exists, external Project context beyond the user-supplied Meeting input requires current explicit authorization or another applicable existing authority basis; uncertainty fails closed for that outbound content.

## 6. Provider adapter contract

A Meeting-capable provider adapter resolves at least:

```text
Provider Identity
Provider Source / Version Evidence when observable
Availability / Health
Input Question
Authorized Context Payload
Stage 1 Individual Responses
Stage 2 Peer Reviews / Rankings when available
Stage 3 Synthesis when available
Model / Chairman provenance when available
Provider Errors / Missing Stages
Completion State
```

For the verified llm-council snapshot, the baseline interaction is:

```text
create conversation
→ send one message through the synchronous message endpoint
→ receive stage1 + stage2 + stage3 + metadata
```

Using `/message/stream` is permitted when a runtime wants progressive presentation, but the normalized final Meeting contract must not depend on event-stream delivery.

ProjectFramework must not require the llm-council frontend to be running merely to define or interpret Meeting semantics. The provider's FastAPI contract is the relevant verified integration surface for the current snapshot.

## 7. Normalized Meeting result contract

A completed or partial `[Meeting]` should normalize provider output into these semantic sections when supported:

```text
Topic / Question
Context Scope Used
Provider / Model Provenance
Independent Views
Areas of Agreement
Disagreements / Competing Reasoning
Blind Spots / Risks / Missing Information
Peer-Review / Ranking Signal
Chairman / Synthesis Result
Recommended Interpretation / Next Consideration
Limitations / Failed Models / Missing Stages
Advisory Authority Notice
```

`Independent Views` should preserve materially distinct responses rather than collapsing them prematurely.

`Peer-Review / Ranking Signal` is a model-generated quality signal only. It is not a truth score, confidence proof, authorization, or deterministic correctness metric.

`Chairman / Synthesis Result` is also advisory. A single Chairman model must never be treated as Project adjudication authority merely because it summarizes the council.

The normalized result should surface meaningful disagreement instead of rewriting it into false consensus.

## 8. Advisory authority boundary

Council outputs may inform Human/Agent reasoning, but they never directly mutate Project state.

Examples:

- A recommendation to change architecture does not modify `06`/`40` automatically.
- A recommendation to change a requirement does not edit `REQ-*` automatically.
- A recommendation to accept a Risk does not satisfy Risk authority.
- A recommendation to push/deploy does not grant Git/deployment authority.
- A majority/ranking result does not create `DEC-*` automatically.

If the user chooses to adopt a recommendation, ProjectFramework routes the requested change through its normal owning object/workflow and required authority.

## 9. Persistence and evidence

TASK-024 does **not** introduce a `MEETING-*` Stable-ID family or a new semantic slot.

A Meeting may remain transient when it is exploratory and has no material Project consequence.

When a Meeting materially informs a Project decision, requirement, risk, design, task, or other governed claim, persist only the minimum reconstructable evidence needed in `13 Evidence Registry` as an `EVD-*` record or source-native evidence reference.

Material Meeting evidence should resolve, as applicable:

```text
Evidence Type: EXTERNAL_AI_COUNCIL / ADVISORY
Captured At
Captured By
Meeting Question
Context Scope / Disclosure Basis
Provider repository/profile
Observed provider version/commit when material and available
Participating models / Chairman when reported
Stage completeness
Independent-view / disagreement / synthesis artifact pointer or bounded summary
Provider/runtime failures
Supports: related Project Stable IDs
Epistemic Status
Advisory-only notice
```

Do not duplicate a full external conversation in Project Source merely because it exists in llm-council storage. Do not treat `data/conversations/*.json` as canonical Project history.

A later `DEC-*`, `REQ-*`, `RISK-*`, `ACT-*`, or other object may reference the `EVD-*`; the evidence itself does not become the governed decision/change.

## 10. Failure and partial-result semantics

Provider/runtime failures must be distinguished from substantive council disagreement.

Normalized Meeting execution states are presentation/workflow labels, not new Project lifecycle families:

```text
COMPLETE
PARTIAL
FAILED
UNAVAILABLE
```

Rules:

- **No Stage-1 responses:** `FAILED` or `UNAVAILABLE`; do not claim council consensus.
- **Some Stage-1 models fail:** `PARTIAL`; preserve successful independent views and list failed/unavailable models when observable.
- **Stage 2 incomplete/unavailable:** individual views remain usable; peer-ranking signal must be marked incomplete/unavailable.
- **Chairman failure:** do not fabricate synthesis or consensus. Return available independent/peer-review material with `SYNTHESIS_UNAVAILABLE` or equivalent limitation.
- **Network/auth/provider error:** report provider/runtime failure, not model disagreement.
- **Ranking parse degradation:** treat aggregate/parsed ranking as partial signal; raw ranking text may remain available as advisory evidence when appropriate.
- **Provider returns generic error text:** do not promote that text to a valid synthesis.

The current llm-council implementation drops unsuccessful model responses from Stage 1/2 and returns `None` from its OpenRouter client on request failures. TASK-024 therefore requires the adapter/result layer to surface partial participation rather than silently describing the remaining responses as a full council.

## 11. Provider freshness and capability handling

The council member list, Chairman model, OpenRouter endpoint, and provider source may change independently of ProjectFramework.

Therefore:

```text
configured model list ≠ permanent Framework invariant
provider availability ≠ Project authority
provider repository commit ≠ Project Source pin
provider freshness ≠ permission to disclose Project context
```

When a Meeting is material, fresh-observe the provider interface/profile to the degree required by the operation. If the provider materially changes away from the contract this spec relies on, fail closed for the affected integration and route TASK-024/provider-profile reconciliation rather than guessing compatibility.

## 12. Security and secret boundary

The verified provider uses an `OPENROUTER_API_KEY` environment variable and sends requests to OpenRouter.

ProjectFramework rules:

- never persist the actual API key in Project Source, Meeting evidence, Handoff, Task plans, logs, or exported context;
- record only governed secret references/metadata when needed;
- Meeting input must not include secret values unless an independently valid disclosure boundary explicitly permits the exact disclosure and higher-level safety/tool rules permit it;
- provider credential configuration is runtime/deployment scope, not granted merely by registering `[Meeting]`.

TASK-024 does not create a secret manager or credential distribution mechanism.

## 13. Relationship to `[Goal]` and `[Session Envelope]`

`[Meeting]` is advisory and may be used inside other authorized work, including a persistent `[Goal]` or session `ENV-*`.

However:

- Goal/Envelope execution authority does not automatically grant external Project-context disclosure.
- Meeting recommendations do not expand parent Goal `AUTH-*` or `ENV-*`.
- A Meeting can support a Goal success criterion as evidence only when the Goal's evidence rules accept it and actual outcome evidence is sufficient.
- `[Meeting]` does not create a hidden approval route around Goal/Authority/Decision boundaries.

## 14. GREENFIELD and Brownfield behavior

Framework `1.8.0` maintained starter/command surfaces may expose `[Meeting]` after TASK-024 implementation, but GREENFIELD initialization does not create a council conversation, Meeting evidence record, provider credential, or external disclosure authorization automatically.

Brownfield upgrade:

- preserve existing Project truth and current external-AI records;
- do not synthesize a Meeting from prior discussion, old AI transcripts, an existing `EVD-*`, backlog prose, or Handoff;
- do not require llm-council runtime installation merely to upgrade governance semantics;
- provider runtime setup remains an explicit applicable implementation/deployment concern.

## 15. Framework surfaces affected by implementation

If the written spec is approved, TASK-024 implementation is expected to affect only current governance/documentation surfaces required for the command contract, including as applicable:

- `Framework-Source/FRAMEWORK-RELEASE.yaml`
- a TASK-024 Framework `1.8.0` amendment
- `Framework-Source/references/core-governance-rules.md`
- `Framework-Source/SKILL.md`
- `Framework-Source/templates/00-project-source-framework.md`
- relevant skeleton/mockup guidance for `13 Evidence Registry` and command/status/help surfaces
- `README.md`
- `Framework-Source/MIGRATION-NOTES.md`
- ChatGPT/Claude launchers, preserving shared-body byte parity and `<=4,500` character ceiling
- `Framework-Source/tests/pressure-scenarios.md`
- Task/design/plan/evidence records

TASK-024 implementation does **not** include, unless separately approved:

```text
FastAPI proxy/server code
MCP server implementation
OpenRouter client implementation inside ProjectFramework
copy/fork of llm-council source
provider daemon/watch service
automatic council runtime installation
automatic credential provisioning
background council execution
CI/CD or deployment automation
```

## 16. Release classification

TASK-024 is designed as a backward-compatible Framework `1.8.0` semantic expansion with Project Source Schema `1.0.0` and release format `3`.

Rationale:

- it registers a command and evidence/advisory integration semantics;
- it does not add a semantic slot;
- it does not add a Stable-ID family;
- it does not require a new Project Source metadata schema field;
- provider runtime is external and optional/applicability-driven.

If implementation reveals that the required council/provider contract cannot be represented without incompatible Project Source schema changes, stop and reclassify rather than silently forcing Schema `1.0.0`.

## 17. Verification strategy

Affected verification must prove at minimum:

1. `[Meeting]` uses required literal brackets and case-insensitive registered-name matching.
2. `[Meeting]` is registered consistently on required current Framework surfaces.
3. Unbracketed meeting/council prose does not invoke the command automatically.
4. Council output is explicitly advisory and never direct Project authority/approval/Decision/mutation permission.
5. No `MEETING-*` Stable-ID family or new semantic slot is introduced.
6. The provider snapshot/interface provenance is captured accurately and does not imply provider storage authority.
7. User-supplied Meeting input is distinguishable from additional Project context disclosure.
8. Additional Project context is minimized and requires applicable disclosure authority; unresolved disclosure fails closed for the outbound content.
9. Secret values remain prohibited.
10. Normalized results preserve independent views, agreement/disagreement, peer-review signal, synthesis, and limitations without false consensus.
11. Partial model/stage failures are surfaced as partial/provider failures rather than hidden.
12. Chairman failure never fabricates consensus.
13. Provider/model configuration is runtime evidence, not a permanent Framework invariant.
14. Material Meeting persistence uses `EVD-*`/source-native evidence references and does not make llm-council JSON storage canonical Project truth.
15. Existing Decision/Requirement/Risk/Authority workflows remain required for adoption of recommendations.
16. `[Goal]`/`ENV-*` authority does not implicitly grant outbound disclosure or expand from Meeting results.
17. GREENFIELD/Brownfield upgrades do not create conversations, credentials, Meeting records, or disclosure authority automatically.
18. Launchers remain byte-identical in their shared marker body and within the current character ceiling.
19. Historical amendments/evidence outside selected current mutable surfaces remain unchanged.
20. `git diff --check` passes and one final `RELEASE_FULL` runs on the unchanged candidate under current release rules.

Pressure scenarios should cover at least: missing brackets, case-insensitive command matching, minimum-context invocation, attempted whole-Project disclosure, secret-value leakage, advisory recommendation treated as approval, majority vote treated as Decision, partial Stage-1 participation, Stage-2 failure, Chairman failure, provider unavailable/auth error, stale/provider-interface mismatch, evidence persistence boundary, provider JSON treated as authority, Goal/Envelope disclosure overreach, and Brownfield no-auto-Meeting behavior.

## 18. Acceptance criteria

TASK-024 is acceptable when a user can invoke `[Meeting]` with a question, a capable runtime can use a verified advisory provider to obtain multiple independent responses/peer review/synthesis, and ProjectFramework can present or persist a normalized advisory result while preserving disclosure minimization, secret safety, partial-failure truth, provider/runtime separation, and all existing Project authority/change workflows.

The key invariant is:

```text
Multi-model advice improves Project reasoning without becoming Project authority.
```

## 19. Non-goals

TASK-024 does not make council consensus authoritative, automatically implement recommendations, create a new authorization family, create `MEETING-*`, replace TASK-026 disclosure governance, choose the canonical AI provider for every Project, guarantee external model availability, manage OpenRouter billing/credentials, or turn ProjectFramework into the llm-council runtime.
