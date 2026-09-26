# Related search system full-text extractions

Verification corrections and final classifications are in [the processing report](undermind-processing-2026-09-27.md). This raw machine transcript contains errors, including the diversity study's Global Majority/Global North label and IRIS.AI venue; it is not authoritative evidence.

Undermind MCP extraction notes. Verify relevant findings against local PDFs before promotion. These include developer benchmarks and independent studies; see each record. Date: 2026-09-27.

[He25b]:
### Bibliographic Information
- **Title:** PaSa: An LLM Agent for Comprehensive Academic Paper Search
- **Authors:** Yichen He\*, Guanhua Huang\*, Peiyuan Feng, Yuan Lin†, Yuchen Zhang, Hang Li, Weinan E (\*equal contribution, †corresponding author)
- **Status/Venue/Date:** arXiv preprint `arXiv:2501.10120v2 [cs.IR]`, May 27, 2025. No DOI printed.
- **Affiliations & Vendor Involvement:** ByteDance Seed (He, Huang, Feng, Lin, Zhang, Li) and Peking University (E). The authors are affiliated with ByteDance, and the acknowledgments state ByteDance personnel assisted in developing and releasing the PaSa demo. No external grant funding is reported.

---

### Systems Tested
- **Proposed System:** PaSa-7b (composed of a Crawler and a Selector, both fine-tuned from Qwen2.5-7B; Crawler trained via imitation learning and session-level PPO) and PaSa-7b-ensemble (Crawler executed twice via sampling decoding).
- **Baselines:** Google Search and Google Scholar (via Serper API); Google with GPT-4o (queries paraphrased by GPT-4o); ChatGPT (search-enabled GPT-4o); GPT-o1 (zero-shot, no search access); and PaSa-GPT-4o (prompted GPT-4o implementing the PaSa workflow).

---

### Study Design, Benchmark, and Reference Standard
- **Study Type:** System introduction and benchmark evaluation conducted by the system's own creators (not an independent product evaluation).
- **Benchmarks (Both Created by the Authors):**
  1. *AutoScholarQuery:* Synthetic dataset derived from the Related Work sections of ICLR 2023, ICML 2023, NeurIPS 2023, ACL 2024, and CVPR 2024 using GPT-4o prompt generation. Target papers are referenced arXiv papers published before the query date (33,551 train / 1,000 dev / 1,000 test).
  2. *RealScholarQuery:* 50 real-world AI queries from researchers. Candidate papers were pooled from PaSa and baselines (average 76 candidate papers per query), then manually labeled by Chinese university computer science professors ($4 per entry; average 15.82 relevant papers per query).

---

### Key Metrics and Results
- **RealScholarQuery (Table 5, p. 8):**
  - **PaSa-7b:** Precision = 0.5146, Recall = 0.6111, Recall@20 = 0.5798, Recall@50 = 0.6563.
  - **PaSa-7b-ensemble:** Precision = 0.4938, Recall = 0.6488, Recall@20 = 0.5986, Recall@50 = 0.6877.
  - **PaSa-GPT-4o baseline:** Precision = 0.4721, Recall = 0.3075.
  - **Google with GPT-4o baseline:** Recall@20 = 0.2020, Recall@50 = 0.2573.
- **AutoScholarQuery Test Set (Table 4, p. 8):**
  - **PaSa-7b:** Precision = 0.1448, Recall = 0.4834, Recall@20 = 0.5301, Recall@50 = 0.6334.
  - **PaSa-GPT-4o baseline:** Precision = 0.1457, Recall = 0.3873.
  - **Google with GPT-4o baseline:** Recall@20 = 0.1921, Recall@50 = 0.2450.

---

### Reporting Inconsistencies & Limitations
- **Inconsistencies:**
  - On page 2, the AutoScholarQuery training split count is listed as 33,511, but on page 3, it is stated as 33,551.
  - Percentage improvements (e.g., exceeding Google with GPT-4o by 37.78% in recall@20 on RealScholarQuery) are reported as absolute percentage-point differences (0.5798 vs. 0.2020) rather than relative increases.
  - In Table 4, ChatGPT was only evaluated on a 100-sample subset due to manual interface submission limits, unlike other automated baselines.
- **Limitations:**
  - Experiments and datasets are restricted exclusively to AI/machine learning papers.
  - Agent foundation models are restricted to 7B parameters.
  - Trajectory search depth is capped at three steps due to computational limits.
  - RealScholarQuery is constrained to 50 queries due to high annotation costs.

---

[Ju25]:
### Document Overview
- **Exact Title:** WisPaper: Your AI Scholar Search Engine
- **Authors:** Li Ju, Jun Zhao, Mingxu Chai, Ziyu Shen, Xiangyang Wang, Yage Geng, Chunchun Ma, Hao Peng, Guangbin Li, Tao Li, Chengyong Liao, Fu Wang, Xiaolong Wang, Junshen Chen, Rui Gong, Shijia Liang, Feiyan Li, Ming Zhang, Kexin Tan, Junjie Ye, Zhiheng Xi, Shihan Dou, Tao Gui, Yuankai Ying, Yang Shi, Yue Zhang, Qi Zhang
- **Publication Status/Venue/Date/DOI:** arXiv preprint (arXiv:2512.06879v2 [cs.IR]); dated 27 Feb 2026; no DOI printed.
- **Affiliations & Vendor Involvement:** WisPaper.ai and Fudan University (Fudan NLP Lab). Several authors are affiliated with WisPaper.ai, indicating direct corporate/vendor backing.
- **Funding:** No grant funding declared; acknowledgments note annotators across several universities.

---

### Systems Tested & Study Design
- **Evaluated System:** WisPaper (agent system) / WisModel (underlying specialized LLM initialized via SFT and trained using GRPO reinforcement learning).
- **Baselines Tested:**
  - *Query Understanding:* Qwen-Max, GPT-4o, GPT-5/GPT-5.1, GLM-4-Flash, GLM-4.6, DeepSeek-V3.2-Exp.
  - *Paper-Criteria Matching:* GPT-5.1, Claude-Sonnet-4.5, Qwen3-Max, DeepSeek-V3.2, Gemini3-Pro.
  - *TaxoBench End-to-End:* O3, Gemini, Grok, Perplexity, DeepSeek, Qwen, Doubao.
- **Sample & Reference Standard:**
  - *Internal Benchmark:* 2,777 English/Chinese queries across 10 academic disciplines with 5,879 criteria annotated by domain-expert PhD students. Reference standards were expert Boolean queries, criteria, and 4-way classification labels (`support`, `somewhat support`, `reject`, `insufficient information`).
  - *TaxoBench Benchmark:* 72 computer science survey papers containing 3,815 expert-mapped core reference papers.

---

### Key Findings & Exact Metrics
1. **Query Decomposition & Criteria Generation** (Page 8, Table 2):
   WisModel achieved 94.8% semantic similarity, 67.7% ROUGE-L, 39.8% BLEU, and a 98.2% length ratio (outperforming second-best GPT-4o at 91.3% similarity and 52.6% ROUGE-L).
2. **Paper-Criteria Matching Accuracy** (Page 9, Table 3):
   WisModel reached 93.70% overall accuracy (highest baseline: Gemini3-Pro at 73.23%). On the difficult partial-support category (`somewhat support`), WisModel scored 91.82%, whereas baselines achieved between 15.90% and 45.00%.
3. **End-to-End Retrieval Recall** (Page 9, Figure 4; Page 10, Section 4.4):
   On TaxoBench, WisPaper achieved 22.26% recall, surpassing the previous state-of-the-art generalist agent baseline (O3 at 20.92%).

The recall comparison across Deep Research agents on TaxoBench is illustrated in Figure 4:
Figure 4 displays a bar chart comparing end-to-end paper recall percentages on the TaxoBench benchmark across eight systems. WisPaper leads at 22.26%, followed by O3 (20.92%), Gemini (15.23%), Grok (12.82%), Perplexity (6.61%), DeepSeek (4.61%), Qwen (4.35%), and Doubao (3.15%).
[REGION: page=9, bbox=668,588,866,885]

---

### Independence, Inconsistencies & Limitations
- **Benchmark Independence:** The TaxoBench benchmark [18] is not fully independent: several WisPaper co-authors (e.g., Ming Zhang, Kexin Tan, Shihan Dou, Tao Gui, Qi Zhang) are also primary co-authors of the TaxoBench paper.
- **Reporting Inconsistencies:**
  - In Table 2, the baseline is labeled "GPT-5", but the text refers to "GPT-5.1".
  - Baseline naming switches between "Gemini3-Pro" (Table 3) and "Gemini-3-Pro" (text), as well as "DeepSeek-V3.2-Exp" and "DeepSeek-V3.2".
  - Typographical errors include "Figuer 4" (page 10) and referencing "WisPaper" instead of "WisModel" as the trained agent in Section 6.
- **Limitations:**
  - Absolute end-to-end recall remains low across all evaluated systems (22.26%).
  - TaxoBench evaluations were restricted to computer science topics.
  - Candidate verification relies predominantly on abstract/metadata snippets rather than complete full-text evaluation.

---

### References
- [18] Ming Zhang, Jiabao Zhuang, Wenqing Jing, Kexin Tan, Ziyu Kong, Jingyi Deng, Yujiong Shen, Yuhang Zhao, Ning Luo, Renzhe Zheng, Jiahui Lin, Mingqi Wu, Long Ma, Shihan Dou, Tao Gui, Qi Zhang, and Xuanjing Huang. Can deep research agents retrieve and organize? evaluating the synthesis gap with expert taxonomies, 2026. URL https://arxiv.org/abs/2601.12369.

---

[Liu26c]:
### Study Metadata
- **Exact Title:** Do AI chatbots find what experts would? Effects of model, user role, and sample size on study retrieval for medical questions
- **Authors:** Qingfang Liu, Qiao Jin, Joe D. Menke, Thorsten Kahnt, Zhiyong Lu
- **Publication / Preprint Status & Venue:** arXiv preprint (`arXiv:2608.13786v1 [cs.IR] 13 Aug 2026`). Also carries a copyright notice: "© 2024 The Authors. Open Access chapter published by World Scientific Publishing Company" (p. 2).
- **Date:** 13 Aug 2026 (arXiv submission date).
- **DOI:** None printed.
- **Affiliations:** National Institute on Drug Abuse Intramural Research Program, NIH (Liu, Kahnt); National Library of Medicine, NIH (Jin, Lu); School of Information Sciences, University of Illinois Urbana-Champaign (Menke).
- **Funding & Vendor Involvement:** Supported by the Intramural Research Program of the NIH; Q.J. supported by NIH K99LM014903. No commercial vendor funding or involvement is reported.

---

### Evaluation Type & Systems Tested
- **Evaluation Type:** Independent product evaluation of commercial consumer LLM chatbots. (The paper references Humanity’s Last Exam as external benchmark context rather than presenting it as the authors' own benchmark.)
- **Systems & Configurations Tested** (Table 1, p. 5):
  - Anthropic Claude Sonnet 5 (Knowledge cutoff: Jan 2026; release: June 30, 2026; "Medium effort; thinking enabled")
  - Google Gemini 3.1 Pro (Knowledge cutoff: Jan 31, 2025; release: Feb 19, 2026; "Extended thinking")
  - OpenAI ChatGPT GPT-5.5 (Knowledge cutoff: Dec 1, 2025; release: April 23, 2026; "High reasoning")
  - All systems evaluated via web interfaces equipped with web search.

---

### Design, Sample, & Reference Standard
- **Design:** Factorial evaluation across 3 chatbots $\times$ 3 simulated user roles (patient, clinician, evidence-synthesis researcher) $\times$ 4 repetitions across 20 clinical questions, totaling 720 responses collected in fresh anonymous sessions (mid- to late July 2026).
- **Sample & Reference Standard:** Questions adapted from 20 intervention reviews from Issues 6 and 7 of the 2026 *Cochrane Database of Systematic Reviews* (encompassing 442 Cochrane-included studies and 932 Cochrane-excluded studies).

---

### Key Findings & Exact Metrics
- **Cochrane Included-Study Recall (Response-level):** ChatGPT achieved $63.1\% \pm 29.5\%$, Claude $37.0\% \pm 23.8\%$, and Gemini $17.3\% \pm 13.1\%$ ($p = 2.0 \times 10^{-5}$; Section 3.2, p. 6; Fig. 2, p. 8). By role: researcher $42.8\% \pm 30.8\%$, clinician $38.6\% \pm 28.9\%$, patient $36.1\% \pm 29.3\%$ ($p = 2.0 \times 10^{-5}$; Section 3.2, p. 6).
- **Cumulative Study Identification:** Across all responses pooled, chatbots retrieved 328 of 442 included studies ($74.2\%$) and cited 143 of 932 excluded studies ($15.3\%$) (Section 3.3, p. 7; Fig. 3, p. 9).
- **Multivariable Predictors of Recall:** Trial sample size was the sole significant independent predictor (adjusted OR 1.800 per 1-unit increase in log sample size, 95% CI 1.37–2.36, $p < 0.001$; Table 3, p. 10).
- **Errors:** 232 of 7,676 matched citations ($3.0\%$) had metadata errors (Claude: 5.9%, ChatGPT: 1.5%, Gemini: 0.2%). Only Claude produced unresolved/fabricated citations ($n = 23$) (Section 3.6, p. 10).

---

### Overview of Primary Recall and Consistency Results

The performance comparison across chatbots and user roles, including consistency across replicates, is detailed in Figure 2:

A composite figure displaying Cochrane included-study recall: a heatmap of the 9 chatbot-by-role combinations, marginal bar plots for chatbot means and user-role means, and a bar plot showing recall consistency (mean pairwise Jaccard similarity across replicates).
[REGION: page=8, bbox=108,82,698,903]

---

### Limitations & Reporting Inconsistencies
- **Limitations:** Only 20 reviews from two Cochrane issues; standardized prompt constraints (e.g., forbidding secondary reviews) do not reflect unconstrained patient queries; potential unmeasured exposure to pre-cutoff evidence; proprietary search/retrieval mechanisms remain opaque (Section 4.6, p. 13).
- **Reporting Inconsistencies:** The document is dated August 2026 on arXiv (and tests 2026 models/issues), but the copyright notice on page 2 states "© 2024 The Authors". Additionally, page 9 text states 143 Cochrane-excluded studies were cited, whereas Section 3.5 and Table 4 (pp. 10–11) report classifying 142 unique excluded studies.

---

[Gao26]:
### Bibliographic & Study Identification
- **Title:** Errors in AI-Assisted Retrieval of Medical Literature: A Comparative Study
- **Authors:** Jenny Gao, Yongfeng Zhang, Mary L Disis, Lanjing Zhang
- **Status/Venue/DOI:** Unpublished manuscript / draft preprint; no journal venue, publication date, or DOI is printed on the document.
- **Affiliations:** New York University; Rutgers University; University of Washington; Princeton Medical Center; Rutgers Cancer Institute.
- **Funding & Disclosures:** Supported by the National Cancer Institute, NIH (R37CA277812 to LZ). Funders had no role in study conduct. Authors declare no conflicts of interest.
- **Evaluation Type:** Independent comparative evaluation of commercial/public LLMs (not the system authors' own benchmark).

---

### Study Design & Methodology
- **Systems Tested:** Free versions of Grok (Grok-2), ChatGPT (GPT-4.1 [sic]), Google Gemini (Flash 2.5), Perplexity AI, and DeepSeek (GPT-4 [sic]).
- **Sample:** 40 original research articles (10 each from *BMJ*, *JAMA*, *Lancet*, and *NEJM*; 5 from 2024 and 5 from early 2025 per journal).
- **Procedure:** Each LLM received the article abstract and was prompted to retrieve 10 key references with bibliographic metadata (title, year, DOI, PubMed ID, Google Scholar URL), followed by a prompt instructing the LLM to verify its citations (2,000 total retrieved references evaluated across 5 LLMs).
- **Reference Standard:** Manual lookup in DOI (doi.org), PubMed, and Google Scholar, plus checking against the source article’s bibliography for relevance.

---

### Key Metrics & Findings
- **Complete Miss Rate (Failure on all metrics):** Overall rate was 47.8% (956/2,000). By platform: Grok 11.2% (45/400), ChatGPT 29.0% (116/400), DeepSeek 51.8% (207/400), Perplexity 73.0% (292/400), Gemini 78.5% (314/400) (Page 8, Figure 3).
- **Multimetric Score Ratio (Composite score / score cap, range 0–1.25):** Mean across platforms was 0.29 (SD 0.35). Grok achieved 0.57, ChatGPT 0.42, DeepSeek 0.21, Perplexity 0.12, and Gemini 0.11 (Page 7, Figure 2).
- **Bibliographic Metadata Retrieval:** Across 2,000 references, valid DOIs were provided in 624 (31.2%), valid PubMed IDs in 372 (18.6%), valid Google Scholar links in 846 (42.3%), and relevant citations in 422 (21.1%) (Page 12, Table 1).

A forest plot on page 8 details the complete miss proportions and multivariable odds ratios across LLM platforms and journals:
Complete miss proportions and odds ratios across journals and platforms demonstrate that Grok had the lowest complete miss rate (11.2%), whereas Gemini had the highest (78.5%), and *NEJM* articles had significantly higher miss rates than *BMJ*.
[REGION: page=8, bbox=370,110,690,880]

---

### Reporting Inconsistencies & Anomalies
- **Timeline/Dates:** The paper describes sampling and query dates occurring between July and December 2025, and references citations indexed into 2025/2026.
- **Model Designations:** Labels such as "ChatGPT (GPT-4.1)" and "DeepSeek (GPT-4)" do not match standard model nomenclature.
- **Omission in Abstract:** The abstract omits *The Lancet* when naming journals, despite analyzing 10 articles from it.
- **Typographical Errors:** Gemini is repeatedly spelled "Genimi" in the abstract and results (Pages 2, 7, 8).
- **Cross-Reference Error:** Page 8 cites Table 1 for complete miss rates, but these data are presented in Figure 3.

---

### Limitations
Evaluated only free tiers; simple prompting without advanced agentic workflows; prompt-based verification failed to correct mistakes; relevance scoring involved human subjective assessment; LLMs received only abstracts rather than full-text articles.

---

[Sah26d]:
### Evidence Summary: [Sah26d]

**Title:** Rethinking Literature Search Evaluation: Deep Research Helps, and Human Citation Lists Are Not a Ground Truth
**Authors:** Gaurav Sahu, Laurent Charlin, Christopher Pal
**Affiliations:** Mila – Quebec AI Institute, HEC Montréal, ServiceNow Research, Canada CIFAR AI Chair, Université de Montréal, Polytechnique Montréal
**Publication Status & Date:** arXiv preprint, `arXiv:2605.29234v1 [cs.AI]`, dated 28 May 2026 (no DOI printed)
**Funding / Vendor Involvement:** Author affiliations include ServiceNow Research and Canada CIFAR AI Chair; no separate commercial sponsorship statement is noted.

---

### Systems Evaluated
- **Evaluated retrieval & re-ranking pipelines:**
  - Deep Research pipeline using breadth-first citation graph expansion with interchangeable re-ranking modules:
    - `QWEN3-EMBEDDING-8B` (served via vLLM)
    - LLM Debate ranker
    - Debate + Qwen3 ensemble
  - Un-reranked Deep Research (`No Reranking (with DR)`)
  - Vanilla API baseline (`No Rerank (no DR)`)
  - Deep research agent baselines: `PASA` and `SCHOLARQA` (both evaluated using abstract-only input)
- **Evaluator / Judge Model:** `GPT-OSS-120B` (served via vLLM)

---

### Benchmark, Study Design, & Reference Standard
- **Benchmark:** The authors constructed their own benchmark, **ROLLINGEVAL-JUN25** (a June 2025 snapshot of 250 computer science arXiv submissions with cleaned full texts and bibliographies).
- **Evaluation Type:** Authors evaluate their own Deep Research framework against independent third-party baselines (PASA, ScholarQA, vanilla API search).
- **Reference Standard & Diagnostics:**
  - Coverage evaluated against the author-curated reference lists (9,204 human query-reference pairs).
  - Semantic Relevance (SR) evaluated on candidate titles/abstracts by a neutral LLM-as-a-judge (`GPT-OSS-120B`) using a 0–5 scale scaled to 0–100.
  - Co-authorship distance ($d \in \{0, 1, 2, 3, \ge 4\}$) computed on the OpenAlex graph.

---

### Key Exact Metrics & Findings

Table 1 and Table 3 report the primary retrieval and relevance metrics:

A summary of precision and recall comparisons across different retrieval configurations:
[REGION: page=3, bbox=82,126,236,493]

Topical relevance breakdown between human reference lists and AI re-ranking methods:
[REGION: page=3, bbox=81,515,191,878]

1. **Recall & Precision (Table 1, p. 3):**
   - **QWEN3 emb.:** Recall@100 = 22.2%, Recall@1k = 51.9%; Precision@20 = 16.8%, Precision@100 = 8.0%.
   - **Debate+Qwen3:** Recall@100 = 18.1%, Recall@1k = 46.2%; Precision@20 = 14.7%, Precision@100 = 6.6%.
   - **No Rerank (no DR):** Recall@100 = 0.3%, Recall@1k = 1.9%; Precision@20 = 0.1%, Precision@100 = 0.1%.
2. **Semantic Relevance at Matched Top-$N_P$ (Table 3, p. 3):**
   - **Human references:** Mean score = 51.2; $\le 40$ in 48.6%; $\ge 60$ in 51.4% ($n = 9{,}204$).
   - **Debate+QWEN3:** Mean score = 62.4; $\le 40$ in 12.2%; $\ge 60$ in 87.8% ($n = 9{,}173$).
   - **QWEN3 emb.:** Mean score = 62.4; $\le 40$ in 14.0%; $\ge 60$ in 86.0% ($n = 9{,}173$).
3. **Co-authorship Bias (Table 4, p. 4):**
   - Direct co-authorship ($d=0$): Humans cite collaborators at 5.13% vs. 1.92% for Debate+QWEN3 and 2.05% for QWEN3.

---

### Limitations & Reporting Inconsistencies
- **Limitations (Section 5 & Limitations, pp. 4–5):** Abstract-conditioned judge ignores in-text citation contexts (penalizing foundational tools/libraries like PyTorch or Adam); evaluation is confined exclusively to arXiv-indexed computer science papers; single LLM judge.
- **Reporting Inconsistencies:**
  - Section C.2 refers to "Table 6" for the debate re-ranker prompt, but it is formatted as a prompt table titled Table 6.
  - Section C.4 refers to the semantic relevance prompt as "Table 8", which is formatted as Table 8 on p. 11.
  - The OpenAlex graph traversal caps each author at the 1,000 most recent works, deliberately under-counting distant paths.

---

[She26b]:
### Bibliographic Information
- **Title:** ScholarGym: Benchmarking Large Language Model Capabilities in the Information-Gathering Stage of Deep Research
- **Authors:** Hao Shen, Hang Yang, Zhouhong Gu, Weili Han
- **Affiliation:** Fudan University
- **Publication / Venue / Status:** Preprint; arXiv:2601.21654v3 [cs.AI], submitted 17 Feb 2026 (header/footer reads *Preprint. February 18, 2026*). No DOI listed.
- **Vendor Involvement / Funding:** No commercial vendor co-authorship or corporate funding is disclosed.

### Benchmark Type & Systems Evaluated
- **Evaluation Type:** Independent academic evaluation establishing the authors' novel benchmark (`ScholarGym`) and evaluating external LLMs.
- **Evaluated Systems / Versions:**
  - *Open-source:* Qwen3 (8B, 30B), Qwen3-8B†, Qwen3-30B†, GLM-4.7.
  - *Proprietary:* DeepSeek-V3.2, DeepSeek-V3.2†, GPT-5.2, Gemini3-Pro.
  - *(† denotes extended thinking mode.)*
  - *Baseline:* Direct Query baseline (evaluated on Qwen3-8B and Qwen3-30B).

### Design, Sample, & Reference Standard
- **Corpus:** A static corpus of 570,000 arXiv papers (1990–2024) across computer science, physics, and mathematics.
- **Queries & Ground Truth:** 2,536 expert-annotated queries sourced from PaSa (AutoScholar and RealScholar splits) and LitSearch, each paired with expert-annotated relevant papers.
- **Evaluation Sets:**
  - `Test-Fast`: 200 queries (average 1.9 ground-truth papers).
  - `Test-Hard`: 100 cross-domain queries where evaluated models perform poorly (average 2.6 ground-truth papers).
- **Setup:** A 3-stage iterative loop (Query Planning, Tool Invocation, Relevance Assessment) operating with memory over 5 iterations ($T=5$, default BM25 sparse retrieval, Abstract-only assessment).

Table 3 summarizes the primary selection and retrieval metrics across all tested models on both the Test-Fast and Test-Hard benchmarks.
[REGION: page=6, bbox=68,88,367,883]

### Key Exact Metrics
- **Direct Query vs. Iterative Planning (Page 6, Table 3):**
  - Qwen3-30B selection F1 increases from 0.098 (Direct Query) to 0.285 (iterative planning), a 2.9× improvement.
  - Qwen3-8B selection F1 increases from 0.069 to 0.231 (3.3× gain).
- **Test-Fast Performance at Iteration 5 (Page 6, Table 3):**
  - *GPT-5.2:* Top selection F1 of 0.447 (Recall = 0.837, Precision = 0.305).
  - *Gemini3-Pro:* Highest selection Recall of 0.950 (Precision = 0.199, F1 = 0.329).
  - *Qwen3-30B†:* Best open-source F1 of 0.362 (Recall = 0.482, Precision = 0.290).
- **Test-Hard Performance at Iteration 5 (Page 6, Table 3 & Page 13, Table 9):**
  - Severe performance collapse across all systems (best F1 falls ~80% relative to Test-Fast).
  - *Qwen3-30B†:* Selection F1 = 0.087 (Recall = 0.172, Precision = 0.058).
  - *GPT-5.2:* Selection F1 = 0.081 (Recall = 0.397, Precision = 0.045).

### Reporting Inconsistencies & Discrepancies
- **Figure 3 vs. Text (Page 7):** Section 4.4.2 states Qwen3-8B† starts at 1.46% and drops to 0.38%, but Figure 3 labels the 1.46% row as base `Qwen3-8B` and shows `Qwen3-8B†` spanning 1.20% to 0.78%.
- **Figure 7 vs. Text (Page 8):** Text reports removing memory causes Qwen3-8B† F1 to drop −18.4% (from 0.293 to 0.239), whereas Figure 7 annotates the reverse bar difference as `+22.6%`.
- **Dataset Utilization:** Although 2,536 total queries are constructed, all reported model experiments use only `Test-Fast` (200) or `Test-Hard` (100).

### Limitations
- Evaluates only upstream information gathering, not end-to-end report generation or synthesis.
- Restricted to a static academic arXiv corpus (stem fields only), omitting web browsing dynamics.
- F1 degrades by ~80% on cross-disciplinary queries (`Test-Hard`).

---

[Son20]:
### Metadata & Study Overview
- **Exact Title:** An evaluation of two commercial deep learning-based information retrieval systems for COVID-19 literature
- **Authors:** Sarvesh Soni and Kirk Roberts
- **Venue & Publication Status:** *Journal of the American Medical Informatics Association*, Volume 28, Issue 1, 2021, Pages 132–137; Advance Access Publication Date: 17 November 2020; Peer-reviewed Case Report.
- **DOI / Dates:** `10.1093/jamia/ocaa271` | Received: 24 July 2020; Editorial Decision: 2 October 2020.
- **Affiliation:** School of Biomedical Informatics, The University of Texas Health Science Center at Houston, Houston, Texas, USA.
- **Vendor Involvement & Conflicts:** None. Authors declare no conflicts of interest. Commercial vendors (Amazon, Google) had no involvement.
- **Funding:** Supported in part by the National Science Foundation (NSF) under award OIA-1937136.
- **Evaluation Type:** Independent post hoc empirical evaluation of commercial tools against academic systems (the commercial vendors did not release formal evaluations or participate in TREC-COVID).

---

### Systems Tested, Study Design, & Reference Standard
- **Systems & Versions Tested:**
  - **Amazon:** CORD-19 Search (built on Amazon Comprehend Medical and Amazon Kendra).
  - **Google:** COVID-19 Research Explorer (BERT fine-tuned on BioASQ with synthetic query generation).
  - *Query configurations:* Tested using "question only" and "question + narrative" variants (accessed first week of May 2020).
  - *TREC-COVID Comparison:* Top five Round 1 submissions ranked by bpref (`sab20.1.meta.docs`, `sab20.1.merged`, `UIowaS_Run3`, `smith.rm3`, `udel_fang_run3`).
- **Sample & Benchmark Corpus:** 30 topics from Round 1 of TREC-COVID evaluated against the April 10, 2020 CORD-19 release. Search results retrieved after April 10 were filtered to this release, and evaluation depth was normalized using a "topic-minimum" threshold (average ~43 documents/topic, median 40.5).
- **Reference Standard:** TREC-COVID Rounds 1 and 2 relevance judgments, augmented by 141 additional relevance assessments conducted by TREC-COVID assessors to evaluate the top 10 results of all commercial variants.

---

### Key Metric Findings
The table summarizes precision, rank-based, and preference metrics (P@5, P@10, NDCG@10, MAP, NDCG, and bpref) across Amazon, Google, and the top five TREC-COVID systems after threshold normalization:
[REGION: page=4, bbox=56,91,263,908]

Key exact metrics (Page 4, Table 2):
- **Top Academic System (`sab20.1.meta.docs`):** P@5 = 0.7800; P@10 = 0.7133; NDCG@10 = 0.6109; MAP = 0.0999; bpref = 0.1352.
- **Amazon (question + narrative):** P@5 = 0.7200; P@10 = 0.6400; NDCG@10 = 0.5583; MAP = 0.0766; bpref = 0.1063.
- **Google (question + narrative):** P@5 = 0.6067; P@10 = 0.5600; NDCG@10 = 0.5112; MAP = 0.0687; bpref = 0.1054.
- **Google (question only):** P@5 = 0.5733; P@10 = 0.5700; NDCG@10 = 0.4972; MAP = 0.0693; bpref = 0.1069.

---

### Limitations & Reporting Inconsistencies
- **Limitations:** API restrictions limited retrieval to 100 documents per query; post hoc evaluation required filtering newer documents and conducting supplemental judgments only for top 10 documents; evaluation depth was limited by the topic-minimum document cutoff.
- **Reporting Inconsistencies / Errata:** A stray numeral appears in the acknowledgments ("7The authors thank..."); the PDF text encodes the plus sign in "question + narrative" as character `þ`.

---

[Sch24d]:
### Bibliographic Information
- **Title:** Conversational Exploratory Search of Scholarly Publications Using Knowledge Graphs
- **Authors:** Phillip Schneider, Florian Matthes
- **Affiliation:** Technical University of Munich, Department of Computer Science, Germany
- **Publication/Preprint Status:** arXiv preprint (arXiv:2410.00427v1 [cs.CL])
- **Date / Venue:** 1 Oct 2024; no printed journal/conference venue or DOI provided.
- **Funding:** Supported by the German Federal Ministry of Education and Research (BMBF) Software Campus grant 01IS17049. No commercial vendor involvement reported.

### Study Nature
This is the system authors' own implementation, benchmark, and user evaluation of their proposed conversational system, rather than an independent third-party evaluation.

### Evaluated Systems & Components
- **Proposed Architecture:** RASA-based dialogue agent with Streamlit frontend; Neo4j knowledge graph (over 85,000 ACL Anthology publications mapped to a 12-topic/71-subtopic NLP taxonomy); Weaviate vector database.
- **Underlying Models:**
  - Topic classification: SetFit fine-tuned `multi-qa-MiniLM-L6-cos-v1` compared against SPECTER2 embedding similarity search and GPT-3.5-Turbo (version: 0613).
  - Abstract sentence classification: SciBERT fine-tuned on Gonçalves et al. (2020) dataset.
  - Generation (cluster naming and paper summarization): Zephyr-7B-Beta (selected over Falcon-7B and Llama-2-7B).
- **Comparison Baseline:** A graphical interface featuring traditional text-based search.

### Design, Sample, & Reference Standard
- **Model Benchmark:** Synthetic classification dataset generated using GPT-3.5-Turbo (1,601 training, 364 test queries) across 12 NLP topics and out-of-scope queries.
- **Human Evaluation:** Crossover user study with 40 non-expert participants (Group A: $n=20$, Group B: $n=20$; 65% male, 35% female; mean age 25.03) evaluating two scenarios (Scenario 1: COVID-19 mental health social media analysis; Scenario 2: automated programming exam question generation).
- **Measures:** System Usability Scale (SUS, 0–100) and 5-point Likert scales (readability, correctness, usefulness, summary quality, overall satisfaction).

### Key Exact Metrics
- **Topic Classifier F1-score** (Page 5, Figure 2): SetFit achieved 0.95, outperforming GPT-3.5-Turbo (~0.75) and SPECTER2 vector similarity search (<0.50).
- **Human Evaluation Metrics [Mean (Std. Dev.)]** (Page 7, Table 1):
  - *System Usability Scale (SUS):*
    - Scenario 1: Conversational 76.00 (18.94) vs. Graphical 77.25 (15.28)
    - Scenario 2: Conversational 76.63 (16.63) vs. Graphical 65.25 (23.91)
  - *Readability:*
    - Scenario 1: Conversational 4.50 (0.95) vs. Graphical 3.40 (1.14)
    - Scenario 2: Conversational 4.45 (0.76) vs. Graphical 3.20 (1.54)
  - *Usefulness:*
    - Scenario 1: Conversational 4.50 (0.61) vs. Graphical 3.65 (0.99)
    - Scenario 2: Conversational 4.30 (0.80) vs. Graphical 2.95 (1.23)
  - *Overall Satisfaction:*
    - Scenario 1: Conversational 4.15 (0.88) vs. Graphical 3.45 (1.00)
    - Scenario 2: Conversational 4.10 (1.07) vs. Graphical 2.85 (1.14)

### Limitations & Reporting Inconsistencies
- **Limitations:** System restricted to ACL Anthology domain; reliance on synthetic training data for topic classification; participants initially struggled with the rigid three-phase structure, backtracking, and inability to engage in free-form, unconstrained chat.
- **Inconsistencies:**
  - In Table 2 (page 12), the second scenario header is mistakenly labeled "Description of Scenario 1" instead of Scenario 2.
  - Section 4.2 text states participants were given "approximately 10 minutes", whereas Table 2 scenario instructions state participants had "up to 8 minutes".

---

[Wu25]:
### Paper Identification & Metadata
* **Exact Title:** PaperAsk: A Benchmark for Reliability Evaluation of LLMs in Paper Search and Reading
* **Authors:** Yutao Wu, Xiao Liu, Yunhao Feng, Jiale Ding, Xingjun Ma (corresponding author)
* **Publication/Preprint Status & Date:** arXiv preprint, arXiv:2510.22242v1 [cs.IR], published 25 October 2025. No formal journal/conference DOI printed.
* **Affiliations:** Deakin University (Yutao Wu, Xiao Liu); Fudan University (Yunhao Feng, Jiale Ding, Xingjun Ma).
* **Vendor Involvement & Funding:** None disclosed in the text.

---

### Evaluation Setup & Systems Tested
* **Nature of Evaluation:** Independent evaluation of commercial LLM products using the authors' newly proposed **PaperAsk** benchmark.
* **Systems Tested:**
  * Web-interface commercial LLMs: ChatGPT (GPT-4o, GPT-5 with web search enabled) and Google Gemini 2.5 Flash (Google Search grounding enabled).
  * API/Ablation baseline models: GPT-4o, GPT-5 (minimal and extended reasoning budgets), and a fine-tuned Llama-3.1-8B-Instruct classifier.
* **Benchmark Design & Sample Sizes (840 total test cases; Table 1, p. 4):**
  1. *Citation Retrieval (300 cases):* Queries requesting $n \in \{3, 5, 10\}$ paper BibTeX entries from a pool of 1,000 arXiv computer science papers (2022–2025). Ground truth: official arXiv BibTeX.
  2. *Content Extraction (140 cases):* Single-paper queries targeting 5 fields (last sentence of introduction, figure/table counts, figure/table captions) across open-access papers. Ground truth: human-annotated text.
  3. *Open-Domain QA (100 cases):* Topic discovery queries derived from PaSa benchmark topics with temporal arXiv constraints. Ground truth: expert-validated paper lists.
  4. *Claim Verification (300 cases):* Multi-claim queries ($n \in \{3, 5, 10\}$ claim-paper pairs) evaluated as supported/refuted.

---

### Key Findings & Exact Metrics
Table 2 summarizes the failure rates across all four PaperAsk tasks for commercial web-deployed models:

The table reports failure rates (percentage, lower is better) across the four core tasks and multiple query sizes ($n \in \{3, 5, 10\}$) for GPT-4o, GPT-5, and Gemini 2.5 Flash, demonstrating high failure rates across all models in realistic web deployments.
[REGION: page=5, bbox=105,217,358,781]

* **Citation Retrieval (Table 2, p. 5):** Multi-paper queries at $n=10$ yielded failure rates of **98%** (GPT-4o), **78%** (GPT-5), and **48%** (Gemini 2.5 Flash). ChatGPT predominantly failed via incomplete responses/refusal, whereas Gemini fabricated non-matching arXiv IDs.
* **Content Extraction (Table 2, p. 5):** Failure rates reached **84.28%** (GPT-4o), **72.86%** (GPT-5), and **91.42%** (Gemini 2.5 Flash), frequently substituting abstract text for requested introduction sentences.
* **Open-Domain QA Discovery (Table 2, p. 5; Table 5, p. 6):** Failure rates were **73%** (GPT-4o), **80%** (GPT-5), and **68%** (Gemini 2.5 Flash). Models missed over 60% of target literature (Recall: 32.5% GPT-4o, 33.33% GPT-5, 38.0% Gemini; F1: 0.20–0.32).
* **Claim Verification Web vs. API (Table 8, p. 7):** At $n=3$, web-based failure rates were **18%** (GPT-4o), **12%** (GPT-5), and **14%** (Gemini 2.5 Flash), dropping sharply to **3%**, **1%**, and **3%** when providing full text directly via API.

---

### Limitations & Reporting Inconsistencies
* **Limitations:** Excludes paywalled literature; evaluates atomic retrieval and verification operations rather than high-level synthesis; subject to proprietary black-box changes in commercial web search.
* **Inconsistencies:**
  * *Discipline discrepancy:* Section 3.1.2 (p. 3) lists disciplines as physics, biology, mathematics, chemistry, medicine, economics, and computer science; Figure 2 (p. 3) displays Biology, Chemistry, Environment, Materials, Medicine, Physics, and Computer Science.
  * *Claimed failure ranges:* The Abstract (p. 1) states citation retrieval fails in "48–98% of multi-reference queries," but at $n=3$ and $n=5$, failure rates range between 2% and 26% (Table 2, p. 5); 48–98% only applies to $n=10$.
  * *Discrepancy in verification gap:* Section 2 (p. 2) reports a failure gap between web and API of "9–15 percentage points," while Section 4.7 (p. 7) reports "a 9-17 percentage point improvement."

---

[Ben26c]:
Here is the structured summary for the evidence wiki based on the provided document:

### Bibliographic Details & Metadata
- **Exact Title:** BibliZap: An exploratory evaluation of an automated multi-level citation searching tool for systematic and rapid reviews
- **Authors:** Raphaël Bentegeac, Bastien Le Guellec, Victor Leblanc, Rémi Lenain, Luc Dauchet, Victoria Gauthier, Erwin Gerard, Emmanuel Chazard, Philippe Amouyel, Estelle Aymes, Aghilès Hamroun
- **Publication Status & Venue:** Published research article in *Research Synthesis Methods* (2026), 00: 1–14
- **Dates & DOI:** Received: 23 June 2025; Revised: 2 February 2026; Accepted: 3 February 2026. DOI: [10.1017/rsm.2026.10079](https://doi.org/10.1017/rsm.2026.10079)
- **Affiliations:** Lille University Hospital; Pasteur Institute of Lille; Lille 2 University of Health and Law; Inserm; Hauts-de-France (France)
- **Vendor Involvement & Funding:** No specific funding received. Lens.org provided free API access without study involvement. The authors declare no competing interests.
- **Evaluation Type:** Authors’ own benchmark (the tool was developed and evaluated by the study authors, not an independent product evaluation).

---

### Systems, Study Design & Reference Standard
- **Systems/Versions Tested:** BibliZap (implemented in Rust, leveraging Lens.org citation data; default depth = 2, bidirectional, output capped at 10,000 records) compared against/combined with PubMed (Best Match ranking).
- **Design & Sample:** Retrospective evaluation across 66 published systematic reviews (SRs) in six general medicine journals (2012–2021), comprising 2,675 included single references (from an initial 70 SRs; 4 excluded due to PubMed query execution retrieving zero results).
- **Reference Standard:** Manually extracted gold-standard included articles from each SR that possessed a PubMed ID.
- **Strategies Evaluated:**
  1. *Approach 1:* Full PubMed screening
  2. *Approach 2:* PubMed + top 500 BibliZap results
  3. *Approach 3:* PubMed + full BibliZap output
  4. *Approach 4:* Early stop (BibliZap seeded with 1st PubMed relevant article)
  5. *Approach 5:* Late stop (BibliZap seeded with first 3 PubMed relevant articles)

---

### Key Exact Metrics & Findings
- **Mean Sensitivity (Recall):**
  - PubMed alone (Approach 1): 75% (95% CI 68–81) (p. 6)
  - PubMed + BibliZap top 500 (Approach 2): 91% (95% CI 88–94) (p. 6)
  - PubMed + BibliZap full (Approach 3): 97% (95% CI 95–98) (p. 6)
  - PubMed early stop (Approach 4): 75% (95% CI 68–81); late stop (Approach 5): 90% (95% CI 86–93) (p. 6)
- **Screening Burden & Precision:**
  - PubMed alone: median 1,889 screened; mean precision 2.1% (95% CI 1.5–2.7) (p. 6)
  - PubMed + BibliZap top 500: median 2,388 screened; mean precision 1.5% (95% CI 1.1–1.9) (p. 6)
  - PubMed + BibliZap full: median 8,422 screened (median 6,450 additional records added by BibliZap); mean precision 0.4% (95% CI 0.3–0.5) (p. 6)
- **Recovery of Missed Studies:**
  - Full BibliZap recovered a median of 3 additional gold-standard articles missed by PubMed per review (range: 1–78) (p. 6).
  - Among PubMed-missed articles, 56% were recovered within the top 500 and 73% within the top 2,000 BibliZap-ranked records (p. 8).

---

### Limitations & Reporting Inconsistencies
- **Limitations:** Retrospective design; gold standard restricted to PMID-bearing included articles; comparison restricted solely to PubMed queries rather than full multi-database searches; depth-1 vs. depth-2 was not formally compared; impact on review conclusions was not evaluated.
- **Reporting Inconsistencies:** The text on p. 5 refers to Figure 2 for the web interface and Figure 3 for the output table, but the figure printed on p. 4 is titled "Figure 1. BibliZap web application input interface," shifting subsequent figure numbering between the text mentions and captions. Additionally, on page 6, the number of screened articles for Approach 4 is reported as "6,126 articles screened" without explicitly indicating whether this is a mean or median.

---

[Kha25e]:
### Overview & Bibliographic Details
* **Exact Title:** NeuroLit Navigator: A Neurosymbolic Approach to Scholarly Article Searches for Systematic Reviews
* **Authors:** Vedant Khandelwal, Kaushik Roy, Valerie Lookingbill, Ritvik Garimella, Harshul Surana, Heather Heckman, Amit Sheth
* **Status, Date, Venue, & DOI:** arXiv preprint (`arXiv:2503.00278v1 [cs.CY]`), dated 1 Mar 2025. Printed copyright indicates Association for the Advancement of Artificial Intelligence (AAAI) 2025. No DOI printed.
* **Affiliations & Funding:** Artificial Intelligence Institute and Library Sciences, University of South Carolina. No commercial vendor involvement. Supported by NSF Award 2335967 (*EAGER: Knowledge-guided neurosymbolic AI*).

---

### Systems Tested, Design, & Evaluation
* **Nature of Evaluation:** System authors’ own benchmark and internal user study; not an independent evaluation.
* **Systems Compared:** NeuroLit Navigator vs. GEAR-Up, Consensus, Scite, and Perplexity (tested as of September 13, 2024).
* **Underlying Components Evaluated:** ClinicalBERT, SciSpacy (`en_core_sci_lg`), PubMed Entrez API, and five embedding models for re-ranking: MPNet, Distill-Bert, SPECTER, PubMedBERT, and MedCPT.
* **Design & Reference Standard:** Real-time evaluation of the first-iteration literature search for systematic reviews (SRs). Inputs consisted of a research query and sentinel articles. Librarians and domain experts evaluated retrieved candidate abstracts (top $k=5$) against sentinel articles using a structured feedback form covering core SR criteria (e.g., population, intervention, outcomes).

---

### Key Exact Metrics
* **System Relevance Comparison (Page 7, Table 1):**
  * Consensus: **38%** (Reproducibility: No, Interpretability: No, Controlled Vocabulary: No)
  * NeuroLit Navigator: **36%** (Reproducibility: Yes, Interpretability: Yes, Controlled Vocabulary: Yes)
  * Scite: **33%**
  * Perplexity: **33%**
  * GEAR-Up: **26.6%**
* **Embedding Model Relevance (Page 7, Section 7; Page 10, Appendix E):** MPNet achieved the highest relevance at **36%**, followed by BertDistill (**28%**), SPECTER (**24%**), PubmedBert (**20%**), and MedCPT (**4%**).
* **Efficiency Impact (Page 1, Abstract; Page 7, Section 8):** Authors report the system reduced initial literature search time by **90%** across testing by over a dozen academic librarians.

Table 1 summarizes the performance of NeuroLit Navigator against baseline and LLM-based retrieval systems across relevance, reproducibility, interpretability, and use of controlled vocabulary:
[REGION: page=7, bbox=305,515,445,915]

---

### Limitations & Reporting Inconsistencies
* **Reporting Inconsistency:** The caption for Table 1 states that NeuroLit Navigator *“outperforms other systems in relevance,”* but the table data and text directly contradict this by reporting Consensus at **38%** and NeuroLit Navigator at **36%**. Model naming also varies between sections (e.g., *PubMedBERT* vs. *PubmedBert*, *Distill-Bert* vs. *BertDistill*).
* **Limitations:**
  * The tool only addresses the initial retrieval iteration, still requiring human screening and manual input in subsequent review phases.
  * Baseline retrieval quality remains modest (36% expert-judged relevance).
  * Structured knowledge graphs (MeSH/UMLS) struggle to capture emerging or rapidly evolving research concepts not yet indexed.

---

[Du26]:
### Bibliographic Identification
- **Exact Title:** Towards Recursive Self-Evolving Agentic Literature Retrieval
- **Authors:** Yuwen Du, Tian Jin, Jing Kang, Xianghe Pang, Jingyi Chai, Tingjia Miao, Fenyi Liu, WenHao Wang, Sikai Yao, Yuzhi Zhang, Siheng Chen (*Equal contribution: Yuwen Du, Tian Jin; Corresponding authors: Yuwen Du, Siheng Chen)
- **Publication / Preprint Status:** arXiv preprint (arXiv:2605.14306v3 [cs.IR])
- **Date / Venue / DOI:** 27 Jun 2026; no DOI or journal venue printed.
- **Affiliations & Funding:** Shanghai Jiao Tong University, SciLand (industry/vendor affiliation), and Zhejiang University. Funding sources are not stated.

---

### Systems Evaluated & Evaluation Nature
- **Benchmark Type:** The evaluation is conducted on **PaSaMaster-Bench**, an in-house benchmark designed and curated by the paper’s authors, rather than an independent third-party evaluation.
- **Tested Systems / Versions:**
  - *Proposed system:* PaSaMaster (Recursive Self-Evolving Agentic Retrieval)
  - *Lexical retrieval:* Google Scholar
  - *Semantic retrieval:* OpenScholar, Bohrium Science Navigator
  - *Tool-assisted generative LLMs:* DeepSeek-v3.2, Kimi-K2.5, MiniMax-M2.7, GLM-5, Gemini-3.1-pro, GPT-5.2
  - *Fixed-pipeline agentic retrieval:* Google Scholar Labs

---

### Study Design & Reference Standard
- **Sample:** 244 multi-constraint, natural-language search tasks across 38 scientific disciplines.
- **Reference Standard:** Ground truth ($P^*$) established by domain experts who constructed candidate pools via multi-channel searches (web LLMs, native engine, web search) and annotated each paper item-by-item against explicit checklists (covering topic, methodology, application context, venue/date, and exclusion criteria).
- **Protocol:** Top-$K$ retrieval evaluated at $K=20$.

---

### Key Exact Metrics

Performance comparison of PaSaMaster against lexical, semantic, generative LLM, and fixed-pipeline baselines across NDCG@20, Recall@20, Precision@20, F1-score@20, source hallucination rate (%), and per-query cost ($):
[REGION: page=7, bbox=[86,168,382,780]]

- **PaSaMaster:** NDCG@20 = 39.52, Recall@20 = 33.24, Precision@20 = 23.46, F1-score@20 = 23.00, Hallucination = 0%, Cost = $0.05 (Page 7, Table 2).
- **Google Scholar:** NDCG@20 = 2.07, Recall@20 = 1.69, Precision@20 = 1.48, F1-score@20 = 1.39, Hallucination = 0% (Page 7, Table 2).
- **GPT-5.2:** NDCG@20 = 31.59, Recall@20 = 25.32, Precision@20 = 16.82, F1-score@20 = 16.69, Hallucination = 5.65%, Cost = $6.06 (Page 7, Table 2).
- **GLM-5:** F1-score@20 = 18.18, Hallucination = 21.64%, Cost = $0.56 (Page 7, Table 2).
- **MiniMax-M2.7:** Hallucination = 32.66% (highest among tested models) (Page 7, Table 2).

---

### Limitations & Reporting Inconsistencies
- **Reported Limitations (Section 2, Page 11):**
  1. Benchmark target lists are expert-curated and subject to annotator search horizons and disciplinary backgrounds.
  2. Evaluates top-ranked paper retrieval only, not downstream paper writing or synthesis.
  3. Does not reconstruct field evolution or formulate new hypotheses.
  4. Scoring remains susceptible to potential model, corpus, and checklist biases.
- **Reporting Inconsistencies:**
  - Citation [5] is listed as "Introducing GPT-5.4 (2026)" in the references (p. 19), but labeled as "GPT-5.2" in the main text and Table 2.
  - Citation [23] is titled "GLM-4.5" in the references (p. 22), but reported as "GLM-5" in the text and tables.

---

[Haz26]:
### Exact Title, Authors, Status, Date & Affiliations
* **Title:** Structurally-bounded Agentic Graph Exploration for Evidence-Grounded Scholarly DeepSearch
* **Authors:** Rima Hazra\* (♠♡), Sayan Layek\* (♢), Somnath Banerjee (♣), Soumen Chakrabarti (†), Animesh Mukherjee (♢) (\*equal contribution).
* **Publication/Preprint Status & Date:** arXiv preprint (`arXiv:2608.24809v1 [cs.CL] 25 Aug 2026`).
* **Venue/DOI:** Not printed (only arXiv ID shown).
* **Affiliations:** ♠National University of Singapore; ♡TCG CREST; ♢Indian Institute of Technology Kharagpur; ♣Singapore Institute of Technology; †Indian Institute of Technology Bombay. Vendor involvement/funding is not stated.

---

### Systems & Versions Evaluated
* **Proposed System:** $\text{\textsc{Crase}}$ (Citation-guided Research Agent for Scholarly Exploration), evaluated in variants: `Crase-Llama-PPR`, `Crase-Llama-SALSA`, `Crase-Qwen-PPR`, `Crase-Qwen-SALSA`, and `Recency` baseline.
  * Models utilized: `Qwen2.5-32B-Instruct` (planning and claim extraction), `Meta-Llama-3-70B-Instruct` (claim extraction), and fine-tuned `Qwen2.5-3B-Instruct` (claim entailment).
* **Baselines Tested:**
  * `DeepResearch-GPT` (OpenAI `o4-mini` with `BAAI/bge-base-en-v1.5`)
  * `DeepResearch-Claude` (Anthropic `claude-sonnet-5` with `BAAI/bge-base-en-v1.5`)
  * `Spector2-Deepwalk` (`SPECTER` / `SciRepEval` + `DeepWalk`)

---

### Study Design, Sample & Reference Standard
* **Corpus:** ~500K arXiv papers (Jan 2016 – Jul 2026) across 8 AI/ML categories.
* **Evaluation Sets:**
  * *LitSearch:* Manual ACL (114 queries) and ICLR (60 queries) splits filtered to corpus (independent existing benchmark).
  * *arXiv set:* Authors' self-constructed benchmark using 98 recent arXiv papers (Nov 2025 – Feb 2026) where paper reference lists serve as ground truth.
  * *Human Audit Sample:* 50 citation edges assessed by 3 domain experts.

---

### Key Exact Metrics

Below are the primary retrieval and efficiency results comparing $\text{\textsc{Crase}}$ to baseline systems:

The table shows comparative performance across ACL, ICLR, and arXiv splits, highlighting superior recall and precision for $\text{\textsc{Crase}}$ on conference benchmarks:
[REGION: page=6, bbox=68,127,272,831]

Resource consumption, latency, and R@50 on ICLR comparing agentic baselines against $\text{\textsc{Crase}}$:
[REGION: page=7, bbox=274,520,344,912]

* **ACL Retrieval:** `Crase-Llama-PPR` achieved **Recall@50 = 0.3848** and **MAP@50 = 0.0730** vs. `DeepResearch-GPT` (0.2294 / 0.0279) and `Spector2-Deepwalk` (0.2629 / 0.0380) (Page 6, Table 1).
* **ICLR Retrieval:** `Crase-Llama-PPR` achieved **Recall@50 = 0.3720** and **MAP@50 = 0.1076** vs. `DeepResearch-GPT` (0.1220 / 0.0155) and `Spector2-Deepwalk` (0.2012 / 0.0361) (Page 6, Table 1).
* **Resource & Cost (ICLR):** `Crase-Llama-PPR` required **5 calls**, **235K tokens**, **104s**, and **$0.37/query** vs. `DeepResearch-GPT` (18 calls, 620K tokens, 272s, $1.76) and `DeepResearch-Claude` (17 calls, 560K tokens, 249s, $2.06) (Page 7, Table 4).
* **Human Audit:** 84.0% agreement with expert majority, 88.0% retained-edge precision, and 80.0% pruned-edge correctness (Fleiss’ $\kappa = 0.71$) (Page 8, Table 5).

---

### Benchmark Nature, Inconsistencies & Limitations
* **Benchmark Distinction:** LitSearch is an established, independent third-party benchmark; the arXiv test set is the authors' own reference-based benchmark.
* **Reporting Inconsistencies:**
  * In Table 4, `Crase-Llama-PPR` lists ICLR R@50 as `0.3659` (and text quotes `0.3659`), but Table 1 reports `0.3720` for the same metric/variant.
  * arXiv dates in the corpus reach July 2026, alongside an arXiv preprint identifier date of 25 Aug 2026.
* **Limitations Noted:**
  > *"A relevant paper outside the citation neighborhood induced by the initial seeds cannot be recovered through later query reformulation."*
  Complete failure occurs under random off-manifold seeds (Recall collapses to 0; Page 15–17).

---

[Wei24]:
### Bibliographic Information
- **Title:** DocReLM: Mastering Document Retrieval with Language Model
- **Authors:** Gengchen Wei, Xinle Pang, Tianning Zhang, Yu Sun, Xun Qian, Chen Lin, Han-Sen Zhong, Wanli Ouyang
- **Status & Date:** arXiv preprint (arXiv:2405.11461v1 [cs.IR]), submitted 19 May 2024. No printed DOI or journal/conference venue.
- **Affiliations:** Shanghai Artificial Intelligence Laboratory; Fudan University; Harbin Institute of Technology; The Chinese University of Hong Kong; Shanghai Jiaotong University; University of Oxford.
- **Funding & Disclosures:** Supported by National Key R&D Program of China (NO.2022ZD0160100) and Shanghai Committee of Science and Technology (Grant No. 21DZ1100100). No corporate vendor sponsorship reported.

### Systems Evaluated
- **Proposed System:** DocReLM, comprising:
  - Retriever: `jina-embedding-v2-base` fine-tuned with contrastive learning.
  - Reranker: `XLM-RoBERTa-large` fine-tuned using Localized Contrastive Estimation (LCE).
  - Reference Extractor: `internLM` (prompted to select up to 3 cited references from the top 10 reranked papers).
  - Training Data Generator: `vicuna-7b-v1.5-16k` generating pseudo-queries from unarXive papers.
- **Baselines:** BM25, OpenAI `text-embedding-ada-002`, base `jina-base-v2`, `bge-reranker-large`, `Cohere rerank-english-v2.0`, and Google Scholar.

### Design, Sample, & Benchmark Nature
- **Evaluation Type:** Authors' own custom benchmark (not an independent third-party evaluation).
- **Corpus & Queries:** Drawn from unarXive in two tracks:
  - *Computer Vision (CV):* 37,390 papers; 204 researcher-created test queries (with survey claims as reference ground truth); 1.1M synthetic training pairs.
  - *Quantum Physics (QP):* 56,927 papers; 301 researcher-created test queries; 2.8M synthetic training pairs.

### Key Metrics & Results
- **Retriever Performance (p. 6, Table 1):**
  - CV Top-10: DocReLM-retriever 39.22% vs. `text-embedding-ada-002` 20.09%, `jina-base-v2` 18.14%, BM25 3.92%.
  - QP Top-10: DocReLM-retriever 15.95% vs. `jina-base-v2` 14.62%, `text-embedding-ada-002` 13.29%, BM25 1.99%.
- **Reranker Performance (p. 6, Table 2):**
  - CV Top-10: DocReLM-reranker 44.61% vs. `bge-reranker-large` 41.67%, Cohere 40.20%, without rerank 39.22%.
  - QP Top-10: Cohere achieved 21.93% vs. DocReLM-reranker 19.93%.
- **Reference Extraction Impact (p. 6, Table 3):**
  - QP Top-10: internLM reached 36.21% (up from 19.93% without extraction); Top-5 reached 26.91% (up from 17.28%).
  - CV Top-5: internLM reached 38.73% (up from 37.75%); Top-20 reached 50.00% (up from 47.06%).

### Limitations & Reporting Inconsistencies
- **Benchmark Specificity:** The test sets are limited to two specialized arXiv domains and contain relatively small query sets (204 and 301 queries).
- **Reporting Discrepancies:**
  - *Google Scholar Baselines:* The abstract reports Google Scholar top-10 accuracy as 15.69% (CV) and 12.96% (QP). However, the bar charts in Figure 1 (p. 2) display values labeled ~0.172 for CV and ~0.196 for QP.
  - *Top-10 Drop in Table 3:* In Table 3 (CV), adding internLM drops top-10 accuracy from 44.61% to 44.12%, but the narrative text mentions only the gains in top-5 and top-20 without addressing this decrease.

---

### Relevant Figure Reference

Bar charts illustrating the comparative top-1, top-5, top-10, and top-20 retrieval accuracy of DocReLM against BM25, Google Scholar, and OpenAI ada002 across both the computer vision and quantum physics benchmark tracks:
[REGION: page=2, bbox=542,135,745,865]

Region format: page is 1-indexed; bbox=top,left,bottom,right, normalized 0-1000 from top-left.
