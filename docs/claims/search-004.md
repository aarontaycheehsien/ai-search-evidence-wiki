> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**

# Fine-tuning and multi-stage query construction can improve Boolean-search recall on specific evidence-synthesis benchmarks, but reported performance depends on dataset and evaluation depth, and may trade precision or workload.

**Status:** supported

## Evidence

### Literature search sandbox: a large language model that generates search queries for systematic reviews

- **Source:** [adam-2024-search](../evidence/adam-2024-search.md)
- **Category:** peer-reviewed-study
- **Relationship:** supports
- **Locator:** Table 1, PDF p. 6; Table 2, PDF p. 7
- **Note:** Fine-tuned Mistral query generation achieved median sensitivity of 85%-86% on 57 reviews, with median numbers needed to read of 908-1,206 citations; librarians cautioned that scrutiny remained necessary.

### Chained Prompting for Better Systematic Review Search Strategies

- **Source:** [nasser-2025-chained](../evidence/nasser-2025-chained.md)
- **Category:** peer-reviewed-study
- **Relationship:** supports
- **Locator:** Table I, PDF p. 5; dataset and exclusions, PDF pp. 3, 7
- **Note:** A chained pipeline reported mean recall 0.87 across 81 selected reviews, compared with 0.10 for direct GPT-4o prompting, but did not report precision or workload and excluded searches returning over 1,000 records.

### AutoBool: Reinforcement-Learned LLM for Effective Automatic Systematic Reviews Boolean Query Generation

- **Source:** [wang-2026-autobool](../evidence/wang-2026-autobool.md)
- **Category:** peer-reviewed-study
- **Relationship:** supports
- **Locator:** Table 5, PDF p. 14; Table 6, PDF p. 15
- **Note:** On CLEF TAR, AutoBool recall was 0.8387 versus 0.8458 for expert queries while retrieving 818 versus 14,327 documents; on the Seed Collection, recall was 0.6828 versus 0.7241.

### Fully Automated Scholarly Search for Biomedical Systematic Literature Reviews

- **Source:** [budau-2024-fass](../evidence/budau-2024-fass.md)
- **Category:** peer-reviewed-study
- **Relationship:** qualifies
- **Locator:** Tables 4 and 8, PDF pp. 6, 9
- **Note:** In a COVID-19 benchmark, ChatGPT zero-seed recall@1000 was below manual queries (0.2594 vs 0.3581); three seed documents narrowed the gap to 0.3300.

## Topics

- [LLMs for search strategy generation and expansion](../questions/llm-search-strategy-generation.md)

**Last reviewed:** 2026-09-26
