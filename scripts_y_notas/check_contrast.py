from PIL import Image

dcu_crop = Image.open('scripts_y_notas/dcu_crop.png')
print("DCU crop size:", dcu_crop.size)
dcd_crop = Image.open('scripts_y_notas/dcd_crop.png')
print("DCD crop size:", dcd_crop.size)

# Check contrast
def check_contrast(img):
    rgb = img.convert('RGB')
    extrema = rgb.getextrema()
    print("Extrema:", extrema)

print("DCU contrast:")
check_contrast(dcu_crop)
print("DCD contrast:")
check_contrast(dcd_crop)
