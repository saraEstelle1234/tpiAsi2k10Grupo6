import pymupdf
import os

os.makedirs('media_presentacion', exist_ok=True)
doc = pymupdf.open('documentos/TPI ASI - Grupo 6 - 2K10.pdf')

for i, page in enumerate(doc):
    imgs = page.get_images()
    print(f"Page {i+1}: {len(imgs)} images")
    for j, img in enumerate(imgs):
        xref = img[0]
        base = doc.extract_image(xref)
        w, h, ext = base["width"], base["height"], base["ext"]
        filename = f"media_presentacion/page_{i+1}_img_{j}_{xref}.{ext}"
        with open(filename, "wb") as f:
            f.write(base["image"])
        print(f"   Saved {filename} ({w}x{h})")

# Also render full pages for diagrams with annotations at 200 DPI
for pno in [3, 7, 8, 9, 14, 15]:
    page = doc[pno-1]
    pix = page.get_pixmap(dpi=200)
    pix.save(f"media_presentacion/rendered_page_{pno}.png")
    print(f"Rendered page {pno} at 200 DPI")
