# -*- coding: utf-8 -*-
"""
Generate ultra-modern, high-end interactive presentation for TPI ASI 2K10 - Grupo 6
"""
import os
import base64

def get_base64_img(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            ext = path.split('.')[-1]
            if ext == 'jpg': ext = 'jpeg'
            return f"data:image/{ext};base64," + base64.b64encode(f.read()).decode('ascii')
    return ""

img_mapa = get_base64_img("media_presentacion/page_3_img_0_16.png")
img_bpmn_desc = get_base64_img("media_presentacion/page_7_img_0_26.png")
img_bpmn_oper = get_base64_img("media_presentacion/page_8_img_0_29.png")
img_dcu = get_base64_img("media_presentacion/page_9_img_0_32.png")
img_proto = get_base64_img("media_presentacion/page_14_img_0_47.jpeg")
img_dcd = get_base64_img("media_presentacion/page_15_img_0_50.png")

print("Assets encoded successfully.")
