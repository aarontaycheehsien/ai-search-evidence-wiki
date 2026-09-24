> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**

# LLMs for Citation Screening

## Question

How well can large language models perform citation screening in evidence synthesis?


## Overview

This question groups 6 claims linked to 7 source records.

## Current evidence

The relationships and source categories below come from the structured evidence records. Results are reported in each source's own review setting; this page does not pool them.

## Key claims

### [Observed sensitivity of LLM citation screening differs substantially between evaluated review datasets and decision rules.](../claims/screening-001.md)

**Status:** supported

- **supports** — [Assessing the Ability of ChatGPT to Screen Articles for Systematic Reviews](../evidence/syriani-2023.md) (preprint); locator: Table 10, PDF p. 19. GPT-3.5 recall ranged from 0.327 to 0.947 across five software-engineering review datasets.
- **supports** — [Sensitivity and Specificity of Using GPT-3.5 Turbo Models for Title and Abstract Screening in Systematic Reviews and Meta-analyses](../evidence/tran-2024.md) (peer-reviewed-study); locator: Table 2, PDF p. 7. Across five reviews, sensitivity was 81.1%-96.5% under the balanced rule and 94.6%-99.8% under the sensitive rule.
- **contextual** — [Can large language models replace humans in systematic reviews? Evaluating GPT-4's efficacy in screening and extracting data from peer-reviewed and grey literature in multiple languages](../evidence/khraisha-2024.md) (peer-reviewed-study); locator: Table 1, PDF p. 7. GPT-4 title/abstract sensitivity was 0.42 for balanced English peer-reviewed records, 0.48 for English grey literature, and 0.50 for other-language records.
- **supports** — [Evaluating the Effectiveness of Large Language Models in Abstract Screening: A Comparative Analysis](../evidence/li-2024.md) (preprint); locator: Tables 2-4, PDF pp. 15, 17, 19. Preprint: ChatGPT v4.0 sensitivity was 0.930, 0.812, and 0.932 in three selected datasets.
- **supports** — [Automated Paper Screening for Clinical Reviews Using Large Language Models: Data Analysis Study](../evidence/guo-2024.md) (peer-reviewed-study); locator: Table 3, PDF p. 5. Inclusion sensitivity ranged from 0.593 to 1.000 across six clinical review datasets; weighted overall sensitivity was 0.764.

### [Overall screening accuracy alone can obscure lower sensitivity for citations that human reference standards included.](../claims/screening-002.md)

**Status:** supported

- **supports** — [Automated Paper Screening for Clinical Reviews Using Large Language Models: Data Analysis Study](../evidence/guo-2024.md) (peer-reviewed-study); locator: Table 3, PDF p. 5. Weighted accuracy was 0.907, whereas sensitivity for included records was 0.764; only 538 of 24,307 records were included by the reference standard.
- **supports** — [Can large language models replace humans in systematic reviews? Evaluating GPT-4's efficacy in screening and extracting data from peer-reviewed and grey literature in multiple languages](../evidence/khraisha-2024.md) (peer-reviewed-study); locator: Table 1, PDF p. 7. Other-language title/abstract accuracy was 0.88 with sensitivity 0.50; the stratum was highly imbalanced.
- **supports** — [Evaluating the Effectiveness of Large Language Models in Abstract Screening: A Comparative Analysis](../evidence/li-2024.md) (preprint); locator: Tables 3-4, PDF pp. 17, 19. Preprint: for example, Google PaLM on Meijboom had accuracy 0.890 and sensitivity 0.647; ChatGPT v3.5 on Menon had accuracy 0.711 and sensitivity 0.315.
- **supports** — [Automated title and abstract screening for scoping reviews using the GPT-4 Large Language Model](../evidence/wilkins-2023.md) (preprint); locator: Results, PDF p. 7. Preprint: GPTscreenR accuracy was 84% while weighted sensitivity was 71%.

### [Several evaluated LLM screening workflows missed eligible citations under their reference standards, so automatic exclusion can omit studies.](../claims/screening-003.md)

**Status:** supported

- **supports** — [Automated Paper Screening for Clinical Reviews Using Large Language Models: Data Analysis Study](../evidence/guo-2024.md) (peer-reviewed-study); locator: Table 3 and Discussion, PDF pp. 5, 7-8. Inclusion sensitivity was 0.764 overall; the authors caution that relevant papers may be omitted.
- **supports** — [Can large language models replace humans in systematic reviews? Evaluating GPT-4's efficacy in screening and extracting data from peer-reviewed and grey literature in multiple languages](../evidence/khraisha-2024.md) (peer-reviewed-study); locator: Table 1, PDF p. 7. GPT-4 title/abstract sensitivity was 0.42-0.50 across the reported literature strata.
- **supports** — [Evaluating the Effectiveness of Large Language Models in Abstract Screening: A Comparative Analysis](../evidence/li-2024.md) (preprint); locator: Tables 2-4, PDF pp. 15, 17, 19. Preprint: ChatGPT v4.0 sensitivity was below 1.0 on each of the three selected datasets.
- **supports** — [Assessing the Ability of ChatGPT to Screen Articles for Systematic Reviews](../evidence/syriani-2023.md) (preprint); locator: Table 10, PDF p. 19. GPT-3.5 recall was 0.327 on MobileMDE and below 1.0 on all five reported datasets.
- **supports** — [Sensitivity and Specificity of Using GPT-3.5 Turbo Models for Title and Abstract Screening in Systematic Reviews and Meta-analyses](../evidence/tran-2024.md) (peer-reviewed-study); locator: Table 3, PDF p. 8. With the sensitivity-optimized trimming rule, full-text inclusions missed were 1/26, 0/8, 1/200, 0/29, and 11/445 across the five reviews. This table conflicts with the paper's smaller abstract summary.
- **supports** — [Automated title and abstract screening for scoping reviews using the GPT-4 Large Language Model](../evidence/wilkins-2023.md) (preprint); locator: Results, PDF p. 7. Preprint: 71% weighted sensitivity across 1,147 records in six scoping reviews.

### [Changing the information supplied to an LLM or the decision rule used to interpret its output can alter screening performance.](../claims/screening-004.md)

**Status:** supported

- **supports** — [Harnessing the Power of ChatGPT for Automating Systematic Review Process: Methodology, Case Study, Limitations, and Future Directions](../evidence/alshami-2023.md) (peer-reviewed-study); locator: Section 3.2 and Figure 9, PDF pp. 17-20. On a 120-record subset, adding abstracts to APA metadata raised the 'not related' class F1 from 81% to 90% and recall from 80% to 93%.
- **supports** — [Sensitivity and Specificity of Using GPT-3.5 Turbo Models for Title and Abstract Screening in Systematic Reviews and Meta-analyses](../evidence/tran-2024.md) (peer-reviewed-study); locator: Table 2, PDF p. 7. The sensitive rule raised sensitivity to 94.6%-99.8% while specificity fell to 2.2%-46.6%, compared with 81.1%-96.5% sensitivity and 25.8%-80.4% specificity under the balanced rule.
- **contextual** — [Evaluating the Effectiveness of Large Language Models in Abstract Screening: A Comparative Analysis](../evidence/li-2024.md) (preprint); locator: Tables 2-4, PDF pp. 15, 17, 19. Preprint: majority voting changed sensitivity and specificity compared with individual models, in different directions by dataset.
- **qualifies** — [Can large language models replace humans in systematic reviews? Evaluating GPT-4's efficacy in screening and extracting data from peer-reviewed and grey literature in multiple languages](../evidence/khraisha-2024.md) (peer-reviewed-study); locator: Methods and Table 1, PDF pp. 3-4, 7. Prompt reliability differed by criterion, but the high-reliability subgroup was also imbalanced; its result cannot isolate a prompt effect.

### [In a six-review scoping-review evaluation, a chain-of-thought GPT-4 screening workflow performed similarly to a zero-shot workflow.](../claims/screening-005.md)

**Status:** provisional

- **supports** — [Automated title and abstract screening for scoping reviews using the GPT-4 Large Language Model](../evidence/wilkins-2023.md) (preprint); locator: Results, PDF p. 7. Preprint: GPTscreenR accuracy/sensitivity/specificity were 84%/71%/89%, versus 83%/72%/87% for the zero-shot comparator on the same 1,147 records.

### [In a retrospective five-review evaluation, using GPT-3.5 as a second reviewer or to trim citations involved a tradeoff between manual work and missed eligible records.](../claims/screening-006.md)

**Status:** provisional

- **supports** — [Sensitivity and Specificity of Using GPT-3.5 Turbo Models for Title and Abstract Screening in Systematic Reviews and Meta-analyses](../evidence/tran-2024.md) (peer-reviewed-study); locator: Results, Discussion, Tables 2-3, PDF pp. 2, 7-8. Balanced-rule recommendations added 10,279 false positives across 22,665 citations for reconciliation. Sensitive-rule trimming removed 2.0%-45.4% of citations by review, while Table 3 shows 0-11 full-text inclusions missed by review. Retrospective design does not establish prospective workload savings.
- **contextual** — [Assessing the Ability of ChatGPT to Screen Articles for Systematic Reviews](../evidence/syriani-2023.md) (preprint); locator: Section 6.2, PDF pp. 21-24. The manuscript models work saved over sampling in software-engineering reviews; it does not test the same human-plus-LLM workflow as Tran et al.

## Peer-reviewed studies

- [Harnessing the Power of ChatGPT for Automating Systematic Review Process: Methodology, Case Study, Limitations, and Future Directions](../evidence/alshami-2023.md)
- [Automated Paper Screening for Clinical Reviews Using Large Language Models: Data Analysis Study](../evidence/guo-2024.md)
- [Can large language models replace humans in systematic reviews? Evaluating GPT-4's efficacy in screening and extracting data from peer-reviewed and grey literature in multiple languages](../evidence/khraisha-2024.md)
- [Sensitivity and Specificity of Using GPT-3.5 Turbo Models for Title and Abstract Screening in Systematic Reviews and Meta-analyses](../evidence/tran-2024.md)

## Preprints and unverified manuscripts

- [Evaluating the Effectiveness of Large Language Models in Abstract Screening: A Comparative Analysis](../evidence/li-2024.md) — Research Square preprint posted 27 March 2024; journal status not established by this PDF
- [Assessing the Ability of ChatGPT to Screen Articles for Systematic Reviews](../evidence/syriani-2023.md) — arXiv preprint submitted 12 July 2023
- [Automated title and abstract screening for scoping reviews using the GPT-4 Large Language Model](../evidence/wilkins-2023.md) — arXiv preprint version 1, 14 November 2023

## Independent experiments

No independent experiments are linked.

## Important uncertainties

- [In a six-review scoping-review evaluation, a chain-of-thought GPT-4 screening workflow performed similarly to a zero-shot workflow.](../claims/screening-005.md) is marked **provisional**.
- [In a retrospective five-review evaluation, using GPT-3.5 as a second reviewer or to trim citations involved a tradeoff between manual work and missed eligible records.](../claims/screening-006.md) is marked **provisional**.

Read the individual source records for study design, scope, and unresolved reporting discrepancies.

**Last reviewed:** 2026-09-25
