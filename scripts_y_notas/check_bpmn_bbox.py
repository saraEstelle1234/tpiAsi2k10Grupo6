from PIL import Image

img = Image.open('media/bpmn_operativo_corregido.png').convert('RGB')
w, h = img.size

# Check borders
def get_bbox(img):
    min_x, min_y, max_x, max_y = w, h, 0, 0
    for y in range(h):
        for x in range(w):
            p = img.getpixel((x, y))
            # if not pure white
            if p != (255, 255, 255):
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
    print(f"Content bbox: min_x={min_x}, min_y={min_y}, max_x={max_x}, max_y={max_y}")
    print(f"Image size: {w}x{h}")
    print(f"Margins: left={min_x}, top={min_y}, right={w - 1 - max_x}, bottom={h - 1 - max_y}")

get_bbox(img)
