# -*- coding: utf-8 -*-
import os
from PIL import Image

for fname in os.listdir('media'):
    if fname.startswith('board_') or fname.startswith('supervisor_'):
        fpath = os.path.join('media', fname)
        im = Image.open(fpath)
        print(f"{fname:30s} size={im.size}")
