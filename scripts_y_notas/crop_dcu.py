from PIL import Image

im9 = Image.open("scripts_y_notas/pdf_page9_dcu.png")
# Let's save a crop of bottom left (actor Usuario?), top, etc.
w, h = im9.size

im9.crop((0, 0, w, int(h*0.3))).save("scripts_y_notas/dcu_top.png")
im9.crop((0, int(h*0.7), w, h)).save("scripts_y_notas/dcu_bottom.png")
im9.crop((0, int(h*0.3), int(w*0.4), int(h*0.7))).save("scripts_y_notas/dcu_left.png")
im9.crop((int(w*0.6), int(h*0.3), w, int(h*0.7))).save("scripts_y_notas/dcu_right.png")

print("DCU crops saved successfully!")
