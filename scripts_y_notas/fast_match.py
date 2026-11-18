# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image

dcu_img = Image.open('scripts_y_notas/page9_new_dcu.png').convert('L')
W, H = dcu_img.size

# Let's inspect where actors are by fast 4x downsampling
dcu_small = np.array(dcu_img.resize((W//4, H//4)), dtype=np.float32)

crops = {
    'guardia': 'media/board_guardia.png',
    'supervisor': 'media/supervisor_crop1.png',
    'obra': 'media/board_obra.png',
    'incidente': 'media/board_incidente.png'
}

for name, path in crops.items():
    c_img = Image.open(path).convert('L')
    cw, ch = c_img.size
    c_small = np.array(c_img.resize((max(1, cw//4), max(1, ch//4))), dtype=np.float32)
    
    # fast cross-correlation using OpenCV or simple sliding window
    # Actually, let's just use scipy if fast or cv2
    try:
        import cv2
        res = cv2.matchTemplate(dcu_small, c_small, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        best_x = max_loc[0] * 4
        best_y = max_loc[1] * 4
        cx = (best_x + cw/2) / W * 100
        cy = (best_y + ch/2) / H * 100
        print(f"Sector {name}: score={max_val:.2f}, x={best_x}, y={best_y}, center=({cx:.1f}%, {cy:.1f}%)")
    except Exception as e:
        print(f"Error for {name}:", e)
