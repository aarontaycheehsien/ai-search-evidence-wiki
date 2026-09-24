"""Validate the repository's YAML evidence records."""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SOURCE_CATEGORIES = {
    "peer-reviewed-study", "preprint", "vendor-documentation",
    "system-documentation", "independent-experiment", "editorial-source",
}
RELATIONSHIPS = {"supports", "contradicts", "qualifies", "contextual", "unclear"}
STATUSES = {"supported", "mixed", "uncertain", "contradicted", "provisional"}
TOPIC_TYPES = {"question", "tool", "concept", "method"}


def _files(kind: str) -> list[Path]:
    return sorted((ROOT / "data" / kind).glob("*.yaml"))


def _load_records(kind: str, errors: list[str]) -> list[dict[str, Any]]:
    records = []
    for path in _files(kind):
        try:
            value = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (yaml.YAMLError, OSError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: malformed YAML: {exc}")
            continue
        if not isinstance(value, dict):
            errors.append(f"{path.relative_to(ROOT)}: record must be a YAML mapping")
            continue
        if "id" in value and path.stem != str(value["id"]):
            errors.append(f"{path.relative_to(ROOT)}: filename must match record id {value['id']!r}")
        records.append(value)
    return records


def _required(record: dict[str, Any], fields: tuple[str, ...], label: str, errors: list[str]) -> None:
    for field in fields:
        if field not in record or record[field] is None or record[field] == "":
            errors.append(f"{label}: missing required field {field!r}")


def _unique_ids(records: list[dict[str, Any]], kind: str, errors: list[str]) -> dict[str, dict[str, Any]]:
    result = {}
    for record in records:
        record_id = record.get("id")
        if not isinstance(record_id, str) or not ID_RE.fullmatch(record_id):
            errors.append(f"{kind}: invalid or missing id {record_id!r}; use lowercase letters, digits, and hyphens")
            continue
        if record_id in result:
            errors.append(f"{kind}: duplicate id {record_id!r}")
        else:
            result[record_id] = record
    return result


def validate(root: Path = ROOT) -> list[str]:
    global ROOT
    original = ROOT
    ROOT = root
    errors: list[str] = []
    sources = _load_records("sources", errors)
    claims = _load_records("claims", errors)
    topics = _load_records("topics", errors)
    experiments = _load_records("experiments", errors)
    source_by_id = _unique_ids(sources, "sources", errors)
    claim_by_id = _unique_ids(claims, "claims", errors)
    topic_by_id = _unique_ids(topics, "topics", errors)
    experiment_by_id = _unique_ids(experiments, "experiments", errors)

    for source in sources:
        label = f"source {source.get('id', '<missing>')}"
        _required(source, ("id", "type", "title", "authors", "publication_status", "source_category"), label, errors)
        if "year" not in source:
            errors.append(f"{label}: missing required field 'year' (use null if unknown)")
        if not isinstance(source.get("title"), str) or not isinstance(source.get("authors"), list) or not source.get("authors"):
            errors.append(f"{label}: title must be text and authors must be a non-empty list")
        if source.get("year") is not None and (not isinstance(source["year"], int) or not 1000 <= source["year"] <= 9999):
            errors.append(f"{label}: year must be a four-digit integer")
        if source.get("source_category") not in SOURCE_CATEGORIES:
            errors.append(f"{label}: invalid source_category {source.get('source_category')!r}")

    for claim in claims:
        label = f"claim {claim.get('id', '<missing>')}"
        _required(claim, ("id", "claim", "status", "topics", "evidence", "last_reviewed"), label, errors)
        if claim.get("status") not in STATUSES:
            errors.append(f"{label}: invalid status {claim.get('status')!r}")
        if not isinstance(claim.get("claim"), str) or not isinstance(claim.get("topics"), list) or not isinstance(claim.get("evidence"), list):
            errors.append(f"{label}: claim must be text; topics and evidence must be lists")
        for topic_id in claim.get("topics", []) if isinstance(claim.get("topics"), list) else []:
            if topic_id not in topic_by_id:
                errors.append(f"{label}: references missing topic {topic_id!r}")
        for evidence in claim.get("evidence", []) if isinstance(claim.get("evidence"), list) else []:
            if not isinstance(evidence, dict):
                errors.append(f"{label}: each evidence entry must be a mapping")
                continue
            _required(evidence, ("source_id", "relationship"), label + " evidence", errors)
            source_id = evidence.get("source_id")
            if source_id not in source_by_id:
                errors.append(f"{label}: references missing source {source_id!r}")
            if evidence.get("relationship") not in RELATIONSHIPS:
                errors.append(f"{label}: invalid relationship {evidence.get('relationship')!r}")
        try:
            raw_reviewed = claim.get("last_reviewed", "")
            reviewed = raw_reviewed if isinstance(raw_reviewed, date) else date.fromisoformat(str(raw_reviewed))
            if reviewed.isoformat() != str(raw_reviewed):
                raise ValueError
        except ValueError:
            errors.append(f"{label}: last_reviewed must use YYYY-MM-DD")

    for topic in topics:
        label = f"topic {topic.get('id', '<missing>')}"
        _required(topic, ("id", "title", "type", "claim_ids"), label, errors)
        if topic.get("type") not in TOPIC_TYPES:
            errors.append(f"{label}: invalid type {topic.get('type')!r}")
        if topic.get("type") == "question" and not topic.get("question"):
            errors.append(f"{label}: question topics require a question field")
        if not isinstance(topic.get("claim_ids"), list):
            errors.append(f"{label}: claim_ids must be a list")
        else:
            for claim_id in topic["claim_ids"]:
                if claim_id not in claim_by_id:
                    errors.append(f"{label}: references missing claim {claim_id!r}")

    for experiment in experiments:
        label = f"experiment {experiment.get('id', '<missing>')}"
        _required(experiment, ("id", "title", "type", "date", "dataset", "system", "related_claims"), label, errors)
        if experiment.get("type") != "independent-experiment":
            errors.append(f"{label}: type must be 'independent-experiment'")
        try:
            date.fromisoformat(str(experiment.get("date", "")))
        except ValueError:
            errors.append(f"{label}: date must use YYYY-MM-DD")
        for claim_id in experiment.get("related_claims", []) if isinstance(experiment.get("related_claims"), list) else []:
            if claim_id not in claim_by_id:
                errors.append(f"{label}: references missing claim {claim_id!r}")

    # Avoid unused-variable lint noise while retaining distinct registries for duplicate checks.
    _ = experiment_by_id
    ROOT = original
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
