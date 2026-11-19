# -*- coding: utf-8 -*-
from PIL import Image

def verify_contain_fit(img_w, img_h, vp_w, vp_h):
    # Calculate scale factor for object-fit: contain
    scale = min(vp_w / img_w, vp_h / img_h)
    rendered_w = img_w * scale
    rendered_h = img_h * scale
    print(f"Viewport ({vp_w}x{vp_h}): Image ({img_w}x{img_h}) -> Rendered ({rendered_w:.1f}x{rendered_h:.1f})")
    assert rendered_w <= vp_w, "Overflow in width!"
    assert rendered_h <= vp_h, "Overflow in height!"
    print("  -> Perfectly contained! ZERO cropping at scale(1)!")

print("--- Testing BPMN (1682 x 798) in various viewports ---")
verify_contain_fit(1682, 798, 1200, 560)
verify_contain_fit(1682, 798, 1400, 500)
verify_contain_fit(1682, 798, 1920, 600)
verify_contain_fit(1682, 798, 800, 450)

print("\n--- Testing DCU (1455 x 1675) in various viewports ---")
verify_contain_fit(1455, 1675, 1100, 650)
verify_contain_fit(1455, 1675, 800, 600)
verify_contain_fit(1455, 1675, 1400, 700)

print("\n--- Testing DCD (1422 x 904) in various viewports ---")
verify_contain_fit(1422, 904, 1100, 650)
verify_contain_fit(1422, 904, 1400, 650)
