# Universal AI Agent Constitution 5.0

UAAC is a universal, locally readable constitutional layer for accountable Human–Agent and Agent–Agent work.

## Production boundary

This directory is the complete UAAC 5.0 production distribution. It contains only Markdown and YAML. A Project does not need Python, a validator, a background service, a retrieval system, a native Skill runtime, CI, or network access to adopt and operate under UAAC.

Operational constitutional requirements live only in [`laws/`](laws/). The [Constitution entrypoint](UAAC-v5.0-CONSTITUTION.md) provides identity, precedence, navigation, version, and the law index.

## Install

Start with [INSTALL-UAAC.md](INSTALL-UAAC.md). The normal Project route is:

```text
persistent launcher
→ governance/UAAC.md
→ governance/UAAC-ADOPTION.yaml
→ locally vendored UAAC-v5.0-CONSTITUTION.md
→ bounded materially required Project sources
→ work
```

Project rules are conditional. Reuse real rules when they exist; create a rules source only when the Project actually has rules.

Installing UAAC does not install or upgrade ProjectFramework.

## Non-normative material

- [Adoption guide](ADOPTION-GUIDE.md)
- [Migration from 4.2](MIGRATION-v4.2-TO-v5.0.md)
- [Templates](templates/)
- [Optional profiles](profiles/)
- [Navigation manifest](LAW-MANIFEST.yaml)
- [Release metadata](CONSTITUTION-RELEASE.yaml)
- [Changelog](CHANGELOG.md)

Profiles are optional and non-normative. Presence on disk does not activate them or create authority.
