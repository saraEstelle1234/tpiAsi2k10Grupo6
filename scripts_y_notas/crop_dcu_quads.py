# -*- coding: utf-8 -*-
from PIL import Image

im = Image.open('scripts_y_notas/page9_new_dcu.png')
w, h = im.size

# Let's save 4 quadrants and center
im.crop((0, 0, w//2, h//2)).save('scripts_y_notas/dcu_q_topleft.png')
im.crop((w//2, 0, w, h//2)).save('scripts_y_notas/dcu_q_topright.png')
im.crop((0, h//2, w//2, h)).save('scripts_y_notas/dcu_q_botleft.png')
im.crop((w//2, h//2, w, h)).save('scripts_y_notas/dcu_q_botright.png')

print("Saved 4 quadrants of DCU")
