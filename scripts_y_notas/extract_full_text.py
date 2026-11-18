import fitz

doc = fitz.open("documentos/TPI ASI - Grupo 6 - 2K10.pdf")

with open("scripts_y_notas/full_tpi_text.txt", "w", encoding="utf-8") as out:
    out.write(f"TOTAL PAGES: {len(doc)}\n\n")
    for i, page in enumerate(doc):
        out.write(f"\n{'='*40} PAGE {i+1} {'='*40}\n")
        out.write(page.get_text())

print("Full text extracted to scripts_y_notas/full_tpi_text.txt")
