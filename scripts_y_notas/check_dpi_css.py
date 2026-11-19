# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("CSS for diagram-preview-img:")
for m in re.finditer(r'\.diagram-preview-img[^{]*\{[^}]*\}', text):
    print(m.group(0))
