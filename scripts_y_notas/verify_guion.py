with open('guion_defensa_tpi.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(min(50, len(lines))):
    print(f"{i+1}: {lines[i]}", end='')
