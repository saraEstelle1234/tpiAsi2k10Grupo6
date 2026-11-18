from PIL import Image

im15 = Image.open("scripts_y_notas/pdf_page15_dcd.png")
w, h = im15.size

im15.crop((0, 0, int(w*0.5), int(h*0.5))).save("scripts_y_notas/dcd_topleft.png")
im15.crop((int(w*0.5), 0, w, int(h*0.5))).save("scripts_y_notas/dcd_topright.png")
im15.crop((0, int(h*0.5), int(w*0.5), h)).save("scripts_y_notas/dcd_botleft.png")
im15.crop((int(w*0.5), int(h*0.5), w, h)).save("scripts_y_notas/dcd_botright.png")

print("DCD crops saved!")
