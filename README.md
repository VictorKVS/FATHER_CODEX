# FATHER_CODEX

**FATHER Programmer Agent — Autonomous Software Engineering**

Status: **Bootstrap / architecture definition**

FATHER_CODEX is the programmer specialization of the shared FATHER Engineering Platform. It is not a second independent core.

## Mission

Convert approved requirements and architecture into maintainable, secure, tested software with traceable provenance.

## Engineering pipeline

1. Intake: receive requirements, constraints and acceptance criteria.
2. Analyze: validate scope with the FATHER Analytical Core.
3. Design: consume and review the architecture / Development Pack.
4. Implement: select language, framework, coding conventions, and tools.
5. Verify: run linting, tests, dependency and security checks.
6. Review: require approval for consequential changes and external actions.
7. Release: generate build artifacts, documentation, manifest and provenance records.

## Planned modules

- `agent/`: programming agent orchestration and policies
- `adapters/`: integration contracts with FATHER, other agents and model/tool providers
- `languages/`: programming-language specializations
- `workflows/`: project and development workflows
- `quality/`: tests, static analysis, evaluation and security gates
- `signature/`: optional terminal/ASCII/Code Art identity
- `provenance/`: hashes, signed manifests, dependencies, licenses and evidence references
- `docs/`: architecture decisions, requirements, development journal and operating instructions
- `tests/`: automated test suite

Folders are proposed, not yet implemented.

## Design principles

- Preserve clear, maintainable source code: artistic formatting must never obstruct compilation, testing, auditing or accessibility.
- FATHER Code Signature is a distinctive visual mark, **not** standalone legal proof of ownership.
- Verify origin, human contributions, permissions and third-party licenses; do not automatically claim exclusive ownership of generated or reused code.
- Never put private keys, credentials or confidential evidence in the public repository.
- Require review and permission before executing destructive commands, deploying or modifying production.
- Record tool invocations and evidence with timestamps; cryptographic signing must use an authorized key.
- Prefer shared FATHER services to copying infrastructure into this repository.

## AI Academy, Programmer Coach and Agent Factory

**Единая точка входа:** [FATHER_CODEX Academy — архитектура и карта проекта](docs/academy/README.md).

- [Школа ИИ-агентов (русский интерактивный MVP)](docs/school/index.html)
- [Учебная программа CH01–CH07](docs/school/COURSE_PROGRAM_RU.md)
- [Полное освоение теории школьником](docs/school/THEORY_MASTERY_SYSTEM_RU.md)
- [Тренер программиста от новичка до senior track](docs/academy/FATHER_CODEX_PROGRAMMER_COACH_V1_RU.md)
- [IDEA+](docs/protocols/FATHER_IDEA_PLUS_PROTOCOL_V1.md) и [Cost Engineering](docs/protocols/FATHER_COST_ENGINEERING_PROTOCOL_V1.md)
- [Инженерный дашборд FATHER](docs/index.html)
- [Библиотека первоисточников и Python-примеров ALINA](https://github.com/VictorKVS/alina-knowledge-worker/tree/feature/father-book-library-index-20261122/library/books/LIB-0040_Agentic_Design_Patterns)

FATHER_CODEX — продуктовый репозиторий и место интеграции. ALINA — поставщик знаний и исходных примеров по контрактам; FATHER Core, UAG и POLYGON остаются общими службами, а не копируются. Наличие документа не означает реализацию, проведённые испытания или профессиональную квалификацию.

## Initial milestones

- **M0** — Inventory current FATHER coding workflows, tool adapters and repositories.
- **M1** — Define agent contracts and build a minimal working programming loop.
- **M2** — Connect sandboxed execution, tests and DevSecOps gates.
- **M3** — Add provenance and FATHER Code Signature.
- **M4** — Integrate in FATHER UI / Visual Agent Designer.

## Repository

Local workspace intended by project owner: `G:\\1\\FATHER_CODEX`

Remote: https://github.com/VictorKVS/FATHER_CODEX

License: **not yet selected**. Public visibility does not grant an open-source license.

## Secure Development / CyberED S-235

- [FATHER NextGen School — S-235 «Основы безопасной разработки»](docs/school/courses/CYBERED_S235_SECURE_DEVELOPMENT_RU.md): пять модулей CyberED, адаптация для школьников, студентов, Junior / Master / Senior и POLYGON. Это регистрация учебного трека, **не подтверждение прохождения курса**.

## FATHER Test Factory — библиотека и система испытаний

- [Общая архитектура, книги, стандарты, модели угроз, ПМИ и каталог тестов](quality/test_factory/README.md)
- [Карта первоисточников и их применения](quality/test_factory/docs/BOOKS_AND_STANDARDS.md)
- [Первая машиночитаемая методика SADEQ API-001](quality/test_factory/catalog/cases/SADEQ_API_001.json)
- [Исходный код валидатора](quality/test_factory/src/test_factory/validator.py), проверяется unit-тестами (на момент создания: **16 PASS** локально). Это **не** доказательство безопасности SADEQ; квалификация и допуск к выпуску заблокированы до независимых испытаний POLYGON и человеческого решения.
