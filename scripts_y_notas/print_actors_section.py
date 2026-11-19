# -*- coding: utf-8 -*-
with open('scripts_y_notas/audit_tpi_pdf/tpi_full_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print(text[12500:14500])
