with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
s11_match = re.search(r'(<div class="slide"[^>]*id="slide-11"[^>]*>.*?)(?=<div class="slide"[^>]*id="slide-12")', html, re.DOTALL)
if s11_match:
    print("Slide 11 in presentacion.html:\n", s11_match.group(1)[:1200])
