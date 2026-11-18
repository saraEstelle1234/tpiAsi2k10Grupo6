# -*- coding: utf-8 -*-
"""
Full Generator for Minimalist Editorial Navy Presentation (presentacion.html)
"""
import os, base64

def get_b64(path):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return ""
    with open(path, "rb") as f:
        ext = path.split('.')[-1].lower()
        if ext == 'jpg': ext = 'jpeg'
        return f"data:image/{ext};base64," + base64.b64encode(f.read()).decode('ascii')

print("Encoding diagram assets...")
b64_mapa = get_b64("media_presentacion/page_3_img_0_16.png")
b64_bpmn_desc = get_b64("media_presentacion/page_7_img_0_26.png")
b64_bpmn_oper = get_b64("media_presentacion/page_8_img_0_29.png")
b64_dcu = get_b64("media_presentacion/page_9_img_0_32.png")
b64_proto = get_b64("media_presentacion/page_14_img_0_47.jpeg")
b64_dcd = get_b64("media_presentacion/page_15_img_0_50.png")
print("Assets encoded.")

# Write builder
with open("scripts_y_notas/generate_deck.py", "w", encoding="utf-8") as f:
    f.write('''# -*- coding: utf-8 -*-
import base64, os
''')
