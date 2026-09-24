"""Report claims whose review date is older than the configured interval."""

from __future__ import annotations

import argparse
from datetime import date, timedelta

import yaml

from scripts.validate import ROOT


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=365)
    args = parser.parse_args()
    if args.days < 0:
        parser.error("--days must be non-negative")
    threshold = date.today() - timedelta(days=args.days)
    stale = []
    for path in sorted((ROOT / "data/claims").glob("*.yaml")):
        claim = yaml.safe_load(path.read_text(encoding="utf-8"))
        try:
            reviewed = date.fromisoformat(str(claim["last_reviewed"]))
        except (KeyError, TypeError, ValueError):
            continue  # validate.py reports malformed or missing review dates.
        if reviewed < threshold:
            stale.append((claim["id"], reviewed.isoformat()))
    if stale:
        print(f"Claims last reviewed before {threshold.isoformat()} (review flag only):")
        for claim_id, reviewed in stale:
            print(f"- {claim_id}: {reviewed}")
    else:
        print(f"No claims are older than {args.days} days.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
