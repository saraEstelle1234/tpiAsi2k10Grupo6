# -*- coding: utf-8 -*-
with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
for m in re.finditer(r'id=["\']slide-(\d+)["\']', text):
    print(f"{m.group(0)} at position {m.start()}")
