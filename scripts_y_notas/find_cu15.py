from PIL import Image

# Let's inspect different quadrants of page8_diagram.png
im = Image.open('media/page8_diagram.png')
w, h = im.size
print('DCU size:', w, h)

# Let's save 4 slices vertically to find CU 15
for i in range(4):
    y0 = int(h * i / 4)
    y1 = int(h * (i + 1) / 4)
    slice_img = im.crop((0, y0, w, y1))
    slice_img.save(f'scripts_y_notas/dcu_slice_{i}.png')
print("DCU slices saved.")
