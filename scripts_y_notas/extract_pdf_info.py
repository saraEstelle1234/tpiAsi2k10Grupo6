import pymupdf

doc1 = pymupdf.open('documentos/D de casos de uso completo.pdf')
print("=== D de casos de uso completo.pdf ===")
for i, page in enumerate(doc1):
    imgs = page.get_images()
    print(f"Page {i}: {len(imgs)} images, rect={page.rect}")
    for img in imgs:
        xref = img[0]
        base_img = doc1.extract_image(xref)
        print(f"  xref {xref}: format={base_img['ext']}, width={base_img['width']}, height={base_img['height']}, colorspace={base_img['colorspace']}")

doc2 = pymupdf.open('documentos/TPI ASI - Grupo 6 - 2K10.pdf')
print("\n=== TPI ASI - Grupo 6 - 2K10.pdf ===")
for pno in [8, 14]: # Page 9 (idx 8) and Page 15 (idx 14)
    page = doc2[pno]
    imgs = page.get_images()
    print(f"Page {pno+1}: {len(imgs)} images, rect={page.rect}")
    for img in imgs:
        xref = img[0]
        base_img = doc2.extract_image(xref)
        print(f"  xref {xref}: format={base_img['ext']}, width={base_img['width']}, height={base_img['height']}, colorspace={base_img['colorspace']}")
