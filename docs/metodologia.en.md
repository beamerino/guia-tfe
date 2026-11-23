# Methodology and development

Methodology is what turns "I did some things" into "I followed a method that someone else could repeat". In the thesis it goes in the **Materials and methods** chapter, and it's worth being clear about the difference between the two parts.

## Materials and methods: what goes where

<div class="grid" markdown>

<div class="card" markdown>
**Materials** = *what* you used

Your tools: data and where it came from, participants, hardware, software, languages and libraries (with versions), measuring instruments, questionnaires…
</div>

<div class="card" markdown>
**Methods** = *which steps* you took and *based on which* methodology

The steps in order, justified by a recognised methodology, with enough detail for someone else to repeat them.
</div>

</div>

!!! clave "One method step per secondary objective"
    If you have three secondary objectives, your method should have (at least) three clear steps, and each one will produce **one result**. That way the thesis organises itself: see [Thesis structure](estructura.md#the-common-thread).

## Build on a recognised methodology

Don't invent your process: pick a framework and say so explicitly ("following the X methodology [ref]"). Some examples by type of project:

| Type of project | Common methodologies or frameworks |
|---|---|
| Literature review | JBI, PRISMA 2020, PRISMA-ScR (see [Literature review](estado-del-arte.md)) |
| Data analysis / machine learning | CRISP-DM; validation with training, validation and test sets or cross-validation |
| Software development | Waterfall life cycle, agile methods (Scrum, Kanban), with requirements, design, implementation and testing |
| Product or app design with users | User-centred design (ISO 9241-210), Design Thinking, usability evaluation (for example with the SUS questionnaire) |
| Building an engineering artefact | Design Science Research |
| Study with people | Study design (observational, experimental, qualitative) + the matching reporting guideline (see below) |

## Reporting guidelines

**Reporting guidelines** are checklists that set out **what information must appear** in a piece of work depending on its type. They are collected by the [EQUATOR Network](https://www.equator-network.org/). Although designed for papers, they're the best way to make sure your methods and results are complete. **If your project fits one, use it and cite it.**

The most relevant ones for digital health and AI projects:

| Type of study | Guideline | AI extension |
|---|---|---|
| Clinical trial protocol | SPIRIT | **SPIRIT-AI** |
| Clinical trial results | CONSORT | **CONSORT-AI** |
| Prediction model (diagnostic or prognostic) | TRIPOD | **TRIPOD+AI** |
| Early clinical evaluation of an AI decision-support system | — | **DECIDE-AI** |
| AI in medical imaging | — | **CLAIM** |
| Diagnostic test accuracy | STARD | — |
| Observational study | STROBE | — |
| Qualitative research (interviews, focus groups) | COREQ, SRQR | — |
| Systematic / scoping review | PRISMA 2020 / PRISMA-ScR | — |

Always check EQUATOR for the latest version: these guidelines are updated and new extensions appear.

!!! tip "How to use the guideline in your project"
    Download the checklist, go through it item by item and, at the end, include it as an **appendix** stating on which page or section of your thesis each item is addressed. Few things signal rigour as clearly.

## Good practice during development

### Data

- Describe the **source** of the data, how it was obtained, how much there is and its main characteristics.
- If it's **data about people**, especially health data, comply with the GDPR: anonymise or pseudonymise, and check whether you need **ethics committee** approval. Apply early, as it takes time.
- **Never** upload personal or clinical data to online tools (including [generative AI](ia.md) tools).

### Validation and evaluation

- Decide **before** you start which **metrics** you'll use and why they suit your problem.
- Compare against something: a **baseline**, the state of the art or a simple alternative. 90% accuracy means nothing if the simplest method gets 89%.
- In machine learning, keep training and test data properly separated and **avoid data leakage**: for example, records from the same patient ending up in both sets.
- If you compare results, use the right **statistical test** and report confidence intervals where possible.

### Reproducibility

- Use **version control** (Git) for your code.
- Record **versions** of libraries and tools, random seeds and parameters.
- If you can, publish your code in a repository (GitHub, Zenodo) and link to it in the thesis.

## Writing the methods

- In the **past tense**, either impersonal or first-person plural, but consistently.
- **In the order** things were done, with one section per step.
- With **enough detail for someone else to repeat it**: not a diary of everything you tried, but not "a model was trained" either.
- What does **not** go here: results. If you write "and 92% was obtained", that belongs in the results chapter.
- A **diagram** of the whole process at the start of the chapter helps enormously.
