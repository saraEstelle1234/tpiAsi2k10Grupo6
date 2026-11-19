# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw

im = Image.open('media/bpmn_operativo_corregido.png').convert('RGB')
w, h = im.size
draw = ImageDraw.Draw(im)

for i in range(1, 10):
    x = int(w * i / 10)
    draw.line([(x, 0), (x, h)], fill=(255, 0, 0), width=2)
    draw.text((x + 4, 10), f"X={i*10}%", fill=(255, 0, 0))
    draw.text((x + 4, h - 30), f"X={i*10}%", fill=(255, 0, 0))
    
for j in range(1, 10):
    y = int(h * j / 10)
    draw.line([(0, y), (w, y)], fill=(0, 0, 255), width=2)
    draw.text((10, y + 4), f"Y={j*10}%", fill=(0, 0, 255))
    draw.text((w - 70, y + 4), f"Y={j*10}%", fill=(0, 0, 255))
    
im.save('scripts_y_notas/bpmn_with_grid.png')
print("Saved bpmn_with_grid.png")
