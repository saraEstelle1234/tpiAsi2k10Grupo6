from PIL import Image

img = Image.open('media/page13_prototipo.png')
w, h = img.size
print(f"page13_prototipo size: {w}x{h}")

# Let's crop into 3 horizontal slices to inspect the mockup screens
s1 = img.crop((0, 0, w, h//3))
s1.save('scripts_y_notas/proto_slice1.png')

s2 = img.crop((0, h//3, w, 2*h//3))
s2.save('scripts_y_notas/proto_slice2.png')

s3 = img.crop((0, 2*h//3, w, h))
s3.save('scripts_y_notas/proto_slice3.png')

print("Saved 3 slices of prototype.")
