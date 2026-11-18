with open("scripts_y_notas/full_tpi_text.txt", encoding="utf-8") as f:
    text = f.read()

import re
pages = re.split(r'={40}\s*PAGE\s*\d+\s*={40}', text)
if len(pages) > 13:
    print(pages[13])
