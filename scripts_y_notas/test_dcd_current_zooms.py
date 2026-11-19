from PIL import Image

im = Image.open('scripts_y_notas/page15_new_dcd.png')
w, h = im.size
print("DCD image size:", w, h)

# Container viewport aspect ratio:
# In Slide 12:
# <div style="display: grid; grid-template-columns: 1fr 280px; gap: 20px; align-items: stretch;">
# Left container has height: clamp(480px, 68vh, 720px); (say ~580px)
# Width: around (1400 - 280 - 40) = ~1080px.
# Aspect ratio of viewport ~ 1080 / 580 ~ 1.86 (landscape)

# In CSS:
# .cinematic-viewport has width: 100%, height: 100%
# img#dcd-img has max-width: 100%, max-height: 100%
# Image native size is 1422 x 904 (aspect ratio 1.573)
# If container is 1080 x 580:
# 580 * 1.573 = 912px width. So image inside viewport is 912 x 580 centered.
# CSS transform: transform-origin: 50% 50%;
# transform: scale(S) translate(tx%, ty%)

# Let's test what 'scale(2.1) translate(21%, -2%)' shows!
# In image coordinate space:
# delta_x = (tx / 100) * w
# delta_y = (ty / 100) * h
# center_x = w/2 - delta_x
# center_y = h/2 - delta_y
# visible_w = w / S
# visible_h = h / S

steps = {
    '0_global': (1.0, 0.0, 0.0),
    '1_incidente_sala_current': (2.1, 21.0, -2.0),
    '2_obra_material_current': (2.0, -13.0, 8.0),
    '3_tipo_incidente_current': (2.4, 32.0, 13.0),
    '4_sala_guardia_current': (2.05, 31.0, -27.5)
}

for name, (s, tx, ty) in steps.items():
    vw = w / s
    vh = h / s
    cx = w/2.0 - (tx / 100.0) * w
    cy = h/2.0 - (ty / 100.0) * h
    
    x1 = int(cx - vw/2.0)
    y1 = int(cy - vh/2.0)
    x2 = int(cx + vw/2.0)
    y2 = int(cy + vh/2.0)
    
    # Clamp for crop
    c_x1 = max(0, x1)
    c_y1 = max(0, y1)
    c_x2 = min(w, x2)
    c_y2 = min(h, y2)
    
    crop = im.crop((c_x1, c_y1, c_x2, c_y2))
    crop.save(f'scripts_y_notas/dcd_test_{name}.png')
    print(f"{name}: S={s}, tx={tx}%, ty={ty}% -> Viewport in image: [{x1}, {y1}, {x2}, {y2}]")
