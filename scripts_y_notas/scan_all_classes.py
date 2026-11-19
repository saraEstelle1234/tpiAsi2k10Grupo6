from PIL import Image
import numpy as np

im = Image.open('scripts_y_notas/page15_new_dcd.png')
arr = np.array(im.convert('L'))
w, h = im.size

# Let's find all class boxes by scanning horizontal lines of width >= 150
lines = []
for y in range(h):
    row = arr[y, :] > 100
    # find continuous segments of True
    in_seg = False
    start_x = 0
    for x in range(w):
        if row[x] and not in_seg:
            in_seg = True
            start_x = x
        elif not row[x] and in_seg:
            in_seg = False
            if (x - start_x) >= 140:
                lines.append((y, start_x, x))
    if in_seg and (w - start_x) >= 140:
        lines.append((y, start_x, w))

print(f"Total horizontal box borders found: {len(lines)}")
# Group lines by X range
from collections import defaultdict
grouped = defaultdict(list)
for y, x1, x2 in lines:
    # cluster x1, x2
    matched = False
    for k in grouped:
        if abs(k[0] - x1) < 20 and abs(k[1] - x2) < 20:
            grouped[k].append(y)
            matched = True
            break
    if not matched:
        grouped[(x1, x2)].append(y)

for (x1, x2), y_list in sorted(grouped.items(), key=lambda item: item[0][0]):
    print(f"Class column X=[{x1}, {x2}] (width={x2-x1}): Y borders at {sorted(y_list)}")
