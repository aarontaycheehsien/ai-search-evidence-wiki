"""Report generated pages that depend on a changed claim or source."""

from __future__ import annotations

import argparse
import sys

from scripts.build_pages import load_records


def affected_claim(claim_id: str) -> list[str]:
    claims = {c["id"]: c for c in load_records("claims")}
    topics = load_records("topics")
    if claim_id not in claims:
        return []
    paths = {f"docs/claims/{claim_id}.md", "docs/claims/index.md"}
    for topic in topics:
        if claim_id in topic.get("claim_ids", []) and topic.get("type") == "question":
            paths.add(f"docs/questions/{topic['id']}.md")
    for evidence in claims[claim_id].get("evidence", []):
        paths.add(f"docs/evidence/{evidence['source_id']}.md")
    return sorted(paths)


def affected_source(source_id: str) -> list[str]:
    sources = {s["id"] for s in load_records("sources")}
    if source_id not in sources:
        return []
    claims = load_records("claims")
    paths = {f"docs/evidence/{source_id}.md", "docs/evidence/index.md"}
    for claim in claims:
        if any(e.get("source_id") == source_id for e in claim.get("evidence", [])):
            paths.add(f"docs/claims/{claim['id']}.md")
            for topic in load_records("topics"):
                if topic.get("type") == "question" and claim["id"] in topic.get("claim_ids", []):
                    paths.add(f"docs/questions/{topic['id']}.md")
    return sorted(paths)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--claim")
    group.add_argument("--source")
    args = parser.parse_args()
    paths = affected_claim(args.claim) if args.claim else affected_source(args.source)
    if not paths:
        print(f"No generated pages found for {args.claim or args.source!r}.")
        return 1
    print(f"Affected pages for {'claim' if args.claim else 'source'}: {args.claim or args.source}\n")
    for path in paths:
        print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
