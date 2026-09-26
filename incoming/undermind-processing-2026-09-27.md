# Undermind full-text processing — 2026-09-27

## Scope and retrieval

Used the connected Undermind MCP, not the browser, to inspect the completed [Academic literature search platform evaluations](https://app.undermind.ai/projects/088fb2d4-b2aa-47ec-a78a-7acf932bbe10?path=%2Fresearch-assistant-tool-evaluations%2FAcademic%20literature%20search%20platform%20evaluations) search, request PDF download links, download full texts and extract study details.

- Search: 118 results. Downloaded all 67 PDFs made available by MCP.
- PDFs stored locally under `incoming/papers/undermind-2026-09-27/`, excluded from Git.
- All 67 pass `pdfinfo`; Du26 initially had a corrupt cross-reference table, was downloaded again, and the replacement passed.
- [Download manifest](undermind-download-manifest-2026-09-27.json) preserves cite keys, local paths, byte lengths, SHA-256 hashes and processing status. No signed download URLs are retained in the audit.
- Full-text processing selected 24 previously unrecorded relevant papers: 23 promoted, one feature-only review excluded. The 43 other downloaded papers were not newly promoted in this batch; they include already recorded papers, older comparators and additional candidates. Downloading is not equivalent to processing.
- New authoritative records: 11 peer-reviewed studies, 11 preprints and one editorial/analytical note. Category alone does not establish independence; developer affiliations are separately recorded.
- No independent experiment was performed. Existing human editorial interpretation and unrelated changes were preserved. No commit.

## Classification against existing claims

Existing assistant-001/002/003/004/007/008/009/010 already describe task-dependent retrieval, citation errors and limitations of broad rankings. New studies were compared with those claims; they do not warrant declaring a general-purpose winner. Existing claim wording was left intact; new scoped claims carry the additional observations.

NEW means a new measured construct, product, benchmark or study in this evidence base, not that the study independently validates its own developers' system. QUALIFIES means task/interface/reference-standard limitations materially constrain the broader performance interpretation. No cross-source contradiction was silently resolved.

| Cite key | Source record | Classification | New claim |
|---|---|---|---|
| Wod24 | [wlodarczyk-2024](../docs/evidence/wlodarczyk-2024.md) | NEW | [assistant-013](../docs/claims/assistant-013.md) |
| Lop25b | [lopezosa-2025-scholar-labs](../docs/evidence/lopezosa-2025-scholar-labs.md) | NEW | [assistant-014](../docs/claims/assistant-014.md) |
| Ord25 | [orduna-malea-2025-asta](../docs/evidence/orduna-malea-2025-asta.md) | NEW | [assistant-015](../docs/claims/assistant-015.md) |
| Aji24 | [ajith-2024-litsearch](../docs/evidence/ajith-2024-litsearch.md) | QUALIFIES | [assistant-016](../docs/claims/assistant-016.md) |
| Sch20c | [schoeb-2020-iris](../docs/evidence/schoeb-2020-iris.md) | NEW | [assistant-017](../docs/claims/assistant-017.md) |
| Leo26 | [leon-2026-search-audit](../docs/evidence/leon-2026-search-audit.md) | QUALIFIES | [assistant-018](../docs/claims/assistant-018.md) |
| Agg26 | [aggarwal-2026-scholarai-scispace](../docs/evidence/aggarwal-2026-scholarai-scispace.md) | QUALIFIES | [assistant-019](../docs/claims/assistant-019.md) |
| Sch26b | [schott-2026-ai-overviews](../docs/evidence/schott-2026-ai-overviews.md) | NEW | [assistant-020](../docs/claims/assistant-020.md) |
| Cha26h | [chandler-2026-scholarly-diversity](../docs/evidence/chandler-2026-scholarly-diversity.md) | NEW | [assistant-021](../docs/claims/assistant-021.md) |
| He25b | [he-2025-pasa](../docs/evidence/he-2025-pasa.md) | NEW | [assistant-022](../docs/claims/assistant-022.md) |
| Ju25 | [ju-2025-wispaper](../docs/evidence/ju-2025-wispaper.md) | NEW | [assistant-023](../docs/claims/assistant-023.md) |
| Liu26c | [liu-2026-study-retrieval](../docs/evidence/liu-2026-study-retrieval.md) | NEW | [assistant-024](../docs/claims/assistant-024.md) |
| Gao26 | [gao-2026-retrieval-errors](../docs/evidence/gao-2026-retrieval-errors.md) | NEW | [assistant-025](../docs/claims/assistant-025.md) |
| Sah26d | [sahu-2026-search-evaluation](../docs/evidence/sahu-2026-search-evaluation.md) | NEW | [assistant-026](../docs/claims/assistant-026.md) |
| She26b | [shen-2026-scholargym](../docs/evidence/shen-2026-scholargym.md) | NEW | [assistant-027](../docs/claims/assistant-027.md) |
| Son20 | [soni-2021-covid-search](../docs/evidence/soni-2021-covid-search.md) | NEW | [assistant-028](../docs/claims/assistant-028.md) |
| Sch24d | [schneider-2024-conversational-search](../docs/evidence/schneider-2024-conversational-search.md) | NEW | [assistant-029](../docs/claims/assistant-029.md) |
| Wu25 | [wu-2025-paperask](../docs/evidence/wu-2025-paperask.md) | NEW | [assistant-030](../docs/claims/assistant-030.md) |
| Ben26c | [bentegeac-2026-biblizap](../docs/evidence/bentegeac-2026-biblizap.md) | NEW | [assistant-031](../docs/claims/assistant-031.md) |
| Kha25e | [khandelwal-2025-neurolit](../docs/evidence/khandelwal-2025-neurolit.md) | QUALIFIES | [assistant-032](../docs/claims/assistant-032.md) |
| Du26 | [du-2026-recursive-retrieval](../docs/evidence/du-2026-recursive-retrieval.md) | NEW | [assistant-033](../docs/claims/assistant-033.md) |
| Haz26 | [hazra-2026-graph-search](../docs/evidence/hazra-2026-graph-search.md) | NEW | [assistant-034](../docs/claims/assistant-034.md) |
| Wei24 | [wei-2024-docrelm](../docs/evidence/wei-2024-docrelm.md) | NEW | [assistant-035](../docs/claims/assistant-035.md) |

Dev24, *Enhancing Literature Review through AI-based Research Tools: A Comparative Study of SciSpace and Semantic Scholar*: **NO CHANGE** for empirical performance. Feature descriptions do not supply a tested query set, reference standard or measured accuracy/recall; no empirical claim/source was promoted from this item. Its extraction remains in the audit.

Previously recorded full-text studies (e.g. Lau25, Fea25, Feb26, Ber25b, Maz26, Dat26, Gal25b, Tra24d) were not duplicated. Gol25 is an earlier Lau/Golder preprint: do not substitute its older numerical estimates for the published record.

## Findings for the named systems

- **Scopus AI:** independent four-question comparison with Scholar GPT, plus a four-topic result-composition audit. The former uses asymmetric prompts/audits; the latter measures representation, not precision or recall.
- **Google Scholar Labs:** a launch-period functional note and a formal quantitative PaSaMaster developer benchmark. The latter reports Scholar Labs recall@20 29.01%, precision@20 18.79%, F1@20 18.87% and NDCG@20 30.54% on 244 queries/38 disciplines (Table 2, PDF p. 7). These are benchmark-specific developer-reported estimates, not independent general validation.
- **Semantic Scholar:** the diversity audit provides descriptive result-composition evidence. The feature review is not an accuracy benchmark; evidence here is insufficient for a general recall/precision conclusion.
- **Web of Science Research Assistant:** selected MCP PDF requests Soo25 and Zhu26c returned unavailable. This does not mean no studies exist; no unsupported full-text claim was created. Conventional Web of Science comparisons are not Research Assistant evaluations.
- **Leapspace:** no directly relevant retrieved source was identified in this search. Absence from a search is not a performance result.
- **Asta, IRIS.AI, ScholarAI, WisPaper and prototypes:** separately documented. SciSpace custom-GPT results are explicitly not standalone SciSpace results.

## Verification and unresolved discrepancies

Undermind PDF extraction notes are machine-assisted and non-authoritative. Relevant methods/results were checked in local PDF text; key tables for Asta, the diversity study, citation audit and overview study were visually inspected. No dataset reanalysis, independent replication or exhaustive verification of every statement in every downloaded PDF is claimed.

Corrections made before promotion:

1. **Chandler Table 2:** counts 27/29/etc refer to papers with first authors based in **Global Majority** countries, not Global North. The initial machine extraction inverted the construct; authoritative claim assistant-021 uses the verified caption. Five conventional-tool displayed totals disagree with their row components; aggregate 115 nevertheless agrees. Do not infer a conventional-tool ranking from the conflicting totals.
2. **Asta:** first-round table totals imply mean 26.2, whereas prose says 22.2; maximum 40 in table versus 42 in prose. Repeat overlap is first-round-set recovery, not Jaccard.
3. **LitSearch/PaSa/Schneider:** published ACL Anthology records were verified; downloaded PDFs are arXiv manuscripts, not evidence of preprint-only status.
4. **IRIS.AI:** downloaded article is *Interactive Journal of Medical Research* 9(1), e16606, not JMIR Medical Informatics.
5. **Leon:** counts disagree across Tables 2/4/5/10; no pooled accuracy or clean aggregate tool ranking promoted. Failed runs are separated from ordinary instability.
6. **NeuroLit:** Consensus exceeds NeuroLit in the displayed table (38% versus 36%), despite broad outperforming language. Undocumented timing assertions are not a measured controlled effect.
7. **Crase/DocReLM:** conflicting table/figure baseline values remain explicitly recorded.
8. **PaperAsk and NeuroLit:** verified local preprints classified conservatively; later venue metadata/copyright does not independently establish publication here. Schott's future November 2026 conference header also does not establish completed publication as of this processing date.
9. **PaSa/WisPaper:** expert pooled reference sets and developer involvement are explicit; component classification accuracy is not end-to-end retrieval recall. Reported zero hallucination in one sample is not a guarantee.

Raw extraction transcripts: [platform papers](undermind-platform-full-text-extractions-2026-09-27.md), [related systems](undermind-related-system-extractions-2026-09-27.md). Use source YAML and scoped claims, not these transcripts, as the evidence layer.

## Repository verification

Run after authoritative edits: `python scripts/validate.py`, `python scripts/build_pages.py`, `python -m pytest`. Generated pages are downstream views, not manually edited evidence. Existing source-count test expectations were updated for the newly linked records; an audit-manifest provenance test was added.

Results: validation passed; 191 pages regenerated; **24 tests passed**; `git diff --check` passed. Git diff and an example new-claim diff were displayed, and the review panel was requested. Temporary signed-link cache was removed; downloaded PDFs remain recoverable locally.

Review the Git diff; downloaded PDFs and temporary extraction/rendering files are not committed. The pre-existing Kotula/Primo changes remain user-owned and are outside this batch.
