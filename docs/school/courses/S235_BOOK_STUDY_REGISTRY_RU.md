# CyberED S-235 / FATHER Academy — реестр разбора четырёх книг

**Дата регистрации:** 2026-11-26  
**Статус:** PDF_METADATA_AND_TOC_INSPECTED / CHAPTER_ANALYSIS_PENDING / LABS_NOT_QUALIFIED  
**Владельцы:** ALINA (источники, фрагменты, версии, граф знаний), FATHER_CODEX (учебные версии и Python), POLYGON (испытания).  
**Связанный курс:** [CyberED S-235](CYBERED_S235_SECURE_DEVELOPMENT_RU.md).  
**Нормативный справочник:** [Российские акты и ГОСТы](../../reference/security-regulations.html).

## Полученные файлы — прочитаны титульные страницы и краткие оглавления, полный разбор впереди

| ID | Книга, данные **из переданного PDF** | Страниц в PDF | Темы, подтверждённые оглавлением | Статус |
|---|---|---:|---|---|
| SEC-BOOK-001 | Phillip J. Windley, **Authorization in Action**, Manning, **MEAP Version 6**, copyright 2026 | 617 | digital identity, authentication, static/dynamic authorization, Cedar, APIs, Zero Trust, verifiable credentials, AI agents | REGISTERED / MEAP |
| SEC-BOOK-002 | Justin Richer, Antonio Sanso, **OAuth 2 in Action**, Manning, **2017**, ISBN 9781617293276 | 362 | OAuth actors/grants, clients, protected resources, authorization server, token threats, OIDC | REGISTERED / HISTORICAL_PROTOCOL_EXAMPLES |
| SEC-BOOK-003 | Neil Madden, **API Security in Action**, Manning, **MEAP Version 10**, copyright 2020 | 929 | secure API development, cookies, tokens, JWT, OAuth/OIDC, identity and capability access, Kubernetes service-to-service, IoT | REGISTERED / MEAP |
| SEC-BOOK-004 | Aiyan Ma, **Identity Security for Software Development**, BPB, **First Edition 2026**, ISBN 978-93-65892-536 | 353 | history of non-human identities, service accounts, tokens, SSH keys, Kubernetes, DevOps, dynamic secrets and Zero Trust | REGISTERED |

**Контроль корректности:** SEC-BOOK-002 — именно издание 2017, **не** OAuth 2 in Action Second Edition; наличие MEAP у книг 001 и 003 означает предварительную версию, примеры и рекомендации нуждаются в сверке. Имя автора книги 004 — **Aiyan Ma**, а не ранее предложенный авторами другого издания состав.

**Авторское право:** владельцем учебных PDF остаётся правообладатель. PDF-файлы **не загружать** в публичный GitHub и не публиковать сканы/существенные главы/переводы. Реестр, собственные объяснения, алгоритмы, оригинальные программы и ссылки на страницы/главы допустимы. Не фиксировать в репозитории приватные пути, токены и секреты.

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

## Очерёдность (не равна приоритету книг)

- **Пакет A, CyberED занятие 1:** `SEC-BOOK-001` главы 1–4 — цифровая идентичность, аутентификация и авторизация. Параллельно `SEC-BOOK-003` глава 1 — цели и принципы защиты API.
- **Пакет B:** `SEC-BOOK-002` главы 1–2, 13–14 — делегирование, участники OAuth и отличие от аутентификации; актуализировать по RFC и OAuth Security BCP.
- **Пакет C:** `SEC-BOOK-003` главы 2–9 — разработка защищённого API, сессии, JWT, OAuth, политики доступа.
- **Пакет D:** `SEC-BOOK-004` с главы 1 — машинные идентичности, сервисы и агенты; связать с FATHER UAG, Kind и Docker.
- **Пакет E:** `SEC-BOOK-001` главы 5–18 — динамические политики, Cedar, управляемая авторизация AI-агентов.

**Ничего не отмечать LEARNED или QUALIFIED до публикации индивидуального анализа, тестов и evidence.**
