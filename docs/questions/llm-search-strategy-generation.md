> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**

# LLMs for search strategy generation and expansion

## Question

How reliably do large language models generate or expand literature-search queries for evidence synthesis?


## Overview

This question groups 2 claims linked to 2 source records.

## Current evidence

The relationships and source categories below come from the structured evidence records. Results are reported in each source's own review setting; this page does not pool them.

## Key claims

### [LLM-generated Boolean search strategies remain highly sensitive to model, prompt, validation, and seed-study choices, and generally do not match the recall of expert manual strategies without substantial precision tradeoffs.](../claims/search-001.md)

**Status:** supported

- **supports** — [Reassessing Large Language Model Boolean Query Generation for Systematic Reviews](../evidence/wang-2025-query.md) (peer-reviewed-study); locator: Tables 2-3, PDF pp. 6-7; Discussion and limitations, PDF p. 13. Across 71 CLEF TAR topics, the expert manual recall was 0.8436 while the best reported generated-query recall in Table 2 was 0.6545. On the seed collection, combining guided queries reached recall 0.7361 versus 0.7241 for manual queries but with very low precision; best-seed selection was post hoc.

### [Generative query expansion does not produce uniform retrieval gains across biomedical benchmarks; its effect depends on the expansion method and dataset and often changes ranking more than overall screening coverage.](../claims/search-002.md)

**Status:** supported

- **supports** — [A critical evaluation of generative query expansion on biomedical literature retrieval](../evidence/fang-2026-query.md) (peer-reviewed-study); locator: Table 2, PDF pp. 6-7; Discussion, PDF pp. 9-11. Across eight expansion methods and three LLMs, several BioASQ and PubMedQA results fell below the unexpanded baseline, while most TREC Precision Medicine configurations improved recall or nDCG. The authors characterize the main effect as reranking with limited screening-stage impact.

## Peer-reviewed studies

- [A critical evaluation of generative query expansion on biomedical literature retrieval](../evidence/fang-2026-query.md)
- [Reassessing Large Language Model Boolean Query Generation for Systematic Reviews](../evidence/wang-2025-query.md)

## Preprints and unverified manuscripts

No preprints or unverified manuscripts are linked.

## Independent experiments

No independent experiments are linked.

## Important uncertainties

No linked claim is currently flagged as provisional, uncertain, mixed, or contradicted.

Read the individual source records for study design, scope, and unresolved reporting discrepancies.

**Last reviewed:** 2026-09-25
