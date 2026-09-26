> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**

# Citation fidelity in LLM-generated reviews

## Research question

Do claims in large-language-model-generated literature reviews accurately represent the papers they cite?


## Scope and review boundaries

Define the evidence-synthesis setting, eligible study types, and task boundaries here. Keep scope decisions explicit and source-backed where they depend on empirical evidence.

## Overview

This topic groups 2 claims linked to 5 source records.

## Current evidence

The relationships and source categories below come from the structured evidence records. Results are reported in each source's own review setting; this page does not pool them.

## Key claims

### [Verifying that an LLM cites real papers is insufficient to establish evidence fidelity because the generated claims may still misstate, overstate, or contradict those papers.](../claims/citation-001.md)

**Status:** supported

- **supports** — [Fluency Without Fidelity: Errors in Citation-Attributed Claims in Large Language Model-Generated Literature Reviews in Mental Health](../evidence/linardon-2026.md) (peer-reviewed-study); locator: Methods, PDF pp. 2-4; Results and Table 2, PDF p. 5. All 209 cited publications were identifiable, but only 43.5% of 333 citation-claim pairs were fully accurate; 19.8% were fabricated or contradictory and 18.3% contained major inaccuracies. The audit used one ChatGPT-5 configuration in mental health.
- **supports** — [Cross sectional pilot study on clinical review generation using large language models](../evidence/luo-2025-clinical-reviews.md) (peer-reviewed-study); locator: Results, PDF pp. 2-4; Methods and Table 4, PDF pp. 8-12. Across 2,169 AI-generated clinical reviews, median reference accuracy was 100% but the IQR was 73.55-100%; standalone LLMs had a median of 95% with an IQR of 51.22-100%. Accuracy measured whether each reference's explanation was consistent with the original article.
- **supports** — [ReportBench: Evaluating Deep Research Agents via Academic Survey Tasks](../evidence/li-2025-reportbench.md) (preprint); locator: Sections 2.1-3.3 and Table 1. Across 100 academic-survey prompts, automated citation-statement match rates ranged from 31.43% to 78.87% across six systems. This is a preprint and used GPT-4o to judge source support.
- **qualifies** — [Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis](../evidence/goo-2026-citation-faithfulness.md) (preprint); locator: Abstract; Sections 5.3-5.4; Figure 3; Table S3. On identical agentic scientific-synthesis outputs, estimated unsupported-citation rates ranged from about 3% to about 18% depending on the verifier. The study is a preprint and evaluates multi-paper cited answers rather than full literature reviews.
- **contextual** — [An automated framework for assessing how well LLMs cite relevant medical references](../evidence/wu-2025-sourcecheckup.md) (peer-reviewed-study); locator: Abstract; Results and Figure 1; Methods. In medical question answering, 50-90% of responses were not fully supported by cited sources; GPT-4o with web search had 55% fully supported responses. This supports the source-validity versus source-support distinction but is not a literature-review study.

### [Reported citation-fidelity rates for LLM-generated scientific syntheses are sensitive to the evaluation protocol, so comparisons require the same unit of analysis, support rubric, verifier, and source-access procedure.](../claims/citation-002.md)

**Status:** provisional

- **supports** — [Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis](../evidence/goo-2026-citation-faithfulness.md) (preprint); locator: Abstract; Sections 5.3-5.4; Figure 3; Table S3. Applying five gold-validated verifiers to identical outputs produced unsupported-citation estimates of about 3-18%; negative-specific agreement on which citations to flag was 0.27-0.30 on 300 cited sentences. This source is a preprint.
- **contextual** — [Fluency Without Fidelity: Errors in Citation-Attributed Claims in Large Language Model-Generated Literature Reviews in Mental Health](../evidence/linardon-2026.md) (peer-reviewed-study); locator: Methods, PDF pp. 2-4. Used two human reviewers, a four-level claim-accuracy rubric, and full cited publications to audit 333 citation-claim pairs.
- **contextual** — [Cross sectional pilot study on clinical review generation using large language models](../evidence/luo-2025-clinical-reviews.md) (peer-reviewed-study); locator: Methods and Table 4, PDF pp. 8-12. Reported per-review reference accuracy based on manual judgments of whether reference explanations were consistent with original articles, a different unit and rubric from claim-pair audits.
- **contextual** — [ReportBench: Evaluating Deep Research Agents via Academic Survey Tasks](../evidence/li-2025-reportbench.md) (preprint); locator: Section 3.2 and Table 1. Used GPT-4o to extract cited statements and judge semantic consistency with retrieved source documents, yielding an automated match-rate metric.

## Connected concepts

- [Reference standards and ground truth](../concepts/reference-standards.md)
- [Reproducibility and output stability](../concepts/reproducibility-and-stability.md)
- [Error types in screening and extraction](../concepts/extraction-and-screening-errors.md)

## Open questions and evidence gaps

Record unresolved questions and evidence gaps here as they are identified during review.

## Peer-reviewed studies

- [Fluency Without Fidelity: Errors in Citation-Attributed Claims in Large Language Model-Generated Literature Reviews in Mental Health](../evidence/linardon-2026.md)
- [Cross sectional pilot study on clinical review generation using large language models](../evidence/luo-2025-clinical-reviews.md)
- [An automated framework for assessing how well LLMs cite relevant medical references](../evidence/wu-2025-sourcecheckup.md)

## Preprints and unverified manuscripts

- [Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis](../evidence/goo-2026-citation-faithfulness.md) — arXiv preprint 2607.20527v1; manuscript submitted to ACM
- [ReportBench: Evaluating Deep Research Agents via Academic Survey Tasks](../evidence/li-2025-reportbench.md) — arXiv preprint 2508.15804v1

## Independent experiments

No independent experiments are linked.

## Important uncertainties

- [Reported citation-fidelity rates for LLM-generated scientific syntheses are sensitive to the evaluation protocol, so comparisons require the same unit of analysis, support rubric, verifier, and source-access procedure.](../claims/citation-002.md) is marked **provisional**.

Read the individual source records for study design, scope, and unresolved reporting discrepancies.

**Last reviewed:** 2026-09-26
