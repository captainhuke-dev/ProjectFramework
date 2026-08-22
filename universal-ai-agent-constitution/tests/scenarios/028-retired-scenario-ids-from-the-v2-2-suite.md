# Retired scenario IDs from the v2.2 suite

Eleven v2.2 scenarios test the same behaviour as a scenario in the merged suite. They are
retired rather than deleted, and each is mapped, so that a reference to a v2.2 ID resolves
rather than going missing. Where the two versions differed, the note says which text
survived.

| v2.2 ID | Now | Note |
|-|-|-|
| `S-READ-01` | `S-CMP-01` | equivalent; merged text keeps the coverage-state vocabulary |
| `S-INP-01` | `S-INS-01` | equivalent; merged text adds the quote-and-name-the-source duty |
| `S-HO-01` | `S-XFR-03` | equivalent; merged text adds the void-on-drift arm |
| `S-HASH-01` | `S-SUB-02` | equivalent |
| `S-WIKI-01` | `S-KNW-02` | equivalent |
| `S-CAP-01` | `S-CNF-01` | equivalent; `S-CNF-04` now covers the opposite direction |
| `S-EXT-01` | `S-MEM-02` and `S-DEP-01` | v2.2 tested one case; the merged suite splits identity-from-label from pin-to-mutable |
| `S-DEC-01` | `S-DEC-01` | ID retained; merged text keeps both arms and adds the criteria-provenance requirement |
| `S-DEC-02` | `S-DEC-02` | ID retained |
| `S-ABR-01` | `S-COM-01` | equivalent; `S-COM-02` covers the summarize-is-allowed direction |
| `S-REV-01` | `S-DEC-05` | equivalent; merged text adds the recorded-initial-review requirement |

---
