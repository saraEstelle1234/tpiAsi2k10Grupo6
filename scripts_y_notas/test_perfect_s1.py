from PIL import Image

im = Image.open('scripts_y_notas/page15_new_dcd.png')
w, h = im.size

# Let's test s1 with cy=475, cx=445, S=1.58
s = 1.58
tx = (w/2.0 - 445)/w * 100.0  # +18.7%
ty = (h/2.0 - 475)/h * 100.0  # -2.5%

vw = w / s
vh = h / s
x1 = int(445 - vw/2.0)
y1 = int(475 - vh/2.0)
x2 = int(445 + vw/2.0)
y2 = int(475 + vh/2.0)

crop = im.crop((max(0, x1), max(0, y1), min(w, x2), min(h, y2)))
crop.save('scripts_y_notas/test_perfect_incidente_sala.png')
print(f"Incidente & Sala perfect: S={s}, tx={tx:.1f}%, ty={ty:.1f}% -> [{x1}, {y1}, {x2}, {y2}]")
