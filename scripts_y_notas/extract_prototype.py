import pymupdf

doc = pymupdf.open('documentos/TPI ASI - Grupo 6 - 2K10.pdf')
page14 = doc[13] # 0-indexed page 14
pix = page14.get_pixmap(dpi=150)
pix.save('scripts_y_notas/sent_pdf_page14_prototype.png')
print("Saved sent_pdf_page14_prototype.png")

for i, img_info in enumerate(page14.get_images()):
    xref = img_info[0]
    base_img = doc.extract_image(xref)
    ext = base_img["ext"]
    with open(f"scripts_y_notas/extracted_proto_{i}.{ext}", "wb") as f:
        f.write(base_img["image"])
    print(f"Extracted prototype image {i}: {base_img['width']}x{base_img['height']}")
