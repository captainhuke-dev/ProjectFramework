# Execution Checkpoint Template

Declarative **derived recovery accelerator** over the Runtime Event Journal. A checkpoint can be rebuilt or invalidated; it never outranks the journal or source-native truth.

```yaml
record_type: EXECUTION_CHECKPOINT
record_version: "1.0"
execution_id: "<execution>"
checkpoint_seq: "<checkpoint sequence>"
event_sequence: "<last included journal event sequence>"
previous_checkpoint_hash: "<previous checkpoint or NOT_APPLICABLE>"
state_version: "<runtime state version>"
resume_cursor: "<deterministic resume location>"
created_at: "<timestamp>"
```

Rules:

- A checkpoint MUST be **traceable to the journal sequence it summarizes.** A checkpoint referencing an `event_sequence` beyond proven journal continuity is invalid and MUST be discarded.
- `Checkpoint != Runtime Event Journal != Project Source != canonical Task lifecycle truth.`
- Recovery SHOULD load a compatible checkpoint and replay the journal tail. If required journal continuity cannot be proven, recovery fails closed as `RECOVERY_BLOCKED` or equivalent; it MUST NOT reconstruct execution truth from a checkpoint fragment, an LLM transcript, or model memory.
- A checkpoint is a **recovery accelerator, not an authority.** It grants no ownership, AUTH, permit, or continuation eligibility.
- No historical Task or execution receives an invented checkpoint; unresolvable mapping remains `UNKNOWN.`
- This file is derived runtime-domain state. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No checkpoint service, snapshot daemon, or automatic restore engine is implied by this record.
