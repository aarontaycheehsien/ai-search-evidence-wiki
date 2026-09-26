> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**

# LLMs for search strategy generation and expansion

## Research question

How reliably do large language models generate or expand literature-search queries for evidence synthesis?


## Scope and review boundaries

Define the evidence-synthesis setting, eligible study types, and task boundaries here. Keep scope decisions explicit and source-backed where they depend on empirical evidence.

## Overview

This topic groups 4 claims linked to 11 source records.

## Current evidence

The relationships and source categories below come from the structured evidence records. Results are reported in each source's own review setting; this page does not pool them.

## Key claims

### [LLM-generated Boolean search strategies remain highly sensitive to model, prompt, validation, and seed-study choices, and generally do not match the recall of expert manual strategies without substantial precision tradeoffs.](../claims/search-001.md)

**Status:** supported

- **supports** — [Reassessing Large Language Model Boolean Query Generation for Systematic Reviews](../evidence/wang-2025-query.md) (peer-reviewed-study); locator: Tables 2-3, PDF pp. 6-7; Discussion and limitations, PDF p. 13. Across 71 CLEF TAR topics, the expert manual recall was 0.8436 while the best reported generated-query recall in Table 2 was 0.6545. On the seed collection, combining guided queries reached recall 0.7361 versus 0.7241 for manual queries but with very low precision; best-seed selection was post hoc.
- **supports** — [Can ChatGPT Write a Good Boolean Query for Systematic Review Literature Search?](../evidence/wang-2023-boolean.md) (peer-reviewed-study); locator: Table 4, PDF p. 8; Tables 6-7, PDF pp. 10-11. On CLEF, the best single ChatGPT formulation prompt had recall 0.5035 versus 0.8317 for the original human query. Guided seed-based formulation improved recall to 0.5171 on the Seed Collection, while still showing run-to-run variation.
- **supports** — [Literature search sandbox: a large language model that generates search queries for systematic reviews](../evidence/adam-2024-search.md) (peer-reviewed-study); locator: Table 1, PDF p. 6. Fine-tuned Mistral queries achieved median sensitivity of 85%-86% on 57 reviews, below the 100% median for human strategies; generated queries required a median 908-1,206 citations to read versus 580 for human queries.
- **supports** — [A Reproducibility and Generalizability Study of Large Language Models for Query Generation](../evidence/staudinger-2024-query.md) (peer-reviewed-study); locator: Tables 1 and 3, PDF pp. 5-6. On CLEF TAR, human-query recall was 0.832, while the maximum reported LLM recall was 0.150; on the Seed Collection, the maximum model recall was 0.267 versus 0.711 for the human baseline.
- **supports** — [Fully Automated Scholarly Search for Biomedical Systematic Literature Reviews](../evidence/budau-2024-fass.md) (peer-reviewed-study); locator: Table 4, PDF p. 6; Table 8, PDF p. 9. On a 62-review COVID-19 subset, ChatGPT recall@1000 was 0.2594 without seeds and 0.3300 with three seeds, compared with 0.3581 for manual queries.
- **supports** — [Quality Evaluation of Generative AI-Based Search Strategies in Systematic Reviews and Comparison of Search Performance with Human Expert (Medical Librarian)](../evidence/park-2025-search.md) (peer-reviewed-study); locator: Table 6, PDF p. 14. For one obesity-psychotherapy topic across 139 included studies, ChatGPT-5 recall was 46.8% and Gemini 2.5 recall 49.6%, compared with 54.7% for a medical librarian; all precision estimates were below 1%.
- **qualifies** — [AutoBool: Reinforcement-Learned LLM for Effective Automatic Systematic Reviews Boolean Query Generation](../evidence/wang-2026-autobool.md) (peer-reviewed-study); locator: Table 5, PDF p. 14; Table 6, PDF p. 15. AutoBool reached CLEF TAR recall 0.8387 versus 0.8458 for expert queries while retrieving 818 versus 14,327 documents, but Seed Collection recall remained lower (0.6828 vs. 0.7241).
- **qualifies** — [Human vs. machine in medical search strategy development: a comparative evaluation of ChatGPT-4.1](../evidence/walz-2025-search.md) (peer-reviewed-study); locator: Results, PDF p. 3. Five of six ChatGPT-4.1 strategies across two topics retrieved all benchmark included articles, but no precision or time advantage was measured and hallucinated MeSH terms were common.

### [Generative query expansion does not produce uniform retrieval gains across biomedical benchmarks; its effect depends on the expansion method and dataset and often changes ranking more than overall screening coverage.](../claims/search-002.md)

**Status:** supported

- **supports** — [A critical evaluation of generative query expansion on biomedical literature retrieval](../evidence/fang-2026-query.md) (peer-reviewed-study); locator: Table 2, PDF pp. 6-7; Discussion, PDF pp. 9-11. Across eight expansion methods and three LLMs, several BioASQ and PubMedQA results fell below the unexpanded baseline, while most TREC Precision Medicine configurations improved recall or nDCG. The authors characterize the main effect as reranking with limited screening-stage impact.

### [LLM-generated Boolean strategies can contain invalid syntax, fabricated or incorrect controlled-vocabulary terms, and substantial run-to-run variation, so generated queries need technical and subject review before use.](../claims/search-003.md)

**Status:** supported

- **supports** — [Can ChatGPT Write a Good Boolean Query for Systematic Review Literature Search?](../evidence/wang-2023-boolean.md) (peer-reviewed-study); locator: MeSH analysis and prompt variability, PDF pp. 12-14. The study reports that more than half of generated MeSH terms for query formulation were invalid, with similarly high invalidity during query refinement; repeated runs also showed wide recall variation.
- **supports** — [A Reproducibility and Generalizability Study of Large Language Models for Query Generation](../evidence/staudinger-2024-query.md) (peer-reviewed-study); locator: Syntax validation results, PDF p. 7. 1,771 of 11,200 generated queries (15.8%) had malformed or unbalanced parentheses.
- **supports** — [Human vs. machine in medical search strategy development: a comparative evaluation of ChatGPT-4.1](../evidence/walz-2025-search.md) (peer-reviewed-study); locator: PRESS assessment and error analysis, PDF pp. 2-3. Hallucinated MeSH terms occurred in 5 of 6 strategies, and output formatting errors required manual correction.
- **supports** — [Assessing the Quality of Biomedical Boolean Search Strings Generated by Prompted and Unprompted Models Using ChatGPT: A Pilot Study](../evidence/reed-2024-search.md) (peer-reviewed-study); locator: Results and discussion, PDF pp. 5-8. Outputs varied substantially over five runs and occasionally used phrase quotation that interfered with PubMed Automatic Term Mapping.

### [Fine-tuning and multi-stage query construction can improve Boolean-search recall on specific evidence-synthesis benchmarks, but reported performance depends on dataset and evaluation depth, and may trade precision or workload.](../claims/search-004.md)

**Status:** supported

- **supports** — [Literature search sandbox: a large language model that generates search queries for systematic reviews](../evidence/adam-2024-search.md) (peer-reviewed-study); locator: Table 1, PDF p. 6; Table 2, PDF p. 7. Fine-tuned Mistral query generation achieved median sensitivity of 85%-86% on 57 reviews, with median numbers needed to read of 908-1,206 citations; librarians cautioned that scrutiny remained necessary.
- **supports** — [Chained Prompting for Better Systematic Review Search Strategies](../evidence/nasser-2025-chained.md) (peer-reviewed-study); locator: Table I, PDF p. 5; dataset and exclusions, PDF pp. 3, 7. A chained pipeline reported mean recall 0.87 across 81 selected reviews, compared with 0.10 for direct GPT-4o prompting, but did not report precision or workload and excluded searches returning over 1,000 records.
- **supports** — [AutoBool: Reinforcement-Learned LLM for Effective Automatic Systematic Reviews Boolean Query Generation](../evidence/wang-2026-autobool.md) (peer-reviewed-study); locator: Table 5, PDF p. 14; Table 6, PDF p. 15. On CLEF TAR, AutoBool recall was 0.8387 versus 0.8458 for expert queries while retrieving 818 versus 14,327 documents; on the Seed Collection, recall was 0.6828 versus 0.7241.
- **qualifies** — [Fully Automated Scholarly Search for Biomedical Systematic Literature Reviews](../evidence/budau-2024-fass.md) (peer-reviewed-study); locator: Tables 4 and 8, PDF pp. 6, 9. In a COVID-19 benchmark, ChatGPT zero-seed recall@1000 was below manual queries (0.2594 vs 0.3581); three seed documents narrowed the gap to 0.3300.

## Connected concepts

- [Recall and sensitivity](../concepts/recall-and-sensitivity.md)
- [Precision](../concepts/precision.md)
- [Reference standards and ground truth](../concepts/reference-standards.md)
- [Reproducibility and output stability](../concepts/reproducibility-and-stability.md)

## Open questions and evidence gaps

Record unresolved questions and evidence gaps here as they are identified during review.

## Peer-reviewed studies

- [Literature search sandbox: a large language model that generates search queries for systematic reviews](../evidence/adam-2024-search.md)
- [Fully Automated Scholarly Search for Biomedical Systematic Literature Reviews](../evidence/budau-2024-fass.md)
- [A critical evaluation of generative query expansion on biomedical literature retrieval](../evidence/fang-2026-query.md)
- [Chained Prompting for Better Systematic Review Search Strategies](../evidence/nasser-2025-chained.md)
- [Quality Evaluation of Generative AI-Based Search Strategies in Systematic Reviews and Comparison of Search Performance with Human Expert (Medical Librarian)](../evidence/park-2025-search.md)
- [Assessing the Quality of Biomedical Boolean Search Strings Generated by Prompted and Unprompted Models Using ChatGPT: A Pilot Study](../evidence/reed-2024-search.md)
- [A Reproducibility and Generalizability Study of Large Language Models for Query Generation](../evidence/staudinger-2024-query.md)
- [Human vs. machine in medical search strategy development: a comparative evaluation of ChatGPT-4.1](../evidence/walz-2025-search.md)
- [Can ChatGPT Write a Good Boolean Query for Systematic Review Literature Search?](../evidence/wang-2023-boolean.md)
- [Reassessing Large Language Model Boolean Query Generation for Systematic Reviews](../evidence/wang-2025-query.md)
- [AutoBool: Reinforcement-Learned LLM for Effective Automatic Systematic Reviews Boolean Query Generation](../evidence/wang-2026-autobool.md)

## Preprints and unverified manuscripts

No preprints or unverified manuscripts are linked.

## Independent experiments

No independent experiments are linked.

## Important uncertainties

No linked claim is currently flagged as provisional, uncertain, mixed, or contradicted.

Read the individual source records for study design, scope, and unresolved reporting discrepancies.

**Last reviewed:** 2026-09-26
