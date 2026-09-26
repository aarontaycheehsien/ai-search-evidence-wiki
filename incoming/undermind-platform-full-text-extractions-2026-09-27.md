# Undermind MCP full-text extractions

Verification corrections and final classifications are in [the processing report](undermind-processing-2026-09-27.md). This raw machine transcript contains errors, including the diversity study's Global Majority/Global North label and IRIS.AI venue; it is not authoritative evidence.

Machine-assisted extraction notes; verify against local PDFs before promotion to authoritative evidence. Workspace: 088fb2d4-b2aa-47ec-a78a-7acf932bbe10. Date: 2026-09-27.

[Wod24]:
### Bibliographic Metadata & Context

- **Exact Title:** Sztuczna inteligencja jako element wsparcia pracy badawczej. Analiza porównawcza narzędzi Scopus AI i Scholar GPT
- **Authors:** Bartłomiej Włodarczyk, Adam Jachimczyk
- **Affiliation:** Uniwersytet Warszawski (University of Warsaw), Poland
- **Venue:** *Studia Medioznawcze* (Media Studies)
- **Publication Date & Status:** 2024, Vol. 25, No. 4 (99), pp. 223–245; published open access (CC BY-NC; ISSN 2451-1617)
- **DOI:** None printed in the article text or running headers (website given as `https://studiamedioznawcze.eu`).
- **Author Contributions & Conflicts of Interest:** Author contribution is explicitly reported in footnote 1 (p. 1): 80% Bartłomiej Włodarczyk, 20% Adam Jachimczyk. No conflict of interest or commercial funding is stated.

---

### Empirical Design & Setup

- **Study Design:** Descriptive comparative case study evaluating generative AI search tools on four sequential research queries related to academic libraries and social media within a single conversation thread (pp. 3, 6).
- **Tools & Versions Tested:**
  - **Scopus AI (SAI):** Trial access version provided to Polish universities by Elsevier, based on OpenAI LLM architecture with RAG Fusion querying post-2013 Scopus metadata (pp. 4, 6).
  - **Scholar GPT (SGPT):** Custom GPT developed by awesomegpts.ai, accessed via ChatGPT Plus interface ("Odkryj modele GPT"), querying indexed academic repositories including Google Scholar, PubMed, JSTOR, and arXiv (pp. 5, 6).
  - **Evaluation Tooling:** Custom Python scripts, Sentence Transformers model `all-mpnet-base-v2` for cosine semantic similarity, YAKE! for keyword extraction (bigrams, window size 2), and Flesch Reading Ease formula (pp. 7–8).
- **Queries Evaluated:**
  1. *How do academic libraries use social media?*
  2. *What are some effective strategies for academic libraries to engage with students on social media?*
  3. *How do academic libraries measure the impact of their social media presence on student engagement and resource usage?*
  4. *What are the ethical considerations for academic libraries when using social media to promote their resources and services?*
  - For SGPT, adapted prompts were used to mirror SAI's structured elements: appending instructions to include post-2013 scholarly references (1.A), generate a concept map (1.B), and list the three most prominent researchers (1.C) (p. 6).
- **Comparator / Reference Standard:**
  - No external ground-truth benchmark dataset was used (purely descriptive evaluation).
  - Verification was conducted manually using Google search, publisher landing pages, APA 7th edition citation formatting standards, and author profiles on Scopus and Google Scholar (p. 8).
  - Citation relevance was operationally tested by verifying the co-occurrence of the exact bigrams `academic library` and `social medium` in cited publication titles (p. 8).

---

### Key Measured Findings & Numerical Results

#### 1. Textual Output Statistics & Semantic Similarity
- **Cosine Similarity (Sentence Transformers):** High overall similarity between SGPT and SAI across all queries (pp. 9–10, Table 2).
  - Short SAI vs. SGPT: Q1 = 0.9329; Q2 = 0.9265; Q3 = 0.9383; Q4 = 0.9586.
  - Expanded SAI vs. SGPT: Q1 = 0.9392; Q2 = 0.9281; Q3 = 0.9184; Q4 = 0.9031.
  - Difference between mean coefficients was minimal (0.0169) (p. 10).
- **Readability (Flesch Reading Ease):** All outputs fell into the difficult/academic range (<50) (p. 11, Wykres 1).
  - Mean score: SGPT = 36.19; Short SAI = 33.79; Long SAI = 28.44.
  - Range: easiest was SGPT Q2 (42.01); most complex was Long SAI Q4 (20.40).

Table 1 summarizes the textual dimensions across the 4 queries:

Table 1 reports the quantitative length characteristics of generated texts (character counts, word counts, unique words, syllable counts, sentence counts, and average words per sentence) across short SAI summaries, long SAI summaries, and SGPT responses for all four research queries.
[REGION: page=9, bbox=155,90,466,908]

#### 2. Bibliographic Citations & Retrieval Quality
- **Citation Volume:**
  - SAI Short: 23 citations total (mean 5.75; Q1: 7, Q2: 4, Q3: 7, Q4: 5) (p. 12, Wykres 2).
  - SAI Expanded: 42 citations total (mean 10.50; Q1: 12, Q2: 7, Q3: 12, Q4: 11) (p. 12, Wykres 2).
  - SGPT: 39 citations total (mean 9.75; Q1: 16, Q2: 12, Q3: 5, Q4: 6) (p. 12, Wykres 2).

Wykres 2 illustrates the distribution of citation counts across all queries:

Wykres 2 shows a column chart comparing the number of bibliographic citations produced for each of the four queries by SAI short summaries, SAI long summaries, and SGPT.
[REGION: page=12, bbox=122,89,612,908]

- **Fabrication / Hallucination Rate:**
  - 0% fabricated sources. All 39 SGPT citations and all SAI citations corresponded to real, findable publications (pp. 12, 18).
- **Formal Accuracy (SGPT):**
  - Fully correct descriptions: 18 / 39 (46%) (p. 12).
  - Citations with omissions: 17 / 39 (44%), including 14 / 39 (36%) lacking volume, issue, or page/article numbers; 2 missing publishers and editors; 1 missing publisher (p. 12).
  - Citations with errors: 5 omitted authors; 2 incorrect issue numbers; 2 broken links; 2 incorrect page/article numbers; 1 erroneous journal title (`Proceedings of the Association for Information Science and Technology` mislabeled as `Proceedings of the ASIS&T Annual Meeting`) (pp. 12–13).
  - SAI had 0 formal citation errors due to direct metadata sourcing from Scopus (p. 12).
- **Topical Relevance of Citations (Title Keyword Match):**
  - SGPT: 0 / 39 (0%) contained both `academic library` and `social medium` in the title; 25 / 39 contained only `social medium`; 14 / 39 contained neither (p. 13, Table 3; p. 14).
  - SAI Short: 6 / 23 (26.1%) contained both keywords; 13 / 23 contained `social medium`; 1 / 23 contained `academic library`; 3 / 23 contained neither (p. 13, Table 3).
  - SAI Expanded: 17 / 42 (40.5%) contained both keywords; 19 / 42 contained `social medium`; 2 / 42 contained `academic library`; 4 / 42 contained neither (p. 13, Table 3).

Table 3 details the exact citation relevance breakdown:

Table 3 details the occurrence of topical bigrams ('academic library' and 'social medium') in the titles of citations generated by SAI (short and long) and SGPT across the four queries.
[REGION: page=13, bbox=287,89,926,908]

#### 3. Concept Maps
- **Node Breadth & Structure:**
  - SAI: 42 total concept nodes, 20 multi-word phrases. Fixed 3-tier hierarchy (root -> 2–5 sub-concepts -> max 9 leaf concepts) (pp. 14–15).
  - SGPT: 54 total concept nodes, 37 multi-word phrases. 3-tier structure (except Q4), broader branching (5–10 sub-concepts, 5–14 leaf concepts) (pp. 14–15).
  - Information density: Concept words represented 3.57% of response words in SAI vs. 12.58% in SGPT (p. 19).
  - Shared overlap: Only 7 concepts were shared across both tools; 0 shared concepts for Q4 (p. 14).

#### 4. Domain Expert Recommendations
- **Accuracy & Faithfulness:**
  - SAI: Proposed 3 experts for Q1 and 3 for Q2; returned an explicit message stating no experts were found for Q3 and Q4 (`No topic experts for your query found`). All 6 proposed experts were verified as having direct, high-relevance publications in the target area, with functional links directly to Scopus author profiles (pp. 15–16, Table 4).
  - SGPT: Returned 3 experts for every query (12 total positions; duplicated the identical 3 names across Q3 and Q4, resulting in 9 unique individuals). Upon verification: 0 had high relevance, 3 had low/indirect relevance, and 6 had zero connection to the query topic (e.g., economists or unrelated educational administrators). Furthermore, provided URLs were frequently invalid or pointed to unrelated scholars (e.g., Tak-Lon Wu's link resolved to Jonathan Reynolds at Oxford) (pp. 15–17, Table 4).

Table 4 details the expert evaluation:

Table 4 lists the domain experts suggested by SAI and SGPT across all queries, documenting their affiliations, profile sources, and author-verified topic relevance ratings ('Wysoki', 'Niski', 'Brak').
[REGION: page=16, bbox=90,89,944,908]

---

### Internal Inconsistencies & Contradictions Within the Paper

- **Text vs. Table 1 Conflict on Page 9:**
  The body text on page 9 states that the statistics for SGPT on Question 3 are higher than those for short SAI texts, with the sole exception of words per sentence (*"Statystyki uzyskane w odpowiedzi na pytanie trzecie w SGPT są wyższe od tych dla krótkich tekstów SAI z wyjątkiem liczby słów w zdaniu"*). However, Table 1 shows the exact opposite: for Question 3, short SAI exceeds SGPT in characters (1434 vs. 1419), total words (246 vs. 228), unique words (144 vs. 116), syllables (435 vs. 427), and average words per sentence (15.38 vs. 13.41). SGPT is higher only in sentence count (17 vs. 16).

---

### Limitations Disclosed by Authors

1. **Small Query Sample & Single Thread:** Limited to four consecutive queries within a single thematic domain (social media in academic libraries) in one session (pp. 6, 20).
2. **Prompt Asymmetry:** SAI provides a standardized out-of-the-box interface, whereas SGPT required manual prompt engineering and chained prompting, which can introduce conversational drift and prompt-formatting variance (pp. 6, 20).
3. **Superficial Citation Relevance Metric:** Relevance was evaluated strictly on the presence of two bigrams in publication titles rather than full abstract or full-text screening (pp. 8, 20).
4. **No Qualitative / Factual Synthesis Analysis:** The generated explanatory texts were not evaluated for deeper factual veracity, scientific correctness, or faithfulness to the cited documents (p. 20).
5. **Database Coverage Biases:** Scopus underrepresents non-English, humanities, and Global South publications, while Google Scholar lacks curation, transparent filtering, and structured query controls (pp. 4, 20).

---

### Reference List Entry
- Włodarczyk, B., & Jachimczyk, A. (2024). Sztuczna inteligencja jako element wsparcia pracy badawczej. Analiza porównawcza narzędzi Scopus AI i Scholar GPT. *Studia Medioznawcze*, 25(4), 223–245. https://studiamedioznawcze.eu

---

[Lop25b]:
### Metadata & Administrative Details
- **Title (printed):** *Scholar Labs: hacia las respuestas académicas vitaminadas con IA* (English: *Scholar Labs: Towards AI-powered academic responses*) [p. 1]
- **Authors:** Carlos Lopezosa, Enrique Orduña-Malea [p. 1]
- **Affiliations:**
  - Carlos Lopezosa: Universitat de Barcelona (lopezosa@ub.edu) [p. 1]
  - Enrique Orduña-Malea: Universitat Politècnica de València (enorma@upv.es) [p. 1]
- **DOI:** `10.3145/thinkepi.2025.e19a28` [p. 1]
- **Venue / Date / Status:** *Anuario ThinkEPI*, v. 19, e19a28 (2025); published on *IweTel* on November 22, 2025; short analytical note (*nota* / *trabajo breve*) [pp. 1–2]
- **Funding:** Project PID2022-142569NA-I00 (MCIN/AEI/10.13039/501100011033 and ERDF) [p. 10]
- **Conflicts of Interest:** None declared (*"Los autores declaran no tener conflictos de interés..."*) [p. 10]

---

### Empirical Design, System Tested & Scope
- **Study Type:** Descriptive, exploratory functional analysis of a newly launched beta feature. No benchmark dataset or automated evaluation harness was used [pp. 1–3].
- **Tool Evaluated:** Google Scholar Labs (beta interface accessed through Google Labs) [p. 2].
- **Capture Dates:** November 19, 2025 and November 22, 2025 [pp. 2, 4–9].
- **LitSearch / Commercial Comparison Table:** None included. The authors only briefly mention in the discussion that Scholar Labs aligns functionally with Scopus AI or Web of Science Research Assistant (deep search/synthesis) rather than theoretical framework generators like Elicit or Epsilon [p. 10, §5].

---

### Queries & Sample
1. **Four built-in default prompts:**
   - *Prompt 1 (specific methodology):* `"Has anyone used single molecule footprinting to examine transcription factor binding in human cells?"` [p. 3, Fig. 3]
   - *Prompt 2 (comparative/evaluative):* `"Are hydrogen powered cars, compared to electric / internal combustion engine cars, really better for the environment?"` [p. 3, Fig. 4]
   - *Prompt 3 (clinical/professional criteria):* `"What is the standard of care for intraductal papilloma without atypia? When is surgical excision recommended, and when can it be managed conservatively?"` [p. 3, Fig. 5]
   - *Prompt 4 (temporal/emerging tech):* `"Find papers from the past 2 years about how to determine whether an abstractive summary generated by an LLM is grounded."` [p. 3, Fig. 6]
2. **Authors' custom queries:**
   - *Query 1 (broad state-of-the-art):* `"What is the current state of the Webometrics (also known as Cybermetrics) discipline in 2025, considering its advantages, limitations, current applications, and main lines of research?"` [p. 6, Fig. 7]
   - *Query 2 (evaluative synthesis):* `"How effective is the h-index in assessing researchers' impact, and what are its main advantages, limitations, and existing variants?"` [p. 7, Fig. 8]
   - *Query 3 (author publication search):* `"Give me the most representative articles by Mike Thellwall"` [p. 8, Fig. 9]
   - *Query 4 (field top citations):* `"Give me the most cited articles on search engine optimization"` [p. 8, Fig. 10]
   - *Query 5 (workflow/multi-query test):* `"What is COARA"` [p. 9, Fig. 11]

---

### Retrieval, Citation, Reproducibility & Measured Findings

#### 1. Retrieval & Interface Architecture [pp. 2, 9, §2, §4]
- **Execution Pipeline:** Deconstructs the natural-language prompt into key concepts, sub-queries, and relations. For `"What is COARA"`, it spawned 11 distinct internal Google Scholar queries [p. 9, §4].
- **Result Pagination & Limits:** Displays 10 results initially per evaluation batch; clicking *"More results"* retrieves subsequent batches of 10 up to an observed ceiling of 50 total results [p. 9, §4].
- **Result Display:** Results appear in a single continuous scrolling pane on the right alongside sub-queries on the left, rather than separate result pages [p. 9, §4].
- **Reproducibility:** Search behavior depends on Google Scholar's underlying index, user profile/access configuration, and generative model synthesis [pp. 7, 9].

#### 2. Measured Findings vs. Qualitative Interpretations
- **Author-Specific Query (`Mike Thellwall`):** Failed completely. Scholar Labs returned 0 results with the message that it is not designed to answer such queries [p. 8, Fig. 9].
- **Most-Cited SEO Query:**
  - *Measured breakdown:* Returned non-optimal items; only 1 out of 4 visible items was a standard journal article (Killoran, 2013). The remaining 3 were 1 book (Thurow, 2003), 1 conference paper (Drivas et al., 2019), and 1 preprint (Godlevsky et al., 2017) [p. 9, §3].
  - *Comparator Check against standard Google Scholar:* Omitted highly cited core texts present in traditional Scholar, e.g., Ledford (2015) with 474 citations as of November 19, 2025 [p. 9, §3].
- **h-index Query:** Generated 10 enriched snippet cards. From the first 3 inspected, Scholar Labs generated synthetic summary snippets regardless of whether full text was accessible (2 lacked open full text, 1 had full text) [p. 7, §3].
- **Webometrics SOTA Query:** Retrieved partially coherent papers (first 3 inspected: 1 direct systematic review, 1 older conceptual paper, 1 altmetrics paper); omitted key historical foundations [pp. 6–7, §3].

---

### Internal Contradictions & Reporting Anomalies
1. **Misspelled Author Name in Prompt:** In prompt 3 (`"Give me the most representative articles by Mike Thellwall"`), the authors typed "Thellwall" with two "l"s [p. 8], whereas the cited researcher is correctly spelled "Mike Thelwall" [p. 6, 11]. The authors did not assess whether this typo contributed to the tool's refusal message.
2. **Product Naming Slip:** On page 9, the text accidentally refers to Google's feature as *"Search Labs"* instead of *Scholar Labs* (*"...también deberían haber aparecido en Search Labs"*).
3. **Date Inconsistencies:** The publication date, event timeline, and citations (e.g., Yuan et al., 2025; Shelley, 2025; Tay, 2025; Anuario ThinkEPI 2025) are dated in late 2025, which may represent an advance volume date or publishing typo.

---

### Reference
- Lopezosa, C.; Orduña-Malea, E. (2025). "Scholar Labs: hacia las respuestas académicas vitaminadas con IA". *Anuario ThinkEPI*, v. 19, e19a28. https://doi.org/10.3145/thinkepi.2025.e19a28

---

[Ord25]:
### Paper Metadata

* **Exact Title:** Unraveling the Ai2 Asta Scholarly Research Assistant Citation System [p. 1]
* **Authors:** Enrique Orduña-Malea and Carlos Lopezosa [p. 1]
* **DOI:** `10.21555/rpc.v7i2.3675` [p. 1]
* **Venue, Date, and Status:**
  * *Revista Panamericana de Comunicación*, Vol. 7, No. 2, July–December 2025, article 3675 [p. 1].
  * Received: 25-11-2025; Accepted: 04-12-2025; Published online: 06-12-2025 [p. 1].
  * Publication status: Published article (Open Access, CC BY 4.0) [p. 1].
* **Affiliations:**
  * Enrique Orduña-Malea: Universitat Politècnica de València, The iMetrics Lab, Spain (`enorma@upv.es`; ORCID: 0000-0002-1989-8477) [p. 1].
  * Carlos Lopezosa: Universitat de Barcelona, Department de Biblioteconomia, Documentació i Comunicació Audiovisual, Spain (`lopezosa@ub.edu`; ORCID: 0000-0001-8619-2194) [p. 1].
* **Funding:** Grant PID2022-142569NA-I00 funded by MCIN/AEI/10.13039/501100011033 and ERDF [p. 14].
* **Conflicts of Interest:** The authors explicitly declare no competing interests [p. 15].

---

### Empirical Design and Methodology

* **Study Design:** Exploratory, descriptive informetric study evaluating the citation characteristics, reproducibility, and stability of AI-generated literature reports [pp. 3–5].
* **System Under Evaluation:**
  * **Tool:** Ai2 Asta (specifically the *Summarise Literature* / Scholar QS feature; URL: `https://asta.allen.ai/discover`), developed by the Allen Institute for AI and launched August 25, 2025 [pp. 4–5].
  * **Underlying Architecture:** Semantic Scholar API endpoints (108 million abstracts keyword index; 12 million full-text papers snippet index), neural re-ranking returning up to 256 snippets and 20 abstracts, generating synthesized text sections with linked citations [p. 4].
  * **Global Baseline Dataset:** Ai2’s open dataset *Asta Summary Citation Counts* (`sqa_citation_ranking_all_time.parquet`, downloaded October 28, 2025), comprising 113,000 queries, ~4,000,000 citations, and ~2,000,000 publications [pp. 4, 6, 12].
* **Queries & Disciplinary Sample:** 10 complex domain-specific questions in quantitative science studies and bibliometrics (e.g., h-index, altmetrics, webometrics, open-access citation advantage, university rankings) [Table 1, p. 5].
* **Sampling Rounds:** Executed twice with identical machines, locations, and configurations:
  * Round 1: October 29, 2025 [p. 6].
  * Round 2: November 2, 2025 [p. 6].
* **Comparator / Reference Standard:** No ground-truth retrieval benchmark (e.g., no TREC-style relevance gold standard or predefined systematic review pool); the evaluation is purely observational and test-retest comparative [p. 5].

---

### Measured Results vs. Interpretations

#### 1. Citation Intensity and Length (Measured)
* **Report Word Count:** 1,461 to 3,129 words in Round 1; 1,500 to 3,716 words in Round 2 [Table 2, pp. 6–7].
* **Passages & Abstracts Retrieved:** Average passages retrieved was 249 across both rounds (system upper cap is 256). Abstracts retrieved ranged from 0 to 19 per query [Table 2, pp. 6–7].
* **Papers Cited per Report:**
  * Round 1: Mean = 22.2 (range: 8 to 40) [Table 2, p. 6].
  * Round 2: Mean = 27.3 (range: 9 to 42) [Table 2, p. 7].
  * Pearson correlation between cited paper counts across rounds: $R_p = 0.86$ [p. 6].
* **In-Text Claims/Citations:**
  * Round 1: Mean = 78.3 (range: 38 to 109) [Table 2, p. 6; p. 7].
  * Round 2: Mean = 73.7 (range: 35 to 113) [Table 2, p. 7].
  * High citation-to-reference ratio indicating identical references are cited repeatedly across report sections [p. 7].

Table 2 presents the query-level search parameters, retrieval numbers, and structural metrics across both data collection rounds:
[REGION: page=6, bbox=587,88,908,739]

#### 2. Retrieval-to-Citation Disconnect (Measured vs. Author Interpretation)
* **Measured:** In 50% of queries (5 out of 10), the number of papers cited in the final report exceeded the number of relevant papers identified during the deep search phase [Table 2, pp. 6–7; p. 7].
* **Author Interpretation:** The authors deduce that papers are either discarded or dynamically injected during the report generation/synthesis phase via unlogged mechanisms [p. 7].

#### 3. Citation Stability / Test-Retest Overlap (Measured)
* **Overlap Rate:** Overlap of cited references between Round 1 and Round 2 ranged from 34.2% (Query 6: 13/38 shared) to 95.5% (Query 10: 21/22 shared) [p. 8].
* **Detailed Pairwise Counts (Round 1 / Round 2 / Shared):**
  * Q1: 8 in R1, 9 in R2, 4 shared (50.0% of R1)
  * Q2: 40 in R1, 42 in R2, 34 shared (85.0% of R1)
  * Q3: 24 in R1, 35 in R2, 22 shared (91.7% of R1)
  * Q4: 17 in R1, 15 in R2, 14 shared (82.4% of R1)
  * Q5: 27 in R1, 32 in R2, 20 shared (74.1% of R1)
  * Q6: 38 in R1, 29 in R2, 13 shared (34.2% of R1)
  * Q7: 36 in R1, 38 in R2, 27 shared (75.0% of R1)
  * Q8: 24 in R1, 24 in R2, 20 shared (83.3% of R1)
  * Q9: 26 in R1, 23 in R2, 16 shared (61.5% of R1)
  * Q10: 22 in R1, 26 in R2, 21 shared (95.5% of R1) [Figure 1, p. 8].
* **Field Classification Shifts:** In 4 out of 10 queries, Asta assigned different disciplinary tags between identical queries (e.g., Query 8 shifted from "Sociology, Business" to "Sociology, Education") [Table 2, pp. 6–7; p. 8].

Figure 1 illustrates the Venn diagrams showing shared and unique cited references per query between Round 1 and Round 2:
[REGION: page=8, bbox=172,88,561,739]

#### 4. Bibliographic Diversity and Venue Concentration (Measured)
* **Unique Venues:**
  * Round 1: 262 references from 105 unique venues; only 19.0% of venues appeared more than once [p. 8].
  * Round 2: 273 references from 111 unique venues; 20.7% appeared more than once [p. 8].
* **Top Venues Cited (Round 1 / Round 2):** *Scientometrics* (41 / 44), *PLoS ONE* (20 / 20), and *arXiv.org* (15 / 20), together representing 29.0% (Round 1) and 30.8% (Round 2) of all citations [Table 3, p. 9].
* **Recency (Publications from 2023 onwards):**
  * Round 1: 12.5% to 41.7% per query [Table 4, p. 9].
  * Round 2: 3.8% to 44.4% per query [Table 4, p. 9].
* **Citation Counts of Cited Works:**
  * Highly cited (>100 citations): 56/262 (21.4%) in Round 1; 57/273 (20.9%) in Round 2 [p. 10].
  * Zero citations: 28/262 (10.7%) in Round 1; 29/273 (10.6%) in Round 2 [p. 10].
* **Global Dataset Characteristics ($N = 2,100,007$ citations across 113,000 queries):**
  * 55.2% (1,158,500) were published in 2020 or later [p. 12].
  * Leading venues globally: *arXiv.org* (53,903 publications; 160,419 citations) and *PLoS ONE* (32,345 publications; 72,910 citations) [Table 5, p. 12].
  * Top fields of study queried: Medicine (300,908 queries) and Computer Science (112,680 queries) [Table 6, p. 13].

Table 4 details the venue spread, recent publication share, and citation impact averages and medians across all ten queries:
[REGION: page=9, bbox=394,88,881,739]

---

### Internal Contradictions Noted in the Paper

1. **Discrepancy in Maximum Cited References for Round 1:** In Section 4.1, the text states that citations in Round 1 ranged from "8 citations in Q1 to 42 in Q2" [p. 6]. However, Table 2 lists Query 2 as having 40 papers cited in Round 1, and 42 papers cited in Round 2 [Table 2, pp. 6–7].
2. **Incorrect Table Reference:** In Section 4.3, the text states "as shown in Table 3" when discussing mean and median citation counts across queries [p. 10]. However, Table 3 contains venue rankings, whereas the referenced mean and median citation figures are in Table 4 [p. 9].

---

### Study Limitations

* **Sample Size & Scope:** Only 10 queries, limited strictly to topics within quantitative science studies and bibliometrics [pp. 5, 11, 14].
* **Absence of Ground-Truth Accuracy Benchmark:** Did not evaluate textual correctness, citation attribution veracity, factual accuracy, or relevance to the prompt [p. 14].
* **Functionality Scope:** Only analyzed the *Summarize Literature* deep research tool, omitting Asta's *Find Papers* search mode [p. 11].
* **Metadata Normalization Issues:** Raw data contained missing venues (23 references in Round 1, 19 in Round 2) and duplicated/unnormalized venue names (e.g., PNAS vs. Proc. Natl. Acad. Sci. USA) [p. 11].
* **Temporal Snapshot:** Conducted over two time points 4 days apart, capturing short-term variability rather than longitudinal algorithm drift [pp. 6, 14].

---

[Aji24]:
### 1. Document Metadata

* **Exact Title:** LitSearch: A Retrieval Benchmark for Scientific Literature Search [p. 1]
* **Complete Authors:** Anirudh Ajith, Mengzhou Xia, Alexis Chevalier, Tanya Goyal, Danqi Chen, Tianyu Gao [p. 1]
* **DOI:** None printed on the manuscript [pp. 1–16].
* **Venue / Date / Status as Printed:** arXiv preprint (`arXiv:2407.18940v2 [cs.IR] 16 Oct 2024`) [p. 1]. No peer-reviewed publication venue, journal, or formal conference citation is printed on the document.
* **Affiliations:**
  1. Princeton Language and Intelligence (PLI), Princeton University [p. 1]
  2. BCG X [p. 1]
* **Conflicts of Interest / Funding:** No conflicts of interest are stated [pp. 1–16]. Funding acknowledgments include an IBM PhD Fellowship, an NSF CAREER award (IIS-2239290), and Microsoft Azure credits via the Accelerate Foundation Models Academic Research Initiative [p. 9, Acknowledgements].

---

### 2. Empirical Design, Dataset, and Tools

#### Benchmark Corpus and Query Sample
* **Target Retrieval Corpus ($\mathcal{P}$):** 64,183 scientific papers (comprising 59,383 ACL Anthology papers and 4,807 ICLR papers, with 7 papers shared between subsets) drawn from the Semantic Scholar Open Research Corpus (S2ORC, version 2024-03-26) [p. 4, §2.5; p. 13, App. C]. Average length: 134 words for title/abstract; 6,041 words for full text [p. 4, §2.5].
* **Query Set ($N = 597$ total questions):**
  * **Inline-Citation Questions ($n = 351$):** Sampled citation paragraphs rewritten using GPT-4 with two demonstration examples [p. 2, §2.1; p. 3, §2.1; p. 15, App. E], filtered by title word overlap (< 0.3 for ACL-sourced; < 0.1 for non-ACL sourced) [p. 3, §2.1], and manually filtered [p. 3, §2.3]. Subsets: 120 broad questions (32 ACL-sourced, 88 non-ACL) and 231 specific questions (66 ACL-sourced, 165 non-ACL) [p. 4, Table 2; p. 16, Table 14].
  * **Author-Written Questions ($n = 246$):** Manually solicited from authors of ACL 2023 ($n = 155$ retained from 175 received) and ICLR 2024 ($n = 91$ retained from 117 received) [p. 3, §2.2; p. 4, §2.3]. Subsets: 35 broad questions (25 ACL 2023, 10 ICLR 2024) and 211 specific questions (130 ACL 2023, 81 ICLR 2024) [p. 4, Table 2; p. 16, Table 14].
* **Reference Standard:** Ground truth consists of one or more papers cited by the sampled paragraph or authored by the question contributor [p. 2, §2; p. 4, Table 2].

#### Evaluated Tools and Specific Versions
* **Sparse Retriever:** BM25 [p. 4, §3.2].
* **Dense Embedding Retrievers:**
  * GTR-T5-large (`sentence-transformers/gtr-t5-large`, 512 max context tokens) [p. 4, §3.2; p. 6, §4.1; p. 13, App. D].
  * Instructor-XL (`hkunlp/instructor-xl`, 512 max context tokens) [p. 4, §3.2; p. 6, §4.1; p. 13, App. D].
  * E5-large-v2 (`intfloat/e5-large-v2`, 512 max context tokens) [p. 4, §3.2; p. 6, §4.1; p. 13, App. D].
  * GritLM-7B (`GritLM/GritLM-7B`, 2,048 max context tokens) [p. 4, §3.2; p. 6, §4.1; p. 13, App. D].
* **LLM Rerankers:** GPT-4o (`gpt-4o-2024-05-13`) evaluated under vanilla listwise reranking ($n = 100$ candidate papers) and one-hop citation reranking ($m = 50$ seeds expanded to $n = 200$ papers) [p. 4, §3.2; p. 5, §3.2; p. 16, Table 13].
* **Commercial Search Tools:** Google Search, Google Scholar, and Elicit (tested via incognito browser sessions) [p. 7, §4.3].

---

### 3. Measured Findings and Numerical Results

#### A. Main Benchmark Evaluation (Title + Abstract Default) [p. 5, Table 3]
* **Broad Questions ($N = 155$ total: 120 inline, 35 author):**
  * BM25: R@20 = 37.4% (inline), 48.6% (author), 39.9% (average).
  * GTR-T5-large: R@20 = 45.7% (inline), 37.1% (author), 43.8% (average).
  * Instructor-XL: R@20 = 56.3% (inline), 57.1% (author), 56.5% (average).
  * E5-large-v2: R@20 = 55.8% (inline), 54.3% (author), 55.4% (average).
  * GritLM-7B: R@20 = 69.7% (inline), 74.3% (author), 70.8% (average).
  * GPT-4o reranking (w/ GritLM): R@20 = 74.7% (inline), 77.1% (author), 75.3% (average).
  * GPT-4o one-hop (w/ GritLM): R@20 = 72.9% (inline), 74.3% (author), 73.2% (average).
* **Specific Questions ($N = 442$ total: 231 inline, 211 author):**
  * BM25: Inline R@5 = 38.5%, R@20 = 55.8%; Author R@5 = 62.6%, R@20 = 73.5%; Average R@5 = 50.0%.
  * GTR-T5-large: Inline R@5 = 38.5%, R@20 = 51.5%; Author R@5 = 40.8%, R@20 = 55.9%; Average R@5 = 39.6%.
  * Instructor-XL: Inline R@5 = 48.9%, R@20 = 60.0%; Author R@5 = 55.9%, R@20 = 70.1%; Average R@5 = 52.3%.
  * E5-large-v2: Inline R@5 = 50.4%, R@20 = 63.9%; Author R@5 = 62.6%, R@20 = 75.8%; Average R@5 = 56.2%.
  * GritLM-7B: Inline R@5 = 67.7%, R@20 = 77.9%; Author R@5 = 82.5%, R@20 = 89.1%; Average R@5 = 74.8%.
  * GPT-4o reranking (w/ GritLM): Inline R@5 = 73.2%, R@20 = 79.9%; Author R@5 = 85.8%, R@20 = 92.4%; Average R@5 = 79.2%.
  * GPT-4o one-hop (w/ GritLM): Inline R@5 = 70.3%, R@20 = 78.4%; Author R@5 = 84.4%, R@20 = 87.2%; Average R@5 = 77.0%.

#### B. Full-Text vs. Abstract-Only Retrieval [p. 6, Table 5]
* Incorporating full text (up to model context boundaries) reduced GritLM-7B specific R@5 from 67.7% to 63.4% on inline questions, and from 82.5% to 73.0% on author questions [p. 6, Table 5].
* BM25 inline R@5 dropped from 38.5% (abstract) to 23.8% (full text), but increased from 62.6% to 71.6% on author specific questions [p. 6, Table 5].

#### C. Cross-Benchmark Comparison (nDCG@10) [p. 8, Table 8]
* **LitSearch (Specific):** GritLM-7B = 60.3; E5-large-v2 = 45.3; Instructor-XL = 41.2; GTR-T5-large = 30.4 [p. 8, Table 8].
* **LitSearch (Broad):** GritLM-7B = 44.1; Instructor-XL = 32.8; E5-large-v2 = 27.1; GTR-T5-large = 23.3 [p. 8, Table 8].

#### D. Commercial Search Engine Evaluation [p. 7, §4.3, Table 7]
* Tested on a manual sample of 80 specific questions ($n = 40$ inline-citation, $n = 40$ author-written) [p. 7, §4.3].
* Top-5 academic results evaluated per engine:

The following table presents Recall@5 for commercial web search tools and baseline retrievers on a subset of 80 specific questions:
[REGION: page=7, bbox=111,514,284,881]

* **Results (Recall@5):**
  * **Google Search:** Inline (specific) = 23.1%; Author (specific) = 62.5% [p. 7, Table 7].
  * **Google Scholar:** Inline (specific) = 20.5%; Author (specific) = 17.5% [p. 7, Table 7].
  * **Elicit:** Inline (specific) = 23.1%; Author (specific) = 17.5% [p. 7, Table 7].
  * Comparative baselines reported in Table 7: BM25 = 38.5% (inline), 62.6% (author); GritLM-7B = 67.7% (inline), 82.5% (author) [p. 7, Table 7].

---

### 4. Author Interpretations vs. Measured Facts

* **Measured Facts:**
  * Commercial engines achieved at most 23.1% R@5 on sampled inline-citation queries and between 17.5% and 62.5% on author-written queries [p. 7, Table 7].
  * Instruction-finetuned models scored higher recall than BM25 across overall tests [p. 5, Table 3].
  * Adding full document text did not yield consistent improvements across models and dropped performance in several configurations [p. 6, Table 5].
* **Author Interpretations:**
  * The authors hypothesize that embedding models degrade on full texts because training distributions (e.g., MS-MARCO, Natural Questions) consist of short passages (56–79 words) compared to full research papers (averaging 6,041 words) [p. 6–7, §4.1].
  * The authors attribute author-written questions being easier than inline questions to annotator bias, where authors reuse terminology from their abstracts [p. 6, §3.3].

---

### 5. Contradictions and Reporting Anomalies Identified

1. **Table 7 Sample Denominators vs. Baseline Numbers:**
   * Section 4.3 states that commercial search tools were tested on a sample of 80 specific questions (40 inline-citation, 40 author-written) [p. 7, §4.3].
   * In Table 7, the reported R@5 values for BM25 (38.5% inline, 62.6% author) and GritLM-7B (67.7% inline, 82.5% author) are numerically identical down to the first decimal place to the scores reported in Table 3 [p. 5, Table 3; p. 7, Table 7], which were evaluated on the full specific dataset ($N = 231$ inline, $N = 211$ author).
   * For author-written specific questions, every question has exactly 1.00 target paper on average [p. 4, Table 2]. A sample size of 40 binary outcomes must yield percentages in integer multiples of 2.5% ($1/40 = 0.025$). While Google Search (62.5% = 25/40), Google Scholar (17.5% = 7/40), and Elicit (17.5% = 7/40) conform to this denominator, BM25 (62.6%) and GritLM-7B (82.5%) match the full test set fraction ($132/211 \approx 62.559\%$ and $174/211 \approx 82.464\%$). This indicates that Table 7 places full-set baseline scores alongside 40-question sample scores without explicitly indicating the change in denominator.
2. **Apples-to-Apples Caveat:**
   * The paper explicitly notes that commercial engines search the open web and wider indices rather than the fixed 64,183-paper corpus, making direct metric comparisons non-equivalent [p. 7, §4.3].

---

### 6. Documented Limitations [p. 9, Limitations]

* English-language focus only [p. 9, Limitations].
* Incomplete coverage of reranking pipelines and dense models [p. 9, Limitations].
* Presence of residual questions that are either out-of-distribution or easy due to term overlap with paper abstracts [p. 9, Limitations].
* Sampling bias in inline citations toward frequently cited target literature [p. 9, Ethics Statement].

---

[Sch20c]:
### Bibliographic Metadata
- **Title:** Use of Artificial Intelligence for Medical Literature Search: Randomized Controlled Trial Using the Hackathon Format [p. 1]
- **Authors:** Dominik Schoeb, MD; Rodrigo Suarez-Ibarrola, MD; Simon Hein, MD; Franz Friedrich Dressler, MD; Fabian Adams, MD; Daniel Schlager, MD; Arkadiusz Miernik, MD, PhD [p. 1]
- **Affiliation:** Medical Center – Department of Urology, Faculty of Medicine, University of Freiburg, Freiburg, Germany [p. 1]
- **Venue:** *Interactive Journal of Medical Research* (*Interact J Med Res*), Volume 9, Issue 1, Article e16606 [p. 1, 6]
- **Publication History / Status:** Submitted October 8, 2019; accepted December 15, 2019; published March 30, 2020 (peer-reviewed journal article) [p. 6]
- **DOI:** 10.2196/16606 [p. 1, 6]
- **Conflicts of Interest:** None declared [p. 4]
- **Funding:** Sponsorship grant from Stryker Leibinger GmbH & Co. KG, Freiburg, Germany [p. 4]
- **Trial Registration Status:** Unregistered in public registries; ICMJE exception granted as recruiting was internal only [p. 4]

---

### Study Design & Methodology
- **Study Type:** Randomized controlled trial utilizing a 1-day "science hackathon" structure [p. 1, 2]
- **Duration:** 5 hours total search time split into two research sessions [p. 2]
- **Participants & Allocation:**
  - 17 scientists recruited with expertise in medical education, surgery, IT, or engineering [p. 2].
  - One participant cancelled on the event day, resulting in groups with 6, 6, and 5 members [p. 2].
  - Participants were stratified by domain (medical vs. engineering/IT) and randomly allocated into three teams: two intervention groups and one control group [p. 2].
- **Evaluated Tool:** IRIS.AI (commercial AI search tool; URL: `https://the.iris.ai/`; specific software version not reported) [p. 1, 2]
- **Comparator Tools (Control Group):** Conventional search engines: Google Scholar, Web of Science, and PubMed [p. 2]
- **Search Task / Problem Statement:** Participants investigated adaptive augmented reality (AR) for intraoperative guidance and resident training, split into three subtopics: (1) anatomical/instrument recognition, (2) system hardware, and (3) step-by-step pedagogical concepts [p. 3].
- **Reference Standard / Evaluation Procedure:** No pre-existing gold-standard test collection or benchmark database was used. Search outputs were evaluated post hoc by an expert panel of three judges (a urological surgeon, an AR software engineer, and a medical technology R&D engineer) using a standardized scoring rubric evaluating scientific quality and quantity [p. 3].

---

### Empirical Findings & Metrics
*(All metrics are based on panel evaluation out of a maximum possible score of 60 points)* [p. 1, 3]

| Metric / Outcome | AI Group 1 | AI Group 2 | Control Group | Locator |
| :--- | :--- | :--- | :--- | :--- |
| **Total Score** (max 60) | 49 / 60 | 39 / 60 | 46 / 60 | p. 1, 3 |
| **Quality Subscore** | 27 | 19 | 25 | p. 3 |
| **Total Papers Submitted** | 13 | 15 | 46 | p. 3 |
| **Papers Judged Relevant to Field** | 13 / 13 (100%) | 8 / 15 (53.3%) | 10 / 46 (21.7%) | p. 3 |
| **Unique Relevant Studies Contributed** | 7 / 20 (35.0%) | 7 / 20 (35.0%) | 6 / 20 (30.0%) | p. 3 |
| **Highly Relevant ("Spot On") Studies** | 5 | 5 | 5 | p. 1, 3 |

- **Graphic Content:**
  A user-interface screenshot illustrating the concept map visualization produced by IRIS.AI:
  Visual display of clustered thematic subcategories generated from seed articles.
  [REGION: page=2, bbox=634,70,915,910]

---

### Measured Findings vs. Authors' Interpretation
- **Measured Findings:**
  - Control retrieved far more total citations (46) than AI Group 1 (13) and AI Group 2 (15) [p. 3].
  - Precision among retrieved papers was higher in the AI groups (100% and 53.3%) compared to the control group (21.7%) [p. 3].
  - All three groups yielded an identical count of 5 highly relevant studies [p. 1, 3].
- **Authors' Interpretation:**
  - The authors conclude that AI yields a more focused literature search without improving overall retrieval volume or search quality compared to standard databases [p. 1, 4].

---

### Limitations & Internal Contradictions
- **Internal Inconsistencies:**
  - *Participant arithmetic:* The text states 17 scientists took part, but also states one cancelled on the event day, yet reports group sizes of 6, 6, and 5 (which sums to 17) [p. 2].
  - *Relevant studies accounting:* The text states AI group 1 found 13 relevant papers, AI group 2 found 8, and Control found 10. It subsequently states 20 total relevant studies were identified across the event with AI groups contributing 7 each and Control contributing 6 (7 + 7 + 6 = 20), without explaining whether the 20 represents an unduplicated subset or a separate pool [p. 3].
- **Study Limitations Identified by Authors:**
  - Small sample size (three teams) [p. 4].
  - Potential subjective bias from the three-judge panel [p. 4].
  - Participants had prior familiarity with conventional search platforms but zero prior experience with IRIS.AI [p. 4].
  - Lack of full-text access in IRIS.AI for certain databases [p. 4].

---

[Leo26]:
### 1. Document Identification & Bibliographic Metadata
* **Exact Title:** Auditing GenAI Literature Search Workflows: A Replicable Protocol for Traceable, Accountable Retrieval in Student-Facing Inquiry [p. 1]
* **Authors:** Cristo Leon, Michelle Kudelka [p. 1]
* **DOI:** `10.3390/aieduc2020008` [pp. 1, 42]
* **OSF Registration DOI:** `10.17605/OSF.IO/U8NHT` [pp. 1, 32]
* **Venue / Dates / Status:** *AI in Education* (*AI Educ.*), Volume 2, Issue 8, published 25 March 2026 (Received: 30 January 2026; Revised: 13 March 2026; Accepted: 16 March 2026). Published peer-reviewed open-access article [p. 1].
* **Affiliations:**
  * Cristo Leon: Office of Research, Jordan Hu College of Science & Liberal Arts, New Jersey Institute of Technology, Newark, NJ, USA [p. 1].
  * Michelle Kudelka: Research, Engagement, and Access Department, Robert W. Van Houten Library, New Jersey Institute of Technology, Newark, NJ, USA [p. 1].
* **Conflicts of Interest:** Authors declare no conflicts of interest [p. 32].
* **Funding:** No external funding [pp. 1, 31].

---

### 2. Empirical Design, Systems, & Retrieval Postures
* **Empirical Methodology:** Autoethnographic search-stage audit using Constructivist Grounded Theory (CGT) constant comparison, evaluating tool output directly as empirical data [pp. 6–7, Section 2.1].
* **Audited Systems & Versions:**
  * Gemini (institutional tier via Google Workspace) [pp. 2, 8]
  * ChatGPT free tier (GPT-4o) [pp. 2, 8]
  * ChatGPT paid tier (GPT-5.2 with Extended Thinking) [pp. 2, 8]
  * Perplexity (Academic configuration) [pp. 2, 8]
  * *Note:* Web browsing was enabled for all conversational executions [p. 8, Section 2.3].
* **Retrieval Postures Evaluated:**
  1. *Natural-language retrieval:* Conversational execution of a fixed canonical prompt [pp. 4, 8, Section 2.4.1].
  2. *Boolean translation:* Execution of tool-generated Scopus syntax queries in Scopus, ordered by citation count ("Cited by (highest)") [pp. 8, 14, Section 2.4.2].
* **Capture Rules & Runs:** 2 runs per tool per posture (16 runs total), truncating output to top-$k$ ($k = 20$) [pp. 4, 8, Section 2.4].

---

### 3. Queries & Reference Baseline
* **Canonical Prompt (Input Specification):** Bounded topic anchor asking for 20 peer-reviewed sources regarding how AI tools impact literature review traceability, metadata integrity, and reproducibility relative to a librarian baseline, formatted in APA 7 with DOIs, along with Scopus Boolean syntax and rationales [p. 4, Box 1].
* **Librarian Comparator / Reference Standard:**
  * Derived by an LIS expert across Scopus, Web of Science, and Google Scholar using standard Boolean queries: `TITLE-ABS-KEY (("AI" OR "artificial intelligence" OR "LLM" OR "large language model") AND ("literature review" OR "systematic review" OR "literature survey"))` [pp. 15–16, 21, 33, Appendix A.1].
  * Yielded a benchmark set of 27 sources (Dataset S7), of which 26 had resolvable, verified DOIs ($|B| = 26$) [pp. 16, 21, 23, Section 3.6.2].

---

### 4. Corpus Filtering & Sample Flow
* **Raw Ingestion:** 220 total items across runs (100 natural-language and 120 Boolean items after removing non-result placeholders) [pp. 8, 13, Section 3.1.1].
* **Deduplication:** Initial Zotero automated/manual deduplication yielded 212 records, followed by CSV normalization removing variations in author strings and titles down to 170 unique records [pp. 9–10, Section 2.5].
* **Expert Addition & Staged Screening:** Addition of 27 LIS expert records produced 197 consolidated records. Title/abstract screening removed 97 records. Of 100 assessed at full text, 63 were excluded, leaving $n = 37$ included studies post-quality appraisal [pp. 7, 9, 12, Section 3.1, Figure 1].

---

### 5. Measured Findings & Exact Numerical Results

#### A. Yield and Completion [p. 13, Table 2; p. 23, Table 8]
* **Natural Language (NL):** 101 raw outputs generated; 1 non-result placeholder (Run 5 Perplexity); 100 captured items (or 92 unique items after Zotero deduplication, representing 57.5% of the 160 theoretical maximum) [pp. 13, 23].
  * Run 1 (Gemini): 18 | Run 2 (Gemini): 18
  * Run 3 (ChatGPT free): 8 | Run 4 (ChatGPT free): 5
  * Run 5 (Perplexity): 0 (N/A) | Run 6 (Perplexity): 7
  * Run 7 (ChatGPT paid): 19 | Run 8 (ChatGPT paid): 17
* **Boolean Translation via Scopus:** 129 raw outputs generated; 1 non-result placeholder (Run 4.1 ChatGPT free returned 0 hits); 128 retrievable items captured (80.0% of the 160 maximum) [pp. 13, 23].
  * Runs 1.1 & 2.1 (Gemini): 20 each
  * Run 3.1 (ChatGPT free): 20 | Run 4.1: 0 (N/A)
  * Run 5.1 (Perplexity): 15 | Run 6.1 (Perplexity): 13
  * Runs 7.1 & 8.1 (ChatGPT paid): 20 each

#### B. Traceability & Identifier Integrity
* **Natural-Language Mode [p. 15, Table 4; p. 22, Table 7]:**
  * Overall: 58/100 (58.0%) `DOI_Correct`, 19/100 (19.0%) `DOI_NON_RESOLVING`, 13/100 (13.0%) `DOI_WRONG_MATCH`, 10/100 (10.0%) `NO_DOI`.
  * Gemini: 9/40 (22.5%) `DOI_Correct`.
  * ChatGPT free tier: 9/13 (69.2%) `DOI_Correct`.
  * Perplexity Academic: 2/7 (28.6%) `DOI_Correct`.
  * ChatGPT paid tier: 38/40 (95.0%) `DOI_Correct`.
* **Boolean Mode [p. 15, Table 5]:**
  * Gemini: 32/40 (80.0%) `DOI_Correct`, 8 `NO_DOI`.
  * ChatGPT free tier: 20/21 (95.2%) `DOI_Correct`.
  * Perplexity Academic: 23/28 (82.1%) `DOI_Correct`, 5 `NO_DOI`.
  * ChatGPT paid tier: 40/40 (100.0%) `DOI_Correct`.

#### C. Overlap with Librarian Baseline ($|B| = 26$) [p. 24, Table 9]
* Overlap occurred in only 2 of 8 natural-language runs:
  * ChatGPT free tier Run 3: 1 shared DOI ($J = 0.0303$; Overlap Coeff = 0.125).
  * Perplexity Academic Run 6: 1 shared DOI ($J = 0.0313$; Overlap Coeff = 0.1429).
  * Gemini (Runs 1, 2) and ChatGPT paid tier (Runs 7, 8): 0 shared DOIs ($J = 0.0$; Overlap Coeff = 0.0).

#### D. Run-to-Run Drift / Reproducibility [p. 25, Tables 10 & 11]
* **Natural-Language Posture (Paired Runs) [Table 10]:**
  * Gemini (Run 1 vs. Run 2): Citation Jaccard = 0.000; DOI Jaccard = 0.057; DOI Overlap/min = 0.118 (2 shared DOIs).
  * ChatGPT free tier (Run 3 vs. Run 4): Citation Jaccard = 0.625; DOI Jaccard = 0.800; DOI Overlap/min = 1.000 (4 shared DOIs; short list artifact).
  * Perplexity Academic (Run 5 vs. Run 6): All overlaps = 0.000 (Run 5 yielded 0).
  * ChatGPT paid tier (Run 7 vs. Run 8): Citation Jaccard = 0.059; DOI Jaccard = 0.059; DOI Overlap/min = 0.125 (2 shared DOIs).
* **Boolean Posture (Paired Runs) [Table 11]:**
  * Gemini (Run 1.1 vs. 2.1): DOI Jaccard = 0.333; DOI Overlap/min = 0.533 (8 shared DOIs).
  * ChatGPT free tier (Run 3.1 vs. 4.1): DOI Jaccard = 0.000 (missing run).
  * Perplexity Academic (Run 5.1 vs. 6.1): DOI Jaccard = 0.278; DOI Overlap/min = 0.455 (5 shared DOIs).
  * ChatGPT paid tier (Run 7.1 vs. 8.1): DOI Jaccard = 0.111; DOI Overlap/min = 0.200 (4 shared DOIs).

---

### 6. Critical Distinctions: Measured Findings vs. Interpretations
* **Measured Findings:**
  * Boolean translation executed in Scopus significantly increased yield completion (80.0% vs. 57.5%) and DOI correctness rates (80.0%–100.0% vs. 22.5%–95.0%) across all tools [pp. 15, 23].
  * High single-run correctness did not prevent set-level drift across identical prompts (e.g., ChatGPT paid tier had 95%–100% DOI correctness but only Jaccard 0.059–0.111 run-to-run overlap) [pp. 22, 25].
  * Direct overlap between conversational AI outputs and librarian-curated baselines was near zero [p. 24].
* **Authors' Interpretations & Governance Recommendations:**
  * Natural language prompting should be restricted to exploratory concept mapping rather than evidence set gathering [p. 30, Section 5].
  * Boolean translation should serve as the required classroom retrieval posture [pp. 27, 30].
  * Metadata errors (e.g., compound name parsing) pose equity and attribution harms in academic evaluation [p. 28, Section 4.4].

---

### 7. Internal Inconsistencies & Contradictions Within the Paper
1. **Item Counts in ChatGPT Paid Runs:** Table 2 logs Run 7 as 19 items and Run 8 as 17 items [p. 13]. Table 7 lists Run 7 with 22 `DOI_Correct`, 1 `DOI_NON_RESOLVING`, and 1 `DOI_WRONG_MATCH` (sum = 24 items), and Run 8 with 16 items [p. 22]. Table 9 lists Run 7 with 19 items and Run 8 with 17 items [p. 24]. Table 10 lists Run 7 $n_A = 20$ and Run 8 $n_B = 16$ [p. 25].
2. **Boolean Item Yield for ChatGPT Free:** Table 2 logs Run 3.1 with 20 items and Run 4.1 with 0 items (sum = 20) [p. 13]. Table 5 reports ChatGPT free retrieved $n = 21$ items with 20 `DOI_Correct` [p. 15].
3. **Pre-consolidation Corpus Tallies:** Section 2.4.2 reports the pre-consolidation corpus as 220 items broken down as "92 natural-language + 128 Boolean" [p. 8]. Section 3.1.1 reports the exact same 220 items as "100 natural-language + 120 Boolean" [p. 13].
4. **Abstract Typographical Reduplication:** Page 1 states: *"the final set included 37 studies after quality appraisal was 37 studies"* [p. 1].

---

### 8. Limitations [pp. 29–30, Section 4.8]
* Reliance on a single canonical prompt and an arbitrary top-20 ($k = 20$) cutoff.
* Audit is confined to the initial retrieval/search stage; it does not measure downstream screening, data extraction, or synthesis quality.
* The librarian baseline is bounded by individual professional judgment, query formulation, and institutional database subscriptions (Scopus/Web of Science).
* Opaque backend browsing behavior and dynamic ranking volatility across tools limit exact reproducibility.

---

[Agg26]:
### Bibliographic Metadata
* **Exact Title:** Evaluation of output of AI models ScholarAI and SciSpace: Implications for use of generative artificial intelligence models as research assistants [Page 1]
* **Authors:** Meenakshi Aggarwal, Sonia Singh Kharay, Priya Bansal, Seema Gupta, Hitant Vohra, Sarit Sharma, Charu Gupta [Page 1]
* **DOI:** `10.18231/j.jchm.17551.1781068642` [Page 1]
* **Venue:** *The Journal of Community Health Management* (abbreviated *J Community Health Manag.*), Volume 13, Issue 2, pages 51–56 [Page 1, 6]
* **Dates & Status:** Received: 22-05-2026; Accepted: 05-06-2026; Available Online: 17-06-2026; published year printed as 2026 [Page 1]
* **Affiliations:**
  * Dept. of Anatomy, Dayanand Medical College & Hospital, Ludhiana, Punjab, India (Aggarwal, Kharay, S. Gupta, Vohra, C. Gupta) [Page 1]
  * Dept. of Community Medicine, Dayanand Medical College & Hospital, Ludhiana, Punjab, India (Bansal, Sharma) [Page 1]
* **Funding:** None [Page 6, Section 7]
* **Conflicts of Interest:** None [Page 6, Section 8]

---

### Empirical Design and Implementation

* **Empirical Design:** Multi-session experimental comparative evaluation across four temporal checkpoints (sessions) auditing two custom GPT assistants on results interpretation and literature search tasks [Page 2, Section 2.1, 2.2.2].
* **Tools and Versions:**
  * Custom GPTs integrated into "ChatGPT 5" platform accessed via free user login [Page 2, Section 2.2.1]:
    * *ScholarAI* (`scholarai.io`), rank 4 under Research & Analysis [Page 2, Section 2.2.1; Page 6, Ref 6: `https://ChatGPT.com/g/g-L2HknCZTC-scholar-ai`]
    * *SciSpace* (`scispace.com`), rank 9 under Research & Analysis [Page 2, Section 2.2.1; Page 6, Ref 7: `https://ChatGPT.com/g/g-NgAcklHd8-scispace`]
* **Access Dates / Checkpoints:** September 5, November 13, November 14, and November 15, 2025 (one session per day per model; 4 sessions total per model) [Page 2, Section 2.2.2, Table 1].
* **Input / Queries:**
  * A single Microsoft Word document (`MS1`) containing research objectives along with quantitative and analytical results (tables and figures) [Page 2, Section 2.5].
  * Submitted with an initial prompt instructing the model to interpret results and conduct a literature search. Only the first prompt response was scored; follow-ups were excluded [Page 2, Section 2.7, 2.8].
* **Sample Size:** 10 citations requested/generated per session per tool across 4 sessions (target $N = 40$ citation outputs per model) [Page 3, Section 3, Table 2].
* **Comparator / Reference Standard:** Manual verification of DOIs and citation metadata via search engine resolution and cross-checking against source journals/indexing; evaluation scored by three independent human reviewers trained on CLEAR tool rubrics with consensus resolution [Page 2, Section 2.6; Page 3, Section 2.8]. (No automated benchmark baseline; descriptive empirical comparison).

---

### Measured Findings vs. Qualitative Interpretations

#### Measured Citation & Retrieval Metrics (Per 10 References per Session)

Table 2 breaks down the performance of the 10 requested citations per session for both tools:

Table 2 summarizes the distribution of invalid DOIs, hallucinated references, and valid peer-reviewed articles generated across four temporal sessions by ScholarAI and SciSpace:
[REGION: page=3, bbox=678,60,920,938]

* **ScholarAI:**
  * *Session 1 (Sept 5):* 1/10 invalid DOIs; 1/10 hallucinations; 8/10 valid, relevant, peer-reviewed, correctly cited [Page 3, Table 2].
  * *Session 2 (Nov 13):* 4/10 invalid DOIs; 3/10 hallucinations; 5/10 valid, peer-reviewed [Page 3, Table 2].
  * *Session 3 (Nov 14):* 5/10 invalid DOIs; 3/10 hallucinations; 5/10 valid, peer-reviewed [Page 3, Table 2].
  * *Session 4 (Nov 15):* 10/10 unpopulated placeholder templates and DOIs (0/10 valid) [Page 3, Table 2 footnote ‡].
* **SciSpace:**
  * *Session 1 (Sept 5):* 6/10 invalid DOIs; 2/10 hallucinations; 2/10 valid, peer-reviewed [Page 3, Table 2].
  * *Session 2 (Nov 13):* 8/10 invalid DOIs; 8/10 hallucinations; 2/10 valid, peer-reviewed [Page 3, Table 2].
  * *Session 3 (Nov 14):* Failed domain-specific retrieval; returned 10 general statistical articles with 2 incorrect DOIs/citations [Page 3, Table 2 footnote *].
  * *Session 4 (Nov 15):* 1 relevant non-peer-reviewed article and 9 generic statistical/psychometric citations [Page 3, Table 2 footnote †].
* **Specific Session 1 Error Categorization:**
  * *Invalid DOIs (Search matched no documents):* 3 in SciSpace (Nori et al. 2023; Schmidt et al. 2011; Zeshan et al. 2022); 1 in ScholarAI (Nisar et al. 2023) [Page 4, Table 3].
  * *Mismatched DOIs (Linked to completely different papers):* 3 in SciSpace (Masters 2019 linked to Barnes et al. 2020; Wang et al. 2023 linked to Zhang et al. 2023; Chan & Zary 2019 linked to Colonnello et al. 2019); 1 in ScholarAI (Yurdugül 2008 linked to a 1987 Turkish article) [Page 4, Table 3].
  * *Fabricated / Non-existing articles:* 1 for ScholarAI (Nisar et al.); 2 for SciSpace (Wang et al.; Zeshan et al.) [Page 5, Table 4].

#### Results Interpretation Findings
* Both models misidentified Cronbach's alpha "if item deleted" in 3 out of 4 sessions, confusing item removal impacts with base scale reliability [Page 1, Abstract; Page 3, Section 3; Page 5, Section 4].

---

### Internal Contradictions and Reporting Anomalies

1. **Future Dating:** The article lists publication, receipt, and acceptance dates in 2026 (Received: 22-05-2026; Accepted: 05-06-2026) while reporting evaluation sessions run in September and November 2025 [Page 1, 2].
2. **Platform Version Label:** The text repeatedly refers to testing custom GPTs integrated into "ChatGPT 5" in late 2025 [Page 2, Section 2.2.1, 2.2.2].
3. **ScholarAI Session 3 Arithmetic:** Table 2 lists 5 invalid DOIs, 3 hallucinations, and 5 valid articles out of a denominator of 10 articles (summing to more than 10 if categories are treated as mutually exclusive) [Page 3, Table 2].

---

### Study Limitations

As stated by the authors [Page 6, Section 5]:
1. Researcher inexperience with GPT assistants.
2. Subjective evaluation scoring.
3. Lack of reproducibility due to algorithmic opacity.
4. Rapid temporal evolution of underlying model checkpoints.
5. Domain-specific and context-dependent limits restricting generalizability.

---

### Reference
* Aggarwal M, Kharay SS, Bansal P, Gupta S, Vohra H, Sharma S, Gupta C. Evaluation of output of AI models ScholarAI and SciSpace: Implications for use of generative artificial intelligence models as research assistants. *J Community Health Manag.* 2026;13(2):51–56. `doi:10.18231/j.jchm.17551.1781068642`

---

[Sch26b]:
### Bibliographic Metadata & Verification
* **Exact Title:** AI Overviews in Academic Search: Evaluating AI-generated Summaries of Search Results in a Domain-specific Search Engine [p. 1]
* **Authors:** Kevin Schott, Kanishka Silva, Ingo Frommholz, Philipp Mayr, Dagmar Kern, Daniel Hienert [p. 1]
* **Institutional Affiliations:**
  * GESIS – Leibniz Institute for the Social Sciences, Cologne/Mannheim, Germany (Kevin Schott, Kanishka Silva, Philipp Mayr, Dagmar Kern, Daniel Hienert) [p. 1]
  * Modul University Vienna, Austria (Ingo Frommholz) [p. 1]
* **Venue, Date & Publication Status:**
  * Printed Header: *89th Annual Meeting of the Association for Information Science & Technology | Nov. 6 – 10, 2026 | Bangkok, Thailand* [p. 1]
  * Category: *ASIS&T Annual Meeting 2026 Long Papers* [p. 1]
  * Status: Conference proceedings paper.
* **DOI:** None printed for the document itself. The acknowledgments section cites an EU grant DOI (10.3030/101086321) [p. 11].
* **Funding & Disclosures:**
  * Funded by the German Research Foundation (DFG project *VACOS 2*, grant no. 388815326) and the European Union *OMINO* project [p. 11].
  * Generative AI disclosure: Authors report using ChatGPT, Claude, and Gemini for text refinement, table formatting, and data analysis scripting [p. 11].
  * Conflicts of Interest: None declared [p. 11].
* **Temporal Anomalies / Discrepancies:** The conference header cites November 2026 and an external link access date is listed as April 2, 2026 [p. 1, 2], while study execution is dated September 1–22, 2025 [p. 5].

---

### Empirical Design & Evaluation Framework
* **Overall Design:** A two-part formative mixed-methods design study [p. 1, 4]:
  1. *Manual accuracy evaluation (RQ1):* Qualitative and metadata-grounded verification comparing two general-purpose LLMs across 10 sample queries [p. 4–5].
  2. *Controlled laboratory user experiment (RQ2):* Within-subjects user study ($N = 30$) comparing search without versus with AI-generated summaries across counterbalanced familiar and predefined tasks [p. 5–7].
* **Search Corpus & Engine:** A specialized academic search engine for social science information indexing approximately 7,500 research datasets (1945–2025) and approximately 250,000 scholarly publications, featuring keyword retrieval, faceted filtering, bookmarking, and on-SERP abstract snippets [p. 4].

The interface condition embedding the multi-document summary above the retrieved records is illustrated below:

The screenshot displays the experimental AISummary interface for the query "democratic principles", featuring a search bar, facet filters, an expandable multi-document overview citing sources with numbered indices (#1, #2), followed by standard academic search result listings.
[REGION: page=4, bbox=238,258,410,742]

---

### RQ1: Summary Quality Evaluation (Models, Errors, Safeguards)
* **Evaluated LLMs:**
  * OpenAI GPT-4o mini (commercial closed model, accessed September 2025 via API) [p. 4, 5].
  * Meta Llama 4 Scout (locally hosted open-weights model; 67 GB, 109B parameters, Q4_K_M quantization) [p. 4, 5].
* **Generation Protocol:** Zero-shot system prompt directing the model to act as a research assistant and output a single paragraph (maximum 5 sentences) synthesizing the top 5 SERP records using only their titles, abstracts, and keywords/topics, citing items via numeric indices (#1–#5) without external deductions [p. 4]. Prompt and rating rubric are archived on OSF (`https://osf.io/gjhky/`).
* **Test Queries ($N = 10$):** Sourced from empirical social science queries: *psychosocial stress*, *social background*, *work equipment employees*, *dimensions of social identity*, *marriage transfers*, *politically motivated crime*, *educational attainment refugees*, *democratic principles*, *discrimination muslims*, and *sampling mobile phone survey* [p. 4].
* **Reference Standard:** Grounded strictly against the metadata of the top 5 retrieved items on the SERP, evaluated independently by three researchers with consensus-based adjudication [p. 4–5].
* **Accuracy Breakdown ($N = 10$ summaries per model):**
  * *GPT-4o mini:* 5 Correct (50%), 4 Partially Correct (40%), 1 Incorrect (10%) [p. 5].
  * *Llama 4 Scout:* 2 Correct (20%), 8 Partially Correct (80%), 0 Incorrect (0%) [p. 5].
* **Identified Error Taxonomy (Qualitative Counts):**
  * *Inaccurate or Unsupported Content Descriptions:* Found in GPT-4o mini ($n = 3$) and Llama 4 Scout ($n = 3$) [p. 5].
  * *Unsubstantiated Guesses / Speculations:* Found only in GPT-4o mini ($n = 3$) [p. 5].
  * *Omission of Search Results:* Found only in GPT-4o mini ($n = 2$) [p. 5].
  * *Incorrect Study Identifiers:* Found only in Llama 4 Scout ($n = 4$) [p. 5].
  * *Formatting and Language Artifacts:* Found only in Llama 4 Scout ($n = 2$) [p. 5].
  * *Inappropriate Result Grouping:* Found only in Llama 4 Scout ($n = 2$) [p. 5].
* **Proposed Deployment Safeguards:** (1) Pre-rendering coverage verification to catch omitted items; (2) deterministic pattern matching/database checks for study identifiers; (3) templated few-shot prompting; (4) stricter constraints against external extrapolation; and (5) a secondary lightweight verifier model to validate citations prior to rendering [p. 10].

---

### RQ2: Controlled User Experiment
* **Participants:** $N = 30$ (20 female, 10 male; age range 19–53 years, $M = 29.00$, $SD = 7.24$) [p. 7].
  * Sourcing: 29 via Prolific, 1 via LinkedIn [p. 7].
  * Composition: 10 professional social scientists, 20 social science students [p. 7].
  * Search Engine Experience: High self-reported familiarity with academic search tools ($M = 6.00 / 7.00$, $SD = 1.02$); only 1 had used this specific system before [p. 7].
  * Compensation: £8.70 per person (average duration 42 min 57 s; equivalent to ~£12.14/hour) [p. 7].
* **Task Protocol:** Within-subjects design with counterbalanced order. Each participant performed two 10-minute time-boxed triage searches:
  1. *Familiar Topic:* User's own area of expertise [p. 5].
  2. *Predefined Topic:* Randomly assigned from three balanced options: (i) European attitudes toward democracy, (ii) immigrant discrimination experiences in the EU, or (iii) social stressors in European nations [p. 5–6].
* **Interface Conditions:**
  * *NoSummary (Baseline):* Standard SERP displaying ranked records and snippet previews [p. 5].
  * *AISummary (Experimental):* Standard SERP prepended with an expandable 4-line collapsed panel summarizing the top 5 records generated on the fly via GPT-4o mini [p. 5].

---

### Measured Findings vs. Interpretations

Table 1 presents the full statistical results across all confirmatory and exploratory self-reported measures:

Table 1 displays means, standard deviations, medians, test statistics (paired t or Wilcoxon signed-rank), raw and Holm–Bonferroni adjusted p-values, effect sizes (Cohen's d or Rosenthal's r), and 95% confidence intervals comparing NoSummary and AISummary conditions across subjective workload (NASA-TLX total and subscales), perceived usefulness, satisfaction, and decision confidence.
[REGION: page=8, bbox=68,116,316,880]

#### 1. Confirmatory Self-Reported Metrics ($N = 30$, family-wise error controlled via Holm–Bonferroni)
* **Subjective Workload (Raw NASA–TLX composite, 0–100):**
  * *NoSummary:* $M = 28.94$ ($SD = 20.75$), Median = 24.17
  * *AISummary:* $M = 23.69$ ($SD = 14.48$), Median = 21.67
  * *Statistic:* Paired $t(29) = -1.598$, $p = .121$, $p_{\text{adj}} = .484$, Cohen's $d = -0.292$, 95% CI $[-11.97, 1.47]$ (H1 not supported) [p. 8].
* **Perceived System Usefulness (Davis 6-item scale, 1–7):**
  * *NoSummary:* $M = 5.11$ ($SD = 1.51$), Median = 5.25
  * *AISummary:* $M = 5.39$ ($SD = 1.16$), Median = 5.58
  * *Statistic:* Wilcoxon $W = 113.5$, $p = .465$, $p_{\text{adj}} = .787$, Rosenthal's $r = +0.152$, 95% CI $[-0.17, 0.17]$ (H2 not supported) [p. 8].
* **Search Satisfaction (Single item, 1–7):**
  * *NoSummary:* $M = 4.90$ ($SD = 1.75$), Median = 5.00
  * *AISummary:* $M = 5.37$ ($SD = 1.52$), Median = 6.00
  * *Statistic:* Paired $t(29) = 1.455$, $p = .156$, $p_{\text{adj}} = .484$, Cohen's $d = +0.266$, 95% CI $[-0.19, 1.12]$ (H3 not supported) [p. 8].
* **Decision-Making Confidence (Single item, 1–7):**
  * *NoSummary:* $M = 5.13$ ($SD = 1.55$), Median = 5.00
  * *AISummary:* $M = 5.43$ ($SD = 1.61$), Median = 6.00
  * *Statistic:* Paired $t(29) = 0.866$, $p = .393$, $p_{\text{adj}} = .787$, Cohen's $d = +0.158$, 95% CI $[-0.41, 1.01]$ (H4 not supported) [p. 8].

#### 2. Exploratory NASA–TLX Subscales ($N = 30$, unadjusted)
* **Mental Demand:** Significantly lower in AISummary ($M = 32.00, SD = 25.35$, Med = 30.00) than NoSummary ($M = 41.67, SD = 31.19$, Med = 42.50); $t(29) = -2.156$, $p = .040$, $d = -0.394$, 95% CI $[-18.84, -0.49]$ [p. 8].
* **Frustration:** Lower in AISummary ($M = 12.17, SD = 19.81$, Med = 2.50) than NoSummary ($M = 22.17, SD = 31.34$, Med = 5.00); Wilcoxon $W = 37.5$, $p = .068$, $r = -0.443$, 95% CI $[-5.00, 0.00]$ [p. 8].
* **Effort:** NoSummary $M = 39.83$, AISummary $M = 35.00$; $t(29) = -0.949$, $p = .351$, $d = -0.173$ [p. 8].
* **Performance Demand:** NoSummary $M = 42.33$, AISummary $M = 40.50$; $t(29) = -0.260$, $p = .796$, $d = -0.050$ [p. 8].
* **Temporal Demand:** NoSummary $M = 17.00$, AISummary $M = 13.50$; $W = 79.0$, $p = .531$, $r = -0.144$ [p. 8].
* **Physical Demand:** NoSummary $M = 10.67$, AISummary $M = 9.00$; $W = 44.0$, $p = .907$, $r = -0.030$ [p. 8].

#### 3. Summary Feature Evaluation & User Preferences
* **Summary Ratings (7-point Likert, AISummary condition):**
  * Appropriateness of size/length: $M = 5.67$ ($SD = 1.56, n = 28/30$) [p. 8].
  * Understandability: $M = 5.43$ ($SD = 1.47, n = 27/30$) [p. 8].
  * Perceived usefulness: $M = 5.20$ ($SD = 1.56, n = 27/30$) [p. 8].
  * Relevance assessability: $M = 5.17$ ($SD = 1.53, n = 26/30$) [p. 8].
  * Perceived reliability: $M = 4.77$ ($SD = 1.55, n = 25/30$) [p. 8].
* **Stated Interface Preference:** 15/30 (50%) favored AISummary; 8/30 (26.7%) favored NoSummary; 7/30 (23.3%) had no preference [p. 8].

#### 4. Behavioral Log Findings
Table 2 details the behavioral counts logged across conditions and topic types:

Table 2 breaks down behavioral logging metrics (mean and standard deviation) for result clicks, panel expansions, bookmarks saved, and query reformulations across overall, familiar, and predefined topics for both NoSummary and AISummary conditions.
[REGION: page=8, bbox=640,230,830,770]

* **Result Clicks:** NoSummary overall $M = 4.67$ ($SD = 3.70$); AISummary overall $M = 3.83$ ($SD = 3.84$). No significant differences overall or across topic strata ($p > .05$) [p. 8].
* **Summary Expansions:** Rarely triggered in AISummary ($M = 0.97, SD = 1.59$ per task; familiar $M = 1.14$, predefined $M = 0.81$) [p. 8].
* **Bookmarks Added:** NoSummary overall $M = 5.87$ ($SD = 5.20$); AISummary overall $M = 5.00$ ($SD = 3.93$). Differences not statistically significant ($p > .05$) [p. 8].
* **Query Reformulations:** NoSummary overall $M = 4.73$ ($SD = 4.13$); AISummary overall $M = 4.27$ ($SD = 3.50$). Condition difference not significant ($p > .05$). Reformulations were significantly higher for familiar topics than unfamiliar topics across both conditions (paired $t$-test $p = 0.011$) [p. 8–9].

#### 5. Qualitative Feedback Patterns
* *Supporters ($n = 15$):* Emphasized speed, lower search friction ($n = 8$), receiving an orientation starting point ($n = 8$), validating search terms ($n = 5$), and assessing relevance ($n = 4$) [p. 9].
* *Skeptics ($n = 8$):* Cited distrust/accuracy concerns and verification overhead ($n = 5$), visual distractions ($n = 3$), habit persistence, or perceived lack of necessity ($n = 1$) [p. 9].
* *Improvement Requests ($n = 28$ suggestions):* Structural presentation over prose paragraphs (e.g., bulleted lists, tables; $n = 8$), inclusion of structured methodological/demographic metadata ($n = 6$), hover source previews ($n = 3$), system confidence indicators ($n = 2$), and conversational drill-down capabilities [p. 9–10].

#### 6. Authors' Theoretical Interpretations (Distinguished from Raw Data)
* The authors hypothesize under Information Foraging Theory that the summary functions as a scent concentrator [p. 2, 10], aggregating dispersed cues from multiple results to reduce initial patch-entry costs without suppressing source inspection.
* Because users rarely expanded the summary beyond four lines, the authors infer that the collapsed preview provided sufficient high-level scent for initial relevance triage [p. 8, 10].
* The authors conclude that AI summaries provide context- and user-dependent utility rather than universal performance gains [p. 1, 10].

---

### Benchmarks & Commercial Comparison Tools
* **Search Benchmark / Ground Truth:** None. The paper does not evaluate TREC-style ad-hoc retrieval effectiveness (MAP, NDCG, P@k) or expert relevance labels; results are descriptive behavioral and subjective measures [p. 10].
* **Scopus AI:** Mentioned in related work as an example of commercial academic multi-document synthesis with linked citations, relying on retrieval-augmented generation [p. 2]. The paper does not benchmark Scopus AI experimentally.
* **Semantic Scholar / Scholar Labs / LitSearch:** Semantic Scholar, Google Scholar Labs, and LitSearch are not evaluated, tabulated, or tested in this paper.

---

### Study Limitations
1. *Small Query Sample for Quality Audit:* Only 10 queries were tested manually, making the error taxonomy exploratory [p. 10].
2. *Underpowered Sample Size:* $N = 30$ provided limited statistical power to detect small effect sizes, leaving confirmatory differences non-significant [p. 10].
3. *Recruitment & Task Constraints:* Participants were recruited primarily via Prolific and tested in brief, time-constrained 10-minute sessions [p. 10].
4. *Unmodeled Variables:* Prior personal GenAI usage habits, user background variations, and nuanced topic familiarity were not modeled [p. 10].
5. *Fixed Result Coverage:* Summaries were strictly fixed to the top 5 ranked records, leaving adaptive coverage or cutoffs unexplored [p. 10].
6. *Absence of Objective Relevance Ground Truth:* Lack of expert relevance annotations prevented direct evaluation of retrieval effectiveness [p. 10].
7. *Domain Generalizability:* Conducted solely within social science data and literature repositories [p. 10].

---

[Dev24]:
Here is the extracted evidence from the provided document:

### 1. Bibliographic Metadata
* **Exact Title**: "Enhancing Literature Review through AI-based Research Tools: A Comparative Study of SciSpace and Semantic Scholar" [p. 1, Title]
* **Complete Authors**: Amrita Devi, Dr PK Barooah, Dr Zabeen Ahmed [p. 1]
* **DOI**: Not printed in the paper. (The paper lists identifier code `TIJER2407101` and ISSN `2349-9249`).
* **Venue / Date / Status**: Published in *TIJER – International Research Journal* (*TIJER || ISSN 2349-9249*), July 2024, Volume 11, Issue 7, pp. a779–a785 [pp. 1–7 headers/footers].
* **Affiliations**: Department of Library and Information Science, University of Science and Technology Meghalaya (for all three authors) [p. 1].
* **Conflicts of Interest**: None declared/printed in the paper.

---

### 2. Empirical Design, Tools, Queries, and Benchmarks
* **Actual Empirical Design**: Qualitative descriptive feature comparison; no controlled experiment or formal evaluation protocol was conducted [pp. 2–7, Sections IV, V, VI].
* **Tools & Versions Evaluated**:
  * **SciSpace** (Business Integra, Bengaluru, Karnataka, India; URL: `https://typeset.io/`) [p. 2, Table 1]. Version/build number not specified.
  * **Semantic Scholar** (Allen Institute of Artificial Intelligence, USA; URL: `https://www.semanticscholar.org/`) [p. 2, Table 1]. Version/build number not specified.
* **Queries**: No search queries evaluated or tested. (Incidental screenshot search strings visible in figures include *"Libraries, Librarians, and the Discourse of Fear"* [p. 3, Fig. 1] and *"Utilizing artificial intelligence tools for improving writing skills: Exploring Omani EFL learners’ perspectives"* [p. 3, Fig. 2 / p. 4, Fig. 4]).
* **Sample**: No formal corpus, document sample, or query test set was evaluated.
* **Comparator / Reference Standard**: No reference standard or ground-truth benchmark was used.

---

### 3. Metrics, Measured Findings, and Retrieval/Reproducibility Data
* **Measured Quantitative Findings** [p. 3, Section VI.a, VI.b]:
  * **Document Count (as of May 10th, 2024)**:
    * SciSpace: **12,209,406 papers** [p. 3, Section VI.a].
    * Semantic Scholar: **218,279,236 papers** [p. 3, Section VI.a].
  * **Language Coverage**:
    * Semantic Scholar: English Language only [p. 3, Section VI.b].
    * SciSpace: **75 languages** [p. 3, Section VI.b].
* **Denominators / Formal Retrieval Metrics**:
  * No retrieval performance metrics (e.g., precision, recall, MAP, nDCG), citation matching metrics, or reproducibility tests are reported.
* **Feature Comparison Findings**:
  * *Alerts/Recommendations*: Semantic Scholar offers literature recommendations and automated email alerts; SciSpace customer support confirmed via chat that this feature was not available at the time [p. 5, Section VI.g, Figs. 5 & 6].
  * *Export Formats*: SciSpace exports tables/records in CSV, BIB, RIS, and XML [p. 2, Table 1] or CSV and XLS in paid tiers [p. 3, Section VI.c; p. 6, Section VI.i]. Semantic Scholar exports/downloads citations in BibTeX and EndNote, and copies BibTeX, MLA, APA, and Chicago formats [p. 6, Section VI.i, Fig. 10].
  * *Reference Manager Integration*: SciSpace integrates with Zotero; Semantic Scholar integrates with EndNote and Zotero [p. 7, Section VI.k].

---

### 4. Graphic Pointers

Basic subscription pricing, country of origin, and website URLs for SciSpace and Semantic Scholar:
[REGION: page=2, bbox=469,87,935,951]

Screenshots of the personal library interfaces of both tools showing organization features and folder options:
[REGION: page=3, bbox=224,77,738,934]

---

### 5. Contradictions, Limitations, and Author Interpretation
* **Contradictions Within the Paper**:
  * *SciSpace Website URL*: Table 1 lists the website as `https://typeset.io/` [p. 2], while the reference list cites `https://scispace.com/` [p. 7, Section VIII].
  * *Export Formats for SciSpace*: Table 1 states *"Export in CSV, BIB, RIS and XML"* [p. 2], whereas Section VI.c states *"exporting records in formats such as .csv and .xls"* [p. 3], and Figure 9 shows options for CSV, Excel, BibTeX, XML, and RIS [p. 6].
  * *Paper Counts*: Figure 4 shows an interface search counter on Semantic Scholar displaying *"218,8276,776 papers from all fields of science"* (with an apparent typo in digit grouping) [p. 4, Fig. 4], whereas Section VI.a reports *"218,279,236 papers indexed"* [p. 3].
* **Limitations**:
  * Purely observational and narrative review; lacks experimental methodology, standardized search tasks, recall/precision benchmarks, or statistical testing.
* **Measured Findings vs. Interpretation**:
  * *Measured*: Database counts on May 10, 2024, pricing, export formats, and UI settings.
  * *Interpretation*: Claims such as SciSpace having *"more text mining and analysis features"* [p. 5] or being able to *"simplify maths, tables and other complicated terms"* [p. 7] are descriptive impressions without empirical validation.

---

### 6. Verbatim Quote
> "As of May 10th, 2024, there are 12,209,406 papers available on SciSpace and 218,279,236 papers indexed on Semantic Scholar." [p. 3]

---

[Cha26h]:
### Bibliographic Information & Metadata
- **Exact Title:** ‘GenAI’ Literature Search Tools and Scholarly Diversity: An Algorithmic Ethnographical Analysis [PDF, p. 1]
- **Complete Authors:** Kathy M. Chandler, Katy Jordan, Ishaq Al-Naabi, Panagiota Tzanni, Leone Gately [PDF, p. 1]
- **DOI:** https://doi.org/10.55982/openpraxis.18.2.970 [PDF, p. 1, 19]
- **Venue, Volume, Date, and Status:** *Open Praxis*, Volume 18, Issue 2, pages 291–309; Submitted: 31 July 2025; Accepted: 05 March 2026; Published: 02 June 2026; Peer-reviewed Research Article [PDF, p. 1, 19]
- **Author Affiliations:** All five authors are affiliated with Lancaster University, UK [PDF, p. 16]
- **Competing Interests:** The authors declare no competing interests [PDF, p. 15]

---

### Empirical Design, Platforms, & Queries
- **Empirical Design:** Algorithmic ethnography incorporating algorithmic comparison and algorithmic triangulation; descriptive cross-sectional audit without inferential hypothesis testing [PDF, pp. 5–7].
- **Sample & Unit of Analysis:** 800 total search results (the top 20 journal article results per query across 10 platforms; $10 \times 4 \times 20 = 800$) [PDF, pp. 1, 6]. Data collected between October 2024 and April 2025 [PDF, p. 6].
- **Comparator / Reference Standard:**
  - *Comparator groups:* 5 GenAI tools versus 5 traditional academic literature search databases [PDF, p. 6, Table 1].
  - *Reference standard / Benchmark:* None. No gold standard or baseline relevance benchmark is used; analysis is purely descriptive [PDF, pp. 6–7].
- **Platforms Evaluated:**
  - *Traditional Databases (5):* Academic Search Ultimate, ERIC, Google Scholar, Scopus (toggled from default date sorting to relevance sorting), Web of Science [PDF, p. 6, Table 1].
  - *GenAI Tools (5):* Consensus, Elicit, Research Rabbit, Scopus AI, Semantic Scholar [PDF, p. 6, Table 1].
  - *Tool Versions / Pricing:* Free tiers were used for Consensus, Elicit, Research Rabbit, and Semantic Scholar; Scopus AI was evaluated via an institutional subscription [PDF, p. 6, 14]. Specific software build numbers are not reported.
- **Search Queries (Higher Education):**
  1. `breakout rooms`
  2. `learning management systems in higher education`
  3. `microcredentials`
  4. `citizen science` [PDF, p. 6]

---

### Metrics & Measured Numerical Results

#### 1. Geographic Representation (Global Majority Affiliations)
The authors operationalized Global Majority as institutional affiliations located outside North America (USA), Europe, Australia, and New Zealand [PDF, p. 7].

Table 2 reports the absolute number of papers with first authors based in Global Majority countries out of 20 results per query (denominator $N = 20$ per cell, $N = 80$ per platform, $N = 400$ per platform category):

This table details the frequency of top-20 search results authored by researchers in Global Majority countries across all four topics and 10 platforms, illustrating higher overall representation in GenAI tools.
[REGION: page=8, bbox=441,71,757,707]

- **Traditional Databases ($N = 400$):** 115 papers (28.75%)
  - Academic Search Ultimate: 28/80 (Breakout rooms: 4/20; Microcredentials: 1/20; LMS: 12/20; Citizen Science: 2/20)
  - ERIC: 27/80 (Breakout rooms: 4/20; Microcredentials: 4/20; LMS: 17/20; Citizen Science: 3/20)
  - Google Scholar: 23/80 (Breakout rooms: 9/20; Microcredentials: 3/20; LMS: 15/20; Citizen Science: 0/20)
  - Scopus: 18/80 (Breakout rooms: 6/20; Microcredentials: 1/20; LMS: 13/20; Citizen Science: 3/20)
  - Web of Science: 19/80 (Breakout rooms: 5/20; Microcredentials: 0/20; LMS: 12/20; Citizen Science: 1/20)
- **GenAI Tools ($N = 400$):** 126 papers (31.50%)
  - Consensus: 21/80 (Breakout rooms: 9/20; Microcredentials: 0/20; LMS: 11/20; Citizen Science: 1/20)
  - Elicit: 24/80 (Breakout rooms: 6/20; Microcredentials: 4/20; LMS: 14/20; Citizen Science: 0/20)
  - Research Rabbit: 25/80 (Breakout rooms: 9/20; Microcredentials: 2/20; LMS: 13/20; Citizen Science: 1/20)
  - Scopus AI: 27/80 (Breakout rooms: 6/20; Microcredentials: 5/20; LMS: 13/20; Citizen Science: 3/20)
  - Semantic Scholar: 29/80 (Breakout rooms: 9/20; Microcredentials: 3/20; LMS: 16/20; Citizen Science: 1/20) [PDF, p. 8, Table 2]

#### 2. First-Author Gender Representation
Determined via institutional biographies and pronouns [PDF, p. 6]. No non-binary lead authors were identified [PDF, p. 6].
- Across all platforms, the mean showed parity (~10 female lead authors out of 20) [PDF, p. 7, Figure 1].
- Variation by platform: Scopus had the highest number of female lead authors overall; Scopus AI and Academic Search Ultimate had the lowest [PDF, p. 7].
- Strong topic confounding: Citizen science and breakout rooms yielded more female first authors; microcredentials and LMS yielded predominantly male first authors [PDF, p. 7].

#### 3. Web of Science Indexing & Journal Impact Factor (JIF)
- **WoS Indexing:** High indexing rates for publisher-linked tools (Web of Science [20/20], Scopus, Scopus AI, Academic Search Ultimate); other GenAI and traditional tools retrieved fewer WoS-indexed articles [PDF, p. 9, Figure 4].
- **JIF Median Ranks (Table 4):**
  - Scopus AI ranked highest for JIF (aggregate score: 8; Breakout rooms: 1, Microcredentials: 1, LMS: 1, Citizen Science: 5) [PDF, p. 13, Table 4].
  - Non-Scopus AI GenAI tools retrieved lower-JIF sources overall (Consensus aggregate: 23.5; Elicit: 23; Research Rabbit: 21.5; Semantic Scholar: 28) [PDF, p. 13, Table 4].
  - Traditional database aggregate ranks: Google Scholar (16.4 [see contradictions]), Academic Search Ultimate (17.5), ERIC (18.5), Scopus (28.5), Web of Science (29) [PDF, p. 13, Table 4].

#### 4. Citations & Ranking Tendencies (Table 3)
Citations counted via Google Scholar [PDF, p. 10]. Table 3 ranks platforms from largest median citations (Rank 1) to lowest (Rank 10):
- Google Scholar (aggregate rank: 13) and Scopus (14) led the traditional tools in retrieving high-citation papers [PDF, p. 11, Table 3].
- Elicit (aggregate rank: 8) and Consensus (13) led the GenAI tools in retrieving high-citation papers [PDF, p. 11, Table 3].
- Lowest median citation ranks: Academic Search Ultimate (33.5), ERIC (31), Semantic Scholar (30), Research Rabbit (27.5) [PDF, p. 11, Table 3].

---

### Focus on Targeted GenAI Systems

1. **Scopus AI:**
   - Tied for the highest representation of Global Majority authors among GenAI tools on microcredentials (5/20) and matched ERIC for the highest on citizen science (3/20); total: 27/80 [PDF, p. 8, Table 2].
   - Consistently favored established, high-prestige journals (lowest median JIF rank = 8) and displayed high Web of Science indexing [PDF, p. 9, 13].
   - Skewed furthest toward male first authors among all evaluated platforms [PDF, p. 7].
2. **Semantic Scholar:**
   - Achieved the highest Global Majority paper count across all evaluated platforms (29/80) [PDF, p. 8, Table 2].
   - Tended toward lower median citation counts (aggregate citation rank: 30) and lower median JIF (aggregate rank: 28) [PDF, pp. 11, 13].
   - Yielded higher-than-average female first-author counts [PDF, p. 7].
3. **Reproducibility & Scholar Labs:**
   - Scholar Labs was not evaluated in this study [PDF, p. 6, Table 1].
   - Reproducibility limitations: Algorithmic opacity ("black box"), dynamic search ranking updates over time, and absence of query timestamps restrict identical retrieval reproduction [PDF, pp. 5, 15].

---

### Limitations & Caveats
- Limited scope: 10 platforms, 4 queries, single broad discipline (higher education / educational technology) [PDF, p. 15].
- Only the top 20 results evaluated per search [PDF, p. 6].
- Payment tier differences: Free tiers were used for four GenAI tools, whereas Scopus AI required a paid institutional license [PDF, p. 6, 14, 15].
- Gender operationalization: Reliant on pronouns found in institutional/social profiles, carrying misgendering risk and limited to binary representation [PDF, p. 6].
- Binary geographic taxonomy: Grouping countries into a Global Majority versus Global Minority dichotomy masks sub-regional variation [PDF, p. 7].

---

### Discrepancies and Inconsistencies Noted in the Text
1. **Duplicate Platform Reference:** In the Discussion, the text states:
   > "Consensus, Elicit, Scopus AI and Scopus AI were notably more likely to include older results" [PDF, p. 13].
   This inadvertently repeats *Scopus AI* twice; on page 8, the corresponding list was: "Consensus, Elicit, ScopusAI and Google Scholar" [PDF, p. 8].
2. **Arithmetic Discrepancy in Table 4:** For Google Scholar, the four topic ranks are listed as 2, 3.5, 8, and 3, which sum to **16.5**, but the printed "TOTAL" column reports **16.4** [PDF, p. 13, Table 4].
3. **Publication Timeline:** The paper records data collection between October 2024 and April 2025, submission on 31 July 2025, and publication on 02 June 2026 [PDF, pp. 6, 19].

Region format: page is 1-indexed; bbox=top,left,bottom,right, normalized 0-1000 from top-left.
