# -*- coding: utf-8 -*-
"""
generate_v10_cinematic_deck.py
Compila presentacion.html e index.html con las 4 características inspiradas en museo-tpi.vercel.app:
1. Pipeline Nodal de Trazabilidad E2E en Slide 13 (BPMN -> RF45 -> CU-15 -> Prototipo UI -> DCD)
2. Modo "Recorrido Guiado con Zoom Cinematográfico y Spotlight" en BPMN (Slide 06) y Clases (Slide 12)
3. Atenuación Inteligente en la Matriz de Trazabilidad (Slide 13)
4. Panel Sincronizado de Notas del Orador (Tecla N y botón en dock)
"""

import os
import re
import json
import base64

def get_base64_img(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

# 1. Load crops
b64_traza_bpmn = get_base64_img('media/traza_node_bpmn.png')
b64_traza_dcu = get_base64_img('media/traza_node_dcu.png')
b64_traza_proto = get_base64_img('media/traza_node_proto.png')
b64_traza_dcd = get_base64_img('media/traza_node_dcd.png')

print("Loaded 4 base64 traceability crops.")

# 2. Read base generator
with open('scripts_y_notas/generate_v9_color_deck.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Add base64 crop variables at top
crops_header = f"""
# Traceability Node Crops Base64
with open('media/traza_node_bpmn.png', 'rb') as _f:
    b64_traza_bpmn = base64.b64encode(_f.read()).decode('utf-8')
with open('media/traza_node_dcu.png', 'rb') as _f:
    b64_traza_dcu = base64.b64encode(_f.read()).decode('utf-8')
with open('media/traza_node_proto.png', 'rb') as _f:
    b64_traza_proto = base64.b64encode(_f.read()).decode('utf-8')
with open('media/traza_node_dcd.png', 'rb') as _f:
    b64_traza_dcd = base64.b64encode(_f.read()).decode('utf-8')
"""
code = code.replace("from build_editorial_html import (", crops_header + "\nfrom build_editorial_html import (")

print("Added base64 variables to header.")

# Write the update logic into a build script
with open('scripts_y_notas/build_v10_deck.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Saved base build_v10_deck.py")
