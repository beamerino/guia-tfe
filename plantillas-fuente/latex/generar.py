"""Genera las plantillas LaTeX (ES y EN) como .zip listos para subir a Overleaf.
Uso: python3 generar.py <carpeta_salida> [--compilar]
"""
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent

T = {
    "es": {
        "zip": "plantilla-latex-es.zip",
        "carpeta_cap": "capitulos",
        "bib": "referencias",
        "babel": r"\usepackage[spanish,es-tabla,es-nodecimaldot]{babel}",
        "universidad": "[Universidad]",
        "escuela": "[Escuela o Facultad]",
        "titulacion": "[Titulación]",
        "tipo": "Trabajo Fin de [Grado / Máster / Estudios]",
        "titulo": "[Título del trabajo: concreto y descriptivo]",
        "autor_et": "Autor/a", "autor": "[Nombre y apellidos]",
        "director_et": "Director/a", "director": "[Nombre y apellidos]",
        "fecha": "[Mes y año]",
        "nota_portada": "Adapta esta portada al modelo oficial de tu universidad.",
        "resumen": "Resumen",
        "resumen_txt": "Escríbelo al final. Entre 250 y 300 palabras: contexto (1--2 frases), objetivo, métodos, resultados principales con cifras y conclusión.",
        "pc": r"\textbf{Palabras clave:} [4--6 palabras clave separadas por comas]",
        "abstract": "Abstract",
        "abstract_txt": "Traducción al inglés del resumen.",
        "kw": r"\textbf{Keywords:} [4--6 keywords]",
        "acronimos": "Lista de acrónimos",
        "ia": "Declaración de uso de IA generativa",
        "ia_txt": "Si la has usado: qué herramienta y versión, para qué, en qué partes y cómo verificaste el resultado.",
        "referencias": "Referencias",
        "anexos": "Anexos",
        "figura": "Ejemplo de pie de figura: describe lo que muestra sin necesidad de leer el texto.",
        "tabla": "Ejemplo de tabla comparativa de trabajos relacionados (el pie de las tablas va encima).",
        "cols": ["Trabajo", "Método", "Datos", "Resultado", "Limitación"],
        "capitulos": [
            ("introduccion", "Introducción", [
                ("Contexto", "Del tema general al problema concreto. Apoya cada afirmación con datos y citas~\\cite{ejemplo2024}."),
                ("Problema y motivación", "¿Qué problema abordas y por qué merece la pena resolverlo?"),
                ("Estructura del documento", "Un párrafo breve que explique qué contiene cada capítulo. Escribe la introducción al final."),
            ]),
            ("trabajos-relacionados", "Trabajos relacionados", [
                ("Metodología de búsqueda", "Tipo de revisión y marco seguido (JBI, PRISMA\\ldots), bases de datos, cadena de búsqueda, fechas, criterios de inclusión y exclusión y diagrama de flujo."),
                ("[Tema 1]", "Organiza por temas, no por artículos. Compara métodos, datos y resultados (ver Tabla~\\ref{tab:comparativa}).\n\nTABLA"),
                ("[Tema 2]", "\\ldots"),
                ("Síntesis y hueco de investigación", "Termina explicando qué falta en la literatura y cómo lo aborda tu trabajo."),
            ]),
            ("objetivos", "Objetivos", [
                ("Objetivo principal", "Uno solo, en una frase, con un verbo comprobable (diseñar, desarrollar, evaluar, comparar, validar\\ldots)."),
                ("Objetivos secundarios", "\\begin{enumerate}[label=\\textbf{OS\\arabic*.}]\n  \\item {}[Objetivo secundario 1]\n  \\item {}[Objetivo secundario 2]\n  \\item {}[Objetivo secundario 3]\n\\end{enumerate}\nCada uno corresponderá a un paso del método y a un resultado."),
            ]),
            ("materiales-metodos", "Materiales y métodos", [
                ("Materiales", "Con qué lo has hecho: datos y su origen, participantes, \\textit{software} y \\textit{hardware} (con versiones), instrumentos."),
                ("Métodos", "Qué pasos has dado y basándote en qué metodología. Empieza con un diagrama del proceso completo (Figura~\\ref{fig:proceso}).\n\nFIGURA"),
                ("!Paso 1 (OS1)", "Detalle suficiente para que otra persona pueda repetirlo."),
                ("!Paso 2 (OS2)", "\\ldots"),
                ("!Paso 3 (OS3)", "\\ldots"),
                ("Evaluación", "Métricas, método de referencia (\\textit{baseline}) y pruebas estadísticas."),
            ]),
            ("resultados", "Resultados", [
                ("Resultado del paso 1", "Un apartado por paso del método, en el mismo orden. Solo hechos: cifras, tablas y figuras, sin interpretar."),
                ("Resultado del paso 2", "\\ldots"),
                ("Resultado del paso 3", "\\ldots"),
            ]),
            ("discusion", "Discusión", [
                ("Interpretación de los resultados", "¿Qué significan tus resultados?"),
                ("Comparación con el estado del arte", "¿Coinciden con lo publicado o lo contradicen? ¿Por qué?"),
                ("Limitaciones", "Qué no se puede afirmar con tus datos o tu diseño."),
                ("Implicaciones", "Para quién es útil y en qué contexto."),
            ]),
            ("conclusiones", "Conclusiones", [
                ("Conclusiones", "Una por objetivo: si se ha cumplido y cómo. Sin datos nuevos ni citas."),
                ("Líneas futuras", "Qué harías con más tiempo o recursos."),
            ]),
        ],
        "anexo": ("Lista de comprobación de la guía de publicación", "Por ejemplo, la lista de comprobación de la guía seguida (PRISMA-ScR, TRIPOD+AI\\ldots), indicando dónde se cumple cada punto."),
        "leeme": (
            "PLANTILLA LaTeX - TRABAJO FIN DE TITULACIÓN\n\n"
            "Overleaf: New Project > Upload Project y sube este .zip sin descomprimir.\n"
            "Archivo principal: main.tex. Capítulos en capitulos/. Figuras en figuras/.\n"
            "Bibliografía: sustituye referencias.bib por la exportación de tu gestor\n"
            "(Zotero + Better BibTeX). Compila con biber (Overleaf lo hace solo).\n"
            "Estilo de cita: cambia 'style=ieee' en main.tex por 'style=numeric-comp',\n"
            "'style=vancouver' o 'style=apa' según tu titulación.\n"
            "Adapta la portada al modelo oficial de tu universidad.\n"
        ),
    },
    "en": {
        "zip": "latex-template-en.zip",
        "carpeta_cap": "chapters",
        "bib": "references",
        "babel": r"\usepackage[english]{babel}",
        "universidad": "[University]",
        "escuela": "[School or Faculty]",
        "titulacion": "[Degree programme]",
        "tipo": "[Bachelor's / Master's] Final Project",
        "titulo": "[Project title: specific and descriptive]",
        "autor_et": "Author", "autor": "[Full name]",
        "director_et": "Supervisor", "director": "[Full name]",
        "fecha": "[Month and year]",
        "nota_portada": "Adapt this cover page to your university's official template.",
        "resumen": "Abstract",
        "resumen_txt": "Write it last. 250--300 words: background (1--2 sentences), objective, methods, main results with figures, and conclusion.",
        "pc": r"\textbf{Keywords:} [4--6 keywords separated by commas]",
        "abstract": "Resumen",
        "abstract_txt": "Abstract in the other language required by your university (for example Spanish), if any. Delete otherwise.",
        "kw": r"\textbf{Palabras clave:} [4--6]",
        "acronimos": "List of acronyms",
        "ia": "Declaration of generative AI use",
        "ia_txt": "If you used it: which tool and version, what for, in which parts, and how you verified the output.",
        "referencias": "References",
        "anexos": "Appendices",
        "figura": "Example caption: describe what the figure shows without needing the text.",
        "tabla": "Example comparison table of related work (table captions go above).",
        "cols": ["Study", "Method", "Data", "Result", "Limitation"],
        "capitulos": [
            ("introduction", "Introduction", [
                ("Background", "From the general topic to the specific problem. Support every claim with data and citations~\\cite{ejemplo2024}."),
                ("Problem and motivation", "Which problem are you tackling and why is it worth solving?"),
                ("Document structure", "A short paragraph explaining what each chapter contains. Write the introduction last."),
            ]),
            ("related-work", "Related work", [
                ("Search methodology", "Type of review and framework followed (JBI, PRISMA\\ldots), databases, search string, dates, inclusion and exclusion criteria and flow diagram."),
                ("[Theme 1]", "Organise by themes, not by papers. Compare methods, data and results (see Table~\\ref{tab:comparativa}).\n\nTABLA"),
                ("[Theme 2]", "\\ldots"),
                ("Synthesis and research gap", "End by explaining what is missing from the literature and how your project addresses it."),
            ]),
            ("objectives", "Objectives", [
                ("Main objective", "Only one, in one sentence, with a verb you can check (design, develop, evaluate, compare, validate\\ldots)."),
                ("Secondary objectives", "\\begin{enumerate}[label=\\textbf{SO\\arabic*.}]\n  \\item {}[Secondary objective 1]\n  \\item {}[Secondary objective 2]\n  \\item {}[Secondary objective 3]\n\\end{enumerate}\nEach will match one method step and one result."),
            ]),
            ("materials-methods", "Materials and methods", [
                ("Materials", "What you used: data and its source, participants, software and hardware (with versions), instruments."),
                ("Methods", "Which steps you took and based on which methodology. Start with a diagram of the whole process (Figure~\\ref{fig:proceso}).\n\nFIGURA"),
                ("!Step 1 (SO1)", "Enough detail for someone else to repeat it."),
                ("!Step 2 (SO2)", "\\ldots"),
                ("!Step 3 (SO3)", "\\ldots"),
                ("Evaluation", "Metrics, baseline and statistical tests."),
            ]),
            ("results", "Results", [
                ("Result of step 1", "One section per method step, in the same order. Facts only: figures, tables and charts, no interpretation."),
                ("Result of step 2", "\\ldots"),
                ("Result of step 3", "\\ldots"),
            ]),
            ("discussion", "Discussion", [
                ("Interpreting the results", "What do your results mean?"),
                ("Comparison with the state of the art", "Do they agree with published work or contradict it? Why?"),
                ("Limitations", "What can't be claimed with your data or design."),
                ("Implications", "Who it is useful for and in what context."),
            ]),
            ("conclusions", "Conclusions", [
                ("Conclusions", "One per objective: whether and how it was met. No new data and no citations."),
                ("Future work", "What you would do with more time or resources."),
            ]),
        ],
        "anexo": ("Reporting guideline checklist", "For example, the checklist of the guideline you followed (PRISMA-ScR, TRIPOD+AI\\ldots), showing where each item is addressed."),
        "leeme": (
            "LaTeX TEMPLATE - FINAL DEGREE PROJECT\n\n"
            "Overleaf: New Project > Upload Project and upload this .zip without unzipping it.\n"
            "Main file: main.tex. Chapters in chapters/. Figures in figures/.\n"
            "Bibliography: replace references.bib with the export from your reference\n"
            "manager (Zotero + Better BibTeX). Compile with biber (Overleaf does it for you).\n"
            "Citation style: change 'style=ieee' in main.tex to 'style=numeric-comp',\n"
            "'style=vancouver' or 'style=apa' as your degree requires.\n"
            "Adapt the cover page to your university's official template.\n"
        ),
    },
}

TABLA = r"""\begin{table}[htbp]
  \centering
  \caption{%s}
  \label{tab:comparativa}
  \small
  \begin{tabularx}{\textwidth}{lXXXX}
    \toprule
    \textbf{%s} & \textbf{%s} & \textbf{%s} & \textbf{%s} & \textbf{%s} \\
    \midrule
    \cite{ejemplo2024} & [\ldots] & [\ldots] & [\ldots] & [\ldots] \\
    {}[\ldots] & [\ldots] & [\ldots] & [\ldots] & [\ldots] \\
    \bottomrule
  \end{tabularx}
\end{table}"""

FIGURA = r"""\begin{figure}[htbp]
  \centering
  \fbox{\parbox[c][4cm][c]{0.8\textwidth}{\centering [figuras/proceso.pdf]}}
  %% \includegraphics[width=0.8\textwidth]{figuras/proceso}
  \caption{%s}
  \label{fig:proceso}
\end{figure}"""


def capitulo(titulo, secciones, L):
    out = [f"\\chapter{{{titulo}}}", ""]
    for nombre, texto in secciones:
        cmd = "subsection" if nombre.startswith("!") else "section"
        out.append(f"\\{cmd}{{{nombre.lstrip('!')}}}")
        texto = texto.replace("TABLA", TABLA % (L["tabla"], *L["cols"]))
        texto = texto.replace("FIGURA", FIGURA.replace("figuras/", L["carpeta_fig"] + "/") % L["figura"])
        out.append(texto)
        out.append("")
    return "\n".join(out)


def main_tex(L):
    cap = L["carpeta_cap"]
    inputs = "\n".join(f"\\input{{{cap}/{c[0]}}}" for c in L["capitulos"])
    return rf"""% Plantilla de trabajo fin de titulación · Final degree project template
% Beatriz Merino-Barbancho — https://beamerino.github.io/guia-tfe/
\documentclass[12pt,a4paper,oneside]{{report}}

% ---------- Idioma y codificación ----------
\usepackage[utf8]{{inputenc}}
\usepackage[T1]{{fontenc}}
{L["babel"]}
\usepackage{{lmodern}}
\usepackage{{csquotes}}

% ---------- Página ----------
\usepackage[margin=2.5cm]{{geometry}}
\usepackage{{setspace}}
\onehalfspacing
\usepackage{{parskip}}

% ---------- Figuras, tablas, listas ----------
\usepackage{{graphicx}}
\usepackage{{booktabs}}
\usepackage{{tabularx}}
\usepackage{{enumitem}}
\usepackage{{xcolor}}
\usepackage[font=small,labelfont=bf]{{caption}}

% ---------- Acrónimos ----------
\usepackage{{acronym}}

% ---------- Bibliografía ----------
% Cambia style=ieee por numeric-comp, vancouver o apa según tu titulación.
\usepackage[backend=biber,style=ieee]{{biblatex}}
\addbibresource{{{L["bib"]}.bib}}

% ---------- Enlaces (cargar al final) ----------
\usepackage[hidelinks]{{hyperref}}

\begin{{document}}

% ================= PORTADA =================
\begin{{titlepage}}
  \centering
  {{\large\bfseries {L["universidad"]}\par {L["escuela"]}\par {L["titulacion"]}\par}}
  \vspace{{3cm}}
  {{\large {L["tipo"]}\par}}
  \vspace{{0.8cm}}
  {{\LARGE\bfseries {L["titulo"]}\par}}
  \vfill
  {{\large {L["autor_et"]}: {L["autor"]}\par\smallskip
   {L["director_et"]}: {L["director"]}\par\smallskip
   {{}}{L["fecha"]}\par}}
  \vspace{{1.5cm}}
  {{\small\itshape\color{{gray}} {L["nota_portada"]}\par}}
\end{{titlepage}}

\pagenumbering{{roman}}

% ================= RESUMEN =================
\chapter*{{{L["resumen"]}}}
\addcontentsline{{toc}}{{chapter}}{{{L["resumen"]}}}
{L["resumen_txt"]}

{L["pc"]}

\chapter*{{{L["abstract"]}}}
\addcontentsline{{toc}}{{chapter}}{{{L["abstract"]}}}
{L["abstract_txt"]}

{L["kw"]}

% ================= ÍNDICES =================
\tableofcontents
\listoffigures
\listoftables

\chapter*{{{L["acronimos"]}}}
\addcontentsline{{toc}}{{chapter}}{{{L["acronimos"]}}}
\begin{{acronym}}[ECG]
  \acro{{ECG}}{{{"electrocardiograma" if L["bib"] == "referencias" else "electrocardiogram"}}}
\end{{acronym}}

% ================= CAPÍTULOS =================
\cleardoublepage
\pagenumbering{{arabic}}

{inputs}

% ================= IA GENERATIVA =================
\chapter*{{{L["ia"]}}}
\addcontentsline{{toc}}{{chapter}}{{{L["ia"]}}}
{L["ia_txt"]}

% ================= REFERENCIAS =================
\printbibliography[heading=bibintoc,title={{{L["referencias"]}}}]

% ================= ANEXOS =================
\appendix
\chapter{{{L["anexo"][0]}}}
{L["anexo"][1]}

\end{{document}}
"""


BIB = r"""% Sustituye este archivo por la exportación de tu gestor de referencias
% (Zotero + Better BibTeX). / Replace with your reference manager's export.
@article{ejemplo2024,
  author  = {Apellido, Nombre and Otro, Autor},
  title   = {Título del artículo de ejemplo},
  journal = {Nombre de la Revista},
  year    = {2024},
  volume  = {10},
  number  = {2},
  pages   = {1--10},
  doi     = {10.0000/ejemplo}
}
"""


def generar(lang, salida: Path, compilar: bool):
    L = dict(T[lang])
    L["carpeta_fig"] = "figuras" if lang == "es" else "figures"
    base = salida / f"_latex_{lang}"
    if base.exists():
        shutil.rmtree(base)
    (base / L["carpeta_cap"]).mkdir(parents=True)
    (base / L["carpeta_fig"]).mkdir()
    (base / "main.tex").write_text(main_tex(L), encoding="utf-8")
    (base / f"{L['bib']}.bib").write_text(BIB, encoding="utf-8")
    (base / ("LEEME.txt" if lang == "es" else "README.txt")).write_text(L["leeme"], encoding="utf-8")
    (base / L["carpeta_fig"] / ".gitkeep").write_text("", encoding="utf-8")
    for slug, titulo, secs in L["capitulos"]:
        (base / L["carpeta_cap"] / f"{slug}.tex").write_text(capitulo(titulo, secs, L), encoding="utf-8")

    if compilar:
        r = subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                           cwd=base, capture_output=True, text=True, errors="replace")
        print(lang, "latexmk ->", r.returncode)
        if r.returncode != 0:
            print(r.stdout[-3000:])
        else:
            shutil.copy(base / "main.pdf", salida / f"_vista_{lang}.pdf")

    destino = salida / L["zip"]
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(base.rglob("*")):
            if f.is_file() and f.suffix in {".tex", ".bib", ".txt", ""}:
                z.write(f, f.relative_to(base))
    shutil.rmtree(base)
    print("->", destino)


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    out.mkdir(parents=True, exist_ok=True)
    for lang in ("es", "en"):
        generar(lang, out, "--compilar" in sys.argv)
