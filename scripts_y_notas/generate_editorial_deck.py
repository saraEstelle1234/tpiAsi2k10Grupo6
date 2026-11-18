# -*- coding: utf-8 -*-
"""
Generates presentacion.html with Minimalist Editorial Navy design.
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

# Let's write the complete generator script
with open("scripts_y_notas/build_editorial_html.py", "w", encoding="utf-8") as out:
    out.write(f'''# -*- coding: utf-8 -*-
b64_mapa = "{b64_mapa}"
b64_bpmn_desc = "{b64_bpmn_desc}"
b64_bpmn_oper = "{b64_bpmn_oper}"
b64_dcu = "{b64_dcu}"
b64_proto = "{b64_proto}"
b64_dcd = "{b64_dcd}"
''')
print("Base asset script written.")
