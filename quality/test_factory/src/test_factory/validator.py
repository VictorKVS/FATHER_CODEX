"""Conservative, dependency-free PARTIAL validator for Test Factory catalog v1.

Architecture: registry-first; fail-closed; immutable approved expected outcomes.
This module does NOT implement every JSON Schema Draft 2020-12 keyword.
It does NOT execute security tests or independently verify PASS.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_FILE = ROOT / "schemas" / "test_case_v1.schema.json"
REGISTRY_FILE = ROOT / "catalog" / "source_registry.json"
ID_PATTERN = re.compile(r"^[A-Z][A-Z0-9_-]{5,63}$")
STEP_PATTERN = re.compile(r"^S-[0-9]{2,3}$")
STATUS = {"DESIGN", "REVIEWED", "APPROVED", "EXECUTED", "QUALIFIED"}
EVIDENCE_KINDS = {"HTTP", "DB_STATE", "AUDIT", "TOOL_COUNTER", "TRACE", "RUN_MANIFEST", "METRICS", "SOURCE_DIGEST"}


def load_json(path: Path) -> Any:
    # Reject duplicate JSON keys instead of relying on silent last-value-wins parsing.
    def no_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate JSON key: {key}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=no_duplicates)


def validate_registry(registry: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(registry, dict) or set(registry) != {"version", "sources"}:
        return ["source_registry: wrong root fields"]
    if registry["version"] != "1.0.0" or not isinstance(registry["sources"], list):
        return ["source_registry: unsupported version or sources type"]
    ids: set[str] = set()
    allowed = {"source_id", "category", "title", "locator", "reference", "rights_status", "checked_scope"}
    for idx, src in enumerate(registry["sources"]):
        if not isinstance(src, dict) or set(src) != allowed:
            errors.append(f"sources[{idx}]: missing or unknown fields")
            continue
        if any(not isinstance(src[k], str) or not src[k].strip() for k in allowed):
            errors.append(f"sources[{idx}]: source fields must be nonblank strings")
        if src["source_id"] in ids:
            errors.append(f"sources[{idx}]: duplicate ID")
        ids.add(src["source_id"])
        if src["category"] not in {"book", "standard", "project"}:
            errors.append(f"sources[{idx}]: invalid category")
        if src["rights_status"] not in {"RESTRICTED", "REFERENCE_ONLY", "OPEN_REFERENCE", "PROJECT_OWNED"}:
            errors.append(f"sources[{idx}]: invalid rights_status")
    if not ids:
        errors.append("source_registry: empty catalog")
    return errors


def validate_case(case: Any, registry: Any, schema: Any, *, for_release: bool = False) -> list[str]:
    errors: list[str] = []
    if not isinstance(case, dict):
        return ["case: not an object"]
    if not isinstance(schema, dict) or schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        return ["schema: unsupported or missing"]
    required = set(schema["required"])
    allowed = set(schema["properties"])
    for key in sorted(required - set(case)):
        errors.append(f"case: missing {key}")
    for key in sorted(set(case) - allowed):
        errors.append(f"case: unknown field {key}")
    if errors:
        return errors
    if case["schema_version"] != "1.0.0":
        errors.append("case: unsupported version")
    if not isinstance(case["case_id"], str) or not ID_PATTERN.fullmatch(case["case_id"]):
        errors.append("case: invalid case_id")
    if case["status"] not in STATUS:
        errors.append("case: invalid status")
    for key, minlen in (("system", 2), ("objective", 30), ("expected_result", 25)):
        if not isinstance(case[key], str) or len(case[key].strip()) < minlen:
            errors.append(f"case: {key} is missing/too short")
    for key in ("requirement_ids", "contract_ids", "threat_ids"):
        value = case[key]
        if not isinstance(value, list) or not value or any(not isinstance(x, str) or len(x) < 3 for x in value) or len(value) != len(set(value)):
            errors.append(f"case: {key} must contain unique nonblank IDs")
    for key in ("preconditions", "setup", "negative_assertions"):
        value = case[key]
        if not isinstance(value, list) or not value or any(not isinstance(x, str) or len(x.strip()) < 8 for x in value):
            errors.append(f"case: {key} must contain meaningful statements")
    source_ids = {s["source_id"] for s in registry.get("sources", []) if isinstance(s, dict) and isinstance(s.get("source_id"), str)}
    refs = case["source_refs"]
    if not isinstance(refs, list) or not refs:
        errors.append("case: no sources")
    else:
        used = set()
        for idx, ref in enumerate(refs):
            if not isinstance(ref, dict) or set(ref) != {"source_id", "locator", "application_note"}:
                errors.append(f"source_refs[{idx}]: missing/unknown keys")
                continue
            if ref["source_id"] not in source_ids:
                errors.append(f"source_refs[{idx}]: unresolved source {ref['source_id']}")
            if ref["source_id"] in used:
                errors.append(f"source_refs[{idx}]: duplicate source")
            used.add(ref["source_id"])
            if not isinstance(ref["locator"], str) or len(ref["locator"].strip()) < 3:
                errors.append(f"source_refs[{idx}]: missing locator")
            if not isinstance(ref["application_note"], str) or len(ref["application_note"].strip()) < 10:
                errors.append(f"source_refs[{idx}]: missing rationale")
    steps = case["steps"]
    if not isinstance(steps, list) or len(steps) < 2:
        errors.append("case: insufficient steps")
    else:
        step_ids = set()
        for idx, step in enumerate(steps):
            if not isinstance(step, dict) or set(step) != {"step_id", "stimulus", "expected", "observables"}:
                errors.append(f"steps[{idx}]: missing/unknown fields")
                continue
            sid = step["step_id"]
            if not isinstance(sid, str) or not STEP_PATTERN.fullmatch(sid) or sid in step_ids:
                errors.append(f"steps[{idx}]: invalid or duplicate id")
            step_ids.add(sid)
            for key in ("stimulus", "expected"):
                if not isinstance(step[key], str) or len(step[key].strip()) < 8:
                    errors.append(f"steps[{idx}]: no {key}")
            obs = step["observables"]
            if not isinstance(obs, list) or not obs or any(not isinstance(x, str) or len(x.strip()) < 8 for x in obs):
                errors.append(f"steps[{idx}]: observables missing")
    evidence = case["evidence_plan"]
    if not isinstance(evidence, list) or len(evidence) < 2:
        errors.append("case: insufficient evidence plan")
    else:
        kinds = set()
        for idx, item in enumerate(evidence):
            if not isinstance(item, dict) or set(item) != {"kind", "description", "hash_required"}:
                errors.append(f"evidence_plan[{idx}]: invalid structure")
                continue
            if item["kind"] not in EVIDENCE_KINDS or item["kind"] in kinds:
                errors.append(f"evidence_plan[{idx}]: bad or duplicate evidence kind")
            kinds.add(item["kind"])
            if item["hash_required"] is not True or not isinstance(item["description"], str) or len(item["description"].strip()) < 10:
                errors.append(f"evidence_plan[{idx}]: require description and SHA256")
    review = case["review"]
    if not isinstance(review, dict) or set(review) != {"owner", "status"}:
        errors.append("case: review is malformed")
    elif not isinstance(review["owner"], str) or len(review["owner"].strip()) < 3 or review["status"] not in {"PENDING", "APPROVED"}:
        errors.append("case: review owner/status invalid")
    if case["status"] in {"REVIEWED", "APPROVED", "EXECUTED", "QUALIFIED"} and isinstance(review, dict) and review.get("status") != "APPROVED":
        errors.append("case: advanced status without reviewer approval")
    if for_release:
        # An approved case alone must NEVER cause a release: separate qualification and human artifacts are required.
        errors.append("RELEASE BLOCKED: no independent POLYGON evidence and human signed release decision")
    return errors


def validate_catalog(root: Path = ROOT, *, for_release: bool = False) -> dict[str, list[str]]:
    registry = load_json(root / "catalog" / "source_registry.json")
    schema = load_json(root / "schemas" / "test_case_v1.schema.json")
    global_errors = validate_registry(registry)
    results: dict[str, list[str]] = {}
    cases = sorted((root / "catalog" / "cases").glob("*.json"))
    if not cases:
        return {"catalog": ["No test cases"]}
    for file in cases:
        try:
            item = load_json(file)
            results[file.name] = global_errors + validate_case(item, registry, schema, for_release=for_release)
        except (ValueError, OSError, json.JSONDecodeError) as exc:
            results[file.name] = [f"JSON parse/read failure: {exc}"]
    return results
