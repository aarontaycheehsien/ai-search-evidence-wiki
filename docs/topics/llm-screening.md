> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**

# LLMs for Citation Screening

## Research question

How well can large language models perform citation screening in evidence synthesis?


## Scope and review boundaries

Define the evidence-synthesis setting, eligible study types, and task boundaries here. Keep scope decisions explicit and source-backed where they depend on empirical evidence.

## Overview

This topic groups 10 claims linked to 14 source records.

## Current evidence

The relationships and source categories below come from the structured evidence records. Results are reported in each source's own review setting; this page does not pool them.

## Key claims

### [Observed sensitivity of LLM citation screening differs substantially between evaluated review datasets and decision rules.](../claims/screening-001.md)

**Status:** supported

- **supports** — [Assessing the Ability of ChatGPT to Screen Articles for Systematic Reviews](../evidence/syriani-2023.md) (preprint); locator: Table 10, PDF p. 19. GPT-3.5 recall ranged from 0.327 to 0.947 across five software-engineering review datasets.
- **supports** — [Sensitivity and Specificity of Using GPT-3.5 Turbo Models for Title and Abstract Screening in Systematic Reviews and Meta-analyses](../evidence/tran-2024.md) (peer-reviewed-study); locator: Table 2, PDF p. 7. Across five reviews, sensitivity was 81.1%-96.5% under the balanced rule and 94.6%-99.8% under the sensitive rule.
- **contextual** — [Can large language models replace humans in systematic reviews? Evaluating GPT-4's efficacy in screening and extracting data from peer-reviewed and grey literature in multiple languages](../evidence/khraisha-2024.md) (peer-reviewed-study); locator: Table 1, PDF p. 7. GPT-4 title/abstract sensitivity was 0.42 for balanced English peer-reviewed records, 0.48 for English grey literature, and 0.50 for other-language records.
- **supports** — [Evaluating the Effectiveness of Large Language Models in Abstract Screening: A Comparative Analysis](../evidence/li-2024.md) (peer-reviewed-study); locator: Tables 2-4, journal PDF pp. 9, 11-12. Published journal version: ChatGPT v4.0 sensitivity was 0.930, 0.812, and 0.932 in three selected datasets.
- **supports** — [Automated Paper Screening for Clinical Reviews Using Large Language Models: Data Analysis Study](../evidence/guo-2024.md) (peer-reviewed-study); locator: Table 3, PDF p. 5. Inclusion sensitivity ranged from 0.593 to 1.000 across six clinical review datasets; weighted overall sensitivity was 0.764.
- **supports** — [High-performance automated abstract screening with large language model ensembles](../evidence/sanghera-2025.md) (peer-reviewed-study); locator: Table 3, PDF p. 7. Across 119,695 records from 23 reviews, selected model-prompt combinations had sensitivity from 0.756 to 1.000.
- **supports** — [Development and evaluation of prompts for a large language model to screen titles and abstracts in a living systematic review](../evidence/homiar-2025.md) (peer-reviewed-study); locator: Table 3, PDF p. 4. Title/abstract sensitivity was 0.91 on the baseline set, 1.00 in update 1, and 0.58 in update 2; sensitivity for final full-text inclusions was 1.00 in each set.
- **supports** — [Development of Prompt Templates for Large Language Model-Driven Screening in Systematic Reviews](../evidence/cao-2025.md) (peer-reviewed-study); locator: PubMed abstract, Results (PMID 39993313). Abstract-only evidence: optimized-prompt sensitivity ranged from 86.7% to 100% across ten reviews, with weighted sensitivity 97.7%.

### [Overall screening accuracy alone can obscure lower sensitivity for citations that human reference standards included.](../claims/screening-002.md)

**Status:** supported

- **supports** — [Automated Paper Screening for Clinical Reviews Using Large Language Models: Data Analysis Study](../evidence/guo-2024.md) (peer-reviewed-study); locator: Table 3, PDF p. 5. Weighted accuracy was 0.907, whereas sensitivity for included records was 0.764; only 538 of 24,307 records were included by the reference standard.
- **supports** — [Can large language models replace humans in systematic reviews? Evaluating GPT-4's efficacy in screening and extracting data from peer-reviewed and grey literature in multiple languages](../evidence/khraisha-2024.md) (peer-reviewed-study); locator: Table 1, PDF p. 7. Other-language title/abstract accuracy was 0.88 with sensitivity 0.50; the stratum was highly imbalanced.
- **supports** — [Evaluating the Effectiveness of Large Language Models in Abstract Screening: A Comparative Analysis](../evidence/li-2024.md) (peer-reviewed-study); locator: Tables 3-4, journal PDF pp. 11-12. Published journal version: Google PaLM on Meijboom had accuracy 0.890 and sensitivity 0.647; ChatGPT v3.5 on Menon had accuracy 0.711 and sensitivity 0.315.
- **supports** — [Automated title and abstract screening for scoping reviews using the GPT-4 Large Language Model](../evidence/wilkins-2023.md) (preprint); locator: Results, PDF p. 7. Preprint: GPTscreenR accuracy was 84% while weighted sensitivity was 71%.
- **contextual** — [High-performance automated abstract screening with large language model ensembles](../evidence/sanghera-2025.md) (peer-reviewed-study); locator: Table 3, PDF p. 7. On 119,695 low-prevalence search results, selected model-prompt combinations had positive predictive values of 0.004-0.096 despite balanced accuracies of 0.710-0.926; this illustrates a different misleading summary-metric problem.

### [Several evaluated LLM screening workflows missed eligible citations under their reference standards, so automatic exclusion can omit studies.](../claims/screening-003.md)

**Status:** supported

- **supports** — [Automated Paper Screening for Clinical Reviews Using Large Language Models: Data Analysis Study](../evidence/guo-2024.md) (peer-reviewed-study); locator: Table 3 and Discussion, PDF pp. 5, 7-8. Inclusion sensitivity was 0.764 overall; the authors caution that relevant papers may be omitted.
- **supports** — [Can large language models replace humans in systematic reviews? Evaluating GPT-4's efficacy in screening and extracting data from peer-reviewed and grey literature in multiple languages](../evidence/khraisha-2024.md) (peer-reviewed-study); locator: Table 1, PDF p. 7. GPT-4 title/abstract sensitivity was 0.42-0.50 across the reported literature strata.
- **supports** — [Evaluating the Effectiveness of Large Language Models in Abstract Screening: A Comparative Analysis](../evidence/li-2024.md) (peer-reviewed-study); locator: Tables 2-4, journal PDF pp. 9, 11-12. Published journal version: ChatGPT v4.0 sensitivity was below 1.0 on each of the three selected datasets.
- **supports** — [Assessing the Ability of ChatGPT to Screen Articles for Systematic Reviews](../evidence/syriani-2023.md) (preprint); locator: Table 10, PDF p. 19. GPT-3.5 recall was 0.327 on MobileMDE and below 1.0 on all five reported datasets.
- **supports** — [Sensitivity and Specificity of Using GPT-3.5 Turbo Models for Title and Abstract Screening in Systematic Reviews and Meta-analyses](../evidence/tran-2024.md) (peer-reviewed-study); locator: Table 3, PDF p. 8. With the sensitivity-optimized trimming rule, full-text inclusions missed were 1/26, 0/8, 1/200, 0/29, and 11/445 across the five reviews. This table conflicts with the paper's smaller abstract summary.
- **supports** — [Automated title and abstract screening for scoping reviews using the GPT-4 Large Language Model](../evidence/wilkins-2023.md) (preprint); locator: Results, PDF p. 7. Preprint: 71% weighted sensitivity across 1,147 records in six scoping reviews.
- **supports** — [High-performance automated abstract screening with large language model ensembles](../evidence/sanghera-2025.md) (peer-reviewed-study); locator: Table 3, PDF p. 7. Four of five selected model-prompt combinations had sensitivity below 1.0 on the comprehensive 119,695-record dataset.
- **contextual** — [Development and evaluation of prompts for a large language model to screen titles and abstracts in a living systematic review](../evidence/homiar-2025.md) (peer-reviewed-study); locator: Table 3, PDF p. 4. This single living-review evaluation retained all final full-text inclusions, while title/abstract sensitivity fell to 0.58 in one update; the reference-standard stage changes the interpretation.

### [Changing the information supplied to an LLM or the decision rule used to interpret its output can alter screening performance.](../claims/screening-004.md)

**Status:** supported

- **supports** — [Harnessing the Power of ChatGPT for Automating Systematic Review Process: Methodology, Case Study, Limitations, and Future Directions](../evidence/alshami-2023.md) (peer-reviewed-study); locator: Section 3.2 and Figure 9, PDF pp. 17-20. On a 120-record subset, adding abstracts to APA metadata raised the 'not related' class F1 from 81% to 90% and recall from 80% to 93%.
- **supports** — [Sensitivity and Specificity of Using GPT-3.5 Turbo Models for Title and Abstract Screening in Systematic Reviews and Meta-analyses](../evidence/tran-2024.md) (peer-reviewed-study); locator: Table 2, PDF p. 7. The sensitive rule raised sensitivity to 94.6%-99.8% while specificity fell to 2.2%-46.6%, compared with 81.1%-96.5% sensitivity and 25.8%-80.4% specificity under the balanced rule.
- **contextual** — [Evaluating the Effectiveness of Large Language Models in Abstract Screening: A Comparative Analysis](../evidence/li-2024.md) (peer-reviewed-study); locator: Tables 2-4, journal PDF pp. 9, 11-12. Published journal version: majority voting changed sensitivity and specificity compared with individual models, in different directions by dataset.
- **qualifies** — [Can large language models replace humans in systematic reviews? Evaluating GPT-4's efficacy in screening and extracting data from peer-reviewed and grey literature in multiple languages](../evidence/khraisha-2024.md) (peer-reviewed-study); locator: Methods and Table 1, PDF pp. 3-4, 7. Prompt reliability differed by criterion, but the high-reliability subgroup was also imbalanced; its result cannot isolate a prompt effect.
- **supports** — [Development of Prompt Templates for Large Language Model-Driven Screening in Systematic Reviews](../evidence/cao-2025.md) (peer-reviewed-study); locator: PubMed abstract, Results (PMID 39993313). Abstract-only evidence: optimized prompts had 97.7% weighted sensitivity in abstract screening across ten reviews versus 49.0% for zero-shot prompts.
- **supports** — [Testing the utility of GPT for title and abstract screening in environmental systematic evidence synthesis](../evidence/nykvist-2025.md) (peer-reviewed-study); locator: Table 1, PDF p. 3. In one environmental review, GPT-4 recall was 1.00 at cutoff 0.5 and 0.96 at cutoff 0.8, while work saved over sampling rose from 0.55 to 0.75.
- **supports** — [High-performance automated abstract screening with large language model ensembles](../evidence/sanghera-2025.md) (peer-reviewed-study); locator: Table 4, PDF p. 9. Across 119,695 records, parallel ensemble rules with sensitivity 1.000 had calculated workload reductions of 37.55%-41.81%; series rules saved more screening but had lower sensitivity.

### [In a six-review scoping-review evaluation, a chain-of-thought GPT-4 screening workflow performed similarly to a zero-shot workflow.](../claims/screening-005.md)

**Status:** provisional

- **supports** — [Automated title and abstract screening for scoping reviews using the GPT-4 Large Language Model](../evidence/wilkins-2023.md) (preprint); locator: Results, PDF p. 7. Preprint: GPTscreenR accuracy/sensitivity/specificity were 84%/71%/89%, versus 83%/72%/87% for the zero-shot comparator on the same 1,147 records.

### [In a retrospective five-review evaluation, using GPT-3.5 as a second reviewer or to trim citations involved a tradeoff between manual work and missed eligible records.](../claims/screening-006.md)

**Status:** provisional

- **supports** — [Sensitivity and Specificity of Using GPT-3.5 Turbo Models for Title and Abstract Screening in Systematic Reviews and Meta-analyses](../evidence/tran-2024.md) (peer-reviewed-study); locator: Results, Discussion, Tables 2-3, PDF pp. 2, 7-8. Balanced-rule recommendations added 10,279 false positives across 22,665 citations for reconciliation. Sensitive-rule trimming removed 2.0%-45.4% of citations by review, while Table 3 shows 0-11 full-text inclusions missed by review. Retrospective design does not establish prospective workload savings.
- **contextual** — [Assessing the Ability of ChatGPT to Screen Articles for Systematic Reviews](../evidence/syriani-2023.md) (preprint); locator: Section 6.2, PDF pp. 21-24. The manuscript models work saved over sampling in software-engineering reviews; it does not test the same human-plus-LLM workflow as Tran et al.

### [Evaluated LLM screening workflows yielded calculated reductions in manual screening volume, with the amount saved dependent on the decision rule and observed sensitivity.](../claims/screening-007.md)

**Status:** supported

- **supports** — [High-performance automated abstract screening with large language model ensembles](../evidence/sanghera-2025.md) (peer-reviewed-study); locator: Table 4, PDF p. 9. On 119,695 retrospective records, perfect-sensitivity parallel ensembles had calculated workload reductions of 37.55%-41.81%; a series ensemble reached 99.13% with sensitivity 0.6900. These are modeled record counts, not observed reviewer time.
- **supports** — [Development and evaluation of prompts for a large language model to screen titles and abstracts in a living systematic review](../evidence/homiar-2025.md) (peer-reviewed-study); locator: Table 3, PDF p. 4. Simulated manual-screening reductions were 65.72% in the baseline set and 79.04% and 85.63% in two updates, with title/abstract sensitivity 0.91, 1.00, and 0.58 respectively.
- **supports** — [Testing the utility of GPT for title and abstract screening in environmental systematic evidence synthesis](../evidence/nykvist-2025.md) (peer-reviewed-study); locator: Table 1 and Results, PDF pp. 3-4. In one environmental review, work saved over sampling rose from 0.55 at cutoff 0.5 to 0.75 at cutoff 0.8, while recall fell from 1.00 to 0.96.
- **contextual** — [Audited large language model triage for systematic review screening in national clinical guideline production: validation and prospective deployment](../evidence/fagerberg-2026.md) (preprint); locator: Table 1 and note, PDF pp. 7-8. Preprint prospective deployment routed 10,821 of 74,679 records to routine human review and estimated 34 versus 415 first-pass person-days; time was modeled and implementation overhead omitted.

### [In a four-reviewer comparison, reviewers given LLM-generated PICOS summaries screened the same citation set faster and had higher observed sensitivity than reviewers who saw titles and abstracts alone.](../claims/screening-008.md)

**Status:** provisional

- **supports** — [Do it faster with PICOS: Generative AI-Assisted systematic review screening](../evidence/vallamchetla-2025.md) (peer-reviewed-study); locator: PubMed abstract, Methods and Results (PMID 40447171). Abstract-only evidence: on 1,003 records, assisted reviewers took 116 and 90 minutes versus 463 and 370 minutes for unassisted reviewers; reported sensitivities were 100% versus 88% and 92%. Four distinct trainees were compared, so the observed difference does not isolate a causal effect of the summaries.

### [A 2026 preprint reports prospective audited LLM triage in two national guideline programmes, with no confirmed final false negatives among sampled AI-excluded records after post-unblinding adjudication.](../claims/screening-009.md)

**Status:** provisional

- **supports** — [Audited large language model triage for systematic review screening in national clinical guideline production: validation and prospective deployment](../evidence/fagerberg-2026.md) (preprint); locator: Table 1 and Results, PDF pp. 7-9. The locked ensemble placed 63,858 of 74,679 records in the AI-excluded pool. In 600 sampled AI-excluded records, none was a confirmed final false negative after unblinding; all 38 finally retained records in the 680-record completed audit had been AI flagged. The final standard incorporated AI outputs, and the sample cannot rule out rare or review-local misses.

### [In one umbrella-review workflow study, Elicit screening on a shared 324-record corpus recovered most traditionally included studies but selected many additional records that reviewers judged ineligible.](../claims/screening-010.md)

**Status:** provisional

- **supports** — [Evaluating Elicit’s systematic reviews workflow in an umbrella review on air pollution and acute lower respiratory infections: a methodological study for quality appraisal](../evidence/mazzali-2026.md) (peer-reviewed-study); locator: Results, PDF p. 7 (title/abstract stage) and p. 8 (full-text stage); abstract, p. 1. At title/abstract screening, Elicit selected 70 records versus 33 traditionally, with 30 overlapping (recall 90.9%, 95% CI 75.7–98.1; precision 42.9%, 95% CI 31.1–55.3). Full-text selection had recall 100% and precision 62.5%. This comparison applies Elicit functions to the same 324 records; the separate natural-language retrieval set overlapped the traditional search by only 8%, so this does not establish end-to-end search recall.

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

- [Harnessing the Power of ChatGPT for Automating Systematic Review Process: Methodology, Case Study, Limitations, and Future Directions](../evidence/alshami-2023.md)
- [Development of Prompt Templates for Large Language Model-Driven Screening in Systematic Reviews](../evidence/cao-2025.md)
- [Automated Paper Screening for Clinical Reviews Using Large Language Models: Data Analysis Study](../evidence/guo-2024.md)
- [Development and evaluation of prompts for a large language model to screen titles and abstracts in a living systematic review](../evidence/homiar-2025.md)
- [Can large language models replace humans in systematic reviews? Evaluating GPT-4's efficacy in screening and extracting data from peer-reviewed and grey literature in multiple languages](../evidence/khraisha-2024.md)
- [Evaluating the Effectiveness of Large Language Models in Abstract Screening: A Comparative Analysis](../evidence/li-2024.md)
- [Evaluating Elicit’s systematic reviews workflow in an umbrella review on air pollution and acute lower respiratory infections: a methodological study for quality appraisal](../evidence/mazzali-2026.md)
- [Testing the utility of GPT for title and abstract screening in environmental systematic evidence synthesis](../evidence/nykvist-2025.md)
- [High-performance automated abstract screening with large language model ensembles](../evidence/sanghera-2025.md)
- [Sensitivity and Specificity of Using GPT-3.5 Turbo Models for Title and Abstract Screening in Systematic Reviews and Meta-analyses](../evidence/tran-2024.md)
- [Do it faster with PICOS: Generative AI-Assisted systematic review screening](../evidence/vallamchetla-2025.md)

## Preprints and unverified manuscripts

- [Audited large language model triage for systematic review screening in national clinical guideline production: validation and prospective deployment](../evidence/fagerberg-2026.md) — medRxiv preprint posted 3 June 2026; not peer reviewed
- [Assessing the Ability of ChatGPT to Screen Articles for Systematic Reviews](../evidence/syriani-2023.md) — arXiv preprint submitted 12 July 2023
- [Automated title and abstract screening for scoping reviews using the GPT-4 Large Language Model](../evidence/wilkins-2023.md) — arXiv preprint version 1, 14 November 2023

## Independent experiments

No independent experiments are linked.

## Important uncertainties

- [In a six-review scoping-review evaluation, a chain-of-thought GPT-4 screening workflow performed similarly to a zero-shot workflow.](../claims/screening-005.md) is marked **provisional**.
- [In a retrospective five-review evaluation, using GPT-3.5 as a second reviewer or to trim citations involved a tradeoff between manual work and missed eligible records.](../claims/screening-006.md) is marked **provisional**.
- [In a four-reviewer comparison, reviewers given LLM-generated PICOS summaries screened the same citation set faster and had higher observed sensitivity than reviewers who saw titles and abstracts alone.](../claims/screening-008.md) is marked **provisional**.
- [A 2026 preprint reports prospective audited LLM triage in two national guideline programmes, with no confirmed final false negatives among sampled AI-excluded records after post-unblinding adjudication.](../claims/screening-009.md) is marked **provisional**.
- [In one umbrella-review workflow study, Elicit screening on a shared 324-record corpus recovered most traditionally included studies but selected many additional records that reviewers judged ineligible.](../claims/screening-010.md) is marked **provisional**.

Read the individual source records for study design, scope, and unresolved reporting discrepancies.

**Last reviewed:** 2026-09-25
