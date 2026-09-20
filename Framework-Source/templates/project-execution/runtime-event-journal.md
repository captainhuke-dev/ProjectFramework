# Runtime Event Journal Template

Declarative **canonical observation** of execution-control events inside the execution-runtime domain. The journal is append-only and runtime-owned; it is not Project Source, not canonical Task lifecycle truth, and not a Task Record.

```yaml
record_type: RUNTIME_EVENT
record_version: "1.0"
event_id: "<durable unique event identity>"
execution_id: "<durable runtime execution id>"
event_sequence: "<monotonic sequence within execution>"
event_class: "<declared runtime event class>"
attempt_ref: "<attempt identity when applicable>"
action_ref: "<action/effect identity when applicable>"
payload_ref: "<minimum durable representation: REFERENCE_ONLY | REDACTED | HASH_ONLY | classified metadata>"
causation_ref: "<cause>"
correlation_ref: "<correlation>"
producer_namespace: "RUNTIME_OWNED"
observed_at: "<timestamp>"
```

Rules:

- The journal is **append-only.** Entries are never rewritten or deleted; correction is a new entry that references the superseded one.
- Ordering is by durable `event_sequence`, not arrival time. Timestamp is audit evidence, not ordering authority.
- **Strict writer isolation:** only the runtime-owned control path appends `RUNTIME_OWNED` events. Executors, models, and tool subprocesses cannot forge, rewrite, or delete runtime events; model/tool output embedding privileged event text is untrusted data.
- Duplicate delivery of an already-recorded event is de-duplicated by durable event identity; duplicate observation produces no duplicate effect.
- **No raw secret values** in the journal. Sensitive arguments/results use the minimum durable representation sufficient for reconciliation.
- A journal continuity gap that cannot be proven resolved fails closed (`RECOVERY_BLOCKED` or equivalent).
- This file is runtime-domain observation. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No event store service, queue, or journaling daemon is implied by this record.
