with open("scripts_y_notas/generate_v8_deck.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("=== SLIDE 5 & 6 (LINES 1640-1750) ===")
for i in range(1639, min(1750, len(lines))):
    print(f"{i+1}: {lines[i]}", end="")
