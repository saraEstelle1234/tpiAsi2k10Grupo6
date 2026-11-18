import pypdf
import os

pdf_path = "documentos/TPI ASI - Grupo 6 - 2K10.pdf"
print("Reading PDF:", pdf_path)
reader = pypdf.PdfReader(pdf_path)
print("Total pages in TPI PDF:", len(reader.pages))

full_text = []
for i, page in enumerate(reader.pages):
    t = page.extract_text() or ""
    full_text.append(f"\n--- PAGE {i+1} ---\n" + t)

all_pdf_text = "\n".join(full_text)
with open("scripts_y_notas/pdf_dump_all.txt", "w", encoding="utf-8") as f:
    f.write(all_pdf_text)

print(f"Dumped {len(all_pdf_text)} characters to scripts_y_notas/pdf_dump_all.txt")

# Let's search for table of contents or main section headers
import re
headers = re.findall(r'(^[0-9]\.[0-9].*?$|^[0-9]\..*?$)', all_pdf_text, re.MULTILINE)
print("\nHeaders found in PDF:")
for h in headers[:40]:
    print(" - ", h.strip())
