import pypdf

enunciado_path = "documentos/TPI 2026 - Museo de Historia Natural.pdf"
reader = pypdf.PdfReader(enunciado_path)
print("Enunciado pages:", len(reader.pages))

text_pages = []
for i, page in enumerate(reader.pages):
    t = page.extract_text() or ""
    text_pages.append(f"\n--- PAGE {i+1} ---\n" + t)

all_enunciado = "\n".join(text_pages)
with open("scripts_y_notas/enunciado_dump.txt", "w", encoding="utf-8") as f:
    f.write(all_enunciado)

print(f"Dumped {len(all_enunciado)} characters of enunciado.")
