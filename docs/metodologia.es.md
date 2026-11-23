# Metodología y desarrollo

La metodología es lo que convierte «he hecho cosas» en «he seguido un método que otra persona podría repetir». En la memoria se cuenta en el capítulo de **Materiales y métodos**, y conviene entender bien la diferencia entre las dos partes.

## Materiales y métodos: qué va en cada parte

<div class="grid" markdown>

<div class="card" markdown>
**Materiales** = *con qué* lo has hecho

Las herramientas: datos y su origen, participantes, *hardware*, *software*, lenguajes y librerías (con versiones), instrumentos de medida, cuestionarios…
</div>

<div class="card" markdown>
**Métodos** = *qué pasos* has dado y *basándote en qué* metodología

Los pasos en orden, justificados con una metodología reconocida, con el detalle suficiente para que otra persona pueda repetirlos.
</div>

</div>

!!! clave "Un paso del método por cada objetivo secundario"
    Si tienes tres objetivos secundarios, tu método debería tener (al menos) tres pasos claros, y cada uno producirá **un resultado**. Así la memoria se ordena sola: lo verás en [Estructura de la memoria](estructura.md#el-hilo-conductor).

## Apóyate en una metodología reconocida

No inventes el proceso: elige un marco y dilo explícitamente («siguiendo la metodología X [ref]»). Algunos ejemplos según el tipo de trabajo:

| Tipo de trabajo | Metodologías o marcos habituales |
|---|---|
| Revisión de literatura | JBI, PRISMA 2020, PRISMA-ScR (ver [Estado del arte](estado-del-arte.md)) |
| Análisis de datos / aprendizaje automático | CRISP-DM; validación con conjuntos de entrenamiento, validación y prueba o validación cruzada |
| Desarrollo de software | Ciclo de vida en cascada, metodologías ágiles (Scrum, Kanban), con requisitos, diseño, implementación y pruebas |
| Diseño de producto o app con usuarios | Diseño centrado en el usuario (ISO 9241-210), *Design Thinking*, evaluación de usabilidad (por ejemplo, con el cuestionario SUS) |
| Creación de un artefacto en ingeniería | *Design Science Research* |
| Estudio con personas | Diseño de estudio (observacional, experimental, cualitativo) + la guía de publicación correspondiente (ver abajo) |

## Guías de publicación

Las **guías de publicación** (*reporting guidelines*) son listas de comprobación que dicen **qué información debe aparecer** en un trabajo según su tipo. Están reunidas en la [Red EQUATOR](https://www.equator-network.org/). Aunque pensadas para artículos, son la mejor forma de asegurarte de que tus métodos y resultados están completos. **Si tu trabajo encaja en una, úsala y cítala.**

Las más relevantes para trabajos de salud digital e IA:

| Tipo de estudio | Guía | Extensión para IA |
|---|---|---|
| Protocolo de ensayo clínico | SPIRIT | **SPIRIT-AI** |
| Resultados de ensayo clínico | CONSORT | **CONSORT-AI** |
| Modelo de predicción (diagnóstico o pronóstico) | TRIPOD | **TRIPOD+AI** |
| Evaluación clínica temprana de un sistema de IA de apoyo a la decisión | — | **DECIDE-AI** |
| IA en imagen médica | — | **CLAIM** |
| Precisión de una prueba diagnóstica | STARD | — |
| Estudio observacional | STROBE | — |
| Investigación cualitativa (entrevistas, grupos focales) | COREQ, SRQR | — |
| Revisión sistemática / de alcance | PRISMA 2020 / PRISMA-ScR | — |

Busca siempre en EQUATOR la versión más reciente: estas guías se actualizan y aparecen extensiones nuevas.

!!! tip "Cómo usar la guía en tu trabajo"
    Descarga la lista de comprobación, recórrela punto por punto y, al final, inclúyela como **anexo** indicando en qué página o sección de tu memoria se cumple cada punto. Pocas cosas dan tanta impresión de rigor.

## Buenas prácticas en el desarrollo

### Datos

- Describe el **origen** de los datos, cómo se obtuvieron, cuántos hay y sus características principales.
- Si son **datos de personas**, y sobre todo de salud, cumple el RGPD: anonimiza o seudonimiza y consulta si necesitas la aprobación de un **comité de ética**. Pídela con tiempo, porque tarda.
- **Nunca** subas datos personales o clínicos a herramientas en línea (tampoco a herramientas de [IA generativa](ia.md)).

### Validación y evaluación

- Define **antes** de empezar con qué **métricas** vas a evaluar y por qué son las adecuadas para tu problema.
- Compara con algo: un **método de referencia** (*baseline*), el estado del arte o una alternativa sencilla. Un 90 % de exactitud no significa nada si el método más simple consigue un 89 %.
- En aprendizaje automático, separa bien entrenamiento y prueba y **evita la fuga de datos** (*data leakage*): por ejemplo, que registros del mismo paciente acaben en los dos conjuntos.
- Si comparas resultados, usa la **prueba estadística** adecuada y aporta intervalos de confianza cuando sea posible.

### Reproducibilidad

- Usa **control de versiones** (Git) para el código.
- Anota **versiones** de librerías y herramientas, semillas aleatorias y parámetros.
- Si puedes, publica el código en un repositorio (GitHub, Zenodo) y enlázalo en la memoria.

## Cómo escribir los métodos

- En **pasado** y de forma impersonal o en primera persona del plural, pero siempre igual.
- **En el orden** en que se hizo, con un apartado por paso.
- Con **el detalle suficiente para que otra persona lo repita**: ni un diario de todo lo que probaste, ni un «se entrenó un modelo».
- Lo que **no** va aquí: los resultados. Si escribes «y se obtuvo un 92 %», eso pertenece al capítulo de resultados.
- Un **diagrama** del proceso completo al principio del capítulo ayuda muchísimo.
