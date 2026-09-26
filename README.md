# AI Search Evidence Wiki

A Git-based evidence wiki about AI-assisted academic search and evidence synthesis. Version 2 organizes the evidence into research topics, tool-specific evaluations, and cross-cutting concept scaffolds. Current topics cover citation screening, search-strategy generation, structured data extraction, evidence appraisal, citation fidelity, and deduplication; the separate Tools section covers evaluated research assistants and discovery systems.

The repository keeps source and claim records in YAML. Python scripts validate those records and deterministically generate Markdown pages. Zensical builds the Markdown into a static site. Codex Desktop can provide interactive reasoning while a human reviews proposed evidence changes; the repository itself makes no LLM or API calls.

The evidence records include journal studies and preprints. Most were extracted from PDFs in `incoming/papers/`; two newer records are limited to saved PubMed abstracts because full texts were unavailable. Review each source's locator and notes before relying on a claim.

## Structure

- `incoming/papers/`: place papers here for human-assisted processing.
- `data/sources/`: bibliographic and source-type records.
- `data/claims/`: stable claim records with explicit source relationships.
- `data/topics/`: topic, tool, and concept records that group claims and connect the wiki's cross-cutting concepts.
- `data/experiments/`: independent experiments, kept distinct from published research.
- `editorial/`: human-written interpretation; not generated or silently edited.
- `docs/`: site source, including generated topic, concept, claim, and evidence pages.
- `scripts/`: validation, deterministic generation, dependency reporting, stale-claim reporting, and site build tools.
- `outputs/`: reserved for future downstream briefs, textbook sections, and articles.

## Setup

Use Python 3.11 or later. Install the project and its lightweight development/site tools in a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

On macOS or Linux, activate with `source .venv/bin/activate` instead.

## Validate, generate, and build

```powershell
python scripts/validate.py
python scripts/build_pages.py
python -m pytest
python scripts/build_site.py
```

The site build validates the data and checks that generated Markdown is current before running Zensical. `zensical serve` starts a local preview after the project tools are installed.

To check whether a change is reflected in generated pages:

```powershell
python scripts/affected_pages.py --claim screening-001
python scripts/affected_pages.py --source guo-2024
```

To flag claims for review without treating age as evidence of error:

```powershell
python scripts/stale.py --days 365
```

## Processing a paper

Read [AGENTS.md](AGENTS.md) before adding evidence. Put a paper in `incoming/papers/`, ask Codex Desktop to process it according to `AGENTS.md`, review the proposed classifications and Git diff, and commit only after human review. The evidence records in `data/` are authoritative; generated Markdown must be rebuilt with `scripts/build_pages.py`.

The supported evidence relationships are `supports`, `contradicts`, `qualifies`, `contextual`, and `unclear`. Claim statuses are `supported`, `mixed`, `uncertain`, `contradicted`, and `provisional`. No numerical confidence score is used.

Incoming PDFs are ignored by Git by default, so a public repository does not automatically redistribute them. Source YAML records retain DOI or URL links when present and the local PDF filename used for extraction. A bibliographic year may be `null` when the supplied source does not establish it. Two supplied papers have a numerical discrepancy between summary prose and a results table; the source and claim records describe those discrepancies and use the table values.

## Static site and GitHub Pages

The wiki is published at [https://aarontaycheehsien.github.io/ai-search-evidence-wiki/](https://aarontaycheehsien.github.io/ai-search-evidence-wiki/). Zensical builds a static site into the ignored `site/` directory. The workflow in `.github/workflows/docs.yml` validates, checks generated files, and builds/publishes the site on pushes to `main` or `master`. No server, database, API key, or LLM service is required.

## Scope limits

Version 2 remains a curated static evidence site. It does not include hosted model calls, API integration, embeddings, vector databases, RAG, autonomous literature search, chatbot features, or automatic publication or Git commits. `outputs/` is reserved for future downstream briefs, textbook sections, and articles.
