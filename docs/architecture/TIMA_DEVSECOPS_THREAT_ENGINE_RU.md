# TIMA — DevSecOps Threat Engineering / FATHER

**Статус:** ARCHITECTURE_PROPOSED / TRAINING_UI_CREATED / INTEGRATION_NOT_IMPLEMENTED / NO_POLYGON_EVIDENCE. **Дата:** 2026-11-26.

## 1. Роль

**TIMA** — инженерный агент автоматизации безопасности разработки и инфраструктуры FATHER. Расширяем прежнюю роль TIMA (Docker / Kubernetes / CI/CD, SBOM и проверка среды) на **Threat Engineering**: системный поиск угроз, дерево атак, риск-контекст, контроль зависимостей, проверки и evidence. **TIMA не заменяет Security Architect, владельца риска и независимый POLYGON**.

### Полномочия и запреты

- READ-ONLY сбор состояния по умолчанию. Ни удалений, ни изменения политик, ни сетевого сканирования чужих систем без явного разрешения на конкретную цель.
- Выдвигает **гипотезы** о возможных угрозах, фиксирует ссылки и неопределённость; не объявляет их доказанными.
- Оформляет отдельные проекты мер и варианты стоимости; не принимает существенные остаточные риски.
- Не присваивает статус `QUALIFIED` без воспроизводимых результатов POLYGON; UNKNOWN/неактуальная vulnerability DB → REVIEW_REQUIRED/BLOCKED.
- Не генерирует эксплуатационные payload для внешних систем и не включает скрытое сканирование в учебном сайте.

## 2. Методический набор по назначению

| Метод | Задача TIMA | Проверка/источник |
|---|---|---|
| **DFD / trust boundaries** | Выяснить границы и входы системы | OWASP Threat Modeling Cheat Sheet |
| **STRIDE** | Систематизировать 6 классов угроз по процессам/потокам | OWASP; Microsoft Threat Modeling Tool |
| **PASTA** | Связать бизнес-цели, архитектуру, сценарии атак и риски | OWASP Guide / PASTA primary literature, chapter details to verify |
| **LINDDUN** | Найти угрозы приватности | linddun.org/methods |
| **OCTAVE Allegro** | Найти важнейшие информационные активы и последствия | Carnegie Mellon SEI |
| **Attack Trees** | Разложить цель атакующего на AND/OR путь с проверяемыми условиями | OWASP Threat Modeling Cheat Sheet |
| **MITRE ATT&CK / CAPEC / CWE** | Уточнить техники/шаблоны атак/типы ошибок | MITRE official knowledge bases |
| **Методика ФСТЭК 05.02.2021** | Определить актуальные угрозы и требования к модели по области применения | ФСТЭК; сверить редакцию и пункты |
| **NIST SP 800-30** | Отдельно обосновать вероятность, последствия и неопределённость | NIST |
| **CVSS / KEV / EPSS / SCA** | Обосновать severity/exploitation signals обнаруженных CVE | FIRST, CISA, Trivy, NVD |

**Граница терминов:** модель угроз ≠ перечень CVE; CVSS severity ≠ вероятность; корпоративная 5×5 матрица ≠ методика ФСТЭК ≠ доказательная FAIR-модель. Угрозы без известных CVE существуют, так же как CVE может быть неприменима к конкретному стенду.

## 3. Сквозная инженерная цепочка

```text
IDEA+ S0  →  scope/active assets/consequences  →  initial risk register
     ↓
S1        →  applicable requirements / security contract
     ↓
TIMA S2   →  inventory + DFD + STRIDE + LINDDUN + FSTEK relevance
     ↓
           →  threat scenarios and AND/OR attack trees
     ↓
ALINA     →  SecGraph grounded evidence / conflict + uncertainty
     ↓
IDEA+     →  update SAME risk_id in ONE risk register
     ↓
S3 + Cost →  treatment options, security design and cost/TCO
     ↓
S4        →  code, dependency and IaC controls (SAST, SCA, SBOM)
     ↓
S5        →  independent POLYGON evidence and regressions
     ↓
S6/S7     →  human release/risk sign-off and re-evaluation
```

## 4. Межкомпонентные контракты (ПРОЕКТ, без работающего API)

### 4.1. THREAT_MODEL_REQUEST — вход TIMA

```json
{
  "schema": "father.tima.threat_model.request.v0",
  "project_id": "example-only",
  "revision": "design-rev-01",
  "scope": {"system_type": "AI_AGENT", "excluded": []},
  "assets": [{"id": "document-store", "type": "CONFIDENTIAL_DOCUMENTS"}],
  "components": [],
  "flows": [],
  "trust_boundaries": [],
  "requirements_refs": [],
  "regulatory_scope": {"ru_fstek_method_applicability": "UNKNOWN"},
  "sources": []
}
```

### 4.2. THREAT_SCENARIO — результат S2

```json
{
  "schema": "father.tima.threat_scenario.v0",
  "threat_id": "THREAT-DEMO-001",
  "risk_id": null,
  "attacker": {"type": "UNKNOWN", "capabilities": []},
  "target_asset": "document-store",
  "goal": "unauthorized document access",
  "entrypoint": "rag-query",
  "trust_boundary": "user-to-data",
  "classification": {"stride": "I", "cwe": [], "capec": [], "attack": [], "bdu": []},
  "assumptions": ["hypothetical-only"],
  "evidence_refs": [],
  "applicability": "UNKNOWN",
  "status": "HYPOTHESIS"
}
```

### 4.3. ATTACK_TREE — дерево

```json
{
  "schema": "father.tima.attack_tree.v0",
  "tree_id": "TREE-DEMO-001",
  "root": "GOAL_UNAUTHORIZED_DOCUMENT_ACCESS",
  "operator": "OR",
  "children": [
    {"id": "PATH_A", "operator": "AND", "preconditions": ["credential-exposed", "accepted-authentication"]},
    {"id": "PATH_B", "operator": "AND", "preconditions": ["foreign-object-request", "broken-object-authorization"]},
    {"id": "PATH_C", "operator": "AND", "preconditions": ["mixed-index", "missing-document-acl", "missing-output-authz"]}
  ],
  "source_refs": [],
  "status": "HYPOTHESIS"
}
```

Зависимые события в деревьях **не считаются независимыми** без обоснования. Сложение вероятностей в OR/AND автоматически запрещено: общие предпосылки и корреляция способны исказить результат.

### 4.4. RISK_ASSESSMENT_DRAFT — проекция IDEA+

```json
{
  "schema": "father.risk.assessment.draft.v0",
  "risk_id": "ASSIGNED_BY_IDEA_PLUS",
  "threat_ids": ["THREAT-DEMO-001"],
  "method": "ORG_QUALITATIVE_5X5",
  "likelihood": {"level": null, "rationale": "UNKNOWN"},
  "impact": {"level": null, "rationale": "UNKNOWN"},
  "initial_risk": "UNKNOWN",
  "residual_risk": "UNKNOWN",
  "decision_owner": "HUMAN_ROLE_REQUIRED",
  "mitigations": [],
  "cost_options": [],
  "evidence_refs": [],
  "approval_status": "NOT_APPROVED"
}
```

## 5. Покрытие SAST/SCA/IaC и тестами

**Не подменять методы:** Trivy, Grype и OSV-Scanner выявляют известные уязвимости в компонентах; Semgrep анализирует исходный код; Threat Modeling обнаруживает и архитектурные угрозы без CVE. Предусмотреть Trivy для образов/SBOM, Grype как вторую независимую выборку, OSV-Scanner для языковых зависимостей, Semgrep для SAST; для Python-контуров позднее определить потребность в Bandit. Network scanning только для явно разрешённых целей.

**FATHER LAB-001 исторически:** Trivy vulnerability DB download BLOCKED, NetworkPolicy NOT VERIFIED. Не объявлять работу сканеров или успешную квалификацию без новых логов.

## 6. Матрица рисков и правила интерпретации

- Пользователь видит иллюстративную матрицу 5×5 и может менять две **порядковые** оценки.
- `index=likelihood_level*impact_level` — **только учебный индекс**. Без утверждённых организационных критериев или данных он не является измерением вероятности и не должен управлять реальным RELEASE gate.
- Анализ актуальности ФСТЭК сохраняется отдельно, с идентификаторами БДУ, нарушителей, негативных последствий и обоснованием применимости.
- Упорядочивание целей атакующего строится с учётом пересекающихся предпосылок и неполноты дерева; нельзя автоматически назначать вероятность корневому узлу по условным AND/OR.
- Для существенных остаточных рисков нужен подписанный выбор уполномоченного человека; неизвестное не равно LOW.

## 7. Этапы реализации и квалификация

| Этап | Артефакт | Проверка |
|---|---|---|
| **P0 (выполнено в документации)** | Методология, JSON drafts, браузерный интерактивный тренажёр | Проверить файлы в GitHub; программные тесты не запускались |
| **P1** | Импорт DFD/asset inventory из IDEA+/FATHER_CODEX, версионирование | Deterministic schema tests, точные границы |
| **P2** | Генератор кандидатов STRIDE/LINDDUN + деревья AND/OR | Coverage tests, human review |
| **P3** | ALINA SecGraph: доказательства, библиография, контроль противоречий | Source provenance, negative tests |
| **P4** | ONE IDEA+ Risk Register, S3/Cost, FSTEK applicability | No duplicates; unknown states; approval required |
| **P5** | Trivy/Grype/Semgrep/OSV and POLYGON evidence pipeline | Working DB, SBOM+hash, CI, manual signed release |

### Engineering baseline

Human-owned commits, ADR, component/data/security/qualification contracts, SHA-256 provenance, SBOM/build attestations, signed tags for important releases, reproducible unit/integration tests, ownership metadata. Нельзя говорить «готово» только потому, что существует страница.

## 8. Библиография

- https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
- https://owasp.org/www-project-threat-modeling/
- https://owasp.org/projects/threat-dragon
- https://linddun.org/methods/
- https://www.sei.cmu.edu/library/introducing-octave-allegro-improving-the-information-security-risk-assessment-process/
- https://attack.mitre.org/ ; https://capec.mitre.org/ ; https://cwe.mitre.org/
- https://www.consultant.ru/document/cons_doc_LAW_378330/ (справочная публикация методики ФСТЭК от 05.02.2021; актуальную официальную редакцию проверять перед применением)
- https://bdu.fstec.ru/
- https://csrc.nist.gov/pubs/sp/800/30/r1/final
- https://www.first.org/cvss/

## Связанные документы

- [Общий справочник угроз](../reference/wiki/SEC-THREAT-MODELING-001.md)
- [Общий реестр рисков IDEA+](ADR-IDEA-RISK-REGISTER-RU.md)
- [Лаборатория TIMA](../school/tima-threat-lab.html)
- [Сканеры и лаборатория CVE](../school/vulnerability-scanners.html)
