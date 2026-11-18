# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np

im = Image.open('scripts_y_notas/dcu_bottom.png').convert('L')
arr = np.array(im)
# Find text or stick figure silhouettes in bottom
# In UML use cases, actors are stick figures or rectangular packages
# Let's see the left, center, right parts of the bottom
im.crop((0, 0, 500, im.height)).save('scripts_y_notas/dcu_bot_left_part.png')
im.crop((500, 0, 1000, im.height)).save('scripts_y_notas/dcu_bot_mid_part.png')
im.crop((1000, 0, im.width, im.height)).save('scripts_y_notas/dcu_bot_right_part.png')
print("Saved bottom parts")
