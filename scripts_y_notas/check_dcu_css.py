# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("CSS matching dcu-img:")
for m in re.finditer(r'#dcu-img[^{]*\{[^}]*\}', text):
    print(m.group(0))

print("\nCSS matching diagram-frame-clean img:")
for m in re.finditer(r'\.diagram-frame-clean\s+img[^{]*\{[^}]*\}', text):
    print(m.group(0))
