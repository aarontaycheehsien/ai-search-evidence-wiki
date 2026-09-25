> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**

# Empirical evaluations of AI research assistants

## Question

What do empirical studies report about the retrieval, relevance, usability, and evidence-extraction performance of AI research assistants and discovery tools?


## Overview

This question groups 6 claims linked to 14 source records.

## Current evidence

The relationships and source categories below come from the structured evidence records. Results are reported in each source's own review setting; this page does not pool them.

## Key claims

### [Elicit has shown higher precision but lower sensitivity than completed evidence-synthesis searches in retrospective comparisons; its output has also varied across repeated searches.](../claims/assistant-001.md)

**Status:** mixed

- **supports** — [Comparison of Elicit AI and Traditional Literature Searching in Evidence Syntheses Using Four Case Studies](../evidence/lau-golder-2025.md) (peer-reviewed-study); locator: Abstract, p. 1; case-study results, PDF pp. 4–6. Across four evidence syntheses, mean sensitivity was 39.5% for Elicit versus 94.5% for original searches, while mean precision was 41.8% versus 7.55%. Elicit also found eligible studies absent from the original searches.
- **qualifies** — [Using artificial intelligence for systematic review: the example of elicit](../evidence/bernard-2025.md) (peer-reviewed-study); locator: Results, PDF pp. 3–4. For one umbrella-review question, repeated runs retrieved 246, 169, and 172 records; Elicit found 3 of 17 included reviews from the prior review and 3 additional eligible reviews. This used an earlier product version and one topic.

### [Independent tool comparisons report different retrieval relevance and coverage profiles across query sets; current evidence does not establish a general-purpose winner over conventional library search.](../claims/assistant-002.md)

**Status:** mixed

- **supports** — [Are AI tools better than traditional tools in literature searching? Evidence from E-commerce research](../evidence/tomczyk-2024.md) (peer-reviewed-study); locator: Methods and Findings, PDF p. 5. For the top eight results across nine e-commerce questions, title/abstract accuracy was 56% for Elicit and 33% for SciSpace, compared with 65% for Scopus and 78% for Web of Science; AI tools also surfaced unique papers.
- **contextual** — [AI-Infused Discovery Environments: Information Retrieval Boon or Overpromised Hype?](../evidence/galbreath-2025.md) (peer-reviewed-study); locator: Abstract, p. 1; results section. Across 103 natural-language queries, the share of top citations judged relevant was similar for Primo Research Assistant and conventional Primo (46.3% vs 45.6%), with limited title overlap.
- **qualifies** — [Navigating Machine-Driven Research Landscapes: A Comparative Approach](../evidence/tranfield-2024.md) (peer-reviewed-study); locator: Preliminary Results, PDF pp. 4–5. In a six-tool comparison across ten STEM subdisciplines, SciSpace had high citation overlap and Elicit retrieved fewer recent materials; abstract relevance scoring was still ongoing, so this is descriptive coverage evidence rather than a completed accuracy comparison.

### [One single-domain study reported high Consensus precision on a specialized tissue-engineering query, while broader comparative studies do not support treating that result as a stable cross-domain performance estimate.](../claims/assistant-003.md)

**Status:** provisional

- **supports** — [Optimizing scholarly literature search: a comparative study of relevance and evidence quality across AI-powered, semantic, and traditional search engines](../evidence/gavgani-2026.md) (peer-reviewed-study); locator: Abstract only; full text not obtained. The abstract reports 86.0% precision and no false drops for the top 50 Consensus results in one tissue-engineering evaluation.
- **contextual** — [Evaluating Eight Retrieval-Augmented Generation (RAG) Large Language Models’ Responses to Clinical Questions: A Comparative Study](../evidence/krump-2026.md) (preprint); locator: medRxiv abstract only. The abstract reports no significant between-tool differences in critical or non-critical concept coverage for 12 generated clinical questions (p=.95 and p=.16), including Consensus, Elicit, SciSpace, and Undermind. This is an unreviewed preprint and the full text was not obtained.
- **contextual** — [Comparative evaluation of artificial intelligence–assisted literature search tools for identifying clinically meaningful evidence in cardiology](../evidence/di-febo-2026.md) (peer-reviewed-study); locator: Abstract, p. 1; Results, PDF pp. 6–8. In four cardiology topics, ChatGPT-5 ranked highest for relevant articles and key references, while Scite ranked lowest. Consensus was included, but the available abstract does not disclose its product-specific point estimate.

### [A small rubric study rated Undermind and paid Elicit highly, but its low interrater agreement makes these ratings preliminary; Undermind’s quantified search-performance claims come from a vendor-authored benchmark.](../claims/assistant-004.md)

**Status:** provisional

- **supports** — [Which AI Tools Work Best for Research? Using Librarian and Student Perspectives to Inform a Rating Rubric](../evidence/patterson-2025.md) (peer-reviewed-study); locator: Methods, PDF pp. 3–4; results and discussion, pp. 5–6. Undermind had a reported mean score of 4.31 and paid Elicit 3.69, but average percent agreement was 21.1% and agreement for Undermind was 54%. Three raters assessed 15 tools; this was a subjective rubric, not a retrieval benchmark.
- **contextual** — [Benchmarking the Undermind Search Assistant](../evidence/hartke-undermind.md) (vendor-documentation); locator: Vendor white paper, PDF pp. 1–3 and 6–10; Tables 1–2 on p. 7. For approximately 300 late-2023 user queries, the report claims roughly tenfold greater relevant-result yield and density than five Google Scholar keyword searches per query, and estimates 97.6% recovery of highly relevant Google Scholar results. Both systems were scored with Undermind's classifier; a separate 432-paper manual check evaluated that classifier. This is vendor-reported, arXiv-scoped evidence rather than independent validation.
- **contextual** — [Evaluating Eight Retrieval-Augmented Generation (RAG) Large Language Models’ Responses to Clinical Questions: A Comparative Study](../evidence/krump-2026.md) (preprint); locator: medRxiv abstract only. Undermind was one of eight evaluated RAG tools; the abstract reports no statistically significant differences in concept coverage across tools.

### [Elicit data-extraction evaluations report imperfect accuracy that varies by field and evidence base, supporting human verification rather than autonomous use.](../claims/assistant-005.md)

**Status:** mixed

- **supports** — [Evaluating the AI Tool ‘Elicit’ as a Semi-Automated Second Reviewer for Data Extraction in Systematic Reviews: A Proof-of-Concept](../evidence/hilkenmeier-2025.md) (peer-reviewed-study); locator: Results, PDF pp. 6–7; methods, pp. 3–5. Across 43 studies and 602 data points, Elicit accuracy was 81.4% versus 86.7% for a human reviewer against a consensus ground truth; agreement and accuracy were lower for complex constructs and main-results fields.
- **qualifies** — [Evaluating Elicit’s systematic reviews workflow in an umbrella review on air pollution and acute lower respiratory infections: a methodological study for quality appraisal](../evidence/mazzali-2026.md) (peer-reviewed-study); locator: Results, PDF p. 8. Elicit disagreed with reviewers on 24.4% of general and 30.4% of additional AMSTAR-2 EH appraisal items; errors clustered on multi-component and expert-interpretation questions.
- **qualifies** — [Using Elicit AI research assistant for data extraction in systematic reviews: A feasibility study across environmental and life sciences](../evidence/lagisz-2026.md) (peer-reviewed-study); locator: Abstract, PDF p. 1; Results, PDF pp. 10–13. Across seven life/environmental science reviews, test-set extraction accuracy was 86.6%; re-extraction across accounts agreed on 90% of values but only 46% of supporting quotes and 30% of reasoning. Accuracy in high-accuracy mode was 82.1%. Prompt-development results tended to be higher than results on held-out articles.

### [User-facing evaluations identify speed and ease of use as benefits of Elicit, alongside concerns about generated-abstract accuracy, brevity, and transparency of result counts.](../claims/assistant-006.md)

**Status:** provisional

- **supports** — [Incorporating Generative AI to Promote Inquiry-Based Learning: Comparing Elicit AI Research Assistant to PubMed and CINAHL Complete](../evidence/fenske-2024.md) (peer-reviewed-study); locator: Results, PDF pp. 5–9. In a descriptive course study with 323 graduate nursing students, 26.0% preferred Elicit, compared with 30.7% for PubMed and 31.6% for CINAHL. Among Elicit-preferring students, 38.8% cited ease of use and 16.3% cited speed; across respondents, 34.1% identified inaccurate abstracts and 39.5% overly brief abstracts as weaknesses. This was not a blinded article-level accuracy benchmark.
- **contextual** — [Which AI Tools Work Best for Research? Using Librarian and Student Perspectives to Inform a Rating Rubric](../evidence/patterson-2025.md) (peer-reviewed-study); locator: Methods and results, PDF pp. 3–6. Librarian/student raters valued discovery and search features, but the study used a small rater group and had low average agreement.

## Peer-reviewed studies

- [Using artificial intelligence for systematic review: the example of elicit](../evidence/bernard-2025.md)
- [Comparative evaluation of artificial intelligence–assisted literature search tools for identifying clinically meaningful evidence in cardiology](../evidence/di-febo-2026.md)
- [Incorporating Generative AI to Promote Inquiry-Based Learning: Comparing Elicit AI Research Assistant to PubMed and CINAHL Complete](../evidence/fenske-2024.md)
- [AI-Infused Discovery Environments: Information Retrieval Boon or Overpromised Hype?](../evidence/galbreath-2025.md)
- [Optimizing scholarly literature search: a comparative study of relevance and evidence quality across AI-powered, semantic, and traditional search engines](../evidence/gavgani-2026.md)
- [Evaluating the AI Tool ‘Elicit’ as a Semi-Automated Second Reviewer for Data Extraction in Systematic Reviews: A Proof-of-Concept](../evidence/hilkenmeier-2025.md)
- [Using Elicit AI research assistant for data extraction in systematic reviews: A feasibility study across environmental and life sciences](../evidence/lagisz-2026.md)
- [Comparison of Elicit AI and Traditional Literature Searching in Evidence Syntheses Using Four Case Studies](../evidence/lau-golder-2025.md)
- [Evaluating Elicit’s systematic reviews workflow in an umbrella review on air pollution and acute lower respiratory infections: a methodological study for quality appraisal](../evidence/mazzali-2026.md)
- [Which AI Tools Work Best for Research? Using Librarian and Student Perspectives to Inform a Rating Rubric](../evidence/patterson-2025.md)
- [Are AI tools better than traditional tools in literature searching? Evidence from E-commerce research](../evidence/tomczyk-2024.md)
- [Navigating Machine-Driven Research Landscapes: A Comparative Approach](../evidence/tranfield-2024.md)

## Preprints and unverified manuscripts

- [Evaluating Eight Retrieval-Augmented Generation (RAG) Large Language Models’ Responses to Clinical Questions: A Comparative Study](../evidence/krump-2026.md) — medRxiv preprint posted 12 August 2026; not peer reviewed; abstract-only evidence

## Independent experiments

No independent experiments are linked.

## Important uncertainties

- [Elicit has shown higher precision but lower sensitivity than completed evidence-synthesis searches in retrospective comparisons; its output has also varied across repeated searches.](../claims/assistant-001.md) is marked **mixed**.
- [Independent tool comparisons report different retrieval relevance and coverage profiles across query sets; current evidence does not establish a general-purpose winner over conventional library search.](../claims/assistant-002.md) is marked **mixed**.
- [One single-domain study reported high Consensus precision on a specialized tissue-engineering query, while broader comparative studies do not support treating that result as a stable cross-domain performance estimate.](../claims/assistant-003.md) is marked **provisional**.
- [A small rubric study rated Undermind and paid Elicit highly, but its low interrater agreement makes these ratings preliminary; Undermind’s quantified search-performance claims come from a vendor-authored benchmark.](../claims/assistant-004.md) is marked **provisional**.
- [Elicit data-extraction evaluations report imperfect accuracy that varies by field and evidence base, supporting human verification rather than autonomous use.](../claims/assistant-005.md) is marked **mixed**.
- [User-facing evaluations identify speed and ease of use as benefits of Elicit, alongside concerns about generated-abstract accuracy, brevity, and transparency of result counts.](../claims/assistant-006.md) is marked **provisional**.

Read the individual source records for study design, scope, and unresolved reporting discrepancies.

**Last reviewed:** 2026-09-25
