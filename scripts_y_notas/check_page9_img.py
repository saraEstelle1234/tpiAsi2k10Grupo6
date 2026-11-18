import pymupdf

doc = pymupdf.open('documentos/TPI ASI - Grupo 6 - 2K10.pdf')
page9 = doc[8]
for img in page9.get_images():
    xref = img[0]
    base = doc.extract_image(xref)
    print(f"Page 9 Image xref {xref}: format {base['ext']}, size {base['width']}x{base['height']}")
    with open('scripts_y_notas/page9_pdf_current.png', 'wb') as f:
        f.write(base['image'])

print("Extracted page 9 image.")
