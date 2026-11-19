from PIL import Image
import numpy as np

im = Image.open('scripts_y_notas/page15_new_dcd.png')
arr = np.array(im.convert('L'))

# Find all pixels > 100 in the region x in [300, 600], y in [180, 320]
sub = arr[180:320, 300:600]
coords = np.argwhere(sub > 100)
if len(coords) > 0:
    min_y = coords[:, 0].min() + 180
    max_y = coords[:, 0].max() + 180
    min_x = coords[:, 1].min() + 300
    max_x = coords[:, 1].max() + 300
    print(f"White content detected in region: X=[{min_x}, {max_x}], Y=[{min_y}, {max_y}]")

# Let's find the top line of the Incidente class box
# The top border of Incidente box is a horizontal line of white pixels
for y in range(200, 300):
    row = arr[y, 340:570]
    white_count = np.sum(row > 100)
    if white_count > 150:
        print(f"Horizontal border detected at Y={y}! White count={white_count}")

# Also find bottom line of Incidente box
for y in range(450, 550):
    row = arr[y, 340:570]
    white_count = np.sum(row > 100)
    if white_count > 150:
        print(f"Bottom border of Incidente detected at Y={y}! White count={white_count}")

# Find Sala box borders
for y in range(500, 600):
    row = arr[y, 340:570]
    white_count = np.sum(row > 100)
    if white_count > 150:
        print(f"Top border of Sala detected at Y={y}! White count={white_count}")

for y in range(700, 820):
    row = arr[y, 340:570]
    white_count = np.sum(row > 100)
    if white_count > 150:
        print(f"Bottom border of Sala detected at Y={y}! White count={white_count}")
