from PIL import Image

im = Image.open('scripts_y_notas/page9_new_dcu.png')
w, h = im.size

# In a container of aspect ratio w_c / h_c ~ 0.869 (matches w/h of image)
# At scale S and translate (TX%, TY%):
# CSS transform: scale(S) translate(TX%, TY%)
# This moves the center of the image by:
# delta_x_pixels = (TX / 100.0) * w
# delta_y_pixels = (TY / 100.0) * h
# The visible window in original image pixels has size:
# win_w = w / S
# win_h = h / S
# The visible center is:
# center_x = w/2 - delta_x_pixels
# center_y = h/2 - delta_y_pixels

actors = {
    'all': (1.0, 0.0, 0.0),
    'vigilancia': (2.4, 31.5, -13.0),
    'supervision': (2.4, 37.5, -35.0),
    'ingreso': (2.4, 37.5, 39.5),
    'atencion': (2.3, 24.5, 8.5),
    'museo': (2.35, 36.0, 22.0),
    'admin': (2.15, -25.5, 32.5),
    'usuario': (2.3, -26.5, -1.0)
}

for name, (s, tx, ty) in actors.items():
    win_w = w / s
    win_h = h / s
    cx = w/2.0 - (tx / 100.0) * w
    cy = h/2.0 - (ty / 100.0) * h
    
    x1 = max(0, int(cx - win_w / 2.0))
    y1 = max(0, int(cy - win_h / 2.0))
    x2 = min(w, int(cx + win_w / 2.0))
    y2 = min(h, int(cy + win_h / 2.0))
    
    crop = im.crop((x1, y1, x2, y2))
    crop.save(f'scripts_y_notas/sim_actor_{name}.png')
    print(f"Actor '{name}': scale={s}, tx={tx}%, ty={ty}% -> box ({x1}, {y1}, {x2}, {y2})")
