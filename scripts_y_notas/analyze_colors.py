from PIL import Image
import base64
import io
import sys

sys.path.insert(0, 'scripts_y_notas')
from build_editorial_html import b64_dcu, b64_dcd

def analyze_img(name, b64_str):
    raw = base64.b64decode(b64_str.split(',')[-1])
    img = Image.open(io.BytesIO(raw))
    print(f"=== {name} ===")
    print(f"Size: {img.size}")
    colors = img.convert('RGB').getcolors(maxcolors=1000000)
    # Sort by count descending
    colors.sort(key=lambda x: x[0], reverse=True)
    print("Top 10 most frequent colors (count, (R,G,B)):")
    total_pixels = img.size[0] * img.size[1]
    for count, col in colors[:10]:
        pct = (count / total_pixels) * 100
        print(f"  {pct:.2f}%: {col} #{col[0]:02x}{col[1]:02x}{col[2]:02x}")

analyze_img("b64_dcu", b64_dcu)
analyze_img("b64_dcd", b64_dcd)
