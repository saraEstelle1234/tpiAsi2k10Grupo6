# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="slide-9"')
idx_end = text.find('id="slide-10"')
s9_html = text[idx:idx_end]

idx_right = s9_html.find('<!-- Columna Derecha')
if idx_right != -1:
    print(s9_html[idx_right:idx_right+1000])
else:
    print("Could not find Columna Derecha comment, printing after diagram:")
    idx_diag = s9_html.find('id="dcu-img"')
    print(s9_html[idx_diag+200:idx_diag+1200])
