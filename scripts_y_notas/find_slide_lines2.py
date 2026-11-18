with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'id="slide-11"' in l or 'id="slide-12"' in l or 'id="slide-13"' in l:
        print(f"Line {i+1}: {l.strip()}")
