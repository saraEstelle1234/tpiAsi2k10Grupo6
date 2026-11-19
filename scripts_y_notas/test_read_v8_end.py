with open(r'scripts_y_notas\generate_v8_deck.py', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
print('Last 50 lines:')
for l in lines[-50:]:
    print(l)
