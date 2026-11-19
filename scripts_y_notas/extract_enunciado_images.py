import pymupdf
import os

pdf_path = r'documentos\TPI 2026 - Museo de Historia Natural.pdf'
doc = pymupdf.open(pdf_path)
print('Total pages in enunciado:', len(doc))
out_dir = r'scripts_y_notas\enunciado_images'
os.makedirs(out_dir, exist_ok=True)

for p_idx, page in enumerate(doc):
    for i_idx, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_img = doc.extract_image(xref)
        w = base_img['width']
        h = base_img['height']
        ext = base_img['ext']
        img_name = f'enunciado_p{p_idx+1}_img{i_idx+1}_{w}x{h}.{ext}'
        with open(os.path.join(out_dir, img_name), 'wb') as f:
            f.write(base_img['image'])
        print(f'{img_name} ({w}x{h})')
