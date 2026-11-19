# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_s9 = text.find('id="slide-9"')
idx_s9_end = text.find('id="slide-10"')
s9_chunk = text[idx_s9:idx_s9_end]

idx_img = s9_chunk.find('id="dcu-img"')
print(s9_chunk[idx_img-600:idx_img])
