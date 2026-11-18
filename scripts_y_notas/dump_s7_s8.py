# -*- coding: utf-8 -*-
with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    code = f.read()

idx_s7 = code.find('<!-- SLIDE 7: REQUERIMIENTOS FUNCIONALES -->')
idx_s9 = code.find('<!-- SLIDE 9: DCU GENERAL')

s7_s8_code = code[idx_s7:idx_s9]
with open('scripts_y_notas/current_s7_s8.txt', 'w', encoding='utf-8') as out:
    out.write(s7_s8_code)

print("Saved current_s7_s8.txt, length:", len(s7_s8_code))
