# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image

dcu_img = Image.open('scripts_y_notas/page9_new_dcu.png').convert('L')
dcu_arr = np.array(dcu_img, dtype=np.float32)

crops = {
    'guardia': 'media/board_guardia.png',
    'supervisor': 'media/supervisor_crop1.png',
    'obra': 'media/board_obra.png',
    'incidente': 'media/board_incidente.png'
}

for name, path in crops.items():
    crop_img = Image.open(path).convert('L')
    crop_arr = np.array(crop_img, dtype=np.float32)
    cw, ch = crop_img.size
    
    # Simple search or correlation around suspected areas
    # Let's downsample 2x for fast correlation
    dcu_sub = dcu_arr[::2, ::2]
    crop_sub = crop_arr[::2, ::2]
    
    from scipy.signal import correlate2d
    try:
        corr = correlate2d(dcu_sub - dcu_sub.mean(), crop_sub - crop_sub.mean(), mode='valid')
        y, x = np.unravel_index(np.argmax(corr), corr.shape)
        orig_x, orig_y = x * 2, y * 2
        print(f"Sector {name}: found at x={orig_x}, y={orig_y} in image of size {dcu_img.size}")
        print(f"Normalized center: x_pct={ (orig_x + cw/2) / dcu_img.width * 100:.1f}%, y_pct={ (orig_y + ch/2) / dcu_img.height * 100:.1f}%")
    except Exception as e:
        print(f"Error for {name}:", e)
