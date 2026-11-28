import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from test_factory.validator import load_json, validate_case, validate_catalog, validate_registry  # noqa: E402


class CatalogValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = load_json(ROOT / "schemas" / "test_case_v1.schema.json")
        cls.registry = load_json(ROOT / "catalog" / "source_registry.json")
        cls.case = load_json(ROOT / "catalog" / "cases" / "SADEQ_API_001.json")

    def clone(self):
        return copy.deepcopy(self.case)

    def test_reference_registry_is_well_formed(self):
        self.assertEqual(validate_registry(self.registry), [])

    def test_example_passes_structural_validation_not_security_evaluation(self):
        self.assertEqual(validate_case(self.case, self.registry, self.schema), [])

    def test_example_remains_design_pending(self):
        self.assertEqual(self.case["status"], "DESIGN")
        self.assertEqual(self.case["review"]["status"], "PENDING")

    def test_unknown_field_is_rejected(self):
        case = self.clone()
        case["skip_authorization"] = True
        self.assertIn("unknown field", " ".join(validate_case(case, self.registry, self.schema)))

    def test_unresolved_book_source_is_rejected(self):
        case = self.clone()
        case["source_refs"][0]["source_id"] = "BOOK-FAKE"
        self.assertIn("unresolved source", " ".join(validate_case(case, self.registry, self.schema)))

    def test_no_negative_assertions_is_rejected(self):
        case = self.clone()
        case["negative_assertions"] = []
        self.assertIn("negative_assertions", " ".join(validate_case(case, self.registry, self.schema)))

    def test_no_required_evidence_is_rejected(self):
        case = self.clone()
        case["evidence_plan"] = []
        self.assertIn("evidence", " ".join(validate_case(case, self.registry, self.schema)))

    def test_duplicate_step_id_is_rejected(self):
        case = self.clone()
        case["steps"][1]["step_id"] = "S-01"
        self.assertIn("duplicate", " ".join(validate_case(case, self.registry, self.schema)))

    def test_duplicate_json_keys_rejected_on_parse(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "duplicate.json"
            path.write_text('{"status":"DESIGN","status":"QUALIFIED"}', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
                load_json(path)

    def test_fake_qualification_without_signoff_is_rejected(self):
        case = self.clone()
        case["status"] = "QUALIFIED"
        self.assertIn("without reviewer approval", " ".join(validate_case(case, self.registry, self.schema)))

    def test_release_cannot_self_approve(self):
        case = self.clone()
        case["status"] = "QUALIFIED"
        case["review"] = {"owner": "security-reviewer", "status": "APPROVED"}
        errors = validate_case(case, self.registry, self.schema, for_release=True)
        self.assertIn("RELEASE BLOCKED", " ".join(errors))

    def test_unhashable_status_fails_closed(self):
        case = self.clone()
        case["status"] = ["QUALIFIED"]
        self.assertIn("invalid status", " ".join(validate_case(case, self.registry, self.schema)))

    def test_unhashable_source_id_fails_closed(self):
        case = self.clone()
        case["source_refs"][0]["source_id"] = ["BOOK-AGSEC"]
        self.assertIn("unresolved source", " ".join(validate_case(case, self.registry, self.schema)))

    def test_unhashable_evidence_kind_fails_closed(self):
        case = self.clone()
        case["evidence_plan"][0]["kind"] = ["HTTP"]
        self.assertIn("bad or duplicate", " ".join(validate_case(case, self.registry, self.schema)))

    def test_unhashable_registry_id_fails_closed(self):
        registry = copy.deepcopy(self.registry)
        registry["sources"][0]["source_id"] = ["BOOK-CD"]
        self.assertIn("invalid source_id", " ".join(validate_registry(registry)))

    def test_catalog_scans_all_cases(self):
        self.assertEqual(validate_catalog(ROOT), {"SADEQ_API_001.json": []})


if __name__ == "__main__":
    unittest.main()
