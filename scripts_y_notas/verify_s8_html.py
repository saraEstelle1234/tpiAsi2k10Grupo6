# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
idx = html.find('id="slide-8"')
idx2 = html.find('id="slide-9"')
print(html[idx:idx2])
