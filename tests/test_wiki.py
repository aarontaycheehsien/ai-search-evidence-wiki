from __future__ import annotations

from pathlib import Path

import yaml

from scripts.affected_pages import affected_claim, affected_source
from scripts.build_pages import ROOT, render_all
from scripts.validate import validate


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
    topic = {"id": "topic-one", "title": "Example topic", "type": "question", "question": "An example?", "claim_ids": ["claim-one"]}
    for folder, record in (("sources", source), ("claims", claim), ("topics", topic)):
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
        "docs/evidence/guo-2024.md",
        "docs/evidence/homiar-2025.md",
        "docs/evidence/khraisha-2024.md",
        "docs/evidence/li-2024.md",
        "docs/evidence/sanghera-2025.md",
        "docs/evidence/syriani-2023.md",
        "docs/evidence/tran-2024.md",
        "docs/questions/llm-screening.md",
    ]


def test_changed_source_maps_to_its_pages() -> None:
    assert affected_source("guo-2024") == [
        "docs/claims/screening-001.md",
        "docs/claims/screening-002.md",
        "docs/claims/screening-003.md",
        "docs/evidence/guo-2024.md",
        "docs/evidence/index.md",
        "docs/questions/llm-screening.md",
    ]
