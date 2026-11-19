with open('guion_defensa_tpi.md', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'### 8\. Juan Sebastián Tarditti.*?(?=### 9\. Kevin Pereyra)', text, re.DOTALL)
if m:
    print('=== TARDITTI SPEECH ===')
    print(m.group(0))
