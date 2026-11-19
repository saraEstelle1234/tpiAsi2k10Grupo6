from PIL import Image

im = Image.open('scripts_y_notas/dcd_full_image.png')
w, h = im.size
print('DCD dimensions:', w, h)

# Let's save a crop of Incidente & Sala
crop = im.crop((int(w*0.2), int(h*0.1), int(w*0.8), int(h*0.9)))
crop.save('scripts_y_notas/test_crop_dcd_actual.png')
print('Crop saved')
