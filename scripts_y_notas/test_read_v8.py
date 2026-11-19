with open(r'scripts_y_notas\generate_v8_deck.py', encoding='utf-8') as f:
    text = f.read()

# check how b64 images are loaded
print('First 30 lines:')
for l in text.splitlines()[:30]:
    print(l)
