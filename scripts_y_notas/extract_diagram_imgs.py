import fitz

doc = fitz.open("documentos/TPI ASI - Grupo 6 - 2K10.pdf")

# Extract page 9 image (DCU) and page 15 image (DCD)
p9 = doc[8] # 0-based
p15 = doc[14]

img9_xref = p9.get_images()[0][0]
img15_xref = p15.get_images()[0][0]

b9 = doc.extract_image(img9_xref)
with open("scripts_y_notas/pdf_page9_dcu.png", "wb") as f:
    f.write(b9["image"])

b15 = doc.extract_image(img15_xref)
with open("scripts_y_notas/pdf_page15_dcd.png", "wb") as f:
    f.write(b15["image"])

print(f"Page 9 DCU extracted: {b9['width']}x{b9['height']}")
print(f"Page 15 DCD extracted: {b15['width']}x{b15['height']}")
