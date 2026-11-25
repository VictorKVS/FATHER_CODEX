# FATHER-IDEA-PLUS-001 — IDEA+ Protocol v1.0

**Status:** PROPOSED / DOCUMENTED / NOT_IMPLEMENTED / NOT_QUALIFIED  
**Scope:** all new FATHER projects, agents, modules, services and substantive enhancements  
**Owner:** FATHER Engineering Platform  
**Principle:** Investigate before planning. Reuse before building. Verify before declaring ready.

> An idea does not authorize implementation. Planning starts only after feasibility and evidence gates.

## 0. Purpose

Convert an idea expressed in natural language into a **feasibility-checked, source-grounded and reusable engineering proposal** before committing resources to design or development.

The protocol asks:
1. What must the end product actually accomplish, and how will acceptance be measured?
2. Which existing FATHER / ALINA / FATHER_CODEX / Agent Fabric components can already solve parts of the task?
3. Which interfaces and contracts must be satisfied to compose them?
4. Who has solved comparable problems worldwide, by which algorithms, models and architectures?
5. Are there published, maintainable, legally usable implementations (GitHub, Hugging Face, vendor SDKs, standards)?
6. Can the desired result be achieved **now**, on available resources, at the required quality, cost and security level?
7. What is the least expensive experiment that can disprove the riskiest assumption?
8. What might the next technology generation enable, and what measurable signals would justify reassessment?

## 1. Decision sequence

```text
IDEA + intended product
  -> IDEA_CONTRACT (requirements + acceptance criteria)
  -> INTERNAL_SCOUT (our existing code, components, evidence)
     + WORLD_SCOUT (papers, benchmarks, public code, standards)
  -> REUSE_MATRIX + WORLD_SOLUTION_MATRIX
  -> COMPATIBILITY_GAP_ANALYSIS + BUILD_VS_BUY_VS_REUSE
  -> COMPOSITION_BLUEPRINT (typed interfaces, integration, dependencies)
  -> FEASIBILITY_GATE (GO / CONDITIONAL_GO / RESEARCH / NO_GO)
  -> TECHNOLOGY_ROADMAP (evidence-based triggers for next generation)
  -> PLANNING -> BUILD -> VERIFY -> POLYGON -> RELEASE
```

**No unconditional automatic transition into Planning.** `GO` and `CONDITIONAL_GO` must specify the allowed scope; `RESEARCH` authorizes a bounded experiment, not a production commitment; `NO_GO` records which requirements fail and why. A `NO_GO` verdict means *not feasible under the stated constraints*, not necessarily impossible in principle.

## 2. Phase contracts

### P0 — IDEA / Requirements Engineering
**Input:** free-form idea, intended user, success condition, constraints.  
**Steps:** normalize the goal; identify required vs negotiable properties; enumerate outputs, negative cases, legal/security limits, cost/time budget, autonomy level; identify missing assumptions and failure criteria.  
**Output:** `IDEA_CONTRACT`: objective, target artifacts, measurable acceptance tests, assumptions, hard constraints, unknowns, decision owner.

### P1 — INTERNAL_SCOUT / Reuse Audit
**Input:** IDEA_CONTRACT and access to authorized repositories and project evidence.  
**Steps:** search FATHER modules, ALINA, FATHER_CODEX, Agent Fabric, OSINT and related projects; inspect code **and** contracts, versions, commits, dependencies, licenses, tests, integration reports, security boundaries. Do not infer readiness from a README or the mere presence of code.  
**Output:** `REUSE_MATRIX` with `component_id, repository, path, commit, purpose, interfaces, dependencies, evidence_refs, qualification_status, fit, required_adapters`.

### P2 — WORLD_SCOUT / Prior Art
**Input:** IDEA_CONTRACT and problem decomposition.  
**Sources (as appropriate):** primary papers (arXiv/publishers), GitHub, Hugging Face, vendor docs/release notes, standards, Stanford AI Index, METR, MLCommons, Epoch AI, Artificial Analysis, NIST. Follow licenses, APIs and rate limits.  
**Steps:** identify algorithms and architectures; distinguish paper, demo, production claim and independent reproduction; collect benchmark methodology, dataset, hardware, runtime, versions, date, cost, known failures, maintenance/issue history and evidence of actual code availability. Record conflicting findings.  
**Output:** `WORLD_SOLUTION_MATRIX` with URLs and retrieval timestamps. Never fabricate source metrics or links.

### P3 — BUILD_VS_BUY_VS_REUSE
Compare: existing internal implementation, internal adaptation, third-party integration, new build, bounded research and rejection. Evaluate fitness, integration cost, security, legal/commercial licenses, support, lock-in, operating cost and alternatives. A license or hard safety restriction is a **gate**, not a negotiable weighted score.

### P4 — COMPOSITION / Compatibility & Gap Analysis
**Output:** `COMPOSITION_BLUEPRINT` including:
- component graph with proven or proposed nodes clearly marked;
- typed input/output and data contracts, version constraints, ownership;
- identity, tenant, role and tool authorization boundaries; secrets policy;
- adapters, queues, retries, timeouts, idempotency and rollback;
- observational evidence from end-to-end tests, or a precise `NOT_TESTED` status;
- unresolved gaps, conflicts and risks.

Prefer a simple verified function over multi-agent machinery unless the latter supplies measurable benefit.

### P5 — FEASIBILITY GATE
For each hard requirement answer:
- Are there reproducible comparable outcomes?
- Are the required algorithms/models/services usable and licensed?
- Can the target hardware/infrastructure reach the necessary latency, throughput, quality and cost?
- What evidence supports the answer? What is unknown?
- What minimal *falsifiable* experiment tests the highest-risk assumption?
- Is the solution maintainable and safe for its application domain?

Verdict:
- **GO:** necessary constraints satisfied with adequate, reproducible evidence.
- **CONDITIONAL_GO:** feasible only with explicit scope restrictions or human review.
- **RESEARCH:** insufficient evidence; define a time/cost-bounded PoC and stop conditions.
- **NO_GO:** mandatory constraint fails; document blocker and alternate requirement sets.

A successful single demo is insufficient to declare GO for production.

### P6 — TECHNOLOGY FORECAST
Separate `OBSERVED`, `INFERRED` and `FORECAST`; identify current bottlenecks, candidate next-generation approaches, plausible implications, uncertainty, and **observable reassessment triggers** (new releases, independently repeated benchmark thresholds, cost reductions, safety qualifications, hardware improvements). Forecast dates are hypotheses, not commitments. Design replaceable adapters where credible benefits justify it.

### P7 — PLANNING / Execution Admission
Only after the gate: choose the minimal viable architecture; generate ADRs, component/data/security/qualification contracts, work breakdown, dependency graph, acceptance tests, budgets, human-approval points, evidence collection plan. If `RESEARCH`, only plan the approved experiment.

### P8 — VERIFY / POLYGON / Release
Acceptance requires appropriate unit, integration, regression, security and operational tests; traceability from each critical requirement to evidence; provenance; independent qualification with held-out POLYGON cases; approval for consequential actions. No status `READY` without evidence.

## 3. Decision records

### Artifact list
| ID | Document | Mandatory evidence |
|---|---|---|
| IDEA_CONTRACT | Goals / constraints / acceptance criteria | Requirement owner and version |
| REUSE_MATRIX | Existing FATHER building blocks | Repository, path, commit, interfaces, tests |
| WORLD_SOLUTION_MATRIX | World experience and GitHub analogues | Primary URL, date, versions, benchmarks |
| BUILD_VS_BUY_VS_REUSE | Option comparison | Score method, hard-gate reasoning, licenses |
| COMPOSITION_BLUEPRINT | Interaction of selected blocks | Contracts, dataflows, security, failure paths |
| FEASIBILITY_REPORT | GO / CONDITIONAL_GO / RESEARCH / NO_GO | Experiment, metrics, blockers, evidence |
| TECHNOLOGY_ROADMAP | Current and possible next stage | Observations, forecasts, reassessment triggers |
| PRODUCT_EVIDENCE_PACKAGE | Qualification and release | Test logs, commit/tag, SHA-256, SBOM/provenance |

### Component decisions
`REUSE` — proven fit; `ADAPT` — own code needs changes; `INTEGRATE` — external component meets licensing, contract and test gates; `BUILD` — missing, feasible to implement; `RESEARCH` — uncertainty needs an experiment; `REJECT` — unacceptable constraints.

### Evidence hierarchy
`CLAIM` (promotional or unverified) < `DOCUMENTED` (paper/vendor specification) < `REPRODUCED` (specified experiment) < `INDEPENDENTLY_VERIFIED` (independent or held-out evaluation). Evidence strength is always **claim- and context-specific**. Claims from external sources are untrusted until verified.

## 4. Example — ALINA narrative analysis
| Need | Existing FATHER asset | Decision / open gap |
|---|---|---|
| PDF/FB2 ingestion and provenance | ALINA ingestion and SQLite/FTS5 | REUSE for tested ingestion, verify actual source coverage |
| LLM abstraction | ModelAdapter, Ollama | ADAPT to typed narrative extraction and runtime tests |
| Literary methods | ALINA Narrative Theory KB NAR-001..005 | RESEARCH: structure validated; source semantics not qualified |
| Revision loop | CH04 Reflection demo | ADAPT: independent evidence tests needed |
| Tool calls | CH05 Tool Use demo | ADAPT: real permissions, trace and negative tests |
| Story graph | ALINA architecture proposals | RESEARCH / BUILD after contracts and review |
| Claim evidence | quote presence checks | ADAPT: presence alone does not entail truth |
| Expert qualification | POLYGON concept | BUILD independent held-out evaluation |

This table is an illustrative **snapshot**, not a production qualification.

## 5. Protocol invariants
1. Search internal and external prior art **before writing new code**.
2. Use an algorithm only with a traceable source or justified internal invention.
3. Check interface compatibility before claiming reuse.
4. Never substitute a model's confidence or critique for independent verification.
5. Keep source facts, interpretations and forecasts separate.
6. Do not turn READ/RESEARCH permission into WRITE/EXECUTE permission.
7. Keep human commits, ADRs, component/data/security/qualification contracts, SHA-256/provenance, signed release commits/tags when applicable, tests and evidence, ownership metadata and SBOM/build provenance.
8. Never publish protected book texts, credentials, confidential project data or protected test sets.
9. Never say `DONE`, `READY`, `VERIFIED` or `QUALIFIED` without corresponding proof.
10. Record unresolved gaps as explicit `UNKNOWN`; allow human review and bounded experimental exceptions.

## 6. Implementation status and next actions
This document creates a **protocol specification only**. It does not implement OSINT collectors, GitHub inventory adapters, automated feasibility judgment, planning gates or POLYGON.

Recommended first increment: manual or assisted `IDEA_CONTRACT + REUSE_MATRIX + WORLD_SOLUTION_MATRIX + FEASIBILITY_REPORT` for one contained use case, with source URLs and a reproducible test. Automate only steps that prove value and pass verification.

**Change control:** future revisions should include an ADR if modifying status semantics, phase ordering, minimum evidence or policy boundaries.
