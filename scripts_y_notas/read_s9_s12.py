with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

s9_start = text.find('<!-- SLIDE 9: DCU')
s10_start = text.find('<!-- SLIDE 10:')
print("=== CURRENT SLIDE 9 ===")
print(text[s9_start:s10_start])

s12_start = text.find('<!-- SLIDE 12: DIAGRAMA DE CLASES')
s13_start = text.find('<!-- SLIDE 13:')
print("=== CURRENT SLIDE 12 ===")
print(text[s12_start:s13_start])
