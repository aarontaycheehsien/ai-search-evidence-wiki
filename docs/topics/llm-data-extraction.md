> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**

# LLMs for structured data extraction

## Research question

How accurate, complete, and efficient are large language models for extracting structured data from studies for evidence synthesis?


## Scope and review boundaries

Define the evidence-synthesis setting, eligible study types, and task boundaries here. Keep scope decisions explicit and source-backed where they depend on empirical evidence.

## Overview

This topic groups 6 claims linked to 16 source records.

## Current evidence

The relationships and source categories below come from the structured evidence records. Results are reported in each source's own review setting; this page does not pool them.

## Key claims

### [In one prospective study within reviews, human-verified LLM extraction was slightly more accurate and faster than a conventional human-only workflow, while both approaches retained consequential errors.](../claims/extraction-001.md)

**Status:** supported

- **supports** — [Artificial Intelligence-Assisted Data Extraction With a Large Language Model: A Study Within Reviews](../evidence/gartlehner-2025.md) (peer-reviewed-study); locator: Results, PDF pp. 7-9; Figure 2, PDF p. 19; Tables 1-2, PDF pp. 20-21. Across 9,341 items from 63 studies, AI-assisted versus human-only accuracy was 91.0% versus 89.0%, major-error rates were 2.5% versus 2.7%, and median time was 84 versus 125 minutes per study. Only discordant extractions were adjudicated.

### [Current LLM data extraction can be precise yet incomplete, with omissions as the dominant error; task-specific prompts improve recall but do not remove the need for human verification of meta-analytic data.](../claims/extraction-002.md)

**Status:** supported

- **supports** — [What level of automation is 'good enough'? A benchmark of large language models for meta-analysis data extraction](../evidence/li-2026-extraction.md) (peer-reviewed-study); locator: Table 2, PDF p. 9; Figures 2-3 and Table 3, PDF pp. 10-11; error analysis, PDF pp. 14-15. Across 58 RCTs, baseline statistical-result recall ranged from 0.214 to 0.445 despite precision of 0.856 to 0.939. Customized prompts raised recall by 14.8 percentage points on average; 87.8% of 22,196 catalogued errors were missing fields.
- **contextual** — [Artificial Intelligence-Assisted Data Extraction With a Large Language Model: A Study Within Reviews](../evidence/gartlehner-2025.md) (peer-reviewed-study); locator: Results, PDF pp. 7-9. A supervised workflow performed well in a real-world comparison, but still had a 9.0% overall incorrect-extraction rate and a 2.5% major-error rate.
- **supports** — [Performance of large language models and prompt engineering strategies for data extraction in systematic reviews](../evidence/oami-2026-extraction.md) (peer-reviewed-study); locator: Tables 2-3, PDF pp. 3-5; Figures 1-2, PDF pp. 5-6. Across three models and 36 sepsis trials, missing or incorrect values comprised most errors; outcome extraction was less accurate and less reproducible than background-field extraction.
- **supports** — [Assessing data extraction in randomized clinical trials with large language models](../evidence/yisha-2026-rct-extraction.md) (peer-reviewed-study); locator: Results and Figures 2-6, PDF pp. 3-8; Table 2, PDF p. 9. Among 105 RCTs, mean and standard-deviation extraction for continuous outcomes was correct in only 24%-56% of cases, despite stronger binary group-size accuracy.
- **supports** — [Diagnosing Structural Failures in LLM-Based Evidence Extraction for Meta-Analysis](../evidence/tan-2026-structural.md) (preprint); locator: Table 6, PDF p. 10; error analysis, PDF pp. 11-12. On a manually annotated 52-paper benchmark, both evaluated models scored F1=0 on full meta-analytic association tuples; variable-role swaps and cross-analysis binding errors contributed to failures. This is an arXiv preprint and a broader scholarly extraction benchmark.
- **qualifies** — [Breaking the Extraction Bottleneck: A Single AI Agent Achieves Statistical Equivalence with Human-Extracted Meta-Analysis Data Across Five Agricultural Datasets](../evidence/halpern-2026-agricultural-extraction.md) (preprint); locator: Tables 4-9, PDF pp. 12-19; limitations, PDF pp. 26-27. This bioRxiv preprint reports proportional equivalence for pooled effects in five agricultural datasets. LLM-based alignment materially affected matching agreement without changing extracted values, and variance extraction was not formally validated; the result therefore qualifies, but does not negate, errors in item-level extraction.
- **qualifies** — [Collaborative large language models for automated data extraction in living systematic reviews](../evidence/khan-2025-collaborative-extraction.md) (peer-reviewed-study); locator: Results, PDF pp. 4-5. Single-model test precision was 0.98/0.94 and recall 0.87/0.91; initial concordant outputs were 94% accurate, showing stronger performance in this narrow prostate-cancer benchmark while retaining omissions and hallucinations.
- **supports** — [Using Artificial Intelligence Tools as Second Reviewers for Data Extraction in Systematic Reviews: A Performance Comparison of Two AI Tools Against Human Reviewers](../evidence/andersen-2025-second-reviewer.md) (peer-reviewed-study); locator: Results and Table 2, PDF pp. 4-6; Discussion, p. 7. Mild underreporting counted as successful extraction, yet only 80/90 Elicit and 76/90 ChatGPT outputs were fully complete. Seven of 180 outputs contained confabulations; the proposed second-reviewer workflow retains human reconciliation.

### [LLM extraction performance varies by field and structural complexity: explicit study descriptors are generally easier than numerical outcomes, relational bindings, and complete synthesis-ready records.](../claims/extraction-003.md)

**Status:** supported

- **supports** — [Performance of large language models and prompt engineering strategies for data extraction in systematic reviews](../evidence/oami-2026-extraction.md) (peer-reviewed-study); locator: Table 2 and Figure 1, PDF pp. 3-5. Across three models, background-data no-error proportions ranged from 81.6%-92.4%, while outcome-data no-error proportions ranged from 27.8%-80.7%.
- **supports** — [Assessing data extraction in randomized clinical trials with large language models](../evidence/yisha-2026-rct-extraction.md) (peer-reviewed-study); locator: Results and Figures 2-6, PDF pp. 3-8. Binary group-size accuracy was 91%-94%, compared with 24%-56% for continuous-outcome means and standard deviations.
- **supports** — [Diagnosing Structural Failures in LLM-Based Evidence Extraction for Meta-Analysis](../evidence/tan-2026-structural.md) (preprint); locator: Table 6, PDF p. 10; error analysis, PDF pp. 11-12. Across 52 empirical papers, single-attribute F1 was higher than multi-attribute binding; both models scored F1=0 on the complete association tuple.
- **supports** — [OpenExtract: Automated Data Extraction for Systematic Reviews in Health](../evidence/achterberg-2026-openextract.md) (peer-reviewed-study); locator: Tables 1-2, PDF p. 4. In a 10-paper digital-health review sample, aggregate precision and recall varied by model size: 0.820/0.820 and 0.846/0.813 for the two larger models versus 0.624/0.564 for the 7B model.
- **supports** — [Custom GPT models for complex rheumatology systematic reviews: A two-part evaluation of data extraction and prognosis appraisal](../evidence/munguia-realpozo-2026-custom-gpt.md) (peer-reviewed-study); locator: Results and Table 1, PDF p. 5. In 15 SLE metabolomics studies, concordance was 100% for country, 26.7% for sample-size and analytical-platform fields, and 0% for age and sex-distribution fields.
- **supports** — [AI-accelerated meta-analysis in psychology: Large language models code study properties with high accuracy](../evidence/azaad-2026-meta-analysis-coding.md) (peer-reviewed-study); locator: Results, PDF pp. 4-5; Figures 1-2, PDF pp. 5-6. GPT-5 and Gemini 2.5 Pro achieved 93% and 92% agreement with published codes for study properties across three psychology meta-analyses, including higher-level conceptual dimensions.
- **qualifies** — [A foundation model for human-AI collaboration in medical literature mining](../evidence/wang-2025-leads.md) (peer-reviewed-study); locator: Figure 4, PDF p. 7; Results, Figure 5, PDF pp. 8-9. LEADS benchmark and workflow evaluations varied by field: manual-evaluation accuracy was 84.0% for participant-statistic text but 56.7% for numeric trial results; the small expert-plus-AI pilot reached 0.85 accuracy for its extraction task.
- **supports** — [Automated data extraction for systematic reviews using GPT-5.2 and Google Gemini Pro 3: A dual-large language model approach in orthopaedic research](../evidence/vivekanantha-2026-dual-extraction.md) (peer-reviewed-study); locator: Results, PDF pp. 4-6; Tables 1-3, PDF pp. 5-8. Across eight orthopaedic studies, study-characteristic fields were both-model correct on 100% of fields, while secondary surgery details were both-model correct on 68.8%; at least one model was fully correct on 95.1% of all fields.
- **qualifies** — [Breaking the Extraction Bottleneck: A Single AI Agent Achieves Statistical Equivalence with Human-Extracted Meta-Analysis Data Across Five Agricultural Datasets](../evidence/halpern-2026-agricultural-extraction.md) (preprint); locator: Tables 4-9, PDF pp. 12-19; limitations, PDF pp. 26-27. This bioRxiv preprint reports pooled-effect equivalence across five agricultural datasets but depends on LLM-based record alignment and does not formally validate variance extraction; it is a qualified counterexample for aggregated effect estimates, not evidence of uniform item-level accuracy.
- **supports** — [Data Extractions Using a Large Language Model (Elicit) and Human Reviewers in Randomized Controlled Trials: A Systematic Comparison](../evidence/bianchi-2025.md) (peer-reviewed-study); locator: Results and Figure 1, PDF pp. 3-4. Across 20 trials, Elicit captured more or equivalent study-design information in every case, while 70% of intervention descriptions and 95% of intervention-effect extractions were incomplete.
- **supports** — [The Use of Artificial Intelligence in Dermatology Systematic Reviews: A Comparative Analysis of Elicit Against Human Reviewers](../evidence/vyas-2026.md) (peer-reviewed-study); locator: Results, PDF p. 1. Disease was extracted correctly for all 24 dermatology trials, while study location and Jadad-score inputs were wrong in 5 of 24 cases each.
- **supports** — [Using Artificial Intelligence Tools as Second Reviewers for Data Extraction in Systematic Reviews: A Performance Comparison of Two AI Tools Against Human Reviewers](../evidence/andersen-2025-second-reviewer.md) (peer-reviewed-study); locator: Results sections 4.1-4.2, PDF p. 5. Elicit found all study-design data in 30/30 articles and all outcome data in 22/30; ChatGPT counts were 29/30 and 21/30. Raw counts are used because abstract and discussion category percentages disagree.
- **qualifies** — [Language models for data extraction and risk of bias assessment in complementary medicine](../evidence/lai-2025-complementary-medicine.md) (peer-reviewed-study); locator: Table 1, PDF p. 4; Methods, p. 5. Moonshot outcomes accuracy was 97.64%, exceeding methods (90.86%) and data/analysis (91.33%); this 107-trial complementary-medicine evaluation is a counterexample to treating numerical outcomes as uniformly hardest.

### [Additional reasoning or self-reflection prompting does not consistently improve extraction accuracy and can increase processing time.](../claims/extraction-004.md)

**Status:** supported

- **supports** — [Performance of large language models and prompt engineering strategies for data extraction in systematic reviews](../evidence/oami-2026-extraction.md) (peer-reviewed-study); locator: Results, Tables 2-3 and Figure 4, PDF pp. 3-7. Chain-of-thought and self-reflection prompts produced only modest accuracy changes; self-reflection increased mean processing time compared with standard prompts.
- **supports** — [Assessing data extraction in randomized clinical trials with large language models](../evidence/yisha-2026-rct-extraction.md) (peer-reviewed-study); locator: Methods and Results, PDF pp. 2-4. LLM-modified prompts did not significantly change extraction accuracy compared with the original prompts in this 105-RCT proof-of-concept.
- **qualifies** — [What level of automation is 'good enough'? A benchmark of large language models for meta-analysis data extraction](../evidence/li-2026-extraction.md) (peer-reviewed-study); locator: Figures 2-3 and Table 3, PDF pp. 10-11. In contrast, customized task-specific prompts increased statistical-result recall by an average 14.8 percentage points, with a small average precision decrease.

### [Small workflow evaluations report that human-plus-LLM or complementary multi-LLM extraction can improve accuracy or coverage and reduce extraction time, while retaining a human verification role.](../claims/extraction-005.md)

**Status:** supported

- **supports** — [A foundation model for human-AI collaboration in medical literature mining](../evidence/wang-2025-leads.md) (peer-reviewed-study); locator: Results, Figure 5 and text, PDF pp. 8-9. In a pilot involving 90 clinical-trial publications and two medical researchers, the expert-plus-LEADS arm achieved accuracy 0.85 versus 0.80 for expert-only and reduced task time by 26.9%; authors note the pilot was small and expert oversight remains needed.
- **supports** — [Custom GPT models for complex rheumatology systematic reviews: A two-part evaluation of data extraction and prognosis appraisal](../evidence/munguia-realpozo-2026-custom-gpt.md) (peer-reviewed-study); locator: Results, Table 1 and Figure 1, PDF pp. 5-6. In 15 SLE metabolomics studies, customized GPT-4o extraction took a mean 5.7 minutes per study versus 30.4 minutes for human reviewers, but overall template concordance was 25.0%, supporting speed gains with substantial verification needs.
- **supports** — [Automated data extraction for systematic reviews using GPT-5.2 and Google Gemini Pro 3: A dual-large language model approach in orthopaedic research](../evidence/vivekanantha-2026-dual-extraction.md) (peer-reviewed-study); locator: Results, Tables 1-3, PDF pp. 5-8; Discussion, PDF pp. 8-9. Across eight studies, at least one of GPT-5.2 or Gemini 3 Pro was fully correct on 95.1% of 384 fields. The authors frame parallel LLMs as a human-verified first-pass approach; the adjudicator was not blinded to model outputs.
- **supports** — [Collaborative large language models for automated data extraction in living systematic reviews](../evidence/khan-2025-collaborative-extraction.md) (peer-reviewed-study); locator: Results, PDF pp. 4-6; Figure 3, p. 6. Among 391 held-out responses, 342 initially concordant outputs had accuracy 0.94 compared with 0.89 and 0.90 for the individual models. Only 25/49 discordant outputs became concordant after critique, with 0.76 accuracy in that subset; no workflow timing measured.
- **supports** — [Language models for data extraction and risk of bias assessment in complementary medicine](../evidence/lai-2025-complementary-medicine.md) (peer-reviewed-study); locator: Results and Figure 2, PDF pp. 2-3; Table 1, p. 4; Methods, p. 5. Human-assisted Moonshot extraction accuracy increased from 95.12% to 97.92%. Generation plus verification/modification took 14.7 min per trial; the 86.9-min manual benchmark came from prior literature, not a concurrent control.

### [Agreement between extraction models can identify a more accurate subset of outputs, but neither initial agreement nor agreement reached through cross-critique guarantees correctness.](../claims/extraction-006.md)

**Status:** supported

- **supports** — [Collaborative large language models for automated data extraction in living systematic reviews](../evidence/khan-2025-collaborative-extraction.md) (peer-reviewed-study); locator: Results, PDF pp. 4-6; Figure 3, p. 6. In 17 held-out publications, 342/391 initial concordant outputs were 94% accurate. Cross-critique made 25/49 discordant outputs concordant, but accuracy in this new-consensus subset was 76%. These are conditional subset accuracies, not an overall 94% accuracy estimate for all outputs.

## Connected concepts

- [Recall and sensitivity](../concepts/recall-and-sensitivity.md)
- [Precision](../concepts/precision.md)
- [Reference standards and ground truth](../concepts/reference-standards.md)
- [Human-in-the-loop verification](../concepts/human-in-the-loop-verification.md)
- [Reproducibility and output stability](../concepts/reproducibility-and-stability.md)
- [Automation bias and reviewer oversight](../concepts/automation-bias.md)
- [Error types in screening and extraction](../concepts/extraction-and-screening-errors.md)

## Open questions and evidence gaps

Record unresolved questions and evidence gaps here as they are identified during review.

## Peer-reviewed studies

- [OpenExtract: Automated Data Extraction for Systematic Reviews in Health](../evidence/achterberg-2026-openextract.md)
- [Using Artificial Intelligence Tools as Second Reviewers for Data Extraction in Systematic Reviews: A Performance Comparison of Two AI Tools Against Human Reviewers](../evidence/andersen-2025-second-reviewer.md)
- [AI-accelerated meta-analysis in psychology: Large language models code study properties with high accuracy](../evidence/azaad-2026-meta-analysis-coding.md)
- [Data Extractions Using a Large Language Model (Elicit) and Human Reviewers in Randomized Controlled Trials: A Systematic Comparison](../evidence/bianchi-2025.md)
- [Artificial Intelligence-Assisted Data Extraction With a Large Language Model: A Study Within Reviews](../evidence/gartlehner-2025.md)
- [Collaborative large language models for automated data extraction in living systematic reviews](../evidence/khan-2025-collaborative-extraction.md)
- [Language models for data extraction and risk of bias assessment in complementary medicine](../evidence/lai-2025-complementary-medicine.md)
- [What level of automation is 'good enough'? A benchmark of large language models for meta-analysis data extraction](../evidence/li-2026-extraction.md)
- [Custom GPT models for complex rheumatology systematic reviews: A two-part evaluation of data extraction and prognosis appraisal](../evidence/munguia-realpozo-2026-custom-gpt.md)
- [Performance of large language models and prompt engineering strategies for data extraction in systematic reviews](../evidence/oami-2026-extraction.md)
- [Automated data extraction for systematic reviews using GPT-5.2 and Google Gemini Pro 3: A dual-large language model approach in orthopaedic research](../evidence/vivekanantha-2026-dual-extraction.md)
- [The Use of Artificial Intelligence in Dermatology Systematic Reviews: A Comparative Analysis of Elicit Against Human Reviewers](../evidence/vyas-2026.md)
- [A foundation model for human-AI collaboration in medical literature mining](../evidence/wang-2025-leads.md)
- [Assessing data extraction in randomized clinical trials with large language models](../evidence/yisha-2026-rct-extraction.md)

## Preprints and unverified manuscripts

- [Breaking the Extraction Bottleneck: A Single AI Agent Achieves Statistical Equivalence with Human-Extracted Meta-Analysis Data Across Five Agricultural Datasets](../evidence/halpern-2026-agricultural-extraction.md) — bioRxiv preprint posted 2026-03-23
- [Diagnosing Structural Failures in LLM-Based Evidence Extraction for Meta-Analysis](../evidence/tan-2026-structural.md) — arXiv preprint posted 2026-02-11

## Independent experiments

No independent experiments are linked.

## Important uncertainties

No linked claim is currently flagged as provisional, uncertain, mixed, or contradicted.

Read the individual source records for study design, scope, and unresolved reporting discrepancies.

**Last reviewed:** 2026-09-26
