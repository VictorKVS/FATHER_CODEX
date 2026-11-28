# FT-PLAN-001 — План развития Test Factory
**Оценки трудозатрат не утверждены.** Выполнение фиксируется только по доказательствам.

| Milestone | Что сделать | Evidence / exit gate | Status |
|---|---|---|---|
| TF-M0 | Реестр книг/стандартов, строгий формат тест-кейса, валидатор каталога, unit-tests | checked-in schema, 1 complete DESIGN case, CLI PASS, release denied | LOCAL IMPLEMENTATION — awaiting Windows confirmation |
| TF-M1 | Паспорта API-001..003 + согласование ПМИ для SADEQ, traceability и fixtures | reviewed methods, fixed 401/403/404 policy, complete negative assertions | NOT_DONE |
| TF-M2 | Adapter pytest/httpx + test auth issuer + DB/ITSM snapshot | true API negative tests + logs before/after + repeatability | NOT_DONE |
| TF-M3 | adapters Semgrep/Bandit/Trivy/Gitleaks/ZAP + SARIF & SBOM | version-pinned local tools, safe scans and issue register | NOT_DONE |
| TF-M4 | RAG/LLM/multi-agent eval sets + injection/tool-policy and provenance | measured metrics and holdout boundaries | NOT_DONE |
| TF-M5 | Orchestrator Docker/WSL, structured logs, resource controls, offline mode | isolated reproducible integration run | NOT_DONE |
| TF-M6 | evidence ledger, change reviews, signatures, provenance | verifiable SHA, retained fails, signed release manifest | NOT_DONE |
| TF-M7 | independent POLYGON bridge + read-only artifacts | independent replay and human decision | NOT_DONE |

**First pilot SADEQ:** API-001 tenant isolation, API-002 JSON schema/duplicates, API-003 authenticated positive ingest — only after reviewed exact HTTP/body/error and database postconditions. We do not weaken security requirements to make tests pass.
