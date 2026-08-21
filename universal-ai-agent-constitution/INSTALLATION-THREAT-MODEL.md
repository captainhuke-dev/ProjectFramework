# UAAC v4.2 Project Installation Threat Model

## Assets

Effective Constitution/Project Law, Project identity/boundary, canonical documents/state, authority records, continuation/evidence/artifact identity, procedures/adapters, secrets and external-effect receipts

## Trust boundaries

```text
upstream release → installer → target Project
launcher → Bootstrap Kernel → Project binding/front door
front door → registries/state stores
local worktree → canonical remote surface → receiver
attempt observation → material write/ref update
context substrate → canonical source
```

## Threats and controls

| Threat | Failure | Control |
|---|---|---|
| Tutorial executed as protocol | example paths/commands mutate real Project | HUMAN metadata + `DO_NOT_EXECUTE`; no Agent execution dependency |
| Bootstrap circularity | BOOT Skill needed before Skill Registry | Minimal Kernel before Skill discovery |
| Wrong Project binding | Agent acts in another root/repo/ref | binding artifact + root/origin/front-door/Project-ID comparison |
| Nested front-door ambiguity | parent sees child as conflict or Agent selects wrong root | one front door per declared boundary; explicit parent/child binding |
| TOCTOU | state changes between boot and write | attempt preconditions + immediate pre-write recheck |
| Local/remote divergence | ChatGPT believes old remote state is current | visibility states + canonical publication/readback before handoff |
| URL without access | prompt looks connected but remote Agent cannot read | per-agent canonical access receipt |
| File-only adapter | Skill exists but never invoked | adapter registry + behavioral invocation evidence |
| Overeager Auto-Boot | every prompt reloads everything | FULL/DELTA/LIGHT + bounded reads and invalidation triggers |
| Under-eager Auto-Boot | task labeled non-material to bypass rules | material-task floor; UNKNOWN with potential impact → MATERIAL |
| Mutable upstream | Project law changes silently | immutable pin/vendor and authorized upgrade |
| Brownfield duplication | competing PRD/Project Law/current state | inventory + semantic mapping + conflict state |
| Last-write-wins | one Agent overwrites another | continuation epochs/predecessors + task-context recheck |
| Partial release | front door visible before targets | atomic final-tree replacement and expected-old-ref guard |
| Self-mutating workflow | effective branch becomes staging transport | read-only CI; build outside effective ref |
| Secret ingestion | credentials enter Git/memory | references/redaction/secret policy; context privacy only defense in depth |
| Evidence theater | positive token self-substantiates | claim contracts + independent receipts + non-positive fallback |

## Residual risk

Static checks cannot prove every future model/session will obey launchers. Re-run adapter/convergence/access tests after Agent, connector, Project binding, governance, requirements, or access-policy changes and sample runtime Boot receipts
