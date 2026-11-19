# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="dcu-img"')
print(text[idx-200:idx+300])
