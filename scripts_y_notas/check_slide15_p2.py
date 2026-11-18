# -*- coding: utf-8 -*-
with open('presentacion.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="slide-15"')
if idx != -1:
    print(text[idx+700:idx+1500])
