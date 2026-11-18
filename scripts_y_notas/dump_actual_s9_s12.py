# -*- coding: utf-8 -*-
with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    code = f.read()

s9_idx = code.find('<!-- SLIDE 9: DCU GENERAL')
s10_idx = code.find('<!-- SLIDE 10: PLANTILLA CU-15')
s12_idx = code.find('<!-- SLIDE 12: DIAGRAMA DE CLASES')
s13_idx = code.find('<!-- SLIDE 13: TRAZABILIDAD')

print("SLIDE 9 length:", s10_idx - s9_idx)
with open('scripts_y_notas/actual_s9_in_deck.txt', 'w', encoding='utf-8') as f:
    f.write(code[s9_idx:s10_idx])

print("SLIDE 12 length:", s13_idx - s12_idx)
with open('scripts_y_notas/actual_s12_in_deck.txt', 'w', encoding='utf-8') as f:
    f.write(code[s12_idx:s13_idx])

print("Dumped actual_s9_in_deck.txt and actual_s12_in_deck.txt")
