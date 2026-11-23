"""Genera la tabla de revisión de literatura (ES y EN).
Uso: python3 generar.py <carpeta_salida>
"""
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation

INDIGO = "2A2563"
HIELO = "EAF0F6"
AMARILLO = "FFF7D6"
F = "Arial"

T = {
    "es": {
        "archivo": "tabla-revision-literatura-es.xlsx",
        "hojas": ["Instrucciones", "Registro de búsquedas", "Extracción de estudios"],
        "instr_titulo": "Tabla de revisión de literatura",
        "instr": [
            "Hoja «Registro de búsquedas»: una fila por cada búsqueda en cada base de datos. Sirve para que la búsqueda sea reproducible y para el diagrama de flujo PRISMA.",
            "Hoja «Extracción de estudios»: una fila por cada estudio que llega a lectura a texto completo.",
            "Las celdas con fondo amarillo claro son las que debes rellenar. La primera fila de cada hoja es un ejemplo: bórrala cuando empieces.",
            "Las filas de totales se calculan solas.",
            "Guía completa: https://beamerino.github.io/guia-tfe/estado-del-arte/",
        ],
        "busq_cols": ["Base de datos", "Fecha de búsqueda", "Cadena de búsqueda exacta", "Campos (título, resumen…)", "Filtros (años, idioma, tipo)", "N.º de resultados", "Notas"],
        "busq_ej": ["EJEMPLO · Scopus", "2026-01-20", 'TITLE-ABS-KEY(("machine learning" OR "deep learning") AND "atrial fibrillation" AND (ECG OR electrocardiogram*))', "Título, resumen y palabras clave", "2020–2025; inglés y español; artículos y congresos", 0, "Borra esta fila"],
        "total": "Total de registros identificados",
        "ext_cols": ["ID", "Autores", "Año", "Título", "DOI", "País", "Objetivo", "Datos / población", "Método", "Resultados principales", "Limitaciones", "¿Incluido?", "Motivo de exclusión"],
        "ext_ej": ["E01", "EJEMPLO · Apellido et al.", 2024, "Título del estudio", "10.xxxx/xxxxx", "España", "Qué pretendía el estudio", "Conjunto de datos o participantes (n)", "Técnica o diseño", "Métrica principal y valor", "Lo que no permite afirmar", "Sí", ""],
        "si_no": '"Sí,No"',
        "incluidos": "Estudios incluidos",
        "excluidos": "Estudios excluidos",
        "si": "Sí", "no": "No",
    },
    "en": {
        "archivo": "literature-review-table-en.xlsx",
        "hojas": ["Instructions", "Search log", "Study extraction"],
        "instr_titulo": "Literature review table",
        "instr": [
            "'Search log' sheet: one row per search in each database. It makes your search reproducible and feeds the PRISMA flow diagram.",
            "'Study extraction' sheet: one row per study that reaches full-text reading.",
            "Cells with a light yellow background are the ones to fill in. The first row of each sheet is an example: delete it when you start.",
            "Total rows calculate themselves.",
            "Full guide: https://beamerino.github.io/guia-tfe/en/estado-del-arte/",
        ],
        "busq_cols": ["Database", "Search date", "Exact search string", "Fields (title, abstract…)", "Filters (years, language, type)", "No. of results", "Notes"],
        "busq_ej": ["EXAMPLE · Scopus", "2026-01-20", 'TITLE-ABS-KEY(("machine learning" OR "deep learning") AND "atrial fibrillation" AND (ECG OR electrocardiogram*))', "Title, abstract and keywords", "2020–2025; English and Spanish; articles and conference papers", 0, "Delete this row"],
        "total": "Total records identified",
        "ext_cols": ["ID", "Authors", "Year", "Title", "DOI", "Country", "Objective", "Data / population", "Method", "Main results", "Limitations", "Included?", "Reason for exclusion"],
        "ext_ej": ["S01", "EXAMPLE · Surname et al.", 2024, "Study title", "10.xxxx/xxxxx", "Spain", "What the study aimed to do", "Dataset or participants (n)", "Technique or design", "Main metric and value", "What it cannot claim", "Yes", ""],
        "si_no": '"Yes,No"',
        "incluidos": "Included studies",
        "excluidos": "Excluded studies",
        "si": "Yes", "no": "No",
    },
}

fino = Side(style="thin", color="C9D7E6")
borde = Border(left=fino, right=fino, top=fino, bottom=fino)
cab_font = Font(name=F, bold=True, color="FFFFFF")
cab_fill = PatternFill("solid", fgColor=INDIGO)
entrada = PatternFill("solid", fgColor=AMARILLO)
ejemplo_font = Font(name=F, italic=True, color="6B7280")
normal = Font(name=F)
FILAS = 60


def cabecera(ws, cols, anchos):
    for i, (c, a) in enumerate(zip(cols, anchos), start=1):
        cell = ws.cell(row=1, column=i, value=c)
        cell.font, cell.fill, cell.border = cab_font, cab_fill, borde
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        ws.column_dimensions[cell.column_letter].width = a
    ws.row_dimensions[1].height = 32
    ws.freeze_panes = "A2"


def zona_entrada(ws, ncols, desde, hasta):
    for r in range(desde, hasta + 1):
        for c in range(1, ncols + 1):
            cell = ws.cell(row=r, column=c)
            cell.fill, cell.border, cell.font = entrada, borde, normal
            cell.alignment = Alignment(wrap_text=True, vertical="top")


def libro(L):
    wb = Workbook()
    # Instrucciones
    ws = wb.active
    ws.title = L["hojas"][0]
    ws["A1"] = L["instr_titulo"]
    ws["A1"].font = Font(name=F, bold=True, size=14, color=INDIGO)
    for i, t in enumerate(L["instr"], start=3):
        c = ws.cell(row=i, column=1, value=t)
        c.font = normal
        c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[i].height = 32
    ws["A5"].fill = entrada
    ws.column_dimensions["A"].width = 110

    # Registro de búsquedas
    ws = wb.create_sheet(L["hojas"][1])
    cols = L["busq_cols"]
    cabecera(ws, cols, [20, 14, 60, 22, 28, 14, 24])
    zona_entrada(ws, len(cols), 2, FILAS + 1)
    for c, v in enumerate(L["busq_ej"], start=1):
        cell = ws.cell(row=2, column=c, value=v)
        cell.font = ejemplo_font
    for r in range(2, FILAS + 2):
        ws.cell(row=r, column=6).number_format = "0"
    tot = FILAS + 3
    ws.cell(row=tot, column=5, value=L["total"]).font = Font(name=F, bold=True, color=INDIGO)
    t = ws.cell(row=tot, column=6, value=f"=SUM(F2:F{FILAS + 1})")
    t.font = Font(name=F, bold=True)
    t.fill = PatternFill("solid", fgColor=HIELO)
    t.number_format = "0"

    # Extracción
    ws = wb.create_sheet(L["hojas"][2])
    cols = L["ext_cols"]
    cabecera(ws, cols, [7, 22, 8, 34, 18, 12, 30, 24, 24, 30, 28, 11, 26])
    zona_entrada(ws, len(cols), 2, FILAS + 1)
    for c, v in enumerate(L["ext_ej"], start=1):
        ws.cell(row=2, column=c, value=v).font = ejemplo_font
    dv = DataValidation(type="list", formula1=L["si_no"], allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"L2:L{FILAS + 1}")
    r1, r2 = FILAS + 3, FILAS + 4
    for r, et, val in ((r1, L["incluidos"], L["si"]), (r2, L["excluidos"], L["no"])):
        ws.cell(row=r, column=11, value=et).font = Font(name=F, bold=True, color=INDIGO)
        c = ws.cell(row=r, column=12, value=f'=COUNTIF(L2:L{FILAS + 1},"{val}")')
        c.font = Font(name=F, bold=True)
        c.fill = PatternFill("solid", fgColor=HIELO)
    return wb


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    out.mkdir(parents=True, exist_ok=True)
    for L in T.values():
        libro(L).save(out / L["archivo"])
        print("->", out / L["archivo"])
