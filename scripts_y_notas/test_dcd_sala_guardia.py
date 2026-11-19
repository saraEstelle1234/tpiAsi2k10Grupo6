# -*- coding: utf-8 -*-
from PIL import Image

im = Image.open('scripts_y_notas/extracted_dcd_full.png').convert('RGB')
iw, ih = im.size
viewport_w = 1060
viewport_h = 670

zoom = 2.05
tx_pct = 19.0
ty_pct = 77.5

vis_h = ih / zoom
vis_w = vis_h * (viewport_w / viewport_h)

tx = iw * (tx_pct / 100.0)
ty = ih * (ty_pct / 100.0)

x0 = int(tx - vis_w / 2)
y0 = int(ty - vis_h / 2)
x1 = int(tx + vis_w / 2)
y1 = int(ty + vis_h / 2)

crop = Image.new('RGB', (int(vis_w), int(vis_h)), (18, 18, 18))
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
crop.save('scripts_y_notas/sim_dcd_sala_guardia.png')
print("Saved sim_dcd_sala_guardia.png")
