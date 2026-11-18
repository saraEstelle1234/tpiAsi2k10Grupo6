with open("presentacion.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
m = re.search(r'(<div class="slide[^"]*" id="slide-10"[^>]*>.*?)(?=<div class="slide[^"]*" id="slide-11")', html, re.DOTALL)
if m:
    s10 = m.group(1)
    # clean tags
    print("=== SLIDE 10 FULL TEXT ===")
    t = re.sub(r'<[^>]+>', ' ', s10)
    print(re.sub(r'\s+', ' ', t))
