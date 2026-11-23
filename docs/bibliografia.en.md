# References: citing and reference managers

Typing references by hand is the surest way to get them wrong: numbers that don't match, mixed formats, citations that disappear when you move a paragraph. A **reference manager** does it for you, and it gets **installed on day one**, not in the week of submission.

!!! error-tipico "What I see almost every time"
    - References copied by hand, each in a different format.
    - Citations in the text that aren't in the reference list, or the other way round.
    - References to generic web pages, Wikipedia or blogs instead of the original source.
    - Installing the manager at the end and trying to reconstruct where everything came from.

## Which manager to use

| | Zotero | Mendeley |
|---|---|---|
| Price | Free and open source | Free (by Elsevier) |
| Browser capture | Zotero Connector | Mendeley Web Importer |
| Word integration | Built-in plugin | Mendeley Cite |
| LaTeX integration | Exports `.bib` (best with the Better BibTeX plugin) | Exports `.bib` |
| Google Docs | Yes | No |
| My recommendation | **Yes**: my default recommendation | If your group or university already uses it |

Both work. What matters is **using one from the start**.

## Zotero in 10 minutes

1. **Install** [Zotero](https://www.zotero.org/download/) and the **Zotero Connector** for your browser.
2. **Create an account** and turn on syncing, so your library is available on any computer.
3. **Create a collection** for your project (and sub-collections by theme if you like).
4. **Save references** from your browser: on the article page (PubMed, Scopus, IEEE Xplore, the journal…), click the Connector icon. Zotero saves the metadata and, where possible, the PDF.
5. **Add by identifier**: the magic wand button lets you paste a **DOI**, PMID or ISBN.
6. **Check the metadata**: authors, year, journal, volume and pages. The Connector sometimes gets it wrong, especially with web pages and preprints.
7. **Cite in Word**: in the Zotero tab, *Add/Edit Citation* inserts a citation and *Add/Edit Bibliography* inserts the reference list. Choose the style in *Document Preferences*.
8. **Cite in LaTeX**: install the [Better BibTeX](https://retorque.re/zotero-better-bibtex/) plugin, export the collection as `.bib` with the keep-updated option, and cite with `\cite{key}`.
9. **Import your search results**: Web of Science, Scopus and PubMed export to RIS or similar formats, which Zotero imports directly. Then use *Duplicate Items* to remove duplicates.

!!! tip "Mendeley"
    The workflow is the same: install [Mendeley Reference Manager](https://www.mendeley.com/), the Web Importer and the **Mendeley Cite** add-in for Word.

## Which citation style

Use the one your university or degree specifies. If none is specified:

| Style | Format | Common in |
|---|---|---|
| **IEEE** | Numbered in square brackets: [1] | Engineering and computing |
| **Vancouver** | Numbered: (1) or superscript | Health sciences |
| **APA 7** | Author–date: (García, 2023) | Social sciences, psychology, education |

Pick one and **don't mix them**. With a manager, changing style is one click.

## Good citation practice

- **Cite the original source.** If a paper says "according to X…", find and read X.
- **Every claim that isn't yours or common knowledge needs a citation**: data, figures, definitions, other people's methods.
- **Paraphrase and cite.** Copying sentences without quotation marks is plagiarism, even if you cite. Direct quotes go in quotation marks and should be rare.
- **Prefer peer-reviewed** sources, recent ones (last 5–10 years, except for classic work), from recognised journals or conferences.
- **Cite data and software too**: datasets (with their DOI if they have one), main libraries and tools.
- **Check every reference.** That it exists, that it says what you claim, and that its details are complete. This matters even more if you've used [generative AI](ia.md): AI tools **make up references** with total confidence.
