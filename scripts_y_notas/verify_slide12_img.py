import re, base64, io
from PIL import Image

with open('presentacion.html', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'id="dcd-img" src="data:image/[^;]+;base64,([^"]+)"', html)
if m:
    data = base64.b64decode(m.group(1))
    im = Image.open(io.BytesIO(data))
    print('Slide 12 image size:', im.size)
else:
    print('dcd-img not found')
