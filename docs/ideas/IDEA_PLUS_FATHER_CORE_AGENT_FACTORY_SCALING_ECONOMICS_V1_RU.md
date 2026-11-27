# FATHER IDEA+ · 2026-11-27 · IDEA-AGF-001
## FATHER CORE & AGENT FACTORY — универсальное аналитическое ядро и фабрика проверяемых агентов

**Статус:** IDEA+ / RESEARCH / DESIGN PROPOSAL; **НЕ РЕАЛИЗОВАНО и НЕ КВАЛИФИЦИРОВАНО**.  
**Решение о запуске:** только после IDEA+ feasibility gate.  
**Владелец идеи:** FATHER Engineering Platform.  
**Связанные стандарты:** [FATHER_IDEA_PLUS_PROTOCOL_V1](../protocols/FATHER_IDEA_PLUS_PROTOCOL_V1.md), [FATHER_COST_ENGINEERING_PROTOCOL_V1](../protocols/FATHER_COST_ENGINEERING_PROTOCOL_V1.md).  
**Контекст:** выпускной проект OTUS AI-архитектор; on-prem / air-gapped, без внешних API; графовый RAG, LangGraph/state machine, C4 L1–L4, Deployment, Sequence, ER, Security, FinOps и измеримый MVP.  
**Миссия:** *из одного проверенного ядра создавать специализированных агентов путём настройки предметных контрактов, знаний, алгоритмов, полномочий и средств оценки, а не копированием кода*.

> Публичная формулировка для CTO: «Одна автономная платформа. Разные отраслевые агенты. Подтверждённые ответы, контролируемые действия и проверяемая стоимость каждого результата».

### 0. IDEA_CONTRACT — что обязана делать система

**Входы:** документы, изменения в БД, ERP/CRM/МИС (только с разрешением), события, сообщения и локальные файлы.  
**Общий конвейер:** `INGEST → EXTRACT / PROVENANCE → KNOWLEDGE GRAPH + VECTOR → STATE/EVENT → REASON / FORECAST → POLICY / APPROVAL → ACTION → FEEDBACK / EVALUATION`.  
**Выходы:** ответ с источниками; анализ состояния; проверяемый прогноз (алгоритм + интервал/неопределённость); предложение реакции; при санкционированном исполнении — результат инструмента и запись аудита.  
**Обучение в MVP:** расширение и уточнение проверенной БЗ, тестов и правил на основе обратной связи; **не fine-tuning LLM**, не автоматическое изменение критических правил.  
**Запрет:** агент не назначает себе права и не получает доступ к данным через prompt.  
**Области расширения:** медицина — операционная аналитика без медицинских диагнозов; торговля — спрос/остатки; ИБ/OSINT — исследовательская аналитика; игры — NPC/симуляции; учебная или логистическая военная область — без автономного боевого применения/целеполагания.
**Цель масштабирования:** уметь **зарегистрировать 20 декларативных спецификаций агентов** и независимо квалифицировать минимум **3 действительно разных** домена в MVP. Количество 20 — цель эксперимента, **не измеренная производительность фабрики**.

### 1. Критерии принятия идеи

| ID | Обязательное условие | Как докажем |
|---|---|---|
| REQ-01 | Все операции исполняются в замкнутой сети | deny-all egress + запись DNS/сетевого трафика + сборка из локального зеркала |
| REQ-02 | Реальный GraphRAG, а не только vector search | узлы/ребра в Neo4j, traversals + citations, сравнительные тесты с vector-only |
| REQ-03 | Stateful orchestration | граф LangGraph с ветвлениями, retry, stop, checkpoint и человеческим подтверждением |
| REQ-04 | Tenant / document isolation | User B не читает секретный документ через API, поиск, граф, цитаты, кэш, логи |
| REQ-05 | Контрактное разделение цехов | JSON Schema / OpenAPI для границ сервисов, внутренние typed interfaces |
| REQ-06 | Реакция подконтрольна | read-only by default; write/execute only allowlisted tools + approvals + audit |
| REQ-07 | Прогнозы воспроизводимы | baseline модели прогнозирования, holdout / backtesting, погрешность и неопределённость |
| REQ-08 | Экономика измерена | cost per accepted result, TCO LOW/BASE/HIGH, CAPEX/OPEX, пределы |
| REQ-09 | У каждого релиза есть evidence | test outputs, SHA-256, signed commits/tags, SBOM, model/data provenance |
| REQ-10 | Система масштабируется без копии core | 3 разных agent specs, общие компоненты, доля reuse и измеренное время добавления |

**Важно:** 20 конфигураций не равно 20 сертифицированных профессиональных агентов; это разные уровни готовности.

### 2. P1 · INTERNAL_SCOUT — реестр повторного использования (документация, не факт квалификации)

| Узел | Где искать | Первичное решение | Требуемое доказательство |
|---|---|---|---|
| FATHER CODEX / Agent Factory | VictorKVS/FATHER_CODEX | ADAPT: контракты и процесс QA | код, commit, интеграционные тесты |
| ALINA Analytical / Knowledge Worker | VictorKVS/alina-knowledge-worker | ADAPT: ingest, знания, RAG | корректность источников, качество retrieval |
| Agent Fabric / UAG | FATHER проекты | RESEARCH: security policy boundary | negative access tests + logs |
| POLYGON qualification | FATHER проекты | BUILD/ADAPT | независимые held-out test suites |
| OSINT / TIMA | FATHER проекты | RESEARCH: инструменты-адаптеры | policy + provenance + reproducibility |

**Ни один узел не объявляется REUSE-ready, пока не проверены реальный интерфейс, версия, лицензия и тесты.**

### 3. P2 · WORLD_SCOUT — решения, не изобретать заново

| Предмет | Кандидат / алгоритм | Исследование, которое нужно провести |
|---|---|---|
| State machine | LangGraph checkpoints, tools, human-in-the-loop | совместимость, лицензия, наблюдаемость, эксплуатация |
| Retrieval | Qdrant vector search + ACL filters | recall@k, filter bypass, масштаб индекса |
| Knowledge graph | Neo4j local property graph | схема 4 типа узлов, source provenance, обрезка разрешённого подграфа |
| Inference | Qwen3 4B/8B Q4 + llama.cpp/Ollama для потребительской GPU; vLLM для поддерживаемого Linux Serving | VRAM, KV-cache, latency/tokens/s и лицензии конкретного чекпойнта |
| Evaluation | RAGAS / DeepEval / собственные эталоны + POLYGON | независимая оценка, отсутствие утечек из тестовых наборов |
| API | OpenAPI, FastAPI, typed data contracts | негативные тесты и совместимость версий |
| Metrics | OpenTelemetry, Prometheus/Grafana | cost/task, latency, tokens, span + cross-service trace |

**Источники для проверки версий:** https://docs.langchain.com/oss/python/langgraph/overview ; https://qdrant.tech/documentation/manage-data/multitenancy/ ; https://docs.vllm.ai/en/latest/ ; https://www.finops.org/framework/ ; https://owasp.org/API-Security/ ; https://modelcontextprotocol.io/specification/  
**Ограничение:** список кандидатов — не принятие лицензий и не подтверждение работы на текущем оборудовании.

### 4. P3 · BUILD vs REUSE vs INTEGRATE

| Стратегия | Преимущество | Цена / риски | Решение |
|---|---|---|---|
| 20 независимых агентов | каждая реализация максимально свободна | дублирование кода, 20 наборов ошибок, дорого поддерживать | **REJECT как базовый метод** |
| Один универсальный огромный агент | минимальная начальная сборка | плохая изоляция полномочий, нет надёжной квалификации специализаций | **REJECT** |
| Общий core + декларативные skill packs | переиспользование, единый QA и безопасность | первоначальная платформа дороже первого агента | **RESEARCH → CONDITIONAL_GO на MVP** |
| Покупка proprietary agent SaaS | потенциально быстро | нарушает air-gapped, лицензирование и контроль | **NO_GO по обязательному офлайн-требованию** |

### 5. P4 · COMPOSITION_BLUEPRINT

```text
                     ┌──────────────────────┐
 User / Events / Docs │  API + Identity      │
           ──────────►│  UAG / Policy       │
                     └──────────┬───────────┘
                                ▼
                  CONTROL PLANE / LangGraph
                    ├─ Intake & Planner
                    ├─ State / Event Analyzer
                    ├─ Tool policy & Approval
                    └─ Evaluation / Feedback
                                │ typed contracts
                                ▼
                   DATA / INFERENCE PLANE
                    ├─ Local Qwen serving
                    ├─ Qdrant + Neo4j
                    ├─ PostgreSQL + audit
                    ├─ Verified algorithm toolbox
                    └─ Document/object storage
                                │
                                ▼
                     Evidence + Audit → Result
```

- **Стандарт Agent Specification:** `id, version, mission, input_contract, output_contract, ontology, knowledge_sources, state_schema, event_rules, planner_policy, model, tools, autonomy, risk_tier, approval_policy, test_suite, cost_budget`.
- **Цех / Component Contract:** `trigger, input, output, algorithm_id/source, precondition, postcondition, timeout, retries, failure_mode, owner, security_policy, qualification_evidence`.
- **Версионирование:** спецификация агента, исходные данные, чекпойнт LLM, embeddings, граф, промпты и tool manifest связаны с audit trail.
- **Степени автономности:** observe → recommend → draft → execute with approval → bounded automatic execute (только низкорисковые операции после risk acceptance).
- **Страховочные ограничения:** agent loop max steps; max cost/task; tool allowlist; circuit breaker; idempotency key; replay; immutable audit where needed.
- **Горизонтальная стратегия:** сначала модульный монолит / ограниченный набор контейнеров, не множество микросервисов без производственной необходимости; для защиты OTUS физические контейнеры сервисов разделены по заданию.

### 6. Архитектура роста — шесть независимых осей

| Ось масштабирования | Этап 1 | Этап 2 | Этап 3 | Что дорожает / когда переходить |
|---|---|---|---|---|
| Число агентов | 1–3 проверенных | 20 конфигураций | десятки квалифицированных | стоимость предметных тестов и контроля; не GPU сама по себе |
| Запросы | один GPU + queue | batching, caching, модельный router | GPU pool / sharding | GPU, энергия, HA, сеть; переход по p95, queue wait, cost/success |
| Знания | единый набор | разделение индексов / графов | sharded/tenant-aware KG | SSD, RAM, индексация, обновление, backup |
| Пользователи/арендаторы | 1 контур | RBAC + раздельные namespace | dedicated tenant resources | ACL/аудит, изоляция, эксплуатация |
| Организация | 1 инженер | owner core + reviewers | domain teams + FinOps/SRE | зарплаты/процессы и coordination |
| Размещение | одна машина в изоляции | локальный GPU/DB-сервер | несколько узлов / DR-site | CAPEX + резерв + сети + отказоустойчивость |

**Два разных вопроса:** *сколько типов агентов* и *сколько одновременных inference-запросов*. 20 агентных паспортов не требуют 20 видеокарт, пока совместно используют bounded inference runtime и не исчерпывают ресурс.

### 7. Экономические последствия каждого шага (проверяемые формулы и cost drivers)

| Шаг | Инженерный результат | Единовременный расход (CAPEX / труд) | Постоянный OPEX | Основной риск перерасхода | Gate |
|---|---|---|---|---|---|
| E0 IDEA+ | идея, внутр. и внеш. scout, feasibility | время поиска и экспериментов | минимальный | исследование без stop criteria | цена теста гипотезы < предела |
| E1 Architecture | C4 1–4, контракт, threat model, ADR | architect-hours | поддержка документации | перепроектирование | принят C4, REQ→TEST |
| E2 Offline core | локальный runtime, FastAPI, LangGraph, observability | разработка, SSD, тестовое окружение | электричество, обслуживание | простой GPU, несовместимость | offline smoke + measured latency |
| E3 GraphRAG | ingest, Qdrant, Neo4j, evidence | индексация, разработка графа | reindex, backup, SSD | дорогие embeddings/retrieval | граф повышает measured accepted outcome |
| E4 Security | UAG/ACL, guardrails, secrets, audit | разработка + негативные тесты | журналы/аудит, обновления | утечка данных, storage рост | User B isolation PASS |
| E5 Learning/Feedback | evaluation, correction, versions | golden dataset + review | human review + reevaluation | drift, неверная обратная связь | held-out quality gate |
| E6 Factory | генератор паспортов, registry, шаблоны, CI | наибольшая стартовая стоимость автоматизации | поддержка SDK, совместимости | overengineering при 1 агенте | `break_even_agents` подтверждено |
| E7 3 agents | медицинский ops, торговый, игровой или ИБ/OSINT | ontology, tools, tests по каждому | предметный контроль + вызовы | доменные ошибки | 3 independent qualified |
| E8 20 specs | массовая декларативная регистрация | спецификации и адаптеры | тесты регрессии, мониторинг | 20 «пустышек» вместо продуктов | registered ≠ qualified |
| E9 HA/Scale | GPU pool, replicas, data backup/DR | новые узлы, сеть, резерв | электричество, операции, лицензии | низкая утилизация, H/A избыточна | BCP, workload/ROI trigger |
| E10 Sale/Support | multi-tenant packaging, SLA, installer | hardening, документация, поддержка | поддержка клиентов, rollout | интеграция дороже лицензии | unit economics и договор |

**Статья расходов, которую легко забыть:** квалификация каждой специализации и обслуживание знаний часто стоят дороже самой генерации нескольких файлов с промптами.

#### 7.1 Базовые экономические формулы

```text
TCO_month =
  (Hardware_purchase - Residual_value) / Useful_life_months
  + Power_kWh * RUB_per_kWh
  + Cooling + Maintenance + Backup + Network
  + Staff_hours * Loaded_labor_rate
  + Security + Qualification + Licenses + Downtime_reserve

COST_QUALIFIED_OUTCOME =
  Total_cost_all_attempts / Number_independently_accepted_results

AGENT_INCREMENTAL_COST =
  Domain_design_hours + Ontology + Tool_adapter + Evaluation_dataset
  + Security_review + Integration_tests + Monthly_runtime_delta

N_break_even_development =
  ceil(Shared_platform_build_cost / (Standalone_agent_cost - Specialized_agent_incremental_cost))

N_break_even_operations =
  Shared_platform_monthly_overhead /
  (Standalone_agent_monthly_opex - Shared_specialization_monthly_increment)
```

**Если разница в знаменателе ≤0, окупаемости от масштаба по этой модели нет**. Общая платформа может быть оправдана безопасностью/управлением, но это отдельный бизнес-кейс. Для cost/accepted denominator 0 → метрика неопределена, не 0.

#### 7.2 Только учебный числовой сценарий — НЕ тарифы, НЕ фактическая оценка

Сравнение **в часах квалифицированной инженерной работы**, а не в цене железа:

| Параметр | Иллюстративное значение |
|---|---:|
| Первичная сборка shared core/factory | 600 чел·час |
| Отдельный специализированный агент «с нуля» | 200 чел·час |
| Специализация поверх factory | 40 чел·час |
| Условная полная ставка для оценки | 2 000 ₽/час |

- **1 агент:** `600 + 1×40 = 640 ч` (factory) против `1×200 = 200 ч` standalone. Фабрика **дороже на старте**.
- **4 агента:** `600+4×40 = 760 ч` против `4×200 = 800 ч`; расчётная первая экономия — `40 ч`.
- **20 агентов:** `600+20×40=1 400 ч = 2,8 млн ₽` против `20×200=4 000 ч = 8 млн ₽`; разница **5,2 млн ₽ / 65% инженерных часов** *исключительно при этих допущениях, одинаковых требованиях и равной квалификации*.
- **Порог окупаемости:** `ceil(600/(200−40)) = 4` агента, без учёта лицензий, инфраструктуры и дорогостоящих отраслевых тестов.
- **Чувствительность:** если специализация вместо 40 ч требует 120 ч, порог `ceil(600/(200−120))=8`; при 20 агентах `600+20×120=3 000 ч`, экономия **25%**, а не 65%.
- **Если отрасли требуют разных ядер** или обратной совместимости нет, формула перестаёт применяться: делаем раздельный build-vs-reuse analysis.

#### 7.3 Операционный сценарий (условный, не смета)

Предположим: общий on-prem core overhead 30 000 ₽/мес (амортизация, обслуживание, энергии, мониторинг), добавление специализации 3 000 ₽/мес, независимый агент 8 000 ₽/мес.  
Тогда `TCO_shared(20)=30 000+20×3 000=90 000 ₽/мес`, `TCO_standalone(20)=20×8 000=160 000 ₽/мес`. **Экономия 70 000 ₽/мес** только по условной модели; фактическая нагрузка может потребовать масштабирования GPU и уничтожить этот выигрыш. Операционная точка равенства: 6 агентов, **экономия начинается с 7-го**.  
Для реальной сметы заменить числа данными счетчиков PDU/GPU, закупок, труда, backup, местного тарифа, лицензий и SLA.

### 8. Экономические стратегии масштабирования

| Стратегия | Когда выбирать | Эффект | Обратная сторона |
|---|---|---|---|
| Переиспользование одного runtime | разные домены, низкая конкуренция запросов | низкая стоимость нового паспорта агента | общая очередь, blast radius |
| Router: small/large model | разная сложность задач | сокращение тяжёлого inference | риск снижения качества, требует eval |
| Quantization (проверенная) | дефицит VRAM | меньше памяти, меньший CAPEX | качество и latency могут измениться |
| Batching / KV-cache | высокая параллельность | больше throughput на GPU | рост queue latency, OOM при плохом sizing |
| Cache embeddings / retrieval | повторяющиеся запросы | меньше вычислений | stale cache, ACL leakage |
| Selective graph search | не каждому вопросу нужен граф | дешевле GraphRAG | пропуски сложных связей |
| GPU pool + queue | p95 queue wait выше SLO | масштаб по фактической загрузке | новые GPU CAPEX/OPEX |
| Per-tenant isolation | разные заказчики/уровни риска | контролируемая изоляция | больше памяти, storage, администрирования |
| Stateless services horizontal scale | API CPU/RPS bottleneck | эластичность API | не повышает LLM tokens/s автоматически |
| Production HA/DR | доказанный RTO/RPO заказчика | устойчивость и SLA | постоянные расходы резерва |

**Финансовое правило:** увеличивать мощность только если утилизация/очередь/качество нарушают измеримый SLO либо ожидаемый прирост ценности превышает полный incremental TCO.

### 9. Технические ограничения исходного железа и варианты решения

Пилотная рабочая станция: Windows 11, 32 GB RAM, RTX 3060 12 GB, i5-10400F (информация от владельца; **актуальное состояние надо проверить**).

- **A: laptop/desktop PoC:** Qwen3 4B/8B quantized в локальном inference, LangGraph, Qdrant, Neo4j, PostgreSQL. Реальные VRAM/RAM/latency/RPS *UNKNOWN* до теста. Для 12 GB — не обещать большой контекст и высокий concurrency.
- **B: single Linux server:** vLLM / supported quantization, continuous batching/KV tuning, upgrade GPU/RAM. Считать CAPEX и amortization.
- **C: multi-server on-prem:** GPU pool + API replicas + separate DB nodes + DR. Обосновывать SLA/ожидаемым масштабом, **не строить до валидации спроса**.
- **Внешний GPU/cloud API:** в целевой air-gapped архитектуре **запрещён**; даже если есть учебная опция, итоговый deployment должен быть offline.

**MVP не должен ложно приравнивать 10 000 HTTP RPS и 10 000 полноценных LLM-generations/sec**. Отдельно измерять API cache responses, LLM RPS, TTFT, end-to-end p95 и tokens/s.

### 10. P5 · FEASIBILITY / Economic Gate

**Предварительный вердикт: RESEARCH / CONDITIONAL_GO только для ограниченного MVP**, а не утверждение масштабируемости 20 промышленных агентов.

Минимальные опровергаемые эксперименты:
1. Offline smoke: запрет всех egress, ingest → GraphRAG → LangGraph → cited response.
2. Source trace: 100% созданных узлов графа с подтверждаемым `source_id` / `chunk_id` в тестовом корпусе; это проектный acceptance target.
3. ACL red team: User B не извлекает секретный chunk/edge/answer через search, API, logs, prompt, cache; **любое подтверждённое нарушение — NO_GO**.
4. Agent factory A/B: написать 3 специализации, записать фактические часы, reuse %, quality & audit coverage, а не только сформировать YAML.
5. Load test: измерить service RPS, inference RPS, p50/p95, TTFT, token/s и memory pressure.
6. Unit economics: сравнить cost/qualified-result для independent-agents vs shared factory на одинаковых задачах.
7. Feedback gate: изменение знаний не нарушает ACL или goldens; изменение политики — только с подтверждением человека.

**Stop/rollback:** известная утечка прав, скрытый внешний вызов, неработающий реальный GraphRAG, невалидная лицензия, uncontrolled action, отсутствие доказательств → BLOCK.

### 11. P6 · TECHNOLOGY ROADMAP (условные сигналы, не пророчества)

- **Триггер роста GPU:** p95 ожидания inference устойчиво выше согласованного SLO при целевой нагрузке и после оптимизации queue/batch/cache.
- **Триггер специализированного inference:** стабильный профиль задач + выигрыш в cost/accepted ответ при сохранении качества.
- **Триггер выделения микросервиса:** независимое масштабирование/команда/безопасность доказали выгоду относительно модульного монолита.
- **Триггер новой версии агента:** изменения ontology/tool contracts, drift и зафиксированная потребность клиента.
- **Триггер 20 агентов:** три независимо квалифицированные специализации и рост не нарушает regression suite / экономический порог.
- **Триггер платной коммерческой поставки:** подтверждённые качества, правовые условия, support/upgrade/backup, SLA, cost and margin.

### 12. P7–P8 · Путь разработки, сроки и доказательства

| Очередь | Поставляемый результат | Proof / acceptance | Статус |
|---|---|---|---|
| 0 | IDEA contract + scout + C4 hypothesis | документы, открытые риски, решение gate | DOCUMENTED |
| 1 | Architecture Charter / C4 1–4 / Deployment / ADR | design review, security boundaries | NOT_STARTED |
| 2 | Offline stack + core LangGraph | network-isolation run + trace | NOT_STARTED |
| 3 | GraphRAG + evidence + tenant ACL | real graph, denied secret access | NOT_STARTED |
| 4 | State/event/forecast/actions | deterministic baseline, backtest, approvals | NOT_STARTED |
| 5 | Factory registry & agent specs | 3 distinct agents, repeated test suites | NOT_STARTED |
| 6 | Cost/sizing/FinOps + load tests | measured profile and TCO, quality linkage | NOT_STARTED |
| 7 | POLYGON, video, OTUS delivery | test reports, signed release, 5–7 min demo | NOT_STARTED |

**Human approval:** до release, любых state-changing actions, смены моделей в критических процессах и коммерческих обязательств. Коммиты осмысленные, ADR обязателен; каждый важный artefact имеет provenance; сборки — SBOM.

**Для OTUS:** финальное задание сдаётся минимум за 8 дней до даты защиты. Дата защиты неизвестна и не должна угадываться.

### 13. Что показать CTO / потенциальному заказчику

1. За 5–7 минут показать: один локальный core → зарегистрировать первый профиль → анализ события → прогноз → предложение действия → объяснение и аудит.
2. Переключить профиль (например, управление остатками → загрузка медицинского подразделения на синтетике), *тот же core*, новые ontology/algorithms/policies.
3. Запустить запрещённый доступ: User B → секретные данные → отказ на этапе retrieval.
4. Открыть: живой граф Neo4j, checkpoint LangGraph, traces, telemetry, результаты негативных тестов.
5. На одном слайде дать **не обещание**, а фактические `hours_per_new_agent`, `cost_per_qualified_result`, `RPS / TTFT / p95`, `qualification_pass_rate`. Пока цифр нет — `NOT_MEASURED`.

### 14. Реестр рисков и решений

| Риск | Влияние | Контроль |
|---|---|---|
| Многообещающее слово «универсальный» | неверные ожидания, scope creep | чёткий класс задач и MVP |
| 20 агентов оказываются промпт-шаблонами | провал демонстрации | квалифицировать 3 разных домена |
| Граф раскрывает секретные связи | критическая утечка | ACL до query и обхода графа; negative tests |
| Обучение на feedback портит знания | регрессия и ошибочные рекомендации | human review, версия KB, replay tests |
| Одна GPU не выдерживает пик | latency/queue | workload-specific SLO, router, queue |
| Доменные решения опасны | ответственность и регуляторные риски | approval gates, ограничение автономности |
| Сумма 20х incremental затрат неожиданно велика | экономика не сходится | break-even/ sensitivity / stop gates |
| Лицензии models/datasets неизвестны | невозможность коммерческого выпуска | license inventory + legal gate |
| Отсутствуют proof тестов | нельзя утверждать READY | POLYGON admission gates |

### 15. Источники и статус происхождения

**Внутренние:** FATHER IDEA+ и COST Engineering v1.0 (ссылки выше); OTUS AI Architect project assignment, полученное от владельца проекта в беседе 2026-11-27.  
**Внешние руководства (для последующей детализации):**
- FinOps Foundation — https://www.finops.org/framework/
- LangGraph persistence/agent runtime — https://docs.langchain.com/oss/python/langgraph/persistence ; https://docs.langchain.com/oss/python/langgraph/overview
- Qdrant multitenancy — https://qdrant.tech/documentation/manage-data/multitenancy/
- vLLM GPU and KV sizing — https://docs.vllm.ai/en/latest/cli/serve/
- OWASP API security — https://owasp.org/API-Security/
- C4 Model — https://c4model.com/

**Граница достоверности:** исходная концепция и персональные аппаратные ограничения — сведения владельца проекта; все примерные цены, трудозатраты и выгоды — явные допущения; документация инструментов не доказывает, что они интегрированы в текущий FATHER. **MVP ещё не запущен, feasibility не подтверждено.**

---
**Заключение IDEA+:** *разрешить только ограниченные исследования архитектуры и минимального автономного GraphRAG-MVP; решение о фабрике 20 промышленных агентов принимать после измерения качества, инкрементальной стоимости и повторного использования на трёх разных специализациях.*
