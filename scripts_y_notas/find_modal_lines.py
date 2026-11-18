with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines):
    if 'id="overview-modal"' in l or 'id="zoom-modal"' in l or 'id="mac-dock"' in l:
        print(f"Line {i+1}: {l[:100]}")
