from PIL import Image

im = Image.open('scripts_y_notas/dcu_full_image.png')
w, h = im.size
print('DCU full size:', w, h)
# Encargado de vigilancia is on the left, below half height
crop = im.crop((0, int(h * 0.58), int(w * 0.42), int(h * 0.96)))
crop.save('scripts_y_notas/test_crop_dcu_vigilancia.png')
print('DCU crop saved')
