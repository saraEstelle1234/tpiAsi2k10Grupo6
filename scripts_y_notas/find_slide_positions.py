# -*- coding: utf-8 -*-
with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find locations
pos_s2 = text.find('<!-- SLIDE 2: DOMINIO Y OBJETIVOS -->')
pos_s3 = text.find('<!-- SLIDE 3: MAPA DE PROCESOS -->')
pos_s4 = text.find('<!-- SLIDE 4: PLANTILLA DE PROCESO DE SOPORTE -->')
pos_s5 = text.find('<!-- SLIDE 5: BPMN DESCRIPTIVO -->')
pos_s6 = text.find('<!-- SLIDE 6: BPMN OPERATIVO -->')
pos_s12 = text.find('<!-- SLIDE 12: DIAGRAMA DE CLASES')
pos_s13 = text.find('<!-- SLIDE 13: TRAZABILIDAD')
pos_s14 = text.find('<!-- SLIDE 14: CIERRE & AGRADECIMIENTO')

print(f"s2: {pos_s2}..{pos_s3}")
print(f"s4: {pos_s4}..{pos_s5}")
print(f"s5: {pos_s5}..{pos_s6}")
print(f"s12: {pos_s12}..{pos_s13}")
print(f"s14: {pos_s14}..")
