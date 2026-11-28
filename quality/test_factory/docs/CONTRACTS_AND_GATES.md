# FT-CTR-001 — Контракт случая испытания и запреты на самоаттестацию
**Status:** PROPOSED.

## Слои проверок
- `SCHEMA`: допустимость и полнота паспорта теста (реализован частично).
- `REQUIREMENTS`: трассировка утверждённого источника и точных условий.
- `METHOD`: наличие ПМИ, схем, входных данных, независимых способов наблюдения.
- `EXECUTION`: воспроизводимый запуск нужного адаптера в sandbox.
- `EVIDENCE`: результаты, подписи, входные hashes, raw logs and side-effect counters.
- `QUALIFICATION`: независимая проверка POLYGON, human release decision.

## Паспорт TestCase
Обязательные атрибуты: `case_id, schema_version, status, system, objective, requirement_ids, contract_ids, threat_ids, source_refs[], preconditions[], setup[], steps[], negative_assertions[], evidence_plan[], expected_result, review`.

Применяется JSON Schema Draft 2020-12. На M0 есть **отдельный ограниченный проверяющий Python validator**; полный JSON Schema compliance ещё не реализован. В случае расхождения валидатор не становится истиной: необходим review схемы/контракта и зарегистрированный дефект.

## Документы и роли
| Статус | Основание | Кто может установить |
|---|---|---|
| DESIGN | идея теста, черновик источников | инженер |
| REVIEWED | постановка + требования + негативные последствия проверены | ответственный по архитектуре и ИБ |
| APPROVED | заморожены данные, ожидания, исходные условия, критерии | назначенный владелец ПМИ |
| EXECUTED | есть version-specific run и наблюдения | исполнитель лаборатории |
| QUALIFIED | POLYGON независимо подтвердил определённый scope | независимый экзаменатор |
| RELEASED | уполномоченное человеческое решение по версии | владелец выпуска |

Проверка «10 тестов успешно» не даёт статуса QUALIFIED. Переходы требуют identity, evidence hashes и записанного решения; изменение кода/политики/модели/тестов инвалидирует относящуюся к ним квалификацию.

## Система контроля запретов
- Нельзя `PASS` без полного протокола определённого TEST-ID.
- Нельзя принимать авторизацию по подставленному tenant заголовку.
- Нельзя очищать проваленный тест через `xfail`/удаление test case без change review.
- Нельзя считать проверку HTTP-кода доказательством отсутствия побочных действий.
- Нельзя запускать DAST/fuzz/active attack против production или чужих targets.
- Нельзя хранить в Git скрытые POLYGON вопросы, реальные секреты, ПДн.
- Нельзя получать `RELEASED` от того же агента, который менял проверяемую реализацию.
- Любое недостающее обязательное evidence = `INCONCLUSIVE/BLOCKED`, не `PASS`.

## Контроль допуска
C0: schema+registry valid → C1: reviewed and approved method → C2: execution + all mandatory security checks → C3: evidence reproducible → C4: POLYGON independent → C5: human release approval. Каждая стадия может остановить выпуск. CLI этой версии реализует только C0 и запрет допуска из состояния DESIGN.
