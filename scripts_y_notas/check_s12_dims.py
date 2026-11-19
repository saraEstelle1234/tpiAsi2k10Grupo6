# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="slide-12"')
idx_end = text.find('id="slide-13"')
s12_html = text[idx:idx_end]

for line in s12_html.split('\n'):
    if 'diagram-frame' in line or 'dcd-img' in line or 'height:' in line:
        print(line[:120])
