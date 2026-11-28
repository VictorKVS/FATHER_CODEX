# FT-LIB-001 — Библиотека теории, алгоритмов и нормативных оснований
**Status:** SOURCE-VERIFIED-AT-TOC/PREFACE-LEVEL; targeted deep chapter reading needed for exact algorithm/page extraction. Библиография книг ниже составлена по конкретным файлам, ранее переданным владельцем проекта; без публикации защищённого текста.

| ID | Книга / автор | Подтверждённое содержание | Проектный модуль / результат |
|---|---|---|---|
| BOOK-CD | **Continuous Delivery**, Jez Humble, David Farley (2010/2011) | Общая организация сборки, тестирования и доставки программного продукта; deployment pipeline | TF-05, TF-08; версионированный pipeline, reproducible build, sequential gates |
| BOOK-GHA | **Learning GitHub Actions**, Brent Laster (2023) | Part I Foundations; Part II Building Blocks; Part III Security and Monitoring; Part IV Advanced Topics (reusable workflows, matrix, containers) | TF-05/06; CI adapters, immutable workflow sources, ограничение прав runner, хранение артефактов |
| BOOK-97 | **97 Things Every Application Security Professional Should Know**, ed. Reet Kaur, Yabing Wang (2024) | По предисловию: 12 тематических разделов AppSec, secure SDLC, threat modeling, code scanning/testing, vulnerability management, supply-chain/AI security | TF-02/06/08; threat design, issue lifecycle, security finding triage |
| BOOK-AGSEC | **Enterprise AI Agent Security**, Thomas De Vos (2026) | Ch. 2 failure modes; Ch. 6 agent identity; Ch. 7 tool security; Ch. 8 eval regression; Ch. 11 RAG attack surface; Ch. 18 policy as code; Ch. 20 AgentSecOps; Ch. 21 readiness | TF-02/06/09; tool approval, policy boundary, RAG ACL, prompt injection suites, version-bound evaluations |

**Важно:** направления в последнем столбце — **наш инженерный вывод о применении** прочитанного, не дословно описанная авторами архитектура FATHER. До внедрения конкретного алгоритма регистрируем `book/chapter/page/exact idea/limitations/alternatives/ADR/test` и проверяем первичный текст главы. Для BOOK-CD и BOOK-97 сейчас проверены титульные сведения и общая тематика, а не все нужные главы. `checked_scope` записан честно в `source_registry.json`.

## Нормативные и методические источники
| ID | Основание | Как используем | URL |
|---|---|---|---|
| STD-56939 | ГОСТ Р 56939-2024 | безопасная разработка ПО, предотвращение, выявление, устранение недостатков | https://protect.gost.ru/gost/details/f3818925-a96f-4f55-96e9-46b44720ee64 |
| STD-59795 | ГОСТ Р 59795-2021, п. 5.13 | программа/методика испытаний АС и связь с ТЗ | https://base.garant.ru/403358611/ |
| STD-59792 | ГОСТ Р 59792-2021 | предварительные, опытная эксплуатация, приёмочные испытания | https://protect.gost.ru/gost/details/60279c95-21dc-430c-bf2c-f626c588576e |
| STD-ASVS | OWASP ASVS v5.0.0 | формализованные требования к проверке web/API security | https://asvs.owasp.org/ |
| STD-WSTG | OWASP WSTG | практические методики тестирования веб-приложений и API | https://github.com/OWASP/wstg |
| STD-SSDF | NIST SP 800-218 v1.1 | организационные практики безопасной разработки | https://csrc.nist.gov/pubs/sp/800/218/final |
| STD-AGENT | OWASP Agentic Security Initiative | угрозы агентных систем как дополнительный каталог | https://genai.owasp.org/initiatives/agentic-security-initiative/ |

## Как превращать книгу в проверяемую методику
1. Занести библиографию и **проверенный локатор**, не переносить весь PDF.
2. Выделить применимое положение и ограничения, не подменять его собственной догадкой.
3. Сопоставить с конкретным риском, требованием, объектом SADEQ и действующими стандартами.
4. Сформулировать наблюдаемый инвариант/запрет с отказом.
5. Построить схему, preconditions и ожидаемые side effects.
6. Написать ПМИ и утвердить baseline **до** исполняемого теста.
7. Реализовать harness; выполнить тест, сохранить независимое evidence с hash.
8. Использовать результат для исправлений и qualification, сохраняя историю ошибок.

## Права и происхождение
В репозитории размещаются наши авторские выжимки, библиография и ссылки. Загруженные владельцем электронные экземпляры не републикуются, не встраиваются целиком в Git и не используются как основание для заявления о правах на исходный текст.

## Книги для расширения библиотеки (не предоставлены, не изучены по полному тексту)
Предлагаемый **список чтения**, проверено только существование книги и издательское описание; не приписывать им конкретные алгоритмы до изучения разделов:

| Приоритет | Издание | Какая компетенция нужна | Официальный/каталожный источник |
|---|---|---|---|
| P0 | Maurício Aniche — *Effective Software Testing* (2022) | проектирование систематических unit/integration/system test suites и testability | https://www.manning.com/books/effective-software-testing |
| P0 | Adam Shostack — *Threat Modeling: Designing for Security* | threat modeling, систематизация атак и проверяемых защитных свойств | https://www.wiley.com/en-us/threat-modeling-designing-for-security-p-9781118809990 |
| P0 | Neil Madden — *API Security in Action* (2020) | аутентификация, авторизация, безопасная конструкция корпоративных API | https://www.manning.com/books/api-security-in-action |
| P1 | Gerard Meszaros — *xUnit Test Patterns* | повторно используемые паттерны и устранение «запахов» тестового кода | https://www.oreilly.com/library/view/xunit-test-patterns/9780131495050/ |
| P1 | Boris Beizer — *Software Testing Techniques*, 2nd ed. | техника проектирования тестов и анализ покрытия / тестопригодности | https://www.wileyindia.com/software-testing-techniques.html |

**Нельзя** заявлять, что все перечисленные книги уже есть у владельца, или копировать из них тексты без разрешения.
