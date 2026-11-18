with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'const traceData\s*=\s*\[(.*?)\];', text, re.DOTALL)
if m:
    print("traceData items found. Total text length:", len(m.group(1)))
    # print first 3 items
    print(m.group(1)[:800])
