from PIL import Image

im = Image.open('scripts_y_notas/current_dcu_in_s9.png')
w, h = im.size
print(f"Image width: {w}, height: {h}")

# The drawio dimensions were:
# X: [30, 1410] + width 30 -> [30, 1440]
# Y: [20, 1627] + height 60 -> [20, 1687]
# Notice how well (1455, 1675) aligns with drawio!
# Let's verify by checking where the actors are in current_dcu_in_s9.png:
# Drawio:
# 1. act_obras: x=30, y=130 -> in img: x ≈ 30, y ≈ 130
# 2. act_admin_museo: x=30, y=440 -> in img: x ≈ 30, y ≈ 440
# 3. act_atencion / admin_web: x=30, y=730..820
# 4. act_vigilancia (Guardia): x=30, y=1010
# 5. act_seguridad (Supervisor): x=30, y=1380
# 6. act_admin_sist: x=1410, y=260
# 7. act_usuario: x=1410, y=840

# Let's crop patches around these coordinates to confirm:
crops = {
    'obras': (0, 80, 450, 300),
    'admin_museo': (0, 380, 450, 600),
    'vigilancia_guardia': (0, 950, 600, 1250),
    'seguridad_supervisor': (0, 1300, 600, 1650),
    'admin_sist': (1000, 150, 1455, 450),
    'usuario': (1000, 750, 1455, 1050),
}

for name, box in crops.items():
    patch = im.crop(box)
    patch.save(f"scripts_y_notas/crop_{name}.png")
    print(f"Saved crop_{name}.png: box={box}")

