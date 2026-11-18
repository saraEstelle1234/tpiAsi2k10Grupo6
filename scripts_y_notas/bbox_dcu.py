# -*- coding: utf-8 -*-
from PIL import Image

im = Image.open('scripts_y_notas/page9_new_dcu.png')
print("page9_new_dcu:", im.size)

# Find bounding box of non-background content in page9_new_dcu (where background is (18,18,18))
bg = (18, 18, 18)
# find min_x, min_y, max_x, max_y where pixel is significantly different from (18,18,18)
pixels = im.load()
w, h = im.size

min_x, min_y, max_x, max_y = w, h, 0, 0
for y in range(h):
    for x in range(w):
        r, g, b = pixels[x, y]
        if abs(r - bg[0]) > 20 or abs(g - bg[1]) > 20 or abs(b - bg[2]) > 20:
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

print(f"Content bbox in dark image: left={min_x}, top={min_y}, right={max_x}, bottom={max_y}")
print(f"Width of content: {max_x - min_x} / {w} ({ (max_x - min_x)/w*100:.1f}%)")
print(f"Height of content: {max_y - min_y} / {h} ({ (max_y - min_y)/h*100:.1f}%)")
