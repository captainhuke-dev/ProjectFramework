# Project Change Feed — Derived Starter

This maintained starter defines the optional Framework 1.14.0 `Project-Change-Feed/` derived surface. It is **not Project Source, not canonical history authority, and not Evidence**. Materialize it in a consuming Project only when an incremental consumer materially benefits and adoption is approved/applicable.

## Authority Boundary

```text
Project-Change-Feed ≠ Project Source
Project-Change-Feed ≠ 10 Change Log
Project-Change-Feed ≠ Git/source-native history
Project-Change-Feed ≠ EVD-*
Project-Change-Feed ≠ Project Knowledge
Project-Change-Feed ≠ OpenViking authority
```

The directory is rebuildable/disposable. If it is missing, stale, or corrupt, authoritative/source-native Project sources remain the basis for current/history truth.

## Suggested Projection Metadata

A consuming Project MAY maintain this metadata in its derived README or equivalent feed header:

```yaml
feed_projection_id: "<UUID_OR_STABLE_OPAQUE_DERIVED_ID>"
project_uuid: "<PROJECT_UUID>"
projection_state: "CURRENT | STALE | REBUILD_REQUIRED | UNAVAILABLE"
source_checkpoint:
  repository_ref: "<COMMIT_OR_UNKNOWN_OR_NOT_APPLICABLE>"
  project_source_manifest_ref: "<ACTIVE_14_POINTER_OR_UNKNOWN>"
  change_log_ref: "<ACTIVE_10_POINTER_OR_UNKNOWN>"
generated_at: "<ISO8601_OR_UNKNOWN>"
retention_policy: "<BOUNDED_POLICY_DESCRIPTION>"
```

`feed_projection_id` is derived-layer identity only. It is not a Project Source Stable ID or authority token.

## Checkpoint / Since Semantics

A consumer asking for changes `since` a checkpoint supplies or resolves source-native pointers such as repository ref + current Manifest + current Change Log. Prefer source-native ordering over timestamp inference. If the requested interval is outside retained feed coverage, rebuild from authoritative history or report the unavailable portion `UNKNOWN / VERIFICATION_REQUIRED`.

## Retention And Rebuild

Retention is bounded but Project-specific; Framework 1.14.0 mandates no universal window. Trimming feed entries never deletes authoritative history. `REBUILD_REQUIRED` means discard/reconstruct the projection from current/history Project Source, Change Log, Git/source-native history, relation history, durable evidence pointers, and release/publication evidence as applicable.

Project Knowledge and AI-ControlTower/OpenViking may assist discovery but never become history/feed authority.

For TASK-029 consumers, feed entries are candidate routing only. A feed entry never proves `DIRECT` impact by itself; material impact classification must trace back to authoritative/current Project evidence.

## Runtime Non-Goal

This starter creates no watcher, crawler, webhook, daemon, scheduler, event bus, queue, CDC runtime, Git hook, background agent, or automatic feed maintenance. It is a documentation/governance starter only.
