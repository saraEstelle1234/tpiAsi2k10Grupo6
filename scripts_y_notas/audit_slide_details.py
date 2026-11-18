# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

def print_slide_text(num):
    m = re.search(rf'id=["\']slide-{num}["\'][\s\S]*?(?=id=["\']slide-{num+1}["\']|</div>\s*</div>\s*<!-- Hotspot|</body>)', html)
    if not m:
        print(f"Slide {num} not found")
        return
    s = m.group(0)
    # clean base64
    s = re.sub(r'data:image/[^;]+;base64,[^"]+', '[IMG]', s)
    s = re.sub(r'<svg[\s\S]*?</svg>', '[SVG]', s)
    # clean tags
    text = re.sub(r'<[^>]+>', '\n', s)
    lines = [line.strip() for line in text.splitlines() if line.strip() and line.strip() != '[SVG]']
    print(f"\n=================== SLIDE {num} ===================")
    print('\n'.join(lines[:30]))

for i in [1, 2, 3, 5, 6, 10, 11]:
    print_slide_text(i)
