import pymupdf

doc = pymupdf.open('documentos/TPI ASI - Grupo 6 - 2K10.pdf')
print(f"Total pages: {len(doc)}")

full_text = []
for i, page in enumerate(doc):
    p_text = page.get_text()
    full_text.append(f"=== PAGE {i+1} ===\n" + p_text)

with open('scripts_y_notas/full_tpi_text_new.txt', 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(full_text))

print("Saved full_tpi_text_new.txt successfully.")
