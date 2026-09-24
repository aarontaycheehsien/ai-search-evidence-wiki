"""Validate evidence and generated pages, then build the static site."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    for script in ("validate.py", "check_generated.py"):
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / script)], cwd=ROOT)
        if result.returncode:
            return result.returncode
    return subprocess.run(["zensical", "build"], cwd=ROOT).returncode


if __name__ == "__main__":
    raise SystemExit(main())
