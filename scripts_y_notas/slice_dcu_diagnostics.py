# -*- coding: utf-8 -*-
from PIL import Image

im = Image.open('scripts_y_notas/extracted_dcu_full.png')
w, h = im.size

# Let's save smaller diagnostic crops of each height slice to identify all actors
# The diagram has actors on the left and right.
# Let's slice y from 0 to 100% in 10% steps
for i in range(10):
    y_start = int(h * i / 10)
    y_end = int(h * (i + 1) / 10)
    # left side (0 to 45% width)
    crop_l = im.crop((0, y_start, int(w * 0.5), y_end))
    crop_l.save(f'scripts_y_notas/diag_l_{i*10}_{(i+1)*10}.png')
    # right side (50% to 100% width)
    crop_r = im.crop((int(w * 0.5), y_start, w, y_end))
    crop_r.save(f'scripts_y_notas/diag_r_{i*10}_{(i+1)*10}.png')

print("Diagnostic slices saved.")
