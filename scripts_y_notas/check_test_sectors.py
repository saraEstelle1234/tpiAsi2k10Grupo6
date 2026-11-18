from PIL import Image
import os

for name in ['test_guardia', 'test_supervisor', 'test_ingreso', 'test_admin']:
    p = f"scripts_y_notas/{name}.png"
    im = Image.open(p)
    print(f"{name}: size={im.size}, exists={os.path.exists(p)}")
