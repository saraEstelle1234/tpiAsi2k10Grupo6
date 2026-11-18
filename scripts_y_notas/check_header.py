with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<header[^>]*>.*?</header>', text, re.DOTALL)
if m:
    print("Header markup:\n", m.group(0))
