"""Fail if generated Markdown differs from the authoritative YAML records."""

from __future__ import annotations

import sys

from scripts.build_pages import GENERATED_DIRS, MARKER, ROOT, render_all
from scripts.validate import validate


def main() -> int:
    errors = validate()
    if errors:
        print("Validation failed; generated files cannot be checked:")
        for error in errors:
            print(f"- {error}")
        return 1
    expected = render_all()
    stale = []
    expected_paths = {ROOT / rel for rel in expected}
    for relative, contents in expected.items():
        path = ROOT / relative
        if not path.exists() or path.read_text(encoding="utf-8") != contents:
            stale.append(relative)
    for dirname in GENERATED_DIRS:
        directory = ROOT / dirname
        if directory.exists():
            for path in directory.glob("*.md"):
                if path not in expected_paths and path.read_text(encoding="utf-8").startswith(MARKER):
                    stale.append(str(path.relative_to(ROOT)))
    if stale:
        print("Generated Markdown is missing or stale. Run python scripts/build_pages.py:")
        for relative in sorted(stale):
            print(f"- {relative}")
        return 1
    print(f"Generated Markdown is current ({len(expected)} pages).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
