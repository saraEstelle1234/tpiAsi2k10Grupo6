with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("=== SLIDE 1 MEMBERS ===")
s1_match = re.search(r'(<div class="slide[^"]*" id="slide-1"[^>]*>.*?)(?=<div class="slide[^"]*" id="slide-2")', html, re.DOTALL)
if s1_match:
    names = re.findall(r'<div style="font-size: 15px; font-weight: 700; color: #FFF;">(.*?)</div>', s1_match.group(1))
    for n in names:
        print("  -", n)

print("=== SLIDE 14 MEMBERS ===")
s14_match = re.search(r'(<div class="slide[^"]*" id="slide-14"[^>]*>.*?)(?=</main>|</body>)', html, re.DOTALL)
if s14_match:
    names14 = re.findall(r'<div style="font-size: 12\.5px; font-weight: 700; color: #FFF;[^"]*">(.*?)</div>', s14_match.group(1))
    for n in names14:
        print("  -", n)
