with open("guion_defensa_tpi.md", "r", encoding="utf-8") as f:
    text = f.read()

import re
m = re.search(r'(### 2\. Agustín Cufre.*?)(?=### 5\. Tobias Molina)', text, re.DOTALL)
if m:
    print(m.group(0))
