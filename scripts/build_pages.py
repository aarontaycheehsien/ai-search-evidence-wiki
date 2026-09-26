"""Deterministically render evidence YAML records as Markdown pages."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

from scripts.validate import ROOT, validate

MARKER = "> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**"
GENERATED_DIRS = ("docs/topics", "docs/concepts", "docs/claims", "docs/evidence")


def load_records(kind: str) -> list[dict[str, Any]]:
    return [yaml.safe_load(path.read_text(encoding="utf-8")) for path in sorted((ROOT / "data" / kind).glob("*.yaml"))]


def _line(value: Any) -> str:
    return str(value).strip() if value not in (None, "") else "Not recorded"


def _source_map(sources: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {item["id"]: item for item in sources}


def _claim_map(claims: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {item["id"]: item for item in claims}


def render_claim(claim: dict[str, Any], sources: dict[str, dict[str, Any]], topics: dict[str, dict[str, Any]]) -> str:
    lines = [MARKER, "", f"# {claim['claim'].strip()}", "", f"**Status:** {claim['status']}", "", "## Evidence", ""]
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
        lines.extend(f"- [{topics[t]['title']}](../topics/{t}.md)" for t in claim["topics"])
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
            lines.append(f"- [{claim['claim'].strip()}](../claims/{claim['id']}.md) — **{ev['relationship']}**")
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
    lines.extend(f"- [{claim['claim'].strip()}]({claim['id']}.md) — **{claim['status']}**" for claim in claims)
    lines.append("")
    return "\n".join(lines)


def render_topic_index(topics: list[dict[str, Any]]) -> str:
    lines = [MARKER, "", "# Topics", "", "Research questions organized around AI-assisted academic search and evidence synthesis.", ""]
    lines.extend(f"- [{topic['title']}]({topic['id']}.md)" for topic in topics if topic["type"] == "question")
    lines.append("")
    return "\n".join(lines)


def render_concept_index(topics: list[dict[str, Any]]) -> str:
    lines = [MARKER, "", "# Concepts", "", "Cross-cutting concepts used to describe and compare AI-assisted evidence-synthesis research.", ""]
    lines.extend(f"- [{topic['title']}]({topic['id']}.md)" for topic in topics if topic["type"] == "concept")
    lines.append("")
    return "\n".join(lines)


def render_topic(topic: dict[str, Any], claims: dict[str, dict[str, Any]], sources: dict[str, dict[str, Any]], experiments: list[dict[str, Any]], concepts: dict[str, dict[str, Any]]) -> str:
    topic_claims = [claims[cid] for cid in topic["claim_ids"]]
    linked_ids = {ev["source_id"] for claim in topic_claims for ev in claim["evidence"]}
    linked_sources = [source for source in sources.values() if source["id"] in linked_ids]
    lines = [
        MARKER, "", f"# {topic['title']}", "", "## Research question", "",
        topic.get("question", "No question recorded."), "", "## Scope and review boundaries", "",
        "Define the evidence-synthesis setting, eligible study types, and task boundaries here. Keep scope decisions explicit and source-backed where they depend on empirical evidence.", "", "## Overview", "",
        f"This topic groups {len(topic_claims)} claims linked to {len(linked_sources)} source records.", "",
        "## Current evidence", "",
        "The relationships and source categories below come from the structured evidence records. Results are reported in each source's own review setting; this page does not pool them.",
        "", "## Key claims", "",
    ]
    for claim in topic_claims:
        lines.extend([f"### [{claim['claim'].strip()}](../claims/{claim['id']}.md)", "", f"**Status:** {claim['status']}", ""])
        if not claim["evidence"]:
            lines.extend(["No source is linked.", ""])
        for ev in claim["evidence"]:
            src = sources[ev["source_id"]]
            lines.append(f"- **{ev['relationship']}** — [{src['title']}](../evidence/{src['id']}.md) ({src['source_category']}); locator: {_line(ev.get('locator'))}. {_line(ev.get('note'))}")
        lines.append("")
    lines.extend(["## Connected concepts", ""])
    connected = [concepts[concept_id] for concept_id in topic.get("concept_ids", [])]
    if connected:
        lines.extend(f"- [{concept['title']}](../concepts/{concept['id']}.md)" for concept in connected)
    else:
        lines.append("No concepts are linked yet.")
    lines.extend(["", "## Open questions and evidence gaps", "", "Record unresolved questions and evidence gaps here as they are identified during review.", ""])
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
        lines.extend(f"- [{claim['claim'].strip()}](../claims/{claim['id']}.md) is marked **{claim['status']}**." for claim in flagged)
    else:
        lines.append("No linked claim is currently flagged as provisional, uncertain, mixed, or contradicted.")
    lines.extend(["", "Read the individual source records for study design, scope, and unresolved reporting discrepancies.", "", f"**Last reviewed:** {topic.get('last_reviewed', 'Not recorded')}", ""])
    return "\n".join(lines)


def render_concept(concept: dict[str, Any], topics: dict[str, dict[str, Any]], claims: dict[str, dict[str, Any]]) -> str:
    lines = [
        MARKER, "", f"# {concept['title']}", "", "## Working definition", "",
        "To be defined and cited. This scaffold does not assert a definition.", "",
        "## Why it matters in evidence synthesis", "",
        "Describe the concept's relevance to AI-assisted academic search or evidence synthesis, supported by linked sources where appropriate.", "",
        "## How studies operationalize it", "",
        "Record the measures, decision rules, and reference standards used by each study; do not assume measures are interchangeable.", "",
        "## Related topics", "",
    ]
    related = concept.get("related_topics", [])
    if related:
        lines.extend(f"- [{topics[topic_id]['title']}](../topics/{topic_id}.md)" for topic_id in related)
    else:
        lines.append("No topics linked yet.")
    lines.extend(["", "## Linked claims", ""])
    if concept.get("claim_ids"):
        lines.extend(f"- [{claims[claim_id]['claim'].strip()}](../claims/{claim_id}.md)" for claim_id in concept["claim_ids"])
    else:
        lines.extend(["No claims are linked directly yet. Follow the related topic pages to see the current evidence.", ""])
    lines.extend(["## Open questions", "", "Record unresolved definitions, measurement choices, and evidence gaps here.", ""])
    return "\n".join(lines)


def render_all() -> dict[str, str]:
    sources = load_records("sources")
    claims = load_records("claims")
    topics = load_records("topics")
    experiments = load_records("experiments")
    source_by_id = _source_map(sources)
    claim_by_id = _claim_map(claims)
    topic_by_id = {item["id"]: item for item in topics}
    questions = [item for item in topics if item["type"] == "question"]
    concepts = [item for item in topics if item["type"] == "concept"]
    concept_by_id = {item["id"]: item for item in concepts}
    output: dict[str, str] = {}
    output["docs/topics/index.md"] = render_topic_index(topics)
    output["docs/concepts/index.md"] = render_concept_index(topics)
    output["docs/claims/index.md"] = render_claim_index(claims)
    output["docs/evidence/index.md"] = render_source_index(sources)
    for topic in questions:
        output[f"docs/topics/{topic['id']}.md"] = render_topic(topic, claim_by_id, source_by_id, experiments, concept_by_id)
    for concept in concepts:
        output[f"docs/concepts/{concept['id']}.md"] = render_concept(concept, topic_by_id, claim_by_id)
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
