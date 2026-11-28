# M2 — SADEQ API-001: готовность к реальным испытаниям
**Status:** PRECONDITIONS_INCOMPLETE / NO TEST RUN.

## Постановка
First independent lab API security test is BOLA and forged tenant identity. The already registered method is `catalog/cases/SADEQ_API_001.json`, linked to PМИ-002 in SADEQ project, the project Contract-Strict SI-01/02/03 and the source registry. Do not change expected behavior to retrofit the legacy demo API.

## Ready-to-run prerequisite register
| ID | Item | Current status | Verification needed |
|---|---|---|---|
| M2-P01 | Approve ПМИ-002 as baseline | PENDING | authorized named owner + revision/signoff |
| M2-P02 | Approve exact API endpoint and HTTP deny code, response envelope and tenant scoping | PENDING | OpenAPI 3.1 + JSON Schema + frozen example |
| M2-P03 | Start isolated local API, no prod/unknown targets | NOT_RUN | local service process and healthcheck |
| M2-P04 | Test IdP with signed tenant A/B identities, issuer/audience/exp checks; no X-Demo identity | NOT_IMPLEMENTED | good/expired/wrong-aud fixtures |
| M2-P05 | Separate A/B tickets with same external ID; immutable initial fingerprints | NOT_RUN | seeded DB snapshot, checksum |
| M2-P06 | Independent audit and mock ITSM call counters | NOT_IMPLEMENTED | before/after check |
| M2-P07 | Git/build/dependency/policy/schema/dataset SHA256 manifest | NOT_RUN | manifest written before execution |
| M2-P08 | Human security reviewer and independent test executor | NOT_ASSIGNED | recorded role/identity |
| M2-P09 | Offline/sandbox network allowlist and secrets redaction | NOT_VERIFIED | lab network rules, test transport |

**Rule:** any absent prerequisite → `BLOCKED`, not PASS/FAIL of SADEQ security.

## Execution sequence once approved
- Seed fixtures and store pre-run hashes.
- Perform authorized subject A read on A resource; examine property ACL.
- Use verified token A to attempt read B resource and forged tenant header/body; verify endpoint-specific exact denial and no data disclosure.
- Attempt invalid/expired/wrong audience credentials; verify 401 and no effects.
- Attempt unauthorized proposal/approval for B; verify no B05/ITSM call.
- Compare B state hashes, versions, event counters and independently observed tool counters.
- Validate redacted policy audit denial, no secret logs.
- Persist individual TEST-ID protocol + HTTP, DB, AUDIT, TOOL_COUNTER, RUN_MANIFEST hashes.
- Independent POLYGON re-examination only on frozen candidate and heldout fixtures; human release signoff separate.

## Engineering acceptance rule
M2 cannot begin code-based tests as a qualification while the actual API has unverified demo auth and missing signed token claims. The current M1 proof of catalog rejection is separate from runtime evidence. Start M2 by **freezing the endpoint/auth contract and approving the test method**. Then implement the tests, then align API source until GREEN without relaxing expected security properties.

[Existing case](../catalog/cases/SADEQ_API_001.json) · [M1 Windows evidence](../evidence/M1_WINDOWS_2026-11-28.md).
