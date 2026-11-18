from PIL import Image

for name in ['proto_step1_busqueda', 'proto_step2_tipo', 'proto_step3_botones']:
    im = Image.open(f"scripts_y_notas/{name}.png")
    print(f"{name}: size={im.size}")
