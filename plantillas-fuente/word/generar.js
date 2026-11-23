// Genera las plantillas Word (memoria y ficha de propuesta) en español e inglés.
// Uso: node generar.js <carpeta_salida>
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, PageBreak,
  TableOfContents, Footer, PageNumber, Table, TableRow, TableCell, WidthType,
  ShadingType, BorderStyle, LevelFormat,
} = require("docx");

const OUT = process.argv[2] || ".";
const FONT = "Calibri";
const INDIGO = "2A2563";
const GRIS = "5B5A66";
const HIELO = "EAF0F6";
const CONTENT_W = 9072; // A4 con márgenes de 2,5 cm

const estilos = {
  default: { document: { run: { font: FONT, size: 24 }, paragraph: { spacing: { after: 120, line: 300 } } } },
  paragraphStyles: [
    { id: "Title", name: "Title", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { font: FONT, size: 44, bold: true, color: INDIGO },
      paragraph: { alignment: AlignmentType.CENTER, spacing: { before: 240, after: 240 }, keepNext: true } },
    { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { font: FONT, size: 32, bold: true, color: INDIGO },
      paragraph: { spacing: { before: 360, after: 200 }, keepNext: true, outlineLevel: 0 } },
    { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { font: FONT, size: 28, bold: true, color: INDIGO },
      paragraph: { spacing: { before: 240, after: 120 }, keepNext: true, outlineLevel: 1 } },
    { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { font: FONT, size: 24, bold: true, color: "2A2563" },
      paragraph: { spacing: { before: 200, after: 100 }, keepNext: true, outlineLevel: 2 } },
  ],
};

const numeracion = {
  config: [{
    reference: "vinetas",
    levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 720, hanging: 360 } } } }],
  }],
};

const guia = (t) => new Paragraph({ children: [new TextRun({ text: t, italics: true, color: GRIS })] });
const guiaVineta = (t) => new Paragraph({ numbering: { reference: "vinetas", level: 0 },
  children: [new TextRun({ text: t, italics: true, color: GRIS })] });
const h1 = (t, saltoAntes = true) => new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: saltoAntes, children: [new TextRun(t)] });
const h2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(t)] });
const centrado = (t, opts = {}) => new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: opts.after ?? 120 },
  children: [new TextRun({ text: t, size: opts.size ?? 24, bold: !!opts.bold, color: opts.color ?? (opts.gris ? GRIS : undefined), italics: !!opts.gris })] });

function pie(textoPagina) {
  return { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
    children: [new TextRun({ children: [textoPagina, PageNumber.CURRENT], size: 20, color: GRIS })] })] }) };
}

const pagina = { page: { size: { width: 11906, height: 16838 }, margin: { top: 1417, bottom: 1417, left: 1417, right: 1417 } } };

// ---------- Textos ----------
const T = {
  es: {
    archivoMemoria: "plantilla-memoria-es.docx",
    archivoFicha: "ficha-propuesta-es.docx",
    pagina: "",
    portada: ["[Universidad]", "[Escuela o Facultad]", "[Titulación]"],
    tipo: "Trabajo Fin de [Grado / Máster / Estudios]",
    titulo: "[Título del trabajo: concreto y descriptivo]",
    datos: ["Autor/a: [Nombre y apellidos]", "Director/a: [Nombre y apellidos]", "[Mes y año]"],
    notaPortada: "Adapta esta portada al modelo oficial de tu universidad.",
    resumen: "Resumen",
    resumenGuia: ["Escríbelo al final. Entre 250 y 300 palabras, o lo que indique tu normativa.",
      "Estructura: contexto (1–2 frases), objetivo, métodos, resultados principales con cifras y conclusión."],
    palabrasClave: "Palabras clave: [4–6 palabras clave separadas por comas]",
    abstract: "Abstract",
    abstractGuia: "Traducción al inglés del resumen. Revísala con cuidado: los términos técnicos deben ser los que se usan en la literatura.",
    keywords: "Keywords: [4–6 keywords]",
    indice: "Índice",
    indiceGuia: "Si el índice aparece vacío, haz clic derecho sobre él y elige «Actualizar campos».",
    acronimos: "Lista de acrónimos",
    acronimosGuia: "Por orden alfabético. Ejemplo: ECG — Electrocardiograma.",
    capitulos: [
      { t: "1. Introducción", secs: [
        ["1.1. Contexto", "Del tema general al problema concreto. Apoya cada afirmación con datos y citas."],
        ["1.2. Problema y motivación", "¿Qué problema abordas y por qué merece la pena resolverlo?"],
        ["1.3. Estructura del documento", "Un párrafo breve que explique qué contiene cada capítulo. Escribe la introducción al final."],
      ] },
      { t: "2. Trabajos relacionados", secs: [
        ["2.1. Metodología de búsqueda", "Tipo de revisión y marco seguido (JBI, PRISMA…), bases de datos, cadena de búsqueda, fechas, criterios de inclusión y exclusión y diagrama de flujo."],
        ["2.2. [Tema 1]", "Organiza por temas, no por artículos. Compara métodos, datos y resultados."],
        ["2.3. [Tema 2]", "Incluye una tabla comparativa de los trabajos más relevantes."],
        ["2.4. Síntesis y hueco de investigación", "Termina explicando qué falta en la literatura y cómo lo aborda tu trabajo. Es el puente hacia los objetivos."],
      ] },
      { t: "3. Objetivos", secs: [
        ["3.1. Objetivo principal", "Uno solo, en una frase, con un verbo comprobable (diseñar, desarrollar, evaluar, comparar, validar…)."],
        ["3.2. Objetivos secundarios", "Entre 2 y 4 (OS1, OS2, OS3…). Cada uno corresponderá a un paso del método y a un resultado."],
      ] },
      { t: "4. Materiales y métodos", secs: [
        ["4.1. Materiales", "Con qué lo has hecho: datos y su origen, participantes, software y hardware (con versiones), instrumentos."],
        ["4.2. Métodos", "Qué pasos has dado y basándote en qué metodología. Empieza con un diagrama del proceso completo."],
        ["4.2.1. Paso 1 (OS1)", "Detalle suficiente para que otra persona pueda repetirlo."],
        ["4.2.2. Paso 2 (OS2)", ""],
        ["4.2.3. Paso 3 (OS3)", ""],
        ["4.3. Evaluación", "Métricas, método de referencia (baseline) y pruebas estadísticas."],
      ] },
      { t: "5. Resultados", secs: [
        ["5.1. Resultado del paso 1", "Un apartado por paso del método, en el mismo orden. Solo hechos: cifras, tablas y figuras, sin interpretar."],
        ["5.2. Resultado del paso 2", "Cada figura y tabla debe mencionarse en el texto."],
        ["5.3. Resultado del paso 3", ""],
      ] },
      { t: "6. Discusión", secs: [
        ["6.1. Interpretación de los resultados", "¿Qué significan tus resultados?"],
        ["6.2. Comparación con el estado del arte", "¿Coinciden con lo publicado o lo contradicen? ¿Por qué? Vuelve a citar los trabajos relacionados."],
        ["6.3. Limitaciones", "Qué no se puede afirmar con tus datos o tu diseño."],
        ["6.4. Implicaciones", "Para quién es útil y en qué contexto."],
      ] },
      { t: "7. Conclusiones", secs: [
        ["7.1. Conclusiones", "Una por objetivo: si se ha cumplido y cómo. Sin datos nuevos ni citas."],
        ["7.2. Líneas futuras", "Qué harías con más tiempo o recursos."],
      ] },
    ],
    ia: "Declaración de uso de IA generativa",
    iaGuia: "Si la has usado: qué herramienta y versión, para qué, en qué partes y cómo verificaste el resultado. Si no la has usado, indícalo o elimina este apartado según tu normativa.",
    referencias: "Referencias",
    referenciasGuia: "Generadas con un gestor de referencias (Zotero o Mendeley), en un único estilo (IEEE, Vancouver, APA…). No las escribas a mano.",
    anexos: "Anexos",
    anexosGuia: ["Anexo A. [Por ejemplo, la lista de comprobación de la guía de publicación seguida, indicando dónde se cumple cada punto]",
      "Anexo B. [Código, cuestionarios o tablas extensas]"],
    // Ficha
    fichaTitulo: "Ficha de propuesta de trabajo fin de titulación",
    fichaIntro: "Rellénala antes de la primera tutoría. Si no puedes completar algún apartado, es una señal de que el objetivo aún no está acotado.",
    campos: ["Nombre y apellidos", "Titulación", "Tipo de trabajo (TFG / TFM / TFE)", "Fecha"],
    problema: "1. El problema",
    problemaGuia: "En una o dos frases: ¿qué problema quieres abordar? Parte de un problema, no de una herramienta.",
    objPrincipal: "2. Objetivo principal",
    objPrincipalGuia: "Uno solo, en una frase, con un verbo comprobable.",
    objSec: "3. Objetivos secundarios, pasos y resultados",
    objSecGuia: "Entre 2 y 4. Cada uno debe tener un paso en el método y un resultado.",
    colsSec: ["Objetivo secundario", "Paso del método", "Resultado esperado"],
    datosHerr: "4. Datos y herramientas",
    datosHerrGuia: "¿Qué datos usarás y de dónde salen? ¿Ya tienes acceso? ¿Qué herramientas necesitas y las sabes usar?",
    viabilidad: "5. Test de viabilidad",
    colsViab: ["Pregunta", "Tu respuesta"],
    preguntas: ["Tiempo: ¿cabe en las horas que tengo (25–30 h por crédito ECTS)?",
      "Datos: ¿los tengo o tendré acceso a tiempo? ¿Necesito comité de ética?",
      "Herramientas: ¿las sé usar o cuánto tardaré en aprender?",
      "Evaluación: ¿cómo sabré al final si lo he conseguido?",
      "Plan B: si falla lo principal, ¿qué parte se sostiene sola?"],
    refsIni: "6. Referencias iniciales",
    refsIniGuia: "Entre 3 y 5 referencias relevantes encontradas en bases de datos académicas, con DOI si lo tienen.",
  },
  en: {
    archivoMemoria: "thesis-template-en.docx",
    archivoFicha: "project-proposal-en.docx",
    pagina: "",
    portada: ["[University]", "[School or Faculty]", "[Degree programme]"],
    tipo: "[Bachelor's / Master's] Final Project",
    titulo: "[Project title: specific and descriptive]",
    datos: ["Author: [Full name]", "Supervisor: [Full name]", "[Month and year]"],
    notaPortada: "Adapt this cover page to your university's official template.",
    resumen: "Abstract",
    resumenGuia: ["Write it last. 250–300 words, or whatever your regulations specify.",
      "Structure: background (1–2 sentences), objective, methods, main results with figures, and conclusion."],
    palabrasClave: "Keywords: [4–6 keywords separated by commas]",
    abstract: "Resumen",
    abstractGuia: "Abstract in the other language required by your university (for example Spanish), if any. Delete this section otherwise.",
    keywords: "Palabras clave: [4–6]",
    indice: "Table of contents",
    indiceGuia: "If the table of contents looks empty, right-click it and choose \"Update Field\".",
    acronimos: "List of acronyms",
    acronimosGuia: "In alphabetical order. Example: ECG — Electrocardiogram.",
    capitulos: [
      { t: "1. Introduction", secs: [
        ["1.1. Background", "From the general topic to the specific problem. Support every claim with data and citations."],
        ["1.2. Problem and motivation", "Which problem are you tackling and why is it worth solving?"],
        ["1.3. Document structure", "A short paragraph explaining what each chapter contains. Write the introduction last."],
      ] },
      { t: "2. Related work", secs: [
        ["2.1. Search methodology", "Type of review and framework followed (JBI, PRISMA…), databases, search string, dates, inclusion and exclusion criteria and flow diagram."],
        ["2.2. [Theme 1]", "Organise by themes, not by papers. Compare methods, data and results."],
        ["2.3. [Theme 2]", "Include a comparison table of the most relevant studies."],
        ["2.4. Synthesis and research gap", "End by explaining what is missing from the literature and how your project addresses it. This is the bridge to your objectives."],
      ] },
      { t: "3. Objectives", secs: [
        ["3.1. Main objective", "Only one, in one sentence, with a verb you can check (design, develop, evaluate, compare, validate…)."],
        ["3.2. Secondary objectives", "Between 2 and 4 (SO1, SO2, SO3…). Each will match one method step and one result."],
      ] },
      { t: "4. Materials and methods", secs: [
        ["4.1. Materials", "What you used: data and its source, participants, software and hardware (with versions), instruments."],
        ["4.2. Methods", "Which steps you took and based on which methodology. Start with a diagram of the whole process."],
        ["4.2.1. Step 1 (SO1)", "Enough detail for someone else to repeat it."],
        ["4.2.2. Step 2 (SO2)", ""],
        ["4.2.3. Step 3 (SO3)", ""],
        ["4.3. Evaluation", "Metrics, baseline and statistical tests."],
      ] },
      { t: "5. Results", secs: [
        ["5.1. Result of step 1", "One section per method step, in the same order. Facts only: figures, tables and charts, no interpretation."],
        ["5.2. Result of step 2", "Every figure and table must be mentioned in the text."],
        ["5.3. Result of step 3", ""],
      ] },
      { t: "6. Discussion", secs: [
        ["6.1. Interpreting the results", "What do your results mean?"],
        ["6.2. Comparison with the state of the art", "Do they agree with published work or contradict it? Why? Cite the related work again."],
        ["6.3. Limitations", "What can't be claimed with your data or design."],
        ["6.4. Implications", "Who it is useful for and in what context."],
      ] },
      { t: "7. Conclusions", secs: [
        ["7.1. Conclusions", "One per objective: whether and how it was met. No new data and no citations."],
        ["7.2. Future work", "What you would do with more time or resources."],
      ] },
    ],
    ia: "Declaration of generative AI use",
    iaGuia: "If you used it: which tool and version, what for, in which parts, and how you verified the output. If you didn't, say so or delete this section, as your regulations require.",
    referencias: "References",
    referenciasGuia: "Generated with a reference manager (Zotero or Mendeley), in a single style (IEEE, Vancouver, APA…). Never type them by hand.",
    anexos: "Appendices",
    anexosGuia: ["Appendix A. [For example, the checklist of the reporting guideline you followed, showing where each item is addressed]",
      "Appendix B. [Code, questionnaires or long tables]"],
    fichaTitulo: "Final project proposal form",
    fichaIntro: "Fill it in before our first meeting. If you can't complete a section, that's a sign your objective isn't focused enough yet.",
    campos: ["Full name", "Degree programme", "Type of project (bachelor's / master's / other)", "Date"],
    problema: "1. The problem",
    problemaGuia: "In one or two sentences: which problem do you want to tackle? Start from a problem, not a tool.",
    objPrincipal: "2. Main objective",
    objPrincipalGuia: "Only one, in one sentence, with a verb you can check.",
    objSec: "3. Secondary objectives, steps and results",
    objSecGuia: "Between 2 and 4. Each must have a method step and a result.",
    colsSec: ["Secondary objective", "Method step", "Expected result"],
    datosHerr: "4. Data and tools",
    datosHerrGuia: "Which data will you use and where does it come from? Do you already have access? Which tools do you need, and can you use them?",
    viabilidad: "5. Feasibility test",
    colsViab: ["Question", "Your answer"],
    preguntas: ["Time: does it fit the hours I have (25–30 h per ECTS credit)?",
      "Data: do I have it, or will I get access in time? Do I need ethics approval?",
      "Tools: can I use them, or how long will it take to learn?",
      "Evaluation: how will I know at the end whether I succeeded?",
      "Plan B: if the main part fails, which part still stands on its own?"],
    refsIni: "6. Initial references",
    refsIniGuia: "3–5 relevant references found in academic databases, with DOI where available.",
  },
};

// ---------- Memoria ----------
function memoria(L) {
  const hijos = [];
  // Portada
  hijos.push(new Paragraph({ spacing: { before: 1200 }, children: [] }));
  L.portada.forEach((t) => hijos.push(centrado(t, { size: 26, bold: true, after: 60 })));
  hijos.push(new Paragraph({ spacing: { before: 1400 }, children: [] }));
  hijos.push(centrado(L.tipo, { size: 28, color: INDIGO, after: 240 }));
  hijos.push(new Paragraph({ style: "Title", children: [new TextRun(L.titulo)] }));
  hijos.push(new Paragraph({ spacing: { before: 2000 }, children: [] }));
  L.datos.forEach((t) => hijos.push(centrado(t, { size: 24, after: 80 })));
  hijos.push(new Paragraph({ spacing: { before: 600 }, children: [] }));
  hijos.push(centrado(L.notaPortada, { size: 20, gris: true }));

  // Resumen / abstract
  hijos.push(h1(L.resumen));
  L.resumenGuia.forEach((t) => hijos.push(guia(t)));
  hijos.push(new Paragraph({ spacing: { before: 240 }, children: [new TextRun({ text: L.palabrasClave, bold: true })] }));
  hijos.push(h1(L.abstract));
  hijos.push(guia(L.abstractGuia));
  hijos.push(new Paragraph({ spacing: { before: 240 }, children: [new TextRun({ text: L.keywords, bold: true })] }));

  // Índice
  hijos.push(new Paragraph({ pageBreakBefore: true, spacing: { after: 200 },
    children: [new TextRun({ text: L.indice, bold: true, size: 32, color: INDIGO })] }));
  hijos.push(new TableOfContents(L.indice, { hyperlink: true, headingStyleRange: "1-3" }));
  hijos.push(guia(L.indiceGuia));

  // Acrónimos
  hijos.push(h1(L.acronimos));
  hijos.push(guia(L.acronimosGuia));

  // Capítulos
  L.capitulos.forEach((cap) => {
    hijos.push(h1(cap.t));
    cap.secs.forEach(([titulo, texto]) => {
      const nivel = titulo.split(" ")[0].split(".").filter(Boolean).length;
      hijos.push(new Paragraph({ heading: nivel >= 3 ? HeadingLevel.HEADING_3 : HeadingLevel.HEADING_2, children: [new TextRun(titulo)] }));
      if (texto) hijos.push(guia(texto));
    });
  });

  hijos.push(h1(L.ia));
  hijos.push(guia(L.iaGuia));
  hijos.push(h1(L.referencias));
  hijos.push(guia(L.referenciasGuia));
  hijos.push(h1(L.anexos));
  L.anexosGuia.forEach((t) => hijos.push(guia(t)));

  return new Document({
    creator: "Beatriz Merino-Barbancho",
    title: L.tipo,
    styles: estilos,
    numbering: numeracion,
    features: { updateFields: true },
    sections: [{ properties: pagina, footers: pie(L.pagina), children: hijos }],
  });
}

// ---------- Ficha ----------
const borde = { style: BorderStyle.SINGLE, size: 4, color: "C9D7E6" };
const bordes = { top: borde, bottom: borde, left: borde, right: borde };

function celda(texto, ancho, { cabecera = false, alto = false } = {}) {
  return new TableCell({
    width: { size: ancho, type: WidthType.DXA },
    borders: bordes,
    shading: cabecera ? { fill: HIELO, type: ShadingType.CLEAR, color: "auto" } : undefined,
    margins: { top: 80, bottom: 80, left: 120, right: 120 },
    children: [new Paragraph({ spacing: { after: alto ? 480 : 0 },
      children: [new TextRun({ text: texto, bold: cabecera, color: cabecera ? INDIGO : undefined, size: 22 })] })],
  });
}

function tabla(anchos, filas) {
  return new Table({
    width: { size: anchos.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: anchos,
    rows: filas.map((f) => new TableRow({ children: f })),
  });
}

function caja(lineas = 3) {
  return tabla([CONTENT_W], [[new TableCell({
    width: { size: CONTENT_W, type: WidthType.DXA }, borders: bordes,
    margins: { top: 80, bottom: 80, left: 120, right: 120 },
    children: Array.from({ length: lineas }, () => new Paragraph({ children: [] })),
  })]]);
}

function ficha(L) {
  const h = [];
  h.push(new Paragraph({ style: "Title", children: [new TextRun(L.fichaTitulo)] }));
  h.push(guia(L.fichaIntro));
  h.push(new Paragraph({ children: [] }));
  h.push(tabla([3200, CONTENT_W - 3200], L.campos.map((c) => [celda(c, 3200, { cabecera: true }), celda("", CONTENT_W - 3200)])));

  h.push(h1(L.problema, false)); h.push(guia(L.problemaGuia)); h.push(caja(3));
  h.push(h1(L.objPrincipal, false)); h.push(guia(L.objPrincipalGuia)); h.push(caja(2));

  h.push(h1(L.objSec, false)); h.push(guia(L.objSecGuia));
  const a3 = [3024, 3024, 3024];
  const filasSec = [L.colsSec.map((c, i) => celda(c, a3[i], { cabecera: true }))];
  ["1", "2", "3", "4"].forEach((n) => filasSec.push([celda(`${L.colsSec[0].startsWith("Sec") ? "SO" : "OS"}${n}.`, a3[0], { alto: true }), celda("", a3[1]), celda("", a3[2])]));
  h.push(tabla(a3, filasSec));

  h.push(h1(L.datosHerr, false)); h.push(guia(L.datosHerrGuia)); h.push(caja(4));

  h.push(h1(L.viabilidad, false));
  const a2 = [4200, CONTENT_W - 4200];
  const filasV = [L.colsViab.map((c, i) => celda(c, a2[i], { cabecera: true }))];
  L.preguntas.forEach((p) => filasV.push([celda(p, a2[0], { alto: true }), celda("", a2[1])]));
  h.push(tabla(a2, filasV));

  h.push(h1(L.refsIni, false)); h.push(guia(L.refsIniGuia));
  h.push(caja(5));

  return new Document({
    creator: "Beatriz Merino-Barbancho",
    title: L.fichaTitulo,
    styles: estilos,
    numbering: numeracion,
    sections: [{ properties: pagina, children: h }],
  });
}

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  for (const L of Object.values(T)) {
    fs.writeFileSync(path.join(OUT, L.archivoMemoria), await Packer.toBuffer(memoria(L)));
    fs.writeFileSync(path.join(OUT, L.archivoFicha), await Packer.toBuffer(ficha(L)));
  }
  console.log("Plantillas Word generadas en", OUT);
})();
