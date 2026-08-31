# TASK-024 `[Meeting]` LLM Council Command — Release Verification Evidence

Date: `2026-08-29` (Asia/Bangkok)
Task: `TASK-024`
Framework candidate: `1.8.0`
Project Source Schema: `1.0.0`
Release format: `3`
Publication state at capture: `NOT_PUSHED`

## Verified candidate identity

```text
Candidate HEAD: e1c8ba0ad40fe956911043ff98239b7682a3d23e
Candidate tree: 3cae37a05c97a3efa66ffb6f2e1cf941579187aa
Framework-Source tree: 9a959e20723c28c58e7b37be7fd52aef8501d8f1
Branch observed: main
origin/main observed before final verification: eb231ee2d1d83b42455ab2f3cab250d4d442fda0
Working tree before RELEASE_FULL: CLEAN
```

The candidate identity above was frozen before the final `RELEASE_FULL`; the candidate did not change during that verification run.

## Scope implemented

TASK-024 registers `[Meeting]` as a Framework `1.8.0` multi-model advisory command while keeping external-provider reasoning separate from Project authority.

Implemented current surfaces include:

- TASK-024 Framework amendment and latest-amendment routing;
- Core Governance and `SKILL.md` command/workflow semantics;
- explicit Meeting question as the default outbound payload;
- minimum-necessary, separately authorized additional Project context;
- actual-secret-value prohibition;
- Thin Council Provider Adapter boundary;
- normalized independent views / agreement / disagreement / peer signal / synthesis / limitations contract;
- `COMPLETE | PARTIAL | FAILED | UNAVAILABLE` Meeting workflow labels;
- Stage-1/Stage-2/Chairman/provider failure truth without fabricated consensus;
- advisory-only authority separation;
- material Meeting persistence through existing `EVD-*` rather than a `MEETING-*` family;
- provider JSON/runtime/storage non-authority;
- `[Goal]` / `ENV-*` execution-authority versus disclosure-authority separation;
- GREENFIELD/Brownfield no-auto-Meeting behavior;
- maintained starter, README, migration-note, launcher, and pressure-scenario propagation;
- no ProjectFramework provider runtime, MCP server, OpenRouter client, daemon, installer, credential provisioning, or background council implementation.

## Verified external provider profile

The approved TASK-024 design and implementation prerequisite directly observed the configured provider repository rather than inferring it from upstream knowledge.

```text
Repository: captainhuke-dev/llm-council
Repository type: public fork
Default branch: master
Observed fork master commit: 92e1fccb1bdcf1bab7221aa9ed90f9dc72529131
Observed fork tree: 221d8afb6eca87537282d509971c505119390e0b
Compared parent: karpathy/llm-council
Parent master at design capture: same commit 92e1fccb1bdcf1bab7221aa9ed90f9dc72529131
Implementation prerequisite re-observation: unchanged fork master/tree
```

Observed provider contract used by the design:

```text
FastAPI backend
OpenRouter transport
POST /api/conversations
POST /api/conversations/{conversation_id}/message
optional /message/stream SSE delivery
Stage 1 independent responses
Stage 2 anonymized peer review/ranking
Stage 3 Chairman synthesis
provider-local JSON conversation storage under data/conversations/
```

The provider snapshot is evidence for the first provider profile, not immutable Framework authority.

## Pressure scenarios

TASK-024 added scenarios `212–227`:

```text
212 Meeting Brackets Required
213 Meeting Matching Is Case-Insensitive
214 Explicit Meeting Input Is The Default Outbound Payload
215 Meeting Cannot Auto-Disclose Whole Project
216 Meeting Never Sends Secret Values By Default
217 Council Recommendation Is Advisory Only
218 Council Majority Is Not A Project Decision
219 Partial Stage-1 Participation Is Surfaced
220 Stage-2 Failure Leaves Peer Ranking Incomplete
221 Chairman Failure Does Not Fabricate Consensus
222 Provider/Auth/Network Failure Is Not Council Disagreement
223 Provider Interface Drift Fails Closed
224 Material Meeting Evidence Uses EVD Not Provider JSON Authority
225 Goal Or ENV Does Not Imply Meeting Disclosure Authority
226 Brownfield Upgrade Does Not Auto-Create Meeting State
227 Provider Runtime Is Optional To Governance Semantics
```

Framework-wide scenario numbering was verified as exactly `1–227`, contiguous and unique.

## AFFECTED verification

Initial AFFECTED run:

```text
50/55
```

Root-cause review found four verifier wording defects where current source already expressed equivalent/stronger semantics, plus one real Task Registry continuity defect: TASK-024 was `IN_PROGRESS` while `Plan State` still said `IMPLEMENTATION_PLAN_READY` and Exact Next Step still referenced Task 1.

The canonical Task Registry defect was corrected in commit `e1c8ba0` by setting the plan to execution state and routing Exact Next Step to Task 5. The verifier was tightened to accept semantically equivalent wording rather than requiring one literal phrase.

Final AFFECTED result on the clean candidate:

```text
TASK024_AFFECTED 55/55 PASS
Launcher lengths: 4492 / 4491
Scenarios: 227 / last 227
```

AFFECTED coverage included command identity, provider profile/interface, advisory authority, disclosure/secret boundaries, partial failures, EVD persistence, no `MEETING-*`, Goal/ENV separation, starter stamps, reserved slots, launcher parity/size, Task lifecycle, local Project pin, historical integrity, no runtime artifacts, `git diff --check`, and clean working tree.

## Final RELEASE_FULL

One final `RELEASE_FULL` was run on the frozen unchanged candidate:

```text
RELEASE_FULL PASS 314/314
Candidate HEAD: e1c8ba0ad40fe956911043ff98239b7682a3d23e
Candidate tree: 3cae37a05c97a3efa66ffb6f2e1cf941579187aa
Framework-Source tree: 9a959e20723c28c58e7b37be7fd52aef8501d8f1
Scenarios: 1–227
Launcher lengths: 4492 / 4491
```

The full run additionally checked every pressure-scenario ID individually, release/bootstrap package integrity, amendment chain, maintained mandatory/conditional starter slot mapping, reserved `18–19`, current command/close tokens, historical TASK-038/TASK-039 evidence integrity, ProjectFramework local `1.7.0` pin preservation, and absence of runtime implementation artifacts.

## Authority and publication boundary

The verified implementation remains documentation/governance scope.

```text
Council Recommendation ≠ User Approval
Council Recommendation ≠ AUTH-*
Council Recommendation ≠ DEC-*
Council Recommendation ≠ REQ-* change
Council Recommendation ≠ Project mutation permission
commit ≠ push
```

No remote publication was performed as part of TASK-024 verification. Publication requires its own applicable authority and fresh integration/remote checks.

## Completion conclusion

TASK-024 implementation satisfies its approved written design and implementation plan on the recorded candidate. Release evidence is sufficient for the subsequent Task Registry / Project Source lifecycle reconciliation to mark TASK-024 complete, while remote publication remains `NOT_PUSHED`.
