with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines):
    for s in ['id="slide-9"', 'id="slide-11"', 'id="slide-12"', 'id="slide-13"', 'id="slide-14"']:
        if s in l:
            print(f"Found {s} at line {i+1}")
