from PIL import Image

def get_bbox(path):
    img = Image.open(path).convert('RGB')
    w, h = img.size
    min_x, min_y, max_x, max_y = w, h, 0, 0
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            if img.getpixel((x, y)) != (255, 255, 255):
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
    print(f"{path}: size={w}x{h}")
    print(f"  bbox: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]")
    print(f"  margins: left={min_x}, top={min_y}, right={w - max_x}, bottom={h - max_y}")

get_bbox('Diagramas/BpmnNivelDescriptivo.png')
get_bbox('Diagramas/BpmnNivelOperativo.png')
