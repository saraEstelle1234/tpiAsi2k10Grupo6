from PIL import Image

im = Image.open('scripts_y_notas/tablet_proto.png')
w, h = im.size

# Let's inspect rows/columns to locate screen bezels
# In a tablet mockup, the screen is usually a rectangle inside bezels
# Let's find the inner screen boundary:
# Let's sample along horizontal line y = h // 2
pixels = im.load()
mid_y = h // 2
# find transitions
trans_x = []
for x in range(1, w):
    diff = sum(abs(pixels[x, mid_y][c] - pixels[x-1, mid_y][c]) for c in range(3))
    if diff > 60:
        trans_x.append(x)

mid_x = w // 2
trans_y = []
for y in range(1, h):
    diff = sum(abs(pixels[mid_x, y][c] - pixels[mid_x, y-1][c]) for c in range(3))
    if diff > 60:
        trans_y.append(y)

print(f"X transitions at mid Y: {trans_x[:10]} ... {trans_x[-10:]}")
print(f"Y transitions at mid X: {trans_y[:10]} ... {trans_y[-10:]}")

# Let's crop the center 80% and save it to see the mockup clearly
screen_crop = im.crop((int(w*0.1), int(h*0.1), int(w*0.9), int(h*0.9)))
screen_crop.save("scripts_y_notas/screen_crop.png")
print("Saved screen_crop.png")
