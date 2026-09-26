> **THIS FILE IS GENERATED. DO NOT EDIT DIRECTLY.**

# Claims

Claims and their evidence relationships are generated from `data/claims/`.

- [Standalone general-purpose LLMs have not demonstrated sufficient agreement or diagnostic performance for autonomous risk-of-bias and evidence-appraisal judgments.](appraisal-001.md) — **supported**
- [Human-LLM agreement workflows may improve simpler checklist-based appraisal, but the apparent benefit falls sharply for appraisal tasks requiring complex contextual judgment.](appraisal-002.md) — **provisional**
- [Elicit has shown higher precision but lower sensitivity than completed evidence-synthesis searches in retrospective comparisons; its output has also varied across repeated searches.](assistant-001.md) — **mixed**
- [Independent tool comparisons report different retrieval relevance and coverage profiles across query sets; current evidence does not establish a general-purpose winner over conventional library search.](assistant-002.md) — **mixed**
- [One single-domain study reported high Consensus precision on a specialized tissue-engineering query, while broader comparative studies do not support treating that result as a stable cross-domain performance estimate.](assistant-003.md) — **provisional**
- [A small rubric study rated Undermind and paid Elicit highly, but its low interrater agreement makes these ratings preliminary; Undermind’s quantified search-performance claims come from a vendor-authored benchmark.](assistant-004.md) — **provisional**
- [Elicit data-extraction evaluations report imperfect accuracy that varies by field and evidence base, supporting human verification rather than autonomous use.](assistant-005.md) — **mixed**
- [User-facing evaluations identify speed and ease of use as benefits of Elicit, alongside concerns about generated-abstract accuracy, brevity, and transparency of result counts.](assistant-006.md) — **provisional**
- [Verifying that an LLM cites real papers is insufficient to establish evidence fidelity because the generated claims may still misstate, overstate, or contradict those papers.](citation-001.md) — **supported**
- [Automated and semi-automated deduplication tools show different tradeoffs between removing unique records, retaining duplicates, and reviewer time, so no single evaluated tool is best for every review workflow.](dedup-001.md) — **supported**
- [In one prospective study within reviews, human-verified LLM extraction was slightly more accurate and faster than a conventional human-only workflow, while both approaches retained consequential errors.](extraction-001.md) — **supported**
- [Current LLM data extraction can be precise yet incomplete, with omissions as the dominant error; task-specific prompts improve recall but do not remove the need for human verification of meta-analytic data.](extraction-002.md) — **supported**
- [Observed sensitivity of LLM citation screening differs substantially between evaluated review datasets and decision rules.](screening-001.md) — **supported**
- [Overall screening accuracy alone can obscure lower sensitivity for citations that human reference standards included.](screening-002.md) — **supported**
- [Several evaluated LLM screening workflows missed eligible citations under their reference standards, so automatic exclusion can omit studies.](screening-003.md) — **supported**
- [Changing the information supplied to an LLM or the decision rule used to interpret its output can alter screening performance.](screening-004.md) — **supported**
- [In a six-review scoping-review evaluation, a chain-of-thought GPT-4 screening workflow performed similarly to a zero-shot workflow.](screening-005.md) — **provisional**
- [In a retrospective five-review evaluation, using GPT-3.5 as a second reviewer or to trim citations involved a tradeoff between manual work and missed eligible records.](screening-006.md) — **provisional**
- [Evaluated LLM screening workflows yielded calculated reductions in manual screening volume, with the amount saved dependent on the decision rule and observed sensitivity.](screening-007.md) — **supported**
- [In a four-reviewer comparison, reviewers given LLM-generated PICOS summaries screened the same citation set faster and had higher observed sensitivity than reviewers who saw titles and abstracts alone.](screening-008.md) — **provisional**
- [A 2026 preprint reports prospective audited LLM triage in two national guideline programmes, with no confirmed final false negatives among sampled AI-excluded records after post-unblinding adjudication.](screening-009.md) — **provisional**
- [In one umbrella-review workflow study, Elicit screening on a shared 324-record corpus recovered most traditionally included studies but selected many additional records that reviewers judged ineligible.](screening-010.md) — **provisional**
- [LLM-generated Boolean search strategies remain highly sensitive to model, prompt, validation, and seed-study choices, and generally do not match the recall of expert manual strategies without substantial precision tradeoffs.](search-001.md) — **supported**
- [Generative query expansion does not produce uniform retrieval gains across biomedical benchmarks; its effect depends on the expansion method and dataset and often changes ranking more than overall screening coverage.](search-002.md) — **supported**
- [LLM-generated Boolean strategies can contain invalid syntax, fabricated or incorrect controlled-vocabulary terms, and substantial run-to-run variation, so generated queries need technical and subject review before use.](search-003.md) — **supported**
- [Fine-tuning and multi-stage query construction can improve Boolean-search recall on specific evidence-synthesis benchmarks, but reported performance depends on dataset and evaluation depth, and may trade precision or workload.](search-004.md) — **supported**
