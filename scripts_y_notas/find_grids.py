with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
grids = re.findall(r'style="[^"]*grid-template-columns:[^"]*"', text)
print(f"Total inline grids found: {len(grids)}")
for g in set(grids):
    print(" ", g)
