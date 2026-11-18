# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image

# Let's inspect where Administrador is
# Let's check the bottom half of page9_new_dcu.png
im = Image.open('scripts_y_notas/page9_new_dcu.png')
w, h = im.size

# Save bottom quads and check
im.crop((0, int(h*0.5), int(w*0.5), h)).save('scripts_y_notas/dcu_admin_search1.png')
im.crop((int(w*0.5), int(h*0.5), w, h)).save('scripts_y_notas/dcu_admin_search2.png')

print("Saved bottom crops for Admin inspection")
