import base64
from io import BytesIO
from PIL import Image
import sys
sys.path.insert(0, 'scripts_y_notas')
from build_editorial_html import b64_dcd, b64_dcu, b64_bpmn_oper

data = base64.b64decode(b64_dcd.split(',')[1] if ',' in b64_dcd else b64_dcd)
im = Image.open(BytesIO(data))
print("DCD image size:", im.size, im.mode)
im.save('scripts_y_notas/dcd_full_image.png')

data_dcu = base64.b64decode(b64_dcu.split(',')[1] if ',' in b64_dcu else b64_dcu)
im_dcu = Image.open(BytesIO(data_dcu))
print("DCU image size:", im_dcu.size, im_dcu.mode)
im_dcu.save('scripts_y_notas/dcu_full_image.png')

data_bpmn = base64.b64decode(b64_bpmn_oper.split(',')[1] if ',' in b64_bpmn_oper else b64_bpmn_oper)
im_bpmn = Image.open(BytesIO(data_bpmn))
print("BPMN Oper image size:", im_bpmn.size, im_bpmn.mode)
im_bpmn.save('scripts_y_notas/bpmn_oper_full_image.png')
