with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '<!-- SLIDE' in line:
        print(f"Line {i+1}: {line.strip()}")
