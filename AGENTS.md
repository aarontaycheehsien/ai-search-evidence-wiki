# Repository guidance

## Purpose

This repository is a living evidence base about AI-assisted academic search and evidence synthesis. Structured evidence records are authoritative; generated pages are views over those records.

## Epistemic rules

- Never invent bibliographic metadata.
- Never invent evidence.
- Never create an empirical claim without an identifiable source.
- Distinguish peer-reviewed research from preprints.
- Distinguish vendor and system documentation from independent research.
- Distinguish independent experiments from published evidence.
- Do not turn vendor statements into established facts.
- Do not silently resolve disagreements between sources.
- Represent contradictory evidence explicitly.
- Preserve uncertainty.
- Generated prose is downstream of structured evidence.
- Structured evidence records are authoritative.
- Do not change human editorial interpretation unless explicitly requested.
- Prefer exact source wording and source locations when establishing what a paper reports.
- If evidence is insufficient, say so rather than infer a result.

## Processing a new source

When asked to process a paper placed in `incoming/papers/`:

1. Read the source.
2. Identify findings relevant to the existing evidence base.
3. Compare them against existing claims.
4. Classify each finding as `NEW`, `SUPPORTS`, `CONTRADICTS`, `QUALIFIES`, or `NO CHANGE`.
5. Explain proposed classifications before making major changes.
6. Create or update the source record.
7. Create or update claims where justified.
8. Do not delete contradictory evidence.
9. Run `python scripts/validate.py`.
10. Regenerate affected pages with `python scripts/build_pages.py`.
11. Run `python -m pytest`.
12. Show the Git diff.
13. Do not commit unless explicitly requested.

## Editing boundaries

- YAML under `data/` is the authoritative evidence layer.
- Generated topic pages and record pages under `docs/claims/` and `docs/evidence/` are generated. Do not edit them directly. Handwritten section indexes in `docs/` may be maintained normally.
- `editorial/` contains human-written interpretation. Do not silently rewrite it.
- Keep independent experiments in `data/experiments/`; never merge them into published research categories.
- Do not add API calls, hosted LLMs, embeddings, vector databases, autonomous search, or automatic commits.
