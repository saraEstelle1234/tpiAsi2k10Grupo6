# -*- coding: utf-8 -*-
with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos_s7 = text.find('SLIDE 7: REQUERIMIENTOS FUNCIONALES')
pos_s8 = text.find('SLIDE 8: REQUERIMIENTOS NO FUNCIONALES')
pos_s9 = text.find('SLIDE 9: DCU GENERAL')

print(f"pos_s7={pos_s7}, pos_s8={pos_s8}, pos_s9={pos_s9}")
