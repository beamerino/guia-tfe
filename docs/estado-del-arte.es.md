# Estado del arte y revisión de literatura

Es la parte que peor se suele hacer, y la que más se nota. Un buen estado del arte no es una lista de artículos resumidos uno detrás de otro. Es una **búsqueda hecha con método** que te permite decir qué se sabe, qué falta y **por qué tu trabajo tiene sentido**.

!!! error-tipico "Lo que veo casi siempre"
    - Buscar en Google (el buscador general) en lugar de en bases de datos académicas.
    - No saber qué tipo de revisión se está haciendo: sistemática, de alcance o narrativa.
    - No conocer los marcos de referencia (JBI, PRISMA) ni las guías de publicación.
    - No documentar la búsqueda, de modo que nadie (ni tú) podría repetirla.

## Tipos de revisión

| Tipo | Para qué sirve | Pregunta | Rasgos principales | Guía de publicación |
|---|---|---|---|---|
| **Narrativa** | Dar contexto general sobre un tema | Amplia y abierta | Sin protocolo formal; selección a criterio del autor | (no tiene) |
| **De alcance** (*scoping review*) | Mapear qué evidencia existe, cómo se ha estudiado algo y dónde están los huecos | Amplia, con el esquema **PCC** (Población, Concepto, Contexto) | Búsqueda sistemática y reproducible; normalmente **sin** evaluar la calidad de los estudios | **PRISMA-ScR** |
| **Sistemática** (*systematic review*) | Responder a una pregunta concreta con toda la evidencia disponible | Concreta, con el esquema **PICO** (Paciente/Población, Intervención, Comparación, Resultado) | Protocolo previo, búsqueda exhaustiva en varias bases, criterios explícitos, **evaluación de calidad o riesgo de sesgo**; puede incluir metaanálisis | **PRISMA 2020** |
| **Rápida** (*rapid review*) | Sistemática simplificada cuando hay poco tiempo | Concreta | Se acortan pasos de forma explícita | (varía) |
| **Paraguas** (*umbrella review*) | Sintetizar revisiones ya publicadas | Concreta | Las unidades de análisis son revisiones | (varía) |

!!! clave "¿Cuál me toca a mí?"
    - Si tu trabajo **es** una revisión, lo más habitual y viable en un TFG o TFM es una **revisión de alcance** siguiendo la metodología **JBI** y publicada según **PRISMA-ScR**.
    - Si tu trabajo es de desarrollo o experimental, tu capítulo de trabajos relacionados no tiene por qué ser una revisión sistemática completa. Pero la búsqueda **sí debe ser estructurada y estar documentada**: bases, cadena de búsqueda, fechas y criterios.
    - Una revisión sistemática formal exige, entre otras cosas, **dos revisores independientes**. Si la haces sola o solo, dilo como limitación.

## Marcos de referencia

Un **marco metodológico** te dice *cómo hacer* la revisión. Una **guía de publicación** te dice *qué tienes que contar* al escribirla. Son cosas distintas y normalmente se usan las dos.

- **JBI Manual for Evidence Synthesis** (Joanna Briggs Institute): metodología paso a paso para revisiones sistemáticas, de alcance y otros tipos. Es la referencia más usada para *scoping reviews*.
- **Arksey y O'Malley (2005)**, ampliado por **Levac y colaboradores (2010)**: el marco clásico de cinco etapas para revisiones de alcance.
- **Cochrane Handbook**: la referencia para revisiones sistemáticas de intervenciones en salud.
- **PRISMA 2020**: lista de comprobación y diagrama de flujo para publicar revisiones sistemáticas.
- **PRISMA-ScR**: la extensión de PRISMA para revisiones de alcance.

Todas estas guías, y muchas más, están reunidas en la [Red EQUATOR](https://www.equator-network.org/), que también usarás para tu [metodología](metodologia.md#guias-de-publicacion).

Si tu trabajo es de salud, puedes **registrar el protocolo** antes de empezar: [PROSPERO](https://www.crd.york.ac.uk/prospero/) para revisiones sistemáticas u [OSF](https://osf.io/) para revisiones de alcance. No es obligatorio en un TFE, pero suma mucho.

## Dónde buscar

| Buscador | Área | Acceso | Notas |
|---|---|---|---|
| [Web of Science](https://www.webofscience.com/) | Multidisciplinar | Institucional | Muy usado para revisiones y análisis bibliométricos |
| [Scopus](https://www.scopus.com/) | Multidisciplinar | Institucional | Gran cobertura en ingeniería y salud |
| [PubMed](https://pubmed.ncbi.nlm.nih.gov/) | Salud y biomedicina | Gratuito | Usa términos **MeSH** para búsquedas precisas |
| [Google Scholar](https://scholar.google.com/) | Todo | Gratuito | Útil para empezar y para encontrar textos completos, pero **no es reproducible**: no lo uses como única fuente de una revisión |
| [IEEE Xplore](https://ieeexplore.ieee.org/) | Ingeniería, electrónica, informática | Institucional | Imprescindible en ingeniería |
| [ACM Digital Library](https://dl.acm.org/) | Informática | Institucional | |
| [Embase](https://www.embase.com/) | Biomedicina y farmacología | Institucional | Complementa a PubMed en revisiones sistemáticas |
| [Cochrane Library](https://www.cochranelibrary.com/) | Salud | Según país o institución | Revisiones sistemáticas de referencia |
| [arXiv](https://arxiv.org/) / [medRxiv](https://www.medrxiv.org/) | Preprints | Gratuito | **No revisados por pares**: úsalos con cuidado y dilo |

El acceso «institucional» lo tienes con tu cuenta de la universidad a través de la biblioteca (VPN o acceso remoto). Pregunta en tu biblioteca: suelen dar formación gratuita sobre estas bases.

**Para una revisión, usa al menos dos o tres bases**: por ejemplo, PubMed + Scopus + Web of Science en salud, o IEEE Xplore + Scopus + ACM en ingeniería.

## Cómo construir la búsqueda

### 1. Descompón tu pregunta

Usa **PICO** (revisión sistemática) o **PCC** (revisión de alcance). Por ejemplo, para una revisión de alcance sobre IA para detectar fibrilación auricular:

| Elemento | Concepto | Sinónimos y términos |
|---|---|---|
| Población | Personas con fibrilación auricular | *atrial fibrillation*, AF, AFib |
| Concepto | Inteligencia artificial | *artificial intelligence*, *machine learning*, *deep learning*, *neural network* |
| Contexto | Electrocardiograma | *electrocardiogram*, ECG, EKG, *wearable* |

### 2. Combina con operadores booleanos

- **OR** dentro de cada concepto (sinónimos), **AND** entre conceptos.
- **Comillas** para frases exactas: `"machine learning"`.
- **Asterisco** para truncar: `predict*` encuentra *predict, prediction, predictive…*
- Restringe a título, resumen y palabras clave para evitar ruido.

```text
("artificial intelligence" OR "machine learning" OR "deep learning" OR "neural network*")
AND ("atrial fibrillation" OR AFib)
AND (electrocardiogram* OR ECG OR EKG OR wearable*)
```

Cada base tiene su sintaxis para buscar en campos concretos, por ejemplo `TITLE-ABS-KEY(...)` en Scopus, `TS=(...)` en Web of Science o `[tiab]` y `[MeSH Terms]` en PubMed. Adapta la cadena a cada una y **guarda la versión exacta que usaste**.

### 3. Documenta todo

Anota en una tabla, para cada base: **fecha de búsqueda, cadena exacta, filtros (años, idioma, tipo de documento) y número de resultados**. Tiene que poder repetirlo otra persona. En [Plantillas](plantillas.md) tienes una tabla para esto.

### 4. Criba

1. Exporta los resultados a tu [gestor de referencias](bibliografia.md) y **elimina duplicados**.
2. **Cribado por título y resumen** aplicando tus criterios de inclusión y exclusión, definidos **antes** de empezar.
3. **Lectura a texto completo** de los que pasan el primer filtro, anotando el motivo de cada exclusión.
4. Herramientas como [Rayyan](https://www.rayyan.ai/) (gratuita) facilitan mucho el cribado.
5. Resume el proceso en un **diagrama de flujo PRISMA**: registros identificados → cribados → excluidos (con motivos) → incluidos.

### 5. Extrae y sintetiza

Para cada estudio incluido, rellena una **tabla de extracción**: autores y año, país, objetivo, datos o población, método, resultados principales y limitaciones. A partir de esa tabla:

- **Agrupa por temas**, no por artículos.
- **Compara**: ¿qué métodos se usan más? ¿Qué resultados obtienen? ¿Con qué datos?
- **Identifica el hueco**: lo que no se ha hecho, se ha hecho mal o no se ha hecho en tu contexto.

Si es una revisión sistemática, evalúa además la **calidad o el riesgo de sesgo** de cada estudio con una herramienta adecuada (por ejemplo, las listas de evaluación crítica de JBI, RoB 2 para ensayos o PROBAST para modelos de predicción).

## Cómo escribir los trabajos relacionados

!!! clave "El capítulo debe acabar justificando tu objetivo"
    La última sección de los trabajos relacionados debería decir, en un párrafo: *«Por tanto, no existe X / X no se ha evaluado en Y / los trabajos previos tienen la limitación Z. Este trabajo aborda…»*. Ese es el puente hacia tus [objetivos](estructura.md#objetivos).

- **Mal:** «García et al. (2021) hicieron X. López et al. (2022) hicieron Y. Smith et al. (2023) hicieron Z…».
- **Bien** (ejemplo inventado): «Los enfoques basados en redes convolucionales dominan la literatura reciente [3–8], con sensibilidades entre el 85 % y el 97 %. Sin embargo, la mayoría se han evaluado en registros hospitalarios de 12 derivaciones [3, 5, 6] y pocos en dispositivos de una derivación [7]…».
- Incluye una **tabla comparativa** de los trabajos más relevantes (método, datos, resultado, limitación). Se lee mucho mejor que diez párrafos.
