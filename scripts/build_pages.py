"""Deterministically render evidence YAML records as Markdown pages."""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

from scripts.validate import ROOT, validate

MARKER = "> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**"
GENERATED_DIRS = ("docs/topics", "docs/tools", "docs/concepts", "docs/claims", "docs/evidence")
SOURCE_LABELS = {
    "peer-reviewed-study": ("peer-reviewed study", "peer-reviewed studies"),
    "preprint": ("preprint", "preprints"),
    "vendor-documentation": ("vendor documentation record", "vendor documentation records"),
    "system-documentation": ("system documentation record", "system documentation records"),
    "independent-experiment": ("independent experiment", "independent experiments"),
    "editorial-source": ("editorial source", "editorial sources"),
}
COUNT_NOTE = "Counts describe distinct linked source records. A source may appear under multiple entries; source counts and year ranges are not evidence-quality ratings. Years are the years recorded for the sources."


def evidence_summary(records: list[dict[str, Any]], include_count: bool = True) -> str:
    unique = {record["id"]: record for record in records}
    count = len(unique)
    years = sorted({record["year"] for record in unique.values() if record.get("year") is not None})
    year_text = str(years[0]) if len(years) == 1 else f"{years[0]}–{years[-1]}" if years else "no source years recorded"
    parts = [f"{count} {'source' if count == 1 else 'sources'}", year_text] if include_count else [year_text]
    undated = sum(record.get("year") is None for record in unique.values())
    if undated:
        parts.append(f"{undated} undated")
    categories = Counter(record["source_category"] for record in unique.values())
    labels = [f"{categories[category]} {names[0] if categories[category] == 1 else names[1]}" for category, names in SOURCE_LABELS.items() if categories[category]]
    if labels:
        parts.append(", ".join(labels))
    return "; ".join(parts)


def claim_sources(claim: dict[str, Any], sources: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    return [sources[source_id] for source_id in sorted({ev["source_id"] for ev in claim["evidence"]})]


def record_sources(record: dict[str, Any], claims: dict[str, dict[str, Any]], sources: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    ids = set(record["evidence_source_ids"]) if record["type"] == "tool" else {ev["source_id"] for cid in record["claim_ids"] for ev in claims[cid]["evidence"]}
    return [sources[source_id] for source_id in sorted(ids)]


def load_records(kind: str) -> list[dict[str, Any]]:
    return [yaml.safe_load(path.read_text(encoding="utf-8")) for path in sorted((ROOT / "data" / kind).glob("*.yaml"))]


def _line(value: Any) -> str:
    return str(value).strip() if value not in (None, "") else "Not recorded"


def _source_map(sources: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {item["id"]: item for item in sources}


def _claim_map(claims: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {item["id"]: item for item in claims}


def _record_link(record: dict[str, Any]) -> str:
    folder = "tools" if record["type"] == "tool" else "topics"
    return f"../{folder}/{record['id']}.md"


def render_claim(claim: dict[str, Any], sources: dict[str, dict[str, Any]], topics: dict[str, dict[str, Any]]) -> str:
    lines = [MARKER, "", f"# {claim['claim'].strip()}", "", f"**Status:** {claim['status']} — {evidence_summary(claim_sources(claim, sources))}", "", "## Evidence", ""]
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
    linked_topics = [topics[t] for t in claim["topics"] if topics[t]["type"] != "tool"]
    linked_tools = [topics[t] for t in claim["topics"] if topics[t]["type"] == "tool"]
    if linked_topics:
        lines.extend(["## Topics", ""])
        lines.extend(f"- [{record['title']}]({_record_link(record)})" for record in linked_topics)
    if linked_tools:
        if linked_topics:
            lines.append("")
        lines.extend(["## Tools", ""])
        lines.extend(f"- [{record['title']}]({_record_link(record)})" for record in linked_tools)
    lines.extend(["", f"**Last reviewed:** {claim['last_reviewed']}", ""])
    return "\n".join(lines)


def render_source(source: dict[str, Any], claims: list[dict[str, Any]]) -> str:
    category = SOURCE_LABELS[source['source_category']][0]
    lines = [MARKER, "", f"# {source['title']}", "", f"**Source:** {source.get('year') or 'year not recorded'}; {category}", "", "## Bibliographic information", "",
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
    lines.extend([evidence_summary(sources), "", COUNT_NOTE, ""])
    for category, heading in (("peer-reviewed-study", "Peer-reviewed studies"), ("preprint", "Preprints"), ("vendor-documentation", "Vendor documentation"), ("system-documentation", "System documentation"), ("independent-experiment", "Independent experiments"), ("editorial-source", "Editorial sources")):
        matching = [source for source in sources if source["source_category"] == category]
        if matching:
            lines.extend([f"## {heading} ({len(matching)})", "", evidence_summary(matching, include_count=False), ""])
            lines.extend(f"- [{source['title']}]({source['id']}.md) ({_line(source.get('year'))})" for source in matching)
            lines.append("")
    return "\n".join(lines)


def render_claim_index(claims: list[dict[str, Any]], sources: dict[str, dict[str, Any]]) -> str:
    lines = [MARKER, "", "# Claims", "", "Claims and their evidence relationships are generated from `data/claims/`.", ""]
    lines.extend([COUNT_NOTE, ""])
    lines.extend(f"- [{claim['claim'].strip()}]({claim['id']}.md) — **{claim['status']}**; {evidence_summary(claim_sources(claim, sources))}" for claim in claims)
    lines.append("")
    return "\n".join(lines)


def render_topic_index(topics: list[dict[str, Any]], claims: dict[str, dict[str, Any]], sources: dict[str, dict[str, Any]]) -> str:
    lines = [MARKER, "", "# Topics", "", "Research questions organized around AI-assisted academic search and evidence synthesis.", ""]
    lines.extend([COUNT_NOTE, ""])
    for topic in topics:
        if topic["type"] == "question":
            linked = record_sources(topic, claims, sources)
            lines.append(f"- [{topic['title']}]({topic['id']}.md) ({len(linked)}) — {evidence_summary(linked, include_count=False)}")
    lines.append("")
    return "\n".join(lines)


def render_tool_index(tools: list[dict[str, Any]], claims: dict[str, dict[str, Any]], sources: dict[str, dict[str, Any]]) -> str:
    lines = [
        MARKER, "", "# Tools", "",
        "Empirical evaluations organized by the research assistant or discovery tool evaluated.", "",
    ]
    lines.extend([COUNT_NOTE, ""])
    for tool in tools:
        linked = record_sources(tool, claims, sources)
        lines.append(f"- [{tool['title']}]({tool['id']}.md) ({len(linked)}) — {evidence_summary(linked, include_count=False)}")
    lines.append("")
    return "\n".join(lines)


def render_concept_index(topics: list[dict[str, Any]]) -> str:
    lines = [MARKER, "", "# Concepts", "", "Cross-cutting concepts used to describe and compare AI-assisted evidence-synthesis research.", ""]
    lines.extend(f"- [{topic['title']}]({topic['id']}.md) — scaffold{' with no directly linked evidence' if not topic['claim_ids'] else ''}" for topic in topics if topic["type"] == "concept")
    lines.append("")
    return "\n".join(lines)


def render_topic(topic: dict[str, Any], claims: dict[str, dict[str, Any]], sources: dict[str, dict[str, Any]], experiments: list[dict[str, Any]], concepts: dict[str, dict[str, Any]]) -> str:
    topic_claims = [claims[cid] for cid in topic["claim_ids"]]
    linked_ids = {ev["source_id"] for claim in topic_claims for ev in claim["evidence"]}
    linked_sources = [source for source in sources.values() if source["id"] in linked_ids]
    lines = [
        MARKER, "", f"# {topic['title']}", "", f"**Evidence:** {evidence_summary(linked_sources)}", "", "## Research question", "",
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


def render_tool(tool: dict[str, Any], claims: dict[str, dict[str, Any]], sources: dict[str, dict[str, Any]], concepts: dict[str, dict[str, Any]]) -> str:
    tool_claims = [claims[cid] for cid in tool["claim_ids"]]
    included_source_ids = set(tool["evidence_source_ids"])
    linked_sources = [source for source in sources.values() if source["id"] in included_source_ids]
    lines = [
        MARKER, "", f"# {tool['title']}", "", f"**Evidence:** {evidence_summary(linked_sources)}", "", "## Scope", "",
        tool["description"], "", "## Overview", "",
        f"This tool page groups {len(tool_claims)} claims and {len(linked_sources)} source records that evaluate or directly contextualize {tool['title']}.", "",
        "Cross-tool claims are repeated where relevant, but the evidence shown below is limited to the source records assigned to this tool.", "",
        "## Key claims", "",
    ]
    for claim in tool_claims:
        relevant_evidence = [ev for ev in claim["evidence"] if ev["source_id"] in included_source_ids]
        if not relevant_evidence:
            continue
        lines.extend([f"### [{claim['claim'].strip()}](../claims/{claim['id']}.md)", "", f"**Status:** {claim['status']}", ""])
        for ev in relevant_evidence:
            src = sources[ev["source_id"]]
            lines.append(f"- **{ev['relationship']}** — [{src['title']}](../evidence/{src['id']}.md) ({src['source_category']}); locator: {_line(ev.get('locator'))}. {_line(ev.get('note'))}")
        lines.append("")
    lines.extend(["## Connected concepts", ""])
    connected = [concepts[concept_id] for concept_id in tool.get("concept_ids", [])]
    if connected:
        lines.extend(f"- [{concept['title']}](../concepts/{concept['id']}.md)" for concept in connected)
    else:
        lines.append("No concepts are linked yet.")
    lines.extend(["", "## Source records", ""])
    peer_reviewed = [s for s in linked_sources if s["source_category"] == "peer-reviewed-study"]
    preprints = [s for s in linked_sources if s["source_category"] == "preprint"]
    other = [s for s in linked_sources if s["source_category"] not in {"peer-reviewed-study", "preprint"}]
    lines.extend(["### Peer-reviewed studies", ""])
    lines.extend(f"- [{s['title']}](../evidence/{s['id']}.md)" for s in peer_reviewed) if peer_reviewed else lines.append("No peer-reviewed study records are linked.")
    lines.extend(["", "### Preprints and unverified manuscripts", ""])
    lines.extend(f"- [{s['title']}](../evidence/{s['id']}.md) — {s['publication_status']}" for s in preprints) if preprints else lines.append("No preprints or unverified manuscripts are linked.")
    lines.extend(["", "### Other evidence categories", ""])
    lines.extend(f"- [{s['title']}](../evidence/{s['id']}.md) — {s['source_category']}" for s in other) if other else lines.append("No vendor, system, experimental, or editorial records are linked.")
    lines.extend(["", "## Important uncertainties", ""])
    flagged = [claim for claim in tool_claims if claim["status"] in {"provisional", "uncertain", "mixed", "contradicted"}]
    lines.extend(f"- [{claim['claim'].strip()}](../claims/{claim['id']}.md) is marked **{claim['status']}**." for claim in flagged) if flagged else lines.append("No linked claim is currently flagged as provisional, uncertain, mixed, or contradicted.")
    lines.extend(["", "Read the individual source records for study design, scope, and unresolved reporting discrepancies.", "", f"**Last reviewed:** {tool.get('last_reviewed', 'Not recorded')}", ""])
    return "\n".join(lines)


def render_concept(concept: dict[str, Any], topics: dict[str, dict[str, Any]], tools: list[dict[str, Any]], claims: dict[str, dict[str, Any]]) -> str:
    lines = [
        MARKER, "", f"# {concept['title']}", "", "Scaffold with no directly linked evidence." if not concept['claim_ids'] else "Concept scaffold with directly linked claims.", "", "## Working definition", "",
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
    related_tools = [tool for tool in tools if concept["id"] in tool.get("concept_ids", [])]
    lines.extend(["", "## Related tools", ""])
    if related_tools:
        lines.extend(f"- [{tool['title']}](../tools/{tool['id']}.md)" for tool in related_tools)
    else:
        lines.append("No tools linked yet.")
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
    tools = [item for item in topics if item["type"] == "tool"]
    concepts = [item for item in topics if item["type"] == "concept"]
    concept_by_id = {item["id"]: item for item in concepts}
    output: dict[str, str] = {}
    output["docs/topics/index.md"] = render_topic_index(topics, claim_by_id, source_by_id)
    output["docs/tools/index.md"] = render_tool_index(tools, claim_by_id, source_by_id)
    output["docs/concepts/index.md"] = render_concept_index(topics)
    output["docs/claims/index.md"] = render_claim_index(claims, source_by_id)
    output["docs/evidence/index.md"] = render_source_index(sources)
    for topic in questions:
        output[f"docs/topics/{topic['id']}.md"] = render_topic(topic, claim_by_id, source_by_id, experiments, concept_by_id)
    for tool in tools:
        output[f"docs/tools/{tool['id']}.md"] = render_tool(tool, claim_by_id, source_by_id, concept_by_id)
    for concept in concepts:
        output[f"docs/concepts/{concept['id']}.md"] = render_concept(concept, topic_by_id, tools, claim_by_id)
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
