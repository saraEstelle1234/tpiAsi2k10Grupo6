# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="slide-9"')
idx_end = text.find('id="slide-10"')
s9_html = text[idx:idx_end]

for line in s9_html.split('\n'):
    if 'dcu-img' in line or 'diagram-frame' in line or 'preset-focus-bar' in line:
        print(line[:140])
