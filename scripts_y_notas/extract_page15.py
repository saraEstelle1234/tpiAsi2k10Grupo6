import pymupdf

doc = pymupdf.open('documentos/TPI ASI - Grupo 6 - 2K10.pdf')
page15 = doc[14] # page 15
print(f"Page 15 rect: {page15.rect}")
for i, img in enumerate(page15.get_images()):
    print(f"Page 15 Image {i}: xref {img[0]}")
    base = doc.extract_image(img[0])
    with open(f"scripts_y_notas/page15_new_dcd.{base['ext']}", "wb") as f:
        f.write(base['image'])
    print(f"Saved page15_new_dcd.{base['ext']} size {base['width']}x{base['height']}")
