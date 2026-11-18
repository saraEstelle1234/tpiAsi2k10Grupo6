from PIL import Image

img = Image.open('scripts_y_notas/page15_new_dcd.png')
w, h = img.size
# Let's crop around Incidente -> TipoIncidente and Sala -> SalaXGuardia
crop = img.crop((int(0.1*w), int(0.2*h), int(0.4*w), int(0.9*h)))
crop.save('scripts_y_notas/check_new_pdf_dcd_crop.png')
print("Saved check_new_pdf_dcd_crop.png")
