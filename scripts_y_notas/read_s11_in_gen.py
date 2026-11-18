with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'(<!-- SLIDE 11:.*?)(?=<!-- SLIDE 12:)', text, re.DOTALL)
if m:
    print("Slide 11 in generate_v8_deck.py:\n", m.group(1)[:400])
