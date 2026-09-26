from __future__ import annotations

import json
from pathlib import Path

import yaml

from scripts.affected_pages import affected_claim, affected_source
from scripts.build_pages import ROOT, evidence_summary, record_sources, render_all
from scripts.validate import validate


def test_undermind_promoted_records_have_download_provenance() -> None:
    manifest = json.loads((ROOT / "incoming/undermind-download-manifest-2026-09-27.json").read_text(encoding="utf-8"))
    papers = manifest["papers"]
    assert len(papers) == manifest["download_count"] == 67
    assert len({paper["cite_key"] for paper in papers}) == 67
    promoted = [paper for paper in papers if paper["processing_status"] == "promoted-full-text"]
    assert len(promoted) == 23
    for paper in papers:
        assert paper["pdf_structure_verified"] is True
        assert len(paper["sha256"]) == 64
        assert set(paper["sha256"]) <= set("0123456789abcdef")
        assert "url" not in paper
    for paper in promoted:
        source = yaml.safe_load((ROOT / "data/sources" / (paper["source_id"] + ".yaml")).read_text(encoding="utf-8"))
        assert source["local_file"] == paper["file"]
    excluded = next(paper for paper in papers if paper["cite_key"] == "Dev24")
    assert excluded["source_id"] is None
    assert excluded["processing_status"] == "excluded-feature-review-no-performance-test"


def make_valid_tree(tmp_path: Path) -> Path:
    for folder in ("sources", "claims", "topics", "experiments"):
        (tmp_path / "data" / folder).mkdir(parents=True, exist_ok=True)
    source = {
        "id": "study-one", "type": "journal-article", "title": "Example source",
        "authors": ["Example Person"], "year": 2025, "doi": None, "url": None,
        "publication_status": "published", "source_category": "peer-reviewed-study", "notes": None,
    }
    claim = {
        "id": "claim-one", "claim": "A demonstration claim.", "status": "provisional",
        "topics": ["topic-one"],
        "evidence": [{"source_id": "study-one", "relationship": "supports", "locator": None, "note": None}],
        "last_reviewed": "2026-01-01",
    }
    topic = {"id": "topic-one", "title": "Example topic", "type": "question", "question": "An example?", "claim_ids": ["claim-one"], "concept_ids": ["concept-one"]}
    concept = {"id": "concept-one", "title": "Example concept", "type": "concept", "claim_ids": [], "related_topics": ["topic-one"]}
    for folder, record in (("sources", source), ("claims", claim), ("topics", topic), ("topics", concept)):
        (tmp_path / "data" / folder / f"{record['id']}.yaml").write_text(yaml.safe_dump(record, sort_keys=False), encoding="utf-8")
    return tmp_path


def edit_record(root: Path, folder: str, filename: str, mutate) -> None:
    path = root / "data" / folder / filename
    record = yaml.safe_load(path.read_text(encoding="utf-8"))
    mutate(record)
    path.write_text(yaml.safe_dump(record, sort_keys=False), encoding="utf-8")


def test_valid_yaml_is_accepted(tmp_path: Path) -> None:
    root = make_valid_tree(tmp_path)
    assert validate(root) == []


def test_invalid_topic_concept_link_is_rejected(tmp_path: Path) -> None:
    root = make_valid_tree(tmp_path)
    edit_record(root, "topics", "topic-one.yaml", lambda item: item.update(concept_ids=["missing-concept"]))
    assert any("references missing concept 'missing-concept'" in error for error in validate(root))


def test_invalid_concept_topic_link_is_rejected(tmp_path: Path) -> None:
    root = make_valid_tree(tmp_path)
    edit_record(root, "topics", "concept-one.yaml", lambda item: item.update(related_topics=["missing-topic"]))
    assert any("references missing research topic 'missing-topic'" in error for error in validate(root))


def test_unknown_bibliographic_year_is_explicit(tmp_path: Path) -> None:
    root = make_valid_tree(tmp_path)
    edit_record(root, "sources", "study-one.yaml", lambda item: item.update(year=None))
    assert validate(root) == []


def test_bad_ids_are_rejected(tmp_path: Path) -> None:
    root = make_valid_tree(tmp_path)
    edit_record(root, "claims", "claim-one.yaml", lambda item: item.update(id="Bad ID"))
    assert any("invalid or missing id" in error for error in validate(root))


def test_missing_sources_are_rejected(tmp_path: Path) -> None:
    root = make_valid_tree(tmp_path)
    edit_record(root, "claims", "claim-one.yaml", lambda item: item["evidence"][0].update(source_id="absent-source"))
    assert any("references missing source" in error for error in validate(root))


def test_missing_claims_are_rejected(tmp_path: Path) -> None:
    root = make_valid_tree(tmp_path)
    (root / "data/topics/topic-one.yaml").write_text(
        "id: topic-one\ntitle: Example topic\ntype: question\nquestion: An example?\nclaim_ids: [absent-claim]\n", encoding="utf-8"
    )
    assert any("references missing claim" in error for error in validate(root))


def test_invalid_relationship_is_rejected(tmp_path: Path) -> None:
    root = make_valid_tree(tmp_path)
    edit_record(root, "claims", "claim-one.yaml", lambda item: item["evidence"][0].update(relationship="maybe"))
    assert any("invalid relationship" in error for error in validate(root))


def test_malformed_yaml_is_rejected(tmp_path: Path) -> None:
    root = make_valid_tree(tmp_path)
    (root / "data/sources/broken.yaml").write_text("id: [unterminated", encoding="utf-8")
    assert any("malformed YAML" in error for error in validate(root))


def test_duplicate_ids_are_rejected(tmp_path: Path) -> None:
    root = make_valid_tree(tmp_path)
    record = yaml.safe_load((root / "data/sources/study-one.yaml").read_text(encoding="utf-8"))
    (root / "data/sources/study-two.yaml").write_text(yaml.safe_dump(record), encoding="utf-8")
    errors = validate(root)
    assert any("duplicate id 'study-one'" in error for error in errors)


def test_page_generation_is_reproducible() -> None:
    assert render_all() == render_all()


def test_v2_topic_and_concept_scaffolds_are_generated() -> None:
    pages = render_all()
    assert "docs/topics/index.md" in pages
    assert "docs/topics/llm-data-extraction.md" in pages
    assert "docs/concepts/index.md" in pages
    concept = pages["docs/concepts/automation-bias.md"]
    assert "## Working definition" in concept
    assert "This scaffold does not assert a definition." in concept
    assert "../topics/ai-evidence-appraisal.md" in concept
    assert "../concepts/recall-and-sensitivity.md" in pages["docs/topics/llm-screening.md"]
    assert "../topics/llm-screening.md" in pages["docs/claims/screening-001.md"]


def test_tools_are_a_separate_generated_section() -> None:
    pages = render_all()
    assert "docs/tools/index.md" in pages
    assert "docs/tools/elicit.md" in pages
    assert "docs/tools/undermind.md" in pages
    assert "docs/tools/consensus.md" in pages
    assert "docs/topics/research-assistant-tools.md" not in pages
    assert "[Elicit.com](elicit.md)" in pages["docs/tools/index.md"]
    assert "../evidence/lau-golder-2025.md" in pages["docs/tools/elicit.md"]
    assert "../evidence/hartke-undermind.md" not in pages["docs/tools/elicit.md"]
    assert "../tools/elicit.md" in pages["docs/claims/assistant-001.md"]
    assert "## Related tools" in pages["docs/concepts/precision.md"]


def test_generated_markdown_matches_expected_output() -> None:
    for relative, expected in render_all().items():
        path = ROOT / relative
        assert path.read_text(encoding="utf-8") == expected
        assert expected.startswith("> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**")


def test_changed_claim_maps_to_its_pages() -> None:
    assert affected_claim("screening-001") == [
        "docs/claims/index.md",
        "docs/claims/screening-001.md",
        "docs/evidence/cao-2025.md",
        "docs/evidence/colangelo-2025-screening.md",
        "docs/evidence/guo-2024.md",
        "docs/evidence/homiar-2025.md",
        "docs/evidence/khraisha-2024.md",
        "docs/evidence/li-2024.md",
        "docs/evidence/sanghera-2025.md",
        "docs/evidence/syriani-2023.md",
        "docs/evidence/tran-2024.md",
        "docs/topics/index.md",
        "docs/topics/llm-screening.md",
    ]


def test_changed_source_maps_to_its_pages() -> None:
    assert affected_source("guo-2024") == [
        "docs/claims/index.md",
        "docs/claims/screening-001.md",
        "docs/claims/screening-002.md",
        "docs/claims/screening-003.md",
        "docs/evidence/guo-2024.md",
        "docs/evidence/index.md",
        "docs/topics/index.md",
        "docs/topics/llm-screening.md",
    ]


def test_changed_tool_claim_maps_to_tool_pages() -> None:
    pages = affected_claim("assistant-004")
    assert "docs/tools/elicit.md" in pages
    assert "docs/tools/undermind.md" in pages


def test_changed_tool_source_maps_only_to_relevant_tool_pages() -> None:
    pages = affected_source("hartke-undermind")
    assert "docs/tools/undermind.md" in pages
    assert "docs/tools/elicit.md" not in pages


def test_evidence_summary_deduplicates_and_handles_years() -> None:
    source = {"id": "one", "year": 2025, "source_category": "peer-reviewed-study"}
    undated = {"id": "two", "year": None, "source_category": "vendor-documentation"}
    assert evidence_summary([source, source]) == "1 source; 2025; 1 peer-reviewed study"
    assert evidence_summary([source, undated]) == "2 sources; 2025; 1 undated; 1 peer-reviewed study, 1 vendor documentation record"
    assert evidence_summary([undated]) == "1 source; no source years recorded; 1 undated; 1 vendor documentation record"
    assert evidence_summary([]) == "0 sources; no source years recorded"
    newer = {"id": "three", "year": 2026, "source_category": "preprint"}
    assert evidence_summary([source, newer]) == "2 sources; 2025–2026; 1 peer-reviewed study, 1 preprint"


def test_record_sources_respects_tool_filter_and_topic_deduplication() -> None:
    sources = {name: {"id": name, "year": 2025, "source_category": "preprint"} for name in ("one", "two")}
    claims = {"claim": {"evidence": [{"source_id": "one"}, {"source_id": "one"}, {"source_id": "two"}]}}
    tool = {"type": "tool", "evidence_source_ids": ["one", "one"], "claim_ids": ["claim"]}
    topic = {"type": "question", "claim_ids": ["claim"]}
    assert [s["id"] for s in record_sources(tool, claims, sources)] == ["one"]
    assert [s["id"] for s in record_sources(topic, claims, sources)] == ["one", "two"]


def test_evidence_context_uses_authoritative_counts_and_categories() -> None:
    pages = render_all()
    tools = pages["docs/tools/index.md"]
    assert "[Elicit.com](elicit.md) (16) — 2024–2026; 15 peer-reviewed studies, 1 preprint" in tools
    assert "[Undermind.ai](undermind.md) (3) — 2024–2026; 1 peer-reviewed study, 1 preprint, 1 vendor documentation record" in tools
    assert "[Consensus](consensus.md) (6) — 2025–2026; 3 peer-reviewed studies, 3 preprints" in tools
    assert "(15) — 2023–2026; 12 peer-reviewed studies, 3 preprints" in pages["docs/topics/index.md"]
    assert "**Evidence:** 16 sources; 2024–2026; 15 peer-reviewed studies, 1 preprint" in pages["docs/tools/elicit.md"]
    assert "Scaffold with no directly linked evidence." in pages["docs/concepts/precision.md"]
    assert "docs/topics/index.md" in affected_source("guo-2024")
    assert "docs/tools/index.md" in affected_source("hartke-undermind")


def test_evidence_indexes_rank_source_volume_with_peer_reviewed_tiebreak() -> None:
    pages = render_all()
    tools = pages["docs/tools/index.md"]
    topics = pages["docs/topics/index.md"]
    assert tools.index("[Elicit.com]") < tools.index("[General-purpose AI assistants]")
    assert tools.index("[SciSpace]") < tools.index("[Undermind.ai]")
    assert topics.index("[LLMs for structured data extraction]") < topics.index("[LLMs for Citation Screening]")
    claims = pages["docs/claims/index.md"]
    assert "13 sources;" in claims
    assert "9 sources;" in claims
    assert claims.index("13 sources;") < claims.index("9 sources;")


def test_evidence_lists_put_peer_reviewed_sources_before_other_categories() -> None:
    pages = render_all()
    claim = pages["docs/claims/assistant-004.md"]
    study = claim.index("### Which AI Tools Work Best for Research?")
    preprint = claim.index("### Evaluating Eight Retrieval-Augmented Generation")
    vendor = claim.index("### Benchmarking the Undermind Search Assistant")
    assert study < preprint < vendor
    source_index = pages["docs/evidence/index.md"]
    assert source_index.index("## Peer-reviewed studies") < source_index.index("## Preprints")
    assert source_index.index("OpenExtract: Automated Data Extraction") < source_index.index("Harnessing the Power of ChatGPT")
