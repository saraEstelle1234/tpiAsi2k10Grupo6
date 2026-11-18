from PIL import Image

im = Image.open('scripts_y_notas/current_dcu_in_s9.png')
print("Corner (0,0):", im.getpixel((0,0)))
print("Corner (10,10):", im.getpixel((10,10)))
print("Corner (1450, 10):", im.getpixel((1450,10)))
print("Center (727, 837):", im.getpixel((727, 837)))
