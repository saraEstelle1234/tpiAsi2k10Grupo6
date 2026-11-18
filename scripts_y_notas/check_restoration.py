import re

with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("=== SLIDE 4 (PLANTILLA PROCESO) ===")
s4 = text[text.find('id="slide-4"'):text.find('id="slide-5"')]
for line in s4.splitlines():
    if any(k in line.lower() for k in ['restaur', 'supervisor', 'evalu', 'resolu', 'fin', 'decis', 'accion']):
        print(line.strip())

print("\n=== SLIDE 5 (BPMN DESCRIPTIVO) ===")
s5 = text[text.find('id="slide-5"'):text.find('id="slide-6"')]
for line in s5.splitlines():
    if any(k in line.lower() for k in ['restaur', 'supervisor', 'evalu', 'resolu', 'accion']):
        print(line.strip())

print("\n=== SLIDE 6 (BPMN OPERATIVO) ===")
s6 = text[text.find('id="slide-6"'):text.find('id="slide-7"')]
for line in s6.splitlines():
    if any(k in line.lower() for k in ['restaur', 'supervisor', 'evalu', 'resolu', 'accion']):
        print(line.strip())
