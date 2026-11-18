with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines[:100]):
    if 'out.write(' in l:
        print(f"Line {i+1}: {l}")
