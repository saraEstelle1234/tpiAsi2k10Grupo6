with open("guion_defensa_tpi.md", "r", encoding="utf-8") as f:
    text = f.read()

import re
m = re.search(r'(## 🗂️ Diapositiva 03:.*?)(?=## 🗂️ Diapositiva 08:)', text, re.DOTALL)
if m:
    print(m.group(0))
