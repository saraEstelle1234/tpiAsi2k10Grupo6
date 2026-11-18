from PIL import Image

img = Image.open('scripts_y_notas/page9_pdf_current.png')
w, h = img.size
# Let's crop around y: 0.4*h to 0.55*h, x: 0 to 0.4*w
crop = img.crop((0, int(0.4*h), int(0.4*w), int(0.55*h)))
crop.save('scripts_y_notas/page9_venta_crop.png')
print("Saved page9_venta_crop.png")
