import pymupdf

doc = pymupdf.open('documentos/D de casos de uso completo.pdf')
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=150)
    out_name = f"scripts_y_notas/dcu_completo_page_{i+1}.png"
    pix.save(out_name)
    print(f"Saved {out_name}: size={pix.width}x{pix.height}")
    # Inspect text
    text = page.get_text()
    print(f"Page {i+1} text length: {len(text)}, sample: {repr(text[:100])}")
