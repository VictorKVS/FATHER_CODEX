# CyberED S-235 / FATHER Academy — реестр пятнадцати зарегистрированных источников

**Дата регистрации:** 2026-11-26; новые партии 2026-11-27  
**Статус:** PDF_AND_EPUB_METADATA_TOC_INSPECTED / CHAPTER_ANALYSIS_PENDING / LABS_NOT_QUALIFIED  
**Владельцы:** ALINA (источники, фрагменты, версии, граф знаний), FATHER_CODEX (учебные версии и Python), POLYGON (испытания).  
**Связанный курс:** [CyberED S-235](CYBERED_S235_SECURE_DEVELOPMENT_RU.md).  
**Нормативный справочник:** [Российские акты и ГОСТы](../../reference/security-regulations.html).

## Полученные файлы — проверены титульные данные и структура; полный разбор впереди

| ID | Книга, данные **из переданного PDF** | Страниц в PDF | Темы, подтверждённые оглавлением | Статус |
|---|---|---:|---|---|
| SEC-BOOK-001 | Phillip J. Windley, **Authorization in Action**, Manning, **MEAP Version 6**, copyright 2026 | 617 | digital identity, authentication, static/dynamic authorization, Cedar, APIs, Zero Trust, verifiable credentials, AI agents | REGISTERED / MEAP |
| SEC-BOOK-002 | Justin Richer, Antonio Sanso, **OAuth 2 in Action**, Manning, **2017**, ISBN 9781617293276 | 362 | OAuth actors/grants, clients, protected resources, authorization server, token threats, OIDC | REGISTERED / HISTORICAL_PROTOCOL_EXAMPLES |
| SEC-BOOK-003 | Neil Madden, **API Security in Action**, Manning, **MEAP Version 10**, copyright 2020 | 929 | secure API development, cookies, tokens, JWT, OAuth/OIDC, identity and capability access, Kubernetes service-to-service, IoT | REGISTERED / MEAP |
| SEC-BOOK-004 | Aiyan Ma, **Identity Security for Software Development**, BPB, **First Edition 2026**, ISBN 978-93-65892-536 | 353 | history of non-human identities, service accounts, tokens, SSH keys, Kubernetes, DevOps, dynamic secrets and Zero Trust | REGISTERED |
| SEC-BOOK-005 | Sebastian Aigner, Roman Elizarov, Svetlana Isakova, Dmitry Jemerov, **Kotlin in Action, 2E**, Manning, EPUB (метаданные файла содержат дату 2024-04-30; это **дата записи метаданных**, не доказательство года финального издания) | EPUB | Kotlin language and programming; подробный разбор глав впереди | REGISTERED / EPUB_METADATA_VERIFIED |
| SEC-BOOK-006 | **Security Engineering**, файл `security-engineering.pdf`: указано имя Ross J. Anderson, но внутри явная строка **“Written by Bookey”** и разделы “Chapter 1 Summary” и “More Book Summary” | 369 | Конспективное вторичное изложение принципов, протоколов, контроля доступа, криптографии, API, распределённых систем и управления защитой | REGISTERED / **THIRD_PARTY_SUMMARY_NOT_ORIGINAL_BOOK** |

**Итог новой партии (27.11.2026):** шесть файлов — четыре PDF из ранее зарегистрированных книг (повторные загрузки, **не четыре новые книги**), один новый EPUB по Kotlin и один PDF, являющийся пересказом Bookey, **не полным текстом Security Engineering Россa Андерсона**. В репозитории хранится только каталог, не сами книги. Дубликаты по содержимому/хешам ещё не проверялись.

**Контроль корректности:** SEC-BOOK-002 — именно издание 2017, **не** OAuth 2 in Action Second Edition; наличие MEAP у книг 001 и 003 означает предварительную версию, примеры и рекомендации нуждаются в сверке. Имя автора книги 004 — **Aiyan Ma**, а не ранее предложенный авторами другого издания состав.

**Авторское право:** владельцем учебных PDF остаётся правообладатель. PDF/EPUB-файлы **не загружать** в публичный GitHub и не публиковать сканы/существенные главы/переводы. Реестр, собственные объяснения, алгоритмы, оригинальные программы и ссылки на страницы/главы допустимы. Не фиксировать в репозитории приватные пути, токены и секреты.

## Партия 3 — ещё 9 загруженных источников (27.11.2026)

**Состояние:** метаданные и доступные титульные страницы/оглавления просмотрены; полный постраничный анализ, код, интеграции и лабораторные испытания ещё не проводились. Новая партия: **7 книг/монографий и 2 академические работы**, не считать arXiv-работы издательскими книгами.

| ID | Подтверждённый источник и издание | PDF-страниц | Трек и извлекаемая практика | Статус |
|---|---|---:|---|---|
| **SEC-BOOK-007** | Myron Mortakis, **Unreal Engine Projects for Non-Coders**, BPB, First Edition **2025**, ISBN 978-93-65896-350 | 698 | Unreal Engine, визуальная разработка и VR; отдельная школа визуальных инструментов, **не базовый DevSecOps** | REGISTERED / TOC_AND_FRONTMATTER_CHECKED |
| **SEC-BOOK-008** | Mahja Sarschar, **Pipeline for Automated Code Generation from Backlog Items (PACGBI): Analysis of Potentials and Limitations of Generative AI for Web Development**, Springer Vieweg / BestMasters, **2025**, ISBN 978-3-658-47208-5, DOI [10.1007/978-3-658-47208-5](https://doi.org/10.1007/978-3-658-47208-5) | 141 | FATHER_CODEX: backlog → LLM code → review → test; исследование React и ограничений GenAI. В abstract подтверждаются ограничения по поддерживаемости, форматированию, UI и галлюцинациям | REGISTERED / ABSTRACT_READ |
| **SEC-BOOK-009** | Brent Laster, **Learning GitHub Actions: Automation and Integration of CI/CD with GitHub**, O’Reilly, **First Edition August 2023**, ISBN 9781098131074 | 570 | **TIMA CI/CD приоритет:** workflow, job, action, runners; построение автоматической сборки и испытаний. Сверять версии Actions с текущими docs | REGISTERED / FRONTMATTER_READ |
| **SEC-BOOK-010** | Jez Humble, David Farley, **Continuous Delivery: Reliable Software Releases Through Build, Test, and Deployment Automation**, Addison-Wesley / Pearson, **2010/2011** (в PDF copyright 2011), ISBN 978-0-321-60191-9 | 497 | **TIMA CI/CD приоритет:** deployment pipeline, воспроизводимость окружений, автоматизация сборки/тестирования и выпусков; история принципов, устаревающие примеры | REGISTERED / FRONTMATTER_READ |
| **SEC-PAPER-011** | Tao Li, Quanyan Zhu, **Agentic AI for Cyber Resilience: A New Security Paradigm and Its System-Theoretic Foundations**, arXiv **2512.22883v1**, **28.12.2025** | 29 | TIMA: resiliency, defender/attacker workflows, адаптация и теоретико-игровое описание безопасности; исследовательские гипотезы, не доказанный production-алгоритм | REGISTERED / ACADEMIC_PREPRINT |
| **SEC-PAPER-012** | Leroy Jacob Valencia, **Artificial Intelligence as the New Hacker: Developing Agents for Offensive Security**, Master's thesis, New Mexico Institute of Mining and Technology, **May 2024**, arXiv **2406.07561v1** | 54 | TIMA/POLYGON: исследование ReaperAI, RAG-памяти, командной оркестрации и ограничений; только разрешённый sandbox, отдельно проверять обобщаемость экспериментов | REGISTERED / THESIS |
| **SEC-BOOK-013** | Het Mehta, **AI Agents for Secure and Software-Defined Networking: Harnessing AI and SDN to Revolutionize Modern Work Environments**, Apress **2026**, DOI [10.1007/979-8-8688-2358-9](https://doi.org/10.1007/979-8-8688-2358-9) | 269 | TIMA network: SDN, intent-based networking, мультиагентное наблюдение; применять к разрешённой сетевой лаборатории | REGISTERED / TOC_INSPECTED |
| **SEC-BOOK-014** | **97 Things Every Application Security Professional Should Know: Collective Wisdom from the Experts**, eds. **Reet Kaur, Yabing Wang**, O’Reilly, **First Edition June 2024**, ISBN 9781098169459 | 487 | **TIMA AppSec приоритет:** 97 советов / 12 тем, SSDLC, threat modeling, SAST/SCA, управление уязвимостями, supply chain и AI security; это сборник эссе, не единый алгоритм | REGISTERED / PREFACE_READ |
| **SEC-BOOK-015** | Thomas De Vos, **Enterprise AI Agent Security: A Practical Guide to MCP Security, Prompt Injection Defense, RAG Security, and Agentic AI Governance**, предоставленный PDF (394 страницы); год и издатель **пока не подтверждены** | 394 | **TIMA/UAG высокий приоритет:** threat model агентных действий, identity, MCP tool poisoning, политики вызовов инструментов, capability matrix, Agent Contract, approvals, audit и rollback | REGISTERED / TOC_INSPECTED / PUBLICATION_METADATA_UNVERIFIED |

### Очерёдность извлечения знаний из этой партии

1. **SEC-BOOK-009 + SEC-BOOK-010** — объясняем CI/CD и воспроизводимость без подмены ключом теста CyberED; проектируем минимальный pipeline FATHER: commit → lint/test → SAST/SCA → SBOM → evidence → human approval.
2. **SEC-BOOK-014** — классифицируем советы AppSec и сопоставляем с SDL, NIST SSDF и применимой нормативной базой; из эссе извлекаем проверяемые практики, а не объявляем их техническими стандартами.
3. **SEC-BOOK-015 + SEC-BOOK-013** — роль TIMA как защищённого агента и сетевого координатора. Начать с контроля агентных полномочий, MCP, изоляции, сетевых ACL, политики read-only и audit. Контракты UAG и S2 согласуются с действующими ADR FATHER.
4. **SEC-BOOK-008 + SEC-PAPER-011** — варианты исследовательской архитектуры автоматической кодогенерации и устойчивости к атакам; выводы автора отделять от собственных предложений FATHER.
5. **SEC-PAPER-012** — оригинальный учебный *defensive validation* в локальном полигоне с разрешёнными целями, без автоматической эксплуатации внешних систем.
6. **SEC-BOOK-007** — отдельный визуальный трек школы, задачи Unreal/VR; не выдавать за базовый курс DevSecOps.

### Первые предполагаемые лабораторные (ещё не выполнены)

| LAB | Основа | Цель приёмки |
|---|---|---|
| TIMA-CI-001 | Laster + Humble/Farley | GitHub Actions workflow, unit tests, artifact checksum, воспроизводимый запуск, статус FAIL при ошибке |
| TIMA-APPSEC-001 | Kaur/Wang | SCA + SAST + секреты + SBOM, исследование одного реального finding с источниками |
| TIMA-AGENT-001 | De Vos + Windley/Ma | deny-by-default tool permission, контракт агента, контроль делегированных прав, negative tests |
| TIMA-RESILIENCE-001 | Li/Zhu | Условная модель отказа/восстановления и критерии наблюдения, без неподтверждённой автономности |
| TIMA-SDN-001 | Mehta | Учебная модель сегментации и допустимых операций, без воздействия на реальные сети |

**Правовой и инженерный контроль:** на публичный GitHub публиковать только собственный каталог, авторские разборы, original code, ссылки на точные фрагменты и подтверждённые evidence; **не загружать сами PDF и скопированные главы**. Все source files остаются только пользовательскими загрузками. До независимой проверки статусы `REGISTERED` / `PLANNED`, не `LEARNED` или `QUALIFIED`.

## Протокол разбора каждой главы

1. **SOURCE:** название книги, точная версия, глава, страница **PDF и печатная**, дата сверки; отдельно факты автора и самостоятельные дополнения.
2. **COVERAGE:** перечень всех смысловых разделов, понятий, предпосылок, терминов и известных ограничений; не пропускать тонкие различия (authentication ≠ authorization; OAuth authorization ≠ OIDC authentication).
3. **ALGORITHM:** последовательность шагов, actors, state machine, протокол обмена, policy decision, отрицательные сценарии, тестовые случаи; там, где алгоритма нет, честно отмечать архитектурный принцип.
4. **VERIFY:** сверка с актуальными официальными стандартами (NIST, IETF RFC, OWASP, Kubernetes) и применимой российской нормативной базой. Устаревшее не удалять, а помечать версией и причиной замены.
5. **TEACH:** для 12–14 лет — игра/история/схема; 15–17 — код и анализ; студент/Junior — Python API и тесты; Master — архитектурные альтернативы; Senior — ADR, политика доступа, риск, масштабирование и аудит.
6. **BUILD:** оригинальная учебная реализация в изолированной песочнице, предварительно исправленная по современным стандартам; запрещено без разрешения сканировать чужие сервисы.
7. **TEST:** позитивные/негативные тесты, edge cases, SAST/SCA/SBOM, deny-by-default, evidence SHA-256, независимая проверка POLYGON и Teach-Back.
8. **INTEGRATE:** новое знание в FATHER Analytical Core/SecGraph; предельно конкретные ссылки из уроков CyberED в релевантных местах; развитие FATHER UAG и авторизации AI-агентов.

Формат каждого артефакта: `source_id / chapter_id / concept_id / chapter_title / original_claim / verified_claim / official_source / applicability / algorithm / implementation / tests / evidence / teach_back / status`.

## Специализация новых источников

- **SEC-BOOK-005 / Kotlin:** дополнительный языковой трек программирования и разработки клиентов / сервисов. Не путать с учебником DevSecOps или безопасной разработки, которых тема книги сама по себе не заменяет. Практические задания TIMA применять только при возникновении Kotlin/Java-проекта.
- **SEC-BOOK-006 / Bookey Summary:** использовать как навигационный конспект, **не** как первоисточник цитат, оригинальных алгоритмов или точных страниц Ross Anderson. Для доказательной энциклопедии потребуется оригинальная работа/официальные материалы автора, иначе указывать `SECONDARY_SUMMARY_ONLY`.

## Очерёдность (не равна приоритету книг)

- **Пакет A, CyberED занятие 1:** `SEC-BOOK-001` главы 1–4 — цифровая идентичность, аутентификация и авторизация. Параллельно `SEC-BOOK-003` глава 1 — цели и принципы защиты API.
- **Пакет B:** `SEC-BOOK-002` главы 1–2, 13–14 — делегирование, участники OAuth и отличие от аутентификации; актуализировать по RFC и OAuth Security BCP.
- **Пакет C:** `SEC-BOOK-003` главы 2–9 — разработка защищённого API, сессии, JWT, OAuth, политики доступа.
- **Пакет D:** `SEC-BOOK-004` с главы 1 — машинные идентичности, сервисы и агенты; связать с FATHER UAG, Kind и Docker.
- **Пакет E:** `SEC-BOOK-001` главы 5–18 — динамические политики, Cedar, управляемая авторизация AI-агентов.

**Ничего не отмечать LEARNED или QUALIFIED до публикации индивидуального анализа, тестов и evidence.**
