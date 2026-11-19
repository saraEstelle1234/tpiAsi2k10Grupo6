# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont

def draw_grid_with_coords(img_path, out_path):
    im = Image.open(img_path).convert('RGB')
    w, h = im.size
    draw = ImageDraw.Draw(im)
    
    # Draw vertical lines every 10%
    for i in range(1, 10):
        x = int(w * i / 10)
        draw.line([(x, 0), (x, h)], fill=(255, 0, 0), width=2)
        draw.text((x + 4, 10), f"X={i*10}%", fill=(255, 0, 0))
        draw.text((x + 4, h - 30), f"X={i*10}%", fill=(255, 0, 0))
        
    # Draw horizontal lines every 10%
    for j in range(1, 10):
        y = int(h * j / 10)
        draw.line([(0, y), (w, y)], fill=(0, 0, 255), width=2)
        draw.text((10, y + 4), f"Y={j*10}%", fill=(0, 0, 255))
        draw.text((w - 70, y + 4), f"Y={j*10}%", fill=(0, 0, 255))
        
    im.save(out_path)
    print(f"Saved {out_path} ({w}x{h})")

draw_grid_with_coords('scripts_y_notas/extracted_dcu_full.png', 'scripts_y_notas/dcu_with_grid.png')
draw_grid_with_coords('scripts_y_notas/extracted_dcd_full.png', 'scripts_y_notas/dcd_with_grid.png')
