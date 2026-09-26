> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**

# Academic search prototypes and benchmarks

**Evidence:** 13 sources; 2021–2026; 4 peer-reviewed studies, 9 preprints

## Scope

Developer and independent benchmarks of academic-search prototypes, search agents and interfaces. Distinguish component metrics, static corpora and native product evaluations.

## Overview

This tool page groups 13 claims and 13 source records that evaluate or directly contextualize Academic search prototypes and benchmarks.

Cross-tool claims are repeated where relevant, but the evidence shown below is limited to the source records assigned to this tool.

## Key claims

### [A developer user study found scenario-dependent usability differences between conversational and graphical scholarly-search interfaces, without measuring exhaustive retrieval quality.](../claims/assistant-029.md)

**Status:** supported

- **supports** — [Conversational Exploratory Search of Scholarly Publications Using Knowledge Graphs](../evidence/schneider-2024-conversational-search.md) (peer-reviewed-study); locator: User study and Table 1, PDF pp. 6–8. Forty nonexperts: scenario-one SUS conversational 76 versus graphical 77.25; scenario-two 76.63 versus 65.25. Topic-classifier F1 .95 is a separate component result, not retrieval precision or recall.

### [An early COVID-19 evaluation found two commercial deep-learning search systems below the strongest academic TREC-COVID submissions on top-rank relevance metrics.](../claims/assistant-028.md)

**Status:** supported

- **supports** — [An evaluation of two commercial deep learning-based information retrieval systems for COVID-19 literature](../evidence/soni-2021-covid-search.md) (peer-reviewed-study); locator: Evaluation setup and Table 2, PDF pp. 2–4. Across thirty topics, best Amazon configuration precision@10 .6400, Google COVID-19 Research Explorer .5600, best academic submission .7133. Historical snapshot with additional pooled judgments and common cutoffs; no inference about current engines or exhaustive recall.

### [LitSearch documents low target-paper recovery for commercial searches on an 80-query specific-question subset; its fixed-corpus benchmark is not directly comparable to commercial engine coverage.](../claims/assistant-016.md)

**Status:** supported

- **supports** — [LitSearch: A Retrieval Benchmark for Scientific Literature Search](../evidence/ajith-2024-litsearch.md) (peer-reviewed-study); locator: Section 5.3 and Table 7, PDF p. 7. Recall@5 for inline/author queries: Google Scholar 20.5%/17.5%, Elicit 23.1%/17.5%, Google Search 23.1%/62.5%. Each type has 40 queries; ML/NLP benchmark and different search corpora limit generalization.

### [PaSa developers report higher target-paper recovery than selected search baselines on their own AI-domain benchmarks, with limited independent validation and differing baseline conditions.](../claims/assistant-022.md)

**Status:** provisional

- **supports** — [PaSa: An LLM Agent for Comprehensive Academic Paper Search](../evidence/he-2025-pasa.md) (peer-reviewed-study); locator: RealScholarQuery methods and Table 5, PDF pp. 4, 8. On 50 expert-labeled AI queries, PaSa-7b precision .5146, recall .6111, recall@20 .5798; Google with GPT-4o recall@20 .2020. This is a developer benchmark with pooled candidate judgments, not evidence of universal superiority.

### [A literature-search preprint demonstrates that citation-list recovery and LLM-judged semantic relevance can yield different rankings; neither is an exhaustive relevance gold standard.](../claims/assistant-026.md)

**Status:** provisional

- **supports** — [Rethinking Literature Search Evaluation: Deep Research Helps, and Human Citation Lists Are Not a Ground Truth](../evidence/sahu-2026-search-evaluation.md) (preprint); locator: Tables 1 and 3, PDF pp. 3–5. On 9,204 query-reference pairs from 250 computer-science papers, Qwen-based deep research recall@100 22.2% and recall@1000 51.9%, versus .3%/1.9% without deep research. LLM-judge relevance favored reranked candidates over reference lists, but that does not establish that original citations are wrong.

### [AI-generated academic search overviews showed factual-quality limitations and no statistically significant confirmatory workload or satisfaction benefit in one 30-user interface experiment.](../claims/assistant-020.md)

**Status:** provisional

- **supports** — [AI Overviews in Academic Search: Evaluating AI-generated Summaries of Search Results in a Domain-specific Search Engine](../evidence/schott-2026-ai-overviews.md) (preprint); locator: Summary evaluation and user study, PDF pp. 5–8, Tables 1–2. On ten queries, five GPT-4o-mini versus two Llama-4-Scout summaries were judged correct. After Holm correction, confirmatory workload/usefulness/satisfaction/confidence tests were not significant; exploratory mental-demand result p=.040 is not a confirmed overall benefit. Developer evaluation; preprint.

### [Crase developers report stronger reference recovery for bounded graph exploration on selected AI-domain benchmarks, with seed-neighborhood and reporting limitations.](../claims/assistant-034.md)

**Status:** provisional

- **supports** — [Structurally-bounded Agentic Graph Exploration for Evidence-Grounded Scholarly DeepSearch](../evidence/hazra-2026-graph-search.md) (preprint); locator: Tables 1 and 4, PDF pp. 6–7. Table 1 Crase Llama-PPR recall@50 ACL .3848/ICLR .3720 versus deep-research GPT .2294/.1220; Table 4 corresponding ICLR value .3659 conflicts. Preserve both. Static AI corpus and seed-bounded traversal are not an open-web exhaustive search.

### [DocReLM developers report gains on specialized survey-reference retrieval tasks; their top-k accuracy is not exhaustive systematic-review recall.](../claims/assistant-035.md)

**Status:** provisional

- **supports** — [DocReLM: Mastering Document Retrieval with Language Model](../evidence/wei-2024-docrelm.md) (preprint); locator: Tables 1 and 3, PDF p. 6. Top-ten accuracy 39.22% for computer vision and 15.95% for quantum physics; quantum-physics reference-extraction accuracy 36.21% versus 19.93% without reranking. Abstract and plotted Google Scholar baselines disagree; no resolved comparative value inferred.

### [PaperAsk reports reliability problems that vary by task and requested citation count; whole-response failure rates are not per-citation hallucination rates.](../claims/assistant-030.md)

**Status:** provisional

- **supports** — [PaperAsk: A Benchmark for Reliability Evaluation of LLMs in Paper Search and Reading](../evidence/wu-2025-paperask.md) (preprint); locator: Benchmark and Tables 2, 5, PDF pp. 3–6. For ten-reference requests, whole-response citation failures GPT-4o 98%, GPT-5 78%, Gemini 48%. Discovery recalls 32.5%, 33.33%, 38%. Benchmark cases differ by task and are not a native academic-engine comparison; verified downloaded version is a preprint.

### [PaSaMaster developers report a quantitative Scholar Labs comparison on a multidisciplinary benchmark; it is not independent validation of either system.](../claims/assistant-033.md)

**Status:** provisional

- **supports** — [Towards Recursive Self-Evolving Agentic Literature Retrieval](../evidence/du-2026-recursive-retrieval.md) (preprint); locator: PaSaMaster-Bench methods and Table 2, PDF pp. 5–7. 244 queries across 38 disciplines, pooled expert-labeled targets. Top-20 Google Scholar Labs recall 29.01%, precision 18.79%, F1 18.87%, NDCG 30.54%; PaSaMaster 33.24%, 23.46%, 23.00%, 39.52%. Both reported zero source hallucination in this sample, not guaranteed absence. Does supply a formal Scholar Labs benchmark beyond the launch note.

### [ScholarGym illustrates agent recall–precision tradeoffs and poorer performance on a deliberately difficult subset, not native search-product effectiveness.](../claims/assistant-027.md)

**Status:** provisional

- **supports** — [ScholarGym: Benchmarking Large Language Model Capabilities in the Information-Gathering Stage of Deep Research](../evidence/shen-2026-scholargym.md) (preprint); locator: Benchmark construction and Table 3, PDF pp. 3–6. On the fast subset GPT-5.2 recall .837, precision .305, F1 .447; Gemini recall .950, precision .199, F1 .329. Hard subset selected by model failures; GPT-5.2 F1 .081. Static arXiv environment and model-derived task selection constrain generalization.

### [The NeuroLit developer preprint provides a small, incompletely documented comparison that does not establish superiority over Consensus or controlled time savings.](../claims/assistant-032.md)

**Status:** uncertain

- **qualifies** — [NeuroLit Navigator: A Neurosymbolic Approach to Scholarly Article Searches for Systematic Reviews](../evidence/khandelwal-2025-neurolit.md) (preprint); locator: Table 1 and evaluation text, PDF pp. 6–8. Table 1 Consensus 38%, NeuroLit 36%, Scite and Perplexity 33%, GEAR 26.6%. Broad outperforming language conflicts with this table; top-five sentinel criteria and unclear denominators limit interpretation. Asserted time savings are not promoted as a measured controlled effect.

### [WisPaper developers report high criterion-matching accuracy but substantially lower end-to-end retrieval recall; these component and system metrics should not be conflated.](../claims/assistant-023.md)

**Status:** provisional

- **supports** — [WisPaper: Your AI Scholar Search Engine](../evidence/ju-2025-wispaper.md) (preprint); locator: Tables 2–3 and Figure 4, PDF pp. 8–10. WisModel criterion matching 93.70% versus Gemini3-Pro 73.23%; TaxoBench end-to-end WisPaper recall 22.26% versus O3 20.92%. TaxoBench is restricted to 72 computer-science surveys and shares authors with the evaluation; not independent validation.

## Connected concepts

- [Recall and sensitivity](../concepts/recall-and-sensitivity.md)
- [Precision](../concepts/precision.md)
- [Reference standards and ground truth](../concepts/reference-standards.md)
- [Human-in-the-loop verification](../concepts/human-in-the-loop-verification.md)
- [Reproducibility and output stability](../concepts/reproducibility-and-stability.md)

## Source records

### Peer-reviewed studies

- [PaSa: An LLM Agent for Comprehensive Academic Paper Search](../evidence/he-2025-pasa.md)
- [Conversational Exploratory Search of Scholarly Publications Using Knowledge Graphs](../evidence/schneider-2024-conversational-search.md)
- [LitSearch: A Retrieval Benchmark for Scientific Literature Search](../evidence/ajith-2024-litsearch.md)
- [An evaluation of two commercial deep learning-based information retrieval systems for COVID-19 literature](../evidence/soni-2021-covid-search.md)

### Preprints and unverified manuscripts

- [AI Overviews in Academic Search: Evaluating AI-generated Summaries of Search Results in a Domain-specific Search Engine](../evidence/schott-2026-ai-overviews.md) — arXiv preprint; downloaded manuscript carries an ASIS&T November 2026 conference header
- [Rethinking Literature Search Evaluation: Deep Research Helps, and Human Citation Lists Are Not a Ground Truth](../evidence/sahu-2026-search-evaluation.md) — arXiv:2605.29234v1, May 28, 2026
- [ScholarGym: Benchmarking Large Language Model Capabilities in the Information-Gathering Stage of Deep Research](../evidence/shen-2026-scholargym.md) — arXiv:2601.21654v3, February 17, 2026
- [Structurally-bounded Agentic Graph Exploration for Evidence-Grounded Scholarly DeepSearch](../evidence/hazra-2026-graph-search.md) — arXiv:2608.24809v1, August 25, 2026
- [Towards Recursive Self-Evolving Agentic Literature Retrieval](../evidence/du-2026-recursive-retrieval.md) — arXiv:2605.14306v3, June 27, 2026
- [NeuroLit Navigator: A Neurosymbolic Approach to Scholarly Article Searches for Systematic Reviews](../evidence/khandelwal-2025-neurolit.md) — arXiv:2503.00278v1, March 1, 2025; printed AAAI copyright does not establish venue here
- [PaperAsk: A Benchmark for Reliability Evaluation of LLMs in Paper Search and Reading](../evidence/wu-2025-paperask.md) — Downloaded arXiv:2510.22242v1, October 25, 2025; later conference status not verified here
- [WisPaper: Your AI Scholar Search Engine](../evidence/ju-2025-wispaper.md) — arXiv:2512.06879v2, February 27, 2026; first posted 2025
- [DocReLM: Mastering Document Retrieval with Language Model](../evidence/wei-2024-docrelm.md) — arXiv:2405.11461v1, May 19, 2024

### Other evidence categories

No vendor, system, experimental, or editorial records are linked.

## Important uncertainties

- [PaSa developers report higher target-paper recovery than selected search baselines on their own AI-domain benchmarks, with limited independent validation and differing baseline conditions.](../claims/assistant-022.md) is marked **provisional**.
- [A literature-search preprint demonstrates that citation-list recovery and LLM-judged semantic relevance can yield different rankings; neither is an exhaustive relevance gold standard.](../claims/assistant-026.md) is marked **provisional**.
- [AI-generated academic search overviews showed factual-quality limitations and no statistically significant confirmatory workload or satisfaction benefit in one 30-user interface experiment.](../claims/assistant-020.md) is marked **provisional**.
- [Crase developers report stronger reference recovery for bounded graph exploration on selected AI-domain benchmarks, with seed-neighborhood and reporting limitations.](../claims/assistant-034.md) is marked **provisional**.
- [DocReLM developers report gains on specialized survey-reference retrieval tasks; their top-k accuracy is not exhaustive systematic-review recall.](../claims/assistant-035.md) is marked **provisional**.
- [PaperAsk reports reliability problems that vary by task and requested citation count; whole-response failure rates are not per-citation hallucination rates.](../claims/assistant-030.md) is marked **provisional**.
- [PaSaMaster developers report a quantitative Scholar Labs comparison on a multidisciplinary benchmark; it is not independent validation of either system.](../claims/assistant-033.md) is marked **provisional**.
- [ScholarGym illustrates agent recall–precision tradeoffs and poorer performance on a deliberately difficult subset, not native search-product effectiveness.](../claims/assistant-027.md) is marked **provisional**.
- [The NeuroLit developer preprint provides a small, incompletely documented comparison that does not establish superiority over Consensus or controlled time savings.](../claims/assistant-032.md) is marked **uncertain**.
- [WisPaper developers report high criterion-matching accuracy but substantially lower end-to-end retrieval recall; these component and system metrics should not be conflated.](../claims/assistant-023.md) is marked **provisional**.

Read the individual source records for study design, scope, and unresolved reporting discrepancies.

**Last reviewed:** 2026-09-27
