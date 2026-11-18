# -*- coding: utf-8 -*-
with open('presentacion.html', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<h1 class="giant-title">(.*?)</h1>', text, re.DOTALL)
for i, m in enumerate(matches, 1):
    print(f"Slide {i:02d}: {m.strip()}")
