# Processing the six Consensus search candidates

Read on 2026-09-27. Structured records under `data/` remain authoritative.
No LibKey MCP calls were made. No records were committed or published.

Five candidate papers already had source records; four had local PDFs.
Reused those PDFs rather than create duplicate source records or downloads.
The new Gwon paper was read in complete Europe PMC JATS XML after public PDF
routes failed. The Gavgani paper remains abstract-only behind publisher access.

| Source | Material read | Classification and action |
| --- | --- | --- |
| Lau and Golder 2025 | Local 12-page PDF; Methods, Results and Table 1 | QUALIFIES assistant-001: reported precision/sensitivity concern retrieval plus screening. NEW assistant-040 records losses at both stages. |
| Featherstone et al. 2025 | Local 20-page PDF; Methods, Tables 2-5 and limitations | QUALIFIES assistant-002/007: retain numerical findings but identify Copilot-generated PubMed strategies, its MEDLINE-only denominator, and modeled screening time. |
| Bernard et al. 2025 | Local 6-page PDF; author list, Results, Table 1 and Figure 1 | QUALIFIES assistant-001: retain the abstract/body disagreement. Correct first author from Nicolas to Nathan, as printed on p. 1. |
| Di Febo et al. 2026 | Local 10-page PDF; Methods, Results, Figure 4 and limitations | NO CHANGE to primary findings already in assistant-002/036/038. Refresh the assistant-003 locator and remove its stale abstract-only framing for this source. |
| Gavgani et al. 2026 | Publisher abstract and linked funding corrigendum | NO CHANGE to provisional performance interpretation. Record the paywall and funding correction; full methods remain unverified. |
| Gwon et al. 2024 | Complete published-article JATS XML from Europe PMC, including Tables 1-2 | NEW source and assistant-039. CONTEXTUAL evidence for assistant-002; do not infer a current tool ranking. |

## Source locations and interpretation

- Lau/Golder: Methods, PDF pp. 2-3, starts with 500 retrieved candidates and
  applies automated screening after manual criterion adjustment. Results,
  pp. 4-6, distinguish records never retrieved from records retrieved but
  excluded. Table 1, p. 6, uses Elicit-included records as precision denominators;
  the reported means do not isolate retrieval performance.
- Bernard: Table 1, p. 3, shows 246/169/172 records over repeated searches.
  Figure 1 and Results, p. 3, give 17 prior included reviews, 3 shared,
  and 14 exclusive to the prior review. The abstract, p. 1, says 17 exclusive.
  Retain both reports and use Results/Figure 1 when establishing benchmark overlap.
- Gwon: Methods identifies GPT-3.5 and Bing AI Precise, with different conversation
  flows. Results distinguishes bibliographic grades from overlap with 24 benchmark
  RCTs: ChatGPT has 7 grade-A entries but 1 strict benchmark match and 4 matches
  under relaxed criteria; Bing has 19 grade-A entries but 2 benchmark matches.
  Output denominators are 1,287 and 48 presented entries, not the 24 included RCTs.
  Results describes one ungraded Bing fake-title/database-attribution case, while
  Discussion says Bing generated no fake studies; preserve the narrower qualification.
- Featherstone: Methods sections 2.2.5-2.2.6, PDF p. 4, specify Copilot-generated
  strategies executed in PubMed after expert prompting. Copilot recall/NNR uses
  eligible MEDLINE reference articles rather than the full cross-database reference
  set. Table 5, p. 12, estimates screening time at 3.33 hours per 100 records.
- Di Febo: Methods, p. 4, defines both primary endpoints using retrieved articles
  as denominators. They are precision-type measures. Results/Figure 4, pp. 6-7,
  does not provide a numerical overall Consensus point estimate in prose; do not
  estimate it from the plotted graphic. Limitations, p. 9, explicitly acknowledge
  the single subdomain, one run per prompt and incorporation bias.
- Gavgani: publisher article page has the four authors and the abstract, but states
  that access is unavailable. The [corrigendum](https://doi.org/10.1108/IDD-08-2026-0302)
  corrects funding information, not retrieval findings.

## Access provenance

- Published Gwon article: https://doi.org/10.2196/51187
- Full text actually read: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11107769/fullTextXML
- Publisher PDF route returned an empty response; PMC PDF routes returned HTML
  rather than PDF, Europe PMC PDF routes returned HTTP 403, and its associated-files
  endpoint timed out. No response was mislabeled as a PDF.
- Saved full-text XML and existing PDFs are ignored by Git. The accompanying
  `consensus-access-manifest-2026-09-27.json` records local paths and SHA-256 hashes.

The earlier discovery response should not be used as full-text extraction: it omitted
Gavgani from the author list and did not distinguish Gwon's relevant-reference counts
from benchmark matches. The source records here follow primary materials.
