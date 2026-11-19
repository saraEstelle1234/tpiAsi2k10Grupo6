from PIL import Image

im = Image.open('scripts_y_notas/page15_new_dcd.png')
w, h = im.size

refined = {
    '0_vista_global': (1.0, 0.0, 0.0),
    '1_incidente_sala': (1.58, 18.7, -2.5),
    '2_obra_material': (1.60, -14.7, 8.0),
    '3_tipo_incidente': (1.95, 30.3, 12.4),
    '4_sala_guardia': (1.75, 30.3, -26.3)
}

for name, (s, tx, ty) in refined.items():
    vw = w / s
    vh = h / s
    cx = w/2.0 - (tx / 100.0) * w
    cy = h/2.0 - (ty / 100.0) * h
    
    x1 = int(cx - vw/2.0)
    y1 = int(cy - vh/2.0)
    x2 = int(cx + vw/2.0)
    y2 = int(cy + vh/2.0)
    
    c_x1 = max(0, x1)
    c_y1 = max(0, y1)
    c_x2 = min(w, x2)
    c_y2 = min(h, y2)
    
    crop = im.crop((c_x1, c_y1, c_x2, c_y2))
    crop.save(f'scripts_y_notas/verified_{name}.png')
    print(f"[{name}] S={s}, tx={tx}%, ty={ty}% -> Viewport: X=[{x1}, {x2}], Y=[{y1}, {y2}]")
