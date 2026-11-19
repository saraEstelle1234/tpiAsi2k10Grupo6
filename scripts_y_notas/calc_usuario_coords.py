from PIL import Image

im = Image.open('scripts_y_notas/page9_new_dcu.png')
w, h = im.size
print("DCU image size:", w, h)

# Coordinates from drawio for Usuario:
# [x=1410, y=840, w=30, h=60] 'Usuario'
# [x=1032, y=764, w=24, h=18] '43' Iniciar sesion
# [x=1032, y=844, w=24, h=18] '44' Cerrar sesion
# [x=1032, y=924, w=24, h=18] '45' Modificar contrasena

# DrawIO dimensions are roughly: w ~1500, h ~1700
# So Usuario is around:
# X: 950 to 1450 (which is right side, center ~1200 / 1455 = 82% of width)
# Y: 720 to 1000 (which is middle height, center ~860 / 1675 = 51% of height)

# If scale = 2.4:
# center of image is (50%, 50%).
# Target is around x = 82%, y = 51%.
# Offset from center: dx = 82% - 50% = +32%, dy = 51% - 50% = +1%.
# So translate should be: translate(-32% * scale, -1% * scale) or translate(-something, ...)

for tx, ty, s in [
    (-26, 0, 2.3),
    (-28, -2, 2.4),
    (-25, 2, 2.2)
]:
    # Let's crop what this transform sees in a container of ratio 0.869
    # Crop center: x_center = w/2 - (tx/100)*w, y_center = h/2 - (ty/100)*h
    # at scale s, viewport is w/s, h/s
    vw = w / s
    vh = h / s
    cx = w/2 - (tx / 100.0) * w
    cy = h/2 - (ty / 100.0) * h
    box = (int(cx - vw/2), int(cy - vh/2), int(cx + vw/2), int(cy + vh/2))
    crop = im.crop(box)
    crop.save(f'scripts_y_notas/test_crop_usuario_{s}_{tx}.png')
    print(f"Saved crop for s={s}, tx={tx}, ty={ty}, box={box}")
