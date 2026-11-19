# -*- coding: utf-8 -*-
from PIL import Image

def simulate_viewport(img_path, target_x_pct, target_y_pct, zoom, viewport_w, viewport_h, out_path):
    im = Image.open(img_path).convert('RGB')
    iw, ih = im.size
    
    # Target center in pixel coordinates
    tx = iw * (target_x_pct / 100.0)
    ty = ih * (target_y_pct / 100.0)
    
    # When displayed with object-fit: contain inside a viewport of aspect ratio AR = viewport_w / viewport_h
    # In Slide 09: viewport is 620 x 520 (AR = 620/520 = 1.192)
    # DCU image is 1455 x 1675 (AR = 0.868) -> fitted by height: height = viewport_h, width = viewport_h * 0.868
    # With zoom S, visible window in image coords:
    # visible_h = ih / zoom
    # visible_w = visible_h * (viewport_w / viewport_h)
    
    vis_h = ih / zoom
    vis_w = vis_h * (viewport_w / viewport_h)
    
    x0 = int(tx - vis_w / 2)
    y0 = int(ty - vis_h / 2)
    x1 = int(tx + vis_w / 2)
    y1 = int(ty + vis_h / 2)
    
    # Clamp or pad with black if needed
    crop = Image.new('RGB', (int(vis_w), int(vis_h)), (18, 18, 18))
    
    # Source box clamped to image
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
    crop.save(out_path)
    print(f"Simulated {out_path} centered at ({target_x_pct}%, {target_y_pct}%) zoom={zoom}")

# Let's test DCU actors:
# 1. Encargado de Vigilancia: tx=17%, ty=62%, zoom=2.3
simulate_viewport('scripts_y_notas/extracted_dcu_full.png', 17, 62, 2.3, 620, 520, 'scripts_y_notas/sim_dcu_vigilancia.png')

# 2. Encargado de Supervision: tx=12%, ty=85%, zoom=2.3
simulate_viewport('scripts_y_notas/extracted_dcu_full.png', 12, 85, 2.3, 620, 520, 'scripts_y_notas/sim_dcu_supervision.png')

# 3. Responsable de Ingreso de Obras: tx=12%, ty=11%, zoom=2.3
simulate_viewport('scripts_y_notas/extracted_dcu_full.png', 12, 11, 2.3, 620, 520, 'scripts_y_notas/sim_dcu_ingreso.png')

# 4. Atencion al Cliente / Visitas: tx=24%, ty=44%, zoom=2.2
simulate_viewport('scripts_y_notas/extracted_dcu_full.png', 24, 44, 2.2, 620, 520, 'scripts_y_notas/sim_dcu_atencion.png')

# 5. Administrador del Museo: tx=12%, ty=29%, zoom=2.3
simulate_viewport('scripts_y_notas/extracted_dcu_full.png', 12, 29, 2.3, 620, 520, 'scripts_y_notas/sim_dcu_museo.png')

# 6. Admin de Sistema (Tablas Maestras): tx=74%, ty=17%, zoom=2.0
simulate_viewport('scripts_y_notas/extracted_dcu_full.png', 74, 17, 2.0, 620, 520, 'scripts_y_notas/sim_dcu_admin.png')
