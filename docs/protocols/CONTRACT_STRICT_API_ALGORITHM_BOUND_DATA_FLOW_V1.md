# FATHER-STD-API-001 — Contract-Strict API / Algorithm-Bound Data Flow

**Версия:** 1.0 (предложение к утверждению)  
**Дата:** 2026-11-27  
**Статус:** `PROPOSED`, NOT IMPLEMENTED, NOT QUALIFIED  
**Область применения:** FATHER_CODEX, FATHER/UAG, агентные интерфейсы, сервисы, API, хранилища, файлы, события, оркестрация, инструменты, модели и их выходы.

> **Нормативная формулировка:** API, агент или сервис не имеет права запрашивать, принимать, обрабатывать, передавать либо сохранять данные и выполнять операции вне утверждённых алгоритмов, схем данных, полномочий и контрактов взаимодействия. Непредусмотренный информационный поток запрещён по умолчанию.

## 1. Источник и статус

Это **зафиксированное требование из проектного обсуждения**, но **не реконструкция неизвестного первоначального списка «12 правил»**. Точный список двенадцати ранее утверждённых пунктов в рамках текущего аудита не установлен. До появления первоисточника **не называть этот документ «12 правилами»** и не приписывать ему недостающие положения.

Обязательная технологическая последовательность:

`IDEA+ → функциональная схема → информационные контракты → алгоритмы блоков → оркестрация → безопасность/отказы → реализация → POLYGON`.

## 2. Контракт уровня компонента

Каждый компонент `CMP-*` описывается не только REST/OpenAPI, но и `Component Design Contract`:
- `purpose`, `business_requirement_ids`, `owner`, `version`, `implementation_sha`;
- `algorithm_id/version/source/evidence`, `preconditions/postconditions/invariants`, ограничения и вычислительная сложность там, где применимо;
- `input_schema` (закрытая, versioned), `output_schema` (закрытая, versioned);
- `source_identity/tenant`, `allowed_recipients`, `allowed_operations`, `allowed_tools`, `required_scopes`;
- `classification`, `retention`, `audit`, `provenance`;
- `states`, `transitions`, `timeouts`, `retries`, `idempotency`, `error_contract`;
- `validation_rules`, `negative_tests`, `qualification_evidence`, `approved_by`.

**Поле вне контракта ⇒ REJECT**, а не silent ignore. Операция вне allowlist ⇒ DENY. Получатель вне `allowed_recipients` ⇒ DENY. Доступ к объекту отдельно проверяется по object/tenant ACL даже при корректной структуре запроса.

## 3. Информационный контракт межкомпонентного ребра

Каждый поток `FLOW-*` должен иметь:
`sender → receiver → purpose → operation → schema_version → allowed_fields → trust_boundary → authorization_rule → transformation_algorithm → evidence_ref → audit_rule`.

**Запрещено:** произвольный `dict` без схемы через доверенные границы, wildcard tool calls, несанкционированные `SELECT *` / file glob, расширение RAG-контекста за ACL, передача получателю полей, которые ему не нужны, обход API через прямой доступ к базе данных.

Особенности:
1. Технические transport metadata (`request_id`, `trace_id`) тоже оговариваются schema, а не добавляются произвольно.
2. При преобразовании пакета фиксируются `input_ref`, `algorithm_version`, `output_hash`; секреты не логируются.
3. Ответ сервиса проверяется не менее строго, чем запрос, включая `additionalProperties: false` или эквивалент в сериализаторе.
4. Контроль содержимого — не только синтаксис. Поле с допустимым типом может содержать запрещённые данные; применяются данные уровня policy/PII/classification.
5. Логика прав доступа реализуется **вне LLM**, в независимом policy enforcement point (UAG).

## 4. Канонический отрицательный пример

Контракт:
```json
{
  "operation": "get_document",
  "document_id": "DOC-001"
}
```

Нарушение:
```json
{
  "operation": "get_document",
  "document_id": "DOC-001",
  "export_all_documents": true
}
```

Результат: `400/422 INVALID_CONTRACT`, tool не выполняется; write-only redacted audit: schema revision, request_id, rejection reason. Даже исходный корректный запрос получает `DENY`, если отсутствует соответствующий `read_document` grant или owner/data classification запрещает доступ.

**Контрпример обхода только schema:** `document_id` допустимой формы не означает, что документ принадлежит caller; требуется object-level authorization.

## 5. Правило изменений

`Change Request → Business/algorithm impact → security review → schema version bump → consumer compatibility analysis → contract tests + negative tests + regression → independent POLYGON qualification → human approval → signed release`.

Изменение schema, алгоритма, получателя, прав, маршрута, модели, source policy или tool interface делает затронутые прежние evidence/qualification **подлежащими пересмотру**. Нельзя модифицировать контракт или правила допуска собственным модельным ответом.

## 6. Контрольные отрицательные тесты

| ID | Отрицательный сценарий | Ожидаемая реакция |
|---|---|---|
| CST-01 | неизвестное поле на входе | REJECT, no side effects |
| CST-02 | неизвестное поле на выходе модели/сервиса | REJECT/ABSTAIN, no forwarding |
| CST-03 | операция не в allowlist | DENY, audited |
| CST-04 | корректное поле, чужой объект/tenant | DENY, no leak in response/cache/graph/log |
| CST-05 | данные направлены непредусмотренному получателю | BLOCK, audit |
| CST-06 | direct DB call в обход UAG | BLOCK by infrastructure identity/ACL |
| CST-07 | prompt injection требует расширить схему | BLOCK, no schema self-edit |
| CST-08 | изменение версии алгоритма без contract update | RELEASE BLOCK |
| CST-09 | допуск истёк после обновления | DENY until qualification |
| CST-10 | повтор операции с idempotency key | no duplicate consequential action |
| CST-11 | malformed nested JSON/excess properties | REJECT at every nested schema depth |
| CST-12 | sensitive field in log, telemetry or RAG citation | BLOCK/redact, report incident |

## 7. Доказательства готовности

Для `READY` обязательны:
- `contract.yaml/json`, разрешённые маршруты, machine-readable input/output schemas;
- алгоритмическое обоснование `ALG-*` и ADR;
- code-to-contract binding + commit SHA, provenance/SBOM;
- executable positive/negative tests и их **фактически выполненный** отчёт;
- независимое заключение POLYGON, результат security review, утверждение человеком;
- проверка в **составе конечной системы**, а не только isolated unit tests.

В терминах SADEQ это часть `Component/Data/Security/Qualification contracts`, а не альтернатива архитектуре C4, BPMN или Twelve-Factor.

## 8. Связь с 12-factor и Kubernetes

The Twelve-Factor App полезен для конфигурации, процессов, логов и поставки. **Он не заменяет** FATHER-STD-API-001. Kubernetes обеспечивает network/service security и скейлинг, но спецификация Kubernetes не гарантирует, что в `payload` нет непредусмотренных полей. Реализация: OpenAPI/JSON Schema (closed schemas), Pydantic strict validation, policy-as-code/UAG, ingress/egress restrictions, contract tests and independent exam.

## 9. Применение к проекту SADEQ

- SADEQ UAA `Observation/Event/Object/Action` интерфейсы должны быть закрытыми схемами, включая вложенные объекты, для которых согласован JSON shape.
- `/api/v1/actions/proposals` — proposal only, не execution. Отдельный tool gateway проверяет последнюю актуальную политику непосредственно перед выполнением.
- Agent 001 может предлагать изменение проекта, но не утверждать изменение алгоритмов, схем и допусков.
- Допуск связки `agent-version + algorithm + tool + data scope` привязан к независимым evidence.

**Приёмочный статус:** `STANDARD_DOCUMENTED`; действительная квалификация и внедрение ещё не выполнены.
