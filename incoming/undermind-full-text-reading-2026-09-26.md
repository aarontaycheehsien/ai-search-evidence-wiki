# Undermind full-text reading audit, 2026-09-26

These are Undermind read_pdfs responses, not locally downloaded PDFs or verbatim full text. Each question requested source locations and separated measured results from interpretation. Source records and claims retain study limitations. Local PDF download was blocked by the environment network restriction.

+[Gau26]:
### Evidence Wiki Record: [Gau26]

---

#### 1. Document Metadata
* **Exact Title:** How Researchers Navigate Accountability, Transparency, and Trust When Using AI Tools in Early-Stage Research: A Think-Aloud Study
* **Complete Author Names (as printed):** Sanjana Gautam, Houjiang Liu, Yujin Choi, Matthew Lease *(Page 1)*
* **Venue:** Proceedings of the 9th ACM Conference on Fairness, Accountability, and Transparency (FAccT’26), June 25–28, 2026, Montreal, Canada *(Pages 1, 2)*
* **Publication / Preprint Status:** Conference publication (FAccT'26) / arXiv preprint (`arXiv:2604.23136v1 [cs.CY] 25 Apr 2026`) *(Page 1)*
* **DOI:** `https://doi.org/XXXXXXX.XXXXXXX` *(Placeholder in preprint text; no resolved numerical DOI is provided)* *(Page 1)*

---

#### 2. Study Design & Methodology
* **Design:** Qualitative, remote think-aloud study (60–90 minutes per session via Zoom on participants’ personal computers). The protocol comprised:
  1. *Pre-task questionnaire* (background, prior AI use, perceived learning curves).
  2. *Five think-aloud tasks*:
     * Task 1: Exploration in a new domain using a preferred LLM tool.
     * Task 2: Thread identification and synthesis using Research Rabbit.
     * Task 3: In-depth thread exploration and query formulation using Elicit AI.
     * Task 4: Evaluation of AI-generated summaries and outlines using Elicit AI.
     * Task 5: Reflection on personal workflows (semi-structured interview).
  3. *Post-task questionnaire* (reflections on workflow efficiency, output quality).
  4. *Data analysis:* Inductive open coding (yielding 23 sub-themes) followed by axial coding and theoretical grouping into three core Responsible AI (RAI) constructs: accountability, transparency, and trust *(Section 3, 3.2.1–3.2.5, 4, pages 3–5)*.
* **Sample:** $N = 15$ researchers:
  * 11 doctoral students (predominantly advanced PhD candidates)
  * 2 postdoctoral researchers
  * 1 faculty member (Associate Professor)
  * 1 industry researcher
  * Demographics: 8 Female, 7 Male, across diverse disciplines (Steel Industry, Astrophysics, AI Journalism, VR & Mental Health, Misinformation Studies, AI & Religion, Neuroscience, Biomedical Imaging, Industrial Labor History, Climate Science, Autonomous Driving, Library Sciences, Technology for Older Adults, Education Technology, Sociotechnical Design) *(Section 3.1, page 3; Table 1, page 4)*.

The following table provides the complete demographic breakdown of the 15 participants in the think-aloud study, listing their participant IDs, gender, research seniority, and specific disciplinary fields:
[REGION: page=4, bbox=103,243,344,755]

* **Tools & Versions:**
  * **Research Rabbit:** Commercial graph-based literature discovery tool; version not specified *(Section 3.2.1, page 3)*.
  * **ElicitAI / Elicit:** Commercial generative literature-grounded synthesis tool (evaluated under a lowest-tier commercial subscription plan); version not specified *(Section 3.2.1, page 3; Section 3.2.2 note, page 4)*.
  * *Other mentioned tools:* Participants referred to prior or initial exploratory use of ChatGPT and Perplexity *(Section 4.1.1, 4.3.4, pages 5, 8)*.
* **Comparator:**
  * No experimental baseline group, control condition, or benchmark system was evaluated. Comparisons were made against participants' traditional non-AI research practices and established academic platforms (e.g., Google Scholar, Semantic Scholar, Zotero, Mendeley) *(Section 3.2, 5.1, pages 3, 9)*.

---

#### 3. Exact Numerical Findings Relevant to Retrieval, Usability, Screening, or Extraction
The study did **not** record or compute automated quantitative benchmark metrics (e.g., precision, recall, mean average precision, extraction F1, or System Usability Scale scores). All empirical numerical results consist of participant counts and theme frequencies across the $N=15$ researchers:

The following table summarizes the overarching thematic findings, mapping the specific tensions and concerns identified under RQ1 to the compensatory strategies developed by participants under RQ2 across Accountability, Transparency, and Trust:
[REGION: page=6, bbox=104,210,336,787]

* **Accountability:**
  * **7 of 15 participants** identified a mismatch between assertive, confident AI outputs and the inherent uncertainty of scholarly inquiry *(Section 4.1.1, page 5)*.
  * **2 of 15 participants** reported platform-level data governance concerns regarding the storage and repurposing of unpublished research prompts *(Section 4.1.2, page 5)*.
  * **9 of 15 participants** explicitly stated that AI cannot bear responsibility for core scholarly judgment, retaining ultimate accountability themselves *(Section 4.1.3, page 5)*.
  * **10 of 15 participants** compensated by restricting AI strictly to organizational and peripheral support tasks (e.g., note-taking, folder organization, broad overviews) *(Section 4.1.4, page 6)*.
* **Transparency:**
  * **9 of 15 participants** raised concerns regarding black-box opacity across data sources, retrieval pipelines, training data, and database coverage *(Section 4.2.1, page 6)*.
  * **7 of 15 participants** framed hallucinations not as technical glitches, but as failures of transparency masking a lack of substance *(Section 4.2.2, page 6)*.
  * **15 of 15 participants (100%)** utilized pre-existing social credibility heuristics (e.g., author familiarity, publication venue, citation counts) as workarounds for retrieval opacity *(Section 4.2.3, page 7)*.
  * **8 of 15 participants** defaulted to redundant manual verification (re-checking citations, publication years, and author names) *(Section 4.2.4, page 7)*.
  * **3 of 15 participants** reported that constrained or highly detailed prompting shifted substantial additional cognitive and time burdens onto researchers *(Section 4.2.5, page 7)*.
* **Trust:**
  * **11 of 15 participants** found trust in AI tools to be fragile, context-dependent, and requiring continuous re-establishment through verification *(Section 4.3.1, page 7)*.
  * **7 of 15 participants** reported that output homogenization (generic, shallow summaries) undermined perceived intellectual depth *(Section 4.3.2, pages 7–8)*.
  * **10 of 15 participants** used strategic hedging by confining AI to low-stakes, surface-level exploratory tasks while independently performing deep analysis and synthesis *(Section 4.3.4, page 8)*.

---

#### 4. Separation of Measured Findings vs. Author Interpretation
* **Empirically Measured Findings:**
  * Researchers consistently verbalized skepticism toward fluent AI answers.
  * Participants engaged in specific compensatory actions during the sessions: multi-step prompt expansion, reading abstracts and original PDFs to confirm citations, looking up author publication records, and switching to traditional citation managers.
* **Author Interpretation:**
  * The authors frame these practices as an "accountability burden" and argue that AI tools act as "epistemic participants" rather than passive cognitive scaffolds *(Section 2.1, page 2)*.
  * The authors argue that AI tools risk creating a "flattening effect" that conflates mere information aggregation with genuine discovery, potentially exacerbating expertise inequities for junior researchers *(Section 4.2.5, 5, pages 7, 8)*.

---

#### 5. Accounting of Time Gains vs. Verification Burden
* **Do time gains include verification?** **No.**
* The authors and participants explicitly note that while AI tools expedite the initial generation of summaries and broad paper identification, **they shift additional time and cognitive burdens onto researchers for verification**:
  * *"By highlighting the compensatory strategies researchers naturally develop, we show that AI-mediated research often adds cognitive burden instead of reducing it."* *(Section 1, page 2)*
  * Mitigations such as social credibility heuristics *"sometimes cost a significant expenditure of time. This complicates the intended efficiency of AI tools."* *(Section 4.2.3, page 7)*
  * Due to phenomena such as *attribution displacement* and *synthetic blending* (where fabricated facts are intertwined with valid citations), verifying outputs requires *"exhaustive manual effort"* and *"redundant, manual verification... re-checking the same information multiple times."* *(Section 4.2.2, 4.2.4, pages 6–7)*
  * Crafting detailed, constrained prompts likewise *"shifts additional effort and time burdens onto researchers."* *(Section 4.2.5, page 7)*
* Consequently, reported speed gains apply only to the preliminary retrieval or drafting step, and are frequently offset or complicated by the subsequent verification demanded by scholarly standards.

---

#### 6. Study Limitations (as stated by authors)
* **Sample Scope:** The participant pool draws primarily from academic researchers (mostly PhD candidates), excluding industry R&D contexts where epistemic norms and accountability structures may differ *(Section 6, page 10)*.
* **Tool Volatility:** The tools tested (Research Rabbit and Elicit) represent a point-in-time snapshot of rapidly evolving commercial platforms that have since been updated *(Section 6, page 10)*.
* **Methodological Constraints:** Think-aloud protocols provide only a partial window into cognition; verbalization is effortful, incomplete, and the act of articulating reasoning can alter the judgment process itself *(Section 6, page 10)*.
* **Task Structuring:** Interactions were guided by experimental task structures and supplied seed papers, which may not fully represent self-directed, open-ended, and naturalistic AI usage *(Section 6, page 10)*.
* **Task & Prompt Sensitivity:** Participant judgments were conditioned on specific prompts and varying degrees of baseline tool familiarity *(Section 6, page 10)*.

---

[Lun26]:
Here is the structured evidence record based on the provided paper:

---

### **Evidence Record: [Lun26]**

#### **1. Bibliographic Information**
* **Exact Title:** Measuring University Students’ Satisfaction with Traditional Search Engines and Generative AI Tools as Information Sources *(Page 1)*
* **Complete Author Names as Printed:**
  * Brady D. Lund, Ph.D. *(Page 1)*
  * Scott J. Warren, Ph.D. *(Page 1)*
  * Zoe A. Teel, Ph.D. Student *(Page 1)*
* **Venue / Publication / Preprint Status:** Not stated in the document (manuscript/preprint format without publication venue, volume, or issue numbers).
* **DOI:** Not reported / None provided.

---

#### **2. Study Design & Methodology**
* **Study Design:** Cross-sectional electronic survey using Qualtrics, administered via convenience sampling in late fall 2025 (specified as August–September 2025 in the *Methods* section, Page 6).
* **Sample:**
  * $N = 236$ valid survey responses from students enrolled at U.S.-based universities *(Page 6, 7)*.
  * **Disciplinary background:** Three-fourths (75%) from natural and computing sciences *(Page 7)*.
  * **Academic standing:** Three-fourths (75%) graduate-level students *(Page 7)*.
  * **Gender:** 48% female, 43% male, 9% other *(Page 7)*.
  * **Student status:** 43% domestic, 57% international *(Page 7)*.
  * **Age distribution:** 63% under age 25, 26% aged 26–30, and 11% aged 31 or older *(Page 7)*.
* **Tools / Versions Evaluated:**
  * Generative AI tools / large language models (specifically referred to in survey items as "AI chatbot/ChatGPT" and "AI tool"; specific model version/build is not specified) *(Pages 3, 6, 19–20)*.
  * Analysis software: Qualtrics (data collection) and SPSS (statistical analysis) *(Page 6)*.
* **Comparator:** Traditional search engines (e.g., Google) *(Pages 3, 6, 19)*.

---

#### **3. Measured Numerical Results**

##### **A. Construct Identification (Principal Components Analysis)**
Satisfaction was evaluated on a 5-point Likert scale (0 to 4: 0 = "I am never satisfied with this tool", 1 = "I am rarely satisfied with this tool", 2 = "I am sometimes satisfied with this tool", 3 = "I am often satisfied with this tool", 4 = "I am always satisfied with this tool") across five information types *(Pages 7–8)*:

Table 1 displays the factor loadings from the Principal Components Analysis for traditional search engine satisfaction across five information tasks, extracting a single component with an eigenvalue of 2.84 explaining 52.66% of the variance:
[REGION: page=7, bbox=696,115,831,632]

* **Table 1: Factor Loadings for Search Engine Satisfaction** *(Page 7)*:
  * Job-Related Information: .768
  * Coursework-Related Information: .720
  * Information for Studying Topics: .768
  * Weather-Related Information: .622
  * News Information: .741
  * Single component eigenvalue = 2.84, explaining 52.66% of total variance.

Table 2 displays the factor loadings from the Principal Components Analysis for generative AI satisfaction across the same five information tasks, extracting a single component with an eigenvalue of 3.41 explaining 68.27% of the variance:
[REGION: page=8, bbox=140,115,274,632]

* **Table 2: Factor Loadings for Artificial Intelligence Satisfaction** *(Page 8)*:
  * Job-Related Information: .855
  * Coursework-Related Information: .805
  * Information for Studying Topics: .839
  * Weather-Related Information: .798
  * News Information: .832
  * Single component eigenvalue = 3.41, explaining 68.27% of total variance.

---

##### **B. Usability & Satisfaction Ratings**
Table 3 compares the summary descriptive statistics (mean, SD, median, bounds, skewness, kurtosis) between search engines and generative AI on the 0–4 satisfaction scale, demonstrating higher overall satisfaction for search engines:
[REGION: page=8, bbox=597,115,774,710]

* **Table 3: Descriptive Statistics for Satisfaction with Search Engines and AI as Information Source** *(Page 8)*:
  * **Mean:** Search Engine = 3.12; Artificial Intelligence = 2.11
  * **Standard Deviation:** Search Engine = 0.80; Artificial Intelligence = 1.00
  * **Median:** Search Engine = 3.25; Artificial Intelligence = 2.17
  * **Lower Bound:** Search Engine = .13; Artificial Intelligence = .68
  * **Upper Bound:** Search Engine = 4.00; Artificial Intelligence = 4.00
  * **Skewness:** Search Engine = -1.11; Artificial Intelligence = -0.075
  * **Kurtosis:** Search Engine = 1.13; Artificial Intelligence = -1.16

---

##### **C. Bivariate Correlations**
*(Page 8–9, section "Comparison of Satisfaction with Search Engine and AI as Information Source")*:
* Satisfaction with search engine vs. satisfaction with AI: $r = -.22$ ($p < .01$)
* Monthly search engine use frequency vs. search engine satisfaction: $r = .33$ ($p < .01$)
* Monthly search engine use frequency vs. AI satisfaction: $r = -.10$ ($p = .13$)
* Monthly AI use frequency vs. AI satisfaction: $r = .58$ ($p < .01$)
* Monthly AI use frequency vs. search engine satisfaction: $r = .03$ ($p = .61$)

---

##### **D. Cluster Analysis (K-Means)**
*(Page 9, section "Categorization of Students Based on Information Source Satisfaction")*:
* **Cluster 1 (41% of cases):** AI satisfaction mean = 1.08; SE satisfaction mean = 3.48
  * Demographics: 60.4% domestic, 17.6% international; 64.7% graduate, 23.2% undergraduate; 64.4% women, 51.8% men.
* **Cluster 2 (59% of cases):** AI satisfaction mean = 2.82; SE satisfaction mean = 2.88
  * Demographics: 39.6% domestic, 82.4% international; 35.3% graduate, 76.8% undergraduate; 35.6% women, 48.2% men.

---

##### **E. Multiple Linear Regression Models**
This table presents the multiple regression model predicting student satisfaction with traditional search engines ($R^2 = .141$), where monthly use frequency is the only statistically significant predictor:
[REGION: page=10, bbox=91,118,235,880]

* **Table 4 (Search Engines): Regression Statistics for Satisfaction with Search Engines as an Info Source** *(Page 10; Model: $R^2 = .141$, $F = 6.11$, $p < .01$)*:
  * Constant: Unstandardized Beta = 2.53, $p < .01$
  * Academic Major (Computing): Unstandardized Beta = .08, Standardized Beta = .05, $p = .59$
  * Academic Standing (Graduate): Unstandardized Beta = .09, Standardized Beta = .04, $p = .58$
  * Age (26+): Unstandardized Beta = -.03, Standardized Beta = -.02, $p = .80$
  * Gender (Male): Unstandardized Beta = -.00, Standardized Beta = -.00, $p = .99$
  * Student Status (International): Unstandardized Beta = -.26, Standardized Beta = -.16, $p = .07$
  * Times Used SE Past Month: Unstandardized Beta = .03, Standardized Beta = .34, $p < .01$

This second regression table (printed as Table 4 on page 10, referred to as Table 5 on page 9) presents the regression model predicting generative AI satisfaction ($R^2 = .453$), showing significant effects for graduate standing, international status, and monthly AI usage frequency:
[REGION: page=10, bbox=461,118,617,880]

* **Table 4 / Table 5 (Generative AI): Regression Statistics for Satisfaction with Generative AI as an Info Source** *(Page 10; Model: $R^2 = .453$, $F = 30.63$, $p < .01$)*:
  * Constant: Unstandardized Beta = 1.66, $p < .01$
  * Academic Major (Computing): Unstandardized Beta = -.11, Standardized Beta = -.05, $p = .42$
  * Academic Standing (Graduate): Unstandardized Beta = -.53, Standardized Beta = -.17, $p < .01$
  * Age (26+): Unstandardized Beta = .16, Standardized Beta = .08, $p = .18$
  * Gender (Male): Unstandardized Beta = -.04, Standardized Beta = -.02, $p = .67$
  * Student Status (International): Unstandardized Beta = .82, Standardized Beta = .40, $p < .01$
  * Times Used AI Past Month: Unstandardized Beta = .04, Standardized Beta = .39, $p < .01$

---

#### **4. Time Gains & Verification**
* **Time Gains Measured:** **No.** The study does **not** evaluate, track, or report empirical task completion times, retrieval speed, extraction efficiency, or time savings.
* **Inclusion of Verification in Time Gains:** Not applicable, as no objective time measures were conducted. The authors note qualitatively from the literature that AI can "reduce cognitive load and save valuable time" *(Page 11)* while requiring "careful verification and source checking" *(Page 3)*, but **no empirical measurement of time gains (with or without verification) exists in this study**.

---

#### **5. Separation of Measured Findings vs. Author Interpretations**
* **Measured Findings:**
  * Mean search engine satisfaction ($3.12/4.00$) was significantly higher than generative AI satisfaction ($2.11/4.00$).
  * Graduate standing negatively predicts AI satisfaction ($\beta = -.53, p < .01$).
  * International status positively predicts AI satisfaction ($\beta = .82, p < .01$).
  * Monthly AI frequency positively predicts AI satisfaction ($\beta = .04, p < .01$).
  * Age, gender, and computing major were not significant predictors of satisfaction for either tool.
* **Author Interpretation:**
  * The authors hypothesize that international students prefer AI because it provides conversational language scaffolding, translation, and adaptation to U.S. academic discourse without dense phrasing *(Pages 4, 11)*.
  * The authors interpret graduate students' lower satisfaction as resulting from their greater training in academic databases, source verification, methodological rigor, and requirement for citable original sources *(Pages 11–12)*.
  * The absence of a cluster satisfied with AI but dissatisfied with search engines suggests that students view GenAI as a "complementary component" rather than a complete replacement for search engines *(Pages 9, 12, 13)*.

---

#### **6. Study Limitations (Reported by Authors)**
*(Pages 12–13, section "Limitations and Future Research")*:
1. **Sampling Bias:** Non-random convenience sample from U.S. universities, heavily skewed toward graduate students (75%) and natural/computing science majors (75%), which may limit generalizability to humanities, education, or social sciences.
2. **Self-Report Bias:** Relies purely on self-reported estimates of frequency of use and subjective satisfaction, subject to recall bias and social desirability.
3. **Lack of Behavioral/Log Data:** Did not include direct system logs, real-time tracking, or experimental task execution.
4. **Broad Information Categories:** Examined satisfaction broadly across general task domains rather than evaluating specific real-time queries, disciplinary workflows, or criteria like trust, credibility, and accuracy directly.

---

[Kim26e]:
Here is the evidence wiki record based strictly on the provided text of the paper.

---

### 1. Bibliographic Information

* **Exact Title:** Understanding Generative AI-mediated User Engagement with Academic Library Resources *(Page 1)*
* **Complete Author Names (as printed):** Hae Min Kim, Stacy Stanislaw *(Page 1)*
* **Venue:** Not stated in the document header, footer, or body *(Pages 1–22)*.
* **Publication / Preprint Status:** Not explicitly indicated in the text (the manuscript appears as an unpublished paper/manuscript with running head "AI-mediated user engagement") *(Pages 1–22)*.
* **DOI:** Not stated / None provided for this paper *(Pages 1–22)*.

---

### 2. Study Design & Methodology

* **Study Design:** Exploratory case study analyzing web analytics data (*Section: "Methodology"*, Page 6).
* **Sample / Dataset:**
  * Analytics tracking period: August 1, 2023, through October 31, 2025 (*Section: "Methodology"*, Page 7).
  * Setting: Drexel University Libraries, serving 20,868 undergraduate and graduate students, and 5,970 faculty and staff (*Section: "Scope of Analyzed Library Managed Platforms"*, Page 7).
  * Content analyzed: Over 1.5 million online resources, including 14,416 electronic theses and dissertations (ETDs) and 104,631 research and scholarly works (*Section: "Scope of Analyzed Library Managed Platforms"*, Page 7).
  * Referral landing pages: 3,451 unique landing pages receiving a total of 9,753 sessions generated through AI referrals (*Section: "Content-level patterns of AI-mediated access"*, Page 14).
* **Tools / Versions:**
  * **Analytics & Processing:** Google Analytics 4 (GA4), Microsoft Excel, Microsoft Power BI (*Pages 7, 8, 9*).
  * **Evaluated AI Referral Platforms (20 identified):** ChatGPT (`chatgpt.com`), Perplexity (`perplexity.ai`), Google Gemini (`gemini.google.com`), Microsoft Copilot (`copilot.microsoft.com`), Blackbox AI (`blackbox.ai`), Claude (`claude.ai`), Consensus (`consensus.app`), NotebookLM (`notebooklm.google.com`), DeepSeek (`chat.deepseek.com`), Dimensions (`pcw.dimensions.ai`), iAsk (`iask.ai`), Txyz (`app.txyz.ai`), Conch (`app.getconch.ai`), Felo (`felo.ai`), Exa (`exa.ai`), Grok (`grok.com`), Undermind (`app.undermind.ai`), QuillBot (`quillbot.com`), Abacus (`apps.abacus.ai`), Mistral (`chat.mistral.ai`) (*Table 1, Pages 9–10*).
  * **AI Models/Features noted in text:** GPT-5 (released August 2025), ChatGPT "Sources" feature (launched late October 2024) (*Pages 10, 11*).
* **Comparator:** Traditional referral and search sources accessing the Drexel Research Repository (*Section: "Distribution Across Library Systems"*, Pages 12–13; *Table 2*, Page 14):
  * Search Engines: Google (`google.com`), Google Scholar (`scholar.google.com`), Bing (`bing.com`).
  * Institutional Platforms: Drexel Discovery Service (`drexel.primo.exlibrisgroup.com`), Drexel Learn / Blackboard Learn (`learn.dcollege.net`).

---

### 3. Exact Numerical Findings

*(Note: The study evaluates web analytics traffic and engagement metrics rather than classical benchmark screening/extraction precision/recall).*

#### A. AI Platform Referral Breakdown Across Library Systems
*Source: Table 1 ("Distribution of AI-Mediated Users Across Library Systems (Total Users)", Pages 9–10)*

This table details the distribution of total users referred by 20 generative AI platforms across seven different library platforms, showing the dominant share going to the institutional research repository.
[REGION: page=9, bbox=542,116,913,934]

* **Total AI-mediated users by system across the entire observation period:**
  * **Research Repository (Esploro):** 2,997 users (out of 159,940 total repository visitors) (*Page 12*)
  * **Library Guides (Springshare):** 688 users (out of 94,937 total visitors) (*Page 12*)
  * **Core Library Website (Sitecore):** 290 users (out of 138,356 total visitors) (*Page 12*)
  * **Discovery Service (ExLibris Primo):** 79 users *(sum across Table 1: ChatGPT 43, Perplexity 14, Gemini 4, Copilot 13, Claude 4, Grok 1)*
  * **Virtual Reference (Springshare):** 29 users *(Page 12)*
  * **Scheduling (Springshare):** 17 users *(Page 12)*
  * **Digital Exhibit (Omeka):** 7 users *(Page 12; Table 1 reports: ChatGPT 8, Copilot 1)*
* **Top AI Platforms by User Count (*Table 1*, Page 9):**
  * `chatgpt.com`: Core library: 292; Discovery service: 43; Research Repository: 2,836; Library Guides: 514; Virtual Reference: 18; Scheduling: 25; Digital Exhibit: 8.
  * `perplexity.ai`: Core library: 46; Discovery service: 14; Research Repository: 367; Library Guides: 147; Virtual Reference: 6; Scheduling: 1; Digital Exhibit: 0.
  * `gemini.google.com`: Core library: 27; Discovery service: 4; Research Repository: 234; Library Guides: 106; Virtual Reference: 7; Scheduling: 2; Digital Exhibit: 0.
  * `copilot.microsoft.com`: Core library: 11; Discovery service: 13; Research Repository: 25; Library Guides: 1; Virtual Reference: 0; Scheduling: 0; Digital Exhibit: 1.
  * `blackbox.ai`: Research Repository: 33; Library Guides: 6.
  * `claude.ai`: Core library: 1; Discovery service: 4; Research Repository: 3; Library Guides: 6.

#### B. Referral Share & Growth Over Time
* **Earliest AI referral:** August 25, 2023, from Perplexity (*Section: "Emergence and Growth of AI-Mediated Access"*, Page 10).
* **Traffic Spikes and Shifts:**
  * By October 2024, AI-mediated users grew by 43% compared to the previous month (*Page 11*).
  * In September 2025 (following GPT-5 launch in August 2025), ChatGPT-mediated traffic rose by 78% relative to August (*Page 11*).
  * In October 2025, ChatGPT traffic grew by 47% relative to September (*Page 11*).
  * October 2025 AI referral share to the library website: ChatGPT 85%, Perplexity 8%, Gemini 6%, Copilot 1% (*Section: "Distribution Across Library Systems"*, Page 12).
  * Monthly proportion of AI-mediated access relative to total traffic peaked at 2.92% (September 2025) and 2.95% (October 2025) (*Figure 2*, Page 11).

#### C. Usability and User Engagement Metrics (Research Repository)
*Source: Table 2 ("Engagement Metrics across Referral Sources to Research Repository", Page 14)*

This table compares engagement metrics (total users, user engagement in seconds, average engagement time per session, bounce rate, and views per active user) between generative AI, traditional search engines, and internal institutional systems.
[REGION: page=14, bbox=91,116,303,884]

Exact figures from Table 2:
* **Search Engine — `google.com`:**
  * Total users: 124,371
  * User engagement: 5,529,143 seconds
  * Avg. engagement time per session: 33.57 seconds
  * Bounce rate: 0.26 (26%)
  * Views per active user: 2.57
* **Search Engine — `scholar.google.com`:**
  * Total users: 17,582
  * User engagement: 488,420 seconds
  * Avg. engagement time per session: 23.98 seconds
  * Bounce rate: 0.46 (46%)
  * Views per active user: 1.40
* **Search Engine — `bing.com`:**
  * Total users: 2,942
  * User engagement: 181,124 seconds
  * Avg. engagement time per session: 41.25 seconds
  * Bounce rate: 0.16 (16%)
  * Views per active user: 3.44
* **Generative AI — `chatgpt.com`:**
  * Total users: 2,396
  * User engagement: 71,975 seconds
  * Avg. engagement time per session: 21.82 seconds
  * Bounce rate: 0.42 (42%)
  * Views per active user: 1.86
* **Institutional Platform — `drexel.primo.exlibrisgroup.com` (Discovery Service):**
  * Total users: 821
  * User engagement: 107,913 seconds
  * Avg. engagement time per session: 71.70 seconds
  * Bounce rate: 0.39 (39%)
  * Views per active user: 7.13
* **Institutional Platform — `learn.dcollege.net` (Drexel Learn / LMS):**
  * Total users: 574
  * User engagement: 139,917 seconds
  * Avg. engagement time per session: 127.20 seconds
  * Bounce rate: 0.24 (24%)
  * Views per active user: 9.47

#### D. Content-Level Breakdown of AI Referrals
*Source: Section: "Content-level patterns of AI-mediated access", Pages 14–15; Table 3, Page 14*

* **Referral sessions by library system (Total: 9,753 sessions):**
  * Research Repository: 75% (7,303 sessions)
  * Library Guides: 12% (1,217 sessions)
  * Core library website: 7%
  * Discovery Service: 4%
* **Research Repository Document Types accessed via AI referrals (Total: 7,303 sessions) (*Table 3*, Pages 14–15):**
  * Dissertation & thesis: 4,098 sessions (56.1%)
  * Journal article: 1,430 sessions (19.6%)
  * Search outputs: 643 sessions (8.8%)
  * Book chapter: 319 sessions (4.4%)
  * Profile: 207 sessions (2.8%)
  * Conference: 186 sessions (2.5%)
  * unknown: 180 sessions (2.5%)
  * Book: 90 sessions (1.2%)
  * Outputs: 68 sessions (0.9%)
  * Report: 35 sessions (0.5%)
  * Researchers: 35 sessions (0.5%)
  * Abstract: 12 sessions (0.2%)

---

### 4. Separation of Measured Performance vs. Author Interpretation

* **Measured Performance (Empirical Facts from Data):**
  * AI-mediated traffic represents a small minority of total web traffic (~2.95% peak monthly share in October 2025) (*Page 11*).
  * Traffic was heavily concentrated in the institutional Research Repository (75% of sessions) and primarily on electronic theses and dissertations (56.1% of repository sessions) (*Pages 14–15*).
  * ChatGPT users exhibited lower average engagement time (21.82 s) and higher bounce rate (42%) than institutional discovery/LMS platforms (71.70 s – 127.20 s; 24% – 39% bounce rates) (*Table 2, Page 14*).
* **Author Interpretations & Hypotheses:**
  * The authors interpret these metrics as showing that AI-mediated traffic is "transactional," "item-focused," and functions as a "point-of-need reference pathway" or "source verification" rather than an exploratory research pathway (*Pages 13, 16, 18*).
  * The authors hypothesize that ETDs and repository records dominate because their technical structure (schema.org tags, controlled vocabularies, static permalinks, open-access status, and hosted PDFs) aligns with RAG retrieval architectures and search crawler preferences (*Pages 15–16*).
  * The authors note the correlation between platform features (such as OpenAI's "Sources" link launch in October 2024 and GPT-5 in August 2025) and traffic increases, but explicitly state that correlation does not establish causation (*Pages 11, 18*).

---

### 5. Time Gains and Verification

* **Did the study measure time gains or screening efficiency?** No. The study did **not** conduct or measure screening, extraction, or task-completion time gains.
* **Explanation regarding verification:** The only time-related metric recorded is **GA4 average engagement time per session** (e.g., 21.82 seconds for ChatGPT referrals vs. 33.57 seconds for Google and 127.20 seconds for Drexel Learn; *Table 2, Page 14*). The authors speculate that the short dwell time reflects users engaging in quick verification or fact-checking of AI-generated answers, but they explicitly state:
  > *"While this study provides a quantitative foundation by analyzing two and half years of access data, it does not capture the nuances of users’ experiences behind these visits. Qualitative methods including user interviews or usability tests should be employed to investigate how AI-mediated access specifically benefits researchers..."* (*Section: "Limitations" / "Conclusion"*, Page 19).

---

### 6. Limitations

As explicitly reported by the authors (*Section: "Limitations"*, Pages 17–18):
1. **Conservative estimate / Tracking inconsistency:** Referral tracking from generative AI tools is not captured uniformly across all access modes (e.g., desktop/mobile apps may not pass HTTP referrers like browser sessions), leading to potential undercounting.
2. **Identification criteria:** The study limited AI sources to LLM-based generative platforms and excluded AI-augmented discovery tools or databases without generative features.
3. **Bot traffic / GA4 noise:** Despite prioritizing "total users" over session counts to mitigate bot crawling distortion, residual non-human traffic noise may remain.
4. **Single-institution case study:** Findings reflect Drexel University Libraries' specific digital repository architecture, SEO setup, and metadata environment, which may not generalize to other institutions.
5. **Causality vs. Correlation:** Traffic spikes correlating with AI tool releases (GPT-5, OpenAI "Sources") cannot definitively be separated from seasonal academic cycles or internal institutional initiatives.

---

[Kha25]:
Here is the structured evidence record based on the provided text of the study:

---

### 1. Bibliographic Information
* **Exact Title:** Collaborative large language models for automated data extraction in living systematic reviews
* **Complete Author Names (as printed):** Muhammad Ali Khan, Umair Ayub, Syed Arsalan Ahmed Naqvi, Kaneez Zahra Rubab Khakwani, Zaryab bin Riaz Sipra, Ammad Raina, Sihan Zhou, Huan He, Amir Saeidi, Bashar Hasan, Robert Bryan Rumble, Danielle S. Bitterman, Jeremy L. Warner, Jia Zou, Amye J. Tevaarwerk, Konstantinos Leventakos, Kenneth L. Kehl, Jeanne M. Palmer, Mohammad Hassan Murad, Chitta Baral, Irbaz bin Riaz
* **Venue:** *Journal of the American Medical Informatics Association* (JAMIA), 2025, Vol. 32, No. 4, pp. 638–647
* **Publication / Preprint Status:** Peer-reviewed journal article (Advance access publication: 21 January 2025; Received: September 21, 2024; Revised: November 25, 2024; Editorial Decision: December 21, 2024)
* **DOI:** `https://doi.org/10.1093/jamia/ocae325`

---

### 2. Study Design, Sample, Tools, and Comparators
* **Study Design:** Simulation/evaluation study assessing an automated collaborative two-reviewer LLM workflow for data extraction from clinical trial publications using a zero-shot prompt design with cross-critique for discordant responses.
* **Sample:**
  * 10 clinical trials comprising 22 original and follow-up publications from a published living systematic review (LSR) and network meta-analysis on first-line treatments for metastatic castration-sensitive prostate cancer (p. 2, "Methods: Data sources").
  * 23 target variables categorized into "trial characteristics," "population characteristics," and "meta-analysis outcomes" (p. 2, "Methods: Data sources").
  * Total tokens/images processed: 277,810 text tokens (median: 11,434.5; IQR: 9,588.3–15,462.3) and 169 images (median: 7.5; IQR: 6.3–9) across all 22 publications (p. 3, "Results").
  * **Prompt Development Set:** 5 publications (23%), 115 total responses (23 variables × 5 publications), 65,024 text tokens (median: 10,426; IQR: 10,285–15,880), and 42 images (median: 9; IQR: 7–9) (pp. 3–4, "Results").
  * **Held-Out Test Set:** 17 publications (77%), 391 total responses (23 variables × 17 publications), 212,786 text tokens (median: 11,907; IQR: 9,508–14,209), and 127 images (median: 7; IQR: 6–8) (pp. 3–4, "Results").
* **Tools and Versions:**
  * OpenAI GPT-4-Turbo: `gpt-4-0125-preview` for text, `gpt-4-vision-preview` for images (temperature = 0) (pp. 2–3, "Methods: Sampling and prompting").
  * Anthropic Claude-3-Opus: `claude-3-opus-20240229` (temperature = 0) (pp. 2–3, "Methods: Sampling and prompting").
  * Supporting libraries: `PyMuPDF 1.24.9` (PDF text extraction), `tiktoken 0.7.0` (token management) (p. 2, "Methods: Data processing"; p. 10, "References").
* **Comparator:** A manually curated gold-standard dataset derived from the full-text PDFs (benchmarking ground truth). Comparisons were made between:
  1. Single LLM extraction (GPT-4T alone vs. Claude-3O alone).
  2. Collaborative LLM concordant responses vs. single LLM performance.
  3. Pre-cross-critique discordant responses vs. post-cross-critique concordant responses.

---

### 3. Exact Measured Numerical Results (Extraction Performance)

#### A. Prompt Development Set (115 Responses Total)
*(Source: p. 4, "Results: Response evaluation in the single LLM approach" and "Response evaluation in the collaborative LLM approach")*
* **Single LLM Performance:**
  * **GPT-4T:** Accuracy = 0.95 (95% CI: 0.93–0.97), Precision = 1.00, Recall = 0.92 (95% CI: 0.88–0.96), F1 score = 0.96 (95% CI: 0.95–0.97). Hallucinations = 0 (0%).
  * **Claude-3O:** Accuracy = 0.95 (95% CI: 0.93–0.97), Precision = 0.96 (95% CI: 0.94–0.98), Recall = 0.97 (95% CI: 0.95–0.99), F1 score = 0.96 (95% CI: 0.94–0.98). Hallucinations = 2.6% (all related to meta-analysis outcomes).
* **Collaborative Workflow (Initial):**
  * Concordant responses: 110 of 115 (96%).
  * Accuracy of concordant responses = 0.99 (95% CI: 0.98–1.00), Precision = 1.00, Recall = 0.96 (95% CI: 0.94–0.97), F1 score = 0.98 (95% CI: 0.97–0.99). Hallucinations = 0 (0%).
  * Discordant responses: 5 of 115 (4%).
  * Discordant accuracy: GPT-4T = 0.25 (95% CI: 0.00–0.69); Claude-3O = 0.50 (95% CI: 0.06–0.93).
* **Cross-Critique of Discordant Responses:**
  * 3 of 5 (60%) became concordant after cross-critique; mean Accuracy, Precision, Recall, and F1 score = 1.00; Hallucinations = 0 (0%).
  * 2 of 5 (40%) remained discordant; Accuracy = 0.00, Precision = 0.00, Recall = 0.00. Hallucinations = 50% for GPT-4T, 100% for Claude-3O (p. 5).

---

#### B. Held-Out Test Set (391 Responses Total)
*(Source: p. 4, "Results: Response evaluation in the single LLM approach" and "Response evaluation in the collaborative LLM approach"; p. 5, "Discordant responses" and "Response evaluation after cross-critique")*

* **Single LLM Approach:**
  * **GPT-4T:** Accuracy = 0.89 (95% CI: 0.87–0.91), Precision = 0.98 (95% CI: 0.96–1.00), Recall = 0.87 (95% CI: 0.85–0.89), F1 score = 0.92 (95% CI: 0.90–0.94). Hallucinations = 2.3%.
  * **Claude-3O:** Accuracy = 0.90 (95% CI: 0.89–0.91), Precision = 0.94 (95% CI: 0.92–0.96), Recall = 0.91 (95% CI: 0.89–0.93), F1 score = 0.92 (95% CI: 0.90–0.94). Hallucinations = 2.8%.

* **Collaborative LLM Concordant Responses:**
  * Concordant: 342 of 391 responses (87%).
  * Accuracy = 0.94 (95% CI: 0.93–0.95), Precision = 1.00, Recall = 0.92 (95% CI: 0.90–0.94), F1 score = 0.96 (95% CI: 0.956–0.964).
  * Statistically significantly outperformed GPT-4T alone in accuracy (*P* = 0.003), precision (*P* = 0.035), recall (*P* = 0.003), and F1 (*P* = 0.003).
  * Statistically significantly outperformed Claude-3O alone in accuracy (*P* = 0.007), precision (*P* = 0.022), and F1 (*P* = 0.004).
  * Hallucinations in concordant set = 0.2% (majority in meta-analysis outcomes).

* **Collaborative LLM Discordant Responses (Initial):**
  * Discordant: 49 of 391 responses (13%).
  * GPT-4T performance on discordant set: Accuracy = 0.41 (95% CI: 0.30–0.52), Precision = 0.54 (95% CI: 0.40–0.68), Recall = 0.46 (95% CI: 0.32–0.60), F1 score = 0.50 (95% CI: 0.36–0.64). Hallucinations = 27% (majority in population characteristics).
  * Claude-3O performance on discordant set: Accuracy = 0.50 (95% CI: 0.36–0.64), Precision = 0.60 (95% CI: 0.46–0.74), Recall = 0.72 (95% CI: 0.61–0.83), F1 score = 0.65 (95% CI: 0.54–0.76). Hallucinations = 41% (majority in meta-analysis outcomes).

* **Cross-Critique of Discordant Responses (49 Total):**
  * **Concordant after cross-critique:** 25 of 49 (51%).
    * Accuracy = 0.76 (95% CI: 0.60–0.92), Precision = 0.72 (95% CI: 0.52–0.92), Recall = 0.65 (95% CI: 0.49–0.81), F1 score = 0.68 (95% CI: 0.52–0.84). Hallucinations = 8.3%.
    * Overall test set concordance increased from 87% (342/391) to 94% (367/391) following cross-critique (p. 6, Figure 3).
  * **Remaining discordant after cross-critique:** 24 of 49 (49%).
    * GPT-4T: Accuracy = 0.18 (95% CI: 0.06–0.30), Precision = 0.29 (95% CI: 0.13–0.45), Recall = 0.48 (95% CI: 0.32–0.64), F1 score = 0.36 (95% CI: 0.20–0.52). Hallucinations = 56%.
    * Claude-3O: Accuracy = 0.45 (95% CI: 0.29–0.61), Precision = 0.46 (95% CI: 0.30–0.62), Recall = 0.75 (95% CI: 0.59–0.91), F1 score = 0.57 (95% CI: 0.41–0.73). Hallucinations = 48%.

* **Test Set Sensitivity Analysis (Excluding trials shared with development set):**
  * Concordant responses: Accuracy = 0.97 (95% CI: 0.96–0.98), Precision = 1.00, Recall = 0.97 (95% CI: 0.96–0.98), F1 = 0.98 (95% CI: 0.975–0.984), Hallucinations = 0% (p. 5).
  * Concordant after cross-critique: Accuracy = 0.85 (95% CI: 0.75–0.95), Precision = 0.78 (95% CI: 0.59–0.97), Recall = 0.63 (95% CI: 0.45–0.81), F1 = 0.70 (95% CI: 0.52–0.88), Hallucinations = 0% (p. 5).

* **Error / Hallucination Analysis Breakdown:**
  * Pre-cross-critique:
    * GPT-4T: 62% of hallucinations were due to misinterpretation at the variable level (p. 6, "Error analysis").
    * Claude-3O: 56% of hallucinations were due to misinterpretation at the context level (extraction from incorrect section of document) (p. 6).
  * Post-cross-critique:
    * GPT-4T: 40% of hallucinations were due to the generation of fabricated responses (p. 6).
    * Claude-3O: 64% of hallucinations were due to misinterpretation at the context level (p. 6).

---

### 4. Graphic Pointers

Bar charts comparing data extraction accuracy between individual LLMs and the collaborative 2-reviewer LLM approach on the test set:
[REGION: page=4, bbox=172,519,819,910]

Bar charts illustrating the increase in test set concordance (from 87% to 94%) and the improvement in accuracy of discordant responses following cross-critique:
[REGION: page=6, bbox=64,80,466,850]

Flow diagram depicting the proposed collaborative LLM living evidence extraction architecture, including routing concordant responses to the database and channeling persistent discordant responses to human or third-LLM review:
[REGION: page=7, bbox=62,80,724,890]

---

### 5. Measured Performance vs. Author Interpretations

* **Measured Performance (Direct Empirical Findings):**
  * Concordant pairs of outputs had high fidelity to gold-standard human extractions (0.94 accuracy on the test set; 0.2% hallucinations).
  * Discordant extractions were poorly accurate on their own (0.41 for GPT-4T; 0.50 for Claude-3O).
  * Cross-critique resolved 51% (25/49) of discordant test-set items into concordant pairs, achieving 0.76 accuracy.
  * When items remained discordant after cross-critique, accuracy dropped sharply (0.18 for GPT-4T and 0.45 for Claude-3O), with high hallucination rates (48%–56%).

* **Author Interpretations & Claims:**
  * Authors state that simulating a 2-reviewer workflow "can extract data with reasonable performance, enabling truly 'living' systematic reviews" (p. 1, "Abstract"; p. 8, "Conclusions").
  * Authors state that concordant responses "can be relied upon" as accurate, while remaining discordant responses require an additional human-in-the-loop or third-LLM arbitrator (p. 6, "Discussion"; p. 7, Figure 4).
  * Authors argue that using two different LLM families provides complementary perspectives analogous to human reviewers due to distinct parametric knowledge (p. 8, "Discussion").

---

### 6. Limitations Noted by Authors
*(Source: pp. 7–8, "Discussion")*
1. **Domain / Scope Specificity:** Evaluated exclusively on clinical trials in oncology (specifically metastatic castration-sensitive prostate cancer); findings may not generalize outside oncology.
2. **Data Contamination / Pretraining Exposure:** LLMs may have been exposed to the published trial papers during their pretraining phase, potentially inflating extraction accuracy.
3. **Implicit Judgment Tasks:** Performance was lower for complex variables requiring implicit clinical judgment compared to explicit trial characteristics.
4. **Model Count:** Only two LLMs were tested. While adding more LLMs might boost performance, it would substantially increase computational cost.

---

### 7. Time and Cost Gains: Does It Include Verification?
* **Reported Cost and Speed Metrics:**
  * Average API cost was **$3.40 per publication** for data extraction, plus an additional **$2.06 per publication** for cross-critique (p. 7, "Discussion").
  * Execution speed is characterized as occurring in **"almost real-time"** (p. 7, "Discussion").
* **Does It Include Verification?**
  * **No, it does not include human verification time.**
  * The reported time and cost savings represent purely the automated computational API extraction and LLM cross-critique passes.
  * The authors explicitly indicate that in practical implementation, remaining discordant responses (and potentially all downstream data) require human-in-the-loop review (*"discordant responses require an additional human or an LLM-in-the-loop approach before being utilized for downstream analyses"*, p. 7, Figure 4; p. 8, "Discussion"), but the time required for humans to review or verify these extractions was not timed, quantified, or factored into the cost figures.

---

### Referenced Citations
* **[Kha25]**: Khan MA, Ayub U, Naqvi SAA, et al. Collaborative large language models for automated data extraction in living systematic reviews. *J Am Med Inform Assoc*. 2025;32(4):638–647. doi:10.1093/jamia/ocae325

---

[Lai25]:
Here is the structured evidence record based on the provided full-text article:

---

### Bibliographic Details
* **Exact Title:** Language models for data extraction and risk of bias assessment in complementary medicine
* **Complete Author Names (as printed):**
  * Main author list: Honghao Lai, Jiayi Liu, Chunyang Bai, Hui Liu, Bei Pan, Xufei Luo, Liangying Hou, Weilong Zhao, Danni Xia, Jinhui Tian, Yaolong Chen, Lu Zhang, Janne Estill, Jie Liu, Xing Liao, Nannan Shi, Xin Sun, Hongcai Shang, Zhaoxiang Bian, Kehu Yang, Luqi Huang, Long Ge, On behalf of ADVANCED Working Group (p. 1)
  * Additional ADVANCED Working Group members listed at the end: Haodong Li, Ye Wang, Huayu Zhang, Di Zhu, Dongrui Peng, Fan Wang, Yueyan Li, Shilin Tang, Hanxiang Liu, Zeming Li, Zhenhua Yang, Xuan Yu, Yishan Qin (p. 8)
* **Venue:** *npj Digital Medicine* (p. 1)
* **Publication / Preprint Status:** Published journal article (Received: 2 July 2024; Accepted: 15 January 2025; Published online: 31 January 2025; citation: *(2025) 8:74*) (p. 1, 6)
* **DOI:** `https://doi.org/10.1038/s41746-025-01457-w` (p. 1)

---

### Study Design & Methods
* **Study Design:** Evaluation and non-inferiority comparative study comparing LLM-only, LLM-assisted, and conventional manual methods for data extraction and risk-of-bias (ROB) assessment (p. 1, 5).
* **Sample:**
  * 107 randomized controlled trials (RCTs) randomly selected via stratified random sampling from 12 Cochrane reviews published between 1979 and 2024 (p. 1, 5).
  * Characteristics: 27.1% in English, 72.9% in Chinese; 44.9% published post-2013; interventions included mind-body practices (41.1%), herbal decoctions (34.6%), and natural products (24.3%) (p. 1–2).
  * PDF recognizability: 94.4% higher recognizability ($\ge 70\%$ of text/data accurately detected by OCR), 5.6% lower recognizability ($< 70\%$) (p. 2).
* **Tools / Versions:**
  * `Moonshot-v1-128k` (Moonshot AI; accessed via API; temperature set to 0) (p. 2, 5).
  * `Claude-3.5-sonnet` (Anthropic; accessed via API; temperature set to 0) (p. 2, 5).
  * `R version 4.3.3` (for data analysis) (p. 6).
  * Optical Character Recognition (OCR) software (p. 5).
* **Comparators:**
  * **Conventional manual methods:** Benchmark estimates derived from published literature:
    * Data extraction: 95.3% accuracy, mean time of 86.9 min per RCT (Buscemi et al. 2006) (p. 5).
    * ROB assessment: 90.0% accuracy, mean time of 10.4 min per RCT (Arno et al. 2022) (p. 5).
  * **Reference standard for accuracy:** A consensus benchmark collaboratively established by two independent methodologists who evaluated the LLM-only outputs, LLM-assisted outputs, and their own manual extraction/assessment (p. 5).
  * **LLM-assisted setup:** Four Chinese-speaking reviewers (1–1.5 years experience, 1 month standardized training) reviewed and modified the outputs of the lower-accuracy LLM (`Moonshot-v1-128k`) (p. 5).

---

### Exact Numerical Results

#### 1. Data Extraction Performance
*(Locations: Page 2, Page 3, Page 4 Table 1)*

This forest plot displays the risk differences and 95% confidence intervals between Moonshot-v1-128k (labeled KimiChat) and Claude-3.5-sonnet across data extraction and risk-of-bias domains, highlighting Claude-3.5-sonnet's statistically significant overall advantage in data extraction.
[REGION: page=2, bbox=63,65,395,945]

This table shows the domain-specific and overall correct extractions, accuracy rates, and rate differences between LLM-only and LLM-assisted data extractions based on Moonshot-v1-128k.
[REGION: page=4, bbox=584,95,938,459]

* **Total extraction items:** 12,814 extractions across 107 RCTs (p. 2).
* **Overall Accuracy (LLM-only):**
  * `Claude-3.5-sonnet`: 96.2% (95% CI: 95.8% to 96.5%; 12,324 / 12,814) (p. 2).
  * `Moonshot-v1-128k`: 95.12% (95% CI: 94.74% to 95.49%; 12,189 / 12,814) (p. 2, 4 Table 1).
  * Difference (Claude vs. Moonshot): Risk Difference (RD) = 1.1% (95% CI: 0.6% to 1.6%; $p < 0.001$) (p. 2).
* **LLM-only Accuracy by Domain (Moonshot-v1-128k) (p. 4 Table 1):**
  * *Methods:* 90.86% (875 / 963; 95% CI: 88.86% to 92.61%)
  * *Participants:* 96.65% (1241 / 1284; 95% CI: 95.52% to 97.57%)
  * *Baseline characteristics:* 95.07% (4652 / 4893; 95% CI: 94.43% to 95.66%)
  * *Outcomes:* 97.64% (3427 / 3510; 95% CI: 97.08% to 98.11%)
  * *Data and analysis:* 91.33% (1781 / 1950; 95% CI: 90.00% to 92.54%)
  * *Others:* 99.53% (213 / 214; 95% CI: 97.42% to 99.99%)
* **LLM-assisted Accuracy (Moonshot-v1-128k assisted by human reviewer) (p. 4 Table 1):**
  * *Overall:* 97.92% (12,547 / 12,814; 95% CI: 97.65% to 98.16%)
  * *Methods:* 98.23% (946 / 963; 95% CI: 97.19% to 98.97%)
  * *Participants:* 98.60% (1266 / 1284; 95% CI: 97.79% to 99.17%)
  * *Baseline characteristics:* 97.02% (4747 / 4893; 95% CI: 96.50% to 97.47%)
  * *Outcomes:* 99.06% (3477 / 3510; 95% CI: 98.68% to 99.35%)
  * *Data and analysis:* 97.28% (1897 / 1950; 95% CI: 96.46% to 97.96%)
  * *Others:* 99.53% (213 / 214; 95% CI: 97.42% to 99.99%)
* **Rate Difference (LLM-assisted vs. LLM-only Data Extraction) (p. 4 Table 1):**
  * Overall: 2.79% (95% CI: 2.35% to 3.24%; text cites RD: 2.8%, 95% CI: 2.4%–3.2%; $p < 0.001$)
  * Methods: +7.37% (95% CI: 5.37% to 9.37%)
  * Data and analysis: +5.95% (95% CI: 4.51% to 7.39%)
  * Participants: +1.95% (95% CI: 0.77% to 3.12%)
  * Baseline characteristics: +1.94% (95% CI: 1.17% to 2.71%)
  * Outcomes: +1.42% (95% CI: 0.83% to 2.02%)
  * Others: 0.00% (95% CI: -1.29% to 1.29%)
* **Comparison to Conventional Data Extraction Benchmark:**
  * LLM-assisted (97.9%) vs. Conventional benchmark (95.3%): RD = 2.6% (95% CI: 2.2% to 3.1%; $p < 0.001$) (p. 2).
* **Inter-model & Inter-rater Agreement for Extraction:**
  * Inter-model agreement rate between Claude-3.5-sonnet and Moonshot-v1-128k: 93.8% (p. 2).
  * 83.3% of Claude's errors were also present in Moonshot's results (p. 2).

---

#### 2. Risk-of-Bias (ROB) Assessment Performance
*(Locations: Page 2, Page 3, Page 4 Table 2)*

This table shows the domain-specific and overall correct evaluations, accuracy rates, and rate differences between LLM-only and LLM-assisted risk-of-bias assessments based on Moonshot-v1-128k.
[REGION: page=4, bbox=533,520,937,890]

* **Total ROB assessments:** 1,070 assessments across 10 domains for 107 RCTs (p. 2).
* **Overall Accuracy (LLM-only):**
  * `Claude-3.5-sonnet`: 96.9% (95% CI: 95.7% to 97.9%; 1037 / 1070) (p. 2).
  * `Moonshot-v1-128k`: 95.70% (95% CI: 94.31% to 96.84%; 1024 / 1070) (p. 2, 4 Table 2).
  * Difference (Claude vs. Moonshot): RD = 1.2% (95% CI: -0.4% to 2.8%; not statistically significant) (p. 2).
* **LLM-only Accuracy by Domain (Moonshot-v1-128k) (p. 4 Table 2):**
  * *Sequence generation:* 87.85% (94 / 107; 95% CI: 80.12% to 93.37%)
  * *Allocation sequence concealment:* 96.26% (103 / 107; 95% CI: 90.70% to 98.97%)
  * *Blinding: patients:* 95.33% (102 / 107; 95% CI: 89.43% to 98.47%)
  * *Blinding: healthcare providers:* 96.26% (103 / 107; 95% CI: 90.70% to 98.97%)
  * *Blinding: data collectors:* 94.39% (101 / 107; 95% CI: 88.19% to 97.91%)
  * *Blinding: outcome assessors:* 96.26% (103 / 107; 95% CI: 90.70% to 98.97%)
  * *Blinding: data analysts:* 96.26% (103 / 107; 95% CI: 90.70% to 98.97%)
  * *Missing outcome data:* 100.00% (107 / 107; 95% CI: 96.61% to 100.00%)
  * *Selective outcome reporting:* 99.07% (106 / 107; 95% CI: 94.90% to 99.98%)
  * *Other bias:* 95.33% (102 / 107; 95% CI: 89.43% to 98.47%)
* **LLM-assisted Accuracy (Moonshot-v1-128k assisted by human reviewer) (p. 4 Table 2):**
  * *Overall:* 97.29% (1041 / 1070; 95% CI: 96.13% to 98.18%)
  * *Sequence generation:* 96.26% (103 / 107; 95% CI: 90.70% to 98.97%)
  * *Allocation sequence concealment:* 98.13% (105 / 107; 95% CI: 93.41% to 99.77%)
  * *Blinding: patients:* 97.20% (104 / 107; 95% CI: 92.02% to 99.42%)
  * *Blinding: healthcare providers:* 98.13% (105 / 107; 95% CI: 93.41% to 99.77%)
  * *Blinding: data collectors:* 96.26% (103 / 107; 95% CI: 90.70% to 98.97%)
  * *Blinding: outcome assessors:* 96.26% (103 / 107; 95% CI: 90.70% to 98.97%)
  * *Blinding: data analysts:* 97.20% (104 / 107; 95% CI: 92.02% to 99.42%)
  * *Missing outcome data:* 99.07% (106 / 107; 95% CI: 94.90% to 99.98%)
  * *Selective outcome reporting:* 99.07% (106 / 107; 95% CI: 94.90% to 99.98%)
  * *Other bias:* 96.26% (103 / 107; 95% CI: 90.70% to 98.97%)
* **Rate Difference (LLM-assisted vs. LLM-only ROB Assessment) (p. 4 Table 2):**
  * Overall: 1.59% (95% CI: 0.03% to 3.15%; text cites RD: 1.6%, 95% CI: 0.0%–3.2%; $p = 0.05$)
  * Sequence generation: +8.41% (95% CI: 1.25% to 15.57%)
  * Allocation sequence concealment: +1.87% (95% CI: -2.55% to 6.29%)
  * Blinding: patients: +1.87% (95% CI: -3.21% to 6.95%)
  * Blinding: healthcare providers: +1.87% (95% CI: -2.55% to 6.29%)
  * Blinding: data collectors: +1.87% (95% CI: -3.78% to 7.52%)
  * Blinding: data analysts: +0.93% (95% CI: -3.83% to 5.70%)
  * Other bias: +0.93% (95% CI: -4.44% to 6.31%)
  * Blinding: outcome assessors: 0.00% (95% CI: -5.08% to 5.08%)
  * Selective outcome reporting: 0.00% (95% CI: -2.58% to 2.58%)
  * Missing outcome data: -0.93% (95% CI: -3.49% to 1.62%)
* **Comparison to Conventional ROB Assessment Benchmark:**
  * LLM-assisted (97.3%) vs. Conventional benchmark (90.0%): RD = 7.3% (95% CI: 6.2% to 8.3%; $p < 0.001$) (p. 2).
* **ROB Diagnostic Metrics & Agreement (p. 2):**
  * Sensitivity: Selective outcome reporting = 0.50; Other bias = 0.40 (p. 2).
  * F-scores: Selective outcome reporting = 0.67; Other bias = 0.44; other domains = 0.97 to 1.00 (p. 2).
  * Cohen's kappa (model agreement): Claude-3.5-sonnet and Moonshot-v1-128k = 0.88; 66.7% of Claude's errors were also present in Moonshot's results (p. 2).
  * Inter-rater agreement among the four human reviewers (PABAK) for LLM-assisted results = 0.88 (p. 2).
  * Breakdown of Moonshot's 46 incorrect assessments: 62.1% due to missing supporting information; 37.9% involved correct data extraction but erroneous judgments (p. 2).

---

### Time and Efficiency Metrics: Does it Include Verification?
*(Locations: Page 2, Page 3 Fig. 2, Page 5 Section "Extraction and Assessment by Reviewers with Large Language Model Assistance")*

This scatter plot compares accuracy (correct rate %) against efficiency (time spent in minutes) for conventional, LLM-only, and LLM-assisted methods, illustrating the trade-offs and net time reductions.
[REGION: page=3, bbox=63,180,442,836]

**Yes, the LLM-assisted time gains explicitly include verification and refinement.**
As stated in the Methods (p. 5): *"The reviewers recorded the total time spent on each RCT, which included the time taken by the LLMs to generate the initial results plus the time spent by the reviewers to verify and modify those results."*

* **Data extraction time per RCT:**
  * *Conventional manual method benchmark:* 86.9 min (inclusive of extraction, verification, consensus) (p. 3, 5).
  * *LLM-only:* 96 s (1.6 min) with Moonshot-v1-128k; 82 s with Claude-3.5-sonnet (p. 3).
  * *LLM-assisted (Generation + Verification/Modification):* 14.7 min per RCT (p. 1, 3).
* **ROB assessment time per RCT:**
  * *Conventional manual method benchmark:* 10.4 min (p. 3, 5).
  * *LLM-only:* 42 s (0.7 min) with Moonshot-v1-128k; 41 s with Claude-3.5-sonnet (p. 3).
  * *LLM-assisted (Generation + Verification/Modification):* 5.9 min per RCT (p. 1, 3).

---

### Subgroup Findings
*(Locations: Page 2, Page 3)*
* **PDF Recognizability:** Higher PDF recognizability positively impacted Moonshot-v1-128k extraction accuracy ($p_{\text{interaction}} = 0.023$), but had no significant effect on LLM-assisted accuracy ($p_{\text{interaction}} = 0.100$) (p. 2, 3).
* **Language:**
  * Claude-3.5-sonnet had significantly higher accuracy in extracting data from English RCTs than Chinese RCTs ($p_{\text{interaction}} = 0.000$) (p. 2, 3).
  * Claude-3.5-sonnet achieved significantly higher accuracy in assessing ROB for English RCTs compared to Chinese RCTs ($p_{\text{interaction}} = 0.000$) (p. 2).
  * LLM-assisted assessments showed higher accuracy for RCTs published in Chinese ($p_{\text{interaction}} = 0.023$) (p. 3).

---

### Author Interpretations vs. Measured Performance & Limitations

#### Author Interpretations
* The authors conclude that LLMs hold strong potential for enhancing evidence synthesis efficiency and quality when integrated with human expertise ("human-in-the-loop") (p. 1, 3).
* They suggest that the higher accuracy of LLM-assisted assessments in Chinese RCTs was influenced by the reviewers' native language background (p. 3).
* They interpret differences between Claude and Moonshot across English/Chinese texts as likely attributable to differences in pre-training data compositions (p. 3).
* They argue that error patterns in ROB assessments (such as Sequence Generation) stem from challenges in applying rule-based criteria despite identifying the correct text justifications (p. 3).

#### Stated Limitations
*(Location: Page 5 Section "Strengths of this study...")*
1. **Language-dependent bias:** All four manual reviewers were native Chinese speakers, which may have favored Chinese-language evaluations during manual refinement (p. 5).
2. **Geographical/author skew:** 83 of the 107 RCTs (77.6%) were conducted in mainland China, which may restrict generalizability to broader global literature (p. 5).
3. **Reliance on external benchmark estimates:** Conventional manual accuracy and time were based on historical published benchmarks (Buscemi et al. 2006, Arno et al. 2022) rather than a concurrent head-to-head manual control group (p. 5).
4. **Model generalizability:** Only two models were tested (`Moonshot-v1-128k` and `Claude-3.5-sonnet`); results may not generalize to other model architectures or rankers without further validation (p. 5).

---

[And25]:
Here is the structured evidence record based on the full text of the article.

---

### Evidence Record: Andersen et al. (2025)

#### 1. Bibliographic Information
* **Exact Title:** Using Artificial Intelligence Tools as Second Reviewers for Data Extraction in Systematic Reviews: A Performance Comparison of Two AI Tools Against Human Reviewers
* **Complete Author Names (as printed):** T. Helms Andersen, T. M. Marcussen, A. D. Termannsen, T. W. H. Lawaetz, O. Nørgaard
* **Venue:** *Cochrane Evidence Synthesis and Methods*
* **Publication / Preprint Status:** Published journal article (Open Access; Received: 27 January 2025, Revised: 23 May 2025, Accepted: 17 June 2025; Citation: *Cochrane Evidence Synthesis and Methods*, 2025; 3:e70036)
* **DOI:** [10.1002/cesm.70036](https://doi.org/10.1002/cesm.70036)

---

#### 2. Study Design & Sample
* **Study Design:** Performance comparison / methodology evaluation study comparing data extracted by two AI tools against independent human double-extracted data (gold standard) across three published systematic reviews (Section 3, p. 2; Figure 1, p. 3).
* **Sample:**
  * **30 primary research articles** published between 2005 and 2022 (Section 4, p. 4; Appendix 2, pp. 14–15).
  * Random sample of 10 articles each from three published systematic reviews:
    * Andersen et al. (2024) [13] (sampled strictly from studies reporting quantitative data)
    * Lawaetz et al. (2025) [14]
    * Termannsen et al. (2022) [15]
  * Inclusion criteria: Searchable full-text PDFs (scanned/image-only PDFs were excluded) (Section 3.2, p. 2).
  * **Total data points:** 180 unique AI extraction data points (90 extractions per AI tool across 3 prompts/variables) (Section 4, p. 4).

---

#### 3. AI Tools, Versions, and Prompts
* **Elicit:**
  * Web application (Elicit: The AI Research Assistant; elicit.com); run using the built-in "high accuracy" mode, with prompts placed in the instructions section of three custom columns (Section 3.1, p. 2; Section 3.3, p. 3).
  * Extraction date: 5 July 2024.
* **ChatGPT:**
  * Model: `gpt-4o-2024-05-13` ("ChatGPT's GPT-4o model") via ChatGPT Plus subscription (Section 3.1, p. 2; Section 5, p. 7).
  * Each article was processed in a fresh chat, uploading the PDF alongside the first prompt, followed by three consecutive prompts (Section 3.3, p. 3).
  * Extraction date: 5 July 2024.
* **Prompting Strategy:** Structured prompts comprising a role-instruction prefix prompt and a task-specific prompt for three variables: (1) population characteristics, (2) study design, and (3) review-specific outcome variable (Section 3.3, pp. 2–3; Appendix 1, pp. 9–14).

---

#### 4. Comparator & Evaluation Process
* **Gold Standard Comparator:** Human double-extracted data independently performed by two researchers and reconciled before this study (all published in peer-reviewed journals) (Section 3.4, p. 3).
* **Comparison Procedure:**
  * Each AI-extracted item was evaluated against human extractions by original review authors.
  * An unaffiliated third researcher validated the comparisons, any disagreements were adjudicated by an additional researcher, and one author reviewed all comparisons for consistency (Section 3.5, p. 4).
  * In four cases from Lawaetz et al. where human reviewers used PlotDigitizer on graphs, AI extractions were scored as "all relevant data was found" if all other data except graph-derived values were correctly reported (Section 3.5, p. 4).
  * Data classification (Table 1, Section 3.6, p. 4):
    * **True Positive (TP):** Category 1a ("All relevant data was found") and Category 1b ("Relevant data was found, but one data point was missing" [mild underreporting]).
    * **False Positive (FP):** Category 1c ("Relevant data was found, but more than one data point was missing" [severe underreporting]), Category 1d ("Relevant data was found, but some was incorrect"), and Category 1e ("Data that was incorrect was found").
    * **False Negative (FN):** Category 1f ("No data was found").
    * **True Negative (TN):** None (dataset contained only articles known to have relevant data).

---

#### 5. Exact Numerical Findings

The following table summarizes the overall performance metrics comparing Elicit and ChatGPT against the gold standard:

This table presents precision, recall, F1 scores, absolute differences, 95% confidence intervals, and p-values from two-proportion tests comparing Elicit to ChatGPT across 90 extraction points each.
[REGION: page=6, bbox=42,67,143,923]

##### A. Overall Performance Metrics (Section 4.4 & Table 2, p. 6)
* **Precision:**
  * Elicit: **92.2%** (rounded to 92% in Abstract)
  * ChatGPT: **90.9%** (rounded to 91% in Abstract)
  * Difference: 1.3 percentage points (95% CI: −6.9% to 9.5%, $p = 0.753$)
* **Recall:**
  * Elicit: **92.2%** (rounded to 92% in Abstract)
  * ChatGPT: **88.8%** (rounded to 89% in Abstract)
  * Difference: 3.3 percentage points (95% CI: −5.2% to 11.9%, $p = 0.445$)
* **F1 Score:**
  * Elicit: **92.2%** (rounded to 92% in Abstract)
  * ChatGPT: **89.9%** (rounded to 90% in Abstract)
  * Difference: 2.3 percentage points (no significance testing performed due to violated test assumptions)

##### B. Variable-Specific Outcomes (Section 4.1, 4.2, Abstract, and Discussion, pp. 1, 5, 6)
The breakdown of retrieval outcomes across the three extraction categories is illustrated below:

This stacked bar chart shows the percentage distribution of extraction outcomes (all relevant found, 1 missing, >1 missing, some incorrect, incorrect, not found) across population characteristics, study design, and review-specific variables for both ChatGPT and Elicit.
[REGION: page=5, bbox=457,135,938,853]

* **Study Design (30 articles):**
  * Elicit: All relevant data found in **30/30 (100%)** (Section 4.1, p. 5).
  * ChatGPT: All relevant data found in **29/30 (96.7% ≈ 97%)**; no data found in **1/30** (Section 4.2, p. 5). *(Note: Abstract lists ChatGPT recall as 90%, whereas Discussion text on p. 6 lists 97% and Section 4.2 reports 29/30).*
* **Population Characteristics (30 articles):**
  * Elicit: All relevant data found in **28/30**; 1 data point missing in **2/30** (Recall: 100% [since 1 missing = TP category 1b]) (Section 4.1, p. 5; Abstract, p. 1).
  * ChatGPT: All relevant data found in **26/30**; 1 missing in **1/30**; $>1$ missing in **2/30**; relevant but some incorrect in **1/30** (Recall: 97% in Abstract, p. 1; reported as 90% in Discussion text, p. 6).
* **Review-Specific Outcome Variables (30 articles):**
  * Elicit (Recall = **77%**; Abstract, p. 1): All relevant data found in **22/30**; 1 missing in **1/30**; $>1$ missing in **3/30**; some incorrect in **3/30**; only incorrect in **1/30** (Section 4.1, p. 5).
  * ChatGPT (Recall = **80%**; Abstract, p. 1): All relevant data found in **21/30**; 1 missing in **3/30**; $>1$ missing in **3/30**; some incorrect in **1/30**; only incorrect in **1/30**; no data found in **1/30** (Section 4.2, p. 5).

##### C. Raw Extraction Categories Across All 90 Points Per Tool (Section 4.1 & 4.2, pp. 4–5)
* **Elicit (90 total):**
  * All relevant data found (Category 1a): **80/90 (88.9%)**
  * Relevant, 1 data point missing (Category 1b): **3/90 (3.3%)**
  * Relevant, $>1$ data point missing (Category 1c): **3/90 (3.3%)**
  * Relevant, but some incorrect (Category 1d): **3/90 (3.3%)**
  * Data incorrect (Category 1e): **1/90 (1.1%)**
  * No data found (Category 1f): **0/90 (0.0%)**
* **ChatGPT (90 total):**
  * All relevant data found (Category 1a): **76/90 (84.4%)**
  * Relevant, 1 data point missing (Category 1b): **4/90 (4.4%)**
  * Relevant, $>1$ data point missing (Category 1c): **5/90 (5.6%)**
  * Relevant, but some incorrect (Category 1d): **2/90 (2.2%)**
  * Data incorrect (Category 1e): **1/90 (1.1%)**
  * No data found (Category 1f): **2/90 (2.2%)**
* **Irrelevant Data (Question 2):** Found in **3/180 (2%)** extractions across both tools (Section 4.3, p. 5).

##### D. Extraction Errors and Confabulations (Section 4.5 & Table 3, p. 6)
* Total extraction errors (Categories 1b–f): **24 errors**.
  * McNemar's test: $p = 0.45$, Odds Ratio = $1.67$ (95% CI: $0.61\%–4.54\%$) (no significant difference).
  * Tool overlap: Only **1 identical error** was shared between tools (omission of change scores for Barnard et al. [20]).
  * Remaining 23 errors: **10 unique to ChatGPT**, **6 unique to Elicit**, and **3 extraction points where both erred with distinct error typologies**.
* **Error context:**
  * ChatGPT unique errors occurred predominantly in continuous text (**70.0%**).
  * Elicit unique errors occurred primarily in tabular data (**66.0%**).
  * Where both tools erred at identical points, **100%** involved tabular data exclusively.
  * RCTs accounted for **50.0%** of unique errors for both ChatGPT and Elicit.
  * The review-specific variable accounted for **50.0%** of ChatGPT's unique errors and **66.6%** of Elicit's unique errors.
  * Document density (tables/media per page) and article length showed no meaningful association with error rates.

The distribution and typology of confabulations are shown in Table 3:

This table categorizes all 7 confabulation events into specific subtypes (random values, incorrect labelling, miscalculations, rounding, or combinations) stratified by AI tool.
[REGION: page=6, bbox=182,68,318,924]

* **Confabulation Rates & Subtypes (Table 3, p. 6):**
  * Total confabulations: **7/180 data points (3.9% ≈ 4%)**.
  * Elicit: **4/90 (4%)**
    * Random values: 2
    * Incorrect labelling: 1
    * Miscalculations: 0
    * Random values and rounding values: 1
    * Random values and incorrect labelling: 0
  * ChatGPT: **3/90 (3%)**
    * Random values: 1
    * Incorrect labelling: 0
    * Miscalculations: 1
    * Random values and rounding values: 0
    * Random values and incorrect labelling: 1
  * Two-proportion z-test difference: 1.11 percentage points (95% CI: −4.54% to 6.76%, $p = 0.6998$).

---

#### 6. Author Interpretation vs. Measured Performance & Study Limitations
* **Measured Performance:**
  * Precision and recall did not significantly differ between Elicit (92.2% precision, 92.2% recall) and ChatGPT (90.9% precision, 88.8% recall).
  * Both tools performed substantially better on standardized/structural variables (study design: 90%–100%; population characteristics: 90%–100%) than on review-specific outcome variables (77%–80%).
  * Errors rarely overlapped (only 1 identical error out of 24), and confabulations were present in ~4% of extractions.
* **Author Interpretation & Proposed Workflow (Section 5, p. 7; Section 6, p. 8; Figure 3, p. 7):**
  * Authors conclude that AI tools can potentially replace the *second* human extractor in a dual-extraction workflow.
  * Because AI produces confabulations (~4%) and extraction errors, fully autonomous extraction is unsafe. Instead, they propose a "human-first" modified workflow:
    1. Human Reviewer 1 extracts data manually.
    2. AI tool (Elicit or ChatGPT) extracts data independently.
    3. Human Reviewer 2 solely compares and reconciles discrepancies between Human Reviewer 1 and the AI extraction.

This flowchart outlines the authors' recommended operational workflow: Human Reviewer 1 extracts data manually while an AI tool extracts data in parallel; Human Reviewer 2 then compares and reconciles the discrepancies between the human and AI extractions.
[REGION: page=7, bbox=665,510,935,925]

* **Explicit Study Limitations (Section 5.1, p. 8):**
  1. **No True Negative Evaluation:** The study did not test how the models handle situations where requested data is genuinely absent from the PDF ("information not available").
  2. **Single Extraction Run per Article:** AI prompts were run only once per data item; consistency/reproducibility across repeated runs within the same tool was not evaluated.
  3. **Generalizability:** The 30 sampled articles from three specific medical reviews may not reflect the full complexity, structures, or formats of systematic reviews in other fields.
  4. **Model Drift & Non-Transparency:** Rapid changes and black-box updates to underlying LLMs limit long-term reproducibility.

---

#### 7. Explanation of Time Gains & Verification
* **Did the authors empirically measure time gains?**
  * **No.** The study did not time either the human extractions or the AI extractions. There are **no measured empirical time or speed data** reported in the study.
* **Are time gains assumed or measured? Do they include verification?**
  * The time savings discussed in the introduction and discussion (e.g., citing prior estimates that systematic reviews take 67 weeks to 2 years; Section 1, p. 1) are entirely **hypothesized / conceptual benefits**, not directly measured quantities.
  * In the proposed workflow, **time savings are explicitly predicated on verification remaining intact**: the authors mandate that Human Reviewer 2 must verify and reconcile any discrepancies between the AI output and the primary human extractor's output to prevent confabulated data from entering the synthesis (Section 5, p. 7).

---

### Reference List
* [And25] T. Helms Andersen, T. M. Marcussen, A. D. Termannsen, T. W. H. Lawaetz, and O. Nørgaard, “Using Artificial Intelligence Tools as Second Reviewers for Data Extraction in Systematic Reviews: A Performance Comparison of Two AI Tools Against Human Reviewers,” *Cochrane Evidence Synthesis and Methods* 3, no. 1 (2025): e70036, https://doi.org/10.1002/cesm.70036.
* [13] T. H. Andersen, T. M. Marcussen, and O. Nørgaard, “Information Needs for GPs on Type 2 Diabetes in Western Countries: A Systematic Review,” *British Journal of General Practice* 74, no. 748 (2024): e749–e757.
* [14] T. W. H. Lawaetz, Z. Kücük, T. H. Andersen, A. K. Jensen, and J. Johannesen, “Incretin Hormone Levels (GLP-1 and GIP) in Children and Adolescents With Type 1 Diabetes: A Systematic Review,” *Pediatric Diabetes* 2025, no. 1 (2025): 1633755.
* [15] A. D. Termannsen, K. K. B. Clemmensen, J. M. Thomsen, et al., “Effects of Vegan Diets on Cardiometabolic Health: A Systematic Review and Meta-Analysis of Randomized Controlled Trials,” *Obesity Reviews* 23, no. 9 (2022): e13462.
* [20] N. D. Barnard, J. Cohen, D. J. A. Jenkins, et al., “A Low-Fat Vegan Diet Improves Glycemic Control and Cardiovascular Risk Factors in a Randomized Clinical Trial in Individuals With Type 2 Diabetes,” *Diabetes Care* 29, no. 8 (2006): 1777–1783.

---

[Col25]:
Here is the evidence wiki record for **[Col25]**, based strictly on the text and figures of the provided article:

---

### 1. Document Identifiers & Metadata
* **Exact Title:** Performance Comparison of Large Language Models for Efficient Literature Screening
* **Complete Author Names (as printed):** Maria Teresa Colangelo, Stefano Guizzardi, Marco Meleti, Elena Calciolari, Carlo Galli
* **Venue:** *BioMedInformatics* (MDPI)
* **Publication / Preprint Status:** Published journal article (Received: 18 March 2025; Revised: 18 April 2025; Accepted: 29 April 2025; Published: 7 May 2025; *BioMedInformatics* 2025, 5, 25)
* **DOI:** `https://doi.org/10.3390/biomedinformatics5020025`

---

### 2. Study Design & Pipeline
* **Study Design:** Methodological evaluation study assessing zero-shot large language model (LLM) performance for title/abstract screening across datasets stratified into quartiles of descending semantic similarity to target randomized controlled trials (RCTs).
* **Sample:**
  * **Reference systematic reviews & target sets:**
    * *Review 1 (Periodontal regeneration):* Fidan et al., 2024 [17] (9 target RCTs listed in Appendix A.1, Table A1, pp. 18–19).
    * *Review 2 (Bronchoscopy):* Yang et al., 2025 [18] (15 target studies listed in Appendix A.2, Table A2, pp. 19–20).
  * **Initial search pools retrieved from Medline/PubMed:**
    * Periodontal regeneration: 16,597 articles (Section 2.2, p. 4).
    * Bronchoscopy: 16,460 articles (Section 2.2, p. 4).
  * **Evaluation subsets ("reduced quartiles"):**
    * After ranking pool articles by cosine similarity (using `all-mpnet-base-v2` embeddings) to the mean embedding vector of the target articles into four quartiles (Q1–Q4), 200 articles were randomly sampled per quartile (Q1 = lowest similarity, Q4 = highest similarity).
    * Target articles were added to each quartile subset (Section 2.3, p. 4; Section 3, p. 10). For Fidan's dataset, each subset had 200 pool articles + 9 target articles = 209 articles total (191 true negatives, 9 true positives).

---

### 3. Tools, Software Versions & Comparators
* **Tools and Software Versions:**
  * **Hardware/Environment:** Google Colab with Tesla T4 GPU (Section 2.8, p. 9).
  * **Python libraries:**
    * `pandas` version 2.2.2 (Section 2.8, p. 10)
    * `Biopython` version 1.85 (`Entrez.efetch`) (Section 2.2, p. 4; Section 2.8, p. 10)
    * `sentence-transformers` version 3.3.1 (`all-mpnet-base-v2` model, 768-dimensional embeddings) (Section 2.3, p. 4; Section 2.8, p. 10)
    * `scikit-learn` version 1.6 (Section 2.8, p. 10)
    * `BERTopic` with `UMAP` and `HDBSCAN`, and `c-TF-IDF` (Section 2.4, p. 4)
  * **Models Evaluated:**
    1. *OpenHermes:* `OpenHermes-2.5-Mistral-7B-GGUF` (`openhermes-2.5-mistral-7b.Q4_K_M.gguf`, 4-bit quantized) (Section 2.5, p. 5).
    2. *Flan T5:* Instruction-tuned language model by Google (Section 2.5, p. 5).
    3. *GPT-2:* Developed by OpenAI (Section 2.5, p. 5).
    4. *Claude 3 Haiku:* Developed by Anthropic (Section 2.5, p. 5).
    5. *GPT-3.5 Turbo:* Accessed via OpenAI’s API (Section 2.5, p. 5).
    6. *GPT-4o:* Accessed via OpenAI’s API (Section 2.5, p. 5).
* **Comparators & Prompting Variations:**
  * Ground truth: Target studies from the original systematic reviews (target = 1) versus non-target studies verified via manual/semi-manual checks (Section 2.7, p. 8).
  * *Single prompt (soft/verbose prompt):* Tested across all models (Section 2.6.1, pp. 5–7).
  * *Double-prompt strategy (two-stage):* Initial coarse keyword filter ("Initial filter to reject articles that do not mention Bone Graft (BG) or Emdogain (EMD)"), followed by the detailed prompt; tested on OpenHermes, Flan T5, and GPT-2 (Section 2.6.2, p. 7).
  * *Concise prompt:* Step-by-step prompt designed to reduce false positives; tested on Claude 3 Haiku, GPT-3.5 Turbo, and GPT-4o (Section 2.6.3, pp. 7–8).

---

### 4. Exact Numerical Results
*(All results below are directly extracted from Section 3, Section 3.1–3.6, and Figures 3–8)*

#### A. Open Hermes (Fidan 2024 dataset; Section 3.1, p. 11; Figure 3)
* **Single Prompt:**
  * *Q1:* Accuracy = 95.5% (190 TNs out of 191; 1 TP; 8 FNs); Precision = 50%; Recall = 11.1%; F1 score = 18.2%.
  * *Q2–Q4:* TP = 0; Precision = undefined; F1 score = undefined; accuracy was "perfect or near-perfect" due to TN rejection.
* **Double Prompt:**
  * *Initial filtering step:*
    * *Q1:* Accuracy = 94.5% (189 TNs, 2 FPs, 0 TPs).
    * *Q2–Q4:* Accuracy = 95.5% (all TNs rejected, 0 TPs); Precision and F1 score = undefined.
  * *Second step (detailed evaluation):* TP = 0 across all quartiles because all target articles were filtered out in the first stage.

#### B. Flan T5 (Fidan 2024 dataset; Section 3.2, pp. 11–12; Figure 4)
* **Single Prompt:**
  * *Q1:* Accuracy = 64.5% (128 TNs, 63 FPs, 8 FNs, 1 TP); Precision = 1.6%; Recall = 11.1%; F1 score = 2.7%.
  * *Q2–Q4:* Accuracy ranged from 68% to 76.0%; precision, recall, and F1 remained consistently low.
* **Double Prompt:**
  * *Initial filtering step:*
    * FNs = 0 (Recall = 100%) across all quartiles.
    * *Q1:* Accuracy = 93.2% (178 TNs, 13 FPs, 0 FNs, 9 TPs); Precision = 40.9%; Recall = 100%; F1 score = 58%.
    * *Q2–Q4:* Accuracy ranged from 78% to 89.5%; Recall = 100%; Precision in Q4 dropped to 17% (44 FPs).
  * *Second step (detailed evaluation):*
    * TP = 0 across all quartiles.
    * *Q1:* Accuracy = 54.5% (12 TNs, 1 FP, 9 FNs, 0 TPs); Precision = 0%; Recall = 0%; F1 score = 0%.
    * *Q2–Q4:* Accuracy ranged from 60.0% to 77.4%; TP = 0.

#### C. GPT-2 (Fidan 2024 dataset; Section 3.3, pp. 12–13; Figure 5)
* **Single Prompt:**
  * Classified all articles as "Accepted" across all quartiles: TNs = 0, FNs = 0.
  * Accuracy = 4.5%; Precision = 4.5%; Recall = 100%; F1 score = 8.7%.
* **Double Prompt:**
  * *Initial filtering step:*
    * *Q1:* TNs = 178, FPs = 13; Precision = 40.9%; Recall = 100%; F1 score = 58%.
    * *Q2:* Precision = 30%.
    * *Q3:* Precision = 28.1%.
    * *Q4:* Precision = 17%; F1 score = 29%; Accuracy = 78%.
    * Accuracy across Q1–Q3 was about 90%; Recall = 100% across all quartiles.
  * *Second step (detailed evaluation):*
    * No TNs or FNs identified; FPs matched TPs across all quartiles (all initially accepted articles retained). Precision remained consistent with initial filtering, but accuracy and F1 scores were not improved.

#### D. Claude 3 Haiku (Section 3.4, pp. 13–14; Figure 6)
* **Fidan 2024 dataset:**
  * Recall was 100% (FNs = 0) across all quartiles under both prompt types.
  * *Verbose Prompt:*
    * Q1–Q3: Accuracy = 97.5%–96.5%; Precision = 64.3%–56.2%.
    * Q4: Accuracy = 76.5%; Precision = 16.1%.
  * *Concise Prompt:*
    * Q1: Accuracy up to 98.5%; Precision = 75.0%; Recall = 100%.
    * Q4: Accuracy = 65.5%; Precision = 11.5%.
* **Yang 2025 dataset:**
  * *Verbose Prompt:*
    * Q1–Q2: High accuracy and precision (exact percentages not stated in text; see Figure 6C).
    * Q3: Accuracy around 99.5%; near-perfect recall.
    * Q4: Accuracy = 87.5%; Precision = 37.5%.
  * *Concise Prompt:*
    * Q4: Precision = 20.8%; Accuracy = 71.5%; Recall remained overall "impeccable".

#### E. GPT-3.5 Turbo (Section 3.5, pp. 14–15; Figure 7)
* **Fidan 2024 dataset:**
  * *Verbose Prompt:*
    * Q1: Accuracy = 99.0%; Precision = 88.9%.
    * Q2–Q3: Accuracy ≥ 99.0%; Precision = 88.9%.
    * Q4: Precision = 30%; F1 score = 46.1%; Recall = 100%.
  * *Concise Prompt:*
    * Q1: Precision = 57.1%; F1 score = 69.4%.
    * Q2: Precision = 72.7%.
    * Q3: Precision = 53.3%.
    * Q4: Precision = 21.6%.
* **Yang 2025 dataset:**
  * *Verbose Prompt:*
    * Q1–Q3: Accuracy near or above 98.5%; high recall (slight dips in recall or precision in some Q3 runs).
    * Q4: Increased false positives.
  * *Concise Prompt:*
    * Q1: Accuracy up to 95.0%; Precision = 60.0%.
    * Q2–Q3: Precision = 70%–90%.
    * Q4: Precision = 55.6%.

#### F. GPT-4o (Section 3.6, pp. 15–16; Figure 8)
* **Fidan 2024 dataset:**
  * *Verbose Prompt:*
    * Q1–Q3: Accuracy = 100%; Precision = 100%; Recall = 100%; F1 score = 100% (all TPs and TNs identified, 0 FPs, 0 FNs).
    * Q4: Precision = 90% (caused by 1 FP); Recall = 100%; F1 score = 94.7%.
  * *Concise Prompt:*
    * Q1–Q3: Accuracy = 100%; Recall = 100%.
    * Q4: Precision = 75% (caused by 3 FPs); F1 score = 85.7%.
* **Yang 2025 dataset:**
  * *Both Prompts (Q1–Q3):* Accuracy = 100%; Precision = 100%; Recall = 100%.
  * *Verbose Prompt (Q4):* Precision ≈ 88.2%; Recall = 100%.
  * *Concise Prompt (Q4):* Precision ≈ 83.3%; Recall = 100%.

---

### Graphic Content References

The performance metrics across the different models, quartiles, and prompt conditions are summarized graphically:

A set of bar charts showing Accuracy, Precision, Recall, and F1 score for Open Hermes across quartiles Q1–Q4 under single-prompt and double-prompt conditions, showing that Open Hermes failed to retrieve true positives in almost all settings:
[REGION: page=11, bbox=197,284,547,716]

Bar charts comparing accuracy, precision, recall, and F1 score for Flan T5 across quartiles Q1–Q4 in single-prompt, double-prompt initial filtering, and double-prompt detailed evaluation configurations:
[REGION: page=12, bbox=209,284,557,716]

Bar charts displaying the performance metrics for GPT-2 across quartiles Q1–Q4, illustrating the 100% acceptance behavior in single prompt versus the impact of initial filtering in double prompt:
[REGION: page=13, bbox=148,284,496,716]

Performance metrics for Claude 3 Haiku evaluated across quartiles Q1–Q4 on both the Fidan et al. 2024 and Yang et al. 2025 reviews under verbose and concise prompts, demonstrating 100% recall but declining precision in Quartile 4:
[REGION: page=14, bbox=88,284,435,716]

Performance metrics for GPT-3.5 Turbo across quartiles Q1–Q4 for both systematic review datasets comparing verbose and concise prompting styles:
[REGION: page=15, bbox=88,284,435,716]

Performance metrics for GPT-4o showing near-perfect classification performance across all quartiles with only minor precision drops in Quartile 4:
[REGION: page=15, bbox=560,284,907,716]

---

### 5. Separation of Measured Performance vs. Author Interpretation

* **Measured Performance (Facts):**
  * Advanced models (Claude 3 Haiku, GPT-3.5 Turbo, GPT-4o) achieved near-perfect to perfect recall (100%) across all quartiles.
  * In Q4 (the highest semantic similarity quartile to the target set), all advanced models showed an increase in false positives, which depressed precision (most severely in Claude 3 Haiku down to 11.5%–16.1% and GPT-3.5 Turbo down to 21.6%–30.0%, whereas GPT-4o maintained 75%–90% precision).
  * Smaller/older models failed: OpenHermes dropped almost all target articles; GPT-2 accepted all articles in single prompting; Flan T5 had very low precision/recall in single prompting and lost all target articles in step 2 of double prompting.
* **Author Interpretations & Claims:**
  * Advanced LLMs, when guided properly, can substantially expedite systematic review screening and "approach human-level performance" (Abstract, p. 1; Section 4, p. 17).
  * Splitting tasks into multi-stage prompts does not guarantee performance gains for weaker models due to issues like "re-contextualization" or changes in classification behavior upon re-prompting (Section 4, p. 16).
  * Flan T5 and GPT-2 might still be used for broad, cost-effective initial pre-screening where high recall is paramount, but are not suitable for fine-grained selection (Section 4, p. 16).
  * GPT-4o delivers the most robust and balanced outcomes across prompt types and similarity levels (Section 4, pp. 16–17).

---

### 6. Limitations Reported by Authors
*(From Section 4, p. 17 & Section 5, p. 18)*
1. **Dataset size and scope:** Reference datasets were relatively small and domain-specific (periodontology and bronchoscopy), potentially restricting generalizability.
2. **Corpora diversity:** Behavior might vary on larger, less curated, or more heterogeneous corpora.
3. **Reliance on abstracts:** Screening relied solely on titles and abstracts; poor abstract reporting quality can skew classifications.
4. **Cost and dependencies:** Reliance on commercial paid APIs (e.g., OpenAI API for GPT-3.5 Turbo and GPT-4o) introduces external dependencies and financial costs that may not be feasible for all teams handling large datasets.
5. **Necessity of human oversight:** Models still generate false positives and occasional false negatives; human expert oversight remains necessary to handle incomplete data, resolve ambiguities, and verify borderline decisions.

---

### 7. Time Gains and Verification
* **Did time gains include verification?**
  * **No.** The authors did not measure, benchmark, or report empirical time-saving numbers (e.g., wall-clock hours) comparing LLM screening plus human verification against full manual screening.
  * When time savings are discussed (e.g., mentioning up to 90% or 96% workload reduction in Section 4, p. 17), the authors are citing external literature (specifically Delgado-Chaves et al. [10], Rayyan [43], and Research Screener [44]), rather than reporting their own measured screening times.
  * While the authors note leveraging a Tesla T4 GPU to accelerate the embedding phase ("which would otherwise take hours to be processed", Section 2.8, p. 9), specific execution times for model inference and subsequent human expert review/verification were not quantified.

---

### References Cited in the Text
* [10] Delgado-Chaves, F.M.; Jennings, M.J.; Atalaia, A.; Wolff, J.; Horvath, R.; Mamdouh, Z.M.; Baumbach, J.; Baumbach, L. Transforming literature screening: The emerging role of large language models in systematic reviews. *Proc. Natl. Acad. Sci. USA* 2025, 122, e2411962122.
* [17] Fidan, I.; Labreuche, J.; Huck, O.; Agossa, K. Combination of Enamel Matrix Derivatives with Bone Graft vs Bone Graft Alone in the Treatment of Periodontal Intrabony and Furcation Defects: A Systematic Review and Meta-Analysis. *Oral Health Prev. Dent.* 2024, 22, 655–664.
* [18] Yang, H.; Huang, J.; Zhang, Y.; Guo, J.; Xie, S.; Zheng, Z.; Ma, Y.; Deng, Q.; Zhong, C.; Li, S. The diagnostic performance and optimal strategy of cone beam CT-assisted bronchoscopy for peripheral pulmonary lesions: A systematic review and meta-analysis. *Pulmonology* 2025, 31, 1–2420562.
* [43] Ouzzani, M.; Hammady, H.; Fedorowicz, Z.; Elmagarmid, A. Rayyan—A web and mobile app for systematic reviews. *Syst. Rev.* 2016, 5, 210.
* [44] Chai, K.E.K.; Lines, R.L.J.; Gucciardi, D.F.; Ng, L. Research Screener: A machine learning tool to semi-automate abstract screening for systematic reviews. *Syst. Rev.* 2021, 10, 93.

Region format: page is 1-indexed; bbox=top,left,bottom,right, normalized 0-1000 from top-left.
