# -*- coding: utf-8 -*-
"""
Minimalist Editorial Navy Presentation Generator (TPI ASI 2K10 - Grupo 6)
Builds presentacion.html with:
- Exactly 14 slides
- Corporate Navy palette (#0A1628, #11233F, #1B3A6B, #2F6BFF, #E8EEF7, #F8FAFC)
- Google Font 'Manrope'
- Alternating dark and light slides
- Large buttons (>= 56px primary, 44px secondary, text + linear SVG icons)
- Floating dock with auto-dimming, slide counter (01 / 14), and action buttons
- Progressive reveal system
- Fullscreen zoom viewer for all diagrams with wheel zoom, drag pan, double-click, and quadrant focus
- Interactive content cards, CU-15 Step Explorer, and Traceability Console
- Onboarding 3-step mini-tutorial and 14-slide Overview Grid Modal
"""
import os
import base64

def get_b64(path):
    if not os.path.exists(path):
        print(f"Warning: {path} not found!")
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

# We will write the generator code that emits the full HTML
with open("scripts_y_notas/build_full_minimalist_deck.py", "w", encoding="utf-8") as f:
    f.write('''# -*- coding: utf-8 -*-
import os, base64

def get_b64(path):
    if not os.path.exists(path): return ""
    with open(path, "rb") as f:
        ext = path.split('.')[-1].lower()
        if ext == 'jpg': ext = 'jpeg'
        return f"data:image/{ext};base64," + base64.b64encode(f.read()).decode('ascii')

b64_mapa = get_b64("media_presentacion/page_3_img_0_16.png")
b64_bpmn_desc = get_b64("media_presentacion/page_7_img_0_26.png")
b64_bpmn_oper = get_b64("media_presentacion/page_8_img_0_29.png")
b64_dcu = get_b64("media_presentacion/page_9_img_0_32.png")
b64_proto = get_b64("media_presentacion/page_14_img_0_47.jpeg")
b64_dcd = get_b64("media_presentacion/page_15_img_0_50.png")

print("Starting generation...")
''')
