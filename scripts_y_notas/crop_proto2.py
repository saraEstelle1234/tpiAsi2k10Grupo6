from PIL import Image

img = Image.open('scripts_y_notas/extracted_proto_0.jpeg')
w, h = img.size
print(f"Prototype size: {w}x{h}")

img.crop((0, 0, w//2, h)).save('scripts_y_notas/proto_left.png')
img.crop((w//2, 0, w, h)).save('scripts_y_notas/proto_right.png')
print("Saved proto_left.png and proto_right.png")
