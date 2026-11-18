import pymupdf

doc = pymupdf.open('documentos/TPI ASI - Grupo 6 - 2K10.pdf')
page9 = doc[8] # page 9 (0-indexed)
print(f"Page 9 rect: {page9.rect}")
for i, img in enumerate(page9.get_images()):
    print(f"Page 9 Image {i}: xref {img[0]}")
    base = doc.extract_image(img[0])
    with open(f"scripts_y_notas/page9_new_dcu.{base['ext']}", "wb") as f:
        f.write(base['image'])
    print(f"Saved page9_new_dcu.{base['ext']} size {base['width']}x{base['height']}")
