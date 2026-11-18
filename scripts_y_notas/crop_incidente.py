from PIL import Image

img = Image.open('scripts_y_notas/page9_pdf_current.png')
w, h = img.size
# Crop around y: 0.55*h to 0.70*h, x: 0 to 0.4*w
crop = img.crop((0, int(0.55*h), int(0.4*w), int(0.70*h)))
crop.save('scripts_y_notas/page9_incidente_crop.png')
print("Saved page9_incidente_crop.png")
