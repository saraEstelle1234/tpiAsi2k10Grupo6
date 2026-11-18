import base64
from PIL import Image
import io
import sys
import os

sys.path.insert(0, 'scripts_y_notas')
from build_editorial_html import b64_proto

img_bytes = base64.b64decode(b64_proto)
im = Image.open(io.BytesIO(img_bytes))
print(f"b64_proto size: {im.size}")
im.save("scripts_y_notas/tablet_proto.png")
print("Saved tablet_proto.png")
