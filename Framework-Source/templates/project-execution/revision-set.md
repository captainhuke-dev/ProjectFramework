# Revision Set Template

Declarative record of **which source state** one execution attempt ran against. The Revision Set answers source identity; it is not a locator, not a mutable pointer, and not authority.

`Resource Identity ≠ Locator ≠ Revision.` A resource may move or be renamed without changing its logical identity; a locator is routing information; a revision is exact observed state.

```yaml
record_type: REVISION_SET
record_version: "1.0"
revision_set_ref: "<contract-local reference>"
digest_profile_ref: "<canonicalization + digest profile>"
resources:
  - resource_ref: "<logical resource identity>"
    role: "<declared role>"
    required: true
    identity_kind: "GIT | FILE_SET | SCHEMA | EXTERNAL_CONTRACT | SOURCE_NATIVE"
    locator_ref: "<routing locator>"
    revision:
      exact_identity: "<source-native exact revision, e.g. exact commit SHA>"
    observed_at: "<timestamp of the observation>"
completeness:
  required_resources: 1
  resolved_required_resources: 1
  state: "COMPLETE | INCOMPLETE | UNKNOWN"
revision_set_digest: "<semantic digest under digest_profile_ref>"
created_at: "<timestamp>"
```

Rules:

- Every declared required resource must resolve exactly for `COMPLETE`; an unresolved required resource blocks `COMPLETE.`
- Optional missing resources do not block `COMPLETE` unless another contract makes them material.
- A single Git repository exact SHA is a valid one-member Revision Set.
- Once referenced by an Execution State Binding, the Revision Set is **immutable evidence.** Source change produces a new observation/set; historical evidence is never changed to `latest.`
- A semantic digest excludes irrelevant timestamps/formatting and is comparable only under a compatible `digest_profile_ref` (canonicalization profile, algorithm identity, profile version). Same digest text under an incompatible profile is not proven semantic identity.
- No `RESOURCE-*` Project Stable-ID family is introduced. `resource_ref` may be a Project-owned identifier, a Project Adapter mapping, or a runtime-local identity whose scope is declared.
- This file is evidence. It is not Root Governance, `AUTH-*`, Project Source, Task lifecycle truth, or a Stable-ID family.
- No runtime, state engine, canonicalization service, or automatic resolver is implied by this record.
