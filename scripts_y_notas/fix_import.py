with open(r'scripts_y_notas\generate_v9_color_deck.py', encoding='utf-8') as f:
    text = f.read()

text = 'import base64\n' + text

with open(r'scripts_y_notas\generate_v9_color_deck.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Added import base64')
