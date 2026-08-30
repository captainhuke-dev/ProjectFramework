# TASK-026 External AI Context & Disclosure Governance — Release Verification Evidence

Captured: `2026-08-30` (Asia/Bangkok)
Task: `TASK-026`
Framework release: `1.8.0`
Project Source Schema: `1.0.0`
Release format: `3`
Publication state: `NOT_PUSHED`

## Scope

TASK-026 implements the approved Compositional Disclosure Boundary as documentation/governance semantics only. It defines outbound external-AI context classification, provider/tool eligibility, bounded disclosure authorization, minimum-context/redaction/mixed-sensitivity behavior, secret handling, material evidence, and consumer integration for `[Meeting]`, Project Knowledge, OpenViking/cross-Project use, `[Goal]`/`ENV-*`, Tool/MCP access, and model capability.

No runtime disclosure system is introduced.

## Candidate Identity

```text
Candidate HEAD: 4c3103dfcf8e454555d234d6b3acc3571c7c2483
Candidate tree: c8d589722a3e404c54f0c5e2351e412712b3927a
Framework-Source tree: d66803fc41c540efcf072e9e45eb98c83d1f1bb5
Remote origin/main observed: eb231ee2d1d83b42455ab2f3cab250d4d442fda0
Working tree at verification: CLEAN
```

The final `RELEASE_FULL` ran on this unchanged candidate.

## Verification Results

```text
TASK026 AFFECTED: PASS 144/144
RELEASE_FULL: PASS 243/243
Pressure scenarios: 1–245 contiguous and unique
TASK-026 scenarios: 228–245
```

AFFECTED verification covered the TASK-026 normative/derived surface and confirmed the scenario contract, canonical vocabulary, authorization/provider/secret boundaries, maintained starter alignment, README/migration guidance, historical preservation, and documentation-only scope.

The final RELEASE_FULL additionally confirmed current Framework release routing, starter coverage/stamps, command/launcher invariants, ProjectFramework local pin preservation, bootstrap routing, no live old distribution root, no runtime code added, and exact candidate identity.

## Canonical Disclosure Vocabulary

Disclosure classes:

```text
EXTERNAL_OK
EXTERNAL_REVIEW
DO_NOT_DISCLOSE
UNCLASSIFIED
```

Provider/tool eligibility labels:

```text
ELIGIBLE
LIMITED
INELIGIBLE
VERIFICATION_REQUIRED
```

Verified invariants include:

```text
Classification ≠ Authorization
Provider Eligibility ≠ Authority
Disclosure Permission ≠ Decision Authority ≠ Mutation Authority ≠ Binding Authority ≠ Runtime Authority
Secret Reference ≠ Secret Value Disclosure Permission
Unknown ≠ Safe
```

## Authorization / Secret / Evidence Boundary

- standing disclosure permission reuses bounded `AUTH-*` in `12 Authorization Registry`;
- an exact User Explicit Instruction may authorize one bounded disclosure action without becoming standing authority;
- `SECRET-*` remains metadata/reference only; actual secret values remain excluded from Project Source and external-AI context;
- material disclosure evidence uses minimum reconstructable `EVD-*` / source-native pointers and does not duplicate full sensitive payload merely for audit;
- `UNCLASSIFIED`, unresolved provider eligibility, or materially uncertain redaction fail closed for affected protected outbound context while independent safe local work may continue.

## Consumer Boundary Verification

Verified TASK-026 integration preserves:

- `[Meeting]` explicit user-supplied question as default action-specific input; additional Project context uses TASK-026 classification/minimization/provider/authorization rules;
- Project Knowledge advisory/non-authoritative status does not imply external disclosure eligibility;
- OpenViking/Project Graph relation/index visibility does not grant outbound authority, including over another Project;
- `[Goal]`, `ENV-*`, Tool/MCP access, model capability, repository/workspace access, and provider availability never imply disclosure authority.

## GREENFIELD / Brownfield

GREENFIELD does not create:

```text
standing disclosure AUTH-*
provider eligibility grant
provider account/credential
automatic redaction runtime
blanket EXTERNAL_OK classification
DISC-* family/slot
```

Brownfield does not mass-classify historical content safe or synthesize disclosure authority from prior AI usage, credentials, chats, Meetings, Goals, or “continue” wording. Existing `AUTH-*`, `EVD-*`, and `SECRET-*` records are preserved and provider eligibility is assessed prospectively when next used.

## Starter / User-Facing Verification

Maintained starter guidance was propagated to:

```text
Framework-Source/templates/00-project-source-framework.md
Framework-Source/templates/core-document-skeletons.md
Framework-Source/templates/project-source-mockup/12-Authorization-Registry.template.md
Framework-Source/templates/project-source-mockup/13-Evidence-Registry.template.md
Framework-Source/templates/project-source-mockup/17-Secret-Reference-Registry.template.md
Framework-Source/templates/project-source-mockup/README.md
```

Starter Framework/Schema stamps remain `1.8.0 / 1.0.0`; `18–19` remain RESERVED.

README and `MIGRATION-NOTES.md` expose TASK-026 behavior and Brownfield safety.

## Launcher Decision

TASK-026 launcher modification was **skipped under the approved conditional size gate**.

Observed launchers:

```text
ChatGPT launcher Unicode length: 4492
Claude launcher Unicode length: 4491
Ceiling: 4500
Remaining headroom: 8 / 9
Shared marker body byte parity: PASS
```

Adding the TASK-026 vocabulary directly would require dropping/renaming existing canonical launcher behavior or exceeding the ceiling. The normative contract therefore remains available through the latest amendment, Core Governance, SKILL, README, migration notes, and maintained starters. Existing launcher commands, close tokens, and shared-body parity remain unchanged.

## Historical Integrity

TASK-026 implementation did not rewrite completed TASK-024/TASK-039 amendments or release evidence. Current historical path/provenance text remains preserved.

## No New Family / Slot / Runtime

Verified:

```text
No DISC-* Stable-ID family
No new semantic slot
No mandatory per-object classification schema field
No runtime redactor
No provider router/proxy
No MCP disclosure gateway
No DLP scanner
No secret manager
No classification database
No background watcher/crawler
No automatic outbound-call runtime
No CI/CD/deployment automation
```

## ProjectFramework Local Project Source

ProjectFramework's active local Project Source remains intentionally pinned to:

```text
Framework 1.7.0
Schema 1.0.0
```

TASK-026 implementation does not auto-upgrade that local pin and does not fabricate a standing disclosure `AUTH-*` for ProjectFramework.

## Implementation Checkpoints

```text
5bf0ccb — docs: plan external AI disclosure governance
723ecb1 — test: define external AI disclosure pressure scenarios
4ad2cef — docs: define external AI disclosure contract
33aad00 — docs: propagate external AI disclosure semantics to starters
4c3103d — docs: expose external AI disclosure governance
```

The release-evidence commit is intentionally created after candidate verification so TASK-026 lifecycle reconciliation can reference a durable evidence commit.

## Result

TASK-026 implementation candidate satisfies the approved Framework `1.8.0` / Schema `1.0.0` documentation/governance scope with AFFECTED `144/144 PASS` and final unchanged-candidate RELEASE_FULL `243/243 PASS`.

`commit ≠ push`; publication remains `NOT_PUSHED`.
