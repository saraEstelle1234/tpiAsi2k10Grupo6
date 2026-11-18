with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [l for l in text.splitlines() if 'renderTraceMatrixItems' in l or 'traceItems' in l or 'RF-' in l][:10]
for m in matches:
    print(m[:100])
