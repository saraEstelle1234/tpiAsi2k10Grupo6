import fitz

doc = fitz.open("documentos/TPI ASI - Grupo 6 - 2K10.pdf")
print("Total pages:", len(doc))

toc = doc.get_toc()
print("TOC:", toc)

for i, page in enumerate(doc):
    text = page.get_text()
    first_lines = text.split('\n')[:4]
    print(f"--- Page {i+1} --- ({len(text)} chars): {' | '.join(l.strip() for l in first_lines if l.strip())}")
