# FATHER-COST-ENGINEERING-001 — Economics & FinOps Gate v1.0

**Status:** PROPOSED / DOCUMENTED / NOT_IMPLEMENTED / NOT_QUALIFIED  
**Applies to:** IDEA+, FATHER Agent Factory, ALINA, FATHER_CODEX, Agent Fabric, RAG and multimodal pipelines.  
**Principle:** Optimize **cost per qualified outcome**, not just price per token, and never treat an assumed RAG multiplier as a measured constant.

## 1. Role in IDEA+

Insert a mandatory **ECONOMIC_GATE** into the IDEA+ feasibility assessment **before** Planning and implementation. The gate evaluates three options where relevant: LOCAL, CLOUD_API, HYBRID, and optionally MANAGED_SERVICE or PURCHASE. For each option declare:
- cost per request / task / book / image / video minute / accepted software feature (as applicable);
- CAPEX, OPEX, variable and fixed costs;
- workloads (per day/month, concurrency, peak RPS, latency targets, size of corpus, data retention);
- scenario estimates LOW / BASE / HIGH and worst-case budget ceiling;
- evidence (vendor URL, region, currency, timestamp, price unit, effective date, measured usage trace);
- sensitivity to model rates, retries, RAG top-k/context size, embedding refresh, failure and quality rates;
- hard financial limits and abort/approval thresholds.

**Stop condition:** if total projected cost exceeds a non-negotiable budget, the outcome is `NO_GO` or `CONDITIONAL_GO` after requirement reduction. Unknown costs must not be reported as zero.

## 2. Cost taxonomy

| Cost group | Required drivers |
|---|---|
| LLM inference | input/output/cache-write/cache-read tokens, model/provider/version, model routing, requests and retries |
| Agent orchestration | planning, routing, reflection, critics, tool calls, nested branches, context compression, failures |
| RAG | ingestion/parser/OCR, embeddings for documents and queries, chunking, dedupe, vector storage/index, retrieval, reranking, added generation context, updates |
| Persistence | source files, vector dimensions/dtype, indexes, snapshots, backups, replicas, GB-month, retention and restore |
| Compute | GPU/CPU/RAM hours, utilization, idle baseline, capacity reservation, autoscaling |
| Networking | ingress/egress, inter-region transfer, object store operations, third-party API fees |
| Multimodal | speech seconds/minutes, image counts/resolution, video seconds, transcoding, storage, evaluation |
| Engineering & operations | implementation, maintenance, monitoring, upgrades, incident response, human review |
| Security & quality | scanning, audit logging, evaluation datasets, independent POLYGON tests, compliance overhead |
| Hardware (local) | purchase, depreciation, electricity, cooling, maintenance, replacement and downtime |

## 3. Formulas and units

All prices are **parameterized**, never hardcoded as enduring facts.

```text
LLM_COST =
  input_tokens/1e6 * input_rate
  + output_tokens/1e6 * output_rate
  + cached_read_tokens/1e6 * cached_read_rate
  + cached_write_tokens/1e6 * cached_write_rate
  + other_provider_metered_costs

RAG_INCREMENTAL_COST =
  document_ingest + embeddings_document + embeddings_query
  + vector_storage + vector_search + reranking + added_context_inference
  + maintenance + backup + data_transfer
  - demonstrable savings (if any)

MONTHLY_TCO =
  LLM_COST + RAG/agent/tool/multimodal variable charges
  + infrastructure + staff/support + security/qualification + amortized_CAPEX
  + tax/FX adjustments where applicable

COST_PER_QUALIFIED_RESULT =
  total_cost_of_complete_attempts / independently_accepted_results
```

**Important:** define whether `input_tokens` includes cached portions before using the formula; avoid double charging token categories. If no accepted results, `COST_PER_QUALIFIED_RESULT` is undefined / infinite, never zero. Record the denominator explicitly.

The RAG example “2–3x tokens” is a **hypothesis**, not a constant. A RAG pipeline may increase input context but also reduce follow-up requests, lower failure rates or enable cheaper models; measure baseline and full workflow. Query ingestion and index-storage costs can be fixed/periodic while contextual retrieval costs are per request.

### Example: hypothetical rates only
- Rate: input $1 / 1M tokens; output $3 / 1M tokens.
- Baseline: 1,000 input + 300 output tokens: $0.0019 per request.
- RAG: 3,000 input + 300 output tokens: $0.0039 per request.
- At 100,000 requests: $190 vs $390 **for LLM token billing only**, about 2.05x; embeddings, infrastructure, storage, validation and retrieval excluded.

Do **not** present these hypothetical rates as a vendor's current price.

## 4. Data model / price provenance

```yaml
cost_estimate_id: COST-0001
project_id: IDEA-0001
as_of_utc: null
currency: USD
region: null
scenario: BASE
provider: null
model_version: null
pricing_sources:
  - url: null
    observed_at_utc: null
    price_unit: null
workload:
  requests_per_month: null
  input_tokens_p50: null
  input_tokens_p95: null
  output_tokens_p50: null
  output_tokens_p95: null
  rag_context_tokens_p50: null
  rag_context_tokens_p95: null
  requests_per_accepted_result: null
  storage_gb_month: null
  gpu_hours: null
line_items: []
monthly_tco: null
cost_per_qualified_result: null
confidence: UNKNOWN
status: NOT_MEASURED
```

Never include credentials, tenant-sensitive billing data or secret price agreements in a public repository.

## 5. Economic decisions and tests

Compare:
1. Basic LLM, no RAG / no multi-agent;
2. Minimal RAG, controlled top-k, selective reranking;
3. Multi-agent with bounded loops and strict budgets;
4. Local, cloud and hybrid infrastructure.

Mandatory benchmarks under matched workload:
- response correctness and independently verified task success;
- latency p50/p95, tokens p50/p95, call counts, tool cost, token spend;
- retries, errors, guardrail failures and work rejected by humans;
- storage-growth projection and backup/egress costs;
- `cost_per_qualified_result`, total monthly cost under LOW/BASE/HIGH usage;
- price shock (e.g. +50%), double usage, cost cap breach, runaway recursive calls;
- validation that cached token accounting, rate cards and region/currency are current.

Required budget controls: per-call max tokens, per-task and per-day budget, agent step/retry limit, expensive-tool authorization, anomalous-spend alerts, explicit `BUDGET_EXCEEDED`, no unauthorized fallback to an expensive cloud model.

## 6. Vendor references (sources, not permanent tariff values)

- OpenAI API pricing: https://developers.openai.com/api/docs/pricing
- OpenAI prompt caching: https://developers.openai.com/api/docs/guides/prompt-caching
- AWS S3 pricing (storage + operations + transfer): https://aws.amazon.com/s3/pricing/
- AWS Bedrock pricing: https://aws.amazon.com/bedrock/pricing/
- AWS generative AI application cost guide: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/cost.html

All vendor rates must be looked up and recorded with region/time **at calculation time**. No blanket claims that RAG, cloud or local operation is always cheaper.

## 7. Minimum outputs

- `COST_MODEL`: measured/estimated breakdown by service and operation;
- `TCO_COMPARISON`: LOCAL vs CLOUD_API vs HYBRID at selected horizon;
- `ECONOMIC_DECISION`: ADOPT / CONDITIONAL / RESEARCH / REJECT;
- `BUDGET_POLICY`: limits, monitors, anomalies and escalation;
- `COST_EVIDENCE`: usage trace, provider tariff snapshots and independent quality results.

**Readiness:** A design document alone does not implement metering or billing. The economic gate becomes operative only after usage instrumentation, regression tests and comparative measurements have evidence.
