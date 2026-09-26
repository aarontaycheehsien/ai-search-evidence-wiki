> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**

# Verifying that an LLM cites real papers is insufficient to establish evidence fidelity because the generated claims may still misstate, overstate, or contradict those papers.

**Status:** supported — 5 sources; 2025–2026; 3 peer-reviewed studies, 2 preprints

## Evidence

### Fluency Without Fidelity: Errors in Citation-Attributed Claims in Large Language Model-Generated Literature Reviews in Mental Health

- **Source:** [linardon-2026](../evidence/linardon-2026.md)
- **Category:** peer-reviewed-study
- **Relationship:** supports
- **Locator:** Methods, PDF pp. 2-4; Results and Table 2, PDF p. 5
- **Note:** All 209 cited publications were identifiable, but only 43.5% of 333 citation-claim pairs were fully accurate; 19.8% were fabricated or contradictory and 18.3% contained major inaccuracies. The audit used one ChatGPT-5 configuration in mental health.

### Cross sectional pilot study on clinical review generation using large language models

- **Source:** [luo-2025-clinical-reviews](../evidence/luo-2025-clinical-reviews.md)
- **Category:** peer-reviewed-study
- **Relationship:** supports
- **Locator:** Results, PDF pp. 2-4; Methods and Table 4, PDF pp. 8-12
- **Note:** Across 2,169 AI-generated clinical reviews, median reference accuracy was 100% but the IQR was 73.55-100%; standalone LLMs had a median of 95% with an IQR of 51.22-100%. Accuracy measured whether each reference's explanation was consistent with the original article.

### ReportBench: Evaluating Deep Research Agents via Academic Survey Tasks

- **Source:** [li-2025-reportbench](../evidence/li-2025-reportbench.md)
- **Category:** preprint
- **Relationship:** supports
- **Locator:** Sections 2.1-3.3 and Table 1
- **Note:** Across 100 academic-survey prompts, automated citation-statement match rates ranged from 31.43% to 78.87% across six systems. This is a preprint and used GPT-4o to judge source support.

### Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis

- **Source:** [goo-2026-citation-faithfulness](../evidence/goo-2026-citation-faithfulness.md)
- **Category:** preprint
- **Relationship:** qualifies
- **Locator:** Abstract; Sections 5.3-5.4; Figure 3; Table S3
- **Note:** On identical agentic scientific-synthesis outputs, estimated unsupported-citation rates ranged from about 3% to about 18% depending on the verifier. The study is a preprint and evaluates multi-paper cited answers rather than full literature reviews.

### An automated framework for assessing how well LLMs cite relevant medical references

- **Source:** [wu-2025-sourcecheckup](../evidence/wu-2025-sourcecheckup.md)
- **Category:** peer-reviewed-study
- **Relationship:** contextual
- **Locator:** Abstract; Results and Figure 1; Methods
- **Note:** In medical question answering, 50-90% of responses were not fully supported by cited sources; GPT-4o with web search had 55% fully supported responses. This supports the source-validity versus source-support distinction but is not a literature-review study.

## Topics

- [Citation fidelity in LLM-generated reviews](../topics/citation-fidelity.md)

**Last reviewed:** 2026-09-26
