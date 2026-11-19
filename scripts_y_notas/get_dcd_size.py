from PIL import Image
import re, base64, io

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'id="dcd-img"\s+src="data:image/png;base64,([^"]+)"', text)
if m:
    b = base64.b64decode(m.group(1))
    im = Image.open(io.BytesIO(b))
    print("dcd-img size:", im.size)
