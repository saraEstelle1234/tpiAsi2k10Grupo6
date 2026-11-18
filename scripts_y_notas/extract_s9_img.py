import re
import base64
from PIL import Image
import io

with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'id="dcu-img"[^>]*src="data:image/png;base64,([^"]+)"', html)
if m:
    b64_data = m.group(1)
    img_bytes = base64.b64decode(b64_data)
    img = Image.open(io.BytesIO(img_bytes))
    print(f"DCU image in Slide 9: size={img.size}, mode={img.mode}")
    # save as scripts_y_notas/current_dcu_in_s9.png
    img.save("scripts_y_notas/current_dcu_in_s9.png")
    print("Saved to scripts_y_notas/current_dcu_in_s9.png")
