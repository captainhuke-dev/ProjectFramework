---
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.8.0"
project_source_framework_version: "1.8.0"
project_source_schema_version: "1.0.0"
approval_basis: "USER_APPROVED_WRITTEN_SPEC_2026-08-29"
compatibility: "BACKWARD_COMPATIBLE_ADVISORY_MEETING_COMMAND"
---

# Framework 1.8.0 Amendment — `[Meeting]` LLM Council Advisory Command

Framework `1.8.0` preserves TASK-038 `Framework-Source/` naming, TASK-039 persistent `[Goal]` semantics, and all prior Framework rules unless refined here. Project Source Schema remains `1.0.0`; release format remains `3`. This amendment registers `[Meeting]` as a bounded multi-model advisory command. Multi-model advice improves Project reasoning without becoming Project authority.

## 1. Command identity

Canonical command:

```text
[Meeting] : convene a multi-model advisory council for a question using minimum authorized context; results are evidence/advice, never Project authority
```

Literal `[` and `]` are required. Registered-name matching inside brackets is case-insensitive. Unbracketed words such as `meeting`, `council`, or `ask several models` remain ordinary language and do not invoke this command automatically.

Minimum invocation:

```text
[Meeting] <topic/question>
```

The explicit text supplied with `[Meeting]` is the Meeting question/input and is the default outbound payload.

## 2. Thin Council Provider Adapter boundary

ProjectFramework owns the `[Meeting]` command semantics, context/disclosure boundary, normalized result contract, evidence rules, and advisory-authority separation. The LLM Council runtime remains an external advisory provider implementation.

Verified provider profile at TASK-024 design/implementation capture:

```text
Repository: captainhuke-dev/llm-council
Default branch: master
Observed commit: 92e1fccb1bdcf1bab7221aa9ed90f9dc72529131
Observed tree: 221d8afb6eca87537282d509971c505119390e0b
Backend: FastAPI
Provider transport: OpenRouter HTTP API
Conversation storage: data/conversations/*.json
Baseline interaction: POST /api/conversations → POST /api/conversations/{conversation_id}/message
Complete response fields: stage1 + stage2 + stage3 + metadata
Optional delivery: /message/stream over SSE
```

This snapshot is provider-profile evidence, not an immutable Framework invariant. Provider availability, model list, Chairman model, endpoint details, source commit, or storage implementation may change independently of ProjectFramework. Material interface drift must be fresh-checked and fails closed for the affected integration rather than guessed compatible.

Provider UI, JSON conversation storage, runtime state, repository commit, or OpenRouter state never becomes Project authority merely because `[Meeting]` uses that provider.

## 3. Context and disclosure boundary

The explicit Meeting question is authorized as the Meeting input itself. It does **not** authorize automatic disclosure of unrelated Project Source, repository content, Handoff, evidence, secrets, or whole-Project context.

Additional Project context follows:

```text
identify relevance
→ select minimum necessary context
→ verify applicable outbound-disclosure authority
→ remove/protect actual secret values
→ send only the authorized bounded payload
```

When disclosure authority/classification is unresolved, block the outbound-context portion. Do not infer disclosure authority from `[Meeting]`, `[Goal]`, `AUTH-*`, `ENV-*`, task scope, local access, or the fact that the provider is available.

TASK-026 External AI Context & Disclosure Governance is the intended canonical disclosure contract when adopted. Until then, Project context beyond the user-supplied Meeting input requires applicable current explicit authorization or another valid existing disclosure basis.

## 4. Secret boundary

Actual secret values MUST NOT be persisted or transmitted merely because they are relevant to a Meeting. A `SECRET-*` reference identifies secret metadata/reference only; it is not permission to reveal the referenced value.

Never persist actual provider API keys or other secret values in Project Source, Meeting evidence, Handoff, Task/spec/plan documents, logs, exports, or normalized Meeting results. Provider credential configuration remains runtime/deployment scope.

## 5. Council workflow and normalized result

A Meeting-capable provider resolves available independent responses, peer review/ranking, synthesis, model/provenance information, missing stages, and provider/runtime failures.

For the verified llm-council profile the observed orchestration is:

```text
Stage 1 — independent model responses
Stage 2 — anonymized peer review / ranking
Stage 3 — Chairman synthesis
```

Normalized Meeting result sections, when supported, are:

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

Preserve materially distinct views and disagreement. Do not rewrite disagreement into false consensus merely because a majority, ranking, or Chairman result exists.

## 6. Advisory authority invariant

Council output is advisory evidence/reasoning only:

```text
Council Recommendation
≠ User Approval
≠ AUTH-*
≠ DEC-*
≠ REQ-* change
≠ Risk acceptance
≠ architecture mutation
≠ push/deployment permission
≠ Project mutation permission
```

A peer ranking is a model-generated quality signal, not a truth score. A majority is not a Project Decision. A Chairman synthesis is not adjudication authority.

If a recommendation is adopted, route the requested change through its existing canonical owner and required governance/authority. `[Meeting]` itself performs no automatic Project mutation.

## 7. Persistence — use existing Evidence

TASK-024 creates no `MEETING-*` Stable-ID family and no new semantic slot.

Exploratory Meetings may remain transient. When a Meeting materially informs governed Project truth, persist only minimum reconstructable evidence as `EVD-*` in `13 Evidence Registry` or a source-native evidence pointer.

Material Meeting evidence should resolve as applicable:

```text
Evidence Type: EXTERNAL_AI_COUNCIL / ADVISORY
Captured At / Captured By
Meeting Question
Context Scope / Disclosure Basis
Provider repository/profile + observed version when material
Participating models / Chairman when reported
Stage completeness
Independent-view / disagreement / synthesis bounded summary or source-native pointer
Provider/runtime failures
Supports: related Project Stable IDs
Epistemic Status
Advisory-only notice
```

Provider `data/conversations/*.json` is provider-local storage and never canonical Project history or Project Source. Do not copy full provider conversations into Project Source merely because they exist.

## 8. Partial and failure semantics

Meeting execution labels are presentation/workflow labels only, not Project lifecycle families:

```text
COMPLETE | PARTIAL | FAILED | UNAVAILABLE
```

Rules:

- no successful Stage-1 response → `FAILED` or `UNAVAILABLE`; never claim consensus;
- partial Stage-1 participation → `PARTIAL`; preserve successful views and list failed/unavailable participants when observable;
- incomplete/unavailable Stage 2 → preserve individual views; peer-ranking signal remains explicitly incomplete/unavailable;
- Chairman failure → preserve available independent/peer-review material and surface `SYNTHESIS_UNAVAILABLE` (or equivalent); never fabricate consensus;
- network/auth/provider/runtime failure → report provider failure, not substantive model disagreement;
- ranking parse degradation → treat parsed/aggregate ranking as partial signal; do not infer a complete ranking;
- provider generic error text → never promote it as a valid synthesis.

## 9. Relationship to `[Goal]` and `[Session Envelope]`

A Meeting may occur inside an authorized `[Goal]` or session `ENV-*`, but execution authority and disclosure authority remain separate.

```text
Goal/ENV authority ≠ outbound Project-context disclosure authority
Meeting recommendation ≠ expansion of parent AUTH-* or ENV-*
Meeting evidence ≠ Goal achievement by itself
```

A Meeting may support a Goal success criterion only when the Goal's evidence contract accepts that evidence and the actual outcome criteria are otherwise satisfied.

## 10. GREENFIELD and Brownfield

Framework `1.8.0` starter/help surfaces expose `[Meeting]` after this amendment, but GREENFIELD initialization MUST NOT automatically create a council conversation, Meeting evidence record, provider credential, provider runtime, or external-disclosure authorization.

Brownfield upgrade MUST NOT synthesize a Meeting from old AI transcripts, prior discussion, backlog prose, Handoff, existing `EVD-*`, old provider JSON, or other historical text. Preserve existing Project truth and external-AI/evidence records. Adopting governance semantics does not require installing/running llm-council.

## 11. Runtime and implementation boundary

This Framework amendment defines governance/documentation semantics only. It does not implement:

```text
FastAPI proxy/server
MCP server
OpenRouter client inside ProjectFramework
copy/fork of llm-council source
provider daemon/watcher
runtime installer
credential provisioning
background council execution
CI/CD/deployment automation
```

A capable Agent/runtime may invoke a compatible provider through available tools, but provider capability never becomes Project authority.

## 12. Compatibility

This is a backward-compatible Framework `1.8.0` semantic expansion. Schema remains `1.0.0`; release format remains `3`; no semantic slot, Stable-ID family, or authorization family is added. TASK-038 distribution-root and TASK-039 `[Goal]` contracts remain binding.
