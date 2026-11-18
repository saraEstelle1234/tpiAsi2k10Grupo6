with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

s1_idx = text.find('<!-- SLIDE 1:')
s2_idx = text.find('<!-- SLIDE 2:')
print("=== SLIDE 1 MEMBERS ===")
print(text[s1_idx:s2_idx])

s14_idx = text.find('<!-- SLIDE 14:')
print("=== SLIDE 14 SNIPPET ===")
print(text[s14_idx:s14_idx+2500])
