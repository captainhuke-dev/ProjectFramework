# Project Source Framework Governance Amendment — 1.1.4

```yaml
document_id: "FRAMEWORK-001"
change_type: "FRAMEWORK_AMENDMENT"
previous_project_source_framework_version: "1.1.3"
project_source_framework_version: "1.1.4"
project_source_schema_version: "1.0.0"
approved_at: "2026-08-20T08:21:00+07:00"
approval_basis: "USER_EXPLICIT_APPROVAL"
compatibility: "BACKWARD_COMPATIBLE_RELEASE_PROVENANCE_CLARIFICATION"
```

## Purpose

Make ProjectFramework bootstrap reproducible at the Git source level without introducing a self-referential release commit identity. Framework `1.1.4` adds machine-readable distribution metadata and requires NEW Projects to preserve the exact Git provenance they actually observed during bootstrap.

## Binding Changes

1. The distribution MUST include `managing-project-source/FRAMEWORK-RELEASE.yaml` as machine-readable release metadata. It is a distribution artifact, not a Project Source semantic slot and not a replacement for `FRAMEWORK-001`.
2. `FRAMEWORK-RELEASE.yaml` declares `stable_release_tag: "v1.1.4"` as the preferred immutable bootstrap ref for NEW Projects.
3. The release descriptor MUST NOT embed the SHA of the commit that contains the descriptor as a binding release identity. Such a field would be self-referential because changing the embedded SHA changes the commit content and therefore changes the SHA again.
4. A consuming Project MUST record the release tag and commit SHA that were actually resolved from the bootstrap source in Project-local provenance. The recorded SHA is observed provenance, not a predicted release SHA.
5. Mutable `main` is a discovery branch and MUST NOT be represented as equivalent to an immutable release tag.
6. If the stable release tag cannot be resolved, the agent MUST disclose the limitation. Bootstrap from mutable `main` MAY proceed only with explicit user approval and MUST preserve degraded provenance such as `VERIFICATION_REQUIRED` / mutable-source warning rather than fabricate immutable tag/SHA evidence.
7. Existing Projects MUST NOT retroactively invent an unobserved historical release SHA merely to look complete. They remain governed by their approved local pin and MUST NOT auto-upgrade when upstream advances.
8. Project Source Schema remains `1.0.0`; provenance is recorded in a machine-readable body block and Manifest continuation metadata rather than adding new mandatory front-matter keys.

## Canonical Provenance Model

For a normally resolved NEW bootstrap:

```yaml
framework_source_provenance:
  repository: "captainhuke-dev/ProjectFramework"
  release_tag: "v1.1.4"
  resolved_commit_sha: "<ACTUALLY_RESOLVED_40_HEX_SHA>"
  framework_version: "1.1.4"
  schema_version: "1.0.0"
  captured_at: "<ISO8601_WITH_TIMEZONE>"
```

The active `00-Project Source Framework` and `14-Project Source Manifest` MUST agree on this observed provenance. A mismatch is Project Source integrity drift and must be resolved rather than silently rewritten.

## Bootstrap Behavior

```text
read repository main entrypoint
→ read managing-project-source/FRAMEWORK-RELEASE.yaml
→ resolve stable_release_tag
→ verify the tagged source declares the expected Framework/Schema
→ read bootstrap source at that immutable tag
→ Preview → explicit user approval
→ create active 00 first
→ create mandatory 01–05 and 09–17; evaluate conditional 06–08
→ record release tag + resolved commit SHA locally
→ pin local Project Source
```

If immutable tag resolution is unavailable, stop the affected governance mutation, report the limitation, and obtain explicit user approval before any mutable-source bootstrap. Mutable-source provenance must remain visibly degraded until independently verified.

## Existing Projects and Migration

Existing Projects remain version-pinned. Adoption of Framework `1.1.4` uses the governed `MIG-*` flow when an upgrade is requested. Migration records provenance from the actual approved migration source ref; it does not fabricate historical provenance for earlier revisions.

## Non-Goals

This amendment does not add a general Project runtime validator, background automation, a release daemon, automatic tag creation, automatic branch protection, or automatic migration of existing Projects. Framework distribution integrity automation is separate Phase-B scope.

## Precedence

This `1.1.4` amendment is the latest binding clarification for release provenance and immutable bootstrap references. Framework `1.1.3` remains binding for platform Project launcher equivalence, `1.1.2` remains binding for bootstrap mockup semantics, and `1.1.1` remains binding for Materialized Current State, Stable-ID resolution, Manifest/CURRENT completeness, and archive independence.
