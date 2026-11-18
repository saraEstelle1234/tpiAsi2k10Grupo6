from PIL import Image

dcd = Image.open('media_presentacion/page_15_img_0_50.png')
print("DCD size:", dcd.size)
dcu = Image.open('media_presentacion/page_9_img_0_32.png')
print("DCU size:", dcu.size)

# Let's check bounding box of non-background content in both images
def find_bbox(img, bg_color=(18, 18, 18), tol=10):
    rgb = img.convert('RGB')
    w, h = rgb.size
    min_x, min_y, max_x, max_y = w, h, 0, 0
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            p = rgb.getpixel((x, y))
            diff = sum(abs(p[i] - bg_color[i]) for i in range(3))
            if diff > tol:
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
    print(f"Content bbox: min_x={min_x}, min_y={min_y}, max_x={max_x}, max_y={max_y}")
    print(f"Content size: {max_x - min_x} x {max_y - min_y}")
    print(f"Margins: left={min_x}, right={w - max_x}, top={min_y}, bottom={h - max_y}")

print("=== DCU bbox ===")
find_bbox(dcu)
print("=== DCD bbox ===")
find_bbox(dcd)
