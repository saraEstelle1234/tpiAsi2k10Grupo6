import re

with open(r'scripts_y_notas\generate_v8_deck.py', encoding='utf-8') as f:
    code = f.read()

print('Checking import of base64 images...')
print(code[:400])
