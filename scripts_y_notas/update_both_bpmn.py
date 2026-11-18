import base64
import re
import shutil
from PIL import Image

desc_path = 'Diagramas/BpmnNivelDescriptivo.png'
oper_path = 'Diagramas/BpmnNivelOperativo.png'

# 1. Copy to media folders for direct referencing if needed
shutil.copyfile(desc_path, 'media/bpmn_nivel_descriptivo.png')
shutil.copyfile(oper_path, 'media/bpmn_nivel_operativo.png')
shutil.copyfile(oper_path, 'media/bpmn_operativo_corregido.png')
shutil.copyfile(desc_path, 'media_presentacion/BpmnNivelDescriptivo.png')
shutil.copyfile(oper_path, 'media_presentacion/BpmnNivelOperativo.png')
print("Copied images to media/ and media_presentacion/")

# 2. Base64 encode
with open(desc_path, 'rb') as f:
    b64_desc = f"data:image/png;base64,{base64.b64encode(f.read()).decode('ascii')}"

with open(oper_path, 'rb') as f:
    b64_oper = f"data:image/png;base64,{base64.b64encode(f.read()).decode('ascii')}"

print(f"b64_desc length: {len(b64_desc)}")
print(f"b64_oper length: {len(b64_oper)}")

# 3. Update build_editorial_html.py
with open('scripts_y_notas/build_editorial_html.py', 'r', encoding='utf-8') as f:
    code = f.read()

code, count_desc = re.subn(
    r'b64_bpmn_desc\s*=\s*"data:image/png;base64,[^"]+"',
    f'b64_bpmn_desc = "{b64_desc}"',
    code
)

code, count_oper = re.subn(
    r'b64_bpmn_oper\s*=\s*"data:image/png;base64,[^"]+"',
    f'b64_bpmn_oper = "{b64_oper}"',
    code
)

print(f"Replaced in build_editorial_html.py: desc={count_desc}, oper={count_oper}")

with open('scripts_y_notas/build_editorial_html.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("build_editorial_html.py saved!")
