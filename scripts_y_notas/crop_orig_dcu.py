from PIL import Image

img = Image.open('scripts_y_notas/pdf_page9_dcu.png')
w, h = img.size
print(f"Image size: {w}x{h}")

# In the PDF, let's crop around row with 10, 11, 12 and row with 15, 16
# Let's inspect where they are
crop1 = img.crop((0, int(h * 0.35), int(w * 0.55), int(h * 0.65)))
crop1.save('scripts_y_notas/dcu_orig_guia_incidente.png')
print("Saved dcu_orig_guia_incidente.png")
