import pymupdf
import os

pdf_path = r'documentos\TPI ASI - Grupo 6 - 2K10 FINAL.pdf'
doc = pymupdf.open(pdf_path)
out_dir = r'scripts_y_notas\audit_tpi_pdf\images'
os.makedirs(out_dir, exist_ok=True)

count = 0
for p_idx, page in enumerate(doc):
    for i_idx, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_img = doc.extract_image(xref)
        ext = base_img['ext']
        w = base_img['width']
        h = base_img['height']
        img_name = f'page_{p_idx+1}_img_{i_idx+1}_{w}x{h}.{ext}'
        with open(os.path.join(out_dir, img_name), 'wb') as f:
            f.write(base_img['image'])
        count += 1
        print(f'{img_name} ({w}x{h})')

print(f'Total images: {count}')
