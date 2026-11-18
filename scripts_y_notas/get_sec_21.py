with open("scripts_y_notas/pdf_dump_all.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re
m = re.search(r'2\.1\s+Identifique todos los procesos.*?(?=2\.2)', text, re.DOTALL)
if m:
    print("=== SECCION 2.1 EN TPI PDF ===")
    print(m.group(0))
else:
    # search where 2.1 is
    idx = text.find("2.1")
    print("Around 2.1:\n", text[idx:idx+1500])
