> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**

# LLM-generated Boolean search strategies remain highly sensitive to model, prompt, validation, and seed-study choices, and generally do not match the recall of expert manual strategies without substantial precision tradeoffs.

**Status:** supported — 8 sources; 2023–2026; 8 peer-reviewed studies

## Evidence

### Reassessing Large Language Model Boolean Query Generation for Systematic Reviews

- **Source:** [wang-2025-query](../evidence/wang-2025-query.md)
- **Category:** peer-reviewed-study
- **Relationship:** supports
- **Locator:** Tables 2-3, PDF pp. 6-7; Discussion and limitations, PDF p. 13
- **Note:** Across 71 CLEF TAR topics, the expert manual recall was 0.8436 while the best reported generated-query recall in Table 2 was 0.6545. On the seed collection, combining guided queries reached recall 0.7361 versus 0.7241 for manual queries but with very low precision; best-seed selection was post hoc.

### Can ChatGPT Write a Good Boolean Query for Systematic Review Literature Search?

- **Source:** [wang-2023-boolean](../evidence/wang-2023-boolean.md)
- **Category:** peer-reviewed-study
- **Relationship:** supports
- **Locator:** Table 4, PDF p. 8; Tables 6-7, PDF pp. 10-11
- **Note:** On CLEF, the best single ChatGPT formulation prompt had recall 0.5035 versus 0.8317 for the original human query. Guided seed-based formulation improved recall to 0.5171 on the Seed Collection, while still showing run-to-run variation.

### Literature search sandbox: a large language model that generates search queries for systematic reviews

- **Source:** [adam-2024-search](../evidence/adam-2024-search.md)
- **Category:** peer-reviewed-study
- **Relationship:** supports
- **Locator:** Table 1, PDF p. 6
- **Note:** Fine-tuned Mistral queries achieved median sensitivity of 85%-86% on 57 reviews, below the 100% median for human strategies; generated queries required a median 908-1,206 citations to read versus 580 for human queries.

### A Reproducibility and Generalizability Study of Large Language Models for Query Generation

- **Source:** [staudinger-2024-query](../evidence/staudinger-2024-query.md)
- **Category:** peer-reviewed-study
- **Relationship:** supports
- **Locator:** Tables 1 and 3, PDF pp. 5-6
- **Note:** On CLEF TAR, human-query recall was 0.832, while the maximum reported LLM recall was 0.150; on the Seed Collection, the maximum model recall was 0.267 versus 0.711 for the human baseline.

### Fully Automated Scholarly Search for Biomedical Systematic Literature Reviews

- **Source:** [budau-2024-fass](../evidence/budau-2024-fass.md)
- **Category:** peer-reviewed-study
- **Relationship:** supports
- **Locator:** Table 4, PDF p. 6; Table 8, PDF p. 9
- **Note:** On a 62-review COVID-19 subset, ChatGPT recall@1000 was 0.2594 without seeds and 0.3300 with three seeds, compared with 0.3581 for manual queries.

### Quality Evaluation of Generative AI-Based Search Strategies in Systematic Reviews and Comparison of Search Performance with Human Expert (Medical Librarian)

- **Source:** [park-2025-search](../evidence/park-2025-search.md)
- **Category:** peer-reviewed-study
- **Relationship:** supports
- **Locator:** Table 6, PDF p. 14
- **Note:** For one obesity-psychotherapy topic across 139 included studies, ChatGPT-5 recall was 46.8% and Gemini 2.5 recall 49.6%, compared with 54.7% for a medical librarian; all precision estimates were below 1%.

### AutoBool: Reinforcement-Learned LLM for Effective Automatic Systematic Reviews Boolean Query Generation

- **Source:** [wang-2026-autobool](../evidence/wang-2026-autobool.md)
- **Category:** peer-reviewed-study
- **Relationship:** qualifies
- **Locator:** Table 5, PDF p. 14; Table 6, PDF p. 15
- **Note:** AutoBool reached CLEF TAR recall 0.8387 versus 0.8458 for expert queries while retrieving 818 versus 14,327 documents, but Seed Collection recall remained lower (0.6828 vs. 0.7241).

### Human vs. machine in medical search strategy development: a comparative evaluation of ChatGPT-4.1

- **Source:** [walz-2025-search](../evidence/walz-2025-search.md)
- **Category:** peer-reviewed-study
- **Relationship:** qualifies
- **Locator:** Results, PDF p. 3
- **Note:** Five of six ChatGPT-4.1 strategies across two topics retrieved all benchmark included articles, but no precision or time advantage was measured and hallucinated MeSH terms were common.

## Topics

- [LLMs for search strategy generation and expansion](../topics/llm-search-strategy-generation.md)

**Last reviewed:** 2026-09-25
