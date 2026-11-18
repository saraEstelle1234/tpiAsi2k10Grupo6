# -*- coding: utf-8 -*-
with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Let's inspect Slide 9 and preset logic
idx_preset = text.find('function setDiagramPreset')
print("setDiagramPreset at:", idx_preset)
if idx_preset != -1:
    print(text[idx_preset:idx_preset+400])

# Let's inspect Slide 11
idx_s11 = text.find('id="slide-11"')
idx_s12 = text.find('id="slide-12"')
print("Slide 11 slice:", idx_s11, idx_s12)
