with open("presentacion.html", "r", encoding="utf-8") as f:
    html = f.read()

import re

def check_slide(num):
    pat = rf'<div class="slide[^"]*" id="slide-{num}"[^>]*>(.*?)(?=<div class="slide[^"]*" id="slide-{num+1}"|</body>)'
    m = re.search(pat, html, re.DOTALL)
    if m:
        t = re.sub(r'<[^>]+>', ' ', m.group(1))
        t = re.sub(r'\s+', ' ', t)
        print(f"\n=== SLIDE {num} TEXT SAMPLE ({len(t)} chars) ===")
        print(t[:400] + "...")

for n in [2, 4, 8, 9, 10, 12, 13]:
    check_slide(n)
