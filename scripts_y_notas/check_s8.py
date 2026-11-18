with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
s8_match = re.search(r'(<div class="slide"[^>]*id="slide-8"[^>]*>.*?)(?=<div class="slide"[^>]*id="slide-9")', html, re.DOTALL)
if s8_match:
    print("Slide 8 snippet:\n", s8_match.group(1)[:1200])
