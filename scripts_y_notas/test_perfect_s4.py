from PIL import Image

im = Image.open('scripts_y_notas/page15_new_dcd.png')
w, h = im.size

# Sector 4: Sala y Guardia
# S = 1.75, cx = 280, cy = 690
s = 1.75
tx = (w/2.0 - 280)/w * 100.0  # +30.3%
ty = (h/2.0 - 690)/h * 100.0  # -26.3%

vw = w / s
vh = h / s
x1 = int(280 - vw/2.0)
y1 = int(690 - vh/2.0)
x2 = int(280 + vw/2.0)
y2 = int(690 + vh/2.0)

crop = im.crop((max(0, x1), max(0, y1), min(w, x2), min(h, y2)))
crop.save('scripts_y_notas/test_perfect_sala_guardia.png')
print(f"Sala & Guardia perfect: S={s}, tx={tx:.1f}%, ty={ty:.1f}% -> [{x1}, {y1}, {x2}, {y2}]")
