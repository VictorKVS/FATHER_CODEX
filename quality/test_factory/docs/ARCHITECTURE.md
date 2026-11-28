# FT-ARCH-001 — Архитектура фабрики испытаний
**Status:** PROPOSED; requires architecture review and ADR signoff.

## Цели, границы и принципы
FATHER Test Factory — общий контроль качества для всех программ и AI-агентов FATHER. Её исполнительная часть может вызывать разрешённые адаптеры тестирования, но не может сама утверждать релиз; независимый POLYGON принимает от неё только кандидата и доказательства, выполняет отдельные неизвестные проверяемому агенту испытания и возвращает заключение. Запрещены реальные целевые API, реальные ПДн, неопубликованные тестовые ключи и произвольный сетевой сканинг вне разрешённого изолированного стенда.

## Функциональные компоненты
| ID | Компонент | Обязанности | MUST NOT |
|---|---|---|---|
| TF-01 | Source Registry | books/ГОСТ/OWASP/NIST; версия, пункт, автор, права, точная ссылка | придумывать пункты и копировать защищённые книги в публичный репо |
| TF-02 | Requirement/Threat Graph | REQ→FLOW→INVARIANT→THR→TEST | создавать требования без владельца и provenance |
| TF-03 | Test Method Designer | оформлять ПМИ, схему, предусловия, критерии FAIL/PASS | генерировать тесты без утверждённого ожидания |
| TF-04 | Case Registry | versioned test cases, immutable reviewed baseline, fixtures | править ожидания задним числом под код |
| TF-05 | Sandbox Orchestrator | создавать изолированный стенд, применять seed, запускать адаптеры | выходить в production и принимать произвольные URL |
| TF-06 | Test Adapters | unit, contract, SAST/SCA, DAST, fuzz, perf, AI eval | самовольно повышать права и принимать решения о выпуске |
| TF-07 | Evidence Ledger | SHA256, raw result, config/policy/source/model/test version, before-after | считать stdout pytest официальным актом испытаний |
| TF-08 | Defect & Retest | severity, owner, red/green, fix commit, повторный тест | удалять историю FAIL |
| TF-09 | Qualification Bridge | передавать воспроизводимый пакет POLYGON, сверять manifest | выдавать сертификат вместо независимого POLYGON |
| TF-10 | Release Gate | проверять обязательные условия, хранить human decision | одобрять собственный релиз автоматически |

## Два контура независимости
- **Development QA**: открытые тесты и фикстуры в репозитории компонента; разработчик запускает часто.
- **Independent Qualification**: POLYGON имеет собственные скрытые наборы, полномочия чтения зафиксированных артефактов и выдаёт оценку с привязкой к hash/revision; тестируемый агент не может менять его ожидания.

## Контур изоляции
Код агента, враждебные fixtures и fuzz payloads запускаются только внутри disposable sandbox с ограничениями CPU/RAM/network/timeout, удалёнными production credentials, pre-approved targets и immutable audit. Во время draft-создания сценариев реальные атаки не выполняются.

## Сквозная сущность
`SourceReference` → `Requirement` → `Threat` → `TestMethod` → `TestCase` → `TestRun` → `EvidenceArtifact` → `Defect` → `QualificationDecision` → `HumanReleaseDecision`.

Для первой итерации источник и сценарий представлены JSON; граф и БД пока **не реализованы**. Раздельный `TestRun` неизменяем: повтор запуска получает новый `run_id`, а не перезаписывает PASS/FAIL.

## ADR, которые предстоит принять
- ADR-TF-01: каталог в Git (JSON + Markdown) или PostgreSQL сразу? Предложение: Git на M0, DB projection на M2.
- ADR-TF-02: pytest + стандартизованные JSON/JUnit/SARIF адаптеры, а не единый собственный runner для всех типов проверок.
- ADR-TF-03: content-addressable immutable artifact storage и подписи через отдельный разрешённый signer.
- ADR-TF-04: локальные sandbox workers в Docker Compose; Kubernetes только после измерений.
- ADR-TF-05: POLYGON как независимый сервис, человеческий signoff.
