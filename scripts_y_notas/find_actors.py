# -*- coding: utf-8 -*-
with open('scripts_y_notas/audit_tpi_pdf/tpi_full_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'2\.7|Casos de Uso|Actores', text, re.IGNORECASE)]
for idx in matches[:10]:
    print("--- MATCH AT", idx, "---")
    print(text[max(0, idx-50):min(len(text), idx+300)])
