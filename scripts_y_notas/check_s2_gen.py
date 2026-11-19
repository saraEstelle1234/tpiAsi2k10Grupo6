with open(r'scripts_y_notas\generate_v8_deck.py', encoding='utf-8') as f:
    text = f.read()

s2_pos = text.find('<!-- SLIDE 2:')
s3_pos = text.find('<!-- SLIDE 3:')
print('=== FULL SLIDE 2 ===')
print(text[s2_pos:s3_pos])
