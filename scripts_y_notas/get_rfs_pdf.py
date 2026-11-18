with open("scripts_y_notas/pdf_dump_all.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re
pages = text.split("--- PAGE ")
rf_text = " ".join([pages[4], pages[5], pages[6]])
rf_text = re.sub(r'\s+', ' ', rf_text)

# Let's extract all sections and items
items = re.findall(r'(\d+\.\s+[^0-9]+(?=\s+\d+\.|\s+Administrar|\s+Gestionar|\s+Generar|\Z))', rf_text)
print(f"Total RF items found in PDF: {len(items)}")
for it in items[:15]:
    print(" -", it.strip())
print("...")
for it in items[-10:]:
    print(" -", it.strip())
