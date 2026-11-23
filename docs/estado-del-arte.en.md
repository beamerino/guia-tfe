# Literature review

This is the part that is usually done worst, and the one that shows the most. A good literature review is not a list of papers summarised one after another. It is a **methodical search** that lets you say what is known, what is missing and **why your project makes sense**.

!!! error-tipico "What I see almost every time"
    - Searching on Google (the general search engine) instead of academic databases.
    - Not knowing which type of review you are doing: systematic, scoping or narrative.
    - Not knowing the frameworks (JBI, PRISMA) or the reporting guidelines.
    - Not documenting the search, so nobody (not even you) could repeat it.

## Types of review

| Type | What it's for | Question | Key features | Reporting guideline |
|---|---|---|---|---|
| **Narrative** | General background on a topic | Broad and open | No formal protocol; selection at the author's discretion | (none) |
| **Scoping review** | Map what evidence exists, how something has been studied and where the gaps are | Broad, using **PCC** (Population, Concept, Context) | Systematic, reproducible search; usually **no** quality appraisal of studies | **PRISMA-ScR** |
| **Systematic review** | Answer a specific question with all available evidence | Specific, using **PICO** (Patient/Population, Intervention, Comparison, Outcome) | Pre-defined protocol, exhaustive search in several databases, explicit criteria, **quality or risk-of-bias appraisal**; may include meta-analysis | **PRISMA 2020** |
| **Rapid review** | A streamlined systematic review when time is short | Specific | Steps are shortened explicitly | (varies) |
| **Umbrella review** | Synthesise published reviews | Specific | The units of analysis are reviews | (varies) |

!!! clave "Which one is mine?"
    - If your project **is** a review, the most common and feasible option for a bachelor's or master's project is a **scoping review** following the **JBI** methodology and reported according to **PRISMA-ScR**.
    - If your project is about development or experiments, your related-work chapter doesn't need to be a full systematic review. But the search **must be structured and documented**: databases, search string, dates and criteria.
    - A formal systematic review requires, among other things, **two independent reviewers**. If you do it alone, state it as a limitation.

## Frameworks and guidelines

A **methodological framework** tells you *how to do* the review. A **reporting guideline** tells you *what you must report* when you write it up. They are different things, and you normally use both.

- **JBI Manual for Evidence Synthesis** (Joanna Briggs Institute): step-by-step methodology for systematic, scoping and other reviews. The most widely used reference for scoping reviews.
- **Arksey and O'Malley (2005)**, extended by **Levac et al. (2010)**: the classic five-stage framework for scoping reviews.
- **Cochrane Handbook**: the reference for systematic reviews of health interventions.
- **PRISMA 2020**: checklist and flow diagram for reporting systematic reviews.
- **PRISMA-ScR**: the PRISMA extension for scoping reviews.

All these guidelines, and many more, are collected by the [EQUATOR Network](https://www.equator-network.org/), which you will also use for your [methodology](metodologia.md#reporting-guidelines).

If your project is in health, you can **register your protocol** before you start: [PROSPERO](https://www.crd.york.ac.uk/prospero/) for systematic reviews or [OSF](https://osf.io/) for scoping reviews. It isn't required for a final project, but it adds a lot.

## Where to search

| Database | Field | Access | Notes |
|---|---|---|---|
| [Web of Science](https://www.webofscience.com/) | Multidisciplinary | Institutional | Widely used for reviews and bibliometric analyses |
| [Scopus](https://www.scopus.com/) | Multidisciplinary | Institutional | Broad coverage of engineering and health |
| [PubMed](https://pubmed.ncbi.nlm.nih.gov/) | Health and biomedicine | Free | Use **MeSH** terms for precise searches |
| [Google Scholar](https://scholar.google.com/) | Everything | Free | Useful for getting started and finding full texts, but **not reproducible**: don't use it as the only source for a review |
| [IEEE Xplore](https://ieeexplore.ieee.org/) | Engineering, electronics, computing | Institutional | Essential in engineering |
| [ACM Digital Library](https://dl.acm.org/) | Computer science | Institutional | |
| [Embase](https://www.embase.com/) | Biomedicine and pharmacology | Institutional | Complements PubMed in systematic reviews |
| [Cochrane Library](https://www.cochranelibrary.com/) | Health | Depends on country or institution | Reference systematic reviews |
| [arXiv](https://arxiv.org/) / [medRxiv](https://www.medrxiv.org/) | Preprints | Free | **Not peer-reviewed**: use with care and say so |

"Institutional" access comes with your university account through the library (VPN or remote access). Ask your library: they often offer free training on these databases.

**For a review, use at least two or three databases**: for example PubMed + Scopus + Web of Science in health, or IEEE Xplore + Scopus + ACM in engineering.

## Building your search

### 1. Break down your question

Use **PICO** (systematic review) or **PCC** (scoping review). For example, for a scoping review on AI to detect atrial fibrillation:

| Element | Concept | Synonyms and terms |
|---|---|---|
| Population | People with atrial fibrillation | atrial fibrillation, AF, AFib |
| Concept | Artificial intelligence | artificial intelligence, machine learning, deep learning, neural network |
| Context | Electrocardiogram | electrocardiogram, ECG, EKG, wearable |

### 2. Combine with Boolean operators

- **OR** within each concept (synonyms), **AND** between concepts.
- **Quotation marks** for exact phrases: `"machine learning"`.
- **Asterisk** to truncate: `predict*` finds *predict, prediction, predictive…*
- Restrict to title, abstract and keywords to reduce noise.

```text
("artificial intelligence" OR "machine learning" OR "deep learning" OR "neural network*")
AND ("atrial fibrillation" OR AFib)
AND (electrocardiogram* OR ECG OR EKG OR wearable*)
```

Each database has its own syntax for searching specific fields, for example `TITLE-ABS-KEY(...)` in Scopus, `TS=(...)` in Web of Science, or `[tiab]` and `[MeSH Terms]` in PubMed. Adapt the string to each one and **save the exact version you used**.

### 3. Document everything

For each database, record in a table: **search date, exact string, filters (years, language, document type) and number of results**. Someone else must be able to repeat it. There's a table for this under [Templates](plantillas.md).

### 4. Screen

1. Export the results to your [reference manager](bibliografia.md) and **remove duplicates**.
2. **Screen titles and abstracts** against your inclusion and exclusion criteria, defined **before** you start.
3. **Read the full text** of those that pass the first screening, recording the reason for each exclusion.
4. Tools such as [Rayyan](https://www.rayyan.ai/) (free) make screening much easier.
5. Summarise the process in a **PRISMA flow diagram**: records identified → screened → excluded (with reasons) → included.

### 5. Extract and synthesise

For each included study, fill in an **extraction table**: authors and year, country, objective, data or population, method, main results and limitations. From that table:

- **Group by themes**, not by papers.
- **Compare**: which methods are most used? What results do they get? With what data?
- **Identify the gap**: what hasn't been done, has been done poorly, or hasn't been done in your context.

For a systematic review, also appraise the **quality or risk of bias** of each study with a suitable tool (for example, the JBI critical appraisal checklists, RoB 2 for trials or PROBAST for prediction models).

## Writing the related work

!!! clave "The chapter must end by justifying your objective"
    The last section of your related work should say, in one paragraph: *"Therefore, X does not exist / X has not been evaluated in Y / previous work has limitation Z. This project addresses…"*. That's the bridge to your [objectives](estructura.md#objectives).

- **Poor:** "García et al. (2021) did X. López et al. (2022) did Y. Smith et al. (2023) did Z…".
- **Good** (made-up example): "Approaches based on convolutional networks dominate recent literature [3–8], with sensitivities between 85% and 97%. However, most have been evaluated on 12-lead hospital recordings [3, 5, 6] and few on single-lead devices [7]…".
- Include a **comparison table** of the most relevant studies (method, data, result, limitation). It reads far better than ten paragraphs.
