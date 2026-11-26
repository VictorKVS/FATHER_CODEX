# SEC-RISK-001 — Риск-ориентированный подход и FATHER Risk Engine

**Версия:** 0.1 / 2026-11-26  
**Статус:** RESEARCHED / ARCHITECTURE_PROPOSED / IMPLEMENTATION_NOT_STARTED / NOT_QUALIFIED  
**Назначение:** краткая каноническая статья FATHER Security Wiki + план сквозного автоматического анализа и управления киберрисками.  
**Связано:** [Нормативный справочник](../security-regulations.html), [CyberED S-235](../../school/courses/CYBERED_S235_SECURE_DEVELOPMENT_RU.md).

## Вопрос и короткий ответ

**Что такое риск-ориентированный подход?** Решать, куда вкладывать ограниченные ресурсы защиты, исходя из конкретных сценариев неблагоприятных событий, их последствий, возможностей и неопределённости, а не только количества уязвимостей и наличия чек-листа. **Уязвимость ≠ угроза ≠ инцидент ≠ риск.** CVSS — характеристика тяжести уязвимости, но не самостоятельное измерение риска организации.

## Алгоритм RISK-LOOP v0.1

1. **FRAME:** задать систему, границы, критические процессы, цели, заинтересованные стороны, допустимый риск (risk appetite), критерии оценки, требуемые нормы.
2. **DISCOVER:** инвентаризировать активы, интерфейсы, зависимости, версии ПО, владельцев, типы информации, действующие меры и их evidence.
3. **SCENARIO:** сопоставить активы с угрозами, нарушителями, CAPEC/ATT&CK, CWE/CVE, негативными последствиями и путями атаки; не считать совпадение идентификатора доказательством эксплуатируемости.
4. **ANALYZE:** для каждого сценария обоснованно оценить частоту/вероятность, последствия и неопределённость; отдельно отмечать подтвержденные факты и допущения.
5. **EVALUATE:** сравнить с предварительно утверждёнными критериями; назначить ответственного за риск. **Не преобразовывать цветовую матрицу 5×5 в выдуманные проценты или денежные потери.**
6. **TREAT:** рассмотреть снижение, избегание, передачу/разделение либо осознанное принятие; выбрать меры по проверяемой эффективности, сроку, стоимости и нормативной применимости.
7. **VERIFY:** провести тесты мер, зарегистрировать evidence, SBOM, контрольные суммы, параметры метода и вычислений; измерить остаточный риск и уровень неопределенности.
8. **APPROVE:** получить разрешение владельца риска для принятия остаточного риска; автоматический аналитик не вправе самостоятельно принимать существенный риск.
9. **MONITOR:** обновления CVE/KEV/БДУ, архитектуры, инциденты и изменения в законодательстве запускают переоценку только затронутых узлов; вести версии, историю решений и повторные экзамены POLYGON.

**Режим автоматики:** ИИ извлекает и связывает данные, предлагает сценарии/оценки/планы, объясняет источники; численные оценщики используют явные модели и входы; человеческая проверка обязательна при критических решениях. Нет данных → `UNKNOWN`, а не `LOW RISK`.

## Каноническая карточка риска (необходимые поля)

`risk_id, scope, system_id, asset_ids, business_process, objective, threat_actor, threat_scenario, entry_points, vulnerabilities, consequences, existing_controls, evidence_refs, sources, source_version, observation_time, assessment_method, likelihood_estimate, impact_estimate, uncertainty_range, inherent_risk, control_effectiveness, residual_risk, confidence, assumptions, norm_applicability, risk_owner, treatment_options, decision, approved_by, review_due_at, change_log, status`.

**Система статусов:** `DISCOVERED → TRIAGED → ASSESSED → TREATMENT_PROPOSED → APPROVED → IMPLEMENTED → CONTROL_TESTED → MONITORED`; `STALE`/ `BLOCKED`/ `NEEDS_REVIEW` при неполноте данных.

## Международные первоисточники

| Источник | Официальная ссылка | Задача |
|---|---|---|
| ISO 31000:2018 | https://www.iso.org/standard/31000 | Общий процесс риск-менеджмента |
| ISO/IEC 27005:2022 | https://www.iso.org/ru/standard/80585.html | Информационные риски |
| NIST SP 800-30 Rev.1 | https://csrc.nist.gov/pubs/sp/800/30/r1/final | Оценка сценариев |
| NIST SP 800-37 Rev.2 | https://csrc.nist.gov/pubs/sp/800/37/r2/final | RMF, жизненный цикл и мониторинг |
| NIST CSF 2.0 | https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20 | Управление киберрисками |
| FAIR | https://www.fairinstitute.org/fair-book | Модель количественного ущерба; применять только при обоснованных распределениях |

## Российская нормативная и методическая ветка

- **ГОСТ Р ИСО 31000-2019**: принципы и руководство менеджмента риска. **Официальная карточка Росстандарта:** https://protect.gost.ru/gost/details/6a383140-61f9-458c-8663-e919a5782434
- **ГОСТ Р 58771-2019**: технологии оценки риска, выбор методов, анализ и реестры рисков. **Официальная карточка Росстандарта:** https://protect.gost.ru/gost/details/f35f83b7-a9fd-453b-b1bd-e05035a5009c
- **ГОСТ Р 72254-2025**: применение ГОСТ Р ИСО 31000 в системах менеджмента. **Официальная карточка:** https://protect.gost.ru/gost/details/6782022b-2fdc-45db-a9a0-f419bf25ec10
- **ФСТЭК: Методика оценки угроз безопасности информации**, утверждена 05.02.2021; использовать как методический источник анализа актуальных угроз, сценариев и негативных последствий, **не** приравнивать к полноценной ISO/FAIR модели оценки финансового риска. Текст: https://www.consultant.ru/document/cons_doc_LAW_378330/ ; искать официальную публикацию/ссылку на https://fstec.ru/ и проверять редакцию.
- **149-ФЗ, 152-ФЗ, 187-ФЗ, ПП 1119, ФСТЭК 21, 117/137, 235/239 и другие:** применимость зависит от ГИС, ИСПДн, субъекта КИИ, категорирования и обрабатываемой информации. Указание закона **само по себе** не даёт универсальной формулы расчёта риска. Текущие редакции искать в https://pravo.gov.ru/ . Ранее созданный нормативный справочник содержит ссылки на релевантные акты.

## Практика мировых GRC/IRM-систем (изучить, а не копировать целиком)

| Решение | Официальный сайт | Что заимствуем как архитектурный паттерн |
|---|---|---|
| CISO Assistant (intuitem) | https://intuitem.com/ciso-assistant/ | Множественные фреймворки, оценка рисков, связи с контролями и соответствием |
| eramba | https://www.eramba.org/risk-management | Реестры asset/third-party/business risks, учёт мер, циклы ревью |
| SimpleRisk | https://www.simplerisk.com/deployment/open-source | Регистрация, обработка, остаточные риски, workflow |
| ServiceNow Integrated Risk Management | https://www.servicenow.com/products/integrated-risk-management/pricing.html | Корпоративный риск-регистр, владельцы, автоматические индикаторы и контролируемое согласование |

**Правило:** проверить лицензии и API отдельно перед переиспользованием кода и обменом данными. Не выдавать маркетинговые заявления поставщиков за доказательство эффективности.

## Архитектура: один FATHER Risk Engine, без дублирования ядер

```text
NORMATIVE & INTELLIGENCE INPUTS        ENGINEERING FACTS
ГОСТ/ФСТЭК/NIST/ISO/FAIR             SBOM/Trivy/БДУ/CISA KEV/CMDB/CI
             \                         /
              -> ALINA: provenance, knowledge graph, contradiction checks
                              |
                  FATHER SecGraph scenarios
                              |
                   Risk Engine: scoring methods
                qualitative / FAIR with justified data
                              |
                     options & risk treatment
                              |
                UAG human approval / risk ownership
                              |
                  POLYGON control effectiveness
                              |
                 risk register + dashboard + alerts
                              |
                      delta re-assessment
```

### Компонентные контракты

- **ALINA Source Contract:** происхождение, цитата/номер пункта, редакция, дата вступления, область действия, confidence, проверка противоречий.
- **Risk Assessment Contract:** scenario_id, method_id/version, factors, data_sources, uncertainty, reproducibility_seed (если stochastic), computed score.
- **Risk Treatment Contract:** proposed controls, implementation cost, expected effect with evidence, deadlines, human decision, risk owner.
- **POLYGON Contract:** tests, independent hidden case, control implementation evidence, residual risk decision; без доказательств — NO PASS.
- **Security:** least privilege, separate secret store, signed changes at approved milestones, audit, privacy/redaction; агенты не должны иметь прямой доступ к промышленному контуру.

## Критерии завершения первого MVP (не выполнены)

1. Минимум 1 учебная система и 3 достоверно описанных сценария риска с traceable источниками.
2. Детерминированный qualitative engine с явной шкалой и тестами границ; пропуски дают UNKNOWN.
3. На каждый риск — исходная оценка, допущения, предложение мер, владелец, остаточная оценка после проверки мер.
4. История изменений и evidence hashes, воспроизведение расчёта.
5. Отрицательные тесты: устаревший CVE feed, несуществующий актив, конфликт норм, отсутствие владельца, провал меры, недоступность policy decision engine.
6. Обновление только затронутых рисков по изменившимся источникам и контроль регрессий.
7. Представление в FATHER Security Wiki и веб-дашборде; недостающие факты не маскировать красивым графиком.
8. Human-approval gate: риск не принимается и меры в инфраструктуре не внедряются автоматически.

**Текущий статус:** только исследование/проект; загрузка реестров, движок оценок, собственное ПО, интеграции и испытания ещё не выполнены.
