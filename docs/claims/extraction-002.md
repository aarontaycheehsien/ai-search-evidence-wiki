> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**

# Current LLM data extraction can be precise yet incomplete, with omissions as the dominant error; task-specific prompts improve recall but do not remove the need for human verification of meta-analytic data.

**Status:** supported

## Evidence

### What level of automation is 'good enough'? A benchmark of large language models for meta-analysis data extraction

- **Source:** [li-2026-extraction](../evidence/li-2026-extraction.md)
- **Category:** peer-reviewed-study
- **Relationship:** supports
- **Locator:** Table 2, PDF p. 9; Figures 2-3 and Table 3, PDF pp. 10-11; error analysis, PDF pp. 14-15
- **Note:** Across 58 RCTs, baseline statistical-result recall ranged from 0.214 to 0.445 despite precision of 0.856 to 0.939. Customized prompts raised recall by 14.8 percentage points on average; 87.8% of 22,196 catalogued errors were missing fields.

### Artificial Intelligence-Assisted Data Extraction With a Large Language Model: A Study Within Reviews

- **Source:** [gartlehner-2025](../evidence/gartlehner-2025.md)
- **Category:** peer-reviewed-study
- **Relationship:** contextual
- **Locator:** Results, PDF pp. 7-9
- **Note:** A supervised workflow performed well in a real-world comparison, but still had a 9.0% overall incorrect-extraction rate and a 2.5% major-error rate.

### Performance of large language models and prompt engineering strategies for data extraction in systematic reviews

- **Source:** [oami-2026-extraction](../evidence/oami-2026-extraction.md)
- **Category:** peer-reviewed-study
- **Relationship:** supports
- **Locator:** Tables 2-3, PDF pp. 3-5; Figures 1-2, PDF pp. 5-6
- **Note:** Across three models and 36 sepsis trials, missing or incorrect values comprised most errors; outcome extraction was less accurate and less reproducible than background-field extraction.

### Assessing data extraction in randomized clinical trials with large language models

- **Source:** [yisha-2026-rct-extraction](../evidence/yisha-2026-rct-extraction.md)
- **Category:** peer-reviewed-study
- **Relationship:** supports
- **Locator:** Results and Figures 2-6, PDF pp. 3-8; Table 2, PDF p. 9
- **Note:** Among 105 RCTs, mean and standard-deviation extraction for continuous outcomes was correct in only 24%-56% of cases, despite stronger binary group-size accuracy.

### Diagnosing Structural Failures in LLM-Based Evidence Extraction for Meta-Analysis

- **Source:** [tan-2026-structural](../evidence/tan-2026-structural.md)
- **Category:** preprint
- **Relationship:** supports
- **Locator:** Table 6, PDF p. 10; error analysis, PDF pp. 11-12
- **Note:** On a manually annotated 52-paper benchmark, both evaluated models scored F1=0 on full meta-analytic association tuples; variable-role swaps and cross-analysis binding errors contributed to failures. This is an arXiv preprint and a broader scholarly extraction benchmark.

### Breaking the Extraction Bottleneck: A Single AI Agent Achieves Statistical Equivalence with Human-Extracted Meta-Analysis Data Across Five Agricultural Datasets

- **Source:** [halpern-2026-agricultural-extraction](../evidence/halpern-2026-agricultural-extraction.md)
- **Category:** preprint
- **Relationship:** qualifies
- **Locator:** Tables 4-9, PDF pp. 12-19; limitations, PDF pp. 26-27
- **Note:** This bioRxiv preprint reports proportional equivalence for pooled effects in five agricultural datasets. LLM-based alignment materially affected matching agreement without changing extracted values, and variance extraction was not formally validated; the result therefore qualifies, but does not negate, errors in item-level extraction.

## Topics

- [LLMs for structured data extraction](../questions/llm-data-extraction.md)

**Last reviewed:** 2026-09-26
