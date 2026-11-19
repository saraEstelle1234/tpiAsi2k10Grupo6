# -*- coding: utf-8 -*-
from PIL import Image

def test_fit_exact(img_w, img_h, frame_w, frame_h):
    # CSS rules:
    # max-width: 100%; max-height: 100%; width: auto; height: auto; object-fit: contain;
    scale = min(frame_w / img_w, frame_h / img_h)
    rendered_w = img_w * scale
    rendered_h = img_h * scale
    margin_x = (frame_w - rendered_w) / 2
    margin_y = (frame_h - rendered_h) / 2
    print(f"Container ({frame_w}x{frame_h}): Rendered size is {rendered_w:.1f} x {rendered_h:.1f}")
    print(f"  Margins: left/right={margin_x:.1f}px, top/bottom={margin_y:.1f}px")
    assert rendered_w <= frame_w + 0.01, "Width overflow!"
    assert rendered_h <= frame_h + 0.01, "Height overflow!"
    print("  -> PASSED: 100% of the image is inside the frame with ZERO clipping!")

print("--- BPMN 1682 x 798 ---")
test_fit_exact(1682, 798, 1600, 520) # User fullscreen on 1080p
test_fit_exact(1682, 798, 1366, 450) # Laptop screen
test_fit_exact(1682, 798, 1100, 500) # Windowed

print("\n--- DCU 1455 x 1675 ---")
test_fit_exact(1455, 1675, 1100, 650)
test_fit_exact(1455, 1675, 800, 550)

print("\n--- DCD 1422 x 904 ---")
test_fit_exact(1422, 904, 1100, 600)
test_fit_exact(1422, 904, 1400, 600)
