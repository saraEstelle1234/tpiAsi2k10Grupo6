with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
s14_match = re.search(r'(<div class="slide"[^>]*id="slide-14"[^>]*>.*?)(?=</main>|</body>)', html, re.DOTALL)
if s14_match:
    s14 = s14_match.group(1)
    # find names in s14
    for m in ["Abad", "Cufre", "Marcuzzi", "Jastrzebski", "Molina", "Padilla", "Ponce", "Prados", "Santill"]:
        found = [l for l in s14.splitlines() if m.lower() in l.lower()]
        print(f"Member search {m}:", found)
