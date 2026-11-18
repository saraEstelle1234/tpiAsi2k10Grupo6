# Let's inspect text/content in page_7_img_0_26.png (BPMN desc) and page_8_img_0_29.png (BPMN oper)
# We can check with OCR or examine the text from the student's submission
with open("scripts_y_notas/full_tpi_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re
print("Occurrences of 'Restaurar' or 'restauracion' in full_tpi_text:")
for line in text.splitlines():
    if any(k in line.lower() for k in ['restaur', 'tarifa', 'carril', 'estado', 'datos', 'carril', 'web']):
        print(" -", line[:100])
