# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

def get_slide(num):
    m = re.search(rf'id=["\']slide-{num}["\'][\s\S]*?(?=id=["\']slide-{num+1}["\']|</body>)', html)
    return m.group(0) if m else ""

with open('scripts_y_notas/slide9_full.html', 'w', encoding='utf-8') as f:
    # strip base64 for readability
    s9 = re.sub(r'src="data:image/[^;]+;base64,[^"]+"', 'src="[BASE64]"', get_slide(9))
    f.write(s9)

with open('scripts_y_notas/slide12_full.html', 'w', encoding='utf-8') as f:
    s12 = re.sub(r'src="data:image/[^;]+;base64,[^"]+"', 'src="[BASE64]"', get_slide(12))
    f.write(s12)

with open('scripts_y_notas/slide13_full.html', 'w', encoding='utf-8') as f:
    f.write(get_slide(13))

print("Dumped slide 9, 12, 13!")
