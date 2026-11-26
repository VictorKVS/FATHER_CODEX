# FATHER CODEX — единая программа Agent Factory + AI Academy + Programmer Coach

**Версия:** 1.0 · 2026-11-25  
**Статус:** INTEGRATED_DOCUMENTATION / SCHOOL_CH01_INTERACTIVE_MVP / RUNTIME_PIPELINE_NOT_IMPLEMENTED / NOT_QUALIFIED.

Этот каталог — **основная точка входа** в образовательные и инженерные функции FATHER_CODEX. Проект **не создаёт второго FATHER Core**. Базовые знания и первоисточники остаются у ALINA, безопасность и допуски — у FATHER/UAG, независимая проверка — у POLYGON; CODEX потребляет их по контрактам.

## Цели

1. Превращать каждую главу *Agentic Design Patterns* в понятный курс, исполняемую Python-заготовку и проверяемый компонент Agent Factory.
2. Учить школьника **всей содержательной теории** главы, а не только алгоритму: понятия, объяснения, границы применения, ошибки, связи, стоимость.
3. Сопровождать траекторию **новичок → junior → middle → senior track** через самостоятельные задачи, наводящие подсказки и независимые экзамены.
4. Использовать Senior Reviewer как **наставника**, который сравнивает алгоритмы, архитектуры и варианты рефакторинга по источникам и измерениям, а не подменяет ученика.
5. Вести красивый русскоязычный сайт с английским переключателем, схемами, мини-играми, квалификацией и Cost Engineering.

## Единый каталог артефактов — всё управляется через FATHER_CODEX

| Назначение | Канонический путь / ссылка | Фактический статус |
|---|---|---|
| Главный сайт | [docs/index.html](../index.html) | HTML Dashboard есть, полнота интеграций не доказана |
| Школа и CH01 | [docs/school/index.html](../school/index.html) | интерактивный MVP без внешнего LLM |
| Программа CH01–CH07 | [docs/school/COURSE_PROGRAM_RU.md](../school/COURSE_PROGRAM_RU.md) | спецификация |
| Полное освоение теории | [docs/school/THEORY_MASTERY_SYSTEM_RU.md](../school/THEORY_MASTERY_SYSTEM_RU.md) | спецификация |
| Programmer Coach junior→senior | [FATHER_CODEX_PROGRAMMER_COACH_V1_RU.md](FATHER_CODEX_PROGRAMMER_COACH_V1_RU.md) | спецификация |
| IDEA+ / World Scout | [docs/protocols/FATHER_IDEA_PLUS_PROTOCOL_V1.md](../protocols/FATHER_IDEA_PLUS_PROTOCOL_V1.md) | спецификация |
| FinOps, TCO, стоимость результата | [docs/protocols/FATHER_COST_ENGINEERING_PROTOCOL_V1.md](../protocols/FATHER_COST_ENGINEERING_PROTOCOL_V1.md) | спецификация |
| CH02 Routing / CH03 Parallelization / CH04 Reflection / CH05 Tool Use / CH06 Planning / CH08 Memory | [ALINA LIB-0040](https://github.com/VictorKVS/alina-knowledge-worker/tree/feature/father-book-library-index-20261122/library/books/LIB-0040_Agentic_Design_Patterns) | первичные учебные исходники / code examples; не переносить слепо и не дублировать |
| CH06 source review и IDEA+ | [CH06 анализ](https://github.com/VictorKVS/alina-knowledge-worker/blob/feature/father-book-library-index-20261122/library/books/LIB-0040_Agentic_Design_Patterns/chapters/CH06_PLANNING_RU.md) | прочитана глава, код ещё не квалифицирован |
| CH06 лаборатория | [CH06 A/B/C](https://github.com/VictorKVS/alina-knowledge-worker/blob/feature/father-book-library-index-20261122/library/books/LIB-0040_Agentic_Design_Patterns/labs/CH06/LAB_PROGRAM.md) | описана, не исполнена |
| FATHER Engineering Competency Lab | [github](https://github.com/VictorKVS/FATHER-Engineering-Competency-Lab) | отдельный источник evidence/компетенций |

**Политика источников:** ALINA — источник знаний с provenance. FATHER_CODEX — продуктовый хозяин учебной платформы, оркестрации тренера, визуализации и будущих пакетов компонентов. Реальные переезды файлов должны выполняться с сохранением авторства, историй Git, тестов и ссылок. Не удалять или объявлять перенесёнными существующие файлы ALINA, пока их перенос не подтверждён.

## Контуры и ответственность

```text
                 FATHER SHARED CORE
                       |
             IDEA+ / Feasibility / UAG
                       |
            +----------+----------+
            |                     |
       ALINA Knowledge       FATHER_CODEX
       Source Registry       Academy & Agent Factory
            |                     |
     Concepts / Theory      Course / Coach / Reviewer
            |                     |
            +------ contracts ----+
                       |
           Exercise & Sandbox (future)
                       |
            Evidence & CostMeter (future)
                       |
              POLYGON Examiner
                       |
             Dashboard / Progress
```

### Контрактные границы
- **Theory package:** `chapter_id, concept_id, origin_ref, source_page, content_version, prerequisites, misconceptions, visual_spec, question_specs`.
- **Learning attempt:** `exercise_id, attempt_id, hint_level, result, evidence_refs, verification_status, timestamp`; не хранить персональные данные детей без нужной правовой основы.
- **Code review:** `source_commit, task_contract, tests_before, candidate_diff, algorithm_sources, complexity_claims, tests_after, benchmark_evidence`.
- **FinOps:** `run_id, model, provider, input/output/cache_tokens, storage, compute, costs, rate_timestamp, cost_per_qualified_outcome`.
- **Qualification:** `exam_id, scope, version, holdout_ref, evidence_refs, decision`; закрытые эталоны не поступают тренеру.

## Учебное правило: «прошёл игру» ≠ «усвоил теорию»

Каждая глава должна покрывать ВСЕ содержательные идеи исходника через `Coverage Matrix`, включая термины, определения, примеры, контрпримеры, границы применения, модели ошибок и источники. Для каждого обязательного понятия: объяснение своими словами, предсказание, применение, анализ ошибочного случая, перенос в новую задачу, повторение через 1/7/30 дней. Интервалы и пороги — пилотные настройки, а не научно обоснованная гарантия.

## Разработка по главам

1. ALINA: source review, концепт-карта, проверенные источники.
2. CODEX: школьные карточки, объяснения, схемы, мини-игры, первая Python-программа.
3. IDEA+: уже существующие реализации, мировой опыт, применимость, экономика.
4. Senior Reviewer: варианты алгоритмов, тесты, рефакторинг, источники, ADR.
5. Programmer Coach: самостоятельные задания и адаптивные подсказки, компетенции.
6. POLYGON: независимые экзамены и интеграционные испытания.
7. Dashboard: рус/англ UI, связи, статус, **измеренные** метрики и cost dashboard.

## Инженерные этапы

- **M0 — DOCUMENTED:** архитектура, ссылочный каталог и протоколы собраны в CODEX.
- **M1 — THEORY:** полная концепт-карта CH01 по первоисточнику и coverage audit.
- **M2 — PYTHON:** семь небольших корректных Python baseline с модульными тестами.
- **M3 — REVIEWER:** автономно ограниченный (без опасных команд) рефакторинг и образовательные diff/explanation.
- **M4 — COACH:** упражнения уровней, mastery graph, прогрессивные подсказки, отложенные проверки.
- **M5 — POLYGON:** доказательная квалификация, контроль скрытых заданий.
- **M6 — LIVE DASHBOARD:** реальные безопасные данные, двуязычный интерфейс и мониторинг затрат.

**Ни один пункт M1–M6 не считать реализованным по одному лишь наличию этого файла.**

## Порядок очередного шага

Начать с **CH01: Concept Coverage Matrix** по оригиналу PDF и русскому переводу, затем Python baseline и тесты. Теоретический контур должен быть достаточным для школьника до усложнения архитектуры тренера.

## Исходники и авторские права

Оригинал Antonio Gulli предоставлен владельцем библиотеки; русскоязычный внешний перевод: https://github.com/TaiPanCy/agentic-design-patterns-book-rus. Не перепубликовать защищённые тексты/рисунки целиком. Для занятий создавать самостоятельные объяснения и оригинальные схемы.

## Baseline FATHER

Human commits, ADR, component/data/security/qualification contracts, SHA-256 provenance, SBOM/build provenance, evidence и независимые тесты; релизные подписи — только разрешёнными ключами. Оригинальный исходный код ребёнка и его первая версия не заменяются «идеальной» версией без сохранения истории и объяснения.

## AppSec и DevSecOps — CyberED S-235

- [Открыть трек S-235 «Основы безопасной разработки»](../school/courses/CYBERED_S235_SECURE_DEVELOPMENT_RU.md) — модули 0–4: введение и SSDLC, веб-угрозы (две части), защита окружения, безопасная разработка в SDL; уровни школьник → студент → Junior → Master → Senior, Teach-Back и POLYGON.
- По ссылкам CyberED учитываются только темы опубликованной программы и пользовательский список LMS; закрытые лекции не копируются. Прогресс CyberED не эквивалентен квалификации FATHER.

## Нормативный справочник и контекстные ссылки

- [Справочник российской нормативной базы ИБ](../reference/security-regulations.html) — федеральные законы, постановления, приказы ФСТЭК/ФСБ и ГОСТы, поиск и цепочки применимости.
- [CyberED S-235](../school/courses/CYBERED_S235_SECURE_DEVELOPMENT_RU.md) — нормативная база указана прямо в темах CIA, аутентификации, авторизации, SSDLC и DevSecOps.

## FATHER Security Wiki

- [SEC-IDENTITY-001: идентификация, аутентификация, авторизация](../reference/wiki/SEC-IDENTITY-001.md) — компактный документ с книжной цитатой, пунктами законодательства, алгоритмом и испытаниями.

## Риск-ориентированный подход / Risk Engine

- [SEC-RISK-001 — нормативная база, алгоритм и архитектура автоматического анализа и управления рисками](../reference/wiki/SEC-RISK-001.md). Статус: исследование и проектирование; ни работающий движок, ни проверки POLYGON не заявлены.

## Второй сквозной слой при изучении программирования — Security & Cost

- [Тренажёр проверки зависимостей и перехода EXPLORE → BUILD → RELEASE](../school/security-layer.html).
- [Инженерный контракт S0–S7, Cost Gate, allow/block/review для версионированных зависимостей](../school/SECURITY_SECOND_LAYER_RU.md).
- Статус: интерактивная демонстрация + политика; реальное CI-принуждение и POLYGON требуют отдельного исполнения и evidence.
