import os
import base64

assets = {
    'mapa': 'media_presentacion/page_3_img_0_16.png',
    'bpmn_desc': 'media_presentacion/page_7_img_0_26.png',
    'bpmn_oper': 'media_presentacion/page_8_img_0_29.png',
    'dcu': 'media_presentacion/page_9_img_0_32.png',
    'proto': 'media_presentacion/page_14_img_0_47.jpeg',
    'dcd': 'media_presentacion/page_15_img_0_50.png'
}

for k, p in assets.items():
    if os.path.exists(p):
        size = os.path.getsize(p)
        print(f"{k:10}: {p} -> {size/1024:.1f} KB")
    else:
        print(f"MISSING: {p}")
