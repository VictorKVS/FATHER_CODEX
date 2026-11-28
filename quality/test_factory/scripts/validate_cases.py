"""CLI: validate test case design; release mode deliberately fails until independent approval."""
from pathlib import Path
import argparse
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from test_factory.validator import validate_catalog  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="FATHER Test Factory catalog validator, NOT test runner")
    parser.add_argument("--release", action="store_true", help="require independent POLYGON + human release gate")
    args = parser.parse_args()
    results = validate_catalog(ROOT, for_release=args.release)
    failed = False
    for name, errors in results.items():
        if errors:
            failed = True
            print(f"BLOCKED {name}: {', '.join(errors)}")
        else:
            print(f"CATALOG_VALID {name} (DESIGN only; NO API TEST EXECUTED)")
    print("RELEASE_DENIED" if args.release else "STRUCTURAL_CATALOG_CHECK_DONE")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
