from PIL import Image

img = Image.open('scripts_y_notas/extracted_dcd_p15.png')
w, h = img.size
# Let's crop x in [0.1*w, 0.4*w], y in [0.2*h, 0.9*h]
crop = img.crop((int(0.1*w), int(0.2*h), int(0.4*w), int(0.9*h)))
crop.save('scripts_y_notas/check_ayudante_crop.png')
print("Saved check_ayudante_crop.png")
