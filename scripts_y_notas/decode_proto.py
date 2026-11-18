import base64
from PIL import Image
import io
import sys
sys.path.insert(0, 'scripts_y_notas')
from build_editorial_html import b64_proto

raw_b64 = b64_proto.split(',', 1)[1] if ',' in b64_proto else b64_proto
im = Image.open(io.BytesIO(base64.b64decode(raw_b64)))
print(f"b64_proto decoded size: {im.size}, mode={im.mode}, format={im.format}")
im.save("scripts_y_notas/tablet_proto.png")
print("Saved tablet_proto.png successfully!")
