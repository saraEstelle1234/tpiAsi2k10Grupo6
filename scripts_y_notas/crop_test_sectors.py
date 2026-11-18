from PIL import Image

im = Image.open('scripts_y_notas/current_dcu_in_s9.png')
w, h = im.size

# Let's crop exact zones:
# 1. Guardia: x: [0, 550], y: [880, 1220]
im.crop((0, 880, 550, 1220)).save("scripts_y_notas/test_guardia.png")
# 2. Supervisor: x: [0, 550], y: [1200, 1675]
im.crop((0, 1200, 550, 1675)).save("scripts_y_notas/test_supervisor.png")
# 3. Ingreso: x: [0, 550], y: [20, 350]
im.crop((0, 20, 550, 350)).save("scripts_y_notas/test_ingreso.png")
# 4. Admin Sistema: x: [700, 1455], y: [20, 580]
im.crop((700, 20, 1455, 580)).save("scripts_y_notas/test_admin.png")

print("Cropped successfully!")
