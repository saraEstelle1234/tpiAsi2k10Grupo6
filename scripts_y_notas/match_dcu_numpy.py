# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image

def find_crop_in_image(main_path, crop_path):
    main_img = Image.open(main_path).convert('L')
    crop_img = Image.open(crop_path).convert('L')
    
    # Let's resize main if sizes don't match, or check if crop comes from a scaled version
    print(f"Main size: {main_img.size}, Crop size: {crop_img.size}")
    
    # Let's test different scale factors if needed
    main_arr = np.array(main_img, dtype=np.float32)
    crop_arr = np.array(crop_img, dtype=np.float32)
    
    # Try exact match first
    ch, cw = crop_arr.shape
    mh, mw = main_arr.shape
    
    # To be fast, take a 40x40 patch from center of crop
    py0 = ch // 2 - 20
    px0 = cw // 2 - 20
    patch = crop_arr[py0:py0+40, px0:px0+40]
    patch = patch - patch.mean()
    patch_norm = np.linalg.norm(patch)
    if patch_norm == 0:
        patch_norm = 1.0
        
    best_score = -1
    best_loc = (0, 0)
    
    # Step by 4
    for y in range(0, mh - 40, 4):
        for x in range(0, mw - 40, 4):
            sub = main_arr[y:y+40, x:x+40]
            sub = sub - sub.mean()
            sub_norm = np.linalg.norm(sub)
            if sub_norm > 0:
                score = np.sum(patch * sub) / (patch_norm * sub_norm)
                if score > best_score:
                    best_score = score
                    best_loc = (x - px0, y - py0)
                    
    print(f"Match for {crop_path}: best_score={best_score:.3f} at top-left x={best_loc[0]}, y={best_loc[1]}")
    cx = (best_loc[0] + cw/2) / mw * 100
    cy = (best_loc[1] + ch/2) / mh * 100
    print(f"Center percentage: X={cx:.1f}%, Y={cy:.1f}%")

find_crop_in_image('scripts_y_notas/extracted_dcu_full.png', 'media/board_guardia.png')
find_crop_in_image('scripts_y_notas/extracted_dcu_full.png', 'media/supervisor_crop1.png')
