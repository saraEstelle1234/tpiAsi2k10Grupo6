with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(2375, 2435):
    print(f"{i+1}: {lines[i]}", end="")
