# -*- coding: utf-8 -*-
"""
Script to generate a standalone HTML presentation for Grupo 6 - ASI 2K10
"""
import os
import base64

def get_base64_img(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode('ascii')
    return ""

proto_b64 = get_base64_img("media/page13_prototipo.png")
dcd_b64 = get_base64_img("scripts_y_notas/page15_new_dcd.png")
dcu_b64 = get_base64_img("scripts_y_notas/page9_pdf_current.png")
bpmn_b64 = get_base64_img("media/page6_bpmn1.png")

print(f"Loaded assets: proto={len(proto_b64)}, dcd={len(dcd_b64)}, dcu={len(dcu_b64)}, bpmn={len(bpmn_b64)}")
