"""Deterministically render evidence YAML records as Markdown pages."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

from scripts.validate import ROOT, validate

MARKER = "> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**"
GENERATED_DIRS = ("docs/questions", "docs/claims", "docs/evidence")


def load_records(kind: str) -> list[dict[str, Any]]:
    return [yaml.safe_load(path.read_text(encoding="utf-8")) for path in sorted((ROOT / "data" / kind).glob("*.yaml"))]


def _line(value: Any) -> str:
    return str(value).strip() if value not in (None, "") else "Not recorded"


def _source_map(sources: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {item["id"]: item for item in sources}


def _claim_map(claims: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {item["id"]: item for item in claims}


def render_claim(claim: dict[str, Any], sources: dict[str, dict[str, Any]], topics: dict[str, dict[str, Any]]) -> str:
    lines = [MARKER, "", f"# {claim['id']}", "", "## Claim", "", claim["claim"].strip(), "", f"**Status:** {claim['status']}", "", "## Evidence", ""]
    if not claim["evidence"]:
        lines.append("No evidence records are linked to this claim.")
    for ev in claim["evidence"]:
        src = sources[ev["source_id"]]
        lines.extend([
            f"### {src['title']}", "",
            f"- **Source:** [{src['id']}](../evidence/{src['id']}.md)",
            f"- **Category:** {src['source_category']}",
            f"- **Relationship:** {ev['relationship']}",
            f"- **Locator:** {_line(ev.get('locator'))}",
            f"- **Note:** {_line(ev.get('note'))}", "",
        ])
    lines.extend(["## Topics", ""])
    if claim["topics"]:
        lines.extend(f"- [{topics[t]['title']}](../questions/{t}.md)" for t in claim["topics"])
    else:
        lines.append("No topic linked.")
    lines.extend(["", f"**Last reviewed:** {claim['last_reviewed']}", ""])
    return "\n".join(lines)


def render_source(source: dict[str, Any], claims: list[dict[str, Any]]) -> str:
    lines = [MARKER, "", f"# {source['title']}", "", "## Bibliographic information", "",
             f"- **Authors:** {', '.join(source['authors'])}", f"- **Year:** {_line(source.get('year'))}", f"- **DOI:** {_line(source.get('doi'))}", f"- **URL:** {_line(source.get('url'))}",
             f"- **Publication status:** {source['publication_status']}", f"- **Source category:** {source['source_category']}", f"- **Record type:** {source['type']}", f"- **Notes:** {_line(source.get('notes'))}", "", "## Linked claims", ""]
    found = False
    for claim in claims:
        matches = [ev for ev in claim["evidence"] if ev["source_id"] == source["id"]]
        for ev in matches:
            found = True
            lines.append(f"- [{claim['id']}](../claims/{claim['id']}.md) — **{ev['relationship']}**: {claim['claim'].strip()}")
    if not found:
        lines.append("No claims linked.")
    lines.append("")
    return "\n".join(lines)


def render_source_index(sources: list[dict[str, Any]]) -> str:
    lines = [MARKER, "", "# Sources", "", "Each source retains its publication category. Open a record for bibliographic details, scope notes, and linked claims.", ""]
    for category, heading in (("peer-reviewed-study", "Peer-reviewed studies"), ("preprint", "Preprints"), ("vendor-documentation", "Vendor documentation"), ("system-documentation", "System documentation"), ("independent-experiment", "Independent experiments"), ("editorial-source", "Editorial sources")):
        matching = [source for source in sources if source["source_category"] == category]
        if matching:
            lines.extend([f"## {heading}", ""])
            lines.extend(f"- [{source['title']}]({source['id']}.md) ({_line(source.get('year'))})" for source in matching)
            lines.append("")
    return "\n".join(lines)


def render_claim_index(claims: list[dict[str, Any]]) -> str:
    lines = [MARKER, "", "# Claims", "", "Claims and their evidence relationships are generated from `data/claims/`.", ""]
    lines.extend(f"- [{claim['id']}]({claim['id']}.md) — **{claim['status']}**: {claim['claim'].strip()}" for claim in claims)
    lines.append("")
    return "\n".join(lines)


def render_question_index(topics: list[dict[str, Any]]) -> str:
    lines = [MARKER, "", "# Questions", ""]
    lines.extend(f"- [{topic['title']}]({topic['id']}.md)" for topic in topics if topic["type"] == "question")
    lines.append("")
    return "\n".join(lines)


def render_topic(topic: dict[str, Any], claims: dict[str, dict[str, Any]], sources: dict[str, dict[str, Any]], experiments: list[dict[str, Any]]) -> str:
    topic_claims = [claims[cid] for cid in topic["claim_ids"]]
    linked_ids = {ev["source_id"] for claim in topic_claims for ev in claim["evidence"]}
    linked_sources = [source for source in sources.values() if source["id"] in linked_ids]
    lines = [
        MARKER, "", f"# {topic['title']}", "", "## Question", "",
        topic.get("question", "No question recorded."), "", "## Overview", "",
        f"This question groups {len(topic_claims)} claims linked to {len(linked_sources)} source records.", "",
        "## Current evidence", "",
        "The relationships and source categories below come from the structured evidence records. Results are reported in each source's own review setting; this page does not pool them.",
        "", "## Key claims", "",
    ]
    for claim in topic_claims:
        lines.extend([f"### [{claim['id']}](../claims/{claim['id']}.md)", "", claim["claim"].strip(), "", f"**Status:** {claim['status']}", ""])
        if not claim["evidence"]:
            lines.extend(["No source is linked.", ""])
        for ev in claim["evidence"]:
            src = sources[ev["source_id"]]
            lines.append(f"- **{ev['relationship']}** — [{src['title']}](../evidence/{src['id']}.md) ({src['source_category']}); locator: {_line(ev.get('locator'))}. {_line(ev.get('note'))}")
        lines.append("")
    lines.extend(["## Peer-reviewed studies", ""])
    studies = [s for s in linked_sources if s["source_category"] == "peer-reviewed-study"]
    lines.extend(f"- [{s['title']}](../evidence/{s['id']}.md)" for s in studies) if studies else lines.append("No peer-reviewed study records are linked.")
    lines.extend(["", "## Preprints and unverified manuscripts", ""])
    preprints = [s for s in linked_sources if s["source_category"] == "preprint"]
    lines.extend(f"- [{s['title']}](../evidence/{s['id']}.md) — {s['publication_status']}" for s in preprints) if preprints else lines.append("No preprints or unverified manuscripts are linked.")
    lines.extend(["", "## Independent experiments", ""])
    related = [e for e in experiments if any(cid in topic["claim_ids"] for cid in e.get("related_claims", []))]
    if related:
        for exp in related:
            lines.extend([f"### {exp['title']}", "", f"- **Date:** {exp['date']}", f"- **Dataset:** {exp['dataset']}", f"- **System:** {exp['system']}", f"- **Notes:** {exp.get('notes') or 'Not recorded'}", "- **Classification:** Independent experiment; not published evidence.", ""])
    else:
        lines.extend(["No independent experiments are linked.", ""])
    lines.extend(["## Important uncertainties", ""])
    flagged = [claim for claim in topic_claims if claim["status"] in {"provisional", "uncertain", "mixed", "contradicted"}]
    if flagged:
        lines.extend(f"- [{claim['id']}](../claims/{claim['id']}.md) is marked **{claim['status']}**: {claim['claim'].strip()}" for claim in flagged)
    else:
        lines.append("No linked claim is currently flagged as provisional, uncertain, mixed, or contradicted.")
    lines.extend(["", "Read the individual source records for study design, scope, and unresolved reporting discrepancies.", "", f"**Last reviewed:** {topic.get('last_reviewed', 'Not recorded')}", ""])
    return "\n".join(lines)


def render_all() -> dict[str, str]:
    sources = load_records("sources")
    claims = load_records("claims")
    topics = load_records("topics")
    experiments = load_records("experiments")
    source_by_id = _source_map(sources)
    claim_by_id = _claim_map(claims)
    topic_by_id = {item["id"]: item for item in topics}
    output: dict[str, str] = {}
    output["docs/questions/index.md"] = render_question_index(topics)
    output["docs/claims/index.md"] = render_claim_index(claims)
    output["docs/evidence/index.md"] = render_source_index(sources)
    for topic in topics:
        if topic["type"] == "question":
            output[f"docs/questions/{topic['id']}.md"] = render_topic(topic, claim_by_id, source_by_id, experiments)
    for claim in claims:
        output[f"docs/claims/{claim['id']}.md"] = render_claim(claim, source_by_id, topic_by_id)
    for source in sources:
        output[f"docs/evidence/{source['id']}.md"] = render_source(source, claims)
    return output


def build() -> int:
    errors = validate()
    if errors:
        print("Validation failed; pages were not generated:")
        for error in errors:
            print(f"- {error}")
        return 1
    expected = render_all()
    for relative, content in expected.items():
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
    expected_paths = {ROOT / rel for rel in expected}
    for dirname in GENERATED_DIRS:
        directory = ROOT / dirname
        if directory.exists():
            for path in directory.glob("*.md"):
                if path not in expected_paths and path.read_text(encoding="utf-8").startswith(MARKER):
                    path.unlink()
    print(f"Generated {len(expected)} Markdown pages.")
    return 0


if __name__ == "__main__":
    sys.exit(build())
