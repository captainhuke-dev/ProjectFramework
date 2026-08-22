---
law_id: CONST-022
version: 4.2.0
status: ACTIVE
derogation: FORBIDDEN
applies_when: ALWAYS
min_conformance: L1
---

# CONST-022 — Amendment, versioning, and migration

An AI agent MAY propose a constitutional amendment and MUST NOT unilaterally amend the Constitution.

Constitutional amendment requires explicit amendment intent, valid human constitutional authority, review, impact assessment, version decision, change record, and release identity.

Reference change classes:

```text
BREAKING
NON_BREAKING
CLARIFICATION
```

Stable law IDs MUST NOT be renumbered, reused, or reassigned. A repealed law keeps its ID and receives a repealed status.

A project remains governed by the version it pinned until authorized migration.

## Complexity and reading load

The Constitution MUST control reading load through modular laws, applicability, reading profiles, and measured size budgets rather than an arbitrary law-count ceiling.

Every release MUST report full normative bytes, unconditional bytes per reading profile, the largest laws, and change in mandatory boot load from the previous release.

An amendment that materially increases unconditional boot load MUST include a reading-load impact assessment and explicit approval.

## Generated-artifact integrity

The law files are canonical. Manifest, consolidated text, coverage index, release receipts, and size budgets are generated or derived artifacts.

After any normative change, the release process MUST regenerate affected derived artifacts and MUST run package validation before publication.

A manifest or template that disagrees with canonical law is defective. The disagreement MUST produce `PACKAGE_DRIFT` and block release of the affected package.

## Verification coverage and release maturity

Every `MUST` / `MUST NOT` requirement MUST have an identified verification method in the coverage index: scenario, inspection, runtime observation, process evidence, independent review, or registered verification gap.

A stable core release MUST pass structural, schema, reference-fixture, manifest, hash, and cross-file consistency validation. It MUST NOT claim that a particular agent/runtime is behaviorally certified unless that certification was run and recorded separately.

Agent and Project conformance are adoption-time certifications. A Project MUST run the scenarios required by its risk and operating profile before relying on an agent for material governed effects.

## Atomic publication

An effective release ref MUST NOT expose a partial package, broken front-door link, transport payload, or self-mutating assembly state.

The release process MUST build and validate outside the effective ref, construct one final tree or equivalent atomic artifact containing the front door and every linked target, and move the effective ref only after validation and freshness/predecessor checks pass.

A failed build, test, extraction, or validation MUST leave the prior effective ref unchanged. Temporary upload chunks, assembly workflows, probes, caches, and machine-local paths MUST NOT remain in the final release tree.

A publication workflow SHOULD be read-only with respect to the release after the ref update. A self-deleting or self-pushing workflow on the effective branch MUST NOT be used as the transport/assembly mechanism for the release it is publishing.

<!-- END_OF_LAW: CONST-022 version=4.2.0 sha256=bcd53809de18c9f216368c027d06f9820c0368fb54f4880f8290b8a580cee1b0 nonce=bcd53809de18 -->
