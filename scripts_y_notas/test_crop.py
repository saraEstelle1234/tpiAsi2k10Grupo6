from PIL import Image, ImageEnhance
import base64
import io
import sys

sys.path.insert(0, 'scripts_y_notas')
from build_editorial_html import b64_dcu, b64_dcd

def check_img(name, b64_str):
    raw = base64.b64decode(b64_str.split(',')[-1])
    img = Image.open(io.BytesIO(raw))
    print(f"{name}: size={img.size}")
    # Check a crop of text
    crop = img.crop((400, 400, 700, 700))
    crop.save(f"scripts_y_notas/{name}_crop.png")
    print(f"Saved {name}_crop.png")

check_img("dcu", b64_dcu)
check_img("dcd", b64_dcd)
