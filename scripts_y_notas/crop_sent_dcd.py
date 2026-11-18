from PIL import Image

img = Image.open('scripts_y_notas/extracted_dcd_p15.png')
w, h = img.size
print(f"Extracted image size: {w}x{h}")

# In the DCD:
# Incidente -> TipoIncidente is on the right side or middle
# Let's crop into various slices to check
# Let's save 4 crops
img.crop((0, 0, w//2, h//2)).save('scripts_y_notas/dcd_sent_topleft.png')
img.crop((w//2, 0, w, h//2)).save('scripts_y_notas/dcd_sent_topright.png')
img.crop((0, h//2, w//2, h)).save('scripts_y_notas/dcd_sent_botleft.png')
img.crop((w//2, h//2, w, h)).save('scripts_y_notas/dcd_sent_botright.png')
print("Saved 4 crops of sent DCD image.")
