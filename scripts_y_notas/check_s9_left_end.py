# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="slide-9"')
idx_end = text.find('id="slide-10"')
s9_html = text[idx:idx_end]

idx_img = s9_html.find('id="dcu-img"')
idx_col_right = s9_html.find('<!-- Columna Derecha')
print(s9_html[idx_img:idx_col_right])
