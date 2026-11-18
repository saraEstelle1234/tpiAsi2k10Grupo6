with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<!-- SLIDE 11:.*?-->', text)
print("Slide 11 comments:", matches)
