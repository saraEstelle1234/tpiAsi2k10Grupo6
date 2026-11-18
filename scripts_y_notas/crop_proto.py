from PIL import Image

img = Image.open('scripts_y_notas/extracted_proto_0.png')
w, h = img.size
print(f"Prototype size: {w}x{h}")

# Let's crop into panels or halves to see the mockup fields
img.crop((0, 0, w//2, h)).save('scripts_y_notas/proto_left.png')
img.crop((w//2, 0, w, h)).save('scripts_y_notas/proto_right.png')
print("Saved proto_left.png and proto_right.png")
