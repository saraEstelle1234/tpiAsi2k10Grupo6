with open("scripts_y_notas/pdf_dump_all.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re
pages = text.split("--- PAGE ")
p10_12 = " ".join([pages[10], pages[11], pages[12]])
p10_12 = re.sub(r'\s+', ' ', p10_12)

# find all numbered use case descriptions: "X. Nombre: Descripcion"
cus = re.findall(r'(\d+\.\s+[^:]+:\s+[^0-9]+(?=\s+\d+\.|\Z))', p10_12)
print(f"Total CU descriptions found in PDF pages 10-12: {len(cus)}")
for c in cus[:10]:
    print(" -", c[:100].strip())
print("...")
for c in cus[-6:]:
    print(" -", c[:100].strip())
