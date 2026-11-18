with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
print("\n".join(lines[2235:2285]))
