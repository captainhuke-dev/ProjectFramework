# Project Source Bootstrap Mockup

This directory is the concrete starter representation of the Project Source semantic namespace for **Framework 1.1.4 / Schema 1.0.0**. Use it to answer: **“เลขไหน คือเรื่องอะไร และ starter file ชื่ออะไร?”**

> **Authority:** This mockup is executable documentation. `../../references/core-governance-rules.md`, the active `00-Project Source Framework`, and `../core-document-skeletons.md` are normative. If this mockup disagrees with Core Governance, Core Governance wins and the mockup mismatch is release-blocking drift.

## Core Slot Map

| Slot | Document | Applicability | Distribution starter |
|---|---|---|---|
| `00` | Project Source Framework | **MANDATORY / NON-REMOVABLE ROOT** | `00-Project-Source-Framework.template.md` |
| `01` | Project Source Index | **MANDATORY** | `01-Project-Source-Index.template.md` |
| `02` | Project Overview | **MANDATORY** | `02-Project-Overview.template.md` |
| `03` | Current State | **MANDATORY** | `03-Current-State.template.md` |
| `04` | Decision Log | **MANDATORY** | `04-Decision-Log.template.md` |
| `05` | Requirements | **MANDATORY** | `05-Requirements.template.md` |
| `06` | Architecture | **CONDITIONAL** | `06-Architecture.template.md` |
| `07` | Implementation Plan | **CONDITIONAL** | `07-Implementation-Plan.template.md` |
| `08` | Open Issues | **CONDITIONAL** | `08-Open-Issues.template.md` |
| `09` | Handoff | **MANDATORY** | `09-Handoff.template.md` |
| `10` | Change Log | **MANDATORY** | `10-Change-Log.template.md` |
| `11` | Actor Registry | **MANDATORY** | `11-Actor-Registry.template.md` |
| `12` | Authorization Registry | **MANDATORY** | `12-Authorization-Registry.template.md` |
| `13` | Evidence Registry | **MANDATORY** | `13-Evidence-Registry.template.md` |
| `14` | Project Source Manifest | **MANDATORY** | `14-Project-Source-Manifest.template.md` |
| `15` | Action Registry | **MANDATORY** | `15-Action-Registry.template.md` |
| `16` | Migration Registry | **MANDATORY** | `16-Migration-Registry.template.md` |
| `17` | Secret Reference Registry | **MANDATORY** | `17-Secret-Reference-Registry.template.md` |

## Reserved and Extended Taxonomy

| Range | Meaning | Bootstrap behavior |
|---|---|---|
| `18–19` | RESERVED | **DO NOT CREATE** default/active files |
| `20–29` | Research / Discovery | Create only when needed |
| `30–39` | Business / Process / UX Design | Create only when needed |
| `40–49` | Architecture / Technical / Integration | Create only when needed |
| `50–59` | Testing / QA / Validation | Create only when needed |
| `60–69` | Deployment / Operations / Infrastructure | Create only when needed |
| `70–79` | Data / Migration / Analytics | Create only when needed |
| `80–89` | Audit / Review / Assessment / Reports | Create only when needed |
| `90–99` | Project-specific / Governance Extension | Create only when needed |

Reserved anchors remain: `20 General Research`, `30 Business Flow`, `40 Technical Design`, `50 Test Strategy`, `60 Deployment Plan`, `70 Data Model`, `80 Review Report`, `90 Special Governance Extension`.

## GREENFIELD Bootstrap Recipe

```text
1. If running inside a platform Project, start from the canonical ChatGPT/Claude Project instruction artifact
2. Read repository README.md on the discovery branch
3. Read ../../FRAMEWORK-RELEASE.yaml
4. Resolve stable_release_tag and use the immutable tagged source for normal bootstrap
5. Read SKILL.md + latest amendment + Core Governance from the resolved source
6. Read 00 template + core-document-skeletons.md
7. Read this mockup mapping
8. Preview proposed Project Source → obtain explicit user approval
9. Create active 00 first
10. Create mandatory 01–05 and 09–17
11. Evaluate 06–08; create active files only when applicable
12. Keep 18–19 reserved
13. Add 20–99 only for real project-specific needs
14. Record observed release tag + resolved commit SHA in active 00 and Manifest provenance metadata
15. Build/verify Index + Manifest + readiness
16. Pin Framework/Schema locally; do not auto-upgrade from upstream later
```

If the immutable release tag/source cannot be resolved, do not pretend mutable `main` is immutable. Report the limitation; mutable-source bootstrap requires explicit user approval and must keep provenance `VERIFICATION_REQUIRED` / visibly degraded until verified.

## Template vs Active Filename

The files in this directory intentionally end in `.template.md`. **Do not copy those names verbatim into an active Project Source.** Governed active documents use revision + timestamp naming, for example:

```text
00-Project Source Framework-r001-YYMMDD-HHMM.md
01-Project Source Index-r001-YYMMDD-HHMM.md
05-Requirements-r001-YYMMDD-HHMM.md
```

The template files contain placeholders, not project facts. Replace placeholders only with verified/user-confirmed values or explicit epistemic states such as `UNKNOWN`, `ASSUMED`, `STALE`, or `VERIFICATION_REQUIRED`.

## Conditional Does Not Mean Pre-create

`06 Architecture`, `07 Implementation Plan`, and `08 Open Issues` have starter templates so agents can discover the expected structure **if/when applicable**. Their presence here MUST NOT be interpreted as permission to create empty active documents merely to make a project tree look complete.
