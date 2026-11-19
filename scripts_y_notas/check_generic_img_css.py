# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("Generic img CSS rules:")
for m in re.finditer(r'img\s*\{[^}]*\}', text):
    print(m.group(0))
