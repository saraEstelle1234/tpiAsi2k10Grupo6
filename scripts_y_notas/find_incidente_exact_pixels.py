from PIL import Image
import numpy as np

im = Image.open('scripts_y_notas/page15_new_dcd.png')
arr = np.array(im.convert('L'))
print("Image shape:", arr.shape)

# Let's check region around x=300..600, y=200..350
# The class box has white borders on dark background or black borders on white?
# Let's check pixel values
print("Min pixel:", arr.min(), "Max pixel:", arr.max(), "Mean:", arr.mean())

# In page15_new_dcd.png:
# Is it white background or black background?
print("Corner pixel (0,0):", arr[0,0], "Corner pixel (10,10):", arr[10,10])

# Let's save a crop of y from 150 to 350, x from 250 to 650
crop = im.crop((250, 150, 650, 350))
crop.save('scripts_y_notas/check_incidente_title_region.png')
print("Saved check_incidente_title_region.png")
