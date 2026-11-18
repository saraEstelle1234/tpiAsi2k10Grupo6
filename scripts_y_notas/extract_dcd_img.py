import pymupdf

doc = pymupdf.open('documentos/TPI ASI - Grupo 6 - 2K10.pdf')
page = doc[14]
for img_info in page.get_images():
    xref = img_info[0]
    base_img = doc.extract_image(xref)
    ext = base_img["ext"]
    w = base_img["width"]
    h = base_img["height"]
    print(f"Image xref {xref}: format {ext}, size {w}x{h}")
    with open(f"scripts_y_notas/extracted_dcd_p15.{ext}", "wb") as f:
        f.write(base_img["image"])
    print("Saved extracted_dcd_p15")
