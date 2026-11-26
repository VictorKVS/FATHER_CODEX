# FATHER Academy — второй слой: Security & Cost by Design

**Версия:** 0.1 / 2026-11-26. **Статус:** LEARNING_POLICY_DOCUMENTED / INTERACTIVE_DEMO / AUTOMATED_ENFORCEMENT_NOT_IMPLEMENTED.  
**Сайт:** [Интерактивная лаборатория выбора среды](security-layer.html).  
**Сквозные контракты:** S0 → S1 → S2 → S3 → S4 → S5 → S6 → S7.  
**Нормативные понятия:** [Security Wiki](../reference/wiki/SEC-IDENTITY-001.md), [Risk Wiki](../reference/wiki/SEC-RISK-001.md), [Справочник ИБ](../reference/security-regulations.html).

## Основная идея

Урок программирования сохраняет свободу эксперимента **в пределах изолированного, законного и безопасного полигона**. При переходе от эксперимента к разработке реального продукта включается второй слой требований: Security Architect, Cost Engineer, квалификация зависимостей и доказательства. **Любую библиотеку нельзя безусловно устанавливать даже в учебном режиме**: запрещены вредоносные компоненты, чужие секреты, доступ к промышленным данным, несанкционированные атаки и недоверенные исполняемые пакеты без изоляции.

| Режим | Что разрешается | Условие завершения / перехода |
|---|---|---|
| **EXPLORE**: учебная песочница | выбирать языки/пакеты, сравнивать версии, воспроизводить дефекты в одноразовой ограниченной среде без чувствительных данных | среда изолирована; цель и рамки известны; безопасность стенда подтверждена; результат объяснён |
| **BUILD**: проект/прототип | зависимости только через предложенный разработчиком и **проверенный для конкретного проекта** manifest/lock; допускаются осознанные исключения после human review | S0 IDEA Precheck, S1 requirements, S2 risks, S3 architecture, security-cost gate, S4 CI; критические неизвестные не замалчиваются |
| **RELEASE**: тиражирование/эксплуатация | только воспроизводимая утверждённая сборка с известным SBOM, provenance, проверками и планом управления уязвимостями | S5 POLYGON evidence, S6 risk owner approval, применимые нормы и rollback/monitoring; S7 continuous monitoring |

## Словарь политики пакетов

- **APPROVED / PROJECT-SCOPED:** идентификатор пакета, версия или разрешённый диапазон, origin, hashes, license, severity/risk, review_date, expiry, approver, environment; никогда не утверждать глобальную «безопасную версию на все времена».
- **BLOCKED:** подтверждённо запрещённые или недопустимые для данного контекста пакеты/версии, с причиной и доказательством.
- **REVIEW_REQUIRED:** обнаружены новые зависимости, неизвестные лицензии, закрыт источник, нет актуальной базы уязвимостей либо нарушена политика.
- **UNKNOWN:** свежесть vulnerability DB или происхождение компонента не доказаны, поэтому выпуск без отдельного решения запрещён.
- **EXCEPTION:** срочное разрешение исключения при документированном компенсирующем контроле, сроке окончания и подписи уполномоченного человека; не автоматический обход обязательных требований.

**Ни один режим не должен утверждать, что отсутствие известного CVE равно безопасности пакета.** Для выпуска требуется контекстный risk decision, а не только CVSS-порог.

## Производственная линия и данные

```text
IDEA → S0 Security Precheck ─────┐
  └── Cost Estimate ────────────┤
                                ↓
                     Security+Cost Feasibility Gate
                                ↓
S1 Requirements → S2 Threat/Risk → S3 Security Architecture
                                ↓
FATHER_CODEX + Package Proposal + Dependency Resolver
                                ↓
S4: lock/hashes + license + SCA + SAST + secrets + SBOM + provenance
                                ↓
S5: POLYGON tests → S6: human risk approval → RELEASE
                                ↓
S7: CVE/KEV/БДУ/версии → delta reassessment → affected code/risks
```

### Контракты

**`SECURITY_PRECHECK.json` (S0):** idea_id, assets, data_classes, actors, integrations, trust_boundaries, applicable_regulations (status: confirmed/potential/not-applicable), major_risks, assumptions, hard_constraints, cost_questions, decision, citations.

**`SECURITY_REQUIREMENTS.json` (S1):** requirement_id, normative_document, clause, revision, legal_applicability, controls, expected_test, cost_impact, owner.

**`THREAT_MODEL.json` (S2):** asset, threat_scenario, trust_boundary, exploit_preconditions, likelihood/impact model, uncertainty, risk_owner, treatment.

**`SECURITY_DESIGN.json` (S3):** architecture_option, alternatives, controls, ADR, TCO, residual_risk_estimate, gate decision.

**`DEPENDENCY_POLICY.json` (S4):** project_id, package, purl, version, source, lockfile_sha256, artifact_sha256, license, vulnerability_db_timestamp, findings, license_decision, review_owner, expiry, decision. A list of allowed packages is versioned and **project-specific**.

**`QUALIFICATION.json` (S5/S6):** tests, SBOM, CI logs, SHA256 evidence, signed approval/exception, risk owner, expiry and deployment target.

**`SECURITY_POSTURE.json` (S7):** installed inventory, CVE/KEV deltas, outdated evidence, reassessment outcomes, tickets and decisions.

## Автоматические правила принятия решения

1. Нет подтверждённых данных о пакете/версии/подписях или нет актуального SCA → `REVIEW_REQUIRED` / `UNKNOWN`, не `PASS`.
2. Новая зависимость или новая версия → проверить происхождение, транзитивные зависимости, лицензию, SBOM, CVE и воздействие на контекст проекта.
3. Уязвимость в эксплуатации не равна уязвимости в установленном пакете; оценить используемый путь, reachability, KEV/EPSS, меры, влияние и неопределённость.
4. При известном несовместимом требовании закона или доказанном неприемлемом риске → `BLOCKED`; исправить архитектуру или снять функцию, а не менять метку.
5. Если есть безопасная альтернатива, агент сравнивает их по **функции, лицензии, поддержке, риску, TCO и миграционным затратам**, а не просто по числу CVE.
6. Любое исключение на выпуск утверждает человек с полномочиями; POLYGON проверяет фактические evidence, а не заявления агента.
7. Переоценка рисков запускается при изменении SBOM/политик/источника угроз, просрочке проверки или изменении архитектуры.

## Практическая связка с уже проведённой LAB-001

**Факты на 26.11.2026:** Python unit 5/5, POLYGON local 11/11, Docker runtime и Kind Kubernetes runtime испытаны; CycloneDX SBOM сохранён. **Trivy CVE BLOCKED** (не удалось скачать DB), **NetworkPolicy enforcement NOT_VERIFIED**. Эти ограничения нельзя замаскировать зелёной меткой. Отдельный сайт-демо **не подключён к живому Docker/Trivy API**.

**Демонстрационное упражнение:** школьник выбирает библиотеку и проверяет, как изменяется статус при переходе EXPLORE → BUILD → RELEASE; студент объясняет lockfile/SBOM, Junior пишет тест отказа на неизвестной зависимости, Master реализует policy-as-code, Senior сравнивает стоимость ограничений и утверждает ADR.

## Обоснование из первоисточников

- [NIST SP 800-218, Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) — интеграция практик безопасной разработки в SDLC.
- [OWASP Software Component Verification Standard](https://owasp.org/www-project-software-component-verification-standard/) — контроль сторонних компонентов.
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/) — проверка известных зависимостей.
- [CycloneDX](https://cyclonedx.org/) — SBOM и отношения зависимостей.
- [NIST SP 800-161 Rev.1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final) — цепочка поставок.
- [ГОСТ Р 56939-2024 — карточка Росстандарта](https://protect.gost.ru/gost/details/f3818925-a96f-4f55-96e9-46b44720ee64) — инженерная методическая основа разработки безопасного ПО.
- [Реестр ФСТЭК](https://bdu.fstec.ru/) — проверка известных уязвимостей.
- [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — подтверждённая эксплуатация, не готовая оценка риска.

**Обязательность** конкретного закона/ГОСТ/приказа устанавливается для типа системы, оператора, данных и редакции документа; без такой проверки не писать «требование закона для любой программы».

**Критерий окончания текущего этапа:** видимое переключение учебных режимов в школьном UI, ссылки на регламенты, версионированный контракт политики, честные статусы LAB-001. Автоматическое принуждение сборки и квалификация — будущие этапы, не готовы по одному документу.
