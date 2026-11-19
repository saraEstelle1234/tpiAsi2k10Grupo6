# -*- coding: utf-8 -*-
import base64
import re
from PIL import Image
import io

with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract dcu-img base64
m_dcu = re.search(r'id="dcu-img"[^>]*src="data:image/png;base64,([^"]+)"', text)
if m_dcu:
    b64 = m_dcu.group(1)
    img_data = base64.b64decode(b64)
    img_dcu = Image.open(io.BytesIO(img_data))
    print(f"DCU Image size: {img_dcu.size}, mode: {img_dcu.mode}")
    img_dcu.save('scripts_y_notas/extracted_dcu_full.png')
    print("Saved scripts_y_notas/extracted_dcu_full.png")

# Extract dcd-img base64
m_dcd = re.search(r'id="dcd-img"[^>]*src="data:image/png;base64,([^"]+)"', text)
if m_dcd:
    b64 = m_dcd.group(1)
    img_data = base64.b64decode(b64)
    img_dcd = Image.open(io.BytesIO(img_data))
    print(f"DCD Image size: {img_dcd.size}, mode: {img_dcd.mode}")
    img_dcd.save('scripts_y_notas/extracted_dcd_full.png')
    print("Saved scripts_y_notas/extracted_dcd_full.png")
