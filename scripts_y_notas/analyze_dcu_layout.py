# -*- coding: utf-8 -*-
from PIL import Image

im = Image.open('scripts_y_notas/extracted_dcu_full.png')
w, h = im.size
print(f"DCU Image dimensions: {w} x {h}")

# Let's create a visual grid of 4x4 slices with coordinates to inspect where the actors are placed.
# Or better, let's write a script that slices the diagram vertically or checks where the actors (stick figures / actor labels) are located.

# In UML Use Case diagrams, actors are usually on the left and right borders.
# Let's crop the left margin (x: 0 to 450) into 6 vertical slices, and the right margin (x: 1000 to 1455) into slices.

for i in range(8):
    y0 = int(h * i / 8)
    y1 = int(h * (i + 1) / 8)
    crop_left = im.crop((0, y0, 600, y1))
    crop_left.save(f'scripts_y_notas/dcu_actor_left_{i}.png')
    
    crop_right = im.crop((855, y0, w, y1))
    crop_right.save(f'scripts_y_notas/dcu_actor_right_{i}.png')

print("Actor inspection crops generated.")
