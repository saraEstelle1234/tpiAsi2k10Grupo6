with open("presentacion.html", "r", encoding="utf-8") as f:
    html = f.read()

import re

for n in [3, 5, 6, 7]:
    pat = rf'<div class="slide[^"]*" id="slide-{n}"[^>]*>(.*?)(?=<div class="slide[^"]*" id="slide-{n+1}")'
    m = re.search(pat, html, re.DOTALL)
    if m:
        t = re.sub(r'<[^>]+>', ' ', m.group(1))
        t = re.sub(r'\s+', ' ', t)
        print(f"\n=== SLIDE {n} TEXT ===")
        print(t)
