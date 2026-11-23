# Cómo hacer un buen trabajo fin de titulación

Guía práctica para estudiantes de TFG, TFM, TFT y TFE, por **Beatriz Merino-Barbancho**.

👉 **Léela aquí: https://beamerino.github.io/guia-tfe/** (español e inglés)

---

## Cómo editar la guía (para mí)

Cada página es un archivo de texto en Markdown dentro de `docs/`, con una versión por idioma:

| Página | Español | Inglés |
|---|---|---|
| Inicio | `docs/index.es.md` | `docs/index.en.md` |
| Elegir y acotar el tema | `docs/tema.es.md` | `docs/tema.en.md` |
| Planificación | `docs/planificacion.es.md` | `docs/planificacion.en.md` |
| Estado del arte | `docs/estado-del-arte.es.md` | `docs/estado-del-arte.en.md` |
| Bibliografía | `docs/bibliografia.es.md` | `docs/bibliografia.en.md` |
| Metodología | `docs/metodologia.es.md` | `docs/metodologia.en.md` |
| Estructura de la memoria | `docs/estructura.es.md` | `docs/estructura.en.md` |
| Redacción y estilo | `docs/redaccion.es.md` | `docs/redaccion.en.md` |
| IA generativa | `docs/ia.es.md` | `docs/ia.en.md` |
| Defensa | `docs/defensa.es.md` | `docs/defensa.en.md` |
| Plantillas | `docs/plantillas.es.md` | `docs/plantillas.en.md` |
| Checklist | `docs/checklist.es.md` | `docs/checklist.en.md` |

**Para cambiar algo:** abre el archivo en GitHub, pulsa el lápiz ✏️, edita y pulsa *Commit changes*. En uno o dos minutos la web se actualiza sola (lo verás en la pestaña *Actions*).

**Cajas especiales** que puedes usar en el texto:

```markdown
!!! clave "Título"
    Texto de la idea clave (con 4 espacios delante).

!!! error-tipico "Título"
    Texto del error típico.
```

**Checklist:** si añades o quitas casillas, hazlo en las dos versiones (ES y EN) y en el mismo orden, porque el progreso guardado se comparte entre idiomas.

**Colores de la marca:** en `docs/assets/stylesheets/marca.css`, al principio del archivo.

## Plantillas descargables

Las plantillas (Word, LaTeX y Excel) **se generan solas** cada vez que se publica la web, a partir de los scripts de `plantillas-fuente/`:

- `plantillas-fuente/word/generar.js`: memoria y ficha de propuesta en Word (ES y EN).
- `plantillas-fuente/latex/generar.py`: memoria en LaTeX, como .zip para Overleaf (ES y EN).
- `plantillas-fuente/excel/generar.py`: tabla de revisión de literatura (ES y EN).

**¿Quieres usar tu propia versión de una plantilla?** Sube tu archivo a la carpeta `docs/descargas/` con **el mismo nombre** (por ejemplo, `plantilla-memoria-es.docx`). Si existe, se usa el tuyo en lugar del generado.

## Ver la web en tu ordenador (opcional)

```bash
pip install -r requirements.txt
mkdocs serve
```

Y abre http://127.0.0.1:8000.

## Licencia

Contenido bajo licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es): puedes compartirlo y adaptarlo citando la autoría, sin fines comerciales y con la misma licencia. Ver [LICENSE.md](LICENSE.md).
