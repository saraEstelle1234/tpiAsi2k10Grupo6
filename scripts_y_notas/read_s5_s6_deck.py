with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

s5_start = text.find('<!-- SLIDE 5:')
s7_start = text.find('<!-- SLIDE 7:')

print("=== SLIDE 5 & 6 ===")
print(text[s5_start:s7_start])
