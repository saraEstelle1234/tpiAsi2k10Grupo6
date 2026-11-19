# -*- coding: utf-8 -*-
from PIL import Image

def simulate_bpmn(target_x_pct, target_y_pct, zoom, out_path):
    im = Image.open('media/bpmn_operativo_corregido.png').convert('RGB')
    iw, ih = im.size
    viewport_w = 1200
    viewport_h = 650
    
    tx = iw * (target_x_pct / 100.0)
    ty = ih * (target_y_pct / 100.0)
    
    vis_h = ih / zoom
    vis_w = vis_h * (viewport_w / viewport_h)
    
    x0 = int(tx - vis_w / 2)
    y0 = int(ty - vis_h / 2)
    x1 = int(tx + vis_w / 2)
    y1 = int(ty + vis_h / 2)
    
    crop = Image.new('RGB', (int(vis_w), int(vis_h)), (255, 255, 255))
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

# Step 1: Ronda del Guardia: tx=25%, ty=13%, zoom=2.1
simulate_bpmn(25, 13, 2.1, 'scripts_y_notas/sim_bpmn_ronda.png')

# Step 2: Detección y Registro: tx=37%, ty=20%, zoom=2.2
simulate_bpmn(37, 20, 2.2, 'scripts_y_notas/sim_bpmn_deteccion.png')

# Step 3: Acciones Sugeridas: tx=56%, ty=50%, zoom=2.0
simulate_bpmn(56, 50, 2.0, 'scripts_y_notas/sim_bpmn_acciones.png')

# Step 4: Restaurar Obra: tx=22%, ty=82%, zoom=2.2
simulate_bpmn(22, 82, 2.2, 'scripts_y_notas/sim_bpmn_restaurar.png')
