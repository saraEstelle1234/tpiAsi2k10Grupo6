# -*- coding: utf-8 -*-
from PIL import Image

def test_dcu_viewport(tx_pct, ty_pct, zoom, out_name):
    im = Image.open('scripts_y_notas/extracted_dcu_full.png').convert('RGB')
    iw, ih = im.size
    viewport_w = 1100
    viewport_h = 740
    
    # Rendered image size inside viewport_w x viewport_h with aspect-ratio:
    # height = viewport_h = 740
    # width = 740 * (1455 / 1675) = 642.8
    # When #dcu-inner has aspect-ratio 1455 / 1675,
    # its visible window at zoom S:
    vis_h = ih / zoom
    vis_w = (ih / zoom) * (viewport_w / viewport_h)
    
    tx = iw * (tx_pct / 100.0)
    ty = ih * (ty_pct / 100.0)
    
    x0 = int(tx - vis_w / 2)
    y0 = int(ty - vis_h / 2)
    x1 = int(tx + vis_w / 2)
    y1 = int(ty + vis_h / 2)
    
    crop = Image.new('RGB', (int(vis_w), int(vis_h)), (15, 23, 42))
    src_x0 = max(0, x0)
    src_y0 = max(0, y0)
    src_x1 = min(iw, x1)
    src_y1 = min(ih, y1)
    
    if src_x1 > src_x0 and src_y1 > src_y0:
        patch = im.crop((src_x0, src_y0, src_x1, src_y1))
        dest_x = src_x0 - x0
        dest_y = src_y0 - y0
        crop.paste(patch, (dest_x, dest_y))
        
    crop = crop.resize((viewport_w, viewport_h), Image.Resampling.LANCZOS)
    crop.save(f'scripts_y_notas/{out_name}.png')
    print(f"Saved scripts_y_notas/{out_name}.png")

test_dcu_viewport(18.5, 63.0, 2.45, 'sim_dcu_laser_vigilancia')
test_dcu_viewport(12.5, 85.0, 2.45, 'sim_dcu_laser_supervision')
test_dcu_viewport(12.5, 10.5, 2.45, 'sim_dcu_laser_ingreso')
test_dcu_viewport(25.5, 41.5, 2.25, 'sim_dcu_laser_atencion')
test_dcu_viewport(75.5, 17.5, 2.15, 'sim_dcu_laser_admin')
