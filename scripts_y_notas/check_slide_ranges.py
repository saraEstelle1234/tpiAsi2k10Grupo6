# -*- coding: utf-8 -*-
with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    code = f.read()

import re

# Find slide 9 and slide 12
s9_idx = code.find('<!-- SLIDE 9: DCU GENERAL')
s10_idx = code.find('<!-- SLIDE 10: PLANTILLA CU-15')
s12_idx = code.find('<!-- SLIDE 12: DIAGRAMA DE CLASES')
s13_idx = code.find('<!-- SLIDE 13: TRAZABILIDAD COMPLETA')
s14_idx = code.find('<!-- SLIDE 14: CIERRE & AGRADECIMIENTO')

print(f"s9: {s9_idx}..{s10_idx}")
print(f"s12: {s12_idx}..{s13_idx}")
print(f"s13: {s13_idx}..{s14_idx}")
