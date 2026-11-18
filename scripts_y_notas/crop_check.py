from PIL import Image

im9 = Image.open("scripts_y_notas/pdf_page9_dcu.png")
im15 = Image.open("scripts_y_notas/pdf_page15_dcd.png")

print(f"im9 size: {im9.size}, mode: {im9.mode}")
print(f"im15 size: {im15.size}, mode: {im15.mode}")

# Save small crops to check them
im15.crop((0, 0, 500, 300)).save("scripts_y_notas/crop_dcd_topleft.png")
im15.crop((500, 200, 1000, 600)).save("scripts_y_notas/crop_dcd_center.png")
print("Crops saved!")
