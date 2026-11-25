# FATHER Engineering Dashboard — deployment and data contracts

**Version:** v0.1 (interactive static MVP)  
**Source:** [docs/index.html](index.html)  
**Status:** SOURCE_COMMITTED / GITHUB_PAGES_NOT_VERIFIED / INTEGRATIONS_PARTIAL

## Purpose

Present the FATHER IDEA+ → world/internal prior art → feasibility → FinOps → Planning → Agent Factory → POLYGON production line as one connected, visual engineering site, not scattered documents.

## Publish to GitHub Pages

1. Open https://github.com/VictorKVS/FATHER_CODEX/settings/pages
2. Under **Build and deployment**, select **Deploy from a branch**.
3. Branch: `main`; folder: `/docs`; save.
4. Wait for GitHub to report the deployment and use the Pages URL displayed in GitHub settings.
5. Verify that all five sections and the cost calculator work. Check browser network console for any GitHub API failures.

The typical URL may be `https://victorkvs.github.io/FATHER_CODEX/`, **but is not verified or claimed active** until Pages deployment completes. GitHub Pages must be enabled by an authorized repository administrator.

## Current panels

| Panel | Current data | Status |
|---|---|---|
| Overview | IDEA+/FinOps diagrams, static labels with explicit caveats | UI implemented; live integrations pending |
| IDEA+ | Direct link to versioned protocol | Documented, not enforced |
| Agent Factory | Verified study-plan snapshot of book chapters and statuses | Static snapshot, real-time evidence pending |
| Economics | Real interactive math with user-editable hypothetical rates | Functional UI; provider tariffs/TCO integration pending |
| Evidence | Versioned public GitHub links and API latest commits | Live public API attempt with graceful fallback |

The site intentionally **does not invent** qualification rates, token usage, cloud tariffs or execution counts.

## Next implementation phases

### P1 — Shared event & evidence schema
Define and version fields: `project_id, run_id, module_id, pattern_id, source_commit, event_ts, status, evidence_url, actor, model, provider, usage_tokens, cost_currency, measured_cost, qualification_scope`. Keep sensitive data off the public site.

### P2 — Read-only metrics backend
Export redacted, approved JSON snapshots to a public or access-controlled feed. Do not publish secrets, user prompts, protected evidence, private repo content, raw LLM logs, or company usage data.

### P3 — Chart by phase
For each IDEA+ checkpoint show required inputs, actual outputs, links, risks, progress, source provenance, tests and failures. Build filterable lineage: `Idea -> Requirement -> Algorithm -> Component -> Test -> Evidence -> Release`.

### P4 — Cost instrumentation
Add provider-specific, timestamped and regional price cards; captured token usage, cache, RAG embedding/index costs, storage/transfer and local GPU expenses. Compare cost **per independently accepted outcome**, not only API calls. Present LOW/BASE/HIGH scenarios and budget limit alarms.

### P5 — Qualification and deployment
Validate accessibility, mobile layout, CSP, external data sanitization, test harness, GitHub Pages publication. Public dashboard only for approved and non-sensitive data.

## Static security constraints
- Public GitHub API calls use read-only unauthenticated GET.
- No tokens are embedded in the frontend.
- The current renderer builds a small status widget from public GitHub metadata; introduce DOM-safe structured rendering before accepting any untrusted user or private content.
- GitHub API rate limits and offline states are expected.
- No front-end operation is authorized to change repos or execute tools.
