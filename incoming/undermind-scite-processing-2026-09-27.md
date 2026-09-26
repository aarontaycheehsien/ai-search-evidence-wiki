# Scite search processing - 2026-09-27

## Retrieval and provenance

The user requested an Undermind MCP search for empirical studies of Scite
Assistant, then download and processing into this wiki. The targeted search
returned four papers. Three PDFs were available and downloaded via links
returned by Undermind MCP; Krump's PDF was unavailable. The PDFs passed
`pdfinfo` and `pypdf` parsing. Text was read locally, with the key tables and
figures rendered and visually inspected. This is a curated processing record,
not a systematic search-completeness guarantee or a new independent experiment.

- [Undermind search](https://app.undermind.ai/projects/088fb2d4-b2aa-47ec-a78a-7acf932bbe10?path=%2Fresearch-assistant-tool-evaluations%2FEmpirical%20evaluation%20of%20Scite%20Assistant)
- [Raw search and metadata export](undermind-scite-search-2026-09-27.json)
- [Download manifest](undermind-scite-download-manifest-2026-09-27.json)

The raw search summary is a discovery aid, not authoritative evidence. All
paper-level claims below were checked against local full texts unless explicitly
marked abstract-only. Temporary signed download URLs are omitted from the audit.
PDFs remain ignored by Git.

Di Febo and Tranfield were byte-identical to existing local PDFs and source
records; they were retained at their existing filenames, without duplicate
source records. Moulaison-Sandy is the one new source record. Krump's abstract
and metadata were saved in the raw export, and its preprint/abstract-only
qualification remains in the source record.

## Classification against existing claims

Classifications were explained before authoritative YAML edits. Existing
assistant-002 describes task-dependent retrieval profiles without a general
winner. Existing assistant-003 uses Di Febo and Krump as contextual comparison
evidence. Neither existing claim text was rewritten. These heterogeneous tasks
do not provide commensurable estimates of one underlying accuracy construct.

| Source / finding | Classification | Wiki action |
|---|---|---|
| Di Febo: explicitly identified Scite Assistant and measured reference relevance and key-reference proportions | NEW; SUPPORTS assistant-002 | Detailed existing source; added assistant-036 and assistant-002 evidence |
| Di Febo: no untraceable citations in bounded main analysis, despite low topical relevance | NEW; QUALIFIES interpretation of citation authenticity | Added assistant-038 |
| Moulaison-Sandy: favourable paid Scite review-generation affordances | NEW; QUALIFIES a general performance ranking | New source and assistant-037; linked to assistant-002 |
| Moulaison-Sandy: no reference hallucinations reported, but no text-veracity/source-relevance audit | QUALIFIES | Contextual evidence in assistant-038 |
| Krump: no significant cross-tool concept-coverage differences, abstract only | NO CHANGE in evidence strength; QUALIFIES equivalence or accuracy interpretations | Retained preprint/abstract-only status; added contextual assistant-002 evidence and Scite tool link |
| Tranfield: ranked bibliographic search, cross-tool overlap, relevance analysis unfinished | NO CHANGE in evidence strength; QUALIFIES Assistant attribution | Added checked Scite detail to source and existing assistant-002 note; full author name verified |

No direct cross-source contradiction was established: favourable review-output
features, low clinical retrieval relevance, descriptive bibliographic overlap,
and non-significant concept-coverage tests use different tasks and outcomes.
All findings are retained with their limits. No human editorial interpretation
was changed.

## Checked findings and source locations

### Di Febo et al. (2026), DOI 10.1093/ehjdh/ztag125

- PDF p. 3, Methods - Tools explicitly names **Scite Assistant**. The source
  setting supplemented its citation database with the open web. Authors report
  free web interfaces used during August 2025-January 2026; the exact Scite
  underlying model/build is not identified in the main text.
- PDF pp. 3-4: four CRT topics, four prompts per AI tool/topic, up to ten
  references per condition. Each prompt was submitted once. Three experts
  independently assessed the pooled corpus, blinded to the originating tool.
  Relevant articles required a mean rating above 2.5 on a 0-3 scale.
- **Denominator correction:** PDF p. 4 defines both primary metrics as the
  proportion of each tool's retrieved articles rated relevant or selected as
  key references. They are precision-type measures. The looser Results prose
  about retrieving a percentage of key references must not be rewritten as
  exhaustive recall. The prior conversational term "capture" was imprecise.
- PDF pp. 5-6/Table 2: Scite contributed 113 eligible retrieval records;
  these are not asserted to be 113 unique papers across all prompt conditions.
- PDF p. 6/Figure 4 on p. 7: Scite median relevant-article proportion 20%
  (IQR 17-31%); key-reference proportion 10% (IQR 0-20%). ChatGPT-5 medians
  were 90% (IQR 88-100%) and 60% (IQR 43-68%), respectively.
- PDF pp. 3-4 and p. 8: no fabricated, untraceable references in the main
  analysis for any tool. Locatable citations with minor metadata discrepancies
  were corrected and not counted as hallucinated. The larger-list subanalysis
  tested ChatGPT only, so it does not estimate Scite behaviour for longer lists.
- PDF p. 9: narrow CRT domain, no repeated identical prompts, free tiers,
  incorporation of tool results into the reference corpus, differing corpus
  coverage and intended tool purposes, and subjective expert judgments limit
  interpretation. The study does not audit Assistant answer factuality or
  claim-source support. PDF p. 10 states no funding or declared conflict.

### Moulaison-Sandy et al. (2025), DOI 10.47989/ir30iConf46906

- PDF pp. 1 and 7 establish author names and university affiliations.
  Printed pages run 1244-1252 in Information Research 30(iConf).
- PDF pp. 4-5 (1247-1248): one team member learned/piloted each of four paid
  tools; live recorded demonstrations used a shared initial prompt requesting
  a 500-1000-word review of e-reading in Spanish and English, then interactive
  refinements. Collaborative coding continued until agreement. Only each
  system's own sources were used. A testing date, exact model, and formal
  repeated-run sample are not supplied.
- Table 1, PDF p. 5: Scite produced more than 500 words, allowed date selection,
  and isolated methodology; it could not specify peer-reviewed-only sources
  or sources by language.
- Table 2, PDF p. 5: Scite linked sources, used primary sources, referenced all
  mentioned sources, provided ten references, permitted APA output and an
  export including references, and was marked as having no reference
  hallucinations. All four tools were marked as having no such hallucinations.
- PDF p. 6: Scite could produce Spanish output, but source-language selection
  remained limited. Positive output assessment is the authors' rubric judgment,
  not an independently quantified measure of answer correctness.
- PDF p. 7 explicitly defers text accuracy, source relevance, and identification
  of important concerns to future research. The paper names **Scite** throughout,
  not **Scite Assistant**. Generative review use is apparent; exact Assistant
  feature/version attribution remains unconfirmed.

### Krump et al. (2026), DOI 10.64898/2026.08.10.26360108

Abstract only, supplied by Undermind. The preprint names Scite among eight RAG
tools evaluated on 12 ChatGPT-generated treatment/etiology/prognosis questions.
ChatGPT helped identify unique concepts, categorized as critical or non-critical,
with information-scientist input. The reported between-tool tests were p=.95
and p=.16; no single tool consistently covered all concepts. No Scite-specific
score, exact Scite feature, model/build, or tier is given in the abstract.
Non-significant tests do not establish equivalence. Detailed methods, score
denominators, citation-support checks, and limitations remain unverified.

### Tranfield and Caldwell (2024), DOI 10.1145/3678884.3681842

- PDF title page verifies **Christy Caldwell**, correcting the abbreviated
  existing author field. Authors are UCSC librarians.
- PDF p. 3: translated novice-style searches across ten STEM subdisciplines,
  first fifty relevance-ranked citations from each of six tools, searched
  May 10-17, 2024. Scite is treated as a bibliographic search tool. The paper
  does not identify Assistant or evaluate generated narrative answers.
- Figure 3, PDF p. 4 labels Scite's duplicated-result proportion **26.6%**.
  It measures overlap with other tools after combining bibliographic returns;
  it is not within-tool duplicate output or a relevance metric. The earlier
  Undermind PDF-reading approximation of 29-30% is not adopted.
- PDF p. 5: relevance analysis is still underway. No completed relevance,
  recall, or Assistant answer-quality estimate is promoted.

## Resulting records

- Tool: [Scite and Scite Assistant](../docs/tools/scite.md)
- New source: [moulaison-sandy-2025](../docs/evidence/moulaison-sandy-2025.md)
- New claims: [assistant-036](../docs/claims/assistant-036.md),
  [assistant-037](../docs/claims/assistant-037.md),
  [assistant-038](../docs/claims/assistant-038.md)
- Existing sources updated: di-febo-2026, tranfield-2024, krump-2026.
- Existing assistant-002 evidence notes/links updated; its claim wording and
  mixed status remain unchanged.

## Verification

Completed checks:

- `python scripts/validate.py`: passed.
- `python scripts/build_pages.py`: generated 196 Markdown pages.
- `python -m pytest`: all 24 tests passed.
- `python scripts/build_site.py`: generated Markdown current; local site build
  completed with no issues.
- Download provenance: all four local record paths exist; all three PDF
  SHA-256 hashes and byte lengths match the manifest; temporary signed URLs
  are absent from the saved audit.
- `git diff --check` and checks for added files: no whitespace errors.
  Complete review diff includes existing modifications and all 13 new files.

No commit or publication was performed by this processing step.
