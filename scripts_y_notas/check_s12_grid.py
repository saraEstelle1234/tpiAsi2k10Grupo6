# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="slide-12"')
idx_end = text.find('id="slide-13"')
s12_html = text[idx:idx_end]

idx_grid = s12_html.find('style="display: grid;')
print(s12_html[idx_grid:idx_grid+600])
