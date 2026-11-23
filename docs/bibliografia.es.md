# Bibliografía: cómo citar y gestores de referencias

Escribir las referencias a mano es la forma más segura de equivocarte: números que no cuadran, formatos mezclados o citas que desaparecen al mover un párrafo. Un **gestor de referencias** lo hace por ti, y **se instala el primer día**, no la semana de la entrega.

!!! error-tipico "Lo que veo casi siempre"
    - Referencias copiadas a mano, cada una con un formato distinto.
    - Citas en el texto que no aparecen en la lista final, o al revés.
    - Referencias a páginas web genéricas, Wikipedia o blogs en lugar de a la fuente original.
    - Instalar el gestor al final e intentar reconstruir de dónde salía cada cosa.

## Qué gestor usar

| | Zotero | Mendeley |
|---|---|---|
| Precio | Gratuito y de código abierto | Gratuito (de Elsevier) |
| Captura desde el navegador | Zotero Connector | Mendeley Web Importer |
| Integración con Word | Complemento incluido | Mendeley Cite |
| Integración con LaTeX | Exporta `.bib` (mejor con el complemento Better BibTeX) | Exporta `.bib` |
| Google Docs | Sí | No |
| Mi recomendación | **Sí**: es el que recomiendo por defecto | Si tu grupo o tu universidad ya lo usan |

Los dos sirven. Lo importante es **usar uno desde el principio**.

## Zotero en 10 minutos

1. **Instala** [Zotero](https://www.zotero.org/download/) y el **Zotero Connector** para tu navegador.
2. **Crea una cuenta** y activa la sincronización: tendrás tu biblioteca en cualquier ordenador.
3. **Crea una colección** para tu TFE (y subcolecciones por tema si quieres).
4. **Guarda referencias** desde el navegador: en la página del artículo (PubMed, Scopus, IEEE Xplore, la revista…), pulsa el icono del Connector. Zotero guarda los metadatos y, si puede, el PDF.
5. **Añade por identificador**: con el botón de la varita mágica puedes pegar un **DOI**, un PMID o un ISBN.
6. **Revisa los metadatos**: autores, año, revista, volumen y páginas. El Connector a veces falla, sobre todo con páginas web y preprints.
7. **Cita en Word**: en la pestaña Zotero, *Add/Edit Citation* para insertar una cita y *Add/Edit Bibliography* para la lista final. En *Document Preferences* eliges el estilo.
8. **Cita en LaTeX**: instala el complemento [Better BibTeX](https://retorque.re/zotero-better-bibtex/), exporta la colección como `.bib` con la opción de mantener actualizado y cita con `\cite{clave}`.
9. **Importa los resultados de tu búsqueda**: Web of Science, Scopus y PubMed exportan en formato RIS o similar, que Zotero importa directamente. Después, usa *Duplicate Items* para eliminar duplicados.

!!! tip "Mendeley"
    El flujo es el mismo: instala [Mendeley Reference Manager](https://www.mendeley.com/), el Web Importer y el complemento **Mendeley Cite** para Word.

## Qué estilo de cita usar

Usa el que indique tu universidad o titulación. Si no indica ninguno:

| Estilo | Forma | Habitual en |
|---|---|---|
| **IEEE** | Numérico entre corchetes: [1] | Ingeniería e informática |
| **Vancouver** | Numérico: (1) o superíndice | Ciencias de la salud |
| **APA 7** | Autor-año: (García, 2023) | Ciencias sociales, psicología, educación |

Elige uno y **no lo mezcles**. Con un gestor, cambiar de estilo es un clic.

## Buenas prácticas al citar

- **Cita la fuente original.** Si lees en un artículo que «según X…», busca y lee X.
- **Toda afirmación que no sea tuya ni de conocimiento común lleva cita**: datos, cifras, definiciones, métodos ajenos.
- **Parafrasea y cita.** Copiar frases sin comillas, aunque cites, es plagio. Las citas textuales van entre comillas y deberían ser excepcionales.
- **Prioriza artículos revisados por pares**, recientes (últimos 5–10 años salvo trabajos clásicos) y de revistas o congresos reconocidos.
- **Cita también los datos y el software** que uses: conjuntos de datos (con su DOI si lo tienen), librerías y herramientas principales.
- **Comprueba cada referencia.** Que exista, que diga lo que dices que dice y que los datos estén completos. Esto es aún más importante si has usado [IA generativa](ia.md): las herramientas de IA **inventan referencias** con total convicción.
