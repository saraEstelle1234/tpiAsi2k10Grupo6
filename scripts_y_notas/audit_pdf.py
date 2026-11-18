import sys
import re

with open("scripts_y_notas/full_tpi_text.txt", "r", encoding="utf-8") as f:
    full_text = f.read()

pages = full_text.split("======================================== PAGE ")

analysis = []

def log(msg):
    analysis.append(msg)

log("=== ANALISIS DETALLADO DEL PDF: TPI ASI - Grupo 6 - 2K10.pdf ===")

# Page 1: Caratula
log("\n--- PAGINA 1: CARATULA ---")
log(pages[1][:500])

# Page 2: Consignas e Introduccion
log("\n--- PAGINA 2: CONSIGNAS ---")
log(pages[2][:500])

# Page 3 & 4: Procesos
log("\n--- PAGINA 3 Y 4: PROCESOS ---")
log(pages[3][:300])

# Search for Actores
log("\n--- SECCION ACTORES ---")
for pnum in range(1, len(pages)):
    if "Objetivos de Actores" in pages[pnum] or "Objetivos de los actores" in pages[pnum]:
        log(f"Encontrado en Pagina {pnum}:")
        log(pages[pnum])

# Search for Objetivos de Casos de Uso
log("\n--- SECCION OBJETIVOS DE CASOS DE USO ---")
for pnum in range(1, len(pages)):
    if "Objetivos de los Casos de Uso" in pages[pnum] or "Objetivos de casos de uso" in pages[pnum]:
        log(f"Encontrado en Pagina {pnum}:")
        log(pages[pnum])

# Search for Plantilla
log("\n--- SECCION PLANTILLA / DESCRIPCION DE CASO DE USO ---")
for pnum in range(1, len(pages)):
    if "DESCRIPCI" in pages[pnum] or "Registrar incidente" in pages[pnum]:
        log(f"Encontrado en Pagina {pnum} (resumen):")
        for line in pages[pnum].split("\n")[:25]:
            log("  " + line)

# Search for Diagrama de Clases
log("\n--- BUSQUEDA DE DIAGRAMA DE CLASES EN EL PDF ---")
found_dc = False
for pnum in range(1, len(pages)):
    if "clases" in pages[pnum].lower() or "diagrama de clase" in pages[pnum].lower():
        log(f"Mencion en Pagina {pnum}:")
        log(pages[pnum][:400])
        found_dc = True
if not found_dc:
    log("NO se encontro mencion ni seccion de Diagrama de Clases en el PDF!")

with open("scripts_y_notas/pdf_analysis_output.txt", "w", encoding="utf-8") as out:
    out.write("\n".join(analysis))

print("Analysis written to scripts_y_notas/pdf_analysis_output.txt")
