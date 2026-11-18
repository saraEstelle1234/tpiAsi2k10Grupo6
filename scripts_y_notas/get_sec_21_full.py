with open("scripts_y_notas/pdf_dump_all.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re
idx = text.find("2.1.\n \nProcesos")
print(text[idx:idx+1200])
